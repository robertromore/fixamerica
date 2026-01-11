# Surveillance Technology in Criminal Justice: Current State

## Overview of Current Deployment

Surveillance technology has become deeply embedded in American law enforcement, with tools ranging from sophisticated biometric systems to neighborhood camera networks. This document examines the current landscape of surveillance technology deployment across the United States.

---

## Facial Recognition Technology

### Current Deployment

Facial recognition is now used by the majority of federal law enforcement agencies and an increasing number of state and local police departments:

| Agency Type | Estimated Usage | Primary Databases |
|-------------|-----------------|-------------------|
| Federal (FBI, ICE, CBP, DEA) | Universal | NGI, IDENT, state DMV photos |
| State Police | 49 of 50 states | State databases, FBI NGI |
| Local Police (large cities) | 65%+ | Varies by vendor/contract |
| Local Police (all) | 25%+ | Commercial and government databases |

### Major Systems in Use

| System | Vendor | Notable Features | Concerns |
|--------|--------|------------------|----------|
| Clearview AI | Clearview AI | 30+ billion images scraped from internet | Scraped without consent, sold to private entities |
| Amazon Rekognition | Amazon | Real-time video analysis | High error rates, sold to ICE |
| NEC NeoFace | NEC Corporation | Used in major airports, stadiums | Accuracy claims unverified |
| Cognitec | Cognitec Systems | DMV and law enforcement integration | Black-box algorithm |
| DataWorks Plus | DataWorks Plus | State-level systems | Limited independent testing |

### Known Wrongful Identification Cases

- Robert Williams (Detroit, 2020): Arrested based on faulty facial recognition match
- Nijeer Parks (New Jersey, 2019): Spent 10 days in jail based on false facial recognition match
- Michael Oliver (Detroit, 2019): Wrongly accused of grabbing phone, based on facial recognition
- Randal Reid (Georgia, 2022): Arrested for crime 600 miles from his location

---

## Predictive Policing Algorithms

### Current Systems

| System | Developer | Deployment | Methodology |
|--------|-----------|------------|-------------|
| PredPol (now Geolitica) | Geolitica | 60+ cities (declining) | Place-based prediction |
| HunchLab | ShotSpotter | Discontinued 2021 | Place and person-based |
| Palantir Gotham | Palantir Technologies | LAPD, NOPD, federal agencies | Integrated data analysis |
| KeyStats | KeyStats Inc. | Various agencies | Place-based prediction |
| CivicScape | CivicScape | Limited deployment | Risk terrain modeling |

### Department Usage

| Major City | System(s) Used | Status |
|------------|----------------|--------|
| Los Angeles | PredPol, Palantir | Ended PredPol (2020), Palantir ongoing |
| Chicago | Strategic Subject List (discontinued) | Ended 2019 |
| New York | Domain Awareness System | Active, expanded |
| New Orleans | Palantir (secret until 2018) | Contract ended after exposure |
| Atlanta | Multiple vendors | Active |
| Oakland | PredPol | Banned 2020 |

---

## License Plate Readers (ALPRs)

### Deployment Statistics

| Category | Estimate |
|----------|----------|
| Total ALPRs in US | 100,000+ |
| States with ALPR databases | 50 |
| Scans collected annually | 2.5+ billion |
| Average retention period | 1-5 years (varies) |
| Percentage capturing innocent drivers | 99%+ |

### Major ALPR Networks

| Network/Vendor | Coverage | Data Sharing |
|----------------|----------|--------------|
| Vigilant Solutions (Motorola) | 9 billion+ scans | Cross-jurisdictional |
| MVTRAC | 5 billion+ scans | 150+ agencies |
| LEARN | Law Enforcement Records Management | State-level networks |
| DRN (Digital Recognition Network) | 15 billion+ scans | Repo/insurance to police |

### Private ALPR Networks

| Company | Primary Business | Police Access |
|---------|------------------|---------------|
| Repo companies | Vehicle repossession | Sells/shares data |
| Insurance companies | Claims investigation | Sells/shares data |
| Parking enforcement | Violation tracking | Sells/shares data |
| Private security | Property monitoring | Partners with police |

---

## Cell Site Simulators (Stingrays)

### Known Deployment

Cell site simulators (also called IMSI catchers or Stingrays) are used by numerous agencies, though secrecy agreements make full documentation difficult:

| Agency Type | Confirmed Users |
|-------------|-----------------|
| Federal | FBI, DEA, ICE, CBP, NSA, Secret Service, IRS, ATF |
| State | At least 27 state police agencies |
| Local | 60+ local police departments |
| Military | All branches |

### Technical Capabilities

| Capability | Description |
|------------|-------------|
| IMSI capture | Identifies all phones in range |
| Location tracking | Pinpoints device location |
| Call interception | Can intercept calls (with upgrade) |
| Denial of service | Can block all cellular service |
| Dragnet surveillance | Captures all nearby devices |

---

## Social Media Monitoring

### Vendor Landscape

| Vendor | Product | Law Enforcement Customers |
|--------|---------|---------------------------|
| Babel Street | Locate X, analytics | DHS, FBI, state/local |
| Media Sonar | Social media monitoring | Various agencies |
| ShadowDragon | SocialNet | DHS, police departments |
| Palantir | Integrated analytics | Multiple federal/local |
| Geofeedia | (Discontinued 2016) | Baltimore, Oakland (historical) |
| Dataminr | Real-time alerts | Law enforcement nationwide |

