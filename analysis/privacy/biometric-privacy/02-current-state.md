---
freshness:
  last-reviewed: 2026-02-20
  data-year: 2025
  review-cycle: 6
---

# Biometric Privacy: Current State

## Biometric Technology Landscape

### Facial Recognition

**Government Use**:

| Agency/Entity | System | Database Size | Source |
|---------------|--------|---------------|--------|
| FBI (FACE Services) | Next Generation Identification | 641+ million photos | GAO-19-579 (2019) |
| CBP | Traveler Verification Service | 270+ million encounters | CBP operational statistics (2024) |
| ICE | Facial recognition via contractors | Access to billions of photos | Georgetown Law CPPT reports (2023) |
| TSA | CAT-2 identity verification | Deployed at 200+ airports | TSA public statements (2024) |
| State DMVs | License photo databases | 640+ million images | GAO-19-579 (2019) |
| Local law enforcement | Various (Clearview AI, FACE, state systems) | Varies by jurisdiction | Varies |

**Commercial Use**:

| Application | Companies | Scale |
|-------------|-----------|-------|
| Phone unlock / authentication | Apple (Face ID), Samsung, Google | 1+ billion devices |
| Social media photo tagging | Meta (formerly), Google Photos | Billions of photos |
| Retail analytics | Walgreens, Rite Aid (discontinued), Macy's | Thousands of stores |
| Payments | Amazon One (palm), Mastercard | Growing deployment |
| Access control | Verkada, Genetec, Honeywell | Commercial buildings |
| Event venue security | Ticketmaster, MSG Entertainment | Stadiums, arenas |

**Clearview AI**:

| Metric | Value | Source |
|--------|-------|--------|
| Images scraped | 30+ billion | Clearview AI public statements (2024) |
| Law enforcement clients | 3,100+ agencies (claimed) | Clearview AI public statements (2023) |
| Source of images | Social media, public websites | Company disclosures |
| GDPR fines received | 20+ million EUR (France, Italy, Greece, UK) | GDPR Enforcement Tracker (2024) |
| BIPA lawsuit status | Settlement pending | *ACLU v. Clearview AI* (N.D. Ill.) |

### Fingerprint Collection

| Context | Scale | Source |
|---------|-------|--------|
| FBI Integrated Automated Fingerprint Identification System (IAFIS) | 160+ million criminal fingerprints; 67+ million civil | FBI statistics (2024) |
| DHS IDENT/HART database | 260+ million unique identities | DHS privacy impact assessments (2024) |
| Smartphone fingerprint sensors | 1+ billion devices | Industry estimates |
| Employer timekeeping (biometric clocks) | Estimated 30+ million workers | Industry reports |
| TSA PreCheck enrollment | 15+ million | TSA statistics (2024) |

### Voice Recognition

| Application | Companies | Scale |
|-------------|-----------|-------|
| Voice assistants | Amazon Alexa, Google Assistant, Apple Siri | 200+ million devices in U.S. |
| Call center authentication | Nuance (Microsoft), Pindrop | Millions of calls daily |
| Voice banking | Wells Fargo, Chase, USAA | Millions of enrollees |
| Law enforcement voice analysis | Various vendors | Limited but growing |

### DNA Databases

| Database | Size | Authority | Source |
|----------|------|-----------|--------|
| FBI CODIS/NDIS | 21+ million profiles | DNA Identification Act (1994) | FBI CODIS statistics (2024) |
| Consumer DNA testing (total) | 40+ million Americans tested | Voluntary (23andMe, Ancestry) | MIT Technology Review (2024) |
| Familial DNA searching | Used in 30+ states | State policy varies | Forensic Genealogy research |
| Rapid DNA systems | 200+ booking stations | Rapid DNA Act (2017) | FBI/DOJ reports (2024) |

### Emerging Biometric Technologies

| Technology | Description | Deployment Status |
|------------|-------------|------------------|
| Gait recognition | Identifies individuals by walking pattern | Research/limited military deployment |
| Emotion recognition | Attempts to detect emotional states from facial expressions | Controversial; some commercial deployment |
| Palm vein recognition | Reads vein patterns through skin | Amazon One (stores, stadiums) |
| Behavioral biometrics | Typing patterns, mouse movements, device handling | Growing in financial services |
| Heartbeat recognition | Identifies individuals by cardiac signature | Military/intelligence research |

