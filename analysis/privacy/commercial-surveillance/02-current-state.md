---
freshness:
  last-reviewed: 2026-02-20
  data-year: 2025
  review-cycle: 6
  sections:
    - name: "The Surveillance Advertising Ecosystem"
      data-year: 2024-2025
    - name: "Key Statistics"
      data-year: 2024-2025
    - name: "Regulatory Landscape"
      data-year: 2025
    - name: "Recent Developments"
      data-year: 2025
notes:
  - Revisit after any federal privacy legislation votes in the 119th Congress.
  - Monitor FTC rulemaking on commercial surveillance.
  - Update state law section after 2025-2026 legislative sessions.
sources:
  count: 14
  verified: 2026-02-20
  broken: 0
---

# Commercial Surveillance: Current State

## The Problem Today

### The Scale of Commercial Surveillance

Every American with a digital device is subject to continuous commercial surveillance. The infrastructure is invisible to most people, operating through technologies embedded in websites, apps, operating systems, and physical environments.

**What Is Collected**

| Data Category | Examples | Collection Methods |
|---------------|----------|-------------------|
| Browsing behavior | Every website visited, link clicked, page viewed, time spent | Cookies, pixels, browser fingerprinting |
| Search queries | Every search term, voice query, autocomplete interaction | Search engines, voice assistants |
| Location | GPS coordinates, Wi-Fi triangulation, Bluetooth beacons, cell tower data | Smartphones, apps, vehicles, wearables |
| Purchases | Online and offline transaction history, payment data | Payment processors, loyalty programs, receipt scanning |
| Communications | Email content (scanned), message metadata, call logs | Email providers, messaging platforms, carriers |
| Social connections | Friends, contacts, group memberships, interaction patterns | Social platforms, contact lists, communication patterns |
| Biometric | Face geometry, voice prints, fingerprints, gait | Smartphones, smart cameras, voice assistants |
| Inferred data | Political affiliation, sexual orientation, health conditions, pregnancy, financial status | Algorithmic analysis of behavioral data |
| Offline behavior | Store visits, physical movement patterns, product interactions | Beacons, Wi-Fi tracking, geofencing, retail analytics |

**Who Collects It**

```text
Commercial Surveillance Ecosystem

Primary Collectors          Intermediaries              End Users
──────────────────          ──────────────              ─────────
Platforms (Google,     ──►  Ad networks           ──►  Advertisers
  Meta, Amazon)             (thousands)                 Insurers
App developers         ──►  Data brokers           ──►  Employers
Retailers/brands       ──►  Data management             Landlords
IoT manufacturers            platforms              ──► Lenders
Telecom carriers       ──►  Identity resolution    ──►  Political campaigns
Payment processors          companies              ──► Government agencies
Loyalty programs       ──►  Analytics firms        ──►  Law enforcement
```

### The Surveillance Advertising Ecosystem

**How Real-Time Bidding Works**

Real-time bidding (RTB) is the mechanism through which most digital advertising operates. When a user loads a webpage or opens an app:

1. The publisher sends a "bid request" to an ad exchange containing the user's personal data
2. The bid request is broadcast to hundreds of potential advertisers simultaneously
3. Advertisers bid on the opportunity to show an ad to that specific user
4. The highest bidder's ad is displayed -- the entire process takes approximately 100 milliseconds
5. The user's personal data has been exposed to every participant in the auction

**Scale of RTB Data Exposure**

- 747 billion RTB bid requests in the US market annually (Irish Council for Civil Liberties, "The Biggest Data Breach," 2022)
- Each bid request can contain location data, browsing history, device information, and demographic inferences
- Hundreds of companies receive this data for each impression
- There is no practical way to verify that companies receiving bid request data use it only for advertising
- The RTB system constitutes the largest continuous data breach in history, operating in plain sight

**Market Concentration**

| Company | US Digital Ad Revenue Share (2023) | Key Assets |
|---------|-----------------------------------|------------|
| Google/Alphabet | ~27% | Search, YouTube, Android, Chrome, Gmail, DoubleClick |
| Meta | ~22% | Facebook, Instagram, WhatsApp, Messenger |
| Amazon | ~13% | E-commerce, Alexa, Whole Foods, Ring, AWS |
| Microsoft | ~4% | Bing, LinkedIn, Windows, Office |
| Apple | ~3% | App Store, Apple News, growing ad business |
| Others | ~31% | Thousands of companies |

