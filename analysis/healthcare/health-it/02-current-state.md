# Health Information Technology: Current State

## The Problem Today

### A Fragmented Digital Landscape

Despite over $36 billion in federal investment through the HITECH Act and subsequent programs, the American healthcare system remains a patchwork of disconnected information systems. While EHR adoption has reached near-universal levels, the promise of seamless information exchange has not materialized. Patients seeking care at different facilities still find their records inaccessible, clinicians spend hours on documentation that serves billing rather than care, and public health authorities struggle to collect basic data during emergencies.

**The Adoption Success That Masked Deeper Failures**

| Metric | 2008 | 2023 | Change |
|--------|------|------|--------|
| Hospital EHR adoption | 9% (basic) | 96% (certified) | +87% |
| Office-based physician EHR | 42% | 89% | +47% |
| Patients accessing portal | 10% | 73% offered | +63% |
| Information exchange capability | Limited | Still limited | Minimal |

The raw numbers suggest success. The reality is that adoption occurred without achieving interoperability, usability, or the clinical benefits that motivated the investment.

## Electronic Health Record Market

### Vendor Concentration

The EHR market has consolidated dramatically, with a handful of vendors controlling most of the market.

**Hospital EHR Market Share (2024)**

| Vendor | Market Share | Notable Clients |
|--------|--------------|-----------------|
| Epic Systems | 38% | Kaiser, Cleveland Clinic, Johns Hopkins |
| Oracle Health (Cerner) | 22% | VA (transitioning), HCA, many large systems |
| Meditech | 14% | Regional hospitals, community facilities |
| Altera Digital Health (Allscripts) | 5% | Medium hospitals, behavioral health |
| All Others | 21% | Smaller vendors, specialized systems |

**Ambulatory EHR Market Share (2024)**

| Vendor | Market Share | Primary Users |
|--------|--------------|---------------|
| Epic | 35% | Large practices, academic centers |
| Oracle Health | 12% | Multi-specialty groups |
| eClinicalWorks | 8% | Primary care, small practices |
| Athenahealth | 8% | Small to medium practices |
| Veradigm (Allscripts) | 6% | Various specialties |
| All Others | 31% | Specialty-specific, legacy systems |

### Market Dynamics

**Switching Costs Create Lock-In**

| Factor | Typical Cost/Impact |
|--------|---------------------|
| Implementation cost | $150-500 million for large health systems |
| Data migration | Incomplete, risky, often loses historical data |
| Training | 6-12 months to full productivity |
| Workflow disruption | 2-3 year adjustment period |
| Interface rebuilding | Connections to labs, pharmacies, devices |

**Consequences of Concentration**

- Annual price increases of 5-15% with limited negotiating leverage
- Customization costs often exceed initial licensing fees
- Interface fees for connecting third-party applications
- Data portability restrictions limit competitive switching
- Innovation concentrated in incumbent roadmaps

## Interoperability Status

### The Gap Between Policy and Reality

Federal regulations now require information sharing, but implementation remains incomplete.

**21st Century Cures Act Implementation**

| Requirement | Status (2024) |
|-------------|---------------|
| Information blocking prohibition | In effect, minimal enforcement |
| USCDI data class requirements | V3 required, adoption ongoing |
| Patient access via apps (API) | Required, adoption slow |
| Trusted Exchange Framework (TEFCA) | Early implementation phase |
| Payer access requirements | Effective, resistance continuing |

### Current Exchange Mechanisms

**Health Information Exchanges (HIEs)**

| Type | Count | Coverage | Limitations |
|------|-------|----------|-------------|
| Statewide public HIEs | 46 states | Varies widely | Underfunded, incomplete participation |
| Regional private HIEs | 100+ | Major metros | Fragmented, limited cross-network sharing |
| Vendor networks (Care Everywhere, CommonWell) | 3 major | Large systems only | Competing standards, coverage gaps |
| Direct Messaging | Universal | All certified EHRs | Push-only, requires knowing recipient |

**Practical Interoperability Rates**

| Scenario | Success Rate | Primary Barrier |
|----------|--------------|-----------------|
| Same EHR vendor | 80-90% | Technical configuration |
| Different vendors, same HIE | 40-60% | Data format inconsistencies |
| Different vendors, different markets | 10-30% | No exchange pathway |
| Patient-requested records | Variable | Process complexity |

### TEFCA Progress

The Trusted Exchange Framework and Common Agreement aims to create a national floor for interoperability.

**Current Status (2024)**

| Component | Status |
|-----------|--------|
| Qualified Health Information Networks (QHINs) | 7 designated, 3 operational |
| Required Use Cases | Query-based exchange, directed exchange |
| Participant Adoption | Early adopters only |
| Geographic Coverage | Major metro areas, gaps in rural |

