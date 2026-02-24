# Location Tracking: Solutions

## Overview

Comprehensive location privacy reform requires action across multiple dimensions: closing the *Carpenter* gap by requiring warrants for all government location data access, establishing consent and data minimization requirements for commercial collection, banning or restricting geofence warrants, regulating location data brokers, addressing connected vehicle data sharing, and empowering individuals with meaningful rights over their location data. The solutions proposed here are designed to be complementary and mutually reinforcing, addressing the structural causes identified in the root causes analysis.

---

## Solution 1: Close the Carpenter Gap -- Warrant Requirement for All Government Location Data Access

### The Problem

*Carpenter v. United States* (2018) required warrants for government access to historical CSLI obtained through compulsory legal process. However, government agencies have exploited the gap by purchasing commercial location data from brokers, effectively circumventing the warrant requirement. ICE, CBP, IRS, FBI, Secret Service, and DIA have all purchased location data without warrants (Georgetown Law, "American Dragnet," 2022).

### The Proposal

Enact federal legislation requiring a warrant based on probable cause for any government access to location data, regardless of the method of acquisition.

**Key elements:**

| Element | Description |
|---------|-------------|
| Universal warrant requirement | Government may not obtain location data -- through compulsion, purchase, or other means -- without a warrant |
| Broad definition of location data | Covers GPS, CSLI, WiFi, Bluetooth, advertising ID location, IP geolocation, and any other technology revealing physical location |
| No purchase exception | Purchasing commercially available location data constitutes a "search" requiring a warrant |
| Emergency exception | Allows warrantless access when there is an immediate threat to life or serious bodily harm, with post-hoc judicial review within 48 hours |
| Suppression remedy | Evidence obtained in violation of the warrant requirement is inadmissible |
| Duration limits | Warrants must specify the time period and geographic scope of requested location data |

**Model:** Sen. Wyden's Fourth Amendment Is Not For Sale Act (introduced in multiple Congresses)

### Evidence of Effectiveness

- States with warrant requirements for location data (Utah, Montana) have not reported degraded law enforcement effectiveness
- The warrant process is familiar and workable; federal magistrate judges process thousands of warrants daily
- The *Carpenter* court explicitly endorsed the warrant requirement as "the familiar and workable approach" for digital data
- International models (Germany, Canada) require judicial authorization for government access to location data

### Implementation Challenges

| Challenge | Mitigation |
|-----------|------------|
| Law enforcement resistance | Emergency exceptions address time-sensitive cases; warrant process is fast (often same-day) |
| National security agencies | Include national security exception with FISA Court oversight rather than no oversight |
| Existing data contracts | Grandfather clause for existing contracts with mandatory transition within 12 months |
| Definition of "location data" | Technology-neutral definition covering any data revealing physical location of an individual |

---

## Solution 2: Commercial Location Data Consent and Minimization

### The Problem

Approximately 70% of apps with location access share data with third parties (AppCensus, 2023). Users grant location permissions without understanding that their data will be sold to brokers, advertisers, and government agencies. Less than 9% of users read location privacy policies (Carnegie Mellon, 2023). The "consent" underlying current location data collection is a fiction.

### The Proposal

Enact federal legislation requiring opt-in consent for commercial location data collection and sharing, with strict data minimization requirements.

**Key elements:**

| Element | Description |
|---------|-------------|
| Opt-in consent for collection | Apps and services must obtain affirmative, specific consent before collecting precise location data |
| Separate consent for sharing | Sharing location data with third parties requires separate, specific consent distinct from collection consent |
| Data minimization | Collection limited to what is strictly necessary for the service requested; no over-collection for advertising or analytics |
| Purpose limitation | Location data collected for one purpose may not be repurposed without additional consent |
| Retention limits | Location data must be deleted within 30 days unless the user provides renewed consent for longer retention |
| Background collection ban | Apps may not collect location data when not actively in use unless the user has specifically consented to background collection |
| SDK transparency | Apps must disclose all third-party SDKs that access location data |

### Evidence of Effectiveness

- Apple's App Tracking Transparency (ATT) demonstrated that when given a clear choice, 75% of users opt out of tracking; this shifted $10+ billion in advertising revenue without destroying the app ecosystem
- GDPR's consent requirement for location data has not prevented European app developers from operating profitably
- California's CCPA/CPRA classifies precise geolocation as sensitive personal information requiring consent for sale/sharing; California's tech economy continues to thrive

### Implementation Challenges

| Challenge | Mitigation |
|-----------|------------|
| "Free" app business model disruption | Apps can use non-location-based advertising; subscription models are viable alternatives |
| Consent fatigue | Standardized, simple consent interfaces mandated by regulation reduce complexity |
| Small developer compliance costs | Graduated effective dates; compliance tools and guidance from FTC |
| SDK ecosystem complexity | Require app developers to audit and disclose all location-accessing SDKs |

