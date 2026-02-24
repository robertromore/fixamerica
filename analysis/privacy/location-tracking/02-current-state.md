---
freshness:
  last-reviewed: 2026-02-20
  data-year: 2025
  review-cycle: 6
  sections:
    - name: "Tracking Technologies"
      data-year: 2025
    - name: "Commercial Location Data Ecosystem"
      data-year: 2025
    - name: "Government Acquisition of Location Data"
      data-year: 2025
    - name: "Legal Framework"
      data-year: 2025
    - name: "Consumer Impact"
      data-year: 2025
notes:
  - Track geofence warrant litigation in federal circuits.
  - Monitor Google and Apple policy changes on location data.
  - Update government data purchase documentation as new FOIA releases emerge.
sources:
  count: 24
  verified: 2026-02-20
  broken: 0
---

# Location Tracking: Current State

## Tracking Technologies

### Mobile Device Tracking Methods

| Method | Accuracy | Source | How It Works |
|--------|----------|--------|-------------|
| **GPS (Global Positioning System)** | 1-5 meters | Device hardware | Satellite triangulation; most precise; used by maps, ride-sharing, fitness apps |
| **Cell tower triangulation (CSLI)** | 50-300 meters (urban); 1+ km (rural) | Carrier network | Phone connects to nearest towers; carriers retain records; subject of *Carpenter* |
| **WiFi positioning** | 10-40 meters | WiFi access points | Device scans for WiFi networks; known network locations used for positioning |
| **Bluetooth beacons** | 1-10 meters | Installed beacons | Short-range; used in retail, museums, stadiums for micro-location tracking |
| **IP address geolocation** | City/neighborhood level | Internet connection | Maps IP addresses to approximate physical location |
| **Ultrasonic beacons** | Room-level | Inaudible audio signals | TV/radio ads emit ultrasonic tones detected by phone microphones; links TV viewing to device (FTC, 2016) |
| **Sensor fusion** | Sub-meter | Combined device sensors | Combines GPS, accelerometer, gyroscope, barometer for highly precise positioning |

### Data Generation Scale

| Metric | Value | Source |
|--------|-------|--------|
| Location data points per smartphone per day | 200-600+ | Carnegie Mellon University, mobile app analysis (2023) |
| Total location data points generated daily (US) | 60+ billion (estimated from 270 million smartphone users) | Industry estimates based on app analytics data |
| Average number of apps with location permission per phone | 35-45 apps | AppCensus, Android app analysis (2023) |
| Apps sharing location data with third parties | 70%+ of apps with location access | AppCensus (2023); *New York Times* "One Nation, Tracked" investigation (2019) |
| Location data points in commercial databases | Trillions | SafeGraph, Placer.ai, and other broker disclosures in legal filings |

### Connected Vehicle Tracking

| Metric | Value | Source |
|--------|-------|--------|
| Connected cars on US roads | 84+ million (2024) | S&P Global Mobility (2024) |
| New vehicles with built-in connectivity | 95%+ (2024 model year) | Alliance for Automotive Innovation (2024) |
| Automakers sharing location data with third parties | 25 of 25 major brands studied | Mozilla Foundation, "*Privacy Not Included: Cars" (2023) |
| GM OnStar data sharing with insurance (LexisNexis) | Exposed; 12+ million drivers' data shared without clear consent | *New York Times* investigation (March 2024) |
| License plate reader cameras (US) | 100,000+ | EFF, "Automated License Plate Readers" (2024) |
| ALPR scans per year | 2.5+ billion | DRN / Motorola Solutions estimates (2024) |

### IoT and Wearable Tracking

| Device Category | Location Capability | User Base |
|----------------|--------------------| ----------|
| **Fitness trackers/smartwatches** | Continuous GPS; heart rate at location | 87 million US users (Statista, 2024) |
| **Smart speakers** | WiFi location; some GPS-equivalent | 90+ million US households (NPR/Edison Research, 2024) |
| **AirTags/Tile trackers** | Bluetooth mesh network; crowd-sourced location | 700+ million Apple devices in Find My network (Apple, 2024) |
| **Smart home devices** | Presence detection; WiFi-based location | 63 million US smart home households (Statista, 2024) |
| **Children's smartwatches** | Continuous GPS; geofencing alerts | 15+ million units sold globally (Counterpoint Research, 2023) |

## Commercial Location Data Ecosystem

### Major Location Data Brokers