## Clinician Experience

### Documentation Burden

**Time Allocation Studies**

| Activity | Physician Time | Nursing Time |
|----------|----------------|--------------|
| Direct patient care | 27% | 37% |
| EHR documentation | 37% | 28% |
| Other administrative | 15% | 20% |
| Inbox management | 12% | 5% |
| Other activities | 9% | 10% |

**"Pajama Time" - After-Hours Work**

| Provider Type | Average After-Hours EHR Time |
|---------------|------------------------------|
| Primary care physicians | 1.5-2.5 hours/day |
| Specialists | 1-2 hours/day |
| Hospitalists | 0.5-1 hour/day |
| Nurses | 0.5-1 hour/day |

### Usability Problems

**Common Complaints from Clinicians**

| Issue | Impact |
|-------|--------|
| Excessive clicks | 4,000+ clicks per day for some workflows |
| Alert fatigue | 90%+ of alerts overridden, missing important ones |
| Template bloat | Notes 4x longer than paper era, harder to review |
| Poor mobile access | Cannot work efficiently outside clinic |
| Slow performance | Wait times disrupt clinical thinking |
| Copy-paste propagation | Errors persist across notes |

### Burnout Connection

**Correlation with EHR Dissatisfaction**

| Burnout Factor | EHR Contribution |
|----------------|------------------|
| Physicians reporting burnout | 50-63% (varies by specialty) |
| EHR as major contributor | 70%+ cite EHR among top factors |
| Intent to reduce hours | 40% considering cutting back |
| Early retirement consideration | 30%+ considering leaving medicine |

## Patient Access

### Portal Adoption and Limitations

**Patient Portal Statistics**

| Metric | Rate |
|--------|------|
| Patients offered portal access | 73% |
| Patients who have accessed portal | 40% |
| Patients using portal regularly | 15-20% |
| Access disparities (by income) | 2x gap between high and low income |
| Access disparities (by age) | Significant gaps for 65+ |

**Common Patient Frustrations**

| Issue | Description |
|-------|-------------|
| Multiple portals | Different portal for each provider |
| Limited data | Clinical notes often excluded |
| Delayed results | Test results held for days before release |
| Download complexity | Formats unusable by patients |
| Mobile limitations | Many portals not mobile-optimized |
| No aggregation | Cannot combine records across providers |

### Patient API Access (21st Century Cures)

**SMART on FHIR App Availability**

| Category | Status |
|----------|--------|
| Apps certified for patient use | 100+ available |
| Health systems supporting apps | Growing but limited |
| Patient awareness | Very low |
| Actual usage rates | Under 5% of eligible patients |

## Cybersecurity Landscape

### Healthcare as a Target

**Why Healthcare Is Vulnerable**

| Factor | Impact |
|--------|--------|
| Data value | Medical records worth 10-50x credit cards on dark web |
| Operational pressure | Hospitals must pay to restore operations |
| Legacy systems | Many running outdated, unpatched software |
| Fragmented ownership | Thousands of independent entities |
| Limited IT budgets | Often 3-5% of operating budget vs. 10%+ in finance |

### Attack Statistics

**Healthcare Cybersecurity Incidents (2023)**

| Metric | Value |
|--------|-------|
| Reported breaches | 700+ |
| Patients affected | 85+ million |
| Ransomware attacks on hospitals | 140+ major incidents |
| Average ransom payment | $1.5 million |
| Average downtime | 21 days |
| Average total cost per breach | $10.9 million |

### Recent Major Incidents

| Incident | Impact |
|----------|--------|
| Change Healthcare (2024) | Nationwide payment disruption, weeks of claims backlog |
| CommonSpirit (2022) | 140 hospitals affected, patient care disrupted |
| Universal Health Services (2020) | 400 facilities, $67 million cost |
| Scripps Health (2021) | Month-long outage, patient diversions |

## Telehealth Infrastructure

### Post-Pandemic Status

**Telehealth Utilization Trends**

| Period | Telehealth Share of Visits |
|--------|---------------------------|
| Pre-COVID (2019) | 1-2% |
| Peak COVID (April 2020) | 40-50% |
| Current (2024) | 15-20% |
| Behavioral health | 35-40% |
| Primary care | 10-15% |
| Specialty care | 5-10% |

### Infrastructure Challenges

**Technical Barriers**

| Issue | Affected Population |
|-------|---------------------|
| Broadband access | 21 million lack access, 100+ million have inadequate speeds |
| Device access | 15% of adults lack smartphone, higher in elderly |
| Digital literacy | Significant barriers for elderly, disabled, low-income |
| Video platform integration | Many not integrated with EHR workflow |

**Policy Uncertainty**

