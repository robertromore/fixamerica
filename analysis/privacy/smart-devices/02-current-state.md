---
last_updated: 2026-02-20
status: current
confidence: high
---

# Smart Devices and IoT: Current State

## Market Overview

### IoT Device Penetration

The smart device market in the United States has grown rapidly, with adoption accelerating during and after the COVID-19 pandemic as remote work and home-focused lifestyles increased demand for connected home technology.

| Metric | Value | Source |
|--------|-------|--------|
| US consumer IoT devices in use | 300+ million | Statista, "IoT Connected Devices in the US" (2024) |
| US households with at least one smart device | 69% | Parks Associates, "Smart Home Dashboard" (2024) |
| Smart speaker ownership | 35% of US adults | Pew Research Center (2024) |
| Connected TV households | 87% of TV households | Leichtman Research Group (2024) |
| Wearable device users | 104 million | eMarketer (2024) |
| Connected vehicles on US roads | 84 million | S&P Global Mobility (2024) |
| Smart home market revenue (US) | $54 billion (2024) | Statista, "Smart Home Market" (2024) |
| IoT devices per US household (average) | 22 connected devices | Deloitte, "Connectivity and Mobile Trends" (2024) |

### Major Device Categories and Market Leaders

| Category | Key Products | Market Leaders | US Market Share |
|----------|-------------|----------------|-----------------|
| **Voice assistants/smart speakers** | Echo, Nest, HomePod | Amazon (63%), Google (24%), Apple (10%) | $9.4 billion |
| **Smart TVs** | Samsung, LG, Roku, Fire TV | Samsung (29%), Roku (31% streaming), LG (12%) | Integrated into TV sales |
| **Fitness trackers/smartwatches** | Apple Watch, Fitbit, Garmin | Apple (55%), Samsung (12%), Garmin (8%) | $14.2 billion |
| **Connected vehicles** | Tesla, GM OnStar, Ford SYNC | GM, Ford, Tesla, Toyota | Part of $1.3T auto market |
| **Smart home security** | Ring, Nest Cam, Arlo, SimpliSafe | Ring/Amazon (40%), ADT (15%), Google (12%) | $6.8 billion |
| **Smart thermostats** | Nest, Ecobee, Honeywell | Google Nest (40%), Ecobee (20%), Honeywell (18%) | $2.1 billion |
| **Robot vacuums** | Roomba, Roborock, Ecovacs | iRobot (39%), Roborock (20%), Ecovacs (12%) | $2.4 billion |
| **Smart lighting** | Philips Hue, LIFX, Wyze | Philips/Signify (42%), Wyze (15%) | $3.2 billion |

Sources: Company reports, IDC, Statista, Counterpoint Research (2024 estimates).

## Data Collection Practices by Device Type

### Voice Assistants and Smart Speakers

| Data Type | Amazon Echo | Google Nest | Apple HomePod |
|-----------|------------|-------------|---------------|
| Voice recordings | Stored until user deletes (default) | Stored until user deletes (default) | Processed on-device (Siri); opt-in for cloud |
| Wake word false activations | Up to 19 per day per device | Up to 12 per day per device | Frequency undisclosed |
| Interaction transcripts | Retained for model training (opt-out available) | Retained for model training (opt-out available) | Not retained by default |
| Purchase/shopping data | Full purchase history retained | Integrated with Google Shopping | Apple Pay data minimized |
| Third-party skill data | Shared with skill developers | Shared with Action developers | Shared with app developers |
| Home occupancy patterns | Inferred from usage times | Inferred from usage times | Processed on-device |
| Human review of recordings | Yes (reduced after 2019 revelations) | Yes (paused, then resumed with opt-in) | Yes (opt-in only since 2019) |

Sources: Amazon, Google, Apple privacy policies (2024); Bloomberg, *The Guardian* reporting (2019).

### Smart Televisions

