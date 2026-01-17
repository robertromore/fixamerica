# Appendix X: Technology Specifications

---

## Overview

This appendix provides detailed technical specifications for ICS information technology systems, including the core database, biometric systems, mobile applications, security requirements, and integration standards. These specifications guide procurement, development, and implementation.

---

## System Architecture

### High-Level Architecture

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                          ICS ENTERPRISE ARCHITECTURE                         │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐    │
│  │   Web Apps   │  │ Mobile Apps  │  │   Kiosks     │  │  Partner API │    │
│  └──────┬───────┘  └──────┬───────┘  └──────┬───────┘  └──────┬───────┘    │
│         │                 │                 │                 │             │
│         └─────────────────┼─────────────────┼─────────────────┘             │
│                           │                 │                               │
│                    ┌──────▼─────────────────▼──────┐                        │
│                    │        API GATEWAY            │                        │
│                    │   (Authentication, Routing)   │                        │
│                    └──────────────┬────────────────┘                        │
│                                   │                                         │
│         ┌─────────────────────────┼─────────────────────────┐               │
│         │                         │                         │               │
│  ┌──────▼──────┐  ┌───────────────▼───────────────┐  ┌──────▼──────┐       │
│  │   Case      │  │       Core Services           │  │  Reporting  │       │
│  │ Management  │  │  (Business Logic Layer)       │  │  Analytics  │       │
│  └──────┬──────┘  └───────────────┬───────────────┘  └──────┬──────┘       │
│         │                         │                         │               │
│         └─────────────────────────┼─────────────────────────┘               │
│                                   │                                         │
│                    ┌──────────────▼──────────────┐                          │
│                    │     DATA LAYER              │                          │
│                    │  ┌─────────┐ ┌──────────┐   │                          │
│                    │  │Postgres │ │Biometric │   │                          │
│                    │  │   DB    │ │  Store   │   │                          │
│                    │  └─────────┘ └──────────┘   │                          │
│                    └─────────────────────────────┘                          │
│                                                                              │
│  EXTERNAL INTEGRATIONS                                                       │
│  ┌──────────┐ ┌──────────┐ ┌──────────┐ ┌──────────┐ ┌──────────┐          │
│  │ E-Verify │ │   FBI    │ │   SSA    │ │   IRS    │ │  DHS     │          │
│  └──────────┘ └──────────┘ └──────────┘ └──────────┘ └──────────┘          │
│                                                                              │
└─────────────────────────────────────────────────────────────────────────────┘
```

### Core Components

| Component | Technology | Purpose |
|-----------|------------|---------|
| **Database** | PostgreSQL 15+ | Primary data store |
| **Biometric store** | Dedicated AFIS-compatible | Fingerprint/facial storage |
| **Application servers** | Kubernetes clusters | Service hosting |
| **API gateway** | Kong or AWS API Gateway | Traffic management |
| **Message queue** | Apache Kafka | Async processing |
| **Cache** | Redis | Performance |
| **Document storage** | S3-compatible | Document management |
| **Search** | Elasticsearch | Full-text search |

---

## Core Database Schema

### Participant Tables

```sql
-- Core participant record
CREATE TABLE participants (
    participant_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    alien_number VARCHAR(10) UNIQUE NOT NULL,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    status VARCHAR(20) NOT NULL CHECK (status IN
        ('pending', 'active', 'suspended', 'revoked', 'departed')),
    current_tier VARCHAR(1) CHECK (current_tier IN ('A', 'B', 'C')),
    track VARCHAR(20) CHECK (track IN ('standard', 'legacy', 'asylum')),
    registration_date DATE,
    clp_expiration DATE,
    CONSTRAINT valid_dates CHECK (clp_expiration > registration_date)
);

