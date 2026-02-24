# Location Tracking: Root Causes

## Overview

The pervasive tracking of Americans' physical movements results from the convergence of technological capability, economic incentive, legal vacuum, and political inaction. Location data is uniquely revealing -- it exposes religious practice, political affiliation, health conditions, and intimate relationships -- yet it receives less legal protection than library records in most states. Understanding why requires examining the structural forces that have prevented effective regulation despite broad public concern.

## Structural Causes

### 1. The Surveillance Advertising Business Model

The digital advertising ecosystem is the primary engine of location tracking. Location data makes advertising more valuable, creating massive financial incentives for collection.

| Factor | Mechanism | Scale |
|--------|-----------|-------|
| **Location-targeted ads command premium pricing** | Ads targeted by precise location earn 2-3x the CPM of non-targeted ads | $32+ billion US location-targeted advertising market (eMarketer, 2024) |
| **App SDK ecosystem** | Apps embed third-party code (SDKs) that collect location data in exchange for analytics tools or revenue | 70%+ of apps with location access share data with third parties (AppCensus, 2023) |
| **Real-time bidding infrastructure** | Every ad auction broadcasts device location to hundreds of companies | 2+ billion US bid requests daily exposing location (ICCL, 2022) |
| **Data broker market** | Aggregated location data sold as "location intelligence" | $14+ billion location intelligence market (MarketsandMarkets, 2024) |

**Why this matters**: The economic value of location data creates a constituency of app developers, advertisers, data brokers, and analytics firms that profits from collection and resists regulation.

### 2. Legal Framework Gaps

| Gap | Description | Consequence |
|-----|-------------|-------------|
| **No federal location privacy law** | Congress has not enacted legislation specifically addressing commercial location data collection or sale | Fundamental regulatory vacuum |
| **ECPA outdated** | Written in 1986, before smartphones, GPS, or app-based tracking existed | Framework cannot meaningfully address modern location tracking |
| **Carpenter left gaps** | Supreme Court addressed only CSLI obtained by government compulsion; did not address purchases, GPS, or app data | Government agencies exploit gaps by purchasing commercial data |
| **Third-party doctrine not fully overturned** | *Carpenter* limited but did not eliminate the doctrine that sharing data with third parties reduces privacy expectations | Users who "voluntarily" share location with apps deemed to have reduced privacy expectations |
| **No constitutional protection from private actors** | Fourth Amendment constrains only government, not private companies | Companies collect location data with virtually no constitutional limit |
| **Preemption uncertainty** | Federal inaction combined with potential for weak federal law to preempt stronger state laws | Industry lobbies for weak federal "privacy" law that preempts state innovation |

### 3. The Consent Fiction

| Problem | Reality | Source |
|---------|---------|--------|
| **"Permission" requested by apps** | Users click "Allow" without understanding that location data will be shared with dozens of third parties | Less than 9% of users read location privacy policies (Carnegie Mellon, 2023) |
| **Bundled consent** | Location access often bundled with app functionality; users cannot use the app without allowing tracking | Practically every navigation, weather, and social media app |
| **Persistent collection** | Many apps collect location even when not in active use ("always" vs. "while using" permission) | iOS and Android audit reports show background location collection |
| **No informed consent** | Users not told who receives their data, how long it is retained, or that it can be sold to government | Annenberg School: 44% of Americans know apps share location with third parties (2023) |
| **Designed for approval** | Permission dialogs designed to maximize "Allow" clicks; dark patterns in consent interfaces | FTC enforcement actions against deceptive location practices (2022-2024) |

### 4. The Anonymization Myth

| Claim | Reality | Source |
|-------|---------|--------|
| "Location data is anonymized" | 95% of individuals identifiable from 4 spatiotemporal data points | de Montjoye et al., *Nature* (2013) |
| "We use advertising IDs, not names" | Advertising IDs trivially linked to identity through home/work location inference | Princeton Web Transparency Project (2020) |
| "Aggregate data protects privacy" | Aggregate foot traffic data for specific locations can reveal individual movements when combined with other data | *New York Times*, "One Nation, Tracked" (2019) |
| "Data is de-identified per HIPAA" | HIPAA de-identification standards do not apply to location data brokers; and are insufficient for location data regardless | Gravy Analytics breach demonstrated re-identification risk (January 2025) |

