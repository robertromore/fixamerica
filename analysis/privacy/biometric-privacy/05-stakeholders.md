# Biometric Privacy: Stakeholders

## Overview

Biometric privacy involves a distinctive stakeholder landscape where law enforcement agencies, technology vendors, civil liberties organizations, and affected communities hold strongly divergent views. Unlike general consumer data rights, biometric privacy has a significant civil rights dimension due to accuracy disparities across racial groups and the use of biometric surveillance in policing.

## Primary Stakeholders

### Individuals Subject to Biometric Collection

| Group | Type of Collection | Consent Status | Risk Level |
|-------|-------------------|----------------|------------|
| All Americans | Consumer device biometrics (phones, laptops) | Generally consensual | Low-Moderate |
| Workers (30+ million) | Employer fingerprint/face time clocks | Often compelled | Moderate |
| Travelers (hundreds of millions) | CBP/TSA facial recognition and fingerprints | Compelled (with opt-out for citizens at airports) | Moderate |
| Social media users (billions) | Photo tagging, facial recognition | Previously non-consensual (Facebook); evolving | Moderate |
| Residents of surveilled areas | Law enforcement facial recognition | Non-consensual | High |
| Black Americans | Facial recognition with highest error rates | Non-consensual | Very High |
| Immigrants | DHS IDENT/HART biometric collection | Compelled | Very High |
| DNA test participants (40+ million) | Consumer genetics companies | Voluntary but with unclear downstream risks | Moderate-High |
| Shoppers in facial recognition stores | Retail surveillance | Non-consensual | Moderate |

### Law Enforcement Agencies

| Agency | Biometric Capability | Database Access |
|--------|---------------------|-----------------|
| FBI | NGI facial recognition, IAFIS fingerprints, CODIS DNA | 641+ million photos; 160+ million fingerprints; 21+ million DNA profiles |
| DHS/CBP | IDENT/HART, Traveler Verification Service | 260+ million identities |
| ICE | Access to FBI, DHS, commercial databases | Broad access through agreements |
| TSA | CAT-2 facial recognition at airports | 200+ airports |
| State/local police | Various (Clearview AI, state databases, FACE Services) | 3,100+ agencies using Clearview AI |
| State crime labs | DNA analysis, fingerprint processing | Varies by state |

### Biometric Technology Companies

| Company | Product | Market Segment | Revenue |
|---------|---------|---------------|---------|
| Clearview AI | Facial recognition (law enforcement) | Law enforcement | Private; estimated $30M+ |
| NEC Corporation | NeoFace facial recognition | Government, commercial | Part of NEC ($25B) |
| IDEMIA | Fingerprint, face, iris systems | Government, aviation, border | $2.5+ billion |
| Amazon (AWS) | Rekognition facial recognition | Commercial, (formerly) law enforcement | Part of AWS ($91B) |
| Microsoft | Azure Face API | Commercial, government | Part of Azure ($96B) |
| Apple | Face ID, Touch ID | Consumer devices | Part of Apple ($383B) |
| Genetec | Video analytics with facial recognition | Commercial, government | $500M+ (private) |
| Verkada | Building security cameras with analytics | Commercial | Private; $400M+ revenue |
| 23andMe | Consumer DNA testing | Direct-to-consumer | $299M (2023, declining) |
| Ancestry | Consumer DNA testing | Direct-to-consumer | Part of Blackstone portfolio |

### Employers Using Biometrics

| Sector | Use Case | Scale |
|--------|----------|-------|
| Manufacturing | Fingerprint time clocks | Millions of workers |
| Healthcare | Fingerprint/palm medication dispensing | Hundreds of thousands |
| Retail | Fingerprint/face time tracking | Millions of workers |
| Warehousing/logistics | Biometric access control and time tracking | Hundreds of thousands |
| Food service | Fingerprint time clocks | Millions of workers |

## Decision Makers

### Federal

| Actor | Role | Current Position |
|-------|------|-----------------|
| Congress (Commerce/Judiciary Committees) | Federal biometric privacy legislation | Multiple bills introduced; none advanced |
| FTC | Enforcement authority (Section 5) | Rite Aid action (2023); limited biometric-specific authority |
| NIST | Biometric accuracy testing (FRVT) | Publishes benchmark tests; no regulatory authority |
| FBI | Operates largest federal biometric databases | Opposes restrictions on database expansion |
| DHS | IDENT/HART system; border biometrics | Actively expanding capabilities; resists privacy limits |
| White House OSTP | AI and biometric policy coordination | Blueprint for AI Bill of Rights (2022) addressed biometrics |

