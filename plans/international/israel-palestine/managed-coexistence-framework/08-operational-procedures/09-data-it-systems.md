# Data and IT Systems Architecture

**Parent Document:** [00-introduction.md](../00-introduction.md)

**Phase:** All Phases

**Status:** Final Draft

---

## Purpose

Data and IT Systems Architecture defines MCF's **information infrastructure**—the databases, networks, security systems, and privacy protections that enable MCF institutions to operate.

MCF relies heavily on verifiable records: CMS enrollment, incident documentation, credential portability, arbitration outcomes. Without robust IT systems, MCF cannot deliver its core functions. This document establishes principles and requirements for MCF data infrastructure.

---

## Design Principles

### 1. Distributed Trust Architecture

No single party controls MCF data systems. Data integrity depends on multi-party verification, not trust in any one institution.

**What This Means:**

- Critical databases have multi-party write access
- Verification requires cross-institutional confirmation
- No single point of control or failure
- Audit trails visible to all guarantors

### 2. Privacy by Design

MCF collects only necessary data and implements privacy protections from architecture level, not as afterthought.

**What This Means:**

- Minimal data collection principle
- Purpose limitation (data used only for stated purpose)
- Data retention limits
- Privacy impact assessments required

### 3. Interoperability Without Integration

MCF systems must communicate with Israeli, Palestinian, and international systems without merging into any of them.

**What This Means:**

- Standardized data formats
- API-based communication
- No data migration to external systems
- Clear boundaries between MCF and party systems

### 4. Security as Baseline Assumption

MCF systems will be targeted by hostile actors. Security is designed for adversarial environment, not cooperative one.

**What This Means:**

- Defense-in-depth architecture
- Assume breach mentality
- Continuous monitoring
- Incident response preparation

### 5. Transparency of Process, Protection of Individuals

MCF system operations are transparent; individual participant data is protected.

**What This Means:**

- Published algorithms and decision criteria
- Anonymized aggregate reporting
- Individual data access controls
- Clear consent mechanisms

---

## Core Data Systems

### 1. CMS Registry

**Purpose:** Authoritative record of Civic Membership Status holders.

**Data Elements:**

| Category | Data | Sensitivity |
|----------|------|-------------|
| **Identity** | Name, ID numbers, biometrics | High |
| **Status** | Enrollment date, tier, standing | Medium |
| **Benefits** | Accessed services, credentials | Medium |
| **Conduct** | Violations, warnings, suspensions | High |

**Architecture:**

- Primary database: MCF Secretariat (neutral location)
- Backup: Distributed across guarantor facilities
- Access: Read (parties, guarantors); Write (MCF institutions only)
- Encryption: At rest and in transit; field-level for sensitive data

**Integrity Mechanisms:**

- Multi-signature for status changes
- Tamper-evident audit logs
- Periodic cross-verification with party records
- Cryptographic commitment chains

### 2. Incident Database

**Purpose:** Authoritative record of security incidents, attributions, and responses.

**Data Elements:**

| Category | Data | Sensitivity |
|----------|------|-------------|
| **Incident** | Date, location, type, severity | Medium |
| **Attribution** | Finding, confidence, evidence | High |
| **Response** | Actions taken, outcomes | Medium |
| **Patterns** | Trend analysis, actor profiles | High |

**Architecture:**

- Primary: JSVC/UVB systems
- Access: Tiered by classification level
- Retention: Indefinite for accountability; access restrictions over time
- Separation: Operational data vs. analytical products

**Integrity Mechanisms:**

- Evidence chain of custody
- Multiple source verification
- Time-stamped immutable records
- External audit access

### 3. Credential Database

**Purpose:** Record of professional and educational credentials for portability.

**Data Elements:**

| Category | Data | Sensitivity |
|----------|------|-------------|
| **Credentials** | Qualifications, certifications, licenses | Medium |
| **Verification** | Issuing authority, verification status | Low |
| **Mapping** | Cross-system equivalencies | Low |
| **Usage** | Access requests, employer queries | Medium |

**Architecture:**

