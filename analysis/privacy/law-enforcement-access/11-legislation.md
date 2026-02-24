# Law Enforcement Access to Data: Legislation and Legal Framework

## Overview

Legislation addressing law enforcement access to data must close three fundamental gaps: the obsolescence of ECPA, the data purchase loophole that allows agencies to buy what they cannot constitutionally seize, and the absence of any regulatory framework for surveillance technology. The legislative approach operates within current constitutional doctrine -- particularly the Fourth Amendment framework refined by *Carpenter v. United States* (2018) -- while pushing for the broadest feasible protections. The proposals below include federal legislation, state model legislation, regulatory frameworks, and a comprehensive loopholes analysis.

## Federal Legislation

### ECPA Modernization Act

**Purpose**: Update the Electronic Communications Privacy Act of 1986 to require warrants for all stored communications content and sensitive metadata, eliminating outdated distinctions that are technologically meaningless.

**Draft Text**:

```text
SEC. 1. SHORT TITLE.

This Act may be cited as the "Electronic Communications Privacy
Act Modernization Act".

SEC. 2. WARRANT REQUIREMENT FOR STORED COMMUNICATIONS CONTENT.

(a) IN GENERAL.—Section 2703 of title 18, United States Code, is
amended—
    (1) inthe heading to read "Required disclosure of stored
    communications content and records";
    (2) in subsection (a) to read as follows:

"(a) CONTENT OF COMMUNICATIONS.—A governmental entity may
require the disclosure by a provider of electronic communication
service or remote computing service of the content of a wire or
electronic communication that is in electronic storage or held
or maintained on behalf of a subscriber or customer only
pursuant to a warrant issued using the procedures described in
the Federal Rules of Criminal Procedure (or, in the case of a
State court, issued using State warrant procedures) by a court
of competent jurisdiction.";

    (3) by striking subsection (b) and inserting the following:

"(b) RECORDS AND OTHER INFORMATION.—
    (1) SENSITIVE RECORDS.—A governmental entity may require
    the disclosure of records or other information pertaining to
    a subscriber or customer of an electronic communication
    service or remote computing service, not including the
    content of communications, that reveal—
        (A) location information (including cell-site location
        information, GPS data, and Wi-Fi connection records);
        (B) web browsing history or search query logs;
        (C) IP address assignment or connection logs that
        reveal patterns of internet activity; or
        (D) records of application usage that reveal private
        conduct—
    only pursuant to a warrant issued using the procedures
    described in the Federal Rules of Criminal Procedure (or,
    in the case of a State court, issued using State warrant
    procedures) by a court of competent jurisdiction.

    (2) OTHER SUBSCRIBER RECORDS.—A governmental entity may
    require the disclosure of subscriber information, including
    name, address, telephone number, and means of payment, only
    pursuant to a court order issued under subsection (d).";

    (4) by amending subsection (d) to read as follows:

"(d) COURT ORDER FOR NON-CONTENT SUBSCRIBER RECORDS.—A
court order for disclosure under subsection (b)(2) shall issue
only if the governmental entity offers specific and articulable
facts showing that there are reasonable grounds to believe that
the records or other information sought are relevant and
material to an ongoing criminal investigation.".

SEC. 3. NOTIFICATION REQUIREMENT.

(a) IN GENERAL.—Section 2703 of title 18, United States Code,
is amended by adding the following subsection:

"(g) NOTIFICATION.—
    (1) REQUIREMENT.—A governmental entity that obtains
    communications content or records under this section shall
    notify the subscriber or customer whose information was
    obtained within 90 days of the date of disclosure.
    (2) DELAYED NOTIFICATION.—A court may authorize delayed
    notification for an additional period not to exceed 180 days
    upon a showing that notification would—
        (A) endanger the life or physical safety of an
        individual;
        (B) result in flight from prosecution;
        (C) result in destruction of or tampering with evidence;
        or
        (D) seriously jeopardize an investigation.
    (3) MAXIMUM DELAY.—Total delayed notification shall not
    exceed 360 days from the date of disclosure."

SEC. 4. TRANSPARENCY REPORTING.

(a) The Attorney General shall publish, not later than 180 days
after the close of each calendar year, a report setting forth—
    (1) the total number of warrants, court orders, and subpoenas
    issued under this chapter, by type;
    (2) the number of such requests by the federal agency making
    the request;
    (3) the categories of data obtained;
    (4) the number of notifications provided and delayed under
    section 2703(g); and
    (5) the number of requests denied by courts.

SEC. 5. EMERGENCY EXCEPTION PRESERVATION.

Nothing in this Act shall be construed to limit the authority of
a governmental entity to access stored communications content
or records without a warrant in circumstances involving—
    (1) an emergency involving danger of death or serious
    physical injury to any person that requires access to
    electronic communications without delay;
provided that, any emergency access shall be reported to a
court of competent jurisdiction within 48 hours and shall be
subject to post-hoc judicial review.

SEC. 6. EFFECTIVE DATE.

This Act shall take effect 180 days after the date of enactment.
```

