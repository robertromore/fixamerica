---
freshness:
  last-reviewed: 2026-02-20
  data-year: 2025
  review-cycle: 6
  sections:
    - name: "Industry Structure and Market Size"
      data-year: 2025
    - name: "Types of Data Collected and Sold"
      data-year: 2025
    - name: "Government Data Purchases"
      data-year: 2025
    - name: "Regulatory Landscape"
      data-year: 2025
    - name: "Consumer Impact"
      data-year: 2025
notes:
  - Track new state data broker registration laws for updates.
  - Monitor FTC enforcement actions against data brokers.
  - Update government data purchase documentation as new FOIA releases emerge.
sources:
  count: 18
  verified: 2026-02-20
  broken: 0
---

# Data Brokers: Current State

## Industry Structure and Market Size

### Market Overview

The US data broker industry has grown into one of the largest segments of the digital economy, though its exact size is difficult to measure because many companies engage in data brokerage as part of broader operations.

| Metric | Value | Source |
|--------|-------|--------|
| Global data broker market size | $350+ billion (inclusive of data analytics and marketing data) | Statista, "Data Broker Industry Revenue Worldwide" (2024) |
| US data brokerage market estimate | $200+ billion | IBISWorld, "Data Processing and Hosting" market report (2024) |
| Number of data brokers (estimated) | 4,000+ in the US | Pew Research Center, based on industry analyses (2023) |
| California-registered data brokers | 530+ | CA AG Data Broker Registry (January 2025) |
| Vermont-registered data brokers | 375+ | VT Secretary of State Data Broker Registry (2024) |
| Major publicly traded data brokers | 20+ | SEC filings; includes Acxiom (now Infogroup/Data.com), TransUnion, Equifax, Experian, LexisNexis (RELX), Verisk |

### Major Industry Players

| Company | Primary Market | Revenue (FY 2024 est.) | Data Points Held |
|---------|---------------|----------------------|------------------|
| Experian | Credit, marketing | $6.6 billion | 1.4+ billion consumer records globally |
| Equifax | Credit, employment | $5.6 billion | 800+ million consumer profiles |
| TransUnion | Credit, insurance | $4.1 billion | 1+ billion consumer records |
| RELX (LexisNexis Risk) | Legal, risk | $9.4 billion (group) | 283+ billion records |
| Acxiom (IPG) | Marketing, analytics | $1.1 billion (est.) | 2.5+ billion consumer records |
| Oracle Data Cloud | Advertising | Revenue undisclosed (Oracle shut BlueKai marketplace 2024) | Billions of consumer profiles |
| Verisk Analytics | Insurance | $2.8 billion | Extensive property, auto, health datasets |
| CoreLogic | Real estate | $1.7 billion | 150+ million property records |
| Kochava | Mobile advertising | Revenue undisclosed | Billions of mobile device records |
| Clearview AI | Law enforcement, facial recognition | Revenue undisclosed | 40+ billion facial images |

Sources: Company annual reports, SEC filings, FY 2023-2024.

### Business Model Categories

| Category | Description | Examples | Primary Customers |
|----------|-------------|----------|-------------------|
| **Credit bureaus** | Collect credit and financial data; operate under FCRA | Equifax, Experian, TransUnion | Lenders, insurers, employers |
| **Marketing data brokers** | Compile consumer profiles for advertising targeting | Acxiom, Oracle Data Cloud, LiveRamp | Advertisers, marketers |
| **People-search sites** | Provide individual lookup services to consumers | Spokeo, BeenVerified, WhitePages, Intelius | Individuals, private investigators, landlords |
| **Risk and fraud brokers** | Sell data for identity verification and fraud detection | LexisNexis Risk, TransUnion, ID Analytics | Financial institutions, government |
| **Location data brokers** | Aggregate and sell mobile location data | Safegraph, Placer.ai, X-Mode/Outlogic, Venntel | Advertisers, government agencies, real estate |
| **Health data brokers** | Compile health-related consumer data | Iqvia, LexisNexis Health, Optum | Pharma companies, insurers, researchers |
| **Political data brokers** | Voter files enriched with consumer data | L2, Aristotle, TargetSmart, i360 | Political campaigns, PACs |

### Revenue Sources