### State

| Actor | Role | Current Position |
|-------|------|-----------------|
| Illinois legislature | BIPA enforcement and amendment | Annual pressure to weaken; so far resisted |
| Illinois courts | BIPA interpretation | Strong plaintiff-friendly rulings (*Rosenbach*, *Cothron*, *Tims*) |
| State legislatures (20+ states) | Considering biometric privacy bills | Most defeated by industry lobbying |
| State AGs | Enforcement of state biometric/privacy laws | TX AG $1.4B Meta settlement; growing activity |
| City councils | Local facial recognition bans | 20+ jurisdictions enacted bans |

## Advocacy Organizations

### Pro-Biometric Privacy

| Organization | Focus | Key Activities |
|-------------|-------|----------------|
| ACLU | Civil liberties, facial recognition | Litigation (*ACLU v. Clearview AI*); local ban campaigns |
| Electronic Frontier Foundation (EFF) | Digital rights | Litigation, advocacy, technical analysis |
| Georgetown Law Center on Privacy and Technology | Facial recognition research | *Perpetual Line-Up* report; Americas Face Recognition |
| Fight for the Future | Digital rights activism | Ban facial recognition campaigns; scorecards |
| Algorithmic Justice League | AI bias | Founded by Joy Buolamwini; accuracy disparity research |
| EPIC | Privacy policy | Federal advocacy; FTC comments |
| Leadership Conference on Civil and Human Rights | Civil rights coalition | Facial recognition as civil rights issue |
| Surveillance Technology Oversight Project (STOP) | NYC surveillance | Local surveillance tracking and advocacy |
| Color of Change | Racial justice | Facial recognition and policing |

### Pro-Industry / Anti-Regulation

| Organization | Position | Key Arguments |
|-------------|----------|---------------|
| Security Industry Association (SIA) | Industry trade group | Facial recognition is safe; regulation premature |
| International Biometrics + Identity Association (IBIA) | Industry trade group | Self-regulation; voluntary standards |
| U.S. Chamber of Commerce | Business coalition | BIPA-style laws create litigation crisis |
| Illinois Chamber of Commerce | State business coalition | BIPA damages excessive; reform needed |
| National Association of Manufacturers | Manufacturing sector | Biometric time clocks essential; BIPA burdensome |
| National Retail Federation | Retail sector | Facial recognition for loss prevention legitimate |

## Coalition Dynamics

### Pro-Regulation Coalition

| Coalition | Members | Strength |
|-----------|---------|----------|
| Civil rights + civil liberties | ACLU, Leadership Conference, Color of Change, EFF | Strong; public support; litigation capacity |
| Privacy advocates | EPIC, CDT, EFF, Georgetown CPPT | Technical expertise; research credibility |
| AI ethics researchers | Algorithmic Justice League, AI Now Institute | Scientific credibility on bias |
| Labor unions | Workers concerned about biometric time clocks | Moderate; varies by sector |
| City councils | Local ban movement | Growing; 20+ jurisdictions |

### Anti-Regulation Coalition

| Coalition | Members | Strength |
|-----------|---------|----------|
| Law enforcement | FBI, DHS, police associations, prosecutors | Strong political influence; national security framing |
| Biometric technology vendors | Clearview AI, NEC, IDEMIA | Government contracts; lobbying resources |
| Employer associations | Chamber, NAM, NRF | Economic impact framing |
| National security hawks | Congressional defense/intelligence committees | Security framing overrides privacy concerns |

## Power Asymmetry

| Stakeholder | Resources | Political Access | Information | Organized |
|-------------|-----------|------------------|-------------|-----------|
| Law enforcement agencies | High | Very High | High | Very High |
| Biometric tech vendors | High | High | Very High (proprietary) | High |
| Employer associations | High | High | Moderate | High |
| Civil liberties organizations | Low-Moderate | Moderate | High | High |
| AI ethics researchers | Low | Low-Moderate | Very High | Moderate |
| Workers subject to biometric clocks | Very Low | Very Low | Very Low | Low |
| Black Americans (accuracy disparities) | Very Low | Low | Low | Moderate |
| Immigrants (compelled collection) | Very Low | Very Low | Very Low | Very Low |

## Document Navigation

- Previous: [Root Causes](04-root-causes.md)
- Next: [Opposition](06-opposition.md)
- Up: [Biometric Privacy Overview](01-overview.md)
