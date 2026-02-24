---
freshness:
  last-reviewed: 2026-02-20
  data-year: 2025
  review-cycle: 6
  sections:
    - name: "HIPAA Framework and Enforcement"
      data-year: 2024-2025
    - name: "Digital Health Data Outside HIPAA"
      data-year: 2024-2025
    - name: "Key Statistics"
      data-year: 2024-2025
    - name: "State Law Developments"
      data-year: 2024-2025
notes:
  - Revisit after HHS issues any new HIPAA rulemaking or guidance on reproductive health data.
  - Monitor FTC enforcement actions against health apps and data brokers for updated penalty figures.
  - Update after any Supreme Court decisions affecting health privacy or Dobbs-related data access.
sources:
  count: 12
  verified: 2026-02-20
  broken: 0
---

# Health Privacy: Current State

## HIPAA Framework and Enforcement

### What HIPAA Covers

The Health Insurance Portability and Accountability Act of 1996, as implemented through the Privacy Rule (2003) and subsequent amendments, establishes the primary federal framework for health privacy. HIPAA applies to three categories of "covered entities" and their "business associates."

**Covered Entities**

| Entity Type | Examples | Approximate Count |
|-------------|----------|-------------------|
| Health care providers | Hospitals, physicians, clinics, pharmacies | 1+ million providers (CMS National Plan and Provider Enumeration System, 2024) |
| Health plans | Insurers, HMOs, Medicare, Medicaid, employer health plans | 1,100+ health insurance issuers (NAIC, 2024) |
| Health care clearinghouses | Entities that process health claims data | Approximately 70 (HHS, 2024) |

**Business Associates**

Any entity that performs functions on behalf of a covered entity involving PHI must sign a Business Associate Agreement (BAA) and comply with HIPAA's security and privacy requirements. Estimates suggest 1-3 million business associates operate in the U.S., ranging from cloud storage providers to billing companies to law firms (HIPAA Journal, 2024).

### Key HIPAA Protections

| Protection | Requirement | Practical Effect |
|------------|-------------|------------------|
| Privacy Rule | Limits use and disclosure of PHI | Patients must authorize most non-treatment disclosures |
| Security Rule | Administrative, physical, and technical safeguards | Covered entities must protect electronic PHI |
| Breach Notification Rule | Notify individuals and HHS of breaches | Breaches affecting 500+ persons publicly reported |
| Minimum necessary standard | Limit PHI to what is needed | Reduces incidental exposure |
| Patient rights | Access, amendment, accounting of disclosures | Patients can request their records |
| Enforcement | Civil monetary penalties, criminal penalties | HHS Office for Civil Rights (OCR) investigates |

### HIPAA Enforcement Record

HHS's Office for Civil Rights (OCR) is the primary HIPAA enforcement agency, but its capacity has not kept pace with the volume of complaints and breaches.

**Enforcement Data (FY 2019-2024)**

| Metric | FY 2019 | FY 2020 | FY 2021 | FY 2022 | FY 2023 | FY 2024 (est.) |
|--------|---------|---------|---------|---------|---------|----------------|
| Complaints received | 27,182 | 27,009 | 30,435 | 32,000+ | 34,000+ | 35,000+ |
| Complaints resolved | 26,688 | 28,859 | 28,859 | 30,000+ | 32,000+ | 33,000+ |
| Enforcement actions (CMPs, settlements) | 12 | 19 | 14 | 22 | 11 | 15+ |
| Total penalties collected | $12.3M | $13.5M | $5.1M | $2.2M | $4.2M | $5.5M+ |
| Large breach reports (500+ individuals) | 510 | 642 | 714 | 707 | 725 | 740+ |

*Sources: HHS OCR Annual Reports; HHS OCR Breach Portal (2024)*

**Key patterns:**

- Complaints far exceed enforcement capacity
- Penalties are modest relative to the value of health data and revenue of violators
- Enforcement focuses on egregious cases, leaving systemic practices unaddressed
- Criminal enforcement by DOJ remains rare (fewer than 5 cases per year)

