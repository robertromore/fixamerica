# Location Tracking: Overview

## Executive Summary

Location tracking represents one of the most pervasive and revealing forms of surveillance in modern America. Every smartphone is a tracking device, and the data it generates -- precise GPS coordinates, cell tower connections, WiFi access point associations, and Bluetooth beacon interactions -- creates a detailed record of where a person goes, when, for how long, and how often. This data reveals political affiliations (rally attendance), religious practices (house of worship visits), health conditions (clinic visits), romantic relationships (overnight stays), and virtually every other aspect of private life. Yet location data is collected, sold, and used with minimal legal constraint.

The Supreme Court's landmark decision in *Carpenter v. United States* (2018) recognized that historical cell-site location information is protected by the Fourth Amendment, requiring a warrant for government access. However, *Carpenter* left enormous gaps: it addressed only government acquisition through legal compulsion, not government purchases of commercial location data; it covered cell-site data but not GPS or app-based location data; and it said nothing about private-sector collection and sale. Government agencies -- particularly ICE, CBP, and the IRS -- have exploited these gaps by purchasing location data from commercial brokers, effectively circumventing the warrant requirement that *Carpenter* established.

On the commercial side, approximately 600 apps on the average American smartphone request location access (Pew Research Center, 2024). Location data brokers like SafeGraph, Placer.ai, and Babel Street aggregate this data and sell it to advertisers, retailers, real estate developers, hedge funds, and government agencies. The data is often described as "anonymized," but extensive research demonstrates that anonymized location data can be re-identified with 95%+ accuracy using just four data points (Nature, de Montjoye et al., 2013; confirmed by subsequent studies). The result is a commercial surveillance infrastructure that tracks the physical movements of virtually every American adult, with no meaningful consent, no right of access, and no effective way to opt out.

## Scope

### What This Subtopic Covers

- **Mobile device tracking**: GPS, cell tower triangulation, WiFi positioning, Bluetooth beacons
- **App-based location collection**: Mobile apps that collect and share location data
- **Location data brokers**: Companies that aggregate and sell location data
- **Government acquisition of location data**: Law enforcement and intelligence agency purchases
- **Geofence warrants and reverse location searches**: Law enforcement requests for all devices in an area
- **Vehicle tracking**: Connected cars, license plate readers, fleet management
- **Retail and commercial tracking**: In-store tracking, foot traffic analytics
- **Legal framework**: *Carpenter*, ECPA, state laws, and regulatory gaps

### What This Subtopic Does Not Cover

- **GPS tracking of employees by employers**: Covered in [Workplace Surveillance](../workplace-surveillance/01-overview.md)
- **Government surveillance programs broadly**: Covered in [Government Surveillance](../government-surveillance/01-overview.md)
- **Data broker industry broadly**: Covered in [Data Brokers](../data-brokers/01-overview.md)
- **Biometric identification from surveillance cameras**: Covered in [Biometric Privacy](../biometric-privacy/01-overview.md)

### Key Terms

| Term | Definition |
|------|------------|
| **Cell-site location information (CSLI)** | Records of which cell towers a phone connects to, revealing approximate location; the data type at issue in *Carpenter v. United States* |
| **Geofence warrant** | A court order directing a technology company to provide information on all devices present within a specified geographic area during a specified time period |
| **Reverse location search** | Law enforcement technique requesting data on all devices in an area, rather than data on a specific suspect's device |
| **Location data broker** | A company that aggregates location data from apps, carriers, and other sources and sells it to third parties |
| **Advertising ID** | A unique device identifier (IDFA on Apple, GAID on Android) used for advertising targeting; links location data to a persistent identity |
| **Geofencing** | Creating a virtual boundary around a physical location to trigger actions when a device enters or leaves the area |
| **De-anonymization** | The process of re-identifying individuals from supposedly anonymized location data by cross-referencing movement patterns with known locations |
| **Real-time bidding (RTB)** | Automated advertising auctions that expose device location to hundreds or thousands of companies in milliseconds |

## Key Facts

| Fact | Detail | Source |
|------|--------|--------|
| Americans carrying trackable devices | 97% of adults own a smartphone | Pew Research Center, "Mobile Fact Sheet" (2024) |
| Apps requesting location access (average) | ~600 apps per phone request location permission | AppCensus, mobile app analysis (2023) |
| Location data re-identification accuracy | 95%+ of individuals identifiable from 4 spatiotemporal data points | de Montjoye et al., "Unique in the Crowd," *Nature Scientific Reports* (2013) |
| Location data broker market size | $14+ billion (location intelligence segment) | MarketsandMarkets, "Location Intelligence Market" (2024) |
| Geofence warrant requests to Google (2020) | 11,554 requests affecting 25%+ of all Google device-related legal requests | Google Transparency Report (2022; last year reported before policy change) |
| Government agencies purchasing location data | ICE, CBP, IRS, FBI, DHS, DEA, Secret Service, DIA | Georgetown Law, "American Dragnet" (2022); *New York Times*, *Wall Street Journal* reporting |
| Apple App Tracking Transparency opt-in rate | 25% of users opt in to tracking (75% opt out) | Flurry Analytics (2023) |
| License plate reader scans per year (US) | 2.5+ billion | DRN (Digital Recognition Network) / Motorola Solutions estimates (2024) |
| Connected car data sharing with insurers | 77% of major automakers share or sell vehicle data | Mozilla Foundation, "*Privacy Not Included: Cars" (2023) |

