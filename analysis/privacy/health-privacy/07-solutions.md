# Health Privacy: Solutions

## Overview

Comprehensive health privacy reform requires action across multiple dimensions: expanding the scope of federal protection beyond HIPAA's covered entities, modernizing HIPAA itself, addressing specific high-risk categories of health data (reproductive, mental health, genetic), strengthening enforcement, and empowering individuals with meaningful rights over their health data. The solutions proposed here are designed to be complementary and mutually reinforcing.

---

## Solution 1: Expand Federal Health Privacy to All Health Data

### The Problem

HIPAA covers less than half of the health-related data generated in the United States. Health apps, wearables, consumer genetic testing companies, health data brokers, and wellness programs operate largely outside any federal health privacy framework.

### The Proposal

Enact a comprehensive federal health data protection law that applies to any entity that collects, processes, or shares health-related data, regardless of whether the entity is a HIPAA-covered entity.

**Key elements:**

| Element | Description |
|---------|-------------|
| Broad definition of health data | Includes diagnoses, treatments, medications, genetic data, biometric health data, reproductive health data, mental health data, health inferences, and data collected for health-related purposes |
| Entity-agnostic coverage | Applies to any person or entity that collects or processes health data, not just covered entities |
| Consent requirements | Affirmative, informed consent required for collection and sharing of health data beyond what is necessary for the requested service |
| Data minimization | Entities may collect only the health data necessary for the stated purpose |
| Purpose limitation | Health data collected for one purpose may not be repurposed without additional consent |
| Deletion rights | Individuals may request deletion of their health data |
| Private right of action | Individuals may sue for violations, with statutory damages |

**Model:** Washington State's My Health My Data Act (2023), expanded to the federal level

### Evidence of Effectiveness

- Washington's My Health My Data Act took effect in March 2024 for large entities; compliance has been feasible
- The EU's GDPR covers health data as a "special category" requiring explicit consent; European digital health innovation continues (European Commission Digital Health report, 2024)
- FTC enforcement actions demonstrate that significant harms occur outside HIPAA's scope, validating the need for broader coverage

### Implementation Challenges

| Challenge | Mitigation |
|-----------|------------|
| Industry opposition | Phase in requirements; provide compliance assistance for small entities |
| Defining "health data" | Use broad definition with regulatory guidance for edge cases |
| Preemption concerns | Establish federal floor without preempting stronger state protections |
| Research access | Include research exceptions with IRB oversight and de-identification requirements |

---

## Solution 2: Modernize HIPAA

### The Problem

HIPAA was enacted in 1996 and its Privacy Rule took effect in 2003. The framework has not been comprehensively updated to address electronic health records, interoperability, cybersecurity threats, or modern data practices.

### The Proposal

Amend HIPAA through legislation and rulemaking to address contemporary challenges:

**Key reforms:**

- **Private right of action**: Allow individuals to sue covered entities for HIPAA violations with statutory damages
- **Enhanced penalties**: Increase maximum penalties to match entity revenue (e.g., 2-4% of annual revenue, similar to GDPR)
- **Minimum necessary reform**: Strengthen the minimum necessary standard with specific data-type restrictions
- **De-identification update**: Require stronger de-identification methods and prohibit re-identification
- **Cybersecurity requirements**: Mandate specific technical safeguards (encryption, multi-factor authentication, incident response plans)
- **Patient access improvements**: Reduce response time for patient access requests; eliminate excessive fees
- **Marketing restrictions**: Close marketing exceptions and prohibit sale of PHI for marketing purposes without explicit consent
- **Accounting of disclosures**: Expand right to accounting of disclosures for treatment, payment, and operations

### Evidence of Effectiveness

- HITECH Act (2009) demonstrated that HIPAA can be meaningfully strengthened through legislation
- Breach notification requirements have increased transparency and accountability
- States with stronger health privacy laws (California CMIA) show that higher standards are workable

---

## Solution 3: Reproductive Health Data Shields

### The Problem

Following *Dobbs*, reproductive health data can be used to enforce criminal abortion restrictions. This affects not only people seeking reproductive care but anyone whose health data might reveal pregnancy, miscarriage, or related medical events.