| Practice | Prevalence | Details |
|----------|-----------|---------|
| **Automated Content Recognition (ACR)** | 87% of smart TVs | Captures screenshots every few seconds to identify content being watched, including streaming, cable, DVD, and gaming |
| **Viewing data monetization** | All major brands | Sold to advertisers for cross-device targeting and audience measurement |
| **Opt-out vs. opt-in** | Mostly opt-out | Most TVs enable ACR during setup; some bury opt-out in settings |
| **Post-purchase tracking changes** | Common | Firmware updates can enable new tracking features without explicit consent |
| **Cross-device identification** | Growing | Smart TVs matched with mobile devices, computers for unified profiles |
| **Microphone always-on** | Select models | Some TVs with built-in voice assistants maintain always-on microphones |

Sources: Consumer Reports (2023); FTC Vizio settlement (2017); Inscape/Vizio disclosures.

### Connected Vehicles

| Data Type | Collection Method | Sharing Documented |
|-----------|------------------|-------------------|
| **Location history** | GPS, cellular | Shared with data brokers, insurers, law enforcement |
| **Driving behavior** | Accelerometers, speed sensors | Sold to insurance companies (GM/OnStar to LexisNexis) |
| **Cabin audio** | In-car microphones | GM, Tesla, others retain voice commands; some capture ambient audio |
| **Biometric data** | Seat sensors, cameras | Ford, BMW patent filings for driver monitoring |
| **Contacts/call logs** | Phone pairing via Bluetooth | Synced to vehicle system; retained after phone disconnects |
| **App usage** | Infotainment system | Entertainment, navigation, and communication data logged |
| **Passenger detection** | Weight sensors, cameras | Occupancy data shared with insurance, safety systems |
| **Maintenance data** | OBD-II, vehicle sensors | Shared with dealers, third-party repair shops, data aggregators |

Sources: Mozilla Foundation, "*Privacy Not Included: Cars" (2023); Sen. Wyden investigation of GM data sharing (2024); *The New York Times*, "Your Car Is Watching You" (2024).

### Key Finding: Connected Car Data Sharing

A 2023 Mozilla Foundation review of 25 major car brands found:

| Finding | Number of Brands |
|---------|-----------------|
| Collect more data than necessary | 25/25 (100%) |
| Share or sell personal data | 21/25 (84%) |
| Cannot confirm they meet minimum security standards | 25/25 (100%) |
| Have a problematic privacy policy | 25/25 (100%) |
| Provide ability to delete personal data | 2/25 (8%) |

### Wearable Devices

| Data Type | Apple Watch | Fitbit (Google) | Garmin | Samsung Galaxy Watch |
|-----------|-------------|-----------------|--------|---------------------|
| Heart rate (continuous) | Yes | Yes | Yes | Yes |
| Blood oxygen | Yes | Yes (premium) | Yes | Yes |
| Sleep stages | Yes | Yes | Yes | Yes |
| Menstrual cycle | Yes | Yes | No | Yes |
| GPS location | Yes | Yes | Yes | Yes |
| Electrocardiogram | Yes | Yes (select) | No | Yes |
| Skin temperature | Yes | Yes | Yes | Yes |
| Data sharing with third parties | Limited (health app permissions) | Google advertising ecosystem | Limited | Samsung ecosystem |
| HIPAA coverage | No | No | No | No |
| Data retention period | User-controlled | Until account deletion | Until account deletion | Until account deletion |

Sources: Device manufacturer privacy policies (2024); Consumer Reports analysis.

### Smart Home Security Devices

| Practice | Ring (Amazon) | Nest (Google) | Arlo | Wyze |
|----------|--------------|---------------|------|------|
| Video storage | Cloud (30-180 days) | Cloud (30-60 days) | Cloud (30 days) | Cloud (14 days) or local |
| Law enforcement sharing | 2,000+ agency partnerships; can request without warrant via "emergency" exception | Responds to legal process | Responds to legal process | Responds to legal process |
| Facial recognition | Disabled (2020) | On-device processing | Cloud-based option | On-device |
| Neighbor sharing | Neighbors app (opt-in sharing) | No equivalent | No equivalent | No equivalent |
| Employee access to footage | Documented incidents of unauthorized access | Undisclosed | Undisclosed | Data breach (2019) |
| Audio recording | Yes (microphone) | Yes (microphone) | Yes (microphone) | Yes (microphone) |

Sources: EFF, "Atlas of Surveillance" (2024); Ring transparency reports; *The Intercept* (2019); Wyze breach reporting (2019).

## Data Flows and Ecosystem

### How Smart Device Data Moves