**Why this matters**: The industry uses "anonymization" claims to justify collection and resist regulation, but the scientific consensus is clear that location data cannot be meaningfully anonymized.

## Economic Causes

### 5. Multi-Billion-Dollar Industry Incentives

| Stakeholder | Revenue from Location Data | Lobbying Against Regulation |
|-------------|--------------------------|---------------------------|
| **Location data brokers** (SafeGraph, Placer.ai, etc.) | $14+ billion combined market | Trade associations, direct lobbying |
| **Mobile advertising networks** | $32+ billion location-targeted segment | Internet Advertising Bureau, trade associations |
| **App developers** | SDK revenue; location data as currency for free apps | App developer associations |
| **Data analytics firms** | Location-derived insights sold to retailers, real estate, hedge funds | Business intelligence trade groups |
| **Wireless carriers** | Direct revenue from data sales; indirect from advertising partnerships | CTIA (cellular trade association), individual carrier lobbying |

Sources: MarketsandMarkets (2024); eMarketer (2024); OpenSecrets.org lobbying data.

### 6. Cost Externalization

The costs of location tracking are borne by individuals and society while benefits accrue to companies.

| Company Benefit | Externalized Cost | Who Bears It |
|----------------|-------------------|-------------|
| Advertising revenue | Stalking, harassment via location data | Domestic violence survivors, stalking victims |
| Government contract revenue | Warrantless surveillance | Immigrants, activists, minority communities |
| Real estate analytics revenue | Privacy erosion, redlining by proxy | Communities, especially minority neighborhoods |
| Insurance analytics revenue | Discriminatory pricing without consent | Drivers (GM/LexisNexis, 2024) |
| "Free" app model | Users pay with location privacy | All app users |

## Political Causes

### 7. Industry Lobbying Effectiveness

| Lobby | Annual Spend | Key Argument | Source |
|-------|-------------|-------------|--------|
| **Internet Association (dissolved 2022) / successor groups** | $7+ million annually (pre-dissolution) | "Innovation requires data; regulation stifles growth" | OpenSecrets.org |
| **CTIA (wireless carriers)** | $12+ million annually | "Carriers need flexibility; consent frameworks exist" | OpenSecrets.org (2024) |
| **US Chamber of Commerce** | $81 million total (privacy is subset) | "Comprehensive privacy law would be too burdensome" | OpenSecrets.org (2024) |
| **Individual tech companies** (Google, Apple, Meta, Amazon) | $50+ million combined on privacy issues | Varies by company; generally oppose strict consent and private right of action | OpenSecrets.org (2024) |

### 8. Law Enforcement Resistance to Reform

| Actor | Position | Impact |
|-------|---------|--------|
| **DOJ** | Opposes warrant requirements for commercial data purchases; argues purchases are not "searches" | Blocks legislative reform; shapes administration positions |
| **FBI** | Opposes restrictions on location data access; cites terrorism and child exploitation investigations | Persuasive to security-focused legislators |
| **ICE/CBP** | Major purchaser of commercial location data; opposes purchase restrictions | Immigration enforcement justification resonates with some lawmakers |
| **State and local law enforcement associations** | Oppose geofence warrant restrictions; want broad access to location data | Lobby state legislatures against location privacy bills |

### 9. Bipartisan Inaction

| Dynamic | Description |
|---------|-------------|
| **Democrats** | Generally support privacy reform but have not made location privacy a priority; divided on law enforcement access; failed to pass ADPPA |
| **Republicans** | Generally oppose federal regulation; some privacy hawks (Sen. Rand Paul, Sen. Mike Lee) support warrant requirements but party does not prioritize |
| **Administration** | Executive orders on government data purchases (Biden EO, 2023) limited but did not ban purchases; no administration has proposed comprehensive location privacy legislation |

## Technological Causes