### Major HIPAA Gaps

| Gap | Description | Consequence |
|-----|-------------|-------------|
| App exclusion | Health and wellness apps not created by or on behalf of a covered entity are not subject to HIPAA | Millions of health app users have no HIPAA protection |
| Consumer device exclusion | Fitness trackers, smartwatches, and wearables not covered | Continuous health monitoring data unprotected |
| De-identification loophole | De-identified data can be sold or shared without restriction | Re-identification is increasingly feasible (Sweeney, Harvard, 2015) |
| No private right of action | Only HHS and DOJ can enforce HIPAA; patients cannot sue | Individuals have no direct remedy for violations |
| Marketing exception | Covered entities can use PHI for certain marketing purposes | Patients receive targeted marketing based on health conditions |
| Psychotherapy notes exception | Separate authorization required but enforcement is weak | Mental health notes sometimes disclosed improperly |
| Research exception | IRB-approved research can use PHI without individual consent | Patients may not know their data is used in research |

---

## Digital Health Data Outside HIPAA

### Health Apps and Wearables

The digital health market has exploded, but the vast majority of health-related apps and devices operate entirely outside HIPAA.

**Market Scale**

| Metric | Value | Source |
|--------|-------|--------|
| Health and fitness app downloads (U.S., 2023) | 350+ million | IQVIA Institute for Human Data Science (2024) |
| mHealth apps available globally | 350,000+ | IQVIA "Digital Health Trends" (2024) |
| Wearable health device users (U.S.) | 110+ million | Insider Intelligence / eMarketer (2024) |
| Telehealth utilization (post-COVID plateau) | 20-25% of outpatient visits | McKinsey & Company, "Telehealth" report (2024) |
| Digital therapeutics market (U.S.) | $5.5+ billion | Grand View Research (2024) |

**Data Collection Practices**

Health apps routinely collect data that would be protected as PHI if held by a covered entity, including:

- Heart rate, blood pressure, blood oxygen, and sleep patterns
- Menstrual cycle tracking and fertility data
- Mental health self-assessments and therapy session logs
- Medication adherence and prescription information
- Diet, exercise, and weight data
- Symptom tracking and self-reported diagnoses

**Data Sharing Practices**

| Practice | Prevalence | Source |
|----------|------------|--------|
| Health apps sharing data with third parties | 81% of apps studied | Mozilla Foundation, *Privacy Not Included* (2023) |
| Apps sharing data with advertising platforms | 55% of apps studied | BMJ study on health app data flows (2019; conditions persist) |
| Apps without privacy policies | 28% of health apps | ONC/FDA app review (2023) |
| Apps sharing location data | 65% of health apps studied | International Digital Accountability Council (2023) |

### Reproductive Health Data Post-*Dobbs*

The Supreme Court's *Dobbs v. Jackson Women's Health Organization* (2022) decision created unprecedented risks for reproductive health data.

**Data Types at Risk**

- Period-tracking app data (cycle dates, pregnancy status, sexual activity)
- Location data showing visits to abortion providers or clinics
- Search history related to abortion services or medications
- Pharmacy records for mifepristone and misoprostol
- Telehealth records for abortion consultations
- Payment records for reproductive health services
- Communication records discussing pregnancy decisions

**Known Incidents and Risks**

| Incident | Year | Detail |
|----------|------|--------|
| Nebraska case: Facebook messages used to prosecute teenager | 2022 | Meta complied with warrant for private messages about medication abortion |
| Period tracker Flo Health: FTC enforcement | 2021 | FTC found Flo shared health data with Facebook and Google analytics despite privacy promises |
| Google geofence warrants near clinics | 2022-2023 | Google announced it would auto-delete location data near abortion clinics, but implementation questions remain |
| Crisis pregnancy centers collecting data | 2022-present | Centers collect detailed health data with minimal privacy protections and no HIPAA coverage |

