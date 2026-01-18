# Privacy: Current State

## Overview

Americans live under pervasive surveillance from both government and corporate entities, with legal protections that have not kept pace with technological change. The Fourth Amendment's prohibition on unreasonable searches was written for physical spaces and papers; courts have struggled to apply it to digital communications, location data, and the vast troves of information held by third parties. Meanwhile, the absence of comprehensive federal privacy legislation leaves most personal data collection and use unregulated.

## Constitutional Privacy Today

### Fourth Amendment Status

| Doctrine | Current Rule | Effect |
|----------|--------------|--------|
| **Third-party doctrine** | No expectation of privacy in data shared with third parties | Most digital data unprotected; *Carpenter* created exception |
| **Border exception** | Reduced Fourth Amendment protections at borders and ports of entry | Device searches routine; some circuits require suspicion for forensic searches |
| **National security exception** | FISA court authorizes surveillance | Secret oversight, broad scope |
| **Good faith exception** | Evidence admissible if police reasonably relied on warrant | Weak deterrence |
| ***Carpenter* exception** | Cell site location requires warrant | Narrow, unclear how far it extends |

### Key Supreme Court Cases

| Case | Year | Holding | Significance |
|------|------|---------|--------------|
| *Katz v. United States* | 1967 | Reasonable expectation of privacy standard | Modern Fourth Amendment test |
| *Smith v. Maryland* | 1979 | No privacy in phone numbers dialed | Third-party doctrine established |
| *United States v. Jones* | 2012 | GPS tracking requires warrant | Physical trespass theory revived |
| *Riley v. California* | 2014 | Warrant needed to search cell phone | Digital devices get protection |
| *Carpenter v. United States* | 2018 | Cell site location data requires warrant | Limited third-party doctrine |

### Post-*Carpenter* Uncertainty

| Data Type | Warrant Required? | Status |
|-----------|-------------------|--------|
| Cell site location (7+ days) | Yes | *Carpenter* holding |
| Real-time location tracking | Likely | Lower courts divided |
| IP address records | Unclear | Circuit split |
| Financial records | Probably not | Third-party doctrine |
| Email content (stored) | Generally yes (ECPA 180-day rule rarely applied in practice) | DOJ policy requires warrant for all email content |
| Smart home data | Unclear | No Supreme Court ruling |
| DNA from discarded items | No | Abandonment doctrine |

## Government Surveillance Programs

### National Security Agency (NSA)

| Program | Authority | Scope | Status |
|---------|-----------|-------|--------|
| **Section 702** | FISA Amendments Act | Foreign targets, incidental US collection | Active, reauthorized 2024 |
| **EO 12333** | Executive order | Foreign intelligence abroad | Active, minimal oversight |
| **PRISM** | Section 702 | Data from tech companies | Active |
| **Upstream** | Section 702 | Internet backbone collection | Active |
| **Call Detail Records** | Section 215 (ended) | Domestic phone metadata | Program ended 2019 |

### Section 702 Concerns

| Issue | Description |
|-------|-------------|
| **Incidental collection** | Americans' communications collected when talking to foreign targets |
| **Backdoor searches** | Querying collected data for US persons without warrant |
| **Scope creep** | Originally for terrorism, now broader national security |
| **Minimization failures** | Procedures to protect Americans inadequately followed |
| **FISA Court limitations** | Secret, one-sided, limited review capacity |

### FBI Surveillance

| Tool | Description | Annual Use (per ODNI/DOJ reports) |
|------|-------------|------------|
| **National Security Letters** | Compel communications records without court | 10,000+ (2022) |
| **FISA orders** | Surveillance of suspected foreign agents | 1,500+ (2022) |
| **Section 702 queries** | Searching NSA-collected data | 200,000+ (2022; 2024 reauthorization added some limits) |
| **Pen registers/trap-trace** | Real-time metadata collection | Thousands (not publicly aggregated) |
| **Undercover operations** | Infiltration, informants | Unknown |

### Local Law Enforcement

*Adoption figures are approximate; comprehensive data on police surveillance technology use is limited.*

| Technology | Adoption | Concerns |
|------------|----------|----------|
| **Automatic license plate readers** | Widespread (no comprehensive count) | Mass location tracking |
| **Facial recognition** | Growing; GAO found FBI and other agencies access state DMV photos (GAO-19-579) | Accuracy issues, bias |
| **Stingrays/cell site simulators** | Documented in many jurisdictions (often via NDAs) | Warrantless use, secrecy |
| **Social media monitoring** | Common (Brennan Center documented use in many cities) | Chilling effects |
| **Predictive policing** | Documented in dozens of jurisdictions; many programs discontinued | Bias amplification |
| **ShotSpotter/gunshot detection** | Over 100 cities (vendor claims, as of 2023) | False positives, mission creep |

### Fusion Centers

| Metric | Value |
|--------|-------|
| Number of centers | 80+ (per DHS) |
| Federal funding | Hundreds of millions annually |
| Data sources | Federal, state, local, private |
| Information sharing | Bidirectional |
| Oversight | Minimal, fragmented (per Senate investigations) |
| Civil liberties issues | Documented repeatedly (ACLU, Senate reports) |

