# Immigration Corridor System: Housing

---

## Overview

Housing is a critical component of the ICS. The system must place newcomers in safe, affordable housing while preventing concentration that strains communities or creates isolated enclaves.

---

## Housing Placement Algorithm

### Design Goals

| Goal | Description |
|------|-------------|
| **Prevent ghettos** | Disperse placements to avoid ethnic enclaves |
| **Avoid overload** | Respect school, clinic, and infrastructure capacity |
| **Maximize stability** | Reduce moves; support employment continuity |
| **Protect civil rights** | No discrimination; FHA compliance |

### Hard Constraints

| Constraint | Threshold | Rationale |
|------------|-----------|-----------|
| **Per-building cap** | ≤30-40% new arrivals | Prevent building-level concentration |
| **Neighborhood cap** | ≤15-25% over 12 months | Prevent neighborhood-level concentration |
| **School capacity** | Below staffed capacity | Ensure EL services available |
| **Clinic capacity** | Below utilization cap | Ensure healthcare access |
| **Family unity** | Preserved | Constitutional and humanitarian requirement |

Cap bands are set by published criteria (vacancy, school/clinic utilization, transit load). Tighter caps apply in high-stress zones.

### Optimization Objectives

| Objective | Weight |
|-----------|--------|
| **Commute to work/training** | High |
| **School continuity** | High (for families with children) |
| **Medical access** | Medium |
| **Rent stability** | Medium |
| **Transit access** | Medium |

### Governance

| Feature | Description |
|---------|-------------|
| **Human override** | Allowed with documented justification |
| **Appeals** | Guaranteed for all placements |
| **Audit logs** | Mandatory for all decisions |

Mixing is enforced structurally, not culturally. Placement caps are capacity-based and set no demographic targets.

### Algorithmic Fairness Guardrails

| Safeguard | Implementation |
|-----------|----------------|
| **Inputs** | Use only capacity, cost, proximity, and service access variables |
| **Prohibited inputs** | Race, ethnicity, religion, nationality, and proxy features |
| **Fairness checks** | Quarterly disparate-impact audits at building and neighborhood levels |
| **Thresholds** | HUD/DOJ fair-housing impact metrics and variance bands |
| **Explainability** | Placement rationale in plain language at intake and on appeal |
| **Override controls** | Documented justification required; random quarterly reviews |
| **Bias response** | Auto-adjust weights and pause rules if thresholds breached |
| **Civil rights review** | Annual FHA and Equal Protection compliance audit |

---

## Housing Supply and Land-Use Coordination

### Housing Stock Realism

Many hub cities (Buffalo, Cleveland, Detroit, Pittsburgh) have older housing stock with known challenges:

| Challenge | Prevalence | Mitigation Required |
|-----------|------------|---------------------|
| **Lead paint** | 60-80% of pre-1978 housing | Mandatory testing and abatement |
| **Asbestos** | Common in pre-1980 insulation | Inspection and encapsulation/removal |
| **Code violations** | 15-30% of older rental stock | Compliance timeline requirements |
| **Deferred maintenance** | Widespread in low-rent units | Rehabilitation investment |
| **Energy inefficiency** | Common in older buildings | Weatherization coordination |

### Housing Quality Standards

All ICS-eligible housing must meet minimum standards:

| Standard | Requirement | Verification |
|----------|-------------|--------------|
| **Lead-safe certification** | Required for units housing children under 6 | EPA-certified inspection |
| **Habitability code** | Local housing code compliance | Municipal inspection within 90 days |
| **Smoke/CO detectors** | Functional detectors on every level | Landlord certification + spot audit |
| **Heat and hot water** | Reliable service | Utility verification |
| **Pest control** | No active infestation | Inspection protocol |
| **Structural integrity** | No hazardous conditions | Engineering review for flagged units |

### Rehabilitation Investment

| Program | Purpose | Funding |
|---------|---------|---------|
| **Lead Hazard Reduction Grants** | Abatement in designated zones | $500M-1B/year federal |
| **Code Compliance Loans** | Low-interest loans for landlords to meet standards | Revolving fund |
| **Weatherization Plus** | Energy efficiency + health hazard remediation | DOE + HUD coordination |
| **Vacant Property Rehabilitation** | Convert abandoned properties to habitable units | Land bank partnerships |

---

## Landlord Certification Program

### Requirements

Landlords participating in ICS housing must:

- register units with the Corridor Housing Registry
- certify compliance with quality standards
- accept standardized lease terms (no discriminatory provisions)
- participate in annual recertification
- accept direct-deposit rent assistance (if applicable)

### Incentives

| Incentive | Benefit |
|-----------|---------|
| **Guaranteed occupancy pipeline** | Reduced vacancy risk |
| **Rent stabilization** | Predictable tenant flow |
| **Rehabilitation grant eligibility** | Access to improvement funds |
| **Property tax abatement** | In designated zones |

### Enforcement

| Violation | Consequence |
|-----------|-------------|
| **First violation** | Warning; corrective action plan |
| **Repeated violations** | Decertification |
| **Unit fails inspection** | Tenant relocation assistance |
| **Pattern of violations** | Public registry of decertified landlords |

---

## Supply Expansion Levers

| Lever | Mechanism |
|-------|-----------|
| **Federal housing production grants** | For hub and corridor regions |
| **Fast-track permitting** | For conversions of underutilized commercial properties |
| **Zoning incentives** | For missing-middle and mixed-use housing near transit |
| **Adaptive reuse** | Of vacant schools, churches, and office buildings |
| **Land bank partnerships** | For abandoned property transfer |
| **Modular construction pilots** | For rapid deployment |

---

## Housing Slack Monitoring

| Metric | Threshold | Action |
|--------|-----------|--------|
| **Vacancy rate** | Below 5% | Trigger corridor expansion to new cities |
| **Rent growth** | Above 8% annually | Activate anti-speculation measures |
| **Waitlist length** | Above 90 days | Expand placement radius or slow intake |
| **Lead certification backlog** | Above 60 days | Surge inspection capacity |

---

## Anti-Displacement Protections

| Protection | Description |
|------------|-------------|
| **Targeted tenant protections** | In high-pressure zones |
| **Right-to-return provisions** | For displaced residents |
| **Anti-speculation measures** | Tied to RID eligibility |
| **Rent increase caps** | Tied to regional CPI |
| **Just-cause eviction** | Required for certified landlords |
| **Relocation assistance** | For involuntary displacement |

---

## Delivery and Financing

| Mechanism | Application |
|-----------|-------------|
| **Public-private partnerships** | Performance-based milestones |
| **Modular and rapid-build pilots** | With quality safeguards |
| **Infrastructure grants** | Water, transit, and school expansion tied to new units |
| **CDBG priority** | For corridor cities |
| **LIHTC set-asides** | For ICS-designated areas |
| **New Markets Tax Credits** | For commercial-to-residential conversions |

---

## Placement System Procurement and Governance

| Requirement | Description |
|-------------|-------------|
| **Open standards** | For model documentation and auditability |
| **Independent validation** | Before deployment and after major updates |
| **Vendor accountability** | For bias, accuracy, and data security failures |
| **Change-control board** | Public minutes for material model updates |
| **Emergency kill-switch** | Rollback plan for placement failures |

---

## Related Documents

- [Geographic Design](03-geographic-design.md) - Hub and corridor city designations
- [Community Integration](05-community-integration.md) - RID payments and host community strategy
- [Fiscal Architecture](08-fiscal-architecture.md) - Housing program budgets

---

## Document Navigation

- Previous: [Geographic Design](03-geographic-design.md)
- Next: [Community Integration](05-community-integration.md)
