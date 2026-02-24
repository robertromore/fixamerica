# Biometric Privacy: Solutions

## Overview

Biometric privacy requires a multi-layered approach: federal legislation establishing baseline consent and use requirements, government facial recognition restrictions, mandatory accuracy and bias standards, and robust enforcement through private right of action. Solutions must account for biometric data's immutability -- the irreversible nature of biometric compromise distinguishes it from all other categories of personal data.

## Solution 1: Federal Biometric Privacy Act

### Description

Enact dedicated federal biometric privacy legislation modeled on Illinois BIPA, establishing consent requirements, retention limits, sale prohibition, and private right of action for all biometric data.

### Key Provisions

- **Written consent**: Informed, written consent required before any collection of biometric identifiers or information
- **Notice**: Entity must inform individual of purpose and duration of collection before obtaining consent
- **Retention and destruction**: Biometric data must be destroyed when initial purpose is satisfied or within 3 years of last interaction, whichever comes first
- **No sale or profit**: Biometric identifiers and information may not be sold, leased, traded, or otherwise profited from
- **Private right of action**: $1,000 per negligent violation, $5,000 per intentional or reckless violation, plus attorney's fees
- **No federal ceiling preemption**: Does not preempt stronger state laws (preserves BIPA)
- **Heightened breach penalties**: Biometric data breaches face enhanced penalties reflecting immutability

### Evidence Base

- BIPA has generated $6+ billion in settlements/judgments, demonstrating both the scale of violations and the effectiveness of private enforcement
- Texas/Washington laws without PRA have produced minimal enforcement, confirming that PRA is essential
- GDPR classifies biometric data as "special category" requiring explicit consent since 2018
- 19 state privacy laws classify biometric data as sensitive, confirming broad acceptance of heightened protections

### Costs

| Cost Category | Estimated | Bearer |
|---------------|-----------|--------|
| Company compliance (consent systems) | $50K-500K per company | Industry |
| Retention and destruction systems | $50K-200K per company | Industry |
| Enforcement (federal) | $30-50 million/year | Federal budget |
| Litigation costs | Variable | Industry (for violations) |

### Timeline

- Legislation: 12-18 months
- Implementation: 12 months after enactment
- Full enforcement: 24-30 months

### International Models

- **EU GDPR**: Biometric data as "special category" (Article 9); explicit consent required
- **Illinois BIPA**: Written consent, no sale, retention/destruction, PRA ($1,000/$5,000)
- **EU AI Act**: Restricts real-time biometric identification; risk-based approach

---

## Solution 2: Government Facial Recognition Moratorium

### Description

Impose a federal moratorium on government use of facial recognition technology in public spaces until mandatory accuracy standards, bias testing, and oversight mechanisms are established.

### Key Provisions

- **Federal moratorium**: Federal agencies may not use facial recognition in public spaces for 3 years
- **State/local funding condition**: State and local agencies receiving federal funds may not use facial recognition in public spaces during moratorium
- **Exceptions**: Targeted warrant-based searches (one-to-one matching against specific suspects) permitted with judicial authorization
- **Accuracy and bias standards**: During moratorium, NIST develops mandatory accuracy standards including demographic performance requirements
- **Independent auditing**: After moratorium, deployment permitted only after independent bias audit and continuing oversight
- **Annual reporting**: All government facial recognition use must be reported publicly

### Evidence Base

- 20+ cities and counties have enacted facial recognition bans without public safety deterioration
- All documented wrongful arrests from facial recognition involve Black individuals, demonstrating systemic bias
- NIST FRVT shows persistent demographic accuracy disparities across vendors
- EU AI Act (2024) bans real-time remote biometric identification with limited exceptions, demonstrating international viability
- Amazon, IBM, Microsoft imposed voluntary moratoriums on law enforcement sales (2020), acknowledging concerns

### Costs

| Cost Category | Estimated | Bearer |
|---------------|-----------|--------|
| Moratorium impact on law enforcement | Minimal; cases solved without FR exceed FR-assisted cases | Law enforcement agencies |
| Accuracy standard development | $10-20 million | NIST/federal budget |
| Auditing infrastructure | $20-30 million/year | Federal budget |
| Alternative investigation methods | Already exist and are used | Law enforcement agencies |

### Timeline

- Legislation: 12-18 months
- Moratorium: 3 years
- Standards development: During moratorium
- Resumption (with standards): Year 4+

### International Models

- **EU AI Act**: Bans real-time remote biometric identification in public spaces; limited law enforcement exceptions with judicial authorization
- **San Francisco/Boston/Portland bans**: Local models demonstrating feasibility
- **Canada Privacy Commissioner**: Called for moratorium on police use of facial recognition (2021)

---

## Solution 3: Mandatory Accuracy and Bias Standards