| Stage | Description | Privacy Risk |
|-------|-------------|-------------|
| **Collection** | Device sensors capture audio, video, location, usage patterns | Over-collection beyond device function |
| **Transmission** | Data sent to manufacturer cloud servers, often unencrypted or minimally encrypted | Interception, unauthorized access |
| **Processing** | Cloud-based analysis, AI training, feature computation | Data used for purposes beyond user expectation |
| **Storage** | Retained indefinitely in manufacturer databases | Breach exposure, law enforcement access |
| **Sharing** | Transferred to advertisers, data brokers, analytics firms, partners | Loss of user control, secondary uses |
| **Government access** | Provided to law enforcement via warrant, subpoena, or voluntary disclosure | Surveillance without user knowledge |
| **Aggregation** | Combined with data from other sources to build comprehensive profiles | Profiling beyond any single device's data |

### Third-Party Data Recipients

| Recipient Category | Data Received | Source Devices | Purpose |
|--------------------|---------------|----------------|---------|
| **Advertisers** | Viewing habits, purchase intent, demographics | Smart TVs, speakers, phones | Targeted advertising |
| **Data brokers** | Location, behavior patterns, device data | Vehicles, wearables, home devices | Resale, profiling |
| **Insurance companies** | Driving behavior, health metrics, home security | Vehicles, wearables, smart home | Risk assessment, pricing |
| **Law enforcement** | Video footage, location history, voice recordings | Cameras, speakers, vehicles | Criminal investigation |
| **AI training companies** | Voice samples, usage patterns | Speakers, assistants | Machine learning model training |
| **Research firms** | Anonymized usage patterns | All categories | Market research |
| **Third-party app developers** | Device state, usage data, some personal data | Smart home platforms, wearables | App functionality, advertising |

## Regulatory Landscape

### Federal Law

| Law | Applicability to IoT | Gaps |
|-----|---------------------|------|
| **FTC Act Section 5** | Can pursue unfair/deceptive practices by device makers | No IoT-specific rules; reactive enforcement only |
| **COPPA** (1998) | Applies to connected toys and devices targeting children under 13 | Weak enforcement; many devices used by children not "directed to" them |
| **Wiretap Act** (18 U.S.C. 2510) | Prohibits unauthorized interception of communications | Consent exceptions; unclear application to always-on microphones |
| **Computer Fraud and Abuse Act** | Addresses unauthorized access to computer systems | Focused on hacking, not manufacturer data collection |
| **HIPAA** | Covers health data at covered entities | Does not apply to wearable health data from consumer devices |
| **IoT Cybersecurity Improvement Act** (2020) | Requires security standards for federal IoT procurement | Applies only to government purchases, not consumer devices |
| **No comprehensive IoT privacy law** | N/A | The fundamental regulatory gap |

### State Laws

| State | Relevant Law | IoT Applicability |
|-------|-------------|-------------------|
| **California** | CCPA/CPRA (2020/2023) | Covers IoT data as "personal information"; opt-out of sale rights |
| **Illinois** | BIPA (2008) | Covers biometric data from IoT devices (voice prints, facial recognition) |
| **Oregon** | Consumer Privacy Act (2024) | Includes IoT data in comprehensive privacy framework |
| **Connecticut** | Data Privacy Act (2023) | General IoT coverage through broad privacy law |
| **Texas** | Data Privacy and Security Act (2024) | Covers IoT data; AG enforcement |
| **19+ states** | Various comprehensive privacy laws | Varying degrees of IoT coverage |

### FTC Enforcement Actions

| Year | Target | Issue | Outcome |
|------|--------|-------|---------|
| 2017 | Vizio | ACR tracking without consent on 11M TVs | $2.2 million settlement |
| 2019 | Ring | Employee access to customer video feeds | FTC investigation, internal reforms |
| 2023 | Ring (Amazon) | Failure to restrict employee access; lax security | $5.8 million settlement |
| 2023 | Amazon (Alexa) | Retaining children's voice recordings; geolocation data | $25 million settlement |
| 2024 | Verkada | Security camera company failed to protect footage | $2.95 million settlement |

Source: FTC enforcement database (2017-2024).

### International Comparison