- Federated model: MCF maintains index; credentials held by issuing authorities
- Verification: Real-time query to issuing authority when possible
- Caching: Limited caching with freshness requirements
- Portability: Standardized credential formats (aligned with international standards)

### 4. Arbitration Records

**Purpose:** Record of commercial court cases, decisions, and enforcement.

**Data Elements:**

| Category | Data | Sensitivity |
|----------|------|-------------|
| **Case files** | Filings, evidence, proceedings | High |
| **Decisions** | Judgments, reasoning, remedies | Medium (public redacted) |
| **Enforcement** | Compliance, execution status | Medium |
| **Precedent** | Searchable legal database | Low (public) |

**Architecture:**

- Case management system: Arbitration Courts
- Publication: Redacted decisions published
- Access: Parties to case; aggregated to public
- Retention: Permanent for legal precedent

### 5. PCC Operations Data

**Purpose:** Real-time and historical data on Protected Civic Corridor operations.

**Data Elements:**

| Category | Data | Sensitivity |
|----------|------|-------------|
| **Status** | Corridor operational state | Low |
| **Traffic** | Movement volumes, timing | Medium |
| **Incidents** | Disruptions, causes, responses | Medium |
| **Maintenance** | Scheduled work, repairs | Low |

**Architecture:**

- Real-time: PCC Directorate operational systems
- Historical: Aggregated for analysis
- Public: Operational status dashboard
- Restricted: Individual movement data

---

## Privacy Framework

### 1. Data Classification

| Level | Description | Access | Examples |
|-------|-------------|--------|----------|
| **Public** | Freely available | Anyone | Aggregate statistics, published decisions |
| **Internal** | MCF operational | MCF personnel | Operational procedures, system status |
| **Confidential** | Protected access | Need-to-know | Individual case files, investigation data |
| **Restricted** | Highest protection | Named individuals | Biometrics, witness identities, intelligence |

### 2. Consent Framework

**CMS Enrollment Consent:**

- Clear explanation of data collection
- Specific purposes stated
- Opt-in for non-essential collection
- Right to access own data
- Right to correction
- Withdrawal process (with limitations)

**Consent Limitations:**

- Cannot consent away minimum protections
- Cannot consent to data use that undermines MCF
- Consent does not override legal requirements
- Withdrawal doesn't erase accountability records

### 3. Data Subject Rights

**Rights Available:**

| Right | Scope | Limitations |
|-------|-------|-------------|
| **Access** | View own data | Redactions for security |
| **Correction** | Fix errors | Verified facts only |
| **Portability** | Export own data | Standard formats |
| **Deletion** | Remove non-essential data | Accountability records exempt |
| **Objection** | Contest processing | Due process required |

**Process:**

- Request to MCF Data Protection Office
- 30-day response requirement
- Appeal to Review Panel if denied
- Guarantor oversight of systematic issues

### 4. Cross-Border Data Transfers

**Principles:**

- MCF data remains under MCF governance
- Transfers to parties only for operational necessity
- No bulk transfers to external systems
- Adequacy assessment for any transfer destination

**Safeguards:**

- Data processing agreements
- Purpose limitation clauses
- Security requirements
- Audit rights
- Breach notification requirements

---

## Cybersecurity Architecture

### 1. Threat Model

**Primary Threats:**

| Threat Actor | Capabilities | Objectives |
|--------------|--------------|------------|
| **State actors** | Advanced persistent threats | Intelligence gathering; disruption; manipulation |
| **Proxy groups** | Targeted attacks | Undermining MCF credibility; identity theft |
| **Criminal groups** | Financial motivation | Fraud; extortion; data theft |
| **Insiders** | Privileged access | Data leakage; sabotage; corruption |

**Attack Surfaces:**

- Network infrastructure
- Application vulnerabilities
- Personnel (social engineering)
- Supply chain
- Physical facilities

### 2. Defense Architecture

**Network Security:**

| Layer | Controls |
|-------|----------|
| **Perimeter** | Firewalls, IDS/IPS, DDoS protection |
| **Network** | Segmentation, encryption, monitoring |
| **Host** | Endpoint protection, hardening, logging |
| **Application** | Secure development, WAF, input validation |
| **Data** | Encryption, access controls, DLP |

