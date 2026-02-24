# Data Brokers: Solutions

## Overview

Reforming the data broker industry requires a multi-layered approach combining federal legislation, state action, regulatory enforcement, and international coordination. The solutions presented here draw on evidence from state-level experiments, international models (particularly the EU's GDPR), FTC enforcement experience, and academic research. No single reform is sufficient; effective change requires addressing the legal, economic, and institutional structures that sustain unregulated data brokerage.

## Solution 1: Comprehensive Federal Data Broker Registration and Transparency Act

**Description**: Require all companies that meet the legal definition of a data broker to register with a federal agency, disclose the types of data they collect, the sources of that data, the categories of purchasers, and the purposes for which data is sold. Registration must be renewed annually, and penalties for failure to register must be substantial.

**Evidence Base**:

- Vermont's 2018 data broker registration law demonstrated that registration is technically feasible but revealed that transparency alone does not change behavior (Vermont Secretary of State, 2024)
- California's CCPA/CPRA registration requirement identified 530+ brokers (CA AG, 2025)
- The FTC's 2014 report recommended registration as a first step toward regulation

**Implementation**:

- Define "data broker" broadly: any entity that collects, aggregates, or sells personal data on individuals with whom it has no direct consumer relationship
- Designate the FTC (or a new federal privacy agency) as the registration authority
- Require annual filings disclosing data categories, sources, purchasers, retention periods, and security practices
- Make registration public and searchable
- Registration fee scaled to company revenue

**Estimated Cost**: $50-100 million annually for federal enforcement; fees from brokers would partially offset costs

**Timeline**: Passage within 1-2 years; implementation within 1 year of enactment

**Challenges**: Industry will argue for narrow definitions that exclude many brokers; First Amendment challenges possible

**Impact Metrics**: Number of registered brokers; completeness of disclosures; consumer use of registry

---

## Solution 2: Opt-In Consent for Data Collection and Sale

**Description**: Replace the current opt-out framework with an opt-in requirement: data brokers may not collect, aggregate, or sell personal data without the affirmative, informed consent of the individual. Consent must be specific (not bundled with terms of service), freely given, and revocable at any time.

**Evidence Base**:

- GDPR's consent requirements have been in effect since 2018, demonstrating that opt-in frameworks are operational at scale (European Data Protection Board annual reports)
- Research shows opt-out systems have less than 1% participation because the burden falls on consumers who are unaware they are being tracked (Consumer Reports, 2023)
- Behavioral economics literature demonstrates that default settings determine outcomes; opt-in vs. opt-out dramatically affects participation rates (Thaler and Sunstein, *Nudge*, 2008)

**Implementation**:

- Require affirmative opt-in before any collection or sale of personal data for non-essential purposes
- Consent must be granular: separate for each category of data and each category of use
- Consent cannot be bundled with access to a service ("take it or leave it" prohibited)
- Consent must be revocable, and revocation must take effect within 30 days
- Exception for data necessary to complete a transaction the consumer initiated

**Estimated Cost**: Industry compliance costs: $5-15 billion industry-wide (industry estimates likely inflated; GDPR compliance was significantly below industry predictions)

**Timeline**: Legislation in 2-3 years; 2-year implementation period

**Challenges**: Industry opposition will be intense; First Amendment challenges; need to define "meaningful consent" clearly

**Impact Metrics**: Consent rates by data category; reduction in data broker records; consumer awareness surveys

---

## Solution 3: Government Data Purchase Warrant Requirement

**Description**: Require government agencies at all levels (federal, state, local) to obtain a warrant based on probable cause before purchasing or otherwise acquiring personal data from data brokers that would otherwise require a warrant to obtain directly. This closes the constitutional loophole exposed by *Carpenter v. United States* (2018).

**Evidence Base**:

- *Carpenter v. United States*, 585 U.S. 296 (2018), required warrants for historical cell-site location data, recognizing that commercial data can reveal intimate details of a person's life
- Georgetown Law's "American Dragnet" (2022) documented extensive warrantless government data purchases
- ODNI's own 2023 report acknowledged that commercially available data "can be as revealing as content" of communications
- The Fourth Amendment It's Not Complicated Act (proposed multiple times by Sen. Wyden) would require warrants for government data purchases

**Implementation**:

- Prohibit federal, state, and local agencies from purchasing personal data from data brokers without a warrant
- Define covered data broadly: location data, communications metadata, financial data, health data, biometric data, and any other data that reveals personal behavior or associations
- Exceptions only for: publicly available government records, data voluntarily provided directly to the agency, and genuine emergency situations with after-the-fact judicial review
- Establish an annual transparency report on government data purchase warrants
- Provide a suppression remedy: data obtained in violation cannot be used as evidence

**Estimated Cost**: Minimal additional cost for agencies (warrant process already exists); some reduction in agency data procurement spending

**Timeline**: Legislation in 1-2 years (bipartisan support plausible)

**Challenges**: Intelligence community and law enforcement opposition; classification of national security data purchases complicates oversight

**Impact Metrics**: Number of data purchase warrants issued; reduction in warrantless data procurement contracts; court challenges and outcomes

---

## Solution 4: Individual Data Rights (Access, Correction, Deletion, Portability)

**Description**: Establish enforceable federal rights for individuals to access, correct, delete, and port their personal data held by data brokers. Modeled on GDPR Articles 15-20 but adapted to the US legal framework.

**Evidence Base**:

- GDPR's individual rights framework has been operational since 2018 across 27 EU member states
- California's CCPA/CPRA provides deletion and access rights; enforcement has revealed operational feasibility (CA AG enforcement reports)
- California's Delete Act (SB 362, 2023) creates a centralized opt-out mechanism, addressing the burden of individual requests

**Implementation**:

- **Right of access**: Data brokers must provide, within 30 days and at no cost, a complete accounting of personal data held, its sources, and who has purchased it
- **Right of correction**: Consumers may require correction of inaccurate data; corrections must be propagated to all entities that received the data
- **Right of deletion**: Consumers may require deletion of their data; brokers must delete within 30 days and cease re-acquisition from previous sources
- **Right of portability**: Consumers may request their data in a machine-readable format for transfer to another service
- **Centralized mechanism**: Create a federal "data rights portal" (similar to California's Delete Act) enabling consumers to exercise rights across all registered brokers through a single request
- **Anti-retaliation**: Brokers may not charge higher prices or degrade service for consumers who exercise their rights

**Estimated Cost**: $200-500 million for federal portal development and maintenance; industry compliance costs: $3-8 billion

**Timeline**: Legislation in 2-3 years; 18-month implementation; centralized portal operational within 3 years

**Challenges**: Technical complexity of centralized deletion; brokers may claim data is "de-identified" and therefore exempt; re-acquisition from new sources

**Impact Metrics**: Number of access/deletion/correction requests; request fulfillment rates; reduction in broker-held records over time

---

## Solution 5: Prohibition on Sale of Sensitive Data Categories

**Description**: Ban the sale of specific categories of highly sensitive personal data by data brokers, with narrow exceptions for regulated uses. Sensitive categories include precise geolocation data, health data, biometric data, data revealing sexual orientation or gender identity, data on minors, and financial vulnerability indicators.

**Evidence Base**:

- Duke University (2023) documented the sale of mental health data by data brokers with no restrictions
- FTC enforcement actions against Kochava and X-Mode/Outlogic demonstrated harms from sale of sensitive location data
- GDPR Article 9 restricts processing of "special categories" of personal data
- Illinois BIPA's restrictions on biometric data have been effective and survived legal challenges

**Implementation**:

- Define sensitive data categories: health (including inferences), precise geolocation (within 1,000 feet), biometric data, sexual orientation/gender identity, minor status, financial vulnerability, religious affiliation, political affiliation, and immigration status
- Prohibit sale of sensitive data except with explicit consent for a specific, disclosed purpose
- No exceptions for "de-identified" data that can be reasonably re-identified
- Heightened penalties for violations involving sensitive data
- Private right of action for individuals whose sensitive data is sold without consent

**Estimated Cost**: Modest enforcement costs; industry revenue loss concentrated in high-harm data categories

**Timeline**: Legislation in 1-2 years (strong public support for protecting sensitive data)

**Challenges**: Defining "sensitive" versus "non-sensitive" data boundaries; industry will argue all data is useful and restrictions are overbroad; inference problem (sensitive data can be inferred from non-sensitive data)

**Impact Metrics**: Reduction in availability of sensitive data on broker markets; FTC/state AG enforcement actions; private litigation outcomes

---

## Solution 6: Federal Data Privacy Agency

**Description**: Establish a dedicated federal agency (or elevate FTC authority) with specific jurisdiction over data broker regulation, rulemaking authority, and adequate enforcement resources.

**Evidence Base**:

- 130+ countries have dedicated data protection authorities (UNCTAD, 2024)
- The EU's supervisory authority structure under GDPR has enabled proactive enforcement
- The FTC's current enforcement-only authority limits its ability to regulate proactively; it can only pursue case-by-case enforcement of "unfair or deceptive" practices
- Multiple bipartisan proposals have recommended a federal privacy agency or enhanced FTC authority

**Implementation**:

- Option A: Create a standalone Federal Data Protection Agency with rulemaking, enforcement, and adjudicatory authority
- Option B: Grant the FTC specific rulemaking authority over data brokers and commercial data practices, with dedicated funding and staffing
- Either option must include: rulemaking authority, civil penalty authority (up to 4% of annual revenue for serious violations), investigation and subpoena powers, annual reporting requirements, and interagency coordination with state attorneys general
- Staffing: 500-1,000 personnel (comparable to CFPB at startup)
- Budget: $300-500 million annually

**Estimated Cost**: $300-500 million annually (offset by fines and registration fees)

**Timeline**: Legislation in 2-4 years; agency operational within 2 years of enactment

**Challenges**: Jurisdictional disputes with existing agencies (FTC, CFPB, state AGs); industry will lobby for weak agency with limited authority; political appointments could undermine effectiveness

**Impact Metrics**: Number of enforcement actions; rules promulgated; industry compliance rates; consumer complaint resolution times

---

## Solution 7: Data Minimization and Purpose Limitation Requirements

**Description**: Require data brokers to collect only the minimum data necessary for disclosed purposes and to use data only for the purposes specified at the time of collection.

**Evidence Base**:

- GDPR's data minimization (Article 5(1)(c)) and purpose limitation (Article 5(1)(b)) principles have been enforceable since 2018
- Research demonstrates that companies routinely collect far more data than needed for their stated purposes (FTC 2014 report)
- Data minimization reduces breach risk by limiting the data available to be stolen

**Implementation**:

- Brokers must specify the purpose of data collection before collecting it
- Collection must be limited to what is "reasonably necessary" for the stated purpose
- Data may not be used for purposes incompatible with the original collection purpose without new consent
- Data must be deleted when no longer necessary for the stated purpose (maximum retention periods by data category)
- Annual audits of data holdings to verify compliance

**Estimated Cost**: Industry compliance costs: $2-5 billion (significantly reduces storage and processing costs long-term)

**Timeline**: Legislation in 2-3 years; 2-year implementation

**Challenges**: Defining "reasonably necessary"; enforcement requires technical expertise; industry will resist restrictions on data reuse

**Impact Metrics**: Reduction in average data points per consumer profile; data retention periods; audit findings

---

## Solution 8: Private Right of Action with Statutory Damages

**Description**: Grant individuals a private right of action to sue data brokers for violations of data protection requirements, with statutory minimum damages to make litigation economically viable.

**Evidence Base**:

- Illinois BIPA's private right of action has been the most effective US data privacy enforcement mechanism, resulting in billions in settlements (including $650 million Facebook settlement, 2021)
- Without private enforcement, government agencies lack the resources to police the entire industry
- GDPR includes both regulatory enforcement and private litigation rights

**Implementation**:

- Any individual whose data rights are violated may sue in federal or state court
- Statutory damages: $100-1,000 per violation per individual (higher for knowing or reckless violations)
- Class action availability for widespread violations
- Attorney's fees and costs awarded to prevailing plaintiffs
- Safe harbor for brokers that demonstrate good-faith compliance with the law
- 2-year statute of limitations from discovery of the violation

**Estimated Cost**: No government cost; industry faces litigation risk proportional to violations

**Timeline**: Included in comprehensive legislation; effective upon enactment

**Challenges**: Industry strongly opposes private right of action; concerns about "litigation abuse" (but BIPA experience shows manageable); need for safe harbor to address good-faith compliance

**Impact Metrics**: Number of private lawsuits filed; settlement and judgment amounts; deterrent effect on industry behavior

## International Models

### European Union (GDPR)

| Feature | GDPR Provision | US Applicability |
|---------|---------------|-----------------|
| Consent requirements | Article 6-7: Consent must be freely given, specific, informed, unambiguous | Directly applicable -- strongest model for opt-in |
| Data minimization | Article 5(1)(c): Data limited to what is necessary | Directly applicable |
| Individual rights | Articles 15-22: Access, correction, deletion, portability, objection | Directly applicable |
| Purpose limitation | Article 5(1)(b): Data used only for specified purposes | Directly applicable |
| Data protection officers | Article 37-39: DPOs required for certain processors | Adaptable to larger US brokers |
| Enforcement | Fines up to 4% of global annual revenue | Strong model; higher than current US penalties |
| Supervisory authorities | Independent regulators in each member state | Model for federal privacy agency |

### California (CCPA/CPRA + Delete Act)

| Feature | California Approach | Scalability |
|---------|-------------------|-------------|
| Data broker registration | Required; 530+ registered | Proven feasible at state scale |
| Opt-out right | Consumer right to opt out of data sale | Operational; limited by consumer burden |
| Delete Act centralized opt-out | Single mechanism for all registered brokers | Innovative; model for federal portal |
| Private right of action | Limited to data breaches under CCPA | BIPA model (Illinois) is stronger |
| Enforcement | AG enforcement + Privacy Protection Agency | First state privacy agency in US |

### Other International Models

| Country | Key Feature | Relevance |
|---------|-------------|-----------|
| **Brazil (LGPD)** | Consent-based framework with national authority | Model for developing country with large digital economy |
| **Japan (APPI)** | Opt-out registry for third-party data transfers | Model for centralized opt-out |
| **South Korea (PIPA)** | One of strictest consent requirements globally | Demonstrates economic compatibility |
| **India (DPDPA 2023)** | Consent managers; data fiduciary obligations | Emerging model for large-scale implementation |

## Sequencing Strategy

### Phase 1 (Year 1-2): Foundation

1. **Federal data broker registration** -- bipartisan support likely; establishes transparency
2. **Government data purchase warrant requirement** -- bipartisan appeal (privacy hawks on both sides)
3. **Sensitive data sale prohibition** -- high public support; narrow scope easier to pass

### Phase 2 (Year 2-4): Comprehensive Framework

4. **Individual data rights (access, correction, deletion)** -- builds on state models
5. **Federal privacy agency or enhanced FTC authority** -- institutional foundation for enforcement
6. **Data minimization and purpose limitation** -- requires enforcement infrastructure

### Phase 3 (Year 4-6): Full Implementation

7. **Opt-in consent requirement** -- most transformative but faces strongest opposition
8. **Private right of action** -- ultimate enforcement mechanism

## Related Topics

- [Data Brokers: Legislation](11-legislation.md) - Draft bill text implementing these solutions
- [Data Brokers: Roadmap](08-roadmap.md) - Implementation timeline
- [Government Surveillance: Solutions](../government-surveillance/07-solutions.md) - Complementary surveillance reforms
- [Privacy: Solutions](../07-solutions.md) - Broader privacy reform framework

## Document Navigation

- Previous: [Opposition](06-opposition.md)
- Next: [Roadmap](08-roadmap.md)
