# Smart Devices and IoT: Legislation and Legal Framework

## Overview

Smart device privacy reform requires legislation at multiple levels: federal law to establish baseline privacy and security standards for all consumer IoT devices, targeted legislation for high-risk categories like connected vehicles and children's devices, state model legislation to fill gaps and innovate beyond federal minimums, and regulatory frameworks to implement and enforce these standards. This document provides draft text for priority reforms.

## Constitutional Considerations

Smart device privacy legislation must navigate several constitutional issues. The Fourth Amendment's protections against unreasonable search and seizure apply to government access to IoT data, particularly after *Carpenter v. United States* (2018) expanded warrant requirements to digital data. The First Amendment may be invoked by manufacturers claiming data collection constitutes protected activity. The Commerce Clause supports federal regulation of the interstate IoT market but raises preemption questions regarding state laws. The following legislation is designed to withstand these challenges.

## Federal Legislation

### IoT Consumer Privacy and Security Act

**Purpose**: Establish comprehensive privacy and security standards for consumer IoT devices sold in the United States, including data minimization requirements, consent frameworks, and minimum security standards.

**Draft Text**:

```text
SEC. 1. SHORT TITLE.

This Act may be cited as the "IoT Consumer Privacy and
Security Act".

SEC. 2. DEFINITIONS.

In this Act:

(1) CONNECTED DEVICE.—The term "connected device" means any
    physical object that—
    (A) is capable of connecting to the internet or a local
        network, directly or indirectly;
    (B) is assigned an Internet Protocol address or Bluetooth
        address; and
    (C) is sold or distributed in the United States for
        consumer use.

(2) COVERED DATA.—The term "covered data" means any information
    collected, processed, stored, or transmitted by a connected
    device that—
    (A) identifies or is linked or reasonably linkable to an
        individual or household; or
    (B) is derived from the use of a connected device by an
        individual or household.

(3) SENSITIVE DATA.—The term "sensitive data" means covered data
    that includes—
    (A) biometric information;
    (B) precise geolocation data;
    (C) health-related data;
    (D) audio or video recordings of individuals;
    (E) data of individuals under 17 years of age;
    (F) financial information; or
    (G) data revealing race, ethnicity, religion, sexual
        orientation, or political affiliation.

(4) MANUFACTURER.—The term "manufacturer" means any person or
    entity that designs, produces, or sells connected devices
    for consumer use in the United States.

(5) CORE DEVICE FUNCTIONALITY.—The term "core device
    functionality" means the primary purpose for which a
    connected device is marketed and sold to consumers,
    excluding advertising, data monetization, or analytics
    services.

SEC. 3. DATA MINIMIZATION.

(a) IN GENERAL.—A manufacturer shall not collect, process,
    store, or transmit covered data beyond what is reasonably
    necessary to provide the core device functionality requested
    by the consumer.

(b) PROHIBITION ON CONDITIONING FUNCTIONALITY.—A manufacturer
    shall not condition the availability of core device
    functionality on a consumer's consent to data collection,
    processing, or sharing beyond what is strictly necessary
    for that functionality.

(c) DATA RETENTION LIMITS.—A manufacturer shall—
    (1) retain covered data only for as long as reasonably
        necessary to fulfill the purpose for which it was
        collected; and
    (2) delete covered data within 90 days of the purpose
        being fulfilled, unless the consumer affirmatively
        requests longer retention.

SEC. 4. CONSENT REQUIREMENTS.

(a) AFFIRMATIVE CONSENT.—A manufacturer shall obtain affirmative,
    informed consent from a consumer before—
    (1) collecting sensitive data;
    (2) sharing covered data with third parties for purposes
        beyond core device functionality;
    (3) using covered data for advertising or profiling; or
    (4) making material changes to data collection practices.

(b) FORM OF CONSENT.—Consent under this section shall be—
    (1) obtained through a clear, conspicuous, and specific
        request separate from other terms and conditions;
    (2) revocable at any time through a mechanism at least as
        easy as the method used to grant consent; and
    (3) not obtained through deceptive design patterns,
        including pre-checked boxes, confusing interfaces,
        or misleading language.

(c) AMBIENT COLLECTION NOTICE.—A manufacturer of a connected
    device that collects data about individuals other than the
    device owner shall—
    (1) provide clear visual or audible indicators when the
        device is actively collecting data; and
    (2) provide a mechanism for non-owners to learn about and
        limit data collection about themselves.

SEC. 5. CONSUMER RIGHTS.

(a) ACCESS.—A consumer shall have the right to access all covered
    data collected about them by a connected device, in a
    machine-readable format, within 30 days of request.

(b) DELETION.—A consumer shall have the right to request
    deletion of all covered data, and the manufacturer shall
    comply within 30 days.

(c) PORTABILITY.—A consumer shall have the right to export their
    covered data in a standardized, interoperable format.

(d) OPT-OUT OF SALE.—A consumer shall have the right to direct a
    manufacturer not to sell or share their covered data with
    third parties.

SEC. 6. PRIVACY LABELING.

(a) REQUIREMENT.—Each connected device sold in the United States
    shall display a standardized privacy label on its packaging,
    at point of sale, and in online product listings.

(b) LABEL CONTENTS.—The label shall disclose, in a standardized
    format prescribed by the Commission—
    (1) categories of data collected;
    (2) whether data is processed on-device or in the cloud;
    (3) third parties with whom data is shared;
    (4) data retention period;
    (5) security update commitment period; and
    (6) whether the device functions without internet
        connectivity.

(c) MACHINE-READABLE FORMAT.—Each label shall include a
    machine-readable component enabling automated comparison
    by consumer tools and applications.

SEC. 7. SECURITY REQUIREMENTS.

(a) MINIMUM STANDARDS.—Each connected device shall—
    (1) not use default or hardcoded passwords;
    (2) encrypt covered data in transit and at rest;
    (3) provide a mechanism for authenticated software updates;
    (4) maintain a vulnerability disclosure program; and
    (5) implement secure boot or equivalent integrity
        verification.

(b) UPDATE COMMITMENT.—Each manufacturer shall provide security
    updates for a period of not less than—
    (1) 5 years for devices with a retail price above $50; and
    (2) 3 years for devices with a retail price of $50 or
        below.

(c) END-OF-SUPPORT.—When a manufacturer ceases to provide
    security updates, it shall—
    (1) notify consumers at least 6 months in advance;
    (2) offer consumers a mechanism to delete all stored data;
        and
    (3) make reasonable efforts to enable continued core
        functionality without cloud services.

SEC. 8. RESTRICTIONS ON GOVERNMENT ACCESS.

(a) WARRANT REQUIREMENT.—No government entity shall access
    covered data from a manufacturer or connected device
    without a warrant issued upon probable cause, except—
    (1) with the affirmative consent of the device owner; or
    (2) in exigent circumstances involving imminent threat to
        life, subject to judicial review within 48 hours.

(b) PROHIBITION ON BULK ACCESS.—No government entity shall
    request or require bulk access to covered data from
    multiple consumers or devices absent individualized
    probable cause.

(c) TRANSPARENCY.—Each manufacturer shall publish an annual
    transparency report disclosing the number and nature of
    government data requests received and complied with.

SEC. 9. ENFORCEMENT.

(a) FTC ENFORCEMENT.—A violation of this Act shall be treated as
    an unfair or deceptive act or practice under Section 5 of
    the Federal Trade Commission Act.

(b) STATE ENFORCEMENT.—The attorney general of any State may
    bring a civil action to enforce this Act.

(c) PRIVATE RIGHT OF ACTION.—Any person injured by a violation
    of this Act may bring a civil action and recover—
    (1) actual damages;
    (2) statutory damages of not less than $100 and not more
        than $1,000 per violation per device; and
    (3) reasonable attorney's fees and costs.

(d) PENALTIES.—The Commission may impose civil penalties of not
    more than $50,000 per violation per day.

SEC. 10. PRESERVATION OF STATE LAW.

Nothing in this Act shall be construed to preempt, displace, or
supplant any State law that provides greater protection for
consumer privacy or connected device security.

SEC. 11. EFFECTIVE DATE.

This Act shall take effect 18 months after the date of enactment.
```

