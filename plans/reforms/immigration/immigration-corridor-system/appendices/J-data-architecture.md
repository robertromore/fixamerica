# Appendix J: Data Architecture

---

## Overview

This appendix provides technical specifications for ICS information systems, data flows, interoperability standards, privacy requirements, and system security.

---

## System Components

### Core Systems

| System | Owner | Function |
|--------|-------|----------|
| **ICS Central Registry** | DHS/USCIS | Participant records, status tracking |
| **Placement Engine** | DHS/HUD | Algorithm-based city matching |
| **Benefits Portal** | Treasury/SSA | RID payments, benefit coordination |
| **Employer Portal** | DOL | Registration, compliance, tax credits |
| **Education Tracker** | ED | ESL enrollment, progress, credentials |
| **Health Information System** | HHS | Screening, clinic utilization |
| **Oversight Dashboard** | IIOO | Public metrics, audit tools |

### Data Exchanges

| Exchange | Systems Connected | Data Type |
|----------|-------------------|-----------|
| **Status Verification** | USCIS ↔ E-Verify | Work authorization |
| **Benefit Eligibility** | ICS ↔ SSA/HHS | Benefit determinations |
| **Capacity Data** | Cities ↔ Placement Engine | Housing, school, healthcare capacity |
| **Progress Reporting** | Providers ↔ ICS | Language, employment benchmarks |
| **Enforcement** | ICS ↔ ICE | Compliance, removal triggers |

---

## Participant Data Model

### Core Record

| Field | Type | Purpose |
|-------|------|---------|
| **ICS ID** | Unique identifier | Primary key across systems |
| **Biometrics** | Fingerprint, photo | Identity verification |
| **Status** | Tier A/B/C | Current placement tier |
| **Location** | City code | Current authorized location |
| **Entry date** | Date | Start of ICS participation |
| **Tier dates** | Date array | Tier advancement history |

### Demographic Data

| Field | Type | Retention |
|-------|------|-----------|
| **Name** | String | Permanent |
| **DOB** | Date | Permanent |
| **Country of origin** | Code | Permanent |
| **Language** | Code list | Updateable |
| **Family unit ID** | Reference | While applicable |

### Benchmark Data

| Field | Type | Source |
|-------|------|--------|
| **Language level** | CEFR code | Assessment system |
| **Employment status** | Boolean + details | Employer/self-report |
| **Training enrollment** | Boolean + details | Provider report |
| **Civic orientation** | Completion flag | Provider report |
| **Compliance status** | Flag | Enforcement system |

---

## Placement Algorithm

### Input Data

| Source | Data |
|--------|------|
| **Participant** | Family size, skills, language, preferences |
| **Cities** | Vacancy rates, school capacity, clinic capacity, job openings |
| **Federal** | Capacity limits, surge status |

### Algorithm Logic

```
FOR each unplaced participant:
  1. Filter cities by capacity (exclude at-limit cities)
  2. Score cities by:
     - Family connections (weighted 30%)
     - Language/cultural match (weighted 20%)
     - Employment fit (weighted 25%)
     - Capacity headroom (weighted 15%)
     - Participant preference (weighted 10%)
  3. Select highest-scoring city meeting all constraints
  4. Reserve capacity; create placement record
  5. If no city available: queue for next cycle
```

### Fairness Constraints

| Constraint | Implementation |
|------------|----------------|
| **No national origin quotas** | Algorithm cannot use nationality as filter |
| **Disparate impact monitoring** | Quarterly analysis of placement by demographics |
| **Audit trail** | All placement decisions logged with factors |
| **Override capability** | Manual override with documented justification |

---

## Interoperability Standards

### Data Exchange Formats

| Standard | Use |
|----------|-----|
| **JSON** | API responses |
| **XML** | Legacy system integration |
| **HL7 FHIR** | Healthcare data |
| **NIEM** | Justice/law enforcement data |

### API Standards

| Specification | Application |
|---------------|-------------|
| **REST** | Primary API architecture |
| **OAuth 2.0** | Authentication |
| **OpenID Connect** | Identity federation |
| **API versioning** | Backward compatibility |

### Integration Patterns

| Pattern | Use Case |
|---------|----------|
| **Synchronous API** | Status verification, eligibility checks |
| **Asynchronous messaging** | Batch updates, notifications |
| **Event streaming** | Real-time dashboards |
| **File transfer** | Legacy system bulk data |

---

## Privacy and Data Governance

### Data Minimization

| Principle | Implementation |
|-----------|----------------|
| **Collect minimum necessary** | Only fields required for defined purposes |
| **Purpose limitation** | Data used only for stated purposes |
| **Access control** | Role-based access to specific fields |