**Explanation**:

- **Section 2**: Eliminates the 180-day distinction for communications content; requires warrants for all content. Creates a "sensitive records" category requiring warrants for location data, browsing history, and similar revealing metadata. Retains a lower standard for basic subscriber information.
- **Section 3**: Requires notification to individuals whose data is accessed, with judicial exceptions for legitimate investigative needs.
- **Section 4**: Creates public transparency about the volume and nature of law enforcement data requests.
- **Section 5**: Preserves emergency access for imminent threats with mandatory post-hoc judicial review.

**Potential Challenges**:

| Challenge | Response |
|-----------|----------|
| Law enforcement claims of investigative impairment | Emergency exceptions preserved; electronic warrant processes are efficient; CalECPA states have not reported investigative harm |
| Defining "sensitive records" | Statutory definition with regulatory guidance; technology-neutral language focuses on sensitivity of information revealed |
| Retroactive application concerns | Prospective application only; does not invalidate prior lawful access |
| Senate inaction | The Email Privacy Act passed the House unanimously multiple times; bipartisan support exists |

**Refinements**:

- Add provision requiring courts to appoint technical advisors for complex digital warrant applications
- Include data retention limits for information obtained through legal process
- Create a certification process for electronic warrant systems to ensure rapid processing

---

### Fourth Amendment Is Not For Sale Act

**Purpose**: Close the data purchase loophole by requiring a warrant for government acquisition of personal data from data brokers and commercial sources.

**Draft Text**:

```text
SEC. 1. SHORT TITLE.

This Act may be cited as the "Fourth Amendment Is Not For Sale
Act".

SEC. 2. PROHIBITION ON WARRANTLESS DATA PURCHASES.

(a) IN GENERAL.—Chapter 206 of title 18, United States Code, is
amended by adding the following section:

"SEC. 3122A. WARRANT REQUIREMENT FOR COMMERCIAL DATA ACQUISITION.

"(a) PROHIBITION.—A Federal, State, or local governmental entity
may not purchase, obtain, or otherwise acquire covered personal
data from a data broker without—
    (1) a warrant issued using the procedures described in the
    Federal Rules of Criminal Procedure (or, in the case of a
    State court, issued using State warrant procedures) by a
    court of competent jurisdiction based upon probable cause to
    believe that the specific data sought constitutes evidence of
    a crime; or
    (2) the informed, voluntary consent of the individual whose
    data is sought.

"(b) DEFINITIONS.—
    (1) COVERED PERSONAL DATA.—The term 'covered personal data'
    means information that identifies or is linked or reasonably
    linkable to an individual, including—
        (A) location data (including cell phone location, GPS,
        Wi-Fi, and Bluetooth data);
        (B) internet browsing history, search history, and app
        usage data;
        (C) records of purchases and financial transactions;
        (D) utility records;
        (E) communications metadata;
        (F) biometric data;
        (G) social media data beyond what is publicly visible
        to all users without an account; and
        (H) any data derived from or inferred from the above.
    (2) DATA BROKER.—The term 'data broker' means an entity
    that collects, aggregates, sells, licenses, or otherwise
    provides personal data of individuals with whom the entity
    does not have a direct relationship.
    (3) EXCLUSIONS.—The term 'covered personal data' does not
    include—
        (A) records that are publicly available as a matter of
        law (court filings, property records, business
        registrations); or
        (B) news reporting and journalistic content.

"(c) PROHIBITION ON BULK ACQUISITION.—No governmental entity may
purchase covered personal data in bulk or in aggregate form that
includes data on individuals not specifically identified in a
warrant.

"(d) PROHIBITION ON REVERSE ENGINEERING.—No governmental entity
may use data purchased from a data broker to establish probable
cause for a warrant seeking the same or related data from the
original source.

"(e) SUPPRESSION.—Covered personal data obtained in violation
of this section, and any evidence derived therefrom, shall not
be admissible as evidence in any trial, hearing, or other
proceeding in or before any court, grand jury, department,
officer, agency, or other authority of the United States, a
State, or a political subdivision thereof.

"(f) CIVIL LIABILITY.—Any individual whose covered personal data
is obtained in violation of this section may bring a civil action
against the governmental entity and recover—
    (1) actual damages, but not less than $10,000;
    (2) punitive damages;
    (3) reasonable attorney's fees; and
    (4) such other relief as the court may deem appropriate.

"(g) REPORTING.—Each Federal agency that purchases covered
personal data shall report annually to Congress on—
    (1) the number of warrants obtained under this section;
    (2) the types of data purchased;
    (3) the total expenditure on data purchases; and
    (4) the data brokers from which data was purchased."
```

**Explanation**:

- Directly addresses the constitutional end-run identified in *Carpenter*: agencies buy what they cannot constitutionally seize
- Covers all categories of personal data that data brokers sell to government
- Prohibition on bulk purchases prevents mass surveillance through data purchases
- Reverse engineering prohibition prevents agencies from using purchased data to bootstrap probable cause
- Suppression remedy creates teeth by excluding improperly obtained evidence
- Civil liability provides individual enforcement mechanism

**Potential Challenges**:

| Challenge | Response |
|-----------|----------|
| Intelligence community carve-out demands | Separate treatment for FISA-governed activities; domestic law enforcement restrictions remain absolute |
| Defining "data broker" | Statutory definition targets entities that sell data on individuals with whom they have no direct relationship |
| Publicly available data exception | Narrowly limited to data available as a matter of law (court records, property records), not commercially "available" data |
| Enforcement against past purchases | Prospective application; agencies must audit and disclose current contracts |

---

### Law Enforcement Surveillance Technology Standards Act

**Purpose**: Establish federal standards for law enforcement use of surveillance technology, including facial recognition, predictive policing, ALPRs, and cell-site simulators.

**Draft Text**:

```text
SEC. 1. SHORT TITLE.

This Act may be cited as the "Law Enforcement Surveillance
Technology Standards Act".

SEC. 2. FACIAL RECOGNITION MORATORIUM.

(a) MORATORIUM.—No Federal, State, or local law enforcement
agency may use real-time facial recognition technology for
identification or surveillance purposes until—
    (1) the National Institute of Standards and Technology has
    established accuracy and bias standards for law enforcement
    facial recognition systems;
    (2) the system in question has been independently tested and
    certified as meeting those standards; and
    (3) the agency has adopted written policies governing use,
    including prohibitions on use based solely on race,
    ethnicity, religion, national origin, or political activity.

(b) WARRANT REQUIREMENT.—After the moratorium conditions are
met, no law enforcement agency may conduct a facial recognition
search without a warrant based on probable cause, except in
exigent circumstances involving imminent danger to life.

SEC. 3. CELL-SITE SIMULATOR WARRANT REQUIREMENT.

(a) WARRANT.—A law enforcement agency may not use a cell-site
simulator device without a warrant based on probable cause,
issued by a court of competent jurisdiction, that—
    (1) identifies the specific individual or device targeted;
    (2) limits the geographic area and duration of use; and
    (3) requires minimization of data collected from non-target
    devices.

(b) NON-DISCLOSURE AGREEMENTS.—No provision of any contract or
agreement between a law enforcement agency and a cell-site
simulator manufacturer may restrict the agency from disclosing
the use of such technology to a court, prosecutor, defense
attorney, or defendant.

SEC. 4. AUTOMATED LICENSE PLATE READER RESTRICTIONS.

(a) RETENTION.—Data collected by automated license plate readers
operated by or on behalf of a law enforcement agency on vehicles
not connected to an active criminal investigation shall be
deleted within 48 hours of collection.

(b) SHARING.—ALPR data may not be shared in bulk with other
agencies, private entities, or federal databases without a
court order.

(c) PURPOSE LIMITATION.—ALPR data may be used only for active
criminal investigations, not for immigration enforcement or
general surveillance.

SEC. 5. PREDICTIVE POLICING TRANSPARENCY AND ACCOUNTABILITY.

(a) DISCLOSURE.—Any law enforcement agency using a predictive
policing algorithm shall publicly disclose—
    (1) the algorithm's inputs and data sources;
    (2) the results of independent bias audits conducted
    annually; and
    (3) the outcomes and accuracy of the algorithm's
    predictions.

(b) BIAS PROHIBITION.—No predictive policing algorithm may be
deployed if independent testing demonstrates that it produces
racially or ethnically disparate results that cannot be
justified by legitimate, non-discriminatory factors.

SEC. 6. COMMUNITY OVERSIGHT.

(a) CONDITION OF FEDERAL FUNDING.—As a condition of receiving
any federal law enforcement grant, a law enforcement agency
shall—
    (1) publicly disclose all surveillance technologies in its
    possession, including capabilities, costs, and data
    retention policies;
    (2) obtain approval from the governing legislative body
    (city council, county commission) before acquiring new
    surveillance technology; and
    (3) publish an annual surveillance technology report
    describing how each technology was used and its outcomes.

SEC. 7. PARALLEL CONSTRUCTION PROHIBITION.

(a) PROHIBITION.—It shall be unlawful for any law enforcement
officer or agent to conceal from a court, prosecutor, defense
attorney, or defendant the method by which evidence, leads, or
investigative information was originally obtained.

(b) DISCLOSURE.—In any criminal proceeding, the prosecution
shall disclose all surveillance methods, data sources, and
investigative techniques used to develop evidence, including
those that provided initial leads or tips.

(c) SUPPRESSION.—Evidence obtained through a process in which
the original surveillance method has been concealed shall be
subject to suppression.

(d) WHISTLEBLOWER PROTECTION.—Any law enforcement officer who
reports parallel construction practices shall be protected
from retaliation under the Whistleblower Protection Act.

SEC. 8. ENFORCEMENT AND PENALTIES.

(a) AGENCIES.—Violation of this Act by a law enforcement agency
shall result in suspension of federal law enforcement grant
funding until compliance is demonstrated.

(b) INDIVIDUALS.—Any individual whose rights under this Act
are violated may bring a civil action and recover actual
damages or statutory damages of $25,000 per violation, plus
reasonable attorney's fees.

(c) CRIMINAL PENALTY FOR PARALLEL CONSTRUCTION.—Any law
enforcement officer or agent who knowingly conceals surveillance
methods in violation of Section 7 shall be subject to a fine
of not more than $50,000, imprisonment of not more than
2 years, or both.

SEC. 9. EFFECTIVE DATE.

This Act shall take effect one year after the date of enactment.
```