### Documented Uses

- Monitoring Black Lives Matter protests
- Tracking immigration activists
- Surveilling Muslim communities
- Monitoring environmental protesters
- Gang database population
- Predictive threat assessment

---

## Body Cameras

### Deployment Statistics

| Category | Statistic |
|----------|-----------|
| Large departments with body cameras | 80%+ |
| Officers with body cameras | 47% nationwide |
| Annual spending on body cameras | $500+ million |
| Major vendors | Axon (70%+ market share), Motorola, Getac |

### Current Issues

| Issue | Description |
|-------|-------------|
| Selective activation | Officers control when cameras record |
| Limited access | Footage access restricted, expensive |
| Retention policies | Vary widely, often too short |
| Facial recognition integration | Increasing vendor capabilities |
| Storage and costs | Municipalities struggle with expenses |
| Effectiveness disputes | Studies show mixed results on use of force |

---

## Ring/Neighbors Partnerships

### Partnership Statistics

| Category | Current Status |
|----------|----------------|
| Police departments partnered | 2,000+ |
| Neighbors app users | 10+ million |
| Countries with partnerships | US, UK, others |
| Video requests annually | Hundreds of thousands |

### Concerns

- No warrant required for video requests
- Users may not understand implications
- Creates distributed surveillance network
- Amplifies racial profiling
- Amazon profits from fear-based marketing
- Minimal oversight of police access

---

## Gunshot Detection (ShotSpotter/SoundThinking)

### Deployment

| Category | Data |
|----------|------|
| Cities using ShotSpotter | 130+ |
| Square miles covered | 1,100+ |
| Annual cost per square mile | $65,000-$95,000 |
| Sensors deployed | 25,000+ |

### Accuracy Concerns

| Finding | Source |
|---------|--------|
| 86% of Chicago alerts: no gun found | MacArthur Justice Center |
| 89% of alerts: no casings found | Chicago Inspector General |
| Company can manually modify alerts | Vice News investigation |
| Officers alter reports to match ShotSpotter | Exposed in court cases |

### Cities That Have Ended Contracts

- Chicago (2024)
- Detroit (paused)
- San Antonio
- Charlotte
- Fall River, MA

---

## Drone Surveillance

### Current Law Enforcement Usage

| Category | Status |
|----------|--------|
| Agencies with drones | 1,700+ |
| Federal agencies | CBP, FBI, DEA, others |
| Uses | Surveillance, search/rescue, crowd monitoring |
| Facial recognition capable | Increasing |

### Concerns

- Persistent surveillance capability
- Weaponization potential
- Limited regulation
- Chinese-manufactured drones (DJI) security concerns

---

## Integrated Systems and Data Fusion

### Fusion Centers

| Category | Data |
|----------|------|
| Total fusion centers | 80+ nationwide |
| Staffing | 4,000+ personnel |
| Information sources | Hundreds per center |
| Oversight | Minimal federal oversight |

### Data Integration

Modern policing increasingly combines multiple surveillance streams:

- License plate + facial recognition + social media
- Cell location + predictive analytics + criminal databases
- Body camera footage + facial recognition
- Private camera networks + ALPR + gunshot detection

---

## Federal Surveillance Programs

### Key Programs

| Program/Database | Agency | Scope |
|------------------|--------|-------|
| Next Generation Identification (NGI) | FBI | 150+ million facial records |
| IDENT/HART | DHS | 270+ million biometric records |
| TECS | CBP | Border crossing records |
| EAGLE/FALCON | ICE | Location tracking |
| Hemisphere | DEA (AT&T partnership) | All US phone call records |

---

## Geographic Disparities

### Surveillance Concentration

| Factor | Pattern |
|--------|---------|
| Facial recognition | Heaviest in airports, urban centers |
| Predictive policing | Concentrated in low-income/minority areas |
| ALPR | Higher density in surveillance-heavy cities |
| ShotSpotter | Exclusively in low-income, minority neighborhoods |
| Stop and frisk + surveillance | Compounding effects in targeted areas |

---

## Document Navigation

| Previous | Current | Next |
|----------|---------|------|
| [01-overview.md](01-overview.md) | [02-current-state.md](02-current-state.md) | [03-history.md](03-history.md) |

**All Documents in This Series:**
- [01-overview.md](01-overview.md) - Executive Summary
- [02-current-state.md](02-current-state.md) - Current State of Surveillance Technology
- [03-history.md](03-history.md) - Historical Development
- [04-root-causes.md](04-root-causes.md) - Root Causes of Expansion
- [05-stakeholders.md](05-stakeholders.md) - Key Stakeholders
- [06-opposition.md](06-opposition.md) - Opposition to Reform
- [07-solutions.md](07-solutions.md) - Proposed Solutions
- [08-roadmap.md](08-roadmap.md) - Implementation Roadmap
- [09-resources.md](09-resources.md) - Resources and Further Reading
- [10-actions.md](10-actions.md) - Action Guide
- [11-legislation.md](11-legislation.md) - Model Legislation