**Identity and Access:**

- Multi-factor authentication required
- Role-based access control
- Privileged access management
- Regular access reviews
- Separation of duties

**Monitoring:**

- Security Operations Center (SOC)
- 24/7 monitoring capability
- Automated threat detection
- Incident response procedures
- Threat intelligence integration

### 3. Incident Response

**Classification:**

| Severity | Criteria | Response Time |
|----------|----------|---------------|
| **Critical** | Active breach; data exfiltration; system compromise | Immediate |
| **High** | Attempted breach; vulnerability exploitation | < 4 hours |
| **Medium** | Suspicious activity; policy violation | < 24 hours |
| **Low** | Minor anomaly; process deviation | < 72 hours |

**Response Process:**

1. Detection and alerting
2. Initial assessment
3. Containment
4. Eradication
5. Recovery
6. Lessons learned

**Communication:**

- Internal: MCF leadership, affected institutions
- External: Guarantors (for significant incidents)
- Public: If individual data affected
- Regulatory: Per legal requirements

### 4. Resilience and Recovery

**Business Continuity:**

- Redundant systems in geographically separated locations
- Automated failover for critical systems
- Manual procedures for system outages
- Regular disaster recovery testing

**Backup Strategy:**

- Real-time replication for critical databases
- Daily encrypted backups
- Off-site backup storage (guarantor facilities)
- Regular restore testing

**Recovery Objectives:**

| System | RTO | RPO |
|--------|-----|-----|
| CMS Registry | 4 hours | 15 minutes |
| Incident Database | 4 hours | 1 hour |
| Arbitration | 24 hours | 4 hours |
| PCC Operations | 1 hour | Real-time |

---

## Interoperability Standards

### 1. Data Exchange Formats

**Adopted Standards:**

| Domain | Standard | Purpose |
|--------|----------|---------|
| **Identity** | ISO/IEC 24760 (Identity Management) | Identity data structure |
| **Credentials** | W3C Verifiable Credentials | Credential portability |
| **Documents** | PDF/A, XML | Document preservation |
| **Geographic** | GeoJSON, WKT | Location data |
| **Time** | ISO 8601 | Date/time representation |

**MCF-Specific Extensions:**

- CMS status schema
- Incident classification taxonomy
- Credential mapping specifications
- PCC operational status format

### 2. API Architecture

**Design Principles:**

- RESTful API design
- OAuth 2.0 / OpenID Connect authentication
- Rate limiting and throttling
- Versioning for backward compatibility
- Comprehensive documentation

**API Categories:**

| Category | Access | Purpose |
|----------|--------|---------|
| **Public** | Open | Aggregate data, PCC status, published decisions |
| **Partner** | Authenticated parties | Verification queries, credential checks |
| **Internal** | MCF institutions | Full operational access |
| **Administrative** | MCF IT staff | System management |

### 3. Integration Patterns

**With Israeli Systems:**

- Credential verification queries
- Employment permit coordination
- Border crossing data (limited)
- Security incident notification

**With Palestinian Authority Systems:**

- Identity verification
- Credential verification
- Service coordination
- Incident notification

**With Guarantor Systems:**

- Monitoring data feeds
- Audit access
- Backup synchronization
- Incident escalation

**Integration Constraints:**

- No bulk data exports
- No real-time person tracking
- No intelligence sharing beyond verification
- All integrations logged and auditable

---

## Infrastructure Requirements

### 1. Physical Infrastructure

**Primary Data Center:**

- Neutral location (not in Israeli or Palestinian territory)
- Guarantor-provided facility (e.g., Jordan, Cyprus, or international zone)
- Tier III+ availability
- Physical security controls
- Environmental controls

**Secondary Sites:**

- Geographically separated backup facility
- Distributed presence in operational areas
- Mobile/deployable systems for field operations

### 2. Network Infrastructure

**Connectivity:**

- Multiple ISP connections for redundancy
- Encrypted links between sites
- Dedicated circuits for critical operations
- Satellite backup for emergency communications