**Explanation**:

- Addresses all major categories of surveillance technology in a single comprehensive framework
- Facial recognition moratorium halts deployment until accuracy and bias problems are resolved, rather than banning the technology permanently
- Cell-site simulator warrant requirement codifies what some agencies already do voluntarily, with the critical addition of NDA override
- ALPR restrictions address the mass surveillance problem of indefinite retention of every vehicle's movements
- Predictive policing transparency allows evaluation of whether these tools work and whether they discriminate
- Parallel construction prohibition addresses a practice that fundamentally undermines due process
- Federal funding condition creates enforcement mechanism without requiring separate enforcement infrastructure

**Potential Challenges**:

| Challenge | Response |
|-----------|----------|
| Law enforcement opposition to moratorium | Moratorium is temporary, conditioned on meeting accuracy standards -- it accelerates responsible deployment |
| Local government resistance to federal mandates | Tied to federal funding, not direct mandates; local governments can decline federal funds |
| Technology vendor lobbying | Transparency requirements benefit responsible vendors; NDA restrictions apply to government contracts, not commercial sales |
| Defining "predictive policing" | Broad statutory definition with regulatory guidance for edge cases |

---

## State Model Legislation

### Model Electronic Privacy Act

**Purpose**: State-level comprehensive electronic privacy protection, modeled on CalECPA, for states without such legislation.

**Draft Text**:

```text
SECTION 1. SHORT TITLE.

This Act may be cited as the "[State] Electronic Communications
Privacy Act".

SECTION 2. WARRANT REQUIRED FOR ELECTRONIC INFORMATION.

(a) A government entity shall not compel the production of or
access to electronic communication information from a service
provider, or compel a service provider to disclose electronic
communication information about a subscriber or customer,
without a warrant issued by a court of competent jurisdiction
based on probable cause.

(b) A government entity shall not access electronic device
information by means of physical interaction or electronic
communication with the device without a warrant.

(c) A government entity shall not obtain the location
information of an electronic device without a warrant.

SECTION 3. NOTIFICATION.

(a) A government entity that obtains electronic communication
information pursuant to this Act shall notify the target of
the warrant within 90 days of obtaining the information.

(b) A court may authorize delayed notification for up to
180 days upon a showing of exigent circumstances.

SECTION 4. EXCLUSIONARY RULE.

Electronic communication information obtained in violation
of this Act shall not be admissible as evidence in any criminal,
civil, or administrative proceeding.

SECTION 5. CIVIL ACTION.

Any person whose electronic communication information is
obtained in violation of this Act may bring a civil action
for actual damages, statutory damages of $5,000 per violation,
and reasonable attorney's fees.
```

### Model Surveillance Technology Oversight Act

**Purpose**: State-level community control over police surveillance technology.

**Draft Text**:

```text
SECTION 1. SHORT TITLE.

This Act may be cited as the "[State] Community Surveillance
Oversight Act".

SECTION 2. DISCLOSURE AND APPROVAL.

(a) Before acquiring any surveillance technology, a law
enforcement agency shall—
    (1) publish a surveillance impact report describing the
    technology's capabilities, costs, and potential civil
    liberties implications;
    (2) hold a public hearing with opportunity for community
    comment; and
    (3) obtain approval from the governing legislative body.

SECTION 3. ANNUAL REPORTING.

Each law enforcement agency shall publish an annual report
describing all surveillance technologies in use, how each was
used, the cost of operation, and any complaints or violations.

SECTION 4. DATA RETENTION.

(a) Data collected by surveillance technologies on individuals
not connected to an active criminal investigation shall be
deleted within 30 days of collection.

(b) Data retention beyond 30 days requires a court order.

SECTION 5. FACIAL RECOGNITION.

No law enforcement agency in this state shall use facial
recognition technology for real-time identification or
surveillance until accuracy and bias standards established
by [state agency] have been met and independently certified.

SECTION 6. ENFORCEMENT.

A violation of this Act shall result in suppression of any
evidence obtained and civil liability under [state civil
rights statute].
```