**Regulatory Responses**

- HHS issued a final rule in April 2024 strengthening HIPAA protections for reproductive health information, prohibiting covered entities from disclosing PHI for purposes of investigating or penalizing lawful reproductive health care
- The FTC has used its Section 5 authority against health apps (Flo Health consent order, 2021; GoodRx enforcement, 2023; BetterHelp, 2023)
- Several states enacted reproductive health data shield laws (California, Washington, New York, Illinois)

### Mental Health Data

**Scale of the Problem**

| Metric | Value | Source |
|--------|-------|--------|
| Americans using mental health apps | 32+ million | Statista / app analytics (2024) |
| Mental health apps sharing data with third parties | 81% | Mozilla Foundation (2023) |
| BetterHelp FTC penalty for data sharing | $7.8 million | FTC enforcement action (2023) |
| Crisis hotline data sharing concerns | 988 Suicide & Crisis Lifeline data shared with dispatchers | Senate investigation (2022) |
| Therapy apps retaining session transcripts | Majority of AI-based therapy apps | Health Affairs study (2023) |

**Key concerns:**

- Therapy chatbot conversations may be used for AI training without clear consent
- Mental health assessment data sold to data brokers and insurers
- Crisis hotline metadata shared with law enforcement in some jurisdictions
- Substance abuse treatment records (42 CFR Part 2) protections weakened by CARES Act amendments in 2020, aligning certain disclosures more closely with HIPAA

### Genetic and Genomic Data

**Consumer Genetic Testing**

| Metric | Value | Source |
|--------|-------|--------|
| Americans who have taken consumer DNA tests | 45+ million | MIT Technology Review (2024) |
| 23andMe data breach (2023) | 6.9 million users affected | 23andMe SEC filing (2023) |
| 23andMe bankruptcy filing | 2024 | Multiple news sources |
| Law enforcement requests to genetic databases | 300+ cases using genetic genealogy | Parabon NanoLabs / ISHI conference data (2024) |
| States with genetic privacy laws beyond GINA | 15+ | NCSL (2024) |

**Federal Protection Gaps**

- GINA (2008) prohibits genetic discrimination in employment and health insurance but does not cover life insurance, disability insurance, or long-term care insurance
- HIPAA covers genetic data held by covered entities but not consumer testing companies
- No federal law governs law enforcement access to consumer genetic databases
- 23andMe's 2024 bankruptcy raised questions about the fate of millions of customers' genetic data

### Hospital Website Data Leakage

**The Tracking Pixel Problem**

| Finding | Detail | Source |
|---------|--------|--------|
| Hospitals with Meta Pixel on patient portals | 33 of top 100 hospitals investigated | The Markup, "Pixel Hunt" (2022) |
| Data transmitted to Meta | IP addresses, appointment types, physician names, search terms | The Markup investigation |
| HHS guidance issued | December 2022 bulletin warning about tracking technologies | HHS OCR (2022) |
| Lawsuits filed | 50+ class action suits against hospitals | Bloomberg Law litigation tracker (2023-2024) |
| FTC enforcement | Landmark settlements with telehealth companies | GoodRx ($1.5M), BetterHelp ($7.8M) (2023) |

---

## State Law Developments

### States with Health-Specific Privacy Protections

| State | Key Provision | Year Enacted |
|-------|---------------|--------------|
| California | CCPA/CPRA covers health inferences; Genetic Information Privacy Act | 2018/2020, expanded 2024 |
| Washington | My Health My Data Act -- covers all health data regardless of collector | 2023 |
| Nevada | Consumer health data privacy law modeled on Washington | 2023 |
| Connecticut | Comprehensive privacy law with health data provisions | 2023 |
| Illinois | Genetic Information Privacy Act | 1998, amended 2024 |
| New York | SHIELD Act; proposed Health Information Privacy Act | 2019; proposed |
| Oregon | Reproductive health data protections | 2023 |
| Colorado | Comprehensive privacy law with sensitive data provisions (health included) | 2023 |