| Company | Data Sources | Customers | Estimated Records |
|---------|-------------|-----------|-------------------|
| **SafeGraph** | Mobile apps via SDKs; aggregated foot traffic data | Retailers, real estate, hedge funds, researchers | Points of interest data for 10+ million locations; device panel of 45+ million |
| **Placer.ai** | Mobile app SDKs; location analytics | Retail, real estate, municipalities | 20+ million device panel (US) |
| **Babel Street / Locate X** | Mobile advertising data; app SDKs | Government agencies (ICE, CBP, Secret Service) | Billions of location records |
| **Venntel** (now Babel Street) | Mobile advertising ecosystem | ICE, CBP, IRS, DOD | 250+ million mobile devices tracked monthly (pre-acquisition estimates) |
| **X-Mode Social / Outlogic** | App SDK location data | Military, government, advertisers | 25+ billion location data points monthly |
| **Near Intelligence** | Advertising SDKs, WiFi signals | Advertisers, marketers | 1.6 billion device IDs; 70 million POI |
| **Foursquare** | Foursquare/Swarm apps; SDK partners | Advertisers, tech companies | 14+ billion check-ins; 100,000+ developer accounts |
| **Gravy Analytics** | Mobile app SDKs | Advertisers, analytics firms | Billions of location records; data breach exposed in January 2025 |

Sources: Company disclosures, court filings, investigative reporting, and marketing materials (2023-2025).

### Data Flow Pipeline

```text
Data Sources                    Intermediaries                     End Users
─────────────                   ──────────────                     ─────────
Mobile apps (SDKs)  ───────►  Location data brokers  ──────►  Advertisers
Cell carriers       ───────►  Real-time bidding      ──────►  Government agencies
WiFi providers      ───────►  Data aggregators       ──────►  Hedge funds
Connected vehicles  ───────►  People-search sites    ──────►  Real estate firms
Fitness trackers    ───────►                         ──────►  Insurance companies
Retail beacons      ───────►                         ──────►  Private investigators
IoT devices         ───────►                         ──────►  Stalkers/abusers
```

### Real-Time Bidding as Location Data Leak

| Metric | Value | Source |
|--------|-------|--------|
| RTB bid requests exposing US location data daily | 2+ billion (US market) | Irish Council for Civil Liberties, "The Biggest Data Breach" (2022) |
| Companies receiving location data per ad impression | 100-1,000+ | Reuben Binns, Oxford Internet Institute research (2023) |
| Location precision in RTB data | Latitude/longitude to 5+ decimal places (~1 meter) | Industry documentation; RTB specification (OpenRTB 2.6) |
| Revenue from location-targeted advertising | $32+ billion (US, 2024) | eMarketer/Insider Intelligence (2024) |

### De-Anonymization Risk

| Study | Finding | Source |
|-------|---------|--------|
| *Unique in the Crowd* | 4 spatiotemporal points sufficient to uniquely identify 95% of individuals | de Montjoye et al., *Nature Scientific Reports* (2013) |
| *No Place to Hide* | Home and work locations identifiable from anonymized data within days | *New York Times*, "One Nation, Tracked" (2019) |
| Princeton Web Transparency & Accountability Project | Advertising IDs can be linked to real identities through home location inference | Englehardt et al. (2020) |
| Gravy Analytics breach (2025) | Breach of location data broker exposed precise movements of millions; confirmed re-identification risks | TechCrunch, *404 Media* (January 2025) |
| Military/intelligence personnel tracking | Commercial location data used to track movements of personnel at NSA, CIA, Pentagon | *New York Times* investigation (2024) |

## Government Acquisition of Location Data

### Documented Federal Agency Purchases

| Agency | Data Type | Vendor | Purpose | Source |
|--------|-----------|--------|---------|--------|
| **ICE** | Mobile location data | Venntel/Babel Street | Immigration enforcement; tracking individuals | Georgetown Law, "American Dragnet" (2022) |
| **CBP** | Mobile location data | Venntel, Babel Street | Border surveillance; tracking at ports of entry | Sen. Wyden investigation (2020) |
| **IRS** | Mobile location data | Venntel | Tax enforcement investigations | *Wall Street Journal* (2020); IRS IG report |
| **FBI** | Location data, advertising data | Various | Criminal investigations, intelligence | Sen. Wyden investigations (2023) |
| **Secret Service** | Mobile location data | Babel Street / Locate X | Protective intelligence | *Vice Motherboard* (2020) |
| **DIA** | Commercial location data | Various | Foreign intelligence | DIA memo, *New York Times* (2021) |
| **DEA** | License plate reader data | DRN/Vigilant Solutions | Drug trafficking investigations | ACLU FOIA (2020) |
| **DHS** (multiple components) | Location data, social media | Multiple vendors | Threat assessment, visa vetting | DHS Privacy Impact Assessments |