**Explanation**:

- Sections 1-2 establish scope and definitions broad enough to cover current and future IoT devices
- Section 3 addresses the core problem of over-collection through data minimization
- Section 4 establishes meaningful consent, including protections for non-owners affected by ambient collection
- Section 5 provides consumer data rights consistent with CCPA/CPRA and GDPR
- Section 6 mandates transparency through standardized privacy labels
- Section 7 establishes minimum security standards modeled on the UK Product Security Act
- Section 8 closes the government access loophole with warrant requirements
- Section 9 provides multiple enforcement mechanisms including private right of action
- Section 10 preserves stronger state protections

**Potential Challenges**:

- First Amendment challenges to restrictions on data collection as "speech"
- Industry arguments about compliance costs for small manufacturers
- Law enforcement opposition to warrant requirements
- Technical challenges in defining "core device functionality"

**Refinements**:

- Small business exemption for manufacturers with fewer than 50,000 devices sold annually
- Phased compliance timeline: labeling in Year 1, data minimization in Year 2, full compliance in Year 3
- Safe harbor for manufacturers who submit to independent privacy audits

### Connected Vehicle Privacy Protection Act

**Purpose**: Address the specific privacy risks of connected vehicles, including data sharing with insurers and data brokers.

**Draft Text**:

```text
SEC. 1. SHORT TITLE.

This Act may be cited as the "Connected Vehicle Privacy
Protection Act".

SEC. 2. DEFINITIONS.

(1) CONNECTED VEHICLE.—Any motor vehicle equipped with
    technology capable of collecting and transmitting data
    beyond the vehicle.

(2) VEHICLE DATA.—Information generated by or collected through
    a connected vehicle, including location, speed, driving
    behavior, cabin audio, biometrics, and passenger data.

(3) VEHICLE MANUFACTURER.—Any person or entity that manufactures,
    assembles, or imports connected vehicles for sale in the
    United States.

SEC. 3. CONSENT AND DISCLOSURE.

(a) A vehicle manufacturer shall not collect or transmit vehicle
    data beyond what is necessary for vehicle safety and
    operation without the express, informed consent of the
    vehicle owner or primary driver.

(b) Consent shall be obtained through a standalone disclosure
    separate from the vehicle purchase agreement.

(c) A vehicle manufacturer shall provide a clear, in-vehicle
    mechanism to disable non-essential data collection.

SEC. 4. PROHIBITION ON INSURER DATA SHARING.

(a) No vehicle manufacturer shall share, sell, or license vehicle
    data to an insurance company without the separate, written
    consent of the vehicle owner.

(b) No insurance company shall use vehicle data obtained without
    compliant consent for underwriting, pricing, or claims
    decisions.

(c) Violation of this section shall constitute an unfair trade
    practice.

SEC. 5. DATA PORTABILITY AND DELETION.

(a) Vehicle owners shall have the right to access and export all
    vehicle data in a machine-readable format.

(b) Vehicle owners shall have the right to delete all non-safety-
    critical vehicle data.

(c) When a vehicle is sold, the previous owner's personal data
    shall be automatically deleted.

SEC. 6. PRIVACY LABEL.

Each new connected vehicle shall display a privacy disclosure on
the window sticker (Monroney label) summarizing data collection
practices, third-party sharing, and data retention periods.

SEC. 7. ENFORCEMENT.

(a) Enforcement by the FTC and NHTSA, jointly.
(b) State AG enforcement authority.
(c) Private right of action with statutory damages of $500 to
    $5,000 per violation.

SEC. 8. EFFECTIVE DATE.

This Act shall apply to vehicles manufactured 12 months after
enactment.
```