---

## Regulatory Framework

### DOJ Rulemaking on Data Access Practices

**Existing Authority**: The Attorney General has authority to establish guidelines and policies governing DOJ components and federal law enforcement agencies.

**Proposed Regulations**:

- Require all DOJ agencies to obtain warrants for any data that would require a warrant to collect directly, including commercial data purchases
- Establish data retention limits for information obtained through legal process (3-year maximum unless connected to active case)
- Mandate annual transparency reports from all federal law enforcement agencies on data access practices
- Prohibit non-disclosure agreements that restrict disclosure of surveillance methods to courts
- Require racial impact assessments before deploying surveillance technologies

### NIST Standards for Surveillance Technology

**Existing Authority**: NIST has authority to develop standards for technology used by federal agencies.

**Proposed Standards**:

- Accuracy and bias testing standards for facial recognition systems
- Performance standards for predictive policing algorithms, including disparate impact thresholds
- Data minimization standards for ALPR systems
- Audit standards for cell-site simulators and other electronic surveillance devices

### Federal Grant Conditions

**Existing Authority**: DOJ and DHS condition federal grants on compliance with various requirements.

**Proposed Conditions**:

- Federal law enforcement grants (COPS, Byrne/JAG, UASI) conditioned on:
    - Public disclosure of all surveillance technologies
    - Community oversight process for new technology acquisition
    - Compliance with ALPR data retention limits
    - Annual bias audits for algorithmic tools
    - Completion of surveillance technology impact assessments

---

## Legal Considerations

### Constitutional Issues

- **Fourth Amendment**: *Carpenter v. United States* (2018) established that the Fourth Amendment protects data revealing "the privacies of life," even when shared with third parties. The proposed legislation extends this principle to categories of data *Carpenter* left unaddressed (browsing history, IP logs, commercial data purchases). The constitutional basis is strong but the Supreme Court has not yet endorsed this extension.
- **First Amendment**: Restrictions on predictive policing and social media monitoring must be carefully drafted to avoid regulating protected speech. The proposals target governmental surveillance conduct, not private expression.
- **Commerce Clause**: Federal legislation regulating data brokers and technology vendors rests on Congress's power to regulate interstate commerce. Data flows across state lines; the interstate nexus is clear.
- **Tenth Amendment**: Federal standards for state and local law enforcement are tied to federal funding conditions, not direct mandates, following the *South Dakota v. Dole* (1987) framework for conditional spending.

### Preemption Questions

- The proposed federal legislation establishes a floor, not a ceiling: states may provide stronger protections
- CalECPA and other state electronic privacy laws would remain in effect
- CCOPS ordinances at the local level would be preserved and encouraged
- Industry may push for ceiling preemption; this should be resisted

### Enforcement Mechanisms

- Multi-layered enforcement (DOJ, state AGs, private right of action) is essential given the history of inadequate government enforcement of surveillance restrictions
- Suppression of evidence provides direct consequence for violations in criminal proceedings
- Civil liability enables individuals and communities to enforce their rights
- Federal funding conditions create institutional incentives for compliance

---

## Loopholes, Shortcomings, and Rectification

### ECPA Modernization Act

#### Potential Loopholes

| Loophole | Description | Severity |
|----------|-------------|----------|
| Emergency exception abuse | Agencies may claim emergency access broadly and then fail to obtain post-hoc judicial review | High |
| "Sensitive records" definition gaps | New data categories not enumerated in the statute (e.g., smart home data, vehicle telematics) may fall outside warrant protection | Medium |
| Foreign-stored data | Agencies may seek data from foreign providers or through international agreements to circumvent domestic warrant requirements | Medium |
| Voluntary disclosure | ECPA permits service providers to voluntarily disclose data to law enforcement; this channel remains open | High |
| Administrative subpoena survival | Agencies may use administrative subpoenas under other statutes (tax code, financial statutes) to access data not covered by ECPA reform | Medium |

