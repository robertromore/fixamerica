# Health Privacy: Legislation and Legal Framework

## Overview

Health privacy legislation must address two fundamental gaps: the inadequacy of HIPAA's entity-based framework for the digital health era, and the absence of protections for specific high-risk categories of health data (reproductive, genetic, mental health). This document proposes federal legislation, state model legislation, and regulatory frameworks to create comprehensive health data protection. The legislative approach operates within current constitutional doctrine while pushing for maximum protection.

## Federal Legislation

### Comprehensive Health Data Protection Act

**Purpose**: Extend privacy protections to all health-related data regardless of who collects it, closing the gap between HIPAA-covered and non-covered health data.

**Draft Text**:

```text
SEC. 1. SHORT TITLE.

This Act may be cited as the "Comprehensive Health Data Protection Act".

SEC. 2. DEFINITIONS.

(a) HEALTH DATA.—The term "health data" means any information
that identifies or is reasonably linkable to an individual and
relates to—
    (1) the past, present, or future physical or mental health
    condition of the individual;
    (2) the provision of health care to the individual;
    (3) biometric data collected for health-related purposes;
    (4) genetic data;
    (5) reproductive or sexual health data;
    (6) precise geolocation data that could reveal visits to
    health care facilities;
    (7) data collected through a health-related application,
    device, or website; or
    (8) any data used to infer or derive information described
    in paragraphs (1) through (7).

(b) REGULATED ENTITY.—The term "regulated entity" means any
person or entity that collects, processes, sells, or shares
health data, excluding—
    (1) a natural person acting in a personal capacity;
    (2) a governmental entity acting within its statutory
    authority; and
    (3) entities covered by HIPAA to the extent they comply
    with HIPAA requirements for protected health information.

SEC. 3. CONSENT REQUIREMENTS.

(a) IN GENERAL.—A regulated entity may not collect, use, or
share health data unless the individual has provided affirmative,
informed consent that is—
    (1) specific to the category of data and purpose of use;
    (2) freely given and not bundled with consent for unrelated
    purposes;
    (3) revocable at any time; and
    (4) documented by the regulated entity.

(b) EXCEPTIONS.—Consent is not required for—
    (1) providing a service or product specifically requested
    by the individual, limited to the data necessary for that
    service or product;
    (2) complying with a legal obligation;
    (3) protecting the life or physical safety of an individual;
    (4) conducting public health activities authorized by law; or
    (5) conducting research approved by an institutional review
    board, using de-identified data.

SEC. 4. DATA MINIMIZATION.

A regulated entity shall collect only the health data reasonably
necessary for the purpose disclosed to the individual and shall
delete such data when no longer necessary for that purpose or
within three years, whichever is earlier, unless the individual
provides renewed consent.

SEC. 5. INDIVIDUAL RIGHTS.

(a) ACCESS.—An individual has the right to access all health
data held about them by a regulated entity within 30 days of
request.

(b) CORRECTION.—An individual has the right to request
correction of inaccurate health data.

(c) DELETION.—An individual has the right to request deletion
of their health data, subject to limited exceptions for legal
obligations and ongoing treatment.

(d) PORTABILITY.—An individual has the right to receive their
health data in a structured, commonly used, machine-readable
format.

SEC. 6. PROHIBITION ON SALE OF HEALTH DATA.

(a) IN GENERAL.—A regulated entity may not sell health data
unless the individual has provided specific, separate consent
for the sale.

(b) PROHIBITION ON SENSITIVE CATEGORIES.—No person may sell
health data relating to mental health, substance use disorders,
reproductive health, HIV/AIDS status, or genetic information
without the explicit, written consent of the individual.

SEC. 7. TRACKING TECHNOLOGY RESTRICTIONS.

(a) IN GENERAL.—A regulated entity that operates a health-
related website, application, or online service may not deploy
tracking technologies that transmit individually identifiable
health data to third parties for advertising purposes.

(b) TRANSPARENCY.—A regulated entity must disclose all third-
party tracking technologies used on health-related websites
and applications.

SEC. 8. ENFORCEMENT.

(a) FTC ENFORCEMENT.—The Federal Trade Commission shall
enforce this Act as if a violation were an unfair or deceptive
act or practice under Section 5 of the FTC Act.

(b) STATE ATTORNEY GENERAL ENFORCEMENT.—State attorneys
general may bring civil actions to enforce this Act.

(c) PRIVATE RIGHT OF ACTION.—Any individual whose health
data rights under this Act are violated may bring a civil
action and recover—
    (1) actual damages or statutory damages of not less than
    $1,000 and not more than $10,000 per violation;
    (2) reasonable attorney's fees; and
    (3) injunctive relief.

(d) PENALTIES.—Civil penalties for violations shall not exceed
the greater of—
    (1) $50,000 per violation; or
    (2) 4 percent of the regulated entity's annual gross
    revenue in the preceding fiscal year.

SEC. 9. PREEMPTION.

This Act establishes a federal floor and does not preempt any
State law that provides greater protection for health data.

SEC. 10. EFFECTIVE DATE.

(a) This Act shall take effect 12 months after the date of
enactment for regulated entities with annual revenue exceeding
$25,000,000.

(b) This Act shall take effect 24 months after the date of
enactment for all other regulated entities.
```