*Source: eMarketer estimates (2024)*

### Platform Data Practices

**Google**

- Controls the dominant search engine (91% US market share, StatCounter 2024), web browser (65%, StatCounter 2024), mobile OS (44% US, StatCounter 2024), and email service (1.8 billion users globally)
- Tracks users across Search, YouTube, Gmail, Maps, Android, Chrome, Google Workspace, and third-party sites via ad network
- "Privacy Sandbox" initiative replaces third-party cookies with Topics API -- still enables interest-based advertising
- $307 billion in advertising revenue (2023, Alphabet annual report)

**Meta**

- Operates Facebook (2.1 billion daily active users), Instagram (2+ billion monthly), WhatsApp (2+ billion monthly), Messenger
- Collects data from on-platform activity, off-platform tracking via Meta Pixel and Conversions API, and partnerships with data brokers
- Even non-users have "shadow profiles" built from contacts' data and web tracking
- $131.9 billion in advertising revenue (2023, Meta annual report)

**Amazon**

- E-commerce, Alexa voice assistant, Ring doorbells/cameras, Kindle, Whole Foods, Prime Video, AWS cloud services
- Combines purchase data, voice recordings, viewing habits, physical movement (Ring), and cloud infrastructure usage
- Advertising business growing rapidly -- $46.9 billion in ad revenue (2023, Amazon annual report)
- Ring partnerships with law enforcement raised surveillance concerns; Ring ended police access program in 2024

**Data Brokers**

- Over 530 data brokers registered in California alone (California AG Data Broker Registry, January 2025)
- Compile profiles with up to 1,500+ data points per individual (FTC, 2014)
- Sell data to advertisers, employers, landlords, insurers, law enforcement, and other brokers
- Operate with minimal regulation and virtually no consumer awareness

### Consumer Harms

**Discrimination**

- Housing: Algorithmic ad targeting enables housing discrimination by race, religion, disability, and family status (*National Fair Housing Alliance v. Facebook*, settled 2019; HUD v. Facebook complaint, 2019)
- Employment: Job ads disproportionately shown or hidden based on age, gender, and race (Lambrecht and Tucker, *Management Science*, 2019)
- Credit: Alternative data used in lending decisions can serve as proxy for protected characteristics (Bartlett et al., *NBER Working Paper*, 2019)
- Insurance: Data-driven pricing correlates with race and income (Consumer Federation of America, 2023)

**Manipulation**

- Dark patterns: Deceptive design practices manipulate users into sharing more data (FTC, "Bringing Dark Patterns to Light," 2022)
- Algorithmic amplification: Engagement-optimized algorithms promote outrage, misinformation, and extremism
- Personalized pricing: Different users shown different prices based on surveillance profiles (Mikians et al., 2013; confirmed by multiple studies)
- Addiction features: Variable-ratio reinforcement schedules (infinite scroll, pull-to-refresh) designed to maximize engagement

**Security Risks**

- Centralized data stores are high-value targets for hackers
- Data breaches exposed 1.8 billion records in 2023 (Identity Theft Resource Center, 2024)
- Commercially collected data can be weaponized by foreign adversaries, stalkers, and identity thieves

## Regulatory Landscape

### Federal Law

**What Exists**

| Law | Scope | Key Limitation |
|-----|-------|----------------|
| FTC Act, Section 5 | Unfair/deceptive practices | No specific privacy standards; relies on case-by-case enforcement |
| COPPA | Children under 13 online | Does not cover teens or general-audience platforms |
| HIPAA | Health care providers and insurers | Does not cover health apps, wearables, or fitness trackers |
| GLBA | Financial institutions | Narrow; allows sharing with affiliates and for marketing |
| FCRA | Consumer reporting | Does not cover most commercial surveillance data |
| ECPA/SCA | Electronic communications | Outdated; does not address modern data practices |

**What Does Not Exist**

- No comprehensive federal privacy law governing commercial data practices
- No federal data minimization requirement
- No general federal purpose limitation requirement
- No federal private right of action for privacy violations (except narrow statutory cases)
- No federal requirement for privacy-by-design
- No federal algorithmic accountability law

### State Laws