**Washington's My Health My Data Act** is notable as the first state law to regulate consumer health data regardless of whether the collector is a HIPAA-covered entity. It requires consent before collecting or sharing health data, provides a private right of action, and covers a broad definition of "consumer health data."

### Reproductive Health Data Shield Laws

Several states enacted laws after *Dobbs* to protect reproductive health data:

| State | Key Protection | Year |
|-------|---------------|------|
| California | AB 352: prohibits disclosure of reproductive health data to out-of-state entities seeking to enforce abortion restrictions | 2022 |
| Washington | SB 5489: reproductive health data shield integrated into My Health My Data Act | 2023 |
| New York | Reproductive health data protection executive order and proposed legislation | 2022-2023 |
| Illinois | Reproductive health data protections under state privacy law amendments | 2023 |
| Maryland | Reproductive health data privacy provisions | 2023 |

---

## Federal Regulatory Activity

### HHS Actions

- **April 2024 HIPAA Reproductive Health Rule**: Final rule prohibiting covered entities from disclosing PHI for investigating lawful reproductive health care, with limited exceptions
- **December 2022 Tracking Technology Bulletin**: OCR guidance warning covered entities about online tracking technologies that may transmit PHI
- **Information Blocking Rule**: ONC rules requiring health IT developers and providers to share electronic health information, with privacy exceptions

### FTC Actions

| Action | Year | Penalty | Significance |
|--------|------|---------|--------------|
| Flo Health (period tracker) | 2021 | Consent order (no monetary penalty) | First health app enforcement for misleading privacy claims |
| GoodRx (pharmacy app) | 2023 | $1.5 million | First enforcement under Health Breach Notification Rule |
| BetterHelp (therapy platform) | 2023 | $7.8 million | Shared therapy intake data with advertisers |
| Cerebral (mental health startup) | 2024 | $7.0 million | Shared patient data with advertising platforms |
| Premom (fertility app) | 2023 | Consent order | Shared health data with third-party analytics |

### Congressional Activity

| Bill | Status (119th Congress) | Key Provisions |
|------|------------------------|----------------|
| Health Data Privacy Act (proposed) | Not yet reintroduced | Would extend HIPAA-like protections to non-covered entities |
| American Data Privacy and Protection Act (ADPPA) | Stalled since 117th Congress | Would create comprehensive federal privacy law with health data provisions |
| My Body, My Data Act (proposed) | Reintroduced | Would create federal protections for reproductive health data |
| GINA 2.0 (proposed) | Not yet advanced | Would extend GINA protections to life, disability, and long-term care insurance |

---

## International Comparison

| Jurisdiction | Framework | Key Differences from U.S. |
|-------------|-----------|---------------------------|
| European Union | GDPR (health data as "special category") | Requires explicit consent; applies to all controllers regardless of sector |
| United Kingdom | UK GDPR + Data Protection Act 2018 | Health data receives heightened protection; NHS-specific guidance |
| Canada | PIPEDA + provincial health privacy laws | Privacy commissioners can investigate; sector-specific laws in provinces |
| Australia | Privacy Act + My Health Records Act | National electronic health record system with opt-out model |

---

## Summary

The current state of health privacy in America is defined by a widening gap between the volume of health data being collected and the legal protections governing it. HIPAA remains important but covers a shrinking share of health-related data as digital health tools proliferate. Federal enforcement is resource-constrained and penalty-weak. State laws are filling some gaps, particularly for reproductive health data and consumer health apps, but the patchwork creates inconsistency. The FTC has emerged as a significant enforcer but lacks a clear statutory mandate for comprehensive health data regulation. Genetic data protections are incomplete, and the 23andMe bankruptcy has underscored the fragility of privacy promises made by private companies.

## Document Navigation

- Previous: [Overview](01-overview.md)
- Next: [History](03-history.md)
- Up: [Overview](01-overview.md)