### Retention Schedule

| Data Category | Retention | Basis |
|---------------|-----------|-------|
| **Core identity** | Permanent | Legal record |
| **Placement history** | 10 years after exit | Audit trail |
| **Benchmark data** | 5 years | Operational need |
| **Healthcare data** | Per HIPAA | Legal requirement |
| **Financial data** | 7 years | IRS requirements |

### Participant Rights

| Right | Implementation |
|-------|----------------|
| **Access** | Self-service portal; request process |
| **Correction** | Dispute process with review |
| **Explanation** | Placement factors disclosed on request |
| **Restriction** | Opt-out of non-essential data uses |

### Sensitive Data Handling

| Category | Protection |
|----------|------------|
| **Asylum claims** | Segregated; limited access |
| **Domestic violence** | Address confidentiality |
| **Medical records** | HIPAA compliance |
| **Minor records** | Enhanced protections |

---

## Security Architecture

### Network Security

| Control | Standard |
|---------|----------|
| **Perimeter** | Firewalls, IDS/IPS |
| **Segmentation** | Separate VLANs by function |
| **Encryption** | TLS 1.3 for transit |
| **VPN** | Required for remote access |

### Data Security

| Control | Standard |
|---------|----------|
| **Encryption at rest** | AES-256 |
| **Key management** | HSM-based |
| **Database security** | Column-level encryption for PII |
| **Backup encryption** | Same standard as production |

### Access Control

| Control | Standard |
|---------|----------|
| **Authentication** | MFA required |
| **Authorization** | Role-based (RBAC) |
| **Privileged access** | PAM solution; just-in-time |
| **Audit logging** | All access logged |

### Incident Response

| Capability | Standard |
|------------|----------|
| **Detection** | SIEM with 24/7 monitoring |
| **Response** | Playbooks for common scenarios |
| **Breach notification** | 72 hours per ICS statute |
| **Recovery** | RPO 1 hour; RTO 4 hours |

---

## System Availability

### Uptime Requirements

| System | Target | Maintenance Window |
|--------|--------|-------------------|
| **Status verification** | 99.9% | Sunday 2-6 AM |
| **Participant portal** | 99.5% | Sunday 2-6 AM |
| **Employer portal** | 99.5% | Sunday 2-6 AM |
| **Public dashboard** | 99.0% | Anytime |

### Disaster Recovery

| Capability | Standard |
|------------|----------|
| **Geographic redundancy** | Active-passive across regions |
| **Failover time** | < 15 minutes |
| **Backup frequency** | Hourly incremental; daily full |
| **DR testing** | Quarterly failover tests |

---

## Reporting and Analytics

### Operational Dashboards

| Dashboard | Users | Refresh |
|-----------|-------|---------|
| **Intake status** | CBP, DHS | Real-time |
| **Placement queue** | HUD, cities | Hourly |
| **Capacity utilization** | All agencies | Daily |
| **Compliance flags** | Enforcement | Real-time |

### Public Dashboard

| Metric | Granularity | Lag |
|--------|-------------|-----|
| **Total participants** | National | Daily |
| **Tier distribution** | By state | Weekly |
| **Advancement rates** | By hub city | Monthly |
| **Program costs** | By category | Quarterly |

### Analytics Capabilities

| Capability | Use |
|------------|-----|
| **Predictive modeling** | Capacity forecasting |
| **Cohort analysis** | Outcome tracking |
| **Anomaly detection** | Fraud identification |
| **Geospatial analysis** | Placement optimization |

---

## Development and Testing

### Environments

| Environment | Purpose |
|-------------|---------|
| **Development** | Feature development |
| **Test** | Integration testing |
| **Staging** | Pre-production validation |
| **Production** | Live operations |

### Testing Requirements

| Test Type | Coverage |
|-----------|----------|
| **Unit tests** | 80%+ code coverage |
| **Integration tests** | All APIs |
| **Performance tests** | Peak load simulation |
| **Security tests** | Penetration testing twice/year |

### Deployment

| Practice | Standard |
|----------|----------|
| **CI/CD** | Automated pipelines |
| **Blue-green deployment** | Zero-downtime releases |
| **Rollback capability** | < 5 minute rollback |
| **Change management** | CAB approval for production |

---

## Related Documents

- [Implementation](../15-implementation.md) - IT system overview
- [Oversight](../12-oversight.md) - Data governance
- [Appendix E: Risk Register](E-risk-register.md) - Data breach risks

---

## Document Navigation

- Previous: [Appendix I: Case Studies](I-case-studies.md)
- Next: [Appendix K: Model Compact](K-model-compact.md)
