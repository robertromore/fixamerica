---
freshness:
  last-reviewed: 2026-02-20
  data-year: 2025
  review-cycle: 6
  sections:
    - name: "Surveillance Authorities and Programs"
      data-year: 2025
    - name: "Oversight Mechanisms"
      data-year: 2025
    - name: "Data Purchases and Commercial Partnerships"
      data-year: 2025
    - name: "Local and State Surveillance"
      data-year: 2025
notes:
  - Track Section 702 reauthorization outcomes for updates.
  - Monitor FISC published opinions for new compliance findings.
  - Update government data purchase documentation as new investigations emerge.
sources:
  count: 22
  verified: 2026-02-20
  broken: 0
---

# Government Surveillance: Current State

## Surveillance Authorities and Programs

### Federal Surveillance Framework

| Authority | Statutory Basis | Scope | Oversight |
|-----------|----------------|-------|-----------|
| **FISA Traditional Orders** | 50 U.S.C. ss 1801-1812 | Individual surveillance warrants for agents of foreign powers | FISC approval required; congressional notification |
| **Section 702** | 50 U.S.C. ss 1881a (FISA Amendments Act 2008) | Warrantless collection targeting non-US persons abroad | FISC certifications; ODNI/DOJ compliance review; congressional reauthorization |
| **Executive Order 12333** | Presidential directive (1981, amended) | Foreign intelligence collection outside FISA framework | Executive branch self-oversight; minimal congressional visibility |
| **Pen Register/Trap & Trace** | 18 U.S.C. ss 3121-3127 | Communications metadata (numbers dialed, email headers) | Court order (lower than probable cause) |
| **National Security Letters** | 18 U.S.C. ss 2709; 12 U.S.C. ss 3414; 50 U.S.C. ss 1862 | Financial records, telephone records, credit records | No judicial approval required; FBI self-issued |
| **Title III Wiretaps** | 18 U.S.C. ss 2510-2522 | Content of communications for criminal investigations | Federal court warrant based on probable cause |
| **Stored Communications Act** | 18 U.S.C. ss 2701-2712 | Stored email, social media data | Warrant (content), subpoena (metadata), or court order |
| **CALEA** | 47 U.S.C. ss 1001-1010 | Telecommunications carrier assistance to law enforcement | Carriers must build interception capabilities |
| **USA FREEDOM Act (2015)** | Amended 50 U.S.C. ss 1861 | Ended bulk telephony metadata collection under Section 215 | FISC amicus; declassification requirements |

### Section 702: The Central Controversy

Section 702 authorizes the intelligence community to target non-US persons reasonably believed to be located outside the United States for foreign intelligence purposes. Two primary collection programs operate under this authority:

| Program | Description | Scale | Relevance to Americans |
|---------|-------------|-------|----------------------|
| **PRISM** | Government requests stored communications data from tech companies (Google, Microsoft, Apple, Meta, etc.) | Thousands of selectors (email addresses, phone numbers) | Americans' communications with foreign targets collected |
| **Upstream** | Interception of internet communications as they transit backbone cables operated by AT&T, Verizon, etc. | Massive volume; collects communications "about" selectors | Higher incidental collection of Americans' data |

### Section 702 Statistics

| Metric | Value | Source |
|--------|-------|--------|
| Section 702 foreign targets (2023) | 246,073 | ODNI Annual Statistical Transparency Report (2024) |
| FBI queries of Section 702 data using US person identifiers (2022) | 119,383 | FISC opinion; ODNI compliance report (2023) |
| FBI queries of Section 702 data using US person identifiers (2021) | ~3.4 million (revised methodology) | ODNI; this number included duplicates and batch queries |
| FISA probable-cause orders issued (2023) | 353 | ODNI Statistical Transparency Report (2024) |
| NSLs issued (2022) | ~15,000 (estimated from disclosed ranges) | DOJ NSD annual reports |

### Executive Order 12333

EO 12333 governs the vast majority of foreign intelligence collection, much of which occurs outside US borders and outside the FISA framework:

- **Scope**: Far broader than FISA; authorizes collection of signals intelligence (SIGINT), human intelligence (HUMINT), and open-source intelligence (OSINT) worldwide
- **Oversight**: Primarily internal executive branch oversight (Attorney General guidelines, agency compliance officers)
- **Americans' data**: Americans' data collected "incidentally" under EO 12333 receives fewer protections than data collected under FISA/Section 702
- **Transparency**: Minimal; most EO 12333 collection remains classified with limited congressional visibility
- **Key concern**: The intelligence community can potentially route collection through EO 12333 to avoid FISA's more stringent requirements

### National Security Letters

| Metric | Value | Source |
|--------|-------|--------|
| NSLs issued annually (recent years) | 15,000-20,000 (estimated) | DOJ NSD reports; ODNI transparency reports |
| NSLs with gag orders | Majority include non-disclosure requirement | DOJ; ACLU litigation records |
| NSL challenges in court | Extremely rare; gag orders prevent recipients from disclosing | ACLU v. Holder, Doe v. Ashcroft |
| Types of records obtainable | Phone, email, financial, credit records | 18 U.S.C. ss 2709 and related statutes |

## Oversight Mechanisms

### Foreign Intelligence Surveillance Court (FISC)

| Metric | Value | Source |
|--------|-------|--------|
| FISC judges | 11 (appointed by Chief Justice of the Supreme Court) | 50 U.S.C. ss 1803 |
| FISC warrant applications approved (1979-2023) | 99.97% | FISC annual reports |
| FISC warrant applications denied outright (1979-2023) | 12 out of approximately 42,000+ | FISC annual reports; EPIC analysis |
| Published FISC opinions | Increasing since 2013 but still limited | FISC, ODNI declassification |
| FISC amicus curiae (post-USA FREEDOM Act) | Appointed in some significant cases | USA FREEDOM Act ss 401 |

**Key criticisms of FISC**:

- **Ex parte proceedings**: Government presents its case with no adversary
- **Rubber stamp**: 99.97% approval rate suggests inadequate scrutiny
- **Secret law**: FISC opinions interpreting surveillance authorities were classified for years
- **No appeal mechanism for targets**: Surveillance targets have no practical way to challenge collection
- **Chief Justice appointment**: Single individual (Chief Justice Roberts) selects all 11 judges

### Congressional Oversight

| Body | Jurisdiction | Assessment |
|------|-------------|------------|
| **Senate Select Committee on Intelligence (SSCI)** | Intelligence community oversight | Mixed record; constrained by classification; some members have pushed reforms |
| **House Permanent Select Committee on Intelligence (HPSCI)** | Intelligence community oversight | Increasingly partisan; oversight quality variable |
| **Senate Judiciary Committee** | FISA, civil liberties | Key role in Section 702 reauthorization debates |
| **House Judiciary Committee** | FISA, civil liberties | Bipartisan reform coalition has emerged at times |

**Key weaknesses of congressional oversight**:

- Members and staff cannot disclose classified information, even to constituents
- Intelligence community controls what information Congress sees
- Committee membership often includes surveillance supporters
- Reform proposals face procedural obstacles (must-pass deadline pressure for reauthorizations)
- Partisan dynamics increasingly override oversight functions

### Inspectors General

| IG Office | Role | Key Reports |
|-----------|------|-------------|
| DOJ Inspector General | Oversight of FBI surveillance activities | Report on FBI FISA application errors (2019, Crossfire Hurricane) |
| NSA Inspector General | Internal NSA compliance | Compliance incident reports |
| IC Inspector General | Intelligence community-wide | Whistleblower complaint handling |
| DHS Inspector General | DHS component surveillance | Reports on ICE data purchases, CBP practices |

### Privacy and Civil Liberties Oversight Board (PCLOB)

| Metric | Detail | Source |
|--------|--------|--------|
| Members | 5 (appointed by President, confirmed by Senate) | 42 U.S.C. ss 2000ee |
| Authority | Advisory; can review CT programs; access to classified information | Enabling statute |
| Key reports | Section 702 report (2014, updated); Section 215 report (2014) | PCLOB publications |
| Current status | Has experienced extended vacancies; quorum issues | Congressional reporting |

