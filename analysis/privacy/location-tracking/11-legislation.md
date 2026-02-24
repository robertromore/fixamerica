# Location Tracking: Legislation and Legal Framework

## Overview

Location privacy legislation must close the *Carpenter* gap by requiring warrants for all government access to location data, establish meaningful consent and data minimization for commercial collection, reform geofence warrants, regulate the location data broker industry, and address connected vehicle data. This document proposes federal legislation, state model legislation, and regulatory frameworks to create comprehensive location privacy protection. The legislative approach operates within current constitutional doctrine while pushing for maximum protection consistent with the Fourth Amendment's evolving digital-age interpretation.

## Federal Legislation

### Location Privacy Protection Act

**Purpose**: Establish comprehensive federal location data protection covering both government access and commercial collection, closing the *Carpenter* gap and creating individual location privacy rights.

**Draft Text**:

```text
SEC. 1. SHORT TITLE.

This Act may be cited as the "Location Privacy Protection Act".

SEC. 2. DEFINITIONS.

(a) LOCATION DATA.--The term "location data" means any
information derived from the operation of a technology or
service that is capable of identifying, with reasonable
precision, the past, present, or projected physical location
of an individual or device, including but not limited to--
    (1) Global Positioning System (GPS) data;
    (2) cell-site location information (CSLI);
    (3) WiFi positioning or access point association data;
    (4) Bluetooth beacon or proximity data;
    (5) IP address geolocation;
    (6) advertising identifier data linked to physical location;
    (7) real-time bidding data containing geographic coordinates;
    (8) connected vehicle telematics or navigation data;
    (9) automated license plate reader data;
    (10) sensor fusion data combining multiple location signals;
    (11) any data used to infer or derive physical location; and
    (12) metadata from which physical location can be determined.

(b) COVERED ENTITY.--The term "covered entity" means any person
or entity that collects, processes, sells, shares, or otherwise
obtains location data, excluding--
    (1) a natural person acting in a personal or household
    capacity; and
    (2) a governmental entity, which is separately governed
    by Section 4 of this Act.

(c) PRECISE LOCATION DATA.--The term "precise location data"
means location data that identifies the physical location of
an individual or device with a precision of 1,750 feet
(approximately one-third of a mile) or less.

(d) SENSITIVE LOCATION.--The term "sensitive location" means--
    (1) a health care facility, including reproductive health
    clinics, mental health providers, and substance abuse
    treatment centers;
    (2) a place of religious worship;
    (3) a location primarily used for political meetings,
    protests, or rallies;
    (4) a domestic violence shelter or victim services facility;
    (5) a school or child care facility;
    (6) an immigration services facility or court; and
    (7) any other location designated by the Federal Trade
    Commission through rulemaking.

SEC. 3. COMMERCIAL LOCATION DATA PROTECTIONS.

(a) CONSENT REQUIREMENT.--A covered entity may not collect
precise location data unless the individual has provided
affirmative, informed consent that is--
    (1) specific to the collection of location data and the
    purposes for which it will be used;
    (2) freely given and not bundled with consent for unrelated
    purposes or conditioned on use of the service except where
    location data is strictly necessary for the core service;
    (3) revocable at any time through a mechanism as easy as
    the method by which consent was granted; and
    (4) documented and retained by the covered entity.

(b) SEPARATE CONSENT FOR SHARING.--A covered entity may not
share, sell, or otherwise transfer precise location data to
a third party unless the individual has provided separate,
specific consent for such transfer that identifies--
    (1) the categories of third parties that will receive
    the data;
    (2) the purposes for which the third party will use the
    data; and
    (3) the retention period for the third party's use.

(c) DATA MINIMIZATION.--A covered entity shall--
    (1) collect only the location data reasonably necessary
    to provide the service or feature specifically requested
    by the individual;
    (2) use the least precise location data sufficient for
    the stated purpose;
    (3) limit the duration of location data retention to the
    minimum period necessary, and in no event longer than
    180 days without renewed consent; and
    (4) delete location data when no longer necessary for the
    stated purpose or upon the individual's request.

(d) BACKGROUND COLLECTION.--A covered entity may not collect
location data when the individual is not actively using the
entity's service or application unless the individual has
provided specific, separate consent for background location
data collection.

(e) SDK TRANSPARENCY.--A covered entity operating a mobile
application shall disclose in its privacy policy and in a
standardized machine-readable format all third-party software
development kits (SDKs) or code libraries embedded in the
application that access or transmit location data.

SEC. 4. GOVERNMENT ACCESS TO LOCATION DATA.

(a) WARRANT REQUIREMENT.--A governmental entity may not obtain
location data, whether through compulsory legal process,
purchase, license, or any other means, without a warrant
issued by a court of competent jurisdiction based on probable
cause.

(b) PURCHASE PROHIBITION.--The purchase, license, or other
acquisition of location data by a governmental entity from a
covered entity or data broker constitutes a search within the
meaning of the Fourth Amendment and shall require a warrant
under subsection (a).

(c) WARRANT PARTICULARITY.--A warrant for location data shall
specify--
    (1) the individual or specific device for which data is
    sought;
    (2) the time period covered, which may not exceed 60 days
    without renewal;
    (3) the geographic scope, if applicable; and
    (4) the particular crime being investigated or the basis
    for the probable cause determination.

(d) EMERGENCY EXCEPTION.--A governmental entity may obtain
location data without a warrant when--
    (1) there is an immediate threat to the life or safety
    of an individual;
    (2) the governmental entity, within 48 hours of obtaining
    the data, applies for a warrant to a court of competent
    jurisdiction; and
    (3) if the warrant application is denied, the data and
    any evidence derived therefrom is destroyed.

(e) GEOFENCE WARRANT RESTRICTIONS.--
    (1) PROHIBITION.--A governmental entity may not obtain a
    warrant or order directing a covered entity to provide
    location data for all individuals or devices present within
    a specified geographic area during a specified time period
    (a "geofence warrant" or "reverse location search") unless--
        (A) there is probable cause to believe a specific crime
        occurred in the geographic area during the time period;
        (B) the geographic area is no larger than reasonably
        necessary to identify the perpetrator;
        (C) the time period does not exceed 2 hours;
        (D) the warrant requires an initial return of
        anonymized data only;
        (E) de-anonymization of specific individuals requires
        a separate showing of particularized probable cause; and
        (F) all non-relevant data is destroyed within 72 hours.
    (2) REPORTING.--Each governmental entity shall report
    annually to Congress and to the public the number of
    geofence warrants sought, granted, and executed.

(f) SUPPRESSION REMEDY.--Location data obtained in violation
of this Section, and any evidence derived therefrom, shall be
inadmissible in any federal, state, or local proceeding.

SEC. 5. LOCATION DATA BROKER REGULATION.

(a) REGISTRATION.--Any person or entity that, in the regular
course of business, sells, licenses, or shares location data
concerning 5,000 or more individuals shall register with the
Federal Trade Commission within 180 days of the effective date
of this Act and annually thereafter.

(b) DISCLOSURE.--Registered location data brokers shall
publicly disclose--
    (1) the sources of location data collected;
    (2) the categories of customers to whom data is sold;
    (3) the number of individuals whose location data is held;
    (4) data retention periods; and
    (5) de-identification methods used, if any.

(c) PROHIBITION ON SENSITIVE LOCATION DATA.--No person may
sell, license, or share location data that reveals an
individual's visit to a sensitive location, as defined in
Section 2(d), unless the individual has provided explicit
consent for the specific disclosure.

(d) INDIVIDUAL RIGHTS.--An individual may--
    (1) request access to all location data held about them
    by a location data broker;
    (2) request deletion of their location data; and
    (3) opt out of the sale or sharing of their location data.

(e) RE-IDENTIFICATION PROHIBITION.--No person may attempt to
re-identify an individual from location data that has been
de-identified, and violation of this prohibition shall be
subject to criminal penalties under Section 7(c).

SEC. 6. CONNECTED VEHICLE DATA PROTECTIONS.

(a) CONSENT.--A manufacturer or operator of a connected vehicle
may not collect, share, sell, or otherwise transfer precise
location data or driving data unless the vehicle owner or
primary driver has provided affirmative, informed consent.

(b) INSURANCE DATA RESTRICTIONS.--Vehicle location data and
driving data may not be shared with insurance companies unless
the vehicle owner has provided specific, separate, written
consent for such sharing, and such consent has been renewed
within the preceding 12 months.

(c) RIGHT TO DISABLE.--Vehicle owners must be able to disable
non-safety-related location data collection without degrading
core vehicle functions including navigation, safety alerts,
and emergency services.

(d) AUTOMATED LICENSE PLATE READERS.--Data collected by
automated license plate reader systems shall be--
    (1) retained for no more than 30 days unless associated
    with an active criminal investigation; and
    (2) not sold or shared with private entities except
    pursuant to a valid court order.

SEC. 7. ENFORCEMENT.

(a) FTC ENFORCEMENT.--The Federal Trade Commission shall
enforce this Act as if a violation were an unfair or deceptive
act or practice under Section 5 of the FTC Act.

(b) STATE ATTORNEY GENERAL ENFORCEMENT.--A State attorney
general may bring a civil action in federal or state court
to enforce this Act on behalf of residents of the State.

(c) CRIMINAL PENALTIES.--
    (1) Any person who knowingly re-identifies an individual
    from de-identified location data in violation of
    Section 5(e) shall be fined not more than $250,000,
    imprisoned for not more than 5 years, or both.
    (2) Any government official who knowingly obtains location
    data in violation of Section 4 shall be fined not more
    than $100,000, imprisoned for not more than 3 years,
    or both.

(d) PRIVATE RIGHT OF ACTION.--Any individual whose location
data rights under this Act are violated may bring a civil
action and recover--
    (1) actual damages or statutory damages of not less than
    $2,500 and not more than $25,000 per violation;
    (2) reasonable attorney's fees and costs; and
    (3) injunctive or declaratory relief.

(e) CIVIL PENALTIES.--Civil penalties for violations shall
not exceed the greater of--
    (1) $50,000 per violation; or
    (2) 4 percent of the covered entity's annual gross
    revenue in the preceding fiscal year.

SEC. 8. PREEMPTION.

This Act establishes a federal floor and does not preempt any
State law that provides greater protection for location data
privacy.

SEC. 9. EFFECTIVE DATE.

(a) Sections 4, 5, and 6 shall take effect 6 months after
the date of enactment.

(b) Section 3 shall take effect 12 months after the date of
enactment for covered entities with annual revenue exceeding
$25,000,000.

(c) Section 3 shall take effect 24 months after the date of
enactment for all other covered entities.
```