## Legal Landscape

### State Biometric Privacy Laws

#### Dedicated Biometric Privacy Statutes

| State | Law | Year | Private Right of Action | Key Provisions |
|-------|-----|------|------------------------|----------------|
| Illinois | BIPA (740 ILCS 14) | 2008 | Yes -- $1,000 negligent / $5,000 intentional per violation | Written consent required; retention schedule; no sale |
| Texas | CUBI (Tex. Bus. & Com. Code SS 503.001) | 2009 | No (AG enforcement only) | Notice and consent required; retention limits |
| Washington | HB 1493 (RCW 19.375) | 2017 | No (AG enforcement only) | Notice required; retention limits; commercial focus |

#### BIPA Enforcement and Litigation

| Metric | Value | Source |
|--------|-------|--------|
| BIPA lawsuits filed (cumulative through 2024) | 2,000+ | Bloomberg Law BIPA Litigation Tracker |
| Major settlements | $650M Facebook/Meta (2022); $228M TikTok (2024); $100M Google (2022) | Court records |
| Average BIPA settlement | $15-30 million | Bloomberg Law analysis (2024) |
| Illinois Supreme Court: per-violation damages | Confirmed in *Cothron v. White Castle* (2023) | 2023 IL 126892 |
| Illinois Supreme Court: 5-year statute of limitations | Confirmed in *Tims v. Black Horse Carriers* (2023) | 2023 IL 127801 |
| Estimated total BIPA liability exposure | $6+ billion (settled/judgment) | Bloomberg Law (2024) |

**Key BIPA Cases**:

| Case | Year | Outcome | Significance |
|------|------|---------|-------------|
| *Rosenbach v. Six Flags* (IL Sup. Ct.) | 2019 | No actual injury needed for standing | Eliminated key defense |
| *Patel v. Facebook* (9th Cir.) | 2020 | $650 million settlement upheld | Largest biometric privacy settlement |
| *Cothron v. White Castle* (IL Sup. Ct.) | 2023 | Each scan is separate violation | Dramatically increased potential damages |
| *Tims v. Black Horse Carriers* (IL Sup. Ct.) | 2023 | 5-year statute of limitations | Clarified filing window |
| *ACLU v. Clearview AI* (N.D. Ill.) | Pending | Settlement requiring restrictions on sales | First major case against facial recognition company |

#### Texas AG BIPA-Equivalent Enforcement

| Action | Year | Amount | Company |
|--------|------|--------|---------|
| Meta facial recognition settlement | 2024 | $1.4 billion | Meta (Facebook) |
| Google biometric data action | 2024 | $8.5 million | Google |

#### States Including Biometrics in Comprehensive Privacy Laws

All 19 states with comprehensive privacy laws classify biometric data as "sensitive data" requiring opt-in consent or heightened protections, including California (CPRA), Virginia (VCDPA), Colorado (CPA), Connecticut (CTDPA), and Texas (TDPSA).

### Federal Landscape

**No federal biometric privacy law exists.** Biometric data receives no dedicated federal protection.

**Relevant Federal Authorities**:

| Authority | Application to Biometrics | Limitation |
|-----------|--------------------------|------------|
| FTC Act Section 5 | Deceptive practices involving biometric data | No specific biometric requirements |
| COPPA | Children's biometric data online | Limited to children under 13 online |
| ADA | Disability-related biometric screening | Limited to disability context |
| HIPAA | Biometric health data (covered entities only) | Does not cover most commercial biometric collection |
| Privacy Act (1974) | Federal agency biometric records | No private sector coverage |
| E-Government Act | Federal agency biometric privacy impact assessments | Procedural requirement only |

**Failed/Pending Federal Legislation**:

| Bill | Status | Key Provisions |
|------|--------|----------------|
| National Biometric Information Privacy Act | Introduced multiple Congresses; never advanced | BIPA-style federal law with PRA |
| Facial Recognition and Biometric Technology Moratorium Act | Introduced 2020, 2023; never advanced | Federal moratorium on government facial recognition |
| ADPPA/APRA biometric provisions | Stalled as part of broader privacy bills | Include biometric data as "sensitive data" |

### Local Government Actions

**Government Facial Recognition Bans**:

| Jurisdiction | Year | Scope |
|-------------|------|-------|
| San Francisco, CA | 2019 | City agency use banned |
| Oakland, CA | 2019 | City agency use banned |
| Berkeley, CA | 2019 | City agency use banned |
| Somerville, MA | 2019 | City agency use banned |
| Boston, MA | 2020 | City agency use banned |
| Portland, OR | 2020 | Government and private use banned |
| King County, WA | 2021 | County agency use banned |
| New York City, NY | 2021 | Commercial tenant facial recognition regulated |
| Baltimore, MD | 2022 | City agency use banned (expired; renewed debate) |
| Various other cities | 2019-2024 | At least 20 jurisdictions with restrictions |

## Accuracy and Bias

### Facial Recognition Error Rates

| Demographic Group | False Positive Rate | False Negative Rate | Source |
|-------------------|--------------------|--------------------|--------|
| Light-skinned males | 0.8% | Low | Buolamwini & Gebru, "Gender Shades" (2018) |
| Dark-skinned males | 12.0% | Higher | Buolamwini & Gebru (2018) |
| Light-skinned females | 7.0% | Moderate | Buolamwini & Gebru (2018) |
| Dark-skinned females | 34.7% | Highest | Buolamwini & Gebru (2018) |

**NIST FRVT (Face Recognition Vendor Test) 2024 Findings**:

- Top algorithms have improved significantly since 2018
- Demographic differentials persist, particularly for one-to-many matching
- Error rates remain higher for darker-skinned individuals in most algorithms
- Environment (lighting, angle, image quality) significantly affects performance
- "In the wild" performance substantially worse than controlled laboratory conditions

### Wrongful Identification Cases

| Individual | Year | Jurisdiction | Outcome |
|-----------|------|-------------|---------|
| Robert Williams | 2020 | Detroit, MI | Wrongfully arrested based on facial recognition; charges dropped |
| Michael Oliver | 2019 | Detroit, MI | Wrongfully arrested; charges dropped |
| Nijeer Parks | 2019 | Woodbridge, NJ | Wrongfully arrested; spent 10 days in jail; charges dismissed |
| Randal Reid | 2022 | Jefferson Parish, LA | Wrongfully arrested; held 6 days in another state |
| Porcha Woodruff | 2023 | Detroit, MI | Wrongfully arrested while pregnant; sued city |

All known wrongful arrest cases based on facial recognition have involved Black individuals.

## International Comparison

| Jurisdiction | Approach | Key Feature |
|-------------|----------|-------------|
| European Union (GDPR + AI Act) | Biometric data is "special category"; explicit consent required; AI Act restricts real-time remote biometric identification | Strongest comprehensive protection |
| United Kingdom | GDPR UK equivalent; ICO guidance on biometric data | Consent required; enforcement growing |
| Canada | PIPEDA treats biometrics as sensitive; Privacy Commissioner investigations | Consent framework |
| Australia | Privacy Act includes biometric data; no specific biometric law | Under reform |
| China | Personal Information Protection Law includes biometric protections | Strong law; weak enforcement against government |
| Illinois (BIPA) | Consent, no sale, retention/destruction, private right of action | Strongest enforcement through PRA |

## Trends

- **BIPA litigation continues expanding**: *Cothron v. White Castle* (2023) ruling that each scan constitutes a separate violation dramatically increased potential damages, driving more filings and settlements
- **State comprehensive laws covering biometrics**: All 19 state privacy laws classify biometric data as sensitive; practical enforcement varies
- **Local facial recognition bans spreading**: 20+ jurisdictions have banned or restricted government facial recognition; movement continues
- **Commercial facial recognition retreating selectively**: Rite Aid banned from use (FTC, 2023); Meta discontinued face recognition tagging (2021); some retailers discontinuing
- **AI Act implications for U.S. companies**: EU AI Act (2024) restricts real-time biometric identification; affects U.S. companies operating in EU
- **Consumer DNA privacy concerns growing**: 23andMe financial troubles raised data security questions; familial DNA searching expanding
- **Emotion recognition science challenged**: Growing scientific consensus that facial expressions do not reliably indicate emotions; EU AI Act bans emotion recognition in some contexts
- **Biometric payment expanding**: Amazon One palm recognition, Mastercard biometric checkout expanding despite privacy concerns

## Document Navigation

- Previous: [Overview](01-overview.md)
- Next: [History](03-history.md)
- Up: [Biometric Privacy Overview](01-overview.md)