| State | Law | Key Features | Effective |
|-------|-----|--------------|-----------|
| California | CCPA/CPRA | Broadest US privacy law; opt-out of sale/sharing; data minimization; private right of action (limited to breaches); California Privacy Protection Agency | 2020/2023 |
| Virginia | VCDPA | Consumer rights (access, delete, opt out); no private right of action | 2023 |
| Colorado | CPA | Consumer rights; universal opt-out mechanism; privacy assessments | 2023 |
| Connecticut | CTDPA | Consumer rights; consent for sensitive data; children's provisions | 2023 |
| Utah | UCPA | Consumer rights (narrower); business-friendly | 2023 |
| Texas | TDPSA | Consumer rights; broad applicability | 2024 |
| Oregon | OCPA | Consumer rights; data broker registration; children's provisions | 2024 |
| Montana | MCDPA | Consumer rights; opt-in for sensitive data | 2024 |
| Delaware | DPDPA | Consumer rights; opt-out of profiling | 2025 |
| 10+ others | Various | Various consumer data rights | 2024-2026 |

**State Law Limitations**

- No state law matches the GDPR in scope or enforcement
- Most state laws lack private right of action (California is partial exception)
- Enforcement depends on state AG resources and priorities
- No state law regulates RTB or the surveillance advertising system directly
- Patchwork creates compliance complexity but does not prevent surveillance

### International Comparison

| Jurisdiction | Framework | Key Differences from US |
|--------------|-----------|------------------------|
| European Union | GDPR (2018) | Comprehensive; consent-based; data minimization; DPAs; fines up to 4% global revenue |
| United Kingdom | UK GDPR + Data Protection Act 2018 | Similar to EU; ICO enforcement; post-Brexit divergence ongoing |
| Canada | PIPEDA (proposed CPPA reform) | Consent-based; proposed modernization with stronger enforcement |
| Brazil | LGPD (2020) | GDPR-inspired; National Data Protection Authority |
| India | Digital Personal Data Protection Act (2023) | Consent-based; significant government exemptions |
| Japan | APPI (amended 2022) | Adequacy agreement with EU; consent-based |

## Key Statistics

| Metric | Value | Source |
|--------|-------|--------|
| US digital ad revenue (2023) | $225 billion | IAB/PwC (2024) |
| Google ad revenue (2023) | $307 billion | Alphabet annual report |
| Meta ad revenue (2023) | $131.9 billion | Meta annual report |
| Data broker industry (global) | $350+ billion | Statista (2024) |
| Average trackers per major website | 40-70 | Ghostery Tracker Radar (2024) |
| RTB bid requests (US, annual) | 747 billion | ICCL (2022) |
| Data breaches (2023) | 3,205 incidents; 1.8 billion records | ITRC (2024) |
| Americans who lack confidence in data practices | 73% | Pew Research (2023) |
| States with comprehensive privacy laws | 19+ | IAPP (January 2025) |
| FTC privacy enforcement budget | Fraction of ~$430M total budget | FTC budget (FY 2024) |

## Recent Developments

### Federal (2023-2025)

- **FTC Commercial Surveillance ANPR (2022-2024)**: FTC sought public comment on potential rulemaking addressing commercial surveillance and data security; proceeding ongoing
- **FTC enforcement escalation**: Major cases against Meta (expanded COPPA order), Amazon (Alexa/Ring privacy), and Epic Games ($520 million, 2022)
- **American Data Privacy and Protection Act (ADPPA)**: Passed House Energy and Commerce Committee in 2022 with bipartisan support; stalled over preemption dispute and private right of action; not reintroduced in 119th Congress in same form
- **Executive Order on AI (October 2023)**: Required assessment of AI risks including privacy; limited direct impact on commercial surveillance
- **Data broker executive order (2024)**: Biden executive order restricting sale of sensitive personal data to countries of concern

### State Level (2023-2025)

- Number of states with comprehensive privacy laws grew from 5 (2022) to 19+ (January 2025)
- California CPPA issued first enforcement actions in 2024
- Texas and other states enacted new comprehensive privacy laws
- State-level AI and algorithmic accountability bills introduced in multiple states

### Industry

- Google delayed and restructured third-party cookie deprecation in Chrome (originally planned for 2024; revised to user-choice model)
- Apple expanded App Tracking Transparency (ATT); ad industry adapted through fingerprinting and other circumvention methods
- AI boom created new demand for training data, raising privacy questions about data scraping
- FTC warning letters to companies using AI trained on commercial surveillance data

---

## Document Navigation

- Previous: [Overview](01-overview.md)
- Next: [History](03-history.md)