### 10. Ubiquitous Tracking Infrastructure

| Factor | Description |
|--------|-------------|
| **Smartphone penetration** | 97% of American adults carry a location-tracking device at all times (Pew, 2024) |
| **Always-on connectivity** | Devices continuously connect to cell towers, WiFi, and Bluetooth, generating location data even without GPS |
| **Sensor proliferation** | Accelerometers, barometers, and magnetometers enable location inference even when GPS is disabled |
| **IoT expansion** | Connected cars, wearables, smart home devices generate additional location signals |
| **Network effects** | Each tracked device improves the tracking of all others (e.g., Apple Find My network of 700+ million devices) |

### 11. Technical Barriers to Opting Out

| Barrier | Description | Impact |
|---------|-------------|--------|
| **Background collection** | Many apps collect location when not in active use | Users cannot prevent collection without uninstalling |
| **WiFi and Bluetooth scanning** | Devices scan for networks even when not connected, revealing location | Disabling WiFi/Bluetooth degrades functionality |
| **Carrier collection** | Cell carriers collect CSLI by design; cannot be opted out without abandoning cell service | Universal, unavoidable tracking |
| **SDK opacity** | Users cannot see which SDKs in an app collect location data | No transparency into third-party data flows |
| **Connected vehicle data** | Turning off connected car features often disables safety and navigation functions | Opting out requires accepting reduced vehicle functionality |

## Root Cause Interactions

```text
Surveillance Advertising Model       Legal Framework Gaps
    │                                      │
    ├── $14B+ location data market         ├── No federal location privacy law
    ├── $32B+ location-targeted ads        ├── ECPA written pre-smartphone
    ├── SDK ecosystem incentives           ├── Carpenter gaps exploited
    │                                      │
    └──────────────┐        ┌──────────────┘
                   │        │
                   ▼        ▼
          PERVASIVE LOCATION TRACKING
                   ▲        ▲
                   │        │
    ┌──────────────┘        └──────────────┐
    │                                      │
Political Dynamics                Technology & Infrastructure
    │                                      │
    ├── Industry lobbying ($50M+)          ├── 97% smartphone penetration
    ├── Law enforcement resistance         ├── Always-on connectivity
    ├── Bipartisan inaction                ├── IoT proliferation
    └── Anonymization myth                 └── Technical opt-out barriers
```

## Implications for Reform

| Root Cause | Reform Implication |
|------------|-------------------|
| Surveillance advertising model | Opt-in consent required; restrict location data use for advertising without affirmative permission |
| No federal law | Congress must enact location-specific privacy legislation |
| Carpenter gaps | Statute must require warrants for all government location data access, including purchases |
| Anonymization myth | Treat all location data as personal data by law; prohibit claims of anonymization as defense |
| Industry lobbying | Build broad coalition (privacy advocates + civil liberties + affected communities); frame as constitutional issue |
| Law enforcement resistance | Provide warrant process that is efficient for legitimate investigations; demonstrate that warrant requirements do not prevent effective law enforcement |
| Technical barriers to opt-out | Mandate privacy-by-default (location off by default; opt-in for sharing); technical standards for SDK transparency |
| Consent fiction | Replace "notice and choice" with substantive limits on collection; prohibit collection beyond what is necessary for the requested service |

## Sources

- AppCensus, mobile app location analysis (2023)
- Annenberg School for Communication, "Americans Can't Consent" (2023)
- Carnegie Mellon University, privacy policy study (2023)
- de Montjoye et al., "Unique in the Crowd," *Nature Scientific Reports* (2013)
- eMarketer/Insider Intelligence, location-targeted advertising data (2024)
- Georgetown Law Center on Privacy and Technology, "American Dragnet" (2022)
- Irish Council for Civil Liberties, "The Biggest Data Breach" (2022)
- MarketsandMarkets, "Location Intelligence Market" (2024)
- OpenSecrets.org, lobbying data (2024)
- Pew Research Center, "Mobile Fact Sheet" (2024)

## Document Navigation

- Previous: [History](03-history.md)
- Next: [Stakeholders](05-stakeholders.md)