-- Biographical data
CREATE TABLE participant_bio (
    participant_id UUID PRIMARY KEY REFERENCES participants(participant_id),
    family_name VARCHAR(100) NOT NULL,
    given_names VARCHAR(200) NOT NULL,
    date_of_birth DATE NOT NULL,
    country_of_birth VARCHAR(3) NOT NULL, -- ISO 3166-1 alpha-3
    country_of_citizenship VARCHAR(3) NOT NULL,
    gender VARCHAR(1) CHECK (gender IN ('M', 'F', 'X')),
    native_language VARCHAR(3), -- ISO 639-3
    CONSTRAINT valid_dob CHECK (date_of_birth < CURRENT_DATE)
);

-- Contact information
CREATE TABLE participant_contact (
    contact_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    participant_id UUID NOT NULL REFERENCES participants(participant_id),
    address_line1 VARCHAR(200),
    address_line2 VARCHAR(200),
    city VARCHAR(100),
    state VARCHAR(2),
    zip_code VARCHAR(10),
    phone VARCHAR(20),
    email VARCHAR(200),
    is_current BOOLEAN DEFAULT TRUE,
    effective_date DATE NOT NULL,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

-- Status history
CREATE TABLE status_history (
    history_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    participant_id UUID NOT NULL REFERENCES participants(participant_id),
    previous_status VARCHAR(20),
    new_status VARCHAR(20) NOT NULL,
    previous_tier VARCHAR(1),
    new_tier VARCHAR(1),
    change_reason VARCHAR(500),
    changed_by UUID NOT NULL, -- References staff table
    changed_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);
```

### Geographic Assignment Tables

```sql
-- Hub and corridor cities
CREATE TABLE cities (
    city_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    city_name VARCHAR(100) NOT NULL,
    state VARCHAR(2) NOT NULL,
    city_type VARCHAR(20) CHECK (city_type IN ('hub', 'corridor')),
    corridor_region VARCHAR(50),
    capacity_tier_a INTEGER,
    capacity_tier_b INTEGER,
    current_population_a INTEGER DEFAULT 0,
    current_population_b INTEGER DEFAULT 0,
    is_active BOOLEAN DEFAULT TRUE,
    joined_date DATE,
    UNIQUE(city_name, state)
);

-- Participant assignments
CREATE TABLE geographic_assignments (
    assignment_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    participant_id UUID NOT NULL REFERENCES participants(participant_id),
    city_id UUID NOT NULL REFERENCES cities(city_id),
    assignment_tier VARCHAR(1) NOT NULL,
    assigned_date DATE NOT NULL,
    end_date DATE,
    assignment_reason VARCHAR(200),
    is_current BOOLEAN DEFAULT TRUE,
    CONSTRAINT no_overlap EXCLUDE USING gist (
        participant_id WITH =,
        daterange(assigned_date, end_date, '[]') WITH &&
    )
);
```

### Employment Tables

```sql
-- Registered employers
CREATE TABLE employers (
    employer_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    ein VARCHAR(10) UNIQUE NOT NULL,
    company_name VARCHAR(200) NOT NULL,
    dba_name VARCHAR(200),
    registration_status VARCHAR(20) DEFAULT 'pending',
    registration_date DATE,
    expiration_date DATE,
    industry_code VARCHAR(6), -- NAICS
    primary_contact_name VARCHAR(200),
    primary_contact_email VARCHAR(200),
    primary_contact_phone VARCHAR(20)
);

-- Employment records
CREATE TABLE employment (
    employment_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    participant_id UUID NOT NULL REFERENCES participants(participant_id),
    employer_id UUID NOT NULL REFERENCES employers(employer_id),
    job_title VARCHAR(200),
    occupation_code VARCHAR(10), -- SOC
    start_date DATE NOT NULL,
    end_date DATE,
    hourly_wage DECIMAL(10,2),
    hours_per_week INTEGER,
    is_current BOOLEAN DEFAULT TRUE,
    verified_by_employer BOOLEAN DEFAULT FALSE,
    verified_date DATE
);
```

### Language Assessment Tables

```sql
-- Language assessments
CREATE TABLE language_assessments (
    assessment_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    participant_id UUID NOT NULL REFERENCES participants(participant_id),
    assessment_date DATE NOT NULL,
    assessment_type VARCHAR(50), -- 'CASAS', 'TOEFL', etc.
    listening_score VARCHAR(5),
    reading_score VARCHAR(5),
    speaking_score VARCHAR(5),
    writing_score VARCHAR(5),
    overall_cefr VARCHAR(2) CHECK (overall_cefr IN
        ('A1', 'A2', 'B1', 'B2', 'C1', 'C2')),
    assessor_id UUID,
    notes TEXT
);
```

---

## Biometric System

### Biometric Data Types

| Type | Standard | Use |
|------|----------|-----|
| **Fingerprints** | FBI EBTS | Identity verification; background check |
| **Facial image** | ISO/IEC 19794-5 | Photo ID; facial recognition |
| **Iris** | ISO/IEC 19794-6 | Optional secondary biometric |

### Fingerprint Specifications

| Parameter | Specification |
|-----------|---------------|
| **Capture method** | Livescan (optical or capacitive) |
| **Resolution** | Minimum 500 ppi |
| **Fingers captured** | All 10 fingers + slaps |
| **Image format** | WSQ compression |
| **Template format** | INCITS 378 minutiae |
| **Quality threshold** | NFIQ 1-3 (good to excellent) |

### Facial Image Specifications

| Parameter | Specification |
|-----------|---------------|
| **Resolution** | Minimum 480x600 pixels |
| **Format** | JPEG2000 or PNG |
| **Pose** | Frontal, neutral expression |
| **Lighting** | Even, no shadows |
| **Background** | Plain white or light gray |
| **Template** | ISO/IEC 19794-5 compliant |

### Biometric Matching

| Match Type | Threshold | Use Case |
|------------|-----------|----------|
| **1:1 verification** | FAR < 0.01% | Status verification |
| **1:N identification** | FNIR < 2% at FAR 0.1% | Duplicate detection |
| **Watchlist** | Per FBI standards | Security screening |

### Integration with FBI

| System | Purpose | Protocol |
|--------|---------|----------|
| **NGI** | Criminal history check | EBTS submission |
| **IDENT** | Immigration history | DHS interface |
| **TECS** | Border crossing | CBP integration |

---

## Mobile Application

### Participant App (ICS Mobile)

**Platforms:** iOS 14+, Android 10+

**Features:**

| Feature | Description |
|---------|-------------|
| **Status dashboard** | Current tier, expiration, compliance |
| **Check-in** | Location verification (if required) |
| **Appointments** | Schedule and manage appointments |
| **Documents** | Digital CLP card; upload documents |
| **Messages** | Secure messaging with case manager |
| **Services** | Find nearby services; make referrals |
| **Progress** | Track advancement requirements |
| **Notifications** | Push alerts for deadlines, updates |

**Technical Specifications:**

| Component | Specification |
|-----------|---------------|
| **Framework** | React Native (cross-platform) |
| **Authentication** | Biometric + PIN |
| **Data storage** | Encrypted local storage |
| **Offline mode** | Limited functionality; sync on connect |
| **Languages** | 10+ languages (user selectable) |
| **Accessibility** | WCAG 2.1 AA compliant |

**Security Features:**

| Feature | Implementation |
|---------|----------------|
| **Authentication** | OAuth 2.0 + PKCE |
| **Session management** | JWT with short expiry |
| **Certificate pinning** | Prevent MITM |
| **Jailbreak detection** | Block on compromised devices |
| **Data encryption** | AES-256 at rest |
| **Secure enclave** | Biometric key storage |

### Case Manager App (ICS Staff)

**Platforms:** iOS, Android (tablet-optimized)

**Features:**

| Feature | Description |
|---------|-------------|
| **Caseload** | View and manage assigned cases |
| **Search** | Find participants; employers |
| **Intake** | Mobile intake processing |
| **Biometrics** | Capture with approved devices |
| **Documents** | Scan and upload |
| **Notes** | Case notes with voice input |
| **Offline** | Full offline capability; sync later |

---

## Web Applications

### Participant Portal

**URL:** portal.ics.gov

**Features:**

| Feature | Description |
|---------|-------------|
| **Account management** | Profile; password; settings |
| **Applications** | File applications; upload documents |
| **Status tracking** | Case status; processing times |
| **Appointments** | Online scheduling |
| **Forms** | Digital form completion |
| **Payments** | Fee payment (if applicable) |

**Technical Specifications:**

| Component | Specification |
|-----------|---------------|
| **Framework** | React 18+ |
| **State management** | Redux Toolkit |
| **UI components** | USWDS (US Web Design System) |
| **Accessibility** | Section 508; WCAG 2.1 AA |
| **Languages** | 20+ languages |
| **Browser support** | Chrome, Firefox, Safari, Edge (latest 2 versions) |

### Staff Portal

**URL:** staff.ics.gov (internal)

**Features:**

| Feature | Description |
|---------|-------------|
| **Case management** | Full case access; workflow |
| **Intake** | Registration; biometrics |
| **Adjudication** | Review; decision; notice |
| **Reporting** | Operational reports |
| **Administration** | User management; configuration |

### Employer Portal

**URL:** employer.ics.gov

**Features:**

| Feature | Description |
|---------|-------------|
| **Registration** | Employer registration application |
| **Verification** | Employee status verification |
| **Reporting** | Employment verification; compliance |
| **Compliance** | View audit status; respond to inquiries |

---

## Integration Specifications

### E-Verify Integration

| Element | Specification |
|---------|---------------|
| **Protocol** | REST API over HTTPS |
| **Authentication** | OAuth 2.0 client credentials |
| **Data format** | JSON |
| **Transactions** | Initial verification; photo match; reverify |
| **Response time** | <3 seconds for initial; <24 hours for TNC |

### SSA Integration

| Element | Specification |
|---------|---------------|
| **Protocol** | SOAP/XML (legacy) |
| **Authentication** | PKI certificates |
| **Transactions** | SSN verification; enumeration |
| **Security** | VPN tunnel required |

### FBI/DHS Integration

| Element | Specification |
|---------|---------------|
| **Protocol** | NIST EBTS for biometrics |
| **Transport** | LEO-restricted network |
| **Transactions** | Criminal history; immigration history |
| **Response time** | 24-72 hours |

### API Standards

| Standard | Specification |
|----------|---------------|
| **Protocol** | REST over HTTPS |
| **Authentication** | OAuth 2.0 |
| **Data format** | JSON (primary); XML (legacy) |
| **Versioning** | URL path versioning (v1, v2) |
| **Rate limiting** | Per-client quotas |
| **Documentation** | OpenAPI 3.0 |

---

## Security Requirements

### Authentication

| User Type | Method |
|-----------|--------|
| **Participants** | Username/password + MFA |
| **Staff** | PIV/CAC card + PIN |
| **Employers** | Username/password + MFA |
| **Administrators** | PIV + biometric |

### Authorization

| Model | Implementation |
|-------|----------------|
| **RBAC** | Role-based access control |
| **ABAC** | Attribute-based for sensitive operations |
| **Least privilege** | Minimum necessary access |
| **Separation of duties** | Dual control for critical actions |

### Data Protection

| Protection | Implementation |
|------------|----------------|
| **Encryption in transit** | TLS 1.3 |
| **Encryption at rest** | AES-256 |
| **Key management** | HSM-backed; FIPS 140-2 Level 3 |
| **Data masking** | PII masked in logs; reports |
| **Tokenization** | SSN; payment data |

### Compliance

| Standard | Requirement |
|----------|-------------|
| **FedRAMP** | High baseline |
| **FISMA** | Moderate+ impact level |
| **Privacy Act** | System of Records Notice |
| **CJIS** | For criminal history access |
| **PCI-DSS** | For payment processing |

### Security Monitoring

| Capability | Implementation |
|------------|----------------|
| **SIEM** | Centralized log aggregation; alerting |
| **IDS/IPS** | Network intrusion detection |
| **DLP** | Data loss prevention |
| **Vulnerability scanning** | Weekly automated scans |
| **Penetration testing** | Annual third-party |

---

## Infrastructure

### Cloud Architecture

| Component | Specification |
|-----------|---------------|
| **Primary cloud** | FedRAMP-authorized (AWS GovCloud, Azure Gov) |
| **Multi-region** | Primary + DR region |
| **CDN** | For static assets; DDoS protection |
| **Load balancing** | Application load balancers |
| **Auto-scaling** | Based on demand |

### Availability Requirements

| Metric | Target |
|--------|--------|
| **Availability** | 99.9% (8.76 hours downtime/year) |
| **RTO** | 4 hours |
| **RPO** | 1 hour |
| **Maintenance windows** | Scheduled; communicated |

### Disaster Recovery

| Element | Specification |
|---------|---------------|
| **Backup frequency** | Continuous replication; daily snapshots |
| **Backup retention** | 30 days online; 7 years archive |
| **DR testing** | Quarterly failover tests |
| **Geographic separation** | Primary and DR in different regions |

---

## Performance Requirements

### Response Time

| Transaction | Target |
|-------------|--------|
| **Page load** | <2 seconds |
| **API response** | <500ms (p95) |
| **Search** | <1 second |
| **Report generation** | <30 seconds |
| **Batch processing** | Overnight completion |

### Capacity

| Metric | Requirement |
|--------|-------------|
| **Concurrent users** | 50,000+ |
| **Transactions/day** | 1 million+ |
| **Data storage** | 10+ PB (including biometrics) |
| **Document storage** | 100+ TB |

### Scalability

| Dimension | Approach |
|-----------|----------|
| **Horizontal** | Stateless services; container orchestration |
| **Vertical** | Database scaling; read replicas |
| **Geographic** | Multi-region deployment |
| **Temporal** | Queue-based load leveling |

---

## Data Standards

### Code Tables

| Domain | Standard |
|--------|----------|
| **Countries** | ISO 3166-1 alpha-3 |
| **Languages** | ISO 639-3 |
| **Currencies** | ISO 4217 |
| **Occupations** | SOC (Standard Occupational Classification) |
| **Industries** | NAICS |
| **Geography** | FIPS codes; Census TIGER |

### Date/Time

| Element | Format |
|---------|--------|
| **Dates** | ISO 8601 (YYYY-MM-DD) |
| **Timestamps** | ISO 8601 with timezone |
| **Storage** | UTC |
| **Display** | User's local timezone |

### Document Formats

| Document Type | Format |
|---------------|--------|
| **Forms** | PDF/A for archive; fillable PDF |
| **Images** | JPEG, PNG, PDF |
| **Data export** | JSON, CSV, XML |
| **Reports** | PDF, Excel |

---

## Testing Requirements

### Test Types

| Type | Coverage |
|------|----------|
| **Unit tests** | >80% code coverage |
| **Integration tests** | All API endpoints |
| **E2E tests** | Critical user journeys |
| **Performance tests** | Load; stress; endurance |
| **Security tests** | SAST; DAST; penetration |
| **Accessibility tests** | Automated + manual |

### Environments

| Environment | Purpose |
|-------------|---------|
| **Development** | Feature development |
| **Test** | QA testing |
| **Staging** | Pre-production validation |
| **Production** | Live system |
| **DR** | Disaster recovery |

---

## Related Documents

- [Appendix J: Data Architecture](J-data-architecture.md) - Data flows
- [Metrics and Evaluation](../29-metrics-evaluation.md) - Reporting requirements
- [Appendix Y: Metrics Dashboard](Y-metrics-dashboard.md) - Dashboard specs

---

## Document Navigation

- Previous: [Appendix W: Bilateral Templates](W-bilateral-templates.md)
- Next: [Appendix Y: Metrics Dashboard](Y-metrics-dashboard.md)