**Explanation**:

- **Section 2**: Defines location data broadly and technology-neutrally, covering current and future location tracking methods, including advertising IDs, RTB data, connected vehicle data, and inferred location data
- **Section 3**: Replaces the current "consent fiction" with meaningful opt-in consent, separate consent for sharing, and strict data minimization
- **Section 4**: Closes the *Carpenter* gap by requiring warrants for all government access to location data, including purchases; includes geofence warrant restrictions codifying the 4th Circuit's *Chatrie* reasoning
- **Section 5**: Creates a comprehensive regulatory framework for location data brokers, including registration, transparency, sensitive location data prohibition, and individual rights
- **Section 6**: Directly addresses the connected vehicle data crisis revealed by the GM/LexisNexis scandal
- **Section 7**: Multi-layered enforcement with criminal penalties for re-identification and unlawful government access, FTC and state AG enforcement, and private right of action with meaningful statutory damages
- **Section 8**: Floor-not-ceiling preemption preserves stronger state protections

**Potential Challenges**:

| Challenge | Response |
|-----------|----------|
| First Amendment claims | Location data regulation targets commercial conduct, not speech; *Carpenter* recognized location data's privacy significance |
| Commerce Clause scope | Location data flows interstate; Congress has broad authority over interstate commercial data practices |
| Law enforcement opposition | Emergency exception addresses time-sensitive cases; warrant process is familiar and efficient |
| National security objections | Include FISA Court oversight for national security location data requests rather than no oversight |
| Industry compliance costs | Graduated effective dates and revenue thresholds address burden on small entities |