| Issue | Status |
|-------|--------|
| Medicare reimbursement parity | Temporary waivers, unclear future |
| Audio-only coverage | State variation, Medicare uncertain |
| Geographic restrictions | Traditional site requirements uncertain |
| Licensure portability | State compacts incomplete |

## AI and Clinical Decision Support

### Current Applications

**Deployed AI/ML in Healthcare**

| Application | Maturity | Adoption |
|-------------|----------|----------|
| Imaging analysis (radiology) | FDA-approved products | Growing |
| Sepsis prediction | Available, mixed results | Moderate |
| Clinical documentation (ambient) | Emerging | Rapid growth |
| Prior authorization automation | Developing | Early adoption |
| Drug interaction checking | Mature | Universal |
| Diagnostic decision support | Available | Limited adoption |

### Regulatory Status

**FDA Approach to AI/ML in Healthcare**

| Category | Regulatory Pathway |
|----------|-------------------|
| Software as Medical Device (SaMD) | 510(k), De Novo, PMA depending on risk |
| Clinical Decision Support | Most exempt under 21st Century Cures |
| Adaptive algorithms | Predetermined change control plans |
| Generative AI documentation | Largely unregulated currently |

### Concerns

| Issue | Description |
|-------|-------------|
| Algorithmic bias | Models trained on biased data propagate disparities |
| Validation gaps | Performance may degrade in different populations |
| Liability uncertainty | Unclear who is responsible for AI errors |
| Transparency | Black box models resist clinical interpretation |
| Workflow integration | Many tools not embedded in clinical workflow |

## Public Health Data Systems

### COVID-19 Exposed Fundamental Weaknesses

**Failures During Pandemic**

| System | Failure |
|--------|---------|
| Case reporting | Fax-based, days/weeks delayed |
| Testing results | Inconsistent electronic reporting |
| Hospitalization data | Required new collection systems |
| Vaccine tracking | Fragmented state registries |
| Variant surveillance | Genomic data not integrated |

### Current Improvement Efforts

**CDC Data Modernization Initiative**

| Component | Status |
|-----------|--------|
| Funding | $1 billion over 4 years (FY21-24) |
| FHIR-based reporting | Pilots underway |
| Cloud infrastructure | Transitioning from legacy |
| Workforce development | Training programs launched |
| State capacity building | Grants distributed |

**Ongoing Gaps**

| Gap | Impact |
|-----|--------|
| State capacity variation | Some states far behind |
| Funding sustainability | Initiative funding time-limited |
| Workforce shortage | Public health informatics specialists scarce |
| Standard adoption | Slow implementation of modern standards |

## Standards Landscape

### Current Standards

| Standard | Use Case | Adoption |
|----------|----------|----------|
| HL7 FHIR R4 | Modern API-based exchange | Required for patient access |
| C-CDA (Consolidated CDA) | Document-based exchange | Universal for clinical summaries |
| HL7 v2 | Legacy messaging | Still dominant for lab, ADT |
| NCPDP SCRIPT | Pharmacy e-prescribing | Universal for prescriptions |
| X12 | Administrative transactions | Universal for claims |

### US Core Data for Interoperability (USCDI)

**USCDI Version 3 (Current Requirement)**

| Data Class | Elements |
|------------|----------|
| Patient Demographics | Name, DOB, address, contact, etc. |
| Allergies and Intolerances | Substance, reaction, severity |
| Medications | Current, historical, administered |
| Problems | Diagnoses, health concerns |
| Procedures | Clinical procedures performed |
| Clinical Notes | Multiple note types |
| Vital Signs | Standard measurements |
| Laboratory | Results, interpretations |
| Immunizations | Vaccine records |
| Health Insurance | Payer information |

**Expansion Trajectory**

USCDI expands annually, with new data classes added through public comment and ONC rulemaking.

## Key Statistics Summary

| Category | Key Metric |
|----------|------------|
| Federal investment | $36+ billion since 2009 |
| Hospital EHR adoption | 96% certified systems |
| Physician EHR adoption | 89% using any EHR |
| Market concentration | Epic + Oracle = 60% hospitals |
| Documentation time | 37% of physician time |
| Burnout citing EHR | 70%+ of burned out physicians |
| Breaches annually | 700+ affecting 85M+ patients |
| HIE query success | 10-30% across different networks |
| Patient portal use | 40% have accessed, 15-20% regular |
| Telehealth current | 15-20% of visits |

## Related Topics

- [History](03-history.md) - How we got here
- [Root Causes](04-root-causes.md) - Why problems persist
- [Healthcare: Current State](../02-current-state.md) - Broader healthcare context
- [Privacy: Data Protection](../../privacy/02-current-state.md) - Privacy frameworks

## Document Navigation

- Previous: [Overview](01-overview.md)
- Next: [History](03-history.md)