### Geofence Warrants

| Metric | Value | Source |
|--------|-------|--------|
| Google geofence requests received (2020) | 11,554 | Google Transparency Report (2022) |
| Growth in geofence requests to Google (2018-2020) | 556% increase | Google Transparency Report data |
| Google's policy change | Stopped storing location data centrally to prevent geofence responses (December 2023) | Google blog announcement (2023) |
| Federal circuits addressing geofence warrants | 4th Circuit (*Chatrie*, 2024), 5th Circuit, others | Federal court decisions |
| States restricting geofence warrants | 4+ (New York, Utah, Montana, and others considering) | NCSL (2025) |

### The Carpenter Gap

| What *Carpenter* Protects | What *Carpenter* Does Not Protect | Consequence |
|---------------------------|----------------------------------|-------------|
| Historical CSLI obtained via court order (warrant required) | Location data purchased from commercial brokers | Government agencies buy location data to avoid warrant requirement |
| 7+ days of CSLI (warrant required) | Short-term CSLI (some circuits; unclear) | Uncertainty for shorter-duration requests |
| Government compulsion of carriers | Government purchase from data brokers | Constitutional end-run around warrant requirement |
| Cell-site location information specifically | GPS data, WiFi positioning, Bluetooth data | More precise tracking technologies not clearly covered |
| Retrospective CSLI | Real-time location tracking (remains under *United States v. Jones*, 2012, with no majority rule) | Real-time tracking standards uncertain |

## Legal Framework

### Federal Law

| Law | Relevance | Gap |
|-----|-----------|-----|
| **Fourth Amendment** | *Carpenter* requires warrant for CSLI; *Jones* (2012) trespassory GPS tracking | Does not apply to private collection; government purchases not clearly covered |
| **ECPA / Stored Communications Act** (1986) | Covers government access to stored communications; location data provisions outdated | Written pre-GPS; does not address app-based location data or commercial purchases |
| **No federal location privacy law** | No statute specifically governs commercial location data collection or sale | Fundamental gap in US law |
| **FTC Act Section 5** | FTC can pursue deceptive location practices | No specific location data authority; requires proving unfairness or deception |

### State Laws

| State | Law | Year | Key Provisions |
|-------|-----|------|----------------|
| **California** | CCPA/CPRA (precise geolocation as sensitive personal information) | 2020/2023 | Consent required for sale/sharing of precise geolocation data; right to delete |
| **Utah** | Location Data Protection Act | 2023 | Warrant requirement for law enforcement access to location data; restrictions on geofence warrants |
| **New York** | Geofence/reverse keyword warrant ban (pending) | 2024 | Proposed ban on geofence warrants and reverse keyword searches |
| **Montana** | Electronic Data Privacy Act (SB 171) | 2023 | Warrant requirement for government access to electronic data including location |
| **Illinois** | Location Privacy Protection Act | 2024 | Requires consent before collecting location data from apps; private right of action |
| **19+ states** | Comprehensive privacy laws (various) | 2018-2025 | Varying location data provisions within broader privacy frameworks |

Sources: NCSL, state statute databases, IAPP State Law Tracker (2025).

### Key Court Decisions

| Case | Year | Holding | Significance |
|------|------|---------|-------------|
| *United States v. Jones* | 2012 | GPS tracker on vehicle constitutes a Fourth Amendment "search" under trespass theory | Limited to physical trespass; did not address digital tracking |
| *Carpenter v. United States* | 2018 | Historical CSLI is protected by Fourth Amendment; warrant required for 7+ days of records | Landmark digital privacy ruling; but narrow holding left many gaps |
| *United States v. Chatrie* | 2024 (4th Cir.) | Geofence warrants are overbroad and violate Fourth Amendment's particularity requirement | First federal circuit decision on geofence warrants |
| *In re Search of Information Associated with Email Accounts* | 2024 | Various circuit decisions on scope of Carpenter | Ongoing litigation over Carpenter's boundaries |

## Consumer Impact

### Tracking Awareness and Attitudes

| Metric | Value | Source |
|--------|-------|--------|
| Americans concerned about location tracking | 72% | Pew Research Center, "Americans and Privacy" (2023) |
| Americans who have turned off location services | 52% have done so on at least one app | Pew Research Center (2023) |
| Americans who know apps share location with third parties | 44% | Annenberg School for Communication (2023) |
| Americans who feel they have control over location data | 18% | Pew Research Center (2023) |
| Consumers who read location-related privacy policies | Less than 9% | Carnegie Mellon University, privacy policy study (2023) |

### Documented Harms