| Revenue Stream | Share of Industry Revenue | Description |
|----------------|--------------------------|-------------|
| Marketing and advertising data | ~40% | Consumer profiles for ad targeting |
| Risk assessment and fraud detection | ~25% | Credit, insurance, employment screening |
| People-search and background checks | ~15% | Consumer-facing lookup services |
| Government and law enforcement | ~10% | Surveillance, investigation, verification |
| Health and pharmaceutical data | ~10% | Patient analytics, drug marketing |

Source: Industry estimates compiled from IBISWorld, market analyses (2024).

## Types of Data Collected and Sold

### Data Categories

| Category | Examples | Sources | Sensitivity |
|----------|----------|---------|-------------|
| **Identifying information** | Name, SSN, date of birth, addresses, phone numbers, email | Public records, financial institutions, apps | High |
| **Financial data** | Income estimates, credit scores, debt levels, purchase history | Credit bureaus, banks, retailers, apps | High |
| **Health-related data** | Prescription history, health conditions inferred from purchases, fitness data | Pharmacies, health apps, loyalty programs | Very high |
| **Location data** | GPS coordinates, cell tower data, Wi-Fi connections, check-ins | Mobile apps, carriers, Bluetooth beacons, connected vehicles | Very high |
| **Online behavior** | Browsing history, search queries, social media activity, app usage | Websites (cookies/pixels), apps (SDKs), ISPs | High |
| **Demographic data** | Age, gender, ethnicity, religion, education, marital status | Public records, surveys, inferred from behavior | Medium-High |
| **Political data** | Voter registration, party affiliation, donation history, issue interests | Voter files, FEC records, inferred from behavior | High |
| **Consumer interests** | Hobbies, travel habits, media consumption, brand preferences | Loyalty programs, purchase data, app usage | Medium |
| **Employment data** | Employer, job title, salary range, work history | LinkedIn, payroll processors, public filings | High |
| **Social connections** | Family members, roommates, associates, social network graphs | Public records, social media, contact lists from apps | High |
| **Vehicle data** | License plate, make/model, driving patterns, connected car telemetry | DMV records, ALPR cameras, automakers, insurance | High |

### Data Granularity

Brokers offer data at multiple levels of detail:

| Level | Description | Typical Use | Price Range |
|-------|-------------|-------------|-------------|
| **Individual record** | Data on a single identified person | Background check, skip tracing | $0.50-$25 per record |
| **Segmented list** | Thousands of records matching criteria (e.g., "pregnant women in Ohio") | Direct marketing campaigns | $0.02-$0.50 per record |
| **Behavioral segment** | Audience segments based on inferred interests or behaviors | Digital advertising targeting | CPM $1-$50 |
| **Real-time data feed** | Streaming location or behavioral data | Ad bidding, foot traffic analysis | Subscription $10K-$500K/year |
| **Enrichment service** | Adding data points to existing customer databases | CRM enhancement | $0.01-$0.10 per match |

Source: Industry pricing guides; FTC, "Data Brokers: A Call for Transparency and Accountability" (2014); updated estimates from Duke University (2023).

### Sensitive Data Sales

| Data Type | Available for Purchase | Documented Buyers | Source |
|-----------|----------------------|-------------------|--------|
| Mental health data | Yes -- including depression, anxiety, bipolar indicators | Pharma, insurers, data brokers | Duke University, "Data Brokers and the Sale of Americans' Mental Health Data" (2023) |
| Precise geolocation (near abortion clinics) | Yes -- available at individual level | Advertisers, political groups, government | *The Wall Street Journal*, SafeGraph reporting (2022) |
| Sexual orientation/identity inferences | Yes -- inferred from app usage and browsing | Advertisers | Mozilla Foundation, "Privacy Not Included" reports (2023) |
| Domestic violence shelter locations | Identified as available via people-search sites | Abusers, stalkers | National Network to End Domestic Violence (2023) |
| Military/veteran status with location | Yes -- available as marketing segments | Government contractors, researchers | Duke University, Sen. Ron Wyden investigations (2023) |
| Children's data (under 13) | Available despite COPPA restrictions | Advertisers (compliance gaps) | New Mexico AG v. Google complaint (2024) |

## Government Data Purchases

### Documented Federal Agency Purchases