**Refinements**:

- Add safe harbor for entities that implement privacy-by-design and conduct annual location data audits
- Include specific provisions for real-time bidding location data leakage restrictions
- Create an advisory committee including privacy technologists, civil liberties advocates, and law enforcement representatives
- Require biennial review of location data definitions to capture new tracking technologies

---

### Fourth Amendment Is Not For Sale Act (Existing Proposal)

**Purpose**: Specifically prohibit government agencies from purchasing location data and other personal information from data brokers without a warrant. This bill has been introduced by Sen. Wyden in multiple Congresses.

**Key provisions** (as proposed):

- Prohibits government agencies from purchasing personal data, including location data, from data brokers
- Requires a court order for government access to data held by third-party intermediaries
- Closes the "purchase" loophole in *Carpenter*
- Applies to all federal, state, and local government agencies

**Status**: Reintroduced in 119th Congress; bipartisan support but has not advanced to floor vote.

---

## State Model Legislation

### Model State Location Privacy Act

**Purpose**: State-level location data protection for states without comprehensive location privacy legislation, providing both government access restrictions and commercial data protections.

**Draft Text**:

```text
SECTION 1. SHORT TITLE.

This Act may be cited as the "[State] Location Privacy Act".

SECTION 2. DEFINITIONS.

(a) "Location data" means information capable of identifying,
with reasonable precision, the past, present, or projected
physical location of an individual or device, including GPS
data, cell-site location information, WiFi positioning data,
Bluetooth beacon data, connected vehicle data, and any
technology-derived data from which physical location can be
determined.

(b) "Covered entity" means any person or entity that collects,
processes, sells, or shares location data in the course of
business.

SECTION 3. GOVERNMENT ACCESS.

(a) A government entity of this State may not obtain location
data without a warrant issued by a court of competent
jurisdiction upon a finding of probable cause.

(b) The prohibition in subsection (a) includes obtaining
location data by purchase, license, or other acquisition
from data brokers or other commercial sources.

(c) A government entity may obtain location data without a
warrant only when there is an immediate threat to the life
or safety of an individual, provided that a warrant application
is submitted within 48 hours.

(d) Geofence warrants or reverse location searches shall
comply with the particularity requirements of the Fourth
Amendment and the [State] Constitution. A geofence warrant
may not request data on all devices in a geographic area
exceeding [500 feet radius] for a time period exceeding
[2 hours].

SECTION 4. COMMERCIAL PROTECTIONS.

(a) A covered entity shall not collect precise location data
without the affirmative consent of the individual.

(b) A covered entity shall not sell or share location data
with a third party without separate, specific consent.

(c) A covered entity shall delete location data when no
longer necessary for the purpose for which it was collected,
and in no event later than 180 days after collection.

SECTION 5. INDIVIDUAL RIGHTS.

An individual may:
    (a) request access to their location data held by a
    covered entity;
    (b) request deletion of their location data;
    (c) opt out of the sale or sharing of their location data.

SECTION 6. PRIVATE RIGHT OF ACTION.

Any individual whose rights under this Act are violated may
bring a civil action and recover actual damages, statutory
damages of $5,000 per violation, and reasonable attorney's
fees.

SECTION 7. NO WAIVER.

Any contract provision waiving rights under this Act is void
and unenforceable.
```