## Government Data Purchases

### The Constitutional Circumvention

| Practice | Description | Constitutional Issue |
|----------|-------------|---------------------|
| **Location data purchases** | Buy from data brokers | Avoids warrant requirement |
| **Advertising data** | Real-time bidding information | No Fourth Amendment protection |
| **Utility data** | Smart meter, connected device data | Third-party doctrine loophole |
| **Financial data** | Transaction patterns | Not considered searches |

### Known Purchasers

| Agency | Data Types | Purpose |
|--------|------------|---------|
| **ICE** | Location from Venntel, Babel Street | Immigration enforcement |
| **CBP** | Location, travel patterns | Border security |
| **IRS** | Location, financial | Tax enforcement |
| **DEA** | Call records, location | Drug investigations |
| **DHS** | Various commercial data | Multiple purposes |
| **Military/intelligence** | Location, social media | Unclear |

### Scale of Purchases

| Data Type | Annual Government Spending | Sources |
|-----------|---------------------------|---------|
| Location data | $10+ million | Venntel, Babel Street, others |
| Social media monitoring | Unknown | Multiple vendors |
| People search services | Unknown | LexisNexis, etc. |
| Facial recognition | Unknown | Clearview AI (contested) |

## Corporate Surveillance

### Data Collection Ecosystem

*Scale figures are approximate, based on company disclosures (2023-2024) and vary by product.*

| Collector | Data Types | Scale (approx.) |
|-----------|------------|-------|
| **Google** | Search, location, email, browsing, YouTube | Billions of users (global) |
| **Meta** | Social, messaging, browsing (pixels) | Billions of users (global) |
| **Amazon** | Purchases, Alexa, Ring, browsing | Hundreds of millions of users (global) |
| **Apple** | Device usage, location, payments | Billions of devices (global) |
| **Microsoft** | Productivity, LinkedIn, gaming | Billions of users (global) |
| **Data brokers** | Everything aggregated | Hundreds of millions of profiles (US) |

### Data Broker Industry

| Metric | Value | Source |
|--------|-------|--------|
| Registered brokers (California) | 500+ | CA AG Data Broker Registry (2024) |
| Total brokers (US, estimated) | Many more unregistered | Industry is fragmented |
| Data points per person | Hundreds to thousands | Varies by broker |
| Accuracy | Variable, often wrong | FTC and academic studies |
| Consumer knowledge | Very low | Pew Research (2023) |
| Federal regulation | Minimal | No comprehensive federal law |

### Major Data Brokers

*Profile counts are company claims or industry estimates; independently verifying scale is difficult.*

| Company | Specialization | Data Held (claimed/estimated) |
|---------|---------------|-----------|
| **Acxiom** | Marketing data | Billions of profiles globally |
| **Experian** | Credit, marketing | Billions of profiles globally |
| **Oracle** | Digital advertising | Extensive (exited ad business 2024) |
| **LexisNexis** | Risk, people search | Hundreds of millions of identities |
| **Equifax** | Credit, employment | Hundreds of millions of consumers |
| **CoreLogic** | Property, mortgage | Extensive property records (US) |

### Location Data Specifically

| Source | Collection Method | Accuracy |
|--------|-------------------|----------|
| **Mobile apps** | SDK integration | Meters |
| **Carriers** | Cell tower triangulation | Varies |
| **WiFi** | Access point detection | Building-level |
| **Advertising exchanges** | Real-time bidding | Varies |
| **Connected vehicles** | GPS, telematics | Meters |

## Sectoral Privacy Status

### Medical Privacy (HIPAA)

| Protected | Not Protected |
|-----------|---------------|
| Healthcare provider records | Health apps (Fitbit, etc.) |
| Health insurance information | Period tracking apps |
| Healthcare clearinghouse data | Genetic testing (23andMe) |
| Business associates | Health data sold to brokers |

**Post-*Dobbs* Concerns:**

- Period tracking apps as evidence
- Location data showing clinic visits
- Search history as evidence
- State demands for out-of-state records

### Financial Privacy

| Law | Protection | Limitation |
|-----|------------|------------|
| **GLBA** | Notice and opt-out | Weak, easily bypassed |
| **FCRA** | Credit report access | Narrow scope |
| **RFPA** | Bank record protection | Government exceptions |
| **Bank Secrecy Act** | N/A (requires reporting) | Anti-privacy |

### Workplace Privacy

| Monitoring Type | Legal Status | Prevalence |
|-----------------|--------------|------------|
| **Email monitoring** | Generally legal | Majority of employers (AMA surveys) |
| **Keystroke logging** | Generally legal | Increasing |
| **Screen monitoring** | Generally legal | Common (especially remote work) |
| **Video surveillance** | Legal (most areas) | Common |
| **Location tracking** | Legal (company devices) | Common |
| **Social media screening** | Varies by state | Majority of employers (SHRM surveys) |
| **Drug testing** | Legal (most jobs) | Common (varies by industry) |

### Children's Privacy (COPPA)

