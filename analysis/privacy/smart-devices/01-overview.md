# Smart Devices and IoT: Overview

## Executive Summary

Smart devices -- including voice assistants, connected appliances, wearable fitness trackers, smart televisions, connected vehicles, and the broader Internet of Things (IoT) -- have transformed American homes, workplaces, and public spaces into environments of continuous data collection. Over 300 million IoT devices are estimated to be in use in US households as of 2025, collectively generating billions of data points daily about intimate aspects of daily life: conversations, health metrics, sleep patterns, location movements, energy usage, and behavioral routines. This pervasive instrumentation of physical spaces represents one of the most significant privacy challenges of the digital age, yet the legal framework governing these devices remains fragmented, outdated, and largely inadequate.

The core privacy problem with smart devices is the combination of always-on sensors with opaque data practices. A smart speaker's microphone is perpetually listening for wake words, but may also capture private conversations that are transmitted to cloud servers and reviewed by human contractors. A connected vehicle records driving patterns, location history, and even cabin conversations, then shares that data with insurance companies, data brokers, and law enforcement -- often without meaningful driver consent. Smart televisions track viewing habits through automated content recognition and sell that information to advertisers. Fitness trackers and health wearables generate medical-grade data that falls outside HIPAA protections because the data is collected by consumer electronics companies rather than healthcare providers.

The regulatory vacuum surrounding smart device privacy results from multiple failures: the sectoral approach to US privacy law that leaves gaps between regulated categories; the outdated assumption that meaningful consent can be obtained through terms of service that no one reads; the lack of a federal privacy agency with IoT-specific expertise; and the powerful economic incentives that drive manufacturers to monetize user data as a secondary revenue stream. While the European Union has begun addressing IoT privacy through GDPR enforcement and the Cyber Resilience Act, the United States has taken a largely hands-off approach, leaving consumers to navigate a marketplace where surveillance is the default and privacy is a luxury.

## Scope

### What This Subtopic Covers

- **Smart home devices**: Voice assistants (Amazon Echo, Google Nest, Apple HomePod), smart speakers, smart displays, and home automation hubs
- **Connected appliances**: Smart refrigerators, thermostats, lighting, security cameras, doorbells, and robot vacuums
- **Wearable technology**: Fitness trackers, smartwatches, health monitors, and augmented/virtual reality headsets
- **Connected vehicles**: Telematics, infotainment systems, autonomous driving sensors, and vehicle-to-infrastructure communication
- **Smart televisions**: Viewing data collection, automated content recognition, and advertising targeting
- **IoT infrastructure**: Edge computing, cloud processing, data retention, and cross-device data sharing
- **Children's devices**: Smart toys, educational tablets, and connected baby monitors

### What This Subtopic Does Not Cover

- **Government surveillance systems**: Covered in [Government Surveillance](../government-surveillance/01-overview.md)
- **Workplace IoT monitoring**: Covered in [Workplace Surveillance](../workplace-surveillance/01-overview.md)
- **Data broker resale of IoT data**: Covered in [Data Brokers](../data-brokers/01-overview.md)
- **Biometric data from devices**: Covered in [Biometric Privacy](../biometric-privacy/01-overview.md)
- **Children's online activity broadly**: Covered in [Children's Privacy](../childrens-privacy/01-overview.md)

### Key Terms

| Term | Definition |
|------|------------|
| **Internet of Things (IoT)** | Network of physical objects embedded with sensors, software, and connectivity to collect and exchange data |
| **Always-on listening** | Device capability where microphones remain active to detect wake words or voice commands |
| **Automated Content Recognition (ACR)** | Technology in smart TVs that identifies audio or visual content being played to track viewing habits |
| **Telematics** | Vehicle-based technology that transmits driving data including speed, location, braking, and acceleration |
| **Edge computing** | Data processing performed on or near the device rather than transmitted to cloud servers |
| **Data minimization** | Principle that devices should collect only the data necessary for their stated function |
| **Firmware update** | Software update to a device's embedded operating system, which can change data collection practices |
| **Device fingerprinting** | Identifying specific devices based on unique characteristics of their hardware, software, or network behavior |

## Key Facts

| Fact | Detail | Source |
|------|--------|--------|
| IoT devices in US homes | 300+ million consumer IoT devices in use | Statista, "IoT Connected Devices in the US" (2024) |
| Smart speaker ownership | 35% of US adults own at least one smart speaker | Pew Research Center, "Mobile Technology and Home Broadband" (2024) |
| Connected vehicle data | Average connected car generates 25 GB of data per hour | McKinsey, "Monetizing Car Data" (2023) |
| Smart TV data collection | 87% of smart TVs use ACR technology | Consumer Reports, "Smart TV Privacy" (2023) |
| Voice assistant recordings reviewed by humans | Amazon, Google, Apple confirmed human review of recordings | Bloomberg (2019), *The Guardian* (2019), Apple newsroom (2019) |
| Data shared by connected car makers | 84% of car brands share or sell driver data | Mozilla Foundation, "*Privacy Not Included: Cars" (2023) |
| IoT security vulnerabilities | 57% of IoT devices vulnerable to medium- or high-severity attacks | Palo Alto Networks, "IoT Threat Report" (2023) |
| Ring doorbell police partnerships | 2,000+ law enforcement agencies had Ring partnerships | EFF, "Atlas of Surveillance" (2024) |
| Fitness tracker health data sales | Health app data sold without HIPAA protections | Duke University Health Data Study (2023) |
| Children's smart toy data breaches | VTech (6.4M children, 2015), CloudPets (800K, 2017) | FTC enforcement records |