**Adaptations**: States should customize the geofence warrant geographic and temporal limits, the statutory damages amount, and the definitions to align with existing state privacy frameworks. States with comprehensive privacy laws (California, Colorado, Connecticut, Virginia) may integrate these provisions into existing statutes.

---

## Regulatory Framework

### FTC Location Data Rulemaking

**Existing Authority**: FTC Act Section 5; general unfairness and deception authority.

**Proposed Regulations**:

- Define "location data" broadly for purposes of Section 5 enforcement, including advertising ID-linked location, RTB-broadcast location, and inferred location
- Require mobile app developers to display standardized location privacy labels disclosing all location data collection, sharing, and retention practices
- Establish consent requirements for location data sharing with third parties by non-HIPAA entities
- Prohibit deceptive claims of location data anonymization when de-identification methods are insufficient to prevent re-identification
- Require location data breach notification for all entities experiencing a breach of precise location data

### DOT/NHTSA Connected Vehicle Data Rulemaking

**Existing Authority**: National Highway Traffic Safety Administration authority over vehicle safety and consumer protection.

**Proposed Regulations**:

- Require automakers to provide standardized, plain-language disclosure of all location and driving data collected
- Mandate opt-in consent for sharing vehicle data with third parties including insurers
- Require that vehicle owners can disable non-safety data collection through a simple, accessible mechanism
- Establish data retention limits for vehicle location data