**Explanation**: Targets the specific gap revealed by the GM/LexisNexis data sharing scandal, where driving behavior data was shared with insurance companies to raise rates without driver knowledge or consent.

**Potential Challenges**: Automaker lobbying; preemption arguments; technical definition of "safety-critical" data.

## State Model Legislation

### Model IoT Privacy Act

**Purpose**: State-level IoT privacy legislation for states seeking to act before federal law.

**Draft Text**:

```text
SECTION 1. SHORT TITLE.

This Act may be cited as the "[State] IoT Consumer Privacy Act".

SECTION 2. SCOPE.

This Act applies to any person or entity that manufactures,
sells, or distributes connected devices to consumers in this
State.

SECTION 3. DATA MINIMIZATION.

A manufacturer shall not collect data from a connected device
beyond what is reasonably necessary for the device's primary
advertised function.

SECTION 4. CONSENT.

(a) A manufacturer shall obtain opt-in consent before collecting
    sensitive data or sharing any data with third parties.

(b) Consent must be separate from general terms of service.

SECTION 5. CONSUMER RIGHTS.

Consumers shall have the right to access, delete, and port
their connected device data.

SECTION 6. SECURITY STANDARDS.

(a) Connected devices shall not use default passwords.
(b) Data in transit shall be encrypted.
(c) Manufacturers shall commit to a minimum security update
    period disclosed at point of sale.

SECTION 7. LANDLORD PROVISIONS.

(a) A landlord shall not require a tenant to use smart devices
    as a condition of tenancy without providing a non-connected
    alternative.

(b) A landlord shall not access data from smart devices
    installed in a rental unit.

SECTION 8. ENFORCEMENT.

(a) The Attorney General shall have enforcement authority.
(b) Violations constitute unfair trade practices under [State
    Consumer Protection Act].
(c) Private right of action with actual and statutory damages.

SECTION 9. EFFECTIVE DATE.

This Act takes effect on [date], 12 months after enactment.
```