## Data Purchases and Commercial Partnerships

### Government-Commercial Data Pipeline

Federal agencies increasingly supplement surveillance authorities with commercial data purchases:

| Agency | Documented Purchases | Data Types | Source |
|--------|---------------------|------------|--------|
| ICE | Venntel (location data), Vigilant Solutions (ALPR), Thomson Reuters (utility records) | Location, license plates, utility records | Georgetown "American Dragnet" (2022) |
| CBP | Venntel, Babel Street (location data) | Cell phone location data | Sen. Wyden investigation (2020) |
| FBI | Multiple commercial data providers | Advertising data, location data, social media | Procurement records; Sen. Wyden (2023) |
| IRS | Venntel (location data) | Cell phone location data | *WSJ* (2020); IRS IG |
| DEA | License plate reader data, phone records | ALPR, communications metadata | ACLU FOIA (2020) |
| DHS | Social media monitoring (multiple vendors) | Social media posts, behavioral data | DHS PIAs (2022-2024) |
| Secret Service | Babel Street (location data) | Location data | *Vice Motherboard* (2020) |
| DIA | Commercial location and advertising data | Location, behavioral data | *NYT* (2021) |
| NSA | Commercial advertising data | Web browsing, advertising IDs | *WSJ* (2024) |

### Scale of Government Data Purchasing

| Metric | Value | Source |
|--------|-------|--------|
| Federal contracts for commercial data services (annual estimate) | $200+ million | USASpending.gov analysis; Tech Inquiry (2023) |
| Federal agencies documented purchasing commercial data | 20+ | Georgetown "American Dragnet" (2022) |
| State/local agencies with data broker subscriptions | Hundreds (number uncertain) | Brennan Center (2024) |

### Constitutional Issue

The ODNI Senior Advisory Group's own 2023 declassified report acknowledged:

> "Commercially available information (CAI) can be as revealing as content of communications... In the wrong hands, such data could be used to facilitate blackmail, stalking, harassment, and public shaming."

Despite this acknowledgment, no comprehensive warrant requirement exists for government data purchases.

## Local and State Surveillance

### Fusion Centers

| Metric | Value | Source |
|--------|-------|--------|
| Recognized fusion centers | 80+ | DHS fusion center program; GAO-13-233 |
| Federal funding for fusion centers | $300+ million since 2003 | Congressional Research Service (2023) |
| Privacy violations documented | Multiple (Senate Homeland Security investigation, 2012) | Senate PSI, "Federal Support for and Involvement in State and Local Fusion Centers" (2012) |

### Local Law Enforcement Surveillance Tools

| Tool | Description | Prevalence | Oversight |
|------|-------------|------------|-----------|
| **Stingray / IMSI catcher** | Mimics cell tower to intercept mobile data | 75+ agencies (known) | Minimal; NDA with FBI restricts disclosure |
| **Automated License Plate Readers (ALPR)** | Cameras reading and storing license plates | Thousands of agencies | Limited; some state laws restrict retention |
| **Facial recognition** | Searching photo databases for identification | Hundreds of agencies | Minimal federal regulation; some local bans |
| **Social media monitoring** | Tracking public social media posts | Widespread | Limited; some policies restrict |
| **Geofence warrants** | Requesting location data for all devices in an area | Growing use | Google and Apple ended compliance (2023-2024) |
| **Keyword warrants** | Requesting identity of users who searched specific terms | Documented but uncommon | Minimal oversight |
| **Predictive policing algorithms** | Algorithms predicting crime locations or individuals | Declining (some cities abandoning) | Growing criticism; some cities banning |
| **Ring/Neighbors partnerships** | Police accessing Amazon Ring camera footage | 2,000+ agency partnerships (2022) | Amazon policy changes; FOIA-resistant |
| **Drone surveillance** | Aerial surveillance using unmanned aircraft | Increasing (CBP, local agencies) | FAA rules; limited privacy regulation |

### Geographic Variation in Oversight