## Core Tensions

- **Convenience vs. surveillance**: Smart devices provide genuine utility but require continuous data collection that enables surveillance
- **Innovation vs. regulation**: Rapid IoT development creates new privacy risks faster than lawmakers can address them
- **Personalization vs. privacy**: Device features improve with more data, creating incentives to collect maximally
- **Security vs. openness**: IoT security requires updates and monitoring, but these mechanisms can also expand surveillance
- **Consumer choice vs. market reality**: Consumers theoretically choose which devices to buy, but privacy-respecting alternatives are scarce and costly
- **Individual consent vs. ambient collection**: IoT devices collect data about everyone in their vicinity, not just the device owner

## Key Questions

1. How much data do common smart devices collect, and where does that data go after collection?
2. What are the actual privacy harms caused by smart device data collection, and who is most affected?
3. Why does US law fail to adequately protect consumers from IoT surveillance, and what legal reforms are needed?
4. How do smart device manufacturers monetize user data, and how significant is this revenue stream?
5. What role do connected vehicles play in the broader surveillance ecosystem, and what data do they share?
6. How can consumers make informed choices about smart devices when privacy practices are opaque?
7. What standards should apply to IoT data security, retention, and sharing?

## Vision of Success

A reformed smart device landscape would feature:

- **Privacy by design**: Devices engineered to minimize data collection, process data locally, and default to the most privacy-protective settings
- **Meaningful transparency**: Clear, standardized privacy labels on device packaging and in marketing materials, modeled on nutrition labels
- **Genuine consent**: Granular opt-in controls for each category of data collection, with devices fully functional without consenting to data sharing
- **Data minimization requirements**: Legal limits on collecting data beyond what is necessary for the device's stated function
- **Security standards**: Mandatory minimum security requirements including encryption, update commitments, and vulnerability disclosure
- **Third-party sharing restrictions**: Prohibitions on selling IoT data to data brokers, advertisers, or law enforcement without a warrant
- **Ambient collection protections**: Rights for non-owners who are recorded or monitored by others' smart devices
- **Children's protections**: Enhanced safeguards for devices marketed to or used by children

## Related Topics

### Within Privacy

| Subtopic | Connection |
|----------|------------|
| [Commercial Surveillance](../commercial-surveillance/01-overview.md) | Smart device manufacturers as surveillance actors |
| [Data Brokers](../data-brokers/01-overview.md) | IoT data flows to and through data broker networks |
| [Location Tracking](../location-tracking/01-overview.md) | Smart devices as major sources of location data |
| [Biometric Privacy](../biometric-privacy/01-overview.md) | Voice prints, facial recognition, and health biometrics from devices |
| [Children's Privacy](../childrens-privacy/01-overview.md) | Smart toys and children's devices as privacy risks |

### Other FixAmerica Topics

| Topic | Connection |
|-------|------------|
| [Technology](../../technology/01-overview.md) | IoT industry structure, AI integration, market dynamics |
| [Housing](../../housing/01-overview.md) | Smart home devices as condition of tenancy in some rental properties |
| [Healthcare](../../healthcare/01-overview.md) | Wearable health data outside HIPAA protections |
| [Justice](../../justice/01-overview.md) | Law enforcement use of IoT data and device partnerships |

### Parent Topic

- [Privacy Overview](../01-overview.md)

## Document Navigation

| Document | Contents |
|----------|----------|
| [Current State](02-current-state.md) | Market data, device categories, and current data practices |
| [History](03-history.md) | Evolution from early connected devices to ubiquitous IoT |
| [Root Causes](04-root-causes.md) | Why smart device privacy remains unprotected |
| [Stakeholders](05-stakeholders.md) | Manufacturers, consumers, regulators, and intermediaries |
| [Opposition](06-opposition.md) | Who opposes smart device privacy regulation and why |
| [Solutions](07-solutions.md) | Technical, regulatory, and market-based reforms |
| [Roadmap](08-roadmap.md) | Path to comprehensive IoT privacy protection |
| [Resources](09-resources.md) | Research, organizations, and tools |
| [Actions](10-actions.md) | What individuals and communities can do |
| [Legislation](11-legislation.md) | Draft federal and state legislation |
| [Perspectives](12-perspectives.md) | Political perspectives analysis |