### Description

Establish mandatory accuracy and demographic performance standards that biometric systems must meet before deployment, with regular auditing and public reporting.

### Key Provisions

- **Pre-deployment testing**: All biometric systems must pass NIST-administered accuracy testing before deployment
- **Demographic performance requirements**: Systems must meet minimum accuracy thresholds across all demographic groups (race, gender, age)
- **Maximum acceptable false positive rate**: No more than 1:1,000,000 for one-to-many matching across all demographic groups
- **Disparate impact prohibition**: If a system's error rate for any demographic group exceeds 3x the rate for the most accurate group, it may not be deployed
- **Regular auditing**: Deployed systems must be audited annually by independent third parties
- **Public reporting**: All accuracy and demographic performance data must be publicly reported
- **Liability for misidentification**: Vendors liable for damages when misidentification leads to wrongful arrest, detention, or other harm

### Evidence Base

- Buolamwini & Gebru (2018) documented 43x accuracy disparity between light-skinned males and dark-skinned females
- NIST FRVT consistently shows demographic differentials across vendors
- All documented wrongful arrests from facial recognition involve Black individuals
- EU AI Act requires "high-risk AI systems" (including biometric identification) to meet accuracy and non-discrimination standards before deployment

### Costs

| Cost Category | Estimated | Bearer |
|---------------|-----------|--------|
| NIST testing program expansion | $20-30 million/year | Federal budget |
| Vendor testing compliance | $100K-1 million per vendor | Industry |
| Annual auditing | $50K-200K per deployed system | Industry/agencies |
| Accuracy improvement R&D | Significant | Industry |

### Timeline

- Standards development: 18-24 months
- Pre-deployment testing requirement: Year 2
- Audit and reporting requirements: Year 2+

---

## Solution 4: Biometric Data Breach Enhanced Penalties

### Description

Establish enhanced penalties for biometric data breaches reflecting the irreversible nature of biometric data compromise.

### Key Provisions

- **Mandatory notification**: Biometric data breaches must be reported within 48 hours (vs. typical 60 days for other data)
- **Enhanced penalties**: Civil penalties 3x the standard breach penalty for biometric data
- **Mandatory credit monitoring**: Lifetime identity protection services (not typical 1-2 year monitoring) for biometric breach victims
- **Vendor liability**: Technology vendors that store biometric data face strict liability for breaches
- **Retention minimization**: Breach penalties increase with volume of stored biometric data, incentivizing minimization
- **No breach safe harbor**: Unlike some data types, reasonable security measures do not provide complete safe harbor for biometric breaches given immutability

### Evidence Base

- Biometric data cannot be changed after a breach, unlike passwords, credit cards, or even SSNs
- Standard breach remediation (change passwords, freeze credit) does not work for biometric data
- Increasing penalties for biometric breaches creates stronger incentive to minimize collection and maximize security
- Current breach notification laws do not distinguish biometric data from other categories

### Costs

| Cost Category | Estimated | Bearer |
|---------------|-----------|--------|
| Enhanced security measures | $100K-1 million per organization | Industry |
| Lifetime monitoring for victims | $500-2,000 per person (annual) | Industry (breaching entity) |
| Enforcement | Part of breach enforcement budget | Federal/state budget |

### Timeline

- Achievable as standalone legislation or part of comprehensive biometric privacy bill
- 12-18 months for legislation; immediate effect after enactment

---

## Solution 5: Worker Biometric Protection Act

### Description

Establish specific protections for workers subject to employer biometric data collection, addressing the power imbalance that makes meaningful consent difficult in employment contexts.

### Key Provisions

- **Voluntary participation**: Employers must offer non-biometric alternatives for timekeeping and access control
- **Written consent with alternative**: Consent is not valid unless a non-biometric alternative is simultaneously available
- **No retaliation**: Employers may not retaliate against workers who choose non-biometric alternatives
- **Retention limits**: Employer biometric data destroyed within 30 days of employment termination
- **No sharing**: Employer biometric data may not be shared with third parties (including parent companies or vendors) beyond what is necessary for system operation
- **Worker notification**: Workers must be notified of all biometric data practices annually
- **Private right of action**: Workers may sue for violations with statutory damages

### Evidence Base

- Estimated 30+ million workers subject to biometric time clocks
- Workers often cannot meaningfully refuse employer biometric demands
- BIPA litigation has frequently involved employer biometric time clock violations (e.g., *Cothron v. White Castle*)
- Employment context creates coercion that undermines consent framework
- EU GDPR Article 29 Working Party opinion treats employee consent as presumptively invalid due to power imbalance

### Costs

| Cost Category | Estimated | Bearer |
|---------------|-----------|--------|
| Non-biometric alternative systems | $5K-50K per employer | Employers |
| Compliance processes | $10K-50K per employer | Employers |
| Enforcement | Part of labor enforcement budget | Federal/state budget |