**Topology:**

- Segmented networks by function
- DMZ for external-facing services
- Internal network isolation
- Out-of-band management network

### 3. Cloud and Outsourcing

**Principles:**

- Critical systems on-premises or in MCF-controlled facilities
- Cloud services only for non-sensitive functions
- No public cloud for CMS or incident data
- Guarantor cloud services acceptable with controls

**Acceptable Cloud Use:**

- Public-facing websites
- Collaboration tools (non-sensitive)
- Development and testing environments
- Disaster recovery (encrypted)

**Prohibited:**

- CMS registry storage
- Incident database storage
- Biometric data processing
- Arbitration case files

---

## Governance and Oversight

### 1. Data Governance Structure

**MCF Data Protection Office:**

- Independent within MCF Secretariat
- Reports to Confederal Council
- Authority over data policy
- Investigation powers

**Responsibilities:**

- Policy development and maintenance
- Privacy impact assessments
- Data subject request processing
- Incident investigation
- Training and awareness

### 2. Oversight Mechanisms

**Internal:**

- Regular security audits
- Privacy compliance reviews
- Access log analysis
- Policy compliance monitoring

**External:**

- Annual third-party security assessment
- Guarantor audit rights
- Data protection authority (if established) oversight
- Public transparency reports

### 3. Accountability

**Violations:**

| Violation Type | Accountability |
|----------------|----------------|
| **Individual misconduct** | Disciplinary action; potential criminal referral |
| **Institutional failure** | Leadership accountability; remediation requirement |
| **Systemic issue** | Policy revision; structural changes |

**Enforcement:**

- MCF internal processes
- Guarantor attention for significant issues
- External legal action where applicable

---

## Implementation Roadmap

### Phase 0: Foundation

**Priority Systems:**

- JSVC incident database
- PCC operations monitoring
- Basic communication systems
- Security infrastructure

**Governance:**

- Initial data policies
- Security procedures
- Basic privacy protections

### Phase 1: CMS Infrastructure

**Priority Systems:**

- CMS registry
- Credential database
- Arbitration case management
- Enhanced monitoring

**Governance:**

- Full privacy framework
- Data Protection Office establishment
- External audit program

### Phase 2+: Expansion

**Priority Systems:**

- SAZ-specific systems
- Enhanced analytics
- Advanced interoperability
- Public services expansion

**Governance:**

- Mature governance processes
- Continuous improvement
- International standards alignment

---

## Risk Management

### 1. Data-Related Risks

| Risk | Likelihood | Impact | Mitigation |
|------|------------|--------|------------|
| **Data breach** | Medium | High | Defense-in-depth; monitoring; response planning |
| **System unavailability** | Medium | High | Redundancy; DR planning; manual procedures |
| **Data integrity compromise** | Low | Critical | Multi-party verification; audit trails |
| **Privacy violation** | Medium | Medium | Privacy by design; training; oversight |
| **Insider threat** | Low | High | Access controls; monitoring; vetting |

### 2. Operational Risks

| Risk | Likelihood | Impact | Mitigation |
|------|------------|--------|------------|
| **Technology obsolescence** | Medium | Medium | Regular updates; standards alignment |
| **Vendor dependency** | Medium | Medium | Multi-vendor strategy; open standards |
| **Skills shortage** | High | Medium | Training; international recruitment |
| **Budget constraints** | Medium | Medium | Prioritization; guarantor funding |

### 3. Political Risks

| Risk | Likelihood | Impact | Mitigation |
|------|------------|--------|------------|
| **Infrastructure targeting** | High | High | Distributed architecture; protection |
| **Access denial** | Medium | High | Multiple access routes; international hosting |
| **Data weaponization** | Medium | High | Privacy protections; access controls |

---

## References

- [MCF Introduction](../00-introduction.md)
- [JSVC Charter](../01-phase-0-institutions/02-jsvc-charter.md)
- [CMS Framework](../02-phase-1-civic-membership/01-cms-framework.md)
- [Communication Protocols](07-communication-protocols.md)
- [Spoiler Response](04-spoiler-response.md)