| Jurisdiction | Surveillance Oversight | Examples |
|-------------|----------------------|----------|
| **San Francisco, CA** | Strong: banned facial recognition by city agencies (2019) | Community Control Over Police Surveillance (CCOPS) ordinance |
| **Oakland, CA** | Strong: surveillance equipment transparency ordinance | Privacy Advisory Commission review |
| **New York, NY** | Mixed: POST Act requires NYPD surveillance technology disclosure | Some transparency; limited restrictions |
| **Portland, OR** | Strong: banned facial recognition (public and private use, 2020) | Broadest ban in the US |
| **Illinois** | Strong: BIPA restricts biometric data collection | Private right of action for biometric violations |
| **Most states** | Weak to nonexistent: no specific surveillance oversight laws | Agencies acquire and use tools without public disclosure |

## Recent Developments (2023-2025)

### Section 702 Reauthorization

- Section 702 was reauthorized in April 2024 after contentious debate
- The Reforming Intelligence and Securing America Act (RISAA) extended Section 702 for two years (through April 2026)
- **Key provisions**: New compliance requirements for FBI queries of US person data; expanded definition of "electronic communications service provider"
- **What failed**: Amendment requiring warrants for US person queries (failed by narrow vote); amendment restricting data purchases
- **Next reauthorization**: 2026 -- major opportunity for reform

### Government Data Purchase Restrictions

- Executive Order 14117 (February 2024): Restricted bulk transfer of sensitive data to "countries of concern" -- but did not restrict domestic government purchases
- Multiple bills introduced to require warrants for government data purchases (Fourth Amendment Is Not For Sale Act; Government Surveillance Reform Act)
- DNI declassified report acknowledging risks of commercial data (2023) -- but no policy changes followed

### Facial Recognition

- GAO report (2021) documented 20+ federal agencies using facial recognition with inadequate oversight
- Multiple cities have passed bans or moratoriums on government facial recognition
- Clearview AI continues to sell to law enforcement despite multiple lawsuits

### AI and Surveillance

- Growing use of AI-powered surveillance tools by federal and local agencies
- DHS expanding use of automated social media screening for visa applicants
- Predictive policing programs declining in some cities (Los Angeles abandoned PredPol in 2020) but expanding elsewhere

## The Gap Between Law and Reality

| Legal Framework Says | Reality Is |
|---------------------|-----------|
| Fourth Amendment protects against unreasonable searches | Government purchases commercial data to avoid warrant requirements |
| FISA requires court approval for surveillance of Americans | Section 702 and EO 12333 enable massive incidental collection |
| Congressional oversight ensures accountability | Intelligence community controls what Congress sees; oversight is often superficial |
| FISC provides judicial check | 99.97% approval rate; ex parte proceedings; secret law |
| Surveillance limited to foreign intelligence and criminal investigation | Fusion centers, social media monitoring, and predictive policing extend surveillance to communities and dissent |
| Whistleblowers can report abuse through proper channels | Whistleblowers face prosecution and retaliation |

## Sources

- ACLU, "Stingray Tracking Devices" (updated 2024)
- Brennan Center for Justice, "Government Use of Commercial Data" (2024)
- Congressional Research Service, "Fusion Centers" (2023)
- FISC, Annual Reports (2020-2024)
- GAO, "Facial Recognition Technology" (GAO-21-526, 2021)
- Georgetown Law Center on Privacy and Technology, "American Dragnet" (2022)
- ODNI, Annual Statistical Transparency Reports (2022-2024)
- ODNI, "Senior Advisory Group Report on Commercially Available Information" (2023)
- PCLOB, "Report on the Surveillance Program Operated Pursuant to Section 702" (2014, updated)
- Senate Permanent Subcommittee on Investigations, "Federal Support for and Involvement in State and Local Fusion Centers" (2012)
- USASpending.gov, federal contract data (2023-2024)

## Related Topics

- [Data Brokers: Current State](../data-brokers/02-current-state.md) - Data broker industry that government purchases from
- [Privacy: Current State](../02-current-state.md) - Broader privacy landscape
- [Political: Government Transparency](../../political/government-transparency/01-overview.md) - Classification and FOIA

## Document Navigation

- Previous: [Overview](01-overview.md)
- Next: [History](03-history.md)