**Adaptations**: States may adjust exemption thresholds, penalty amounts, and landlord provisions to local conditions.

## Regulatory Framework

### FTC IoT Privacy Rulemaking

| Element | Description |
|---------|-------------|
| **Authority** | Section 5 unfairness and deception authority; enhanced by proposed legislation |
| **Scope** | All consumer IoT devices sold in the US |
| **Key Rules** | Privacy label standards; data minimization guidance; consent requirements; security standards |
| **Timeline** | ANPRM within 6 months of legislation; NPRM within 18 months; final rule within 30 months |
| **Enforcement** | Civil penalties; consent orders; referral to DOJ for criminal violations |

### NIST IoT Privacy Framework

| Element | Description |
|---------|-------------|
| **Scope** | Technical standards for IoT privacy and security |
| **Key Standards** | Privacy label format; edge computing guidelines; data format interoperability; security testing criteria |
| **Process** | Multi-stakeholder development; public comment; regular revision cycle |
| **Coordination** | Alignment with EU Cyber Resilience Act; UK Product Security Act; ISO/IEC standards |

## Legal Considerations

### Constitutional Issues

| Issue | Analysis | Risk Level |
|-------|----------|------------|
| **First Amendment** | Data collection may be characterized as speech; however, *Sorrell v. IMS Health* (2011) does not preclude all data regulation; conduct vs. speech distinction | Medium |
| **Fourth Amendment** | Warrant requirements for government IoT access align with *Carpenter*; likely constitutional | Low |
| **Commerce Clause** | Federal regulation of interstate IoT market clearly within commerce power | Low |
| **Preemption** | Preserving state law (Section 10 of federal bill) avoids preemption conflicts | Low |
| **Due Process** | Civil penalties must be proportional; private right of action must include Article III standing | Low-Medium |

### Enforcement Mechanisms

| Mechanism | Advantages | Disadvantages |
|-----------|-----------|---------------|
| FTC enforcement | Existing infrastructure; national reach | Resource-constrained; slow process |
| State AG enforcement | Local expertise; political incentive | Uneven enforcement across states |
| Private right of action | Scalable; consumer empowerment; deterrence | Litigation costs; potential for frivolous suits |
| Industry self-regulation | Flexibility; lower compliance costs | History of failure; unenforceable |

## Loopholes, Shortcomings, and Rectification

### Potential Loopholes

| Loophole | Description | Severity |
|----------|-------------|----------|
| **"Necessary" data definition gaming** | Manufacturers may broadly define what data is "necessary" for core functionality to justify extensive collection | High |
| **Firmware update consent bypass** | Companies could introduce new data collection via firmware updates, arguing ongoing consent covers changes | High |
| **Third-party SDK data collection** | Manufacturers may argue they are not responsible for data collection by third-party software embedded in devices | Medium |
| **De-identification workaround** | Companies may claim data is "de-identified" to avoid consent requirements, when re-identification is feasible | High |
| **Device-to-device data sharing** | Data shared between devices within the same ecosystem may bypass "third party" sharing restrictions | Medium |
| **Business transfer exception** | Consumer data transferred during mergers or acquisitions without renewed consent | Medium |
| **Research exemption abuse** | Claiming data collection serves "product improvement research" to avoid minimization requirements | Medium |
| **Ambient collection limitations** | Difficulty enforcing notice requirements for non-owners in proximity to devices | High |

### Shortcomings