## Core Tensions

- **Convenience vs. privacy**: Location-based services (navigation, ride-sharing, weather, emergency response) require some location data, but collection far exceeds necessity
- **Law enforcement utility vs. constitutional rights**: Location data is valuable for investigations, but warrantless access undermines Fourth Amendment protections
- **Commercial value vs. individual control**: Location data powers a multibillion-dollar industry; individual data rights threaten revenue models
- **Security vs. anonymity**: Tracking dangerous individuals requires surveillance capabilities that can also target innocent people
- **Technology innovation vs. regulation**: Rapidly evolving tracking technology outpaces legislative frameworks
- **National security vs. civil liberties**: Intelligence agencies argue location data is essential for threat assessment; critics see mass surveillance

## Key Questions

1. How is location data collected from smartphones, vehicles, and IoT devices, and who has access to it?
2. What did *Carpenter v. United States* actually protect, and what gaps remain?
3. How do government agencies use commercial location data purchases to circumvent warrant requirements?
4. Can location data be meaningfully anonymized, or is de-anonymization inevitable?
5. What role do geofence warrants play in modern law enforcement, and what are their constitutional implications?
6. How does location tracking disproportionately affect minority communities, immigrants, and reproductive healthcare patients?
7. What reforms would establish meaningful control over personal location data?

## Vision of Success

A reformed location data landscape would feature:

- **Warrant requirement for all government location access**: Including purchases of commercial data, closing the *Carpenter* gap
- **Meaningful consent for commercial collection**: Opt-in rather than opt-out; granular permissions for location data sharing with third parties
- **Data minimization**: Collection limited to what is necessary for the specific service requested
- **Anonymization standards**: Legally enforceable standards for de-identification with penalties for re-identification
- **Geofence warrant reform**: Strict probable cause, minimization, and scope requirements for reverse location searches
- **Location data broker regulation**: Registration, transparency, consent, and deletion rights for location data
- **Vehicle tracking limits**: Restrictions on automaker collection and sale of connected car location data
- **Right to location privacy**: Enforceable individual right to control disclosure of one's physical movements

## Related Topics

### Within Privacy

| Subtopic | Connection |
|----------|------------|
| [Workplace Surveillance](../workplace-surveillance/01-overview.md) | Employer GPS tracking of vehicles and devices |
| [Data Brokers](../data-brokers/01-overview.md) | Location data is among the most valuable categories brokers sell |
| [Government Surveillance](../government-surveillance/01-overview.md) | Government purchases of commercial location data |
| [Commercial Surveillance](../commercial-surveillance/01-overview.md) | App-based location collection feeds advertising ecosystem |
| [Smart Devices](../smart-devices/01-overview.md) | IoT devices generate location and presence data |

### Other FixAmerica Topics

| Topic | Connection |
|-------|------------|
| [Justice](../../justice/01-overview.md) | Geofence warrants, predictive policing, and location-based investigations |
| [Immigration](../../immigration/01-overview.md) | ICE/CBP use of location data for immigration enforcement |
| [Healthcare](../../healthcare/01-overview.md) | Location data revealing visits to reproductive, mental health, and addiction clinics |
| [Technology](../../technology/01-overview.md) | Advertising technology infrastructure enabling location tracking |

### Parent Topic

- [Privacy Overview](../01-overview.md)

## Document Navigation

| Document | Contents |
|----------|----------|
| [Current State](02-current-state.md) | Tracking technologies, legal landscape, and market data |
| [History](03-history.md) | Evolution from physical surveillance to digital location tracking |
| [Root Causes](04-root-causes.md) | Why location tracking is pervasive and unregulated |
| [Stakeholders](05-stakeholders.md) | Who profits, who is harmed, and who has power |
| [Opposition](06-opposition.md) | Who opposes regulation and how to counter arguments |
| [Solutions](07-solutions.md) | Policy proposals for location privacy protection |
| [Roadmap](08-roadmap.md) | Path to comprehensive location privacy reform |
| [Resources](09-resources.md) | Research, organizations, and data sources |
| [Actions](10-actions.md) | What individuals and communities can do |
| [Legislation](11-legislation.md) | Draft federal and state legislation |
| [Perspectives](12-perspectives.md) | Political perspectives analysis |