| Protected | Gap |
|-----------|-----|
| Children under 13 online | Children 13-17 unprotected |
| Parental consent required | Consent easily faked |
| Data collection limits | Enforcement weak |
| | Educational technology exemption |
| | Connected toy loopholes |

## State Privacy Laws

### Comprehensive State Laws (as of January 2025)

*At least 19 states have enacted comprehensive privacy laws per IAPP tracking.*

| State | Law | Effective | Key Features |
|-------|-----|-----------|--------------|
| California | CPRA | 2023 | Strongest; dedicated agency; private right for breaches |
| Virginia | CDPA | 2023 | Business-friendly; AG enforcement only |
| Colorado | CPA | 2023 | Universal opt-out mechanism |
| Connecticut | CTDPA | 2023 | Strong consumer rights |
| Utah | UCPA | 2023 | Business-friendly; higher thresholds |
| Iowa | ICDPA | 2025 | Limited scope |
| Indiana | ICDPA | 2026 | Limited scope |
| Tennessee | TIPA | 2025 | Business-friendly |
| Montana | MCDPA | 2024 | Lower thresholds; broader coverage |
| Oregon | OCPA | 2024 | Strong provisions; nonprofit coverage |
| Texas | TDPSA | 2024 | Large state; no revenue threshold |
| Delaware | DPDPA | 2025 | Strong consumer rights |
| New Jersey | DPL | 2025 | Strong provisions |
| New Hampshire | SB 255 | 2025 | Standard provisions |
| Maryland | MODPA | 2025 | Data minimization focus |
| Kentucky | KCDPA | 2026 | Standard provisions |
| Minnesota | MCDPA | 2025 | Strong provisions |
| Nebraska | NDPA | 2025 | Standard provisions |
| Rhode Island | RIDPA | 2026 | Standard provisions |

*Note: Florida enacted a narrow law (FDBR) limited to specific sectors. Additional states have laws effective 2026+.*

### Coverage Variations

| Element | Stronger (CA) | Weaker (UT) |
|---------|-------------|-----------|
| Business threshold | $25M revenue OR 100K consumers OR 50% data revenue | $25M revenue AND (100K consumers OR 25K consumers if 50% data revenue) |
| Consumer rights | Access, delete, correct, port, opt-out, limit use | Fewer rights; narrower scope |
| Sensitive data | Heightened protection; opt-in consent | Basic protections |
| Private right of action | Limited (data breaches only) | None |
| Enforcement | Dedicated agency (CPPA) | AG only |
| Opt-out mechanisms | Global Privacy Control honored | Limited recognition |

### Biometric Privacy Laws

| State | Law | Private Right of Action |
|-------|-----|------------------------|
| Illinois | BIPA | Yes ($1,000-$5,000 per violation) |
| Texas | CUBI | No (AG only) |
| Washington | HB 1493 | No |

## International Comparison

### US vs. GDPR

| Element | US | EU (GDPR) |
|---------|-----|-----------|
| Legal basis | Sectoral, state patchwork | Comprehensive; requires lawful basis (consent, contract, legitimate interest, legal obligation, vital interest, or public task) |
| Default | Opt-out (if available) | Lawful basis required before processing; consent must be affirmative where relied upon |
| Rights | Limited, varies | Extensive, uniform |
| Enforcement | Weak, fragmented | Strong, coordinated |
| Fines | Low, inconsistent | Up to 4% global revenue |
| DPA resources | FTC understaffed | Well-funded authorities |
| Private action | Mostly unavailable | Available |

### US vs. Other Democracies

| Country | Framework | US Comparison |
|---------|-----------|---------------|
| **Canada** | PIPEDA | More protective |
| **UK** | UK GDPR | Much more protective |
| **Australia** | Privacy Act | More protective |
| **Japan** | APPI | More protective |
| **Brazil** | LGPD | More protective |
| **South Korea** | PIPA | Much more protective |

## Recent Developments

### Legislative Activity

| Development | Status | Significance |
|-------------|--------|--------------|
| ADPPA (federal privacy bill) | Stalled | Would preempt state laws |
| Section 702 reauthorization | Passed April 2024 | Extended authority; no broad warrant requirement for US person queries adopted |
| Kids Online Safety Act | Pending | Child protection focus |
| State law expansion | Ongoing | 19+ states enacted comprehensive laws |

### Judicial Developments

| Case/Development | Impact |
|------------------|--------|
| *Carpenter* applications | Lower courts expanding/limiting |
| Geofence warrant challenges | Some courts skeptical |
| Keyword warrant scrutiny | Emerging challenges |
| State constitution rulings | Some stronger protections |

### Technology Developments

| Technology | Privacy Impact |
|------------|----------------|
| **AI/ML** | Enables inference, profiles |
| **Connected vehicles** | Pervasive location, behavior |
| **Smart home** | Interior surveillance |
| **Wearables** | Health, location, biometric |
| **Generative AI** | Training on personal data |

---

## Document Navigation

- Previous: [Overview](01-overview.md)
- Next: [History](03-history.md)
- Up: [Overview](01-overview.md)