| Harm | Description | Source |
|------|-------------|--------|
| **Stalking and domestic violence** | AirTags, Tile trackers, and phone tracking used by abusers to locate victims | National Network to End Domestic Violence (2023); Apple safety report (2024) |
| **Reproductive healthcare targeting** | Location data near abortion clinics sold by data brokers; used for advertising and potentially enforcement | *Wall Street Journal* SafeGraph investigation (2022); FTC v. Kochava (2022) |
| **Immigration enforcement** | ICE uses commercial location data to track and arrest undocumented immigrants | Georgetown Law, "American Dragnet" (2022) |
| **Protest surveillance** | Geofence warrants used to identify participants at protests | *Forbes*, Kenosha BLM protest geofence warrant (2021) |
| **Religious profiling** | Location data revealing mosque, synagogue, or church attendance available for purchase | Duke University, sensitive data broker study (2023) |
| **Insurance discrimination** | Driving data from connected cars shared with insurers without clear consent; affecting premiums | *New York Times*, GM OnStar/LexisNexis investigation (March 2024) |
| **Real estate redlining by proxy** | Foot traffic data used for property valuation can reinforce racial segregation patterns | Brookings, "Technology and Fair Housing" (2023) |

### Vulnerable Populations

| Population | Specific Risk | Source |
|------------|--------------|--------|
| **Undocumented immigrants** | ICE/CBP purchase commercial location data to track movements near border and in interior | Georgetown Law (2022) |
| **Abortion seekers** | Location data near clinics purchasable; post-*Dobbs* legal risk in restrictive states | FTC enforcement actions; *Wall Street Journal* (2022) |
| **Domestic violence survivors** | Trackers and phone-based stalking; people-search sites reveal shelter locations | NNEDV (2023) |
| **Protesters and activists** | Geofence warrants identify attendees; chilling effect on First Amendment activity | ACLU, geofence warrant analysis (2023) |
| **LGBTQ+ individuals** | Location data at LGBTQ+ venues purchasable; risk in hostile jurisdictions | Human Rights Campaign, privacy report (2023) |
| **Military and intelligence personnel** | Commercial location data reveals movements at classified facilities | *New York Times* investigation (2024) |

## Trends (2023-2025)

- **Google geofence policy change**: Google stopped storing location data in centralized Sensorvault (December 2023), largely ending its ability to respond to geofence warrants -- but other companies may fill the gap
- **Apple App Tracking Transparency impact**: 75% of iOS users opt out of tracking; shifted advertising industry toward new tracking methods (fingerprinting, cohort-based approaches)
- **Connected vehicle data controversy**: GM/LexisNexis revelations (2024) brought vehicle tracking to public attention; FTC and Congress investigating
- **Gravy Analytics data breach** (January 2025): Breach of major location data broker exposed precise location data of millions; demonstrated risks of centralized collection
- **State legislative momentum**: Utah, Montana, Illinois, and others passing location-specific privacy laws
- **AI-powered location inference**: Machine learning can infer location from non-location signals (WiFi network names, ambient sound, photos); expanding tracking beyond GPS

## Sources

- Apple, App Tracking Transparency documentation (2024)
- Carnegie Mellon University, mobile privacy research (2023)
- de Montjoye et al., "Unique in the Crowd," *Nature Scientific Reports* (2013)
- EFF, "Automated License Plate Readers" (2024)
- Flurry Analytics, ATT opt-in rates (2023)
- Georgetown Law Center on Privacy and Technology, "American Dragnet" (2022)
- Google Transparency Report (2022)
- IAPP, US State Privacy Legislation Tracker (2025)
- Irish Council for Civil Liberties, "The Biggest Data Breach" (2022)
- MarketsandMarkets, "Location Intelligence Market" (2024)
- Mozilla Foundation, "*Privacy Not Included: Cars" (2023)
- National Conference of State Legislatures (2025)
- *New York Times*, "One Nation, Tracked" investigation (2019)
- *New York Times*, GM/LexisNexis investigation (2024)
- Pew Research Center, "Americans and Privacy" (2023)
- S&P Global Mobility, connected car data (2024)
- TechCrunch, Gravy Analytics breach coverage (2025)

## Related Topics

- [Workplace Surveillance](../workplace-surveillance/01-overview.md) - Employer GPS tracking
- [Data Brokers](../data-brokers/01-overview.md) - Location data as broker commodity
- [Government Surveillance](../government-surveillance/01-overview.md) - Government location data purchases
- [Privacy Overview](../01-overview.md) - Broader privacy context

## Document Navigation

- Previous: [Overview](01-overview.md)
- Next: [History](03-history.md)