---

## Solution 3: Geofence Warrant Reform

### The Problem

Geofence warrants (reverse location searches) request data on all devices present in a geographic area during a specific time period. Google received 11,554 geofence requests in 2020 alone, a 556% increase from 2018. These warrants identify potentially thousands of innocent people to find a suspect, violating the Fourth Amendment's particularity requirement. The 4th Circuit in *United States v. Chatrie* (2024) held geofence warrants unconstitutional, but no comprehensive federal legislation exists.

### The Proposal

Enact federal legislation prohibiting or strictly limiting geofence warrants and reverse location searches.

**Key elements:**

| Element | Description |
|---------|-------------|
| Prohibition on dragnet geofence warrants | Ban reverse location searches that seek data on all devices in an area without individualized suspicion |
| Narrow exception | Allow geofenced location requests only when: (1) probable cause exists for a specific crime; (2) the geographic area is narrowly drawn; (3) the time period does not exceed 2 hours; (4) minimization procedures destroy non-relevant data within 72 hours |
| Anonymization step | Any permitted geofence request must first return anonymized data; de-anonymization requires additional probable cause for specific individuals |
| Private right of action | Individuals identified through unlawful geofence warrants may sue for damages |
| Reporting requirements | Agencies must report geofence warrant usage annually to Congress and the public |

**Model:** New York and Utah geofence warrant restriction laws; 4th Circuit *Chatrie* decision

### Evidence of Effectiveness

- Google's decision to stop storing location data centrally (December 2023) demonstrated that companies can choose privacy-protective architectures
- The 4th Circuit's *Chatrie* decision found geofence warrants constitutionally deficient, validating reform arguments
- States restricting geofence warrants (Utah, Montana) have not reported negative effects on criminal investigations

---

## Solution 4: Location Data Broker Registration and Regulation

### The Problem

Location data brokers aggregate billions of location records from apps, carriers, and connected devices, selling them to advertisers, retailers, hedge funds, and government agencies with no registration, transparency, or consent requirements. The $14+ billion location intelligence market operates in a regulatory vacuum.

### The Proposal

Establish a comprehensive regulatory framework for location data brokers.

**Key elements:**

| Element | Description |
|---------|-------------|
| Registration requirement | All entities that sell or share location data must register with the FTC |
| Transparency obligations | Brokers must disclose data sources, categories of data, number of individuals tracked, customer categories, and data retention periods |
| Consent requirement | Location data may not be sold unless the original data subject provided affirmative consent for the sale |
| Prohibition on sensitive location data | Ban sale of location data revealing visits to health care facilities, religious institutions, political events, domestic violence shelters, and addiction treatment centers |
| Right to access and delete | Individuals can access and delete their location data held by brokers |
| Government purchase restrictions | Brokers may not sell location data to government agencies without a warrant |
| De-anonymization prohibition | Re-identification of location data claimed as de-identified is prohibited and carries criminal penalties |

**Model:** California's data broker registry; Vermont's data broker registration law

### Evidence of Effectiveness

- California's data broker registry has increased transparency about data broker operations
- FTC enforcement actions against Kochava and X-Mode/Outlogic demonstrate that location data broker regulation is feasible
- Vermont's data broker law has not caused broker industry flight from the state

---

## Solution 5: Connected Vehicle Privacy Protection

### The Problem

95% of new vehicles have built-in connectivity (Alliance for Automotive Innovation, 2024). 25 of 25 major automakers studied share or sell vehicle data (Mozilla Foundation, 2023). The GM/LexisNexis scandal (2024) revealed that OnStar driving and location data was shared with insurance companies, affecting premiums without clear driver consent.

### The Proposal

Enact connected vehicle privacy legislation addressing automaker data collection and sharing.

**Key elements:**

| Element | Description |
|---------|-------------|
| Opt-in consent for data sharing | Automakers may not share or sell vehicle location or driving data without affirmative consent |
| Data minimization | Vehicle data collection limited to what is necessary for vehicle safety, navigation, and requested services |
| Insurance data restrictions | Vehicle data may not be shared with insurers without specific, separate consent; prohibition on automatic data sharing through telematics partnerships |
| Right to disable tracking | Vehicle owners must be able to disable non-safety location tracking without degrading core vehicle functions |
| Transparency requirements | Automakers must disclose all data collection, sharing, and sale practices in standardized, plain-language format |
| ALPR restrictions | Automated license plate reader data may not be retained for more than 30 days without a law enforcement purpose |

**Model:** California Privacy Protection Agency rulemaking on connected vehicles (proposed 2025)