**Explanation**:

- **Section 2**: Defines "health data" broadly to cover data types that currently fall outside HIPAA, including health inferences, app data, and location data near health facilities
- **Section 3**: Requires affirmative consent, not the notice-and-opt-out model that has failed
- **Section 4**: Data minimization prevents overcollection and indefinite retention
- **Section 5**: Individual rights modeled on GDPR but adapted for U.S. legal context
- **Section 6**: Restricts data sales, with heightened protections for sensitive categories
- **Section 7**: Directly addresses the tracking pixel problem identified by The Markup
- **Section 8**: Multi-layered enforcement with private right of action as the key innovation
- **Section 9**: Floor-not-ceiling preemption preserves stronger state protections

**Potential Challenges**:

| Challenge | Response |
|-----------|----------|
| First Amendment claims | Health data regulation does not regulate speech; it regulates commercial conduct |
| Commerce Clause scope | Congress has broad authority over interstate commercial data practices |
| Industry compliance costs | Graduated effective dates and revenue thresholds address burden |
| Research access concerns | IRB-approved research exception preserves legitimate research |

**Refinements**:

- Add safe harbor for regulated entities that conduct and remediate annual privacy audits
- Include specific provisions for AI-derived health inferences
- Create an advisory committee of patients, providers, technologists, and privacy experts

---

### Reproductive Health Data Protection Act

**Purpose**: Provide federal protection for reproductive health data from being used to enforce state criminal restrictions on reproductive care.

**Draft Text**:

```text
SEC. 1. SHORT TITLE.

This Act may be cited as the "Reproductive Health Data
Protection Act".

SEC. 2. PROHIBITION ON COMPELLED DISCLOSURE.

(a) IN GENERAL.—No person or entity may be compelled by any
federal, state, or local government entity to disclose health
data for the purpose of—
    (1) investigating whether an individual has obtained or
    provided reproductive health care;
    (2) imposing criminal, civil, or administrative liability
    related to the provision or receipt of reproductive health
    care that is lawful in the state where it was provided; or
    (3) identifying individuals who have sought, obtained, or
    provided reproductive health care.

(b) SCOPE.—This prohibition applies to—
    (1) medical records and health data held by providers,
    insurers, and pharmacies;
    (2) data collected by health applications, including period
    trackers, fertility apps, and telehealth platforms;
    (3) location data, search history, and communications data
    that could reveal reproductive health care activity;
    (4) payment records for reproductive health services or
    products; and
    (5) any other data that could be used to identify receipt
    of reproductive health care.

SEC. 3. PRIVILEGE.

(a) Communications between a patient and a reproductive health
care provider, and records of such communications, are
privileged and may not be compelled in any federal, state, or
local proceeding.

SEC. 4. DATA RETENTION LIMITS.

(a) Entities collecting reproductive health data shall retain
such data for no longer than necessary to provide the
requested service, and in no event longer than 18 months.

SEC. 5. ENFORCEMENT.

(a) PRIVATE RIGHT OF ACTION.—Any individual whose rights
under this Act are violated may bring a civil action and
recover statutory damages of not less than $10,000 per
violation, plus attorney's fees.

(b) CRIMINAL PENALTIES.—Any person who knowingly discloses
reproductive health data in violation of this Act shall be
subject to a fine of not more than $250,000, imprisonment
of not more than 5 years, or both.
```