| Agency | Data Types Purchased | Purpose | Source |
|--------|---------------------|---------|--------|
| **ICE** (Immigration and Customs Enforcement) | Location data (Venntel), license plate data (Vigilant Solutions), utility records | Immigration enforcement, tracking individuals | Georgetown Law, "American Dragnet" (2022); DHS OIG reports |
| **CBP** (Customs and Border Protection) | Cell phone location data (Venntel, Babel Street) | Border surveillance, tracking patterns | Sen. Wyden office investigation (2020); ACLU FOIA |
| **IRS** (Internal Revenue Service) | Cell phone location data (Venntel) | Tax enforcement investigations | *The Wall Street Journal* (2020); IRS IG report |
| **FBI** | Advertising data, social media data, location data | Criminal investigations, intelligence | Sen. Wyden investigations (2023); FBI procurement records |
| **DEA** (Drug Enforcement Administration) | License plate reader data, phone records | Drug trafficking investigations | ACLU FOIA requests (2020) |
| **DHS** (Department of Homeland Security) | Social media monitoring, location data | Threat assessment, visa vetting | DHS Privacy Impact Assessments (2022-2024) |
| **Secret Service** | Cell phone location data (Babel Street) | Protective intelligence | *Vice Motherboard* (2020) |
| **Defense Intelligence Agency** | Commercial location data, advertising data | Foreign intelligence | DIA memo obtained by *The New York Times* (2021) |

### Scale of Government Purchasing

| Metric | Value | Source |
|--------|-------|--------|
| Federal contracts for commercial data (annual) | $200+ million (estimated for data broker services specifically) | USASpending.gov analysis, Tech Inquiry (2023) |
| Number of federal agencies with documented data purchases | 20+ | Georgetown Law, "American Dragnet" (2022) |
| State and local agencies purchasing commercial data | Hundreds (specific number unknown) | Brennan Center for Justice, "Government Use of Commercial Data" (2024) |
| Warrant requirement for government purchases | None (per current DOJ interpretation) | DOJ Office of Legal Counsel memos; *Carpenter v. United States* left open |

### Constitutional Concerns

The government data purchase pipeline creates a constitutional end-run:

| Scenario | Direct Collection | Broker Purchase |
|----------|------------------|-----------------|
| Cell phone location history | Warrant required (*Carpenter v. United States*, 2018) | No warrant required (current practice) |
| Email content | Warrant required (4th Amendment) | Not typically available from brokers |
| Web browsing history | Uncertain (no clear ruling) | Freely purchasable |
| Financial transactions | Subpoena or warrant (*Miller*, but evolving) | Available from data enrichment brokers |
| Social media activity | Public posts accessible; private requires legal process | Aggregated and analyzed by commercial firms |

## Regulatory Landscape

### Federal Law

| Law | Scope | Relevance to Data Brokers | Gaps |
|-----|-------|--------------------------|------|
| **Fair Credit Reporting Act (FCRA)** (1970) | Consumer reporting agencies | Covers credit bureaus but not marketing data brokers | Narrow definition of "consumer report"; most broker activity falls outside FCRA |
| **Gramm-Leach-Bliley Act** (1999) | Financial institutions | Restricts sharing of financial data | Applies only to financial institutions, not downstream brokers |
| **HIPAA** (1996) | Covered health entities | Protects medical records at providers and insurers | Does not cover health data sold by apps, pharmacies to brokers |
| **COPPA** (1998, updated 2013) | Websites/apps targeting children under 13 | Requires parental consent for children's data | Weak enforcement; many brokers hold children's data anyway |
| **FTC Act Section 5** | Unfair or deceptive practices | FTC can pursue brokers for deceptive practices | No data broker-specific authority; requires proving "unfairness" or "deception" |
| **No comprehensive federal data broker law** | N/A | N/A | The fundamental gap in US law |

### State Laws

| State | Law | Year | Key Provisions |
|-------|-----|------|----------------|
| **Vermont** | Data Broker Registration Act (9 V.S.A. ch. 62) | 2018 | First state to require data broker registration; annual registration, disclosure of opt-out procedures |
| **California** | CCPA/CPRA data broker provisions | 2020/2023 | Data broker registration; consumer right to opt out of sale; "Delete Act" (SB 362, 2023) creating centralized opt-out |
| **Texas** | Data Broker Law (HB 4390) | 2023 | Registration requirement; consumer opt-out; AG enforcement |
| **Oregon** | Data Broker Registration (SB 1587) | 2024 | Registration, disclosure, opt-out mechanisms |
| **New Jersey** | Data Broker Transparency Act | 2024 | Registration, disclosure of data categories and sources |
| **19+ states** | Comprehensive privacy laws (various) | 2018-2025 | Varying data broker provisions within broader privacy frameworks |