#### Shortcomings

| Issue | Impact | Root Cause |
|-------|--------|------------|
| Does not address data already collected | Agencies retain vast databases of previously collected data | Legislation applies prospectively |
| Notification delays | 360-day maximum delay still allows significant period without individual knowledge | Compromise to secure law enforcement support |
| No private right of action for ECPA violations specifically | Enforcement depends on exclusionary rule and government action | Political opposition to expanding litigation rights |

#### Rectification Procedures

1. Require judicial approval within 48 hours for any emergency access, with automatic suppression if not obtained
2. Define "sensitive records" using a technology-neutral standard (any records that reveal patterns of private conduct) rather than enumerated list alone
3. Apply ECPA reform to data obtained through international agreements and the CLOUD Act
4. Amend ECPA to restrict voluntary disclosure by requiring providers to verify legal authority before disclosing
5. Harmonize administrative subpoena statutes with ECPA warrant standards for overlapping data categories

### Fourth Amendment Is Not For Sale Act

#### Potential Loopholes

| Loophole | Description | Severity |
|----------|-------------|----------|
| Definition of "data broker" | Companies may restructure to claim direct relationships with data subjects, avoiding the "data broker" definition | High |
| Intelligence community carve-out | If intelligence agencies are exempted, information sharing between intelligence and law enforcement creates a back door | Very High |
| Open-source intelligence (OSINT) exception | Agencies may argue that data gathered from "open sources" is not a "purchase" | Medium |
| State and local workarounds | State/local agencies may fund data purchases through non-government intermediaries | Medium |
| Consent manipulation | Data brokers may obtain blanket "consent" from consumers through buried terms of service | High |

#### Shortcomings

| Issue | Impact | Root Cause |
|-------|--------|------------|
| Does not address existing data troves | Agencies retain databases built from prior purchases | Prospective application |
| Relies on suppression remedy | Suppression only matters in criminal proceedings; surveillance used for intelligence, immigration enforcement, or non-prosecutorial purposes is not affected | Structural limitation of exclusionary rule |
| Data broker registration not included | Without a data broker registry, identifying covered entities is difficult | Scope limitation of the bill |

#### Rectification Procedures

1. Define "data broker" broadly and include anti-evasion provisions targeting restructuring to avoid coverage
2. Require intelligence agencies to obtain warrants for any data shared with domestic law enforcement
3. Define "purchase" to include any acquisition of value, including barter, data exchange, and indirect procurement
4. Apply to data acquired through intermediaries or contractors acting on behalf of governmental entities
5. Require meaningful, specific consent -- not blanket terms-of-service acceptance -- for the consent exception

### Law Enforcement Surveillance Technology Standards Act

#### Potential Loopholes

| Loophole | Description | Severity |
|----------|-------------|----------|
| NIST standards delay | NIST may take years to develop standards, effectively extending the moratorium indefinitely or allowing agencies to argue compliance is impossible | Medium |
| Self-funded technology | Agencies that do not receive federal grants may argue they are not subject to federal conditions | High |
| Technology redefinition | Vendors may redesign products to fall outside statutory definitions (e.g., "facial analysis" instead of "facial recognition") | Medium |
| Predictive policing rebranding | Agencies may rebrand predictive tools as "intelligence-led policing" or "crime analysis" to avoid disclosure requirements | Medium |
| Parallel construction survival | Despite prohibition, detecting parallel construction is inherently difficult because the practice is designed to be undetectable | High |

#### Shortcomings

| Issue | Impact | Root Cause |
|-------|--------|------------|
| Federal funding condition may not reach all agencies | Agencies that decline federal funds are not covered | Constitutional limits on federal power over state/local governments |
| Community oversight burden | Small jurisdictions may lack resources for oversight boards | Structural resource constraints |
| Criminal penalty for parallel construction may be under-enforced | DOJ may be reluctant to prosecute its own officers | Institutional self-interest |