### Timeline

- Achievable at state level within 12 months
- Federal level within 18-24 months

---

## Solution 6: Consumer DNA Privacy Act

### Description

Establish specific protections for consumer genetic data, addressing the unique privacy risks of DNA information including familial exposure and law enforcement access.

### Key Provisions

- **Affirmative consent for each use**: Separate consent required for DNA testing, research participation, and third-party sharing
- **Law enforcement access**: Consumer DNA companies may not share data with law enforcement absent a warrant or valid court order; no voluntary cooperation
- **Familial privacy**: Individuals have the right to opt out of familial matching that could identify relatives
- **Data portability and deletion**: Consumers may download their data and demand destruction of physical samples and digital records
- **No sale**: Consumer DNA data may not be sold to insurance companies, employers, or data brokers
- **Company insolvency**: DNA data must be destroyed (not transferred or sold) if company ceases operations or is acquired
- **Research consent**: Separate, specific consent for use in research; blanket consent not valid

### Evidence Base

- 40+ million Americans have submitted DNA to consumer testing companies
- 23andMe financial difficulties raised questions about data disposition in insolvency
- Law enforcement has used consumer DNA databases for forensic genealogy (Golden State Killer case, 2018)
- Genetic information reveals health predispositions affecting insurance and employment
- GINA (Genetic Information Nondiscrimination Act, 2008) protects against genetic discrimination in health insurance and employment but does not regulate consumer DNA companies

### Costs

| Cost Category | Estimated | Bearer |
|---------------|-----------|--------|
| Company compliance (consent systems) | $500K-2 million per company | Industry |
| Data destruction requirements | Variable | Industry |
| Enforcement | $10-20 million/year | Federal budget |

### Timeline

- Achievable as standalone legislation within 12-18 months

---

## Solution 7: Emotion Recognition Ban

### Description

Ban the use of emotion recognition technology in commercial and government contexts, reflecting the scientific consensus that the technology is unreliable and harmful.

### Key Provisions

- **Complete ban**: Prohibit the use of systems that claim to detect, infer, or predict emotions, mental states, or intentions from biometric data (facial expressions, voice, gait)
- **Exceptions**: Clinical use in healthcare settings with informed consent; academic research with IRB approval
- **No government use**: Federal, state, and local government agencies may not use emotion recognition for any purpose
- **No employment use**: Employers may not use emotion recognition for hiring, evaluation, or monitoring
- **No commercial use**: Retailers, advertisers, and service providers may not use emotion recognition for customer analysis

### Evidence Base

- Scientific consensus increasingly rejects the premise that facial expressions reliably indicate emotions (Barrett et al., "Emotional Expressions Reconsidered," *Psychological Science in the Public Interest*, 2019)
- EU AI Act (2024) bans emotion recognition in workplaces and educational settings
- Emotion recognition has been used to evaluate job applicants, monitor students, and assess criminal suspects without scientific validity
- Association for Psychological Science has raised concerns about emotion recognition claims

### Costs

| Cost Category | Estimated | Bearer |
|---------------|-----------|--------|
| Enforcement | Minimal; part of biometric enforcement | Federal/state budget |
| Industry adjustment | Variable | Vendors who sell emotion recognition products |

### Timeline

- Achievable within 12 months
- EU AI Act ban provides international precedent

## Solution Sequencing

| Priority | Solution | Timeline | Difficulty |
|----------|----------|----------|------------|
| 1 | Federal Biometric Privacy Act | 12-18 months | High |
| 2 | Government Facial Recognition Moratorium | 12-18 months | Very High (law enforcement opposition) |
| 3 | Mandatory Accuracy and Bias Standards | 18-24 months | High |
| 4 | Worker Biometric Protection | 12-24 months | Moderate |
| 5 | Biometric Data Breach Enhanced Penalties | 12-18 months | Moderate |
| 6 | Consumer DNA Privacy Act | 12-18 months | Moderate |
| 7 | Emotion Recognition Ban | 12 months | Low-Moderate |

## Dependencies

- Solution 1 (Federal Biometric Privacy Act) is the foundation; other solutions can be standalone or integrated
- Solution 2 (moratorium) and Solution 3 (accuracy standards) are linked: moratorium creates time for standards development
- Solution 4 (breach penalties) can be enacted independently
- Solution 5 (worker protection) addresses subset of Solution 1 but can proceed independently
- Solution 6 (DNA privacy) is largely independent of other solutions
- Solution 7 (emotion recognition ban) can proceed immediately

## Document Navigation

- Previous: [Opposition](06-opposition.md)
- Next: [Roadmap](08-roadmap.md)
- Up: [Biometric Privacy Overview](01-overview.md)