Source: International Association of Privacy Professionals (IAPP) State Law Tracker (January 2025); National Conference of State Legislatures.

### FTC Enforcement Actions

| Year | Target | Action | Outcome |
|------|--------|--------|---------|
| 2012 | Spokeo | FCRA violations -- selling consumer profiles for employment screening | $800,000 fine |
| 2014 | LeapLab/Sitesearch | Selling consumer applications with SSNs to overseas scammers | Settlements, FTC complaint |
| 2016 | Turn Inc. | Tracking consumers who opted out via undisclosed methods | Consent order |
| 2022 | Kochava | Selling precise geolocation data revealing visits to sensitive locations | FTC lawsuit (ongoing as of 2025) |
| 2023 | X-Mode/Outlogic | Selling precise location data without consent | Consent order banning sale of sensitive location data |
| 2024 | InMarket | Geofencing and location data for advertising without adequate consent | Consent order |
| 2024 | Avast (antivirus) | Selling browsing data through subsidiary Jumpshot | $16.5 million fine |

Source: FTC enforcement database, press releases (2012-2024).

### International Comparison

| Jurisdiction | Framework | Key Provisions Affecting Brokers | Enforcement |
|--------------|-----------|----------------------------------|-------------|
| **European Union** | GDPR (2018) | Explicit consent required; purpose limitation; data minimization; right to deletion; data portability | Fines up to 4% of global revenue; multiple enforcement actions |
| **United Kingdom** | UK GDPR + DPA 2018 | Similar to EU GDPR post-Brexit | ICO enforcement |
| **Canada** | PIPEDA / Bill C-27 | Consent-based framework; proposed Consumer Privacy Protection Act | Moderate enforcement |
| **Brazil** | LGPD (2020) | GDPR-inspired; consent and legitimate interest bases | National Data Protection Authority |
| **India** | Digital Personal Data Protection Act (2023) | Consent requirements; data fiduciary obligations | New enforcement regime being established |
| **Japan** | APPI (amended 2022) | Consent for third-party transfers; opt-out registry | Personal Information Protection Commission |

## Consumer Impact

### Documented Harms

| Harm Category | Description | Examples | Source |
|---------------|-------------|----------|--------|
| **Discrimination** | Data profiles used to deny opportunities | Higher insurance rates, redlining by proxy, employment denial | Brookings, "Algorithmic Bias" (2023); National Fair Housing Alliance reports |
| **Fraud and identity theft** | Broker data exposed in breaches or sold to criminals | Equifax breach (147M consumers, 2017); ID theft from people-search sites | FTC Identity Theft reports (2024) |
| **Stalking and harassment** | People-search sites enable abusers to locate victims | Domestic violence victims found via Spokeo, WhitePages | NNEDV, "Technology Safety" reports (2023) |
| **Financial harm** | Inaccurate data leads to credit denials, higher rates | Consumer Financial Protection Bureau complaints on data accuracy | CFPB Consumer Complaint Database (2024) |
| **Manipulation** | Detailed profiles enable psychological targeting | Political microtargeting, predatory lending targeting | Senate Intelligence Committee, Cambridge Analytica investigation (2018) |
| **Loss of autonomy** | Pervasive profiling creates chilling effects | Self-censorship, avoidance of sensitive health searches | PEN America, "Chilling Effects" (2023) |
| **Wrongful government action** | Inaccurate broker data leads to false arrests, investigations | ICE arrests based on faulty database matches | Georgetown Law, "American Dragnet" (2022) |

### Consumer Awareness and Attitudes

| Metric | Value | Source |
|--------|-------|--------|
| Americans aware that data brokers exist | 34% | Annenberg School for Communication, "Americans Can't Consent to Companies' Use of Their Data" (2023) |
| Americans who believe they can control their data | 21% | Pew Research Center, "Americans and Privacy" (2023) |
| Americans who find current data practices unacceptable | 79% | Pew Research Center (2023) |
| Consumers who have tried to opt out of a data broker | Less than 5% | Consumer Reports (2023) |
| Average time to opt out of 10 major brokers | 10+ hours across multiple sessions | Privacy Rights Clearinghouse, opt-out study (2023) |

### Opt-Out Burden