### Evidence of Effectiveness

- GM discontinued its OnStar Smart Driver program sharing data with LexisNexis after public backlash, demonstrating that public pressure can change industry practices
- European GDPR applies to connected vehicle data; European automakers comply while maintaining connected services

---

## Solution 6: Real-Time Bidding Location Data Leakage Restrictions

### The Problem

Real-time bidding (RTB) advertising auctions broadcast precise device location (latitude/longitude to 5+ decimal places) to hundreds or thousands of companies in milliseconds. The Irish Council for Civil Liberties (2022) called RTB "the biggest data breach" ever recorded, with 2+ billion US bid requests daily exposing location data.

### The Proposal

Regulate location data exposure through the advertising auction process.

**Key elements:**

| Element | Description |
|---------|-------------|
| Location precision limits | RTB bid requests may not include location data more precise than zip code/postal code level without user consent |
| Contractual restrictions | Advertising exchanges must contractually prohibit participants from aggregating location data from bid requests |
| Audit requirements | RTB platforms must conduct annual audits of location data handling by auction participants |
| Data retention limits | Location data received through RTB must be deleted within 24 hours if not used for the specific ad transaction |
| Enforcement | FTC enforcement with penalties of up to $50,000 per violation or 4% of annual revenue |

### Evidence of Effectiveness

- Apple's ATT and privacy-preserving ad attribution demonstrate that advertising can function with reduced location precision
- GDPR enforcement has driven some privacy improvements in European RTB systems
- The IAB's own Transparency and Consent Framework acknowledges that location data in RTB requires consent under GDPR

---

## Solution 7: Individual Location Privacy Rights

### The Problem

Americans have no enforceable right to control their location data. Only 18% of Americans feel they have control over their location data (Pew Research Center, 2023). There is no federal right to know who has location data, request deletion, or sue for violations.

### The Proposal

Establish a federal right to location privacy with individual enforcement.

**Key elements:**

| Element | Description |
|---------|-------------|
| Right to know | Individuals may request a list of all entities that hold their location data, including data source, retention period, and sharing history |
| Right to delete | Individuals may request deletion of their location data from any entity that holds it |
| Right to opt out of sale | Individuals may prohibit the sale or sharing of their location data at any time |
| Private right of action | Individuals may sue for violations with statutory damages ($1,000-$10,000 per violation) plus attorney's fees |
| Anti-retaliation | Entities may not deny services or degrade service quality for individuals who exercise location privacy rights |
| Data portability | Individuals may request their location data in a machine-readable format |

### Evidence of Effectiveness

- California's CCPA/CPRA provides deletion and opt-out rights for location data; compliance has been feasible
- GDPR provides similar individual rights for EU residents; enforced with significant penalties
- Private right of action creates meaningful enforcement incentive beyond resource-constrained government agencies

---

## Summary of Solutions

| Solution | Primary Target | Key Mechanism | Timeline |
|----------|---------------|---------------|----------|
| Close the Carpenter gap | Government agencies | Universal warrant requirement for location data access | Short-term (1-2 years) |
| Commercial consent and minimization | App developers, advertisers | Opt-in consent; data minimization mandates | Medium-term (2-3 years) |
| Geofence warrant reform | Law enforcement | Prohibition or strict limits on reverse location searches | Short-term (1-2 years) |
| Location data broker regulation | Data brokers | Registration, transparency, consent, deletion rights | Medium-term (2-3 years) |
| Connected vehicle privacy | Automakers | Opt-in consent for data sharing; insurance data restrictions | Medium-term (2-4 years) |
| RTB location data restrictions | Advertising exchanges | Location precision limits in bid requests | Medium-term (2-3 years) |
| Individual location privacy rights | All location data holders | Federal right to know, delete, and opt out with private right of action | Medium-term (2-4 years) |

---

## International Models

| Country/Region | Model | Key Lesson for U.S. |
|---------------|-------|---------------------|
| EU (GDPR) | Consent required for location data processing; classified as personal data | Data-based, not entity-based, regulation is feasible; innovation continues under strict rules |
| Germany | Strong restrictions on government access to location data; judicial authorization required | Warrant requirements are compatible with effective law enforcement |
| Canada | PIPEDA requires consent for location data collection; Privacy Commissioner enforcement | Federal privacy commissioner model for location data oversight |
| South Korea | Location Information Protection Act (2005); dedicated location data law | Sector-specific location privacy legislation is effective |
| Japan | Act on Protection of Personal Information covers location data with consent requirements | Technology-neutral privacy frameworks adapt to new location technologies |

## Document Navigation

- Previous: [Opposition](06-opposition.md)
- Next: [Roadmap](08-roadmap.md)
- Up: [Overview](01-overview.md)