---

## Legal Considerations

### Constitutional Issues

- **Fourth Amendment**: *Carpenter* established that location data is constitutionally protected; the proposed warrant requirement extends this principle to all government acquisition methods. The emergency exception preserves government access for genuine emergencies. *United States v. Chatrie* (4th Circuit, 2024) provides strong precedent for geofence warrant restrictions.
- **First Amendment**: Location data regulation may face challenges similar to *Sorrell v. IMS Health Inc.*, 564 U.S. 552 (2011), which struck down restrictions on sale of prescriber-identifying data. Legislation should be drafted to target commercial conduct (collection, sale, sharing) rather than speech. The significant government interest in preventing surveillance harms and protecting Fourth Amendment values supports intermediate scrutiny.
- **Commerce Clause**: Federal location data legislation rests on Congress's power to regulate interstate commerce. Location data flows freely across state lines through RTB, data brokers, and cloud services; the interstate nexus is unambiguous.
- **Tenth Amendment**: The warrant requirement for state and local government access to commercial location data is supportable under Section 5 of the Fourteenth Amendment (enforcing due process) and the Supremacy Clause.

### Preemption Questions

- The proposed federal floor approach preserves stronger state laws (California CCPA/CPRA, Utah Location Data Protection Act, Illinois Location Privacy Protection Act)
- Industry will push for ceiling preemption to replace stronger state laws with weaker federal standards; this should be resisted
- The floor-not-ceiling model follows precedent from HIPAA and numerous federal consumer protection statutes

### Enforcement Mechanisms

- Multi-layered enforcement (FTC, state AGs, private right of action, criminal penalties) is essential given the scale of location data collection
- Private right of action with statutory damages is the single most important enforcement mechanism; government agencies are resource-constrained and cannot address millions of individual violations
- Criminal penalties for re-identification and unlawful government access create meaningful deterrence for the most harmful conduct
- Suppression remedy for unlawful government access creates immediate incentive for compliance

---

## Loopholes, Shortcomings, and Rectification

### Location Privacy Protection Act

#### Potential Loopholes

| Loophole | Description | Severity |
|----------|-------------|----------|
| Definition circumvention | Companies may develop new location-inference technologies not explicitly covered by the definition | Medium |
| Consent fatigue | Frequent consent requests across many apps may lead to automatic approval | Medium |
| Aggregate data exception | Companies may argue that aggregate foot traffic data does not constitute "location data" about individuals | High |
| Foreign data processing | Companies may process location data outside US jurisdiction to avoid coverage | Medium |
| Carrier CSLI retention | Act does not address carrier data retention periods for CSLI, which may be indefinite | Medium |
| National security exception creep | National security justifications may expand to swallow the warrant requirement | High |
| SDK layering | Location data may pass through multiple SDK intermediaries, making consent chain unclear | Medium |

#### Shortcomings

| Issue | Impact | Root Cause |
|-------|--------|------------|
| Revenue threshold exempts small entities initially | Small apps and developers can collect without compliance during phase-in | Political compromise to reduce industry opposition |
| Geofence warrant restrictions allow narrow exceptions | Even narrow geofence warrants implicate innocent bystanders | Compromise with law enforcement to secure passage |
| No data portability mandate for location history | Individuals cannot transfer location data between services | Technical complexity |
| ALPR retention limit (30 days) may be too long | 30 days of license plate reader retention enables significant tracking | Compromise with law enforcement |

#### Rectification Procedures

1. Use technology-neutral definition language ("any data from which physical location can be determined") and grant FTC authority to update definitions through rulemaking as new technologies emerge
2. Mandate standardized, simplified consent interfaces for location data to reduce consent fatigue; require consent interfaces to be submitted to FTC for review
3. Clarify that aggregate location data derived from individual-level tracking constitutes "location data" when it can be combined with other data to identify individuals
4. Apply the Act extraterritorially to any entity processing location data of US residents, regardless of processing location
5. Set maximum CSLI retention periods for carriers (7 days without warrant; longer retention only pursuant to preservation order)
6. Require annual reporting on national security exceptions; create inspector general oversight of classified location data programs
7. Require each entity in the SDK data chain to obtain and pass through consent, with liability for the originating app developer

### Government Access Provisions

#### Potential Loopholes