| Issue | Impact | Root Cause |
|-------|--------|------------|
| **No federal privacy agency** | Enforcement depends on under-resourced FTC | Political opposition to new agencies |
| **Retroactive data problem** | Law does not address data already collected before enactment | Constitutional limits on retroactive regulation |
| **International manufacturer reach** | Difficulty enforcing against manufacturers based outside the US | Jurisdictional limitations |
| **Rapid technology change** | Legislation may not cover new device categories or data types | Inherent limitation of prescriptive regulation |
| **Consumer fatigue** | Even with labels and rights, consumers may not exercise them | Behavioral economics; information overload |
| **Small device exemptions** | Low-cost devices may be exempt from some requirements | Proportionality concerns |

### Rectification Procedures

1. **Define "necessary" narrowly in regulations**: FTC rulemaking should establish specific, category-by-category definitions of what data is necessary for core functionality, using a "reasonable consumer expectation" standard.

2. **Require re-consent for material changes**: Any firmware update that materially changes data collection practices should trigger a new, separate consent request that is presented prominently before the update installs.

3. **Extend manufacturer liability to embedded third-party software**: Manufacturers should be jointly liable for data collection by SDKs and third-party software they incorporate into their devices.

4. **Establish de-identification standards**: FTC should promulgate specific technical standards for de-identification, with ongoing verification and penalties for re-identification.

5. **Include intra-ecosystem data sharing**: Define "third party" broadly to include affiliates and ecosystem partners, with separate consent required for cross-device data combination.

6. **Require data disposition plans for business transfers**: Mandate consumer notification and opt-out rights before data is transferred in mergers and acquisitions.

7. **Narrow research exemption**: Limit product improvement research to aggregated, anonymized data; prohibit use of individual-level data for research without explicit consent.

8. **Fund enforcement adequately**: Authorize and appropriate dedicated funding for FTC IoT enforcement, supplemented by penalty revenue.

9. **Build in technology-neutral principles**: Frame key provisions around principles (minimization, consent, transparency) rather than specific technologies to ensure adaptability.

10. **Create sunset and review provisions**: Require congressional review of the Act every 5 years with specific metrics for effectiveness evaluation.

### General Implementation Concerns

- **Industry compliance timeline**: 18 months may be insufficient for smaller manufacturers; consider tiered timelines based on company size
- **International coordination**: US-only standards may create compliance complexity; pursue mutual recognition with EU standards
- **Consumer education**: Labeling and rights are only effective if consumers understand them; allocate funding for public education
- **Enforcement capacity**: FTC will need additional staff and budget to oversee the IoT market; congressional appropriation is essential
- **Technology evolution**: The framework must be flexible enough to accommodate AI-integrated devices, AR/VR headsets, and brain-computer interfaces

## References

### Federal Law

- 15 U.S.C. 45 (FTC Act, Section 5)
- 15 U.S.C. 6501-6506 (COPPA)
- 18 U.S.C. 2510-2522 (Electronic Communications Privacy Act)
- Pub. L. 116-207 (IoT Cybersecurity Improvement Act of 2020)

### Court Cases

- *Carpenter v. United States*, 585 U.S. ___ (2018)
- *Riley v. California*, 573 U.S. 373 (2014)
- *Kyllo v. United States*, 533 U.S. 27 (2001)
- *Sorrell v. IMS Health Inc.*, 564 U.S. 552 (2011)

### State Laws

- California Consumer Privacy Act, Cal. Civ. Code 1798.100 et seq.
- Illinois Biometric Information Privacy Act, 740 ILCS 14
- California IoT Security Law, Cal. Civ. Code 1798.91.04 (SB-327)

### International

- EU General Data Protection Regulation, Regulation 2016/679
- EU Cyber Resilience Act, Regulation 2024/2847
- UK Product Security and Telecommunications Infrastructure Act 2022

### Academic and Policy

- Emami-Naeini, P. et al., "An IoT Privacy and Security Label" (Carnegie Mellon, 2020)
- FTC, "IoT: Privacy and Security in a Connected World" (2015)
- GAO, "Internet of Things: Enhanced Assessments and Guidance Are Needed" (GAO-20-633, 2020)
- NIST, "Considerations for Managing IoT Cybersecurity and Privacy Risks" (SP 800-183)

## Related Topics

- [Privacy: Legislation](../11-legislation.md) - Broader privacy legislation framework
- [Consumer Data Rights: Legislation](../consumer-data-rights/11-legislation.md)
- [Data Brokers: Legislation](../data-brokers/11-legislation.md)
- [Children's Privacy: Legislation](../childrens-privacy/11-legislation.md)

## Document Navigation

- Previous: [Actions](10-actions.md)
- Next: [Perspectives](12-perspectives.md)