### The Proposal

Enact federal legislation prohibiting the use of health data to investigate, prosecute, or penalize reproductive health care that is lawful in the state where it was provided.

**Key elements:**

| Element | Description |
|---------|-------------|
| Prohibition on compelled disclosure | Entities may not be compelled to disclose health data for reproductive health investigations |
| Privilege creation | Federal testimonial privilege for reproductive health communications |
| Preemption of state subpoenas | Federal law preempts state-law subpoenas seeking reproductive health data across state lines |
| App and device coverage | Covers period trackers, fertility apps, and location data near clinics |
| Penalty for violations | Criminal penalties for misuse of reproductive health data |

**Model:** HHS April 2024 HIPAA Reproductive Health Rule (for covered entities) + My Body, My Data Act (proposed federal legislation)

### Limitations

- May face constitutional challenges under Commerce Clause and state sovereignty arguments
- Does not protect against in-state investigations where reproductive care itself occurred
- Requires enforcement mechanisms that may be difficult in hostile state jurisdictions

---

## Solution 4: Genetic Data Protection

### The Problem

Consumer genetic testing has generated a database of 45+ million Americans' DNA profiles. GINA (2008) prohibits genetic discrimination in health insurance and employment but leaves gaps in life insurance, disability insurance, long-term care insurance, and law enforcement access. The 23andMe bankruptcy (2024) highlighted the fragility of privacy promises made by private companies.

### The Proposal

Comprehensive genetic data protection legislation:

**Key elements:**

- **Expand GINA**: Extend non-discrimination protections to life insurance, disability insurance, long-term care insurance, and education
- **Consent for law enforcement access**: Require a warrant based on probable cause for law enforcement access to consumer genetic databases; prohibit bulk searches without individualized suspicion
- **Bankruptcy protections**: Genetic data cannot be transferred as a business asset in bankruptcy without individual consent
- **Right to deletion**: Individuals can require genetic testing companies to delete their raw genetic data and derived information
- **Limits on secondary use**: Genetic data collected for ancestry or health insights cannot be sold to third parties without specific, separate consent
- **Research safeguards**: Genetic research requires informed consent with ongoing opt-out rights

### Evidence of Effectiveness

- Illinois Genetic Information Privacy Act provides a model for state-level protections
- EU GDPR treats genetic data as a "special category" requiring explicit consent; European genetic testing companies comply successfully
- Several states have enacted post-23andMe-breach genetic privacy legislation

---

## Solution 5: Mental Health Data Protections

### The Problem

Mental health apps share data with third parties at alarming rates (81%, per Mozilla Foundation, 2023). Therapy platforms have been caught sharing intake data with advertisers. Crisis hotline data has been shared with law enforcement dispatchers. The stigma associated with mental health conditions makes data exposure particularly harmful.

### The Proposal

Targeted mental health data protections:

- **Extend 42 CFR Part 2-level protections** to mental health apps, therapy platforms, and crisis services
- **Prohibit advertising use** of mental health data under all circumstances
- **Strengthen crisis hotline privacy**: Prohibit sharing 988 Suicide & Crisis Lifeline data with law enforcement without a court order based on imminent danger
- **AI therapy restrictions**: Require disclosure when AI is used in mental health services; prohibit use of therapy session data for AI training without explicit consent
- **Anti-discrimination**: Prohibit use of mental health data in employment, insurance (beyond what GINA and ADA cover), and housing decisions

---

## Solution 6: Tracking Technology Restrictions

### The Problem

Hospitals and health care websites embed tracking pixels, analytics tools, and advertising SDKs that transmit patient health data to third parties. The Markup's 2022 investigation found that 33 of the top 100 U.S. hospitals had Meta Pixel on their patient-facing websites.

### The Proposal

- **Prohibit tracking technologies on health-related websites and apps** that transmit individually identifiable health information to advertising platforms
- **Require transparency**: Health websites must disclose all third-party tracking technologies
- **Extend to telehealth**: Telehealth platforms subject to same restrictions
- **FTC and HHS joint enforcement**: Coordinate enforcement between agencies
- **Safe harbor**: Organizations that conduct and remediate regular audits of tracking technologies receive reduced liability