**Explanation**:

- Addresses the specific threat created by *Dobbs* by shielding reproductive health data from criminal enforcement
- Covers data beyond HIPAA's scope, including app data, location data, and search history
- Creates a federal privilege that overrides state-law subpoenas
- Criminal penalties reflect the severity of harm from unauthorized disclosure

**Potential Challenges**:

| Challenge | Response |
|-----------|----------|
| Federalism objections | Federal power under Commerce Clause and Supremacy Clause supports preemption of state subpoenas for interstate data |
| Law enforcement opposition | The privilege is targeted to reproductive health, not all health data |
| Definition of "lawful" care | Defined by the law of the state where care was provided |

---

### GINA Expansion Act

**Purpose**: Close gaps in the Genetic Information Nondiscrimination Act by extending protections to life insurance, disability insurance, long-term care insurance, and consumer genetic testing companies.

**Draft Text**:

```text
SEC. 1. SHORT TITLE.

This Act may be cited as the "Genetic Information
Nondiscrimination Act Expansion Act" or "GINA 2.0".

SEC. 2. EXPANDED NON-DISCRIMINATION.

(a) LIFE INSURANCE.—It shall be unlawful for a life insurer
to use genetic information in making decisions regarding
issuance, coverage, or pricing of life insurance.

(b) DISABILITY INSURANCE.—It shall be unlawful for a
disability insurer to use genetic information in making
decisions regarding issuance, coverage, or pricing of
disability insurance.

(c) LONG-TERM CARE INSURANCE.—It shall be unlawful for a
long-term care insurer to use genetic information in making
decisions regarding issuance, coverage, or pricing of
long-term care insurance.

SEC. 3. CONSUMER GENETIC TESTING PROTECTIONS.

(a) CONSENT.—A consumer genetic testing company may not share,
sell, or transfer genetic data without the specific, written
consent of the individual.

(b) DELETION.—An individual has the right to request deletion
of their genetic data, and the company must comply within
30 days.

(c) BANKRUPTCY PROTECTION.—Genetic data may not be transferred
as a business asset in bankruptcy proceedings without the
affirmative consent of each individual whose data would be
transferred.

(d) LAW ENFORCEMENT.—A consumer genetic testing company may
not provide genetic data to law enforcement without a warrant
based on probable cause, issued by a court of competent
jurisdiction, identifying a specific individual.

SEC. 4. ENFORCEMENT.

Violations of this Act shall be enforced under the same
mechanisms as the original GINA, with the addition of a
private right of action permitting recovery of statutory
damages of not less than $2,500 per violation plus
attorney's fees.
```

**Explanation**:

- Closes the well-documented gap in GINA that leaves life insurance, disability insurance, and long-term care insurance unprotected
- Addresses the 23andMe bankruptcy scenario by preventing genetic data from being treated as a transferable business asset
- Requires a warrant for law enforcement access, preventing bulk searches of genetic databases

---

## State Model Legislation

### Model Consumer Health Data Privacy Act

**Purpose**: State-level comprehensive health data protection for states without such legislation, modeled on Washington's My Health My Data Act.

**Draft Text**:

```text
SECTION 1. SHORT TITLE.

This Act may be cited as the "[State] Consumer Health Data
Privacy Act".

SECTION 2. DEFINITIONS.

(a) "Consumer health data" means personal information that is
linked or reasonably linkable to a consumer and identifies the
consumer's past, present, or future physical or mental health
status, including but not limited to:
    (1) individual health conditions, treatment, or diagnosis;
    (2) social, psychological, or behavioral data collected
    for health-related purposes;
    (3) bodily functions, vital signs, or biometric data
    collected for health purposes;
    (4) reproductive or sexual health data;
    (5) gender-affirming care data;
    (6) genetic data;
    (7) precise location data that could indicate visits to
    health care facilities;
    (8) data that identifies a consumer seeking health care
    services; and
    (9) any data that a regulated entity uses to derive or
    infer the above.

SECTION 3. CONSENT.

A regulated entity may not collect or share consumer health
data without the consumer's affirmative consent.

SECTION 4. INDIVIDUAL RIGHTS.

Consumers have the right to:
    (a) access their consumer health data;
    (b) withdraw consent at any time;
    (c) request deletion of their consumer health data.

SECTION 5. PRIVATE RIGHT OF ACTION.

Any consumer whose rights under this Act are violated may
bring a civil action and recover actual damages, statutory
damages of $5,000 per violation, and attorney's fees.

SECTION 6. NO WAIVER.

Any contract provision waiving rights under this Act is void
and unenforceable.
```

**Adaptations**: States should customize definitions to address their specific needs, including coverage of crisis pregnancy centers, gender-affirming care data, and state-specific enforcement mechanisms.

---

## Regulatory Framework

### HHS HIPAA Modernization Rulemaking

**Existing Authority**: HHS has broad rulemaking authority under HIPAA Section 264 and the HITECH Act.

**Proposed Regulations**:

- Strengthen de-identification standards to require expert determination for all de-identification, eliminating the Safe Harbor method
- Expand accounting of disclosures to include treatment, payment, and operations disclosures
- Require covered entities to conduct and publish annual privacy impact assessments
- Mandate encryption of all electronic PHI at rest and in transit
- Prohibit use of tracking technologies on patient-facing websites without specific, separate patient consent

### FTC Health Data Rulemaking

**Existing Authority**: FTC Act Section 5; Health Breach Notification Rule (16 CFR Part 318).

**Proposed Regulations**:

- Define "health data" broadly for purposes of Section 5 enforcement
- Require health app developers to publish standardized privacy nutrition labels
- Establish consent requirements for health data sharing by non-HIPAA entities
- Mandate breach notification for all health data breaches, not just those covered by HIPAA

---

## Legal Considerations

### Constitutional Issues

- **First Amendment**: Health data regulation will face challenges arguing data sales are protected speech. Precedent from *Sorrell v. IMS Health Inc.*, 564 U.S. 552 (2011), which struck down a Vermont law restricting sale of prescriber-identifying data, requires careful drafting to survive heightened scrutiny. Regulations should target commercial conduct, not speech.
- **Commerce Clause**: Federal health data legislation rests on Congress's power to regulate interstate commerce. Health data flows freely across state lines; the interstate nexus is clear.
- **Supremacy Clause**: Federal reproductive health data shields would preempt conflicting state-law subpoenas under the Supremacy Clause, though states may challenge this under Tenth Amendment principles.

### Preemption Questions

- The proposed federal floor approach preserves stronger state laws (California CMIA, Washington My Health My Data Act)
- HIPAA's current preemption framework already follows this model (states may be more protective)
- Industry will push for ceiling preemption; this should be resisted

### Enforcement Mechanisms

- Multi-layered enforcement (FTC, HHS OCR, state AGs, private right of action) is essential
- Private right of action is the single most important enforcement mechanism, as government agencies are consistently resource-constrained
- Statutory damages create meaningful incentives for compliance without requiring proof of quantifiable harm

---

## Loopholes, Shortcomings, and Rectification

### Comprehensive Health Data Protection Act

#### Potential Loopholes