| Broker | Opt-Out Process | Timeline | Re-Listing |
|--------|----------------|----------|------------|
| Spokeo | Online form requiring personal verification | 3-5 days | Can be re-listed from new data sources |
| BeenVerified | Online form or email | 24-48 hours | Re-listing common |
| Acxiom | Online portal with identity verification | 10-14 days | Re-listing from partner data |
| WhitePages | Online, requires phone verification | 24-48 hours | Re-listing from public records |
| LexisNexis | Written request with identity documents | 30+ days | Complex, limited confirmation |
| Equifax (marketing) | Written request or phone call | 30+ days | Partial; credit data cannot be fully removed |

## Trends

### Industry Trends (2023-2025)

- **Consolidation**: Major brokers acquiring smaller firms; Interpublic Group acquired Acxiom for $2.3 billion (2018); continued M&A activity
- **Shift to first-party data**: Deprecation of third-party cookies driving brokers to new collection methods
- **AI-powered inference**: Machine learning enabling brokers to infer sensitive attributes from non-sensitive data
- **Connected vehicle data**: Automakers becoming major data sources for brokers (location, driving behavior)
- **Real-time bidding reform pressure**: Growing recognition of RTB as a mass data exposure mechanism
- **State law proliferation**: New registration and transparency laws in multiple states since 2023

### Geographic Variation

| State/Region | Regulatory Approach | Key Features |
|--------------|--------------------| -------------|
| California | Comprehensive (CCPA/CPRA + Delete Act) | Strongest state regime; centralized opt-out mechanism under development |
| Vermont | Registration only | First mover; registration but limited substantive requirements |
| Texas | Registration + opt-out | 2023 law with AG enforcement |
| Illinois | BIPA for biometric data; broader privacy law (2024) | Strong biometric protections; private right of action |
| Northeast states | Emerging comprehensive laws | Connecticut, Virginia, Colorado, others adopting privacy laws that touch brokers |
| Southern states | Minimal regulation | Few specific data broker provisions |
| Federal level | No comprehensive law | Sectoral approach (FCRA, HIPAA, COPPA) leaves brokers largely unregulated |

## The Gap

| What Exists | What Is Needed | Current Status |
|-------------|----------------|----------------|
| State registration laws (4 states) | Universal registration and disclosure requirements | Patchy coverage; most brokers unregistered |
| Opt-out rights (select states) | Opt-in consent before data collection and sale | Consumers bear burden; brokers re-list data |
| Sectoral federal laws (FCRA, HIPAA) | Comprehensive federal data broker regulation | No federal bill has passed; ADPPA stalled |
| FTC enforcement (case-by-case) | Dedicated federal privacy agency with broker authority | FTC resource-constrained; no rulemaking authority specific to brokers |
| Post-hoc breach notification | Proactive data minimization and security requirements | Companies collect maximally, notify after breach |
| Third-party doctrine allowing warrantless purchases | Warrant requirement for government data purchases | *Carpenter* narrowly decided; legislative fix needed |

## Sources

- California Attorney General, Data Broker Registry, accessed January 2025
- Consumer Financial Protection Bureau, Consumer Complaint Database (2024)
- Duke University, "Data Brokers and the Sale of Americans' Mental Health Data" (2023)
- Federal Trade Commission, "Data Brokers: A Call for Transparency and Accountability" (2014)
- Georgetown Law Center on Privacy and Technology, "American Dragnet" (2022)
- IAPP, US State Privacy Legislation Tracker (January 2025)
- IBISWorld, US Data Processing and Hosting Industry Report (2024)
- Irish Council for Civil Liberties, "The Biggest Data Breach" (2022)
- National Conference of State Legislatures, Data Broker Legislation Database (2025)
- Pew Research Center, "Americans and Privacy: Concerned, Confused, and Feeling Lack of Control" (2023)
- Senate Commerce Committee, "A Review of the Data Broker Industry" (2013)
- Statista, "Data Broker Industry Revenue Worldwide" (2024)
- USASpending.gov, federal contract analysis (2023-2024)
- Vermont Secretary of State, Data Broker Registry (2024)

## Related Topics

- [Government Surveillance](../government-surveillance/01-overview.md) - Agencies purchasing broker data
- [Commercial Surveillance](../commercial-surveillance/01-overview.md) - Platform data feeding brokers
- [Consumer Data Rights](../consumer-data-rights/01-overview.md) - Legal frameworks for data rights
- [Privacy Overview](../01-overview.md) - Broader privacy context

## Document Navigation

- Previous: [Overview](01-overview.md)
- Next: [History](03-history.md)