#### Rectification Procedures

1. Set statutory deadlines for NIST standards development (18 months); extend moratorium only if standards are not complete due to demonstrated technical necessity
2. Use conditional spending broadly -- virtually all law enforcement agencies receive some federal funding
3. Define surveillance technologies using functional descriptions rather than product names
4. Require agencies to disclose all algorithmic or data-driven decision-support tools, regardless of labeling
5. Create an independent Inspector General for surveillance practices, separate from DOJ IG, to enforce parallel construction prohibition

### General Implementation Concerns

#### Systemic Issues

| Issue | Proposed Solution |
|-------|------------------|
| Enforcement funding inadequacy | Tie enforcement funding to penalty revenue; create a dedicated digital rights enforcement fund |
| Technology evolution outpacing law | Require biennial review and update of regulatory definitions and standards |
| Coordination failures | Establish a multi-agency working group (DOJ, FTC, NIST, civil society representatives) to coordinate surveillance reform implementation |
| Resistance from entrenched agencies | Presidential directive and congressional oversight pressure; tie senior officials' performance reviews to compliance |

#### Sunset and Review Provisions

- Require GAO report on implementation effectiveness within 3 years of enactment
- Mandate annual DOJ reports on compliance with warrant requirements and surveillance technology standards
- Include 5-year review provision for congressional reassessment of statutory definitions, technology coverage, and effectiveness of community oversight requirements
- Require NIST to update surveillance technology standards every 3 years

---

## References

- Electronic Communications Privacy Act, 18 U.S.C. 2510-2522, 2701-2712 (1986)
- Wiretap Act (Title III), 18 U.S.C. 2510-2522 (1968)
- Pen Register Act, 18 U.S.C. 3121-3127 (1978)
- USA PATRIOT Act, Pub. L. 107-56 (2001)
- CLOUD Act, Pub. L. 115-141, Division V (2018)
- CalECPA, Cal. Penal Code 1546-1546.4 (2015)
- Illinois Biometric Information Privacy Act, 740 ILCS 14 (2008)
- *Katz v. United States*, 389 U.S. 347 (1967)
- *United States v. Miller*, 425 U.S. 435 (1976)
- *Smith v. Maryland*, 442 U.S. 735 (1979)
- *Riley v. California*, 573 U.S. 373 (2014)
- *Carpenter v. United States*, 585 U.S. 296 (2018)
- *United States v. Chatrie*, No. 3:19-cr-130 (E.D. Va. 2022)
- *South Dakota v. Dole*, 483 U.S. 203 (1987)
- *Brady v. Maryland*, 373 U.S. 83 (1963)
- Georgetown Law Center on Privacy and Technology, "American Dragnet" (2022)
- NIST, "Face Recognition Vendor Test" (2019, updated 2023)
- GAO, "Facial Recognition Technology: Current and Planned Uses by Federal Agencies" (2023)
- Fourth Amendment Is Not For Sale Act, S. 1265, 118th Congress
- ACLU, "Community Control Over Police Surveillance Model Bill" (2023)

## Related Topics

- [Government Surveillance: Legislation](../government-surveillance/11-legislation.md) - Intelligence surveillance authorities
- [Data Brokers: Legislation](../data-brokers/11-legislation.md) - Data broker regulation
- [Biometric Privacy: Legislation](../biometric-privacy/11-legislation.md) - Facial recognition and biometric laws
- [Communications Privacy: Legislation](../communications-privacy/11-legislation.md) - Wiretap and communications law
- [Privacy: Legislation](../11-legislation.md) - Parent topic legislation

## Document Navigation

- Previous: [Actions](10-actions.md)
- Next: [Perspectives](12-perspectives.md)
- Up: [Overview](01-overview.md)