### Evidence of Effectiveness

- HHS December 2022 bulletin warning about tracking technologies led many hospitals to remove pixels
- FTC enforcement against GoodRx and BetterHelp demonstrated that existing authority can address tracking, but prescriptive rules would be more effective
- Class action litigation has created financial incentives for compliance

---

## Solution 7: Strengthen Enforcement

### The Problem

Health privacy enforcement is underfunded, fragmented, and penalty-weak. HHS OCR processes tens of thousands of complaints annually but takes fewer than 25 enforcement actions. The FTC has expanded health privacy enforcement but lacks a clear statutory mandate. Patients have no private right of action under HIPAA.

### The Proposal

**Enforcement reforms:**

| Reform | Detail |
|--------|--------|
| Increase HHS OCR budget | Double enforcement budget from approximately $39 million to $80 million |
| Create private right of action | Allow individuals to sue for HIPAA violations with statutory damages ($1,000-$10,000 per violation) |
| Revenue-based penalties | Cap penalties at 2-4% of annual revenue for covered entities |
| State AG enforcement | Explicitly authorize state AGs to enforce federal health privacy laws |
| FTC health privacy authority | Grant FTC explicit authority to regulate health data practices through rulemaking |
| Whistleblower protections | Protect employees who report health privacy violations |
| Audit requirements | Mandate periodic privacy audits for large health data holders |

---

## Solution 8: Health Data Broker Regulation

### The Problem

Health data brokers aggregate health-related information from non-HIPAA sources (apps, web browsing, purchasing data, public records) to create health profiles and inferences that are sold to insurers, employers, and marketers.

### The Proposal

- **Registration requirement**: All entities that sell health-related data or inferences must register with the FTC
- **Consent requirement**: Health data may not be sold without affirmative consent from the data subject
- **Transparency**: Brokers must disclose data sources, categories, and customers
- **Right to access and delete**: Individuals can access and delete their health profiles held by brokers
- **Prohibition on sensitive categories**: Ban sale of health inferences related to specific conditions (HIV/AIDS, mental health, substance use, reproductive health) without explicit consent
- **Government purchase restrictions**: Government agencies may not purchase health data from brokers without a warrant or court order

---

## Summary of Solutions

| Solution | Primary Target | Key Mechanism | Timeline |
|----------|---------------|---------------|----------|
| Expand federal health privacy | Non-HIPAA health data | Comprehensive legislation | Medium-term (2-4 years) |
| Modernize HIPAA | Covered entities | Legislative amendment | Medium-term (2-4 years) |
| Reproductive data shields | All reproductive health data | Federal legislation | Short-term (1-2 years) |
| Genetic data protection | Consumer genetic testing | GINA expansion + new law | Medium-term (2-4 years) |
| Mental health data protections | Therapy apps, crisis services | Targeted regulation | Short-term (1-2 years) |
| Tracking technology restrictions | Health websites and apps | Prescriptive rules | Short-term (1-2 years) |
| Enforcement strengthening | All health data holders | Funding, penalties, private right of action | Short-to-medium-term (1-3 years) |
| Health data broker regulation | Data brokers | Registration, consent, transparency | Medium-term (2-4 years) |

---

## International Models

| Country/Region | Model | Key Lesson for U.S. |
|---------------|-------|---------------------|
| EU (GDPR) | Health data as "special category" requiring explicit consent | Data-based, not entity-based, approach is feasible and effective |
| UK | NHS Digital data governance framework | Sector-specific governance within comprehensive framework |
| Australia | My Health Records Act with opt-out model | National health records need strong governance but universal access benefits patients |
| Canada | Provincial health privacy laws (PHIPA in Ontario) | Provincial/state-level health privacy laws can complement federal frameworks |

## Document Navigation

- Previous: [Opposition](06-opposition.md)
- Next: [Roadmap](08-roadmap.md)
- Up: [Overview](01-overview.md)