| Jurisdiction | Framework | IoT-Specific Provisions |
|--------------|-----------|------------------------|
| **EU** | GDPR + Cyber Resilience Act (2024) | Mandatory security requirements; data protection by design; purpose limitation |
| **UK** | Product Security and Telecommunications Infrastructure Act (2022) | Bans default passwords; requires vulnerability disclosure; minimum update periods |
| **Japan** | IoT Security Guidelines (2024) | Government-led security standards for IoT manufacturers |
| **Singapore** | Cybersecurity Labelling Scheme | Voluntary security ratings for consumer IoT devices |
| **Australia** | Code of Practice for IoT (voluntary) | Security recommendations; proposed mandatory standards |

## Consumer Awareness

### Public Attitudes Toward Smart Device Privacy

| Finding | Percentage | Source |
|---------|-----------|--------|
| Concerned about smart speaker always listening | 63% | Morning Consult (2023) |
| Do not read smart device privacy policies | 91% | Deloitte, "Digital Consumer Trends" (2024) |
| Would pay more for a privacy-focused device | 48% | Cisco, "Consumer Privacy Survey" (2023) |
| Unaware that smart TV tracks viewing | 46% | Consumer Reports (2023) |
| Believe smart devices share data without consent | 72% | Pew Research Center (2024) |
| Have adjusted device privacy settings | 28% | Parks Associates (2024) |

## Trends (2023-2025)

- **AI integration**: Large language models being embedded in smart devices, creating new data flows and privacy considerations
- **Matter protocol adoption**: Cross-platform smart home standard increasing interoperability but also data sharing between ecosystems
- **Vehicle data monetization**: Automakers increasingly treating data as a revenue stream, with subscription models for features
- **Health monitoring expansion**: Wearables adding medical-grade sensors (blood glucose, blood pressure) without corresponding HIPAA coverage
- **Edge AI processing**: Some manufacturers moving processing on-device, potentially improving privacy but also enabling new local surveillance capabilities
- **Generative AI in home devices**: Amazon, Google, and Apple integrating generative AI into assistants, raising questions about training data from home interactions

## The Gap

| What Exists | What Is Needed | Current Status |
|-------------|----------------|----------------|
| FTC case-by-case enforcement | Comprehensive federal IoT privacy law | No specific legislation pending |
| Manufacturer self-regulation | Mandatory privacy-by-design requirements | Voluntary standards largely ignored |
| Opt-out mechanisms (some states) | Opt-in consent for all data collection beyond device function | Only California approaches this standard |
| Device-level privacy settings | Standardized privacy labels and disclosures | No mandatory labeling requirement |
| HIPAA for healthcare providers | Health data protections for wearable/IoT health data | Consumer health data unprotected |
| IoT security for government devices | Security standards for all consumer IoT devices | Only federal procurement covered |
| Post-breach notification | Proactive security requirements and testing | No pre-market security certification |

## Sources

- Cisco, "Consumer Privacy Survey" (2023)
- Consumer Reports, "Smart TV Privacy" (2023)
- Deloitte, "Connectivity and Mobile Trends Survey" (2024)
- EFF, "Atlas of Surveillance" (2024)
- eMarketer, "US Wearable Users" (2024)
- FTC enforcement records (2017-2024)
- McKinsey, "Monetizing Car Data" (2023)
- Morning Consult, "Smart Speaker Consumer Survey" (2023)
- Mozilla Foundation, "*Privacy Not Included: Cars" (2023)
- Palo Alto Networks, "IoT Threat Report" (2023)
- Parks Associates, "Smart Home Dashboard" (2024)
- Pew Research Center, "Americans and Digital Privacy" (2024)
- S&P Global Mobility, "Connected Car Report" (2024)
- Statista, "IoT Connected Devices" and "Smart Home Market" (2024)

## Related Topics

- [Commercial Surveillance](../commercial-surveillance/01-overview.md) - Device manufacturers as surveillance companies
- [Data Brokers](../data-brokers/01-overview.md) - IoT data in broker ecosystem
- [Location Tracking](../location-tracking/01-overview.md) - Device-based location surveillance
- [Privacy Overview](../01-overview.md) - Broader privacy context

## Document Navigation

- Previous: [Overview](01-overview.md)
- Next: [History](03-history.md)