| Loophole | Description | Severity |
|----------|-------------|----------|
| "Publicly available" exception | Government may argue location data posted on social media or visible through apps is "publicly available" and exempt from warrant requirement | High |
| Foreign intelligence sharing | Foreign intelligence agencies may collect location data on Americans and share it with US agencies, bypassing domestic warrant requirements | High |
| Consent exception exploitation | Government may pressure individuals to "consent" to location monitoring as condition of bail, probation, or immigration proceedings | Medium |
| Parallel construction | Agencies may use warrantless location data to develop leads, then construct a parallel legal basis for the investigation | High |

#### Rectification Procedures

1. Define "publicly available" narrowly to exclude data obtained through deception, data aggregation from multiple sources, or data requiring technical tools to access
2. Prohibit US agencies from using foreign-collected location data on US persons without a warrant; include intelligence community in the Act's coverage
3. Prohibit government conditioning of benefits, release, or immigration status on consent to location monitoring absent a valid court order
4. Require agencies to disclose the initial source of location data leads in all criminal proceedings; suppression remedy applies to evidence discovered through unlawful location data access

### General Implementation Concerns

#### Systemic Issues

| Issue | Proposed Solution |
|-------|------------------|
| Enforcement funding inadequacy | Tie enforcement funding to penalty revenue; create dedicated location privacy enforcement fund |
| Technology evolution outpacing law | Require biennial FTC review and update of definitions and technical standards |
| International data transfers | Require adequacy assessments for cross-border location data transfers |
| AI-inferred location | Explicitly include AI-derived location inferences in the definition of location data |
| RTB infrastructure leakage | Require advertising exchanges to implement technical safeguards limiting location precision in bid requests |

#### Sunset and Review Provisions

- Require GAO report on implementation effectiveness within 3 years of enactment
- Mandate FTC annual report on location data practices and enforcement activities
- Include 5-year review provision for congressional reassessment of definitions, thresholds, and technological developments
- Require DOJ annual report on geofence warrant usage and compliance with restrictions

---

## References

- U.S. Const. amend. IV
- Electronic Communications Privacy Act, 18 U.S.C. 2510-2522, 2701-2712 (1986)
- Communications Assistance for Law Enforcement Act, 47 U.S.C. 1001-1010 (1994)
- FTC Act, 15 U.S.C. 45 (Section 5)
- California Consumer Privacy Act / CPRA, Cal. Civ. Code 1798.100-1798.199.100
- Utah Location Data Protection Act, Utah Code 77-23c (2023)
- Illinois Location Privacy Protection Act, 740 ILCS 14.5 (2024)
- *Carpenter v. United States*, 585 U.S. 296 (2018)
- *United States v. Jones*, 565 U.S. 400 (2012)
- *United States v. Chatrie*, 4th Cir. (2024)
- *Katz v. United States*, 389 U.S. 347 (1967)
- *Smith v. Maryland*, 442 U.S. 735 (1979)
- *Sorrell v. IMS Health Inc.*, 564 U.S. 552 (2011)
- *FTC v. Kochava, Inc.*, No. 2:22-cv-00377 (D. Idaho, 2022)
- Georgetown Law Center on Privacy and Technology, "American Dragnet" (2022)
- de Montjoye et al., "Unique in the Crowd," *Nature Scientific Reports* (2013)
- Sen. Wyden, Fourth Amendment Is Not For Sale Act (introduced in multiple Congresses)
- Google Transparency Report, geofence warrant data (2022)
- Irish Council for Civil Liberties, "The Biggest Data Breach" (2022)

## Related Topics

- [Data Brokers: Legislation](../data-brokers/11-legislation.md) - Regulation of location data brokers within broader data broker framework
- [Government Surveillance: Legislation](../government-surveillance/11-legislation.md) - Government surveillance reform context
- [Consumer Data Rights: Legislation](../consumer-data-rights/11-legislation.md) - Comprehensive privacy legislation framework
- [Commercial Surveillance: Legislation](../commercial-surveillance/11-legislation.md) - Commercial data collection regulations
- [Privacy: Legislation](../11-legislation.md) - Parent topic legislation

## Document Navigation

- Previous: [Actions](10-actions.md)
- Next: [Perspectives](12-perspectives.md)
- Up: [Overview](01-overview.md)