| Loophole | Description | Severity |
|----------|-------------|----------|
| Definition gaming | Companies may argue certain data types are not "health data" under the definition | High |
| Consent fatigue | Frequent consent requests may lead to automatic acceptance | Medium |
| Research exception abuse | Broad research exception could be exploited for commercial purposes | High |
| De-identification end-run | Companies may de-identify data to avoid consent requirements | High |
| Jurisdictional arbitrage | Companies may move operations offshore to avoid coverage | Medium |

#### Shortcomings

| Issue | Impact | Root Cause |
|-------|--------|------------|
| Excludes government entities | Government health data collection not covered | Political compromise to secure passage |
| Revenue threshold | Small companies exempt initially | Compliance burden concerns |
| Enforcement lag | Private right of action may take years to develop meaningful case law | Inherent in litigation-based enforcement |

#### Rectification Procedures

1. Issue regulatory guidance defining "health data" categories with specific examples and edge cases
2. Require standardized consent interfaces to reduce consent fatigue and dark patterns
3. Require all research exception uses to be registered in a public database
4. Strengthen de-identification standards and impose penalties for re-identification
5. Apply law extraterritorially to any entity processing U.S. residents' health data

### Reproductive Health Data Protection Act

#### Potential Loopholes

| Loophole | Description | Severity |
|----------|-------------|----------|
| "Lawful where provided" definition | States may attempt to criminalize assisting out-of-state care | High |
| Metadata exposure | Act may not adequately cover metadata (timing, frequency) that reveals patterns | Medium |
| Third-party intermediaries | Data may flow through intermediaries not clearly covered | Medium |

#### Rectification Procedures

1. Define "lawful where provided" to include care lawful under federal law or the law of any state where the provider is located
2. Explicitly include metadata in the definition of protected reproductive health data
3. Extend coverage to all entities in the data supply chain

### General Implementation Concerns

#### Systemic Issues

| Issue | Proposed Solution |
|-------|------------------|
| Enforcement funding inadequacy | Tie enforcement funding to penalty revenue; create dedicated health data enforcement fund |
| Technology evolution outpacing law | Require biennial review and update of regulatory definitions |
| International data transfers | Require health data adequacy assessments for cross-border transfers |
| AI-inferred health data | Explicitly include AI-derived health inferences in statutory definitions |

#### Sunset and Review Provisions

- Require GAO report on implementation effectiveness within 3 years of enactment
- Mandate HHS and FTC joint report on health data practices every 2 years
- Include 7-year review provision for congressional reassessment of statutory definitions and thresholds

---

## References

- Health Insurance Portability and Accountability Act, Pub. L. 104-191 (1996)
- HITECH Act, Pub. L. 111-5, Title XIII (2009)
- Genetic Information Nondiscrimination Act, Pub. L. 110-233 (2008)
- 42 CFR Part 2 (Substance abuse treatment record confidentiality)
- FTC Act, 15 U.S.C. 45 (Section 5 unfair and deceptive practices)
- Washington My Health My Data Act, RCW 19.373 (2023)
- HHS, "HIPAA Privacy Rule and Disclosures of Information Relating to Reproductive Health Care," 89 Fed. Reg. 32,976 (April 2024)
- *Sorrell v. IMS Health Inc.*, 564 U.S. 552 (2011)
- *Dobbs v. Jackson Women's Health Organization*, 597 U.S. 215 (2022)
- *Carpenter v. United States*, 585 U.S. 296 (2018)
- FTC, "Data Brokers: A Call for Transparency and Accountability" (2014)

## Related Topics

- [Data Brokers: Legislation](../data-brokers/11-legislation.md) - Regulation of health data brokers
- [Consumer Data Rights: Legislation](../consumer-data-rights/11-legislation.md) - Comprehensive privacy legislation framework
- [Healthcare: Legislation](../../healthcare/11-legislation.md) - Health system reform context
- [Privacy: Legislation](../11-legislation.md) - Parent topic legislation

## Document Navigation

- Previous: [Actions](10-actions.md)
- Next: [Perspectives](12-perspectives.md)
- Up: [Overview](01-overview.md)
