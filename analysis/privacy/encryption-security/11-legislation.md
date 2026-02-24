# Encryption and Security: Legislation and Legal Framework

## Overview

Protecting encryption requires a dual legislative strategy: first, enact affirmative legal protections that prohibit government-mandated backdoors and key escrow; second, reform institutional structures that create pressure to weaken encryption, including the Vulnerabilities Equities Process and law enforcement investigative funding. This document provides draft legislative text for priority reforms at the federal and state levels.

## Constitutional Amendments

No constitutional amendment is required for encryption protection. The First Amendment (encryption code as protected speech, per *Bernstein v. United States*) and the Fourth Amendment (privacy of digital communications, per *Carpenter v. United States* and *Riley v. California*) provide existing constitutional foundations. Federal and state statutory protections are the appropriate vehicle.

However, if statutory protections are repeatedly overridden or courts narrow First and Fourth Amendment protections, a constitutional amendment could be considered:

### Proposed Amendment (If Needed)

```text
Section 1. The right of the people to use encryption to secure
their persons, papers, communications, and effects against
unreasonable surveillance shall not be infringed.

Section 2. Neither the United States nor any State shall require
any person or entity to design, build, maintain, or deploy any
mechanism that weakens, circumvents, or provides exceptional
access to encrypted communications or data.

Section 3. Congress shall have the power to enforce this article
by appropriate legislation.

Section 4. This article shall take effect two years after the
date of ratification.
```

**Note**: This amendment would constitutionalize the right to strong encryption. It is listed as a contingency measure; statutory protection is the preferred and more feasible approach.

## Federal Legislation

### Secure Encryption Act

**Purpose**: Establish comprehensive federal protection for strong encryption, prohibiting mandated backdoors, key escrow, and compelled decryption mechanisms, while affirming the right of individuals and organizations to use encryption of any strength.

**Draft Text**:

```text
SEC. 1. SHORT TITLE.

This Act may be cited as the "Secure Encryption Act of [Year]".

SEC. 2. FINDINGS.

Congress finds the following:

(1) Encryption is essential to the security of digital
    communications, financial transactions, healthcare
    records, critical infrastructure, national defense
    systems, and the privacy of all Americans.

(2) End-to-end encryption protects the communications of
    billions of people worldwide, including journalists,
    domestic violence survivors, political dissidents,
    attorneys, healthcare providers, and ordinary citizens.

(3) The technical consensus among cryptographers and
    cybersecurity experts, as documented in the 2015
    report "Keys Under Doormats" and the 2018 National
    Academies study "Decrypting the Encryption Debate,"
    is that there is no mechanism for providing government
    access to encrypted communications that does not
    create vulnerabilities exploitable by adversaries.

(4) Every prior attempt to mandate government access to
    encryption -- including the Clipper Chip key escrow
    system (1993-1997) and the Dual_EC_DRBG backdoor
    (2007-2013) -- has resulted in security vulnerabilities
    that were exploited by adversaries.

(5) Mandating encryption backdoors would undermine the
    cybersecurity of the United States, weaken critical
    infrastructure protections, and set a global precedent
    empowering authoritarian governments to demand
    identical access.

(6) Law enforcement agencies have access to more digital
    evidence than at any point in history, including
    metadata, location data, cloud-stored data, financial
    records, and device forensics tools.

(7) Encryption source code is protected speech under the
    First Amendment, as recognized in Bernstein v.
    United States, 176 F.3d 1132 (9th Cir. 1999).

SEC. 3. DEFINITIONS.

In this Act:

(1) BACKDOOR.--The term "backdoor" means any hardware or
    software mechanism, feature, or vulnerability that is
    designed, built, or maintained to allow a party other
    than the intended recipient to access encrypted
    communications or data, including--
    (A) key escrow systems;
    (B) split-key mechanisms;
    (C) master keys or skeleton keys;
    (D) "ghost" protocol participants;
    (E) client-side scanning systems that report content
        to parties other than the sender and intended
        recipient before, during, or after encryption; and
    (F) any other mechanism that provides exceptional
        access to encrypted communications or data.

(2) ENCRYPTION.--The term "encryption" means any method of
    converting data into a form that is unintelligible
    without the use of a cryptographic key, including
    end-to-end encryption, full-disk encryption, file
    encryption, and transport encryption.

(3) ENCRYPTION PROVIDER.--The term "encryption provider"
    means any person or entity that develops, distributes,
    or operates a product or service that provides
    encryption capabilities to users.

(4) END-TO-END ENCRYPTION.--The term "end-to-end encryption"
    means encryption in which the plaintext content of a
    communication is accessible only to the sender and
    the intended recipient, and is not accessible to the
    encryption provider, any intermediary, or any third
    party.

(5) EXCEPTIONAL ACCESS.--The term "exceptional access" means
    any mechanism, whether mandated by law or otherwise,
    that enables a party other than the intended recipient
    to access the plaintext of an encrypted communication
    or the decrypted form of encrypted data.

(6) CLIENT-SIDE SCANNING.--The term "client-side scanning"
    means any system that analyzes the content of a
    communication or data on a user's device and reports
    findings to a party other than the user, regardless
    of whether such analysis occurs before, during, or
    after encryption.

SEC. 4. PROHIBITION ON MANDATED BACKDOORS.

(a) IN GENERAL.--No Federal agency, State, or political
    subdivision of a State may--
    (1) require, request through legal process, or otherwise
        compel an encryption provider to design, build,
        maintain, deploy, or operate a backdoor in any
        product or service;
    (2) require an encryption provider to provide
        exceptional access to encrypted communications
        or data;
    (3) require an encryption provider to implement
        client-side scanning or similar content analysis
        as a condition of operating in the United States;
    (4) impose liability on an encryption provider based
        on the provider's use of end-to-end encryption
        or refusal to implement a backdoor; or
    (5) condition any license, certification, benefit,
        or privilege on the weakening of encryption or
        the implementation of exceptional access.

(b) COURT ORDERS.--No court shall issue an order requiring
    an encryption provider to--
    (1) decrypt communications or data that the provider
        does not have the technical ability to decrypt;
    (2) redesign, modify, or degrade encryption in any
        product or service; or
    (3) build, deploy, or maintain a backdoor or
        exceptional access mechanism.

(c) PRESERVATION OF EXISTING OBLIGATIONS.--Nothing in this
    section shall be construed to--
    (1) limit the authority of law enforcement to obtain
        data through lawful process directed at an
        encryption provider, where the provider possesses
        the data in unencrypted form or possesses the
        technical ability to decrypt the data; or
    (2) limit law enforcement use of lawful investigative
        techniques, including device forensics, metadata
        analysis, undercover operations, or other methods
        that do not require weakening encryption.

SEC. 5. RIGHT TO USE ENCRYPTION.

(a) AFFIRMATIVE RIGHT.--Every person in the United States
    has the right to use encryption of any type and any
    strength to protect their communications, data, and
    digital property.

(b) NO ADVERSE INFERENCE.--The use of encryption by any
    person shall not serve as the basis for--
    (1) an inference of criminal intent or wrongdoing;
    (2) probable cause for a search warrant;
    (3) the denial of any license, benefit, or privilege;
        or
    (4) any adverse action by a government entity.

(c) ENCRYPTION CODE AS SPEECH.--Congress affirms that
    encryption source code is protected speech under the
    First Amendment to the Constitution, consistent with
    Bernstein v. United States, 176 F.3d 1132
    (9th Cir. 1999).

SEC. 6. FEDERAL PREEMPTION.

(a) PREEMPTION.--This Act preempts any State or local law,
    regulation, or ordinance that--
    (1) mandates the implementation of a backdoor or
        exceptional access mechanism in any encryption
        product or service;
    (2) imposes liability on an encryption provider for
        the use of end-to-end encryption; or
    (3) prohibits or restricts the sale, distribution,
        or use of encryption products or services.

(b) PRESERVATION OF STATE AUTHORITY.--Nothing in this Act
    shall preempt any State law that provides greater
    protection for encryption or privacy rights than
    this Act.

SEC. 7. SECTION 230 PROTECTION.

(a) AMENDMENT.--Section 230(c) of the Communications Act
    of 1934 (47 U.S.C. 230(c)) is amended by adding
    at the end the following:

    "(3) ENCRYPTION.--No provider of an interactive computer
    service shall be treated as a publisher or speaker of
    any information provided by another information content
    provider on the basis that such provider uses end-to-end
    encryption, declines to implement a backdoor or
    exceptional access mechanism, or is unable to access
    the content of encrypted communications on its
    platform."

SEC. 8. PENALTIES.

(a) GOVERNMENT VIOLATIONS.--Any Federal official who
    knowingly violates section 4 of this Act shall be
    subject to--
    (1) removal from office or employment; and
    (2) a civil penalty of not more than $100,000 per
        violation.

(b) PRIVATE RIGHT OF ACTION.--Any encryption provider
    compelled to violate this Act may bring a civil action
    in any Federal district court and shall be entitled to--
    (1) declaratory and injunctive relief;
    (2) actual damages or statutory damages of $50,000
        per violation; and
    (3) reasonable attorney's fees and costs.

SEC. 9. EFFECTIVE DATE.

This Act shall take effect on the date of enactment.
```

**Explanation**:

- Section 2 establishes the factual and technical basis for the Act, citing the cryptographic consensus
- Section 3 provides comprehensive definitions covering all known mechanisms for weakening encryption, including client-side scanning
- Section 4 prohibits any government entity from mandating backdoors, exceptional access, or client-side scanning, and prevents courts from ordering encryption weakening
- Section 5 affirms the affirmative right to use encryption and prevents adverse inferences from encryption use
- Section 6 preempts state mandates for backdoors while preserving state authority to provide greater encryption protections
- Section 7 explicitly prevents Section 230 liability for providing E2EE, closing the avenue exploited by the EARN IT Act
- Section 8 provides enforcement through government official penalties and a private right of action for encryption providers

**Potential Challenges**:

- Strong opposition from FBI, DOJ, and law enforcement lobby
- CSAM framing will be used to argue the Act "protects predators"
- Intelligence community may oppose through classified briefings
- International allies (UK, Australia) may pressure against passage
- Some legislators may fear being seen as "soft on crime"

**Refinements**:

- Consider an explicit exemption-prevention clause barring future legislation from creating backdoor exceptions to this Act without supermajority vote
- Add a sunset review (but not a sunset clause) requiring congressional review of the Act's effectiveness every 5 years
- Include findings section addressing CSAM specifically: law enforcement has effective alternative tools for CSAM investigation

### Vulnerability Disclosure Reform Act

**Purpose**: Codify and reform the Vulnerabilities Equities Process, establishing a statutory framework for government disclosure of security vulnerabilities with a presumption favoring disclosure.

**Draft Text**:

```text
SEC. 1. SHORT TITLE.

This Act may be cited as the "Vulnerability Disclosure Reform
Act of [Year]".

SEC. 2. DEFINITIONS.

In this Act:

(1) VULNERABILITY.--The term "vulnerability" means a
    weakness in a computing system, including hardware,
    software, firmware, or protocols, that can be
    exploited to compromise the security of the system.

(2) ZERO-DAY VULNERABILITY.--The term "zero-day
    vulnerability" means a vulnerability that is not
    publicly known and for which no patch or mitigation
    is available.

(3) COVERED AGENCY.--The term "covered agency" means
    any Federal department or agency that discovers,
    acquires, or uses vulnerabilities in computing
    systems, including the National Security Agency,
    the Central Intelligence Agency, the Federal Bureau
    of Investigation, the Department of Defense, and
    the Department of Homeland Security.

SEC. 3. VULNERABILITIES EQUITIES BOARD.

(a) ESTABLISHMENT.--There is established an independent
    Vulnerabilities Equities Board (the "Board").

(b) COMPOSITION.--The Board shall consist of--
    (1) three members with expertise in cybersecurity
        and cryptography, appointed by the President
        with the advice and consent of the Senate;
    (2) one member appointed by the Speaker of the House;
    (3) one member appointed by the Senate Majority Leader;
    (4) the Director of CISA (ex officio); and
    (5) the Director of NIST (ex officio).

(c) INDEPENDENCE.--No member of the Board may be a
    current employee of an intelligence agency or law
    enforcement agency.

(d) SECURITY CLEARANCE.--All Board members shall hold
    appropriate security clearances to review classified
    vulnerability information.

SEC. 4. DISCLOSURE PRESUMPTION.

(a) PRESUMPTION.--There shall be a presumption that any
    vulnerability discovered or acquired by a covered
    agency shall be disclosed to the affected vendor or
    appropriate coordinating body within 90 days.

(b) EXCEPTION.--A covered agency may retain a vulnerability
    without disclosure only if the Board determines, by
    majority vote, that--
    (1) the vulnerability provides intelligence or law
        enforcement value that significantly outweighs
        the cybersecurity risk of non-disclosure;
    (2) no alternative method exists to achieve the
        intelligence or law enforcement objective;
    (3) the affected systems are not widely used in
        critical infrastructure, financial services,
        healthcare, or government; and
    (4) the agency has implemented measures to minimize
        the risk of the vulnerability being independently
        discovered or exploited by adversaries.

(c) TIME LIMIT.--No vulnerability may be retained for
    more than 180 days without re-authorization by the
    Board. There shall be no limit on the number of
    re-authorizations, but each must satisfy the
    criteria in subsection (b).

SEC. 5. REPORTING.

(a) ANNUAL PUBLIC REPORT.--The Board shall publish an
    annual public report disclosing--
    (1) the total number of vulnerabilities reviewed;
    (2) the number disclosed to vendors;
    (3) the number retained, by category of justification;
    (4) the average time to disclosure; and
    (5) any vulnerabilities that were exploited by
        adversaries during the retention period.

(b) CLASSIFIED ANNEX.--The Board may provide additional
    detail in a classified annex available to
    congressional intelligence committees.

SEC. 6. LIABILITY.

(a) GOVERNMENT LIABILITY.--If a vulnerability retained
    by a covered agency under this Act is subsequently
    exploited by an adversary causing harm to United
    States persons or entities, the affected persons
    or entities may bring a civil action against the
    United States under the Federal Tort Claims Act
    (28 U.S.C. 2671 et seq.) for damages resulting
    from the exploitation.

(b) LIMITATION.--Liability under this section shall
    apply only where the Board authorized retention
    and the vulnerability was exploited within the
    retention period or within 90 days thereafter.

SEC. 7. EFFECTIVE DATE.

This Act shall take effect 180 days after the date of
enactment.
```

**Explanation**:

- Section 3 creates an independent oversight board with expertise and security clearances, rather than relying on intelligence community self-governance
- Section 4 establishes a presumption of disclosure, reversing the current default of retention, and requires specific findings to retain vulnerabilities
- Section 5 mandates transparency through annual public reporting
- Section 6 creates government liability for harm resulting from retained vulnerabilities, providing a deterrent against stockpiling

**Potential Challenges**:

- Intelligence community will oppose independent oversight of vulnerability decisions
- Classification barriers complicate public accountability
- Defining "critical infrastructure" broadly enough to capture relevant systems
- Federal Tort Claims Act liability is a significant policy change

### Law Enforcement Digital Investigation Investment Act

**Purpose**: Fund alternative investigative techniques that work alongside strong encryption, providing law enforcement with effective tools while eliminating the argument that backdoors are the only solution.

**Draft Text**:

```text
SEC. 1. SHORT TITLE.

This Act may be cited as the "Law Enforcement Digital
Investigation Investment Act of [Year]".

SEC. 2. FINDINGS.

Congress finds the following:

(1) Law enforcement agencies require effective digital
    investigation capabilities to address serious crime.

(2) The solution to investigative challenges posed by
    encryption is investment in alternative techniques,
    not weakening the encryption that protects all
    Americans.

(3) Alternative investigative techniques -- including
    metadata analysis, device forensics, financial
    tracking, undercover operations, and lawful hacking
    -- are effective and do not compromise the security
    of the broader digital ecosystem.

SEC. 3. DIGITAL INVESTIGATION RESOURCE CENTER.

(a) ESTABLISHMENT.--The Attorney General shall establish
    a Digital Investigation Resource Center (the "Center")
    within the Department of Justice.

(b) MISSION.--The Center shall--
    (1) develop and disseminate digital investigation
        techniques that do not require weakening
        encryption;
    (2) provide training and technical assistance to
        Federal, State, and local law enforcement;
    (3) fund research into lawful alternatives to
        exceptional access;
    (4) maintain a clearinghouse of best practices for
        digital investigation; and
    (5) publish an annual report on the state of digital
        investigation capabilities.

(c) PROHIBITION.--The Center shall not develop, promote,
    or distribute any tool or technique that requires
    mandated backdoors or the weakening of encryption
    standards.

SEC. 4. AUTHORIZATION OF APPROPRIATIONS.

(a) There are authorized to be appropriated $100,000,000
    for each of fiscal years [Year] through [Year+5]
    for the Digital Investigation Resource Center.

(b) Funds shall be allocated as follows:
    (1) 40 percent for State and local law enforcement
        training and technical assistance;
    (2) 30 percent for research and development of
        alternative investigative techniques;
    (3) 20 percent for equipment and tool acquisition; and
    (4) 10 percent for administration and evaluation.

SEC. 5. EFFECTIVE DATE.

This Act shall take effect on the date of enactment.
```

## State Model Legislation

### Model State Encryption Protection Act

**Purpose**: Provide a template for state-level encryption protection, complementing federal legislation and protecting against state-level backdoor mandates.

```text
SECTION 1. SHORT TITLE.

This Act may be cited as the "[State] Encryption Protection
Act".

SECTION 2. DEFINITIONS.

(a) "Backdoor" means any mechanism designed to allow a party
    other than the intended recipient to access encrypted
    communications or data, including key escrow systems,
    split-key mechanisms, master keys, client-side scanning
    that reports to third parties, and any other exceptional
    access mechanism.

(b) "Encryption" means any method of converting data into a
    form that is unintelligible without the use of a
    cryptographic key.

(c) "Encryption provider" means any person or entity that
    develops, distributes, or operates a product or service
    that provides encryption capabilities.

SECTION 3. PROHIBITION ON STATE-MANDATED BACKDOORS.

(a) No State or local government entity may require an
    encryption provider to design, build, maintain, or
    deploy a backdoor in any product or service.

(b) No State or local government entity may impose liability
    on an encryption provider based on the provider's use of
    end-to-end encryption or inability to access the content
    of encrypted communications.

(c) No State or local court may issue an order requiring an
    encryption provider to decrypt communications or data
    that the provider does not have the technical ability
    to decrypt.

SECTION 4. RIGHT TO USE ENCRYPTION.

(a) Every person in this State has the right to use encryption
    of any type and any strength.

(b) The use of encryption shall not be the basis for an
    inference of criminal intent, probable cause for a search
    warrant, or any adverse action by a government entity.

SECTION 5. STATE GOVERNMENT ENCRYPTION REQUIREMENTS.

(a) Within two years of enactment, all State agencies that
    collect, store, or transmit personally identifiable
    information shall implement encryption at rest and in
    transit meeting NIST standards.

(b) The State Chief Information Officer shall publish an
    annual encryption compliance report.

SECTION 6. ENFORCEMENT.

(a) Any person or entity aggrieved by a violation of this Act
    may bring a civil action in State court and shall be
    entitled to declaratory relief, injunctive relief,
    statutory damages of $10,000 per violation, and
    reasonable attorney's fees.

(b) The Attorney General may bring enforcement actions for
    violations by State or local government entities.

SECTION 7. EFFECTIVE DATE.

This Act takes effect on [date of enactment], except that
Section 5 takes effect two years after enactment.
```

### Model State Government Encryption Mandate

**Purpose**: Require state government agencies to adopt strong encryption for citizen data, independent of the encryption protection provisions.

```text
SECTION 1. SHORT TITLE.

This Act may be cited as the "[State] Government Data
Encryption Act".

SECTION 2. ENCRYPTION REQUIREMENTS.

(a) Within 18 months of the effective date, every State
    agency that collects, stores, processes, or transmits
    personally identifiable information shall--
    (1) encrypt all such information at rest using
        AES-256 or equivalent standard;
    (2) encrypt all such information in transit using
        TLS 1.3 or equivalent standard;
    (3) implement access controls limiting decryption
        to authorized personnel;
    (4) maintain encryption key management procedures
        consistent with NIST guidelines.

(b) State contractors and service providers handling
    personally identifiable information on behalf of
    the State shall meet the same encryption requirements.

SECTION 3. REPORTING AND COMPLIANCE.

(a) The State Chief Information Officer shall conduct an
    annual encryption audit of all State agencies.

(b) Audit results shall be published in summary form,
    identifying agencies that are not in compliance.

(c) Agencies not in compliance within 24 months shall
    face reduced appropriations of 5 percent until
    compliance is achieved.

SECTION 4. EFFECTIVE DATE.

This Act takes effect on [date 6 months after enactment].
```

## Regulatory Framework

### Executive Order on Encryption Protection

| Element | Proposed Action |
|---------|----------------|
| **Federal government encryption** | Mandate E2EE for all interagency communications involving sensitive but unclassified information |
| **Vendor requirements** | Require all federal technology vendors to support strong encryption; prohibit procurement of products with mandated backdoors |
| **Vulnerability disclosure** | Strengthen VEP with disclosure presumption pending statutory reform |
| **Post-quantum transition** | Mandate federal transition plan to post-quantum encryption standards by [date] |
| **NIST independence** | Affirm NIST independence from intelligence community influence in standards-setting |
| **International engagement** | Direct State Department to advocate for strong encryption in international forums and oppose backdoor mandates by allies |

### CISA Guidance on Encryption Best Practices

| Element | Proposed Guidance |
|---------|------------------|
| **Critical infrastructure** | All critical infrastructure operators should deploy strong encryption for data at rest and in transit |
| **Incident response** | Encryption status should be a key factor in cybersecurity incident assessment and reporting |
| **Supply chain security** | Federal supply chain security requirements should mandate strong encryption throughout |
| **Post-quantum readiness** | All critical infrastructure operators should begin post-quantum migration planning |
| **Consumer guidance** | CISA should publish consumer-facing guidance on encryption adoption and best practices |

## Legal Considerations

### Constitutional Issues

| Issue | Analysis |
|-------|----------|
| **First Amendment** | Encryption source code is protected speech (*Bernstein v. United States*); compelled backdoor mandates likely violate compelled speech doctrine |
| **Fourth Amendment** | Warrant requirement for digital data (*Carpenter*, *Riley*) supports encryption protections; backdoor mandates would undermine Fourth Amendment privacy |
| **Fifth Amendment** | Compelled decryption implicates self-incrimination privilege; circuit split on whether producing a decryption password is "testimonial" |
| **Commerce Clause** | Federal authority to regulate encryption products in interstate commerce is clear; preemption of state backdoor mandates is constitutionally sound |
| **Due Process** | Government reliance on encryption-weakened systems for citizen services raises due process concerns |

### Preemption

| Dynamic | Analysis |
|---------|----------|
| **Upward preemption (federal over state)** | Federal encryption protection should preempt state backdoor mandates but preserve state authority to provide greater protections |
| **International dimensions** | US statutory protections cannot directly preempt foreign laws (UK Online Safety Act, Australia TOLA), but provide companies legal backing to resist foreign mandates that conflict with US law |
| **Sector-specific interaction** | Encryption protection should supplement, not displace, existing sector-specific encryption requirements (HIPAA, GLBA, FERPA) |

### Enforcement Mechanisms

| Mechanism | Analysis |
|-----------|----------|
| **Criminal penalties for government officials** | Would provide strong deterrent but may face political opposition |
| **Civil penalties and private right of action** | More politically feasible; provides direct remedy for encryption providers compelled to weaken products |
| **Injunctive relief** | Most immediately effective mechanism; courts can block backdoor orders before implementation |
| **Congressional oversight** | Intelligence committee oversight of VEP and government encryption-related activities |

## Loopholes, Shortcomings, and Rectification

### Potential Loopholes

| Loophole | Description | Severity |
|----------|-------------|----------|
| **"Metadata exception"** | Law enforcement argues that metadata (who communicated, when, from where) is not covered by encryption protections; could be used to justify expansive metadata collection as a workaround | High |
| **"Voluntary cooperation" pressure** | Even with a prohibition on compelled backdoors, government agencies may use informal pressure, threats of regulatory action, or procurement preferences to obtain voluntary cooperation | High |
| **Client-side scanning relabeling** | Mandatory content scanning could be reframed as "device-level safety feature" rather than "client-side scanning" to evade the prohibition | High |
| **Foreign intelligence exception** | FISA authorities or intelligence-specific statutes might be claimed to override encryption protections for foreign intelligence purposes | High |
| **Third-party access** | Government contracts with private companies (Cellebrite, NSO Group) to break encryption could circumvent the prohibition on government-mandated backdoors | Medium |
| **State actor proxies** | Foreign allied governments (UK, Australia) could be used to compel backdoors that the US government cannot directly mandate | Medium |
| **Emergency exception abuse** | Broad "emergency" exceptions could be used to justify temporary encryption weakening that becomes permanent | Medium |
| **"Technical assistance" redefinition** | Future legislation could redefine what constitutes "technical assistance" versus a "backdoor," narrowing the protection | Medium |
| **Standards manipulation** | Intelligence agencies could continue to covertly influence encryption standards through NIST participation, as occurred with Dual_EC_DRBG | Medium |
| **Sunset or repeal after crisis** | A major security incident could be used to justify repealing protections under emotional pressure | Low |

### Shortcomings

| Issue | Impact | Root Cause |
|-------|--------|------------|
| **No international enforcement** | US law cannot prevent foreign governments from mandating backdoors; companies operating globally face conflicting requirements | Jurisdictional limitations of national law |
| **Classification barrier** | Intelligence community can make claims about encryption's impact on national security that cannot be publicly evaluated or challenged | Classified information system |
| **Technical evolution** | Legislation may not anticipate future technical mechanisms for accessing encrypted data that fall outside current definitions | Technology outpaces legislation |
| **Enforcement asymmetry** | Government agencies have vastly more resources than encryption providers or civil society to test legal boundaries | Resource imbalance |
| **Covert operations** | Even with strong statutory protections, intelligence agencies may conduct covert operations to undermine encryption outside legal frameworks | Inherent secrecy of intelligence operations |
| **Political vulnerability** | Encryption protections could be weakened or repealed after a major terrorist attack or child exploitation case is publicly linked to encryption | Political dynamics around security crises |

### Rectification Procedures

1. **Metadata protection companion legislation**: Enact a separate statute requiring warrants for metadata collection and limiting bulk metadata analysis; ensure encryption protection extends to traffic analysis, not just content

2. **Anti-pressure provisions**: Prohibit government agencies from using procurement preferences, regulatory threats, or informal pressure to obtain voluntary encryption weakening; require agencies to disclose any requests for voluntary cooperation to congressional oversight committees

3. **Technology-neutral definitions**: Define prohibited conduct based on functional effect (weakening security, providing exceptional access) rather than specific technical mechanisms; include catch-all provision covering "any mechanism that has the effect of enabling access to encrypted communications by parties other than the intended recipient"

4. **Intelligence authority clarity**: Explicitly state that FISA, Executive Order 12333, and other intelligence authorities do not override encryption protection; require any government hacking conducted under intelligence authorities to comply with vulnerability disclosure requirements

5. **Third-party tool oversight**: Require government agencies to disclose (to the oversight board) the use of third-party tools for accessing encrypted devices or communications; apply vulnerability disclosure requirements to vulnerabilities exploited by government-contracted third parties

6. **Allied government coordination**: Establish that US companies may not comply with foreign backdoor mandates that conflict with US encryption protection law; provide diplomatic and legal support for companies resisting foreign mandates

7. **Emergency exception guardrails**: Prohibit any "emergency" exception from the backdoor prohibition; if emergency investigative access is needed, it must use existing lawful techniques (device forensics, metadata analysis, cooperating witnesses) rather than encryption weakening

8. **Standards integrity protection**: Establish a "firewall" between NSA's offensive mission and NIST standards-setting; require independent review of all cryptographic standards for undisclosed vulnerabilities; mandate NIST report any intelligence community attempts to influence standards

9. **Anti-sunset provision**: Require a two-thirds supermajority in both chambers to repeal or materially weaken encryption protections, preventing repeal under crisis-driven emotional pressure

10. **Covert operations reporting**: Require the Director of National Intelligence to report to congressional intelligence committees any intelligence community operations that have the effect of weakening encryption products used by US persons

### General Implementation Concerns

- **Political will**: Passing encryption protection requires overcoming FBI, DOJ, and intelligence community opposition, plus the CSAM-based emotional framing used by opponents
- **Bipartisan coalition maintenance**: Encryption protection requires sustained bipartisan support (libertarian-progressive alliance) that may fracture under political pressure
- **International coordination**: Unilateral US protection is insufficient if key allies mandate backdoors; diplomatic engagement must accompany domestic legislation
- **Post-quantum transition urgency**: Encryption protection must be paired with accelerated migration to quantum-resistant standards to address the "harvest now, decrypt later" threat
- **Public education**: Legislative success depends on public understanding of encryption's importance; sustained investment in education is necessary

## References

- *Bernstein v. United States*, 176 F.3d 1132 (9th Cir. 1999)
- *Carpenter v. United States*, 585 U.S. 296 (2018)
- *Riley v. California*, 573 U.S. 373 (2014)
- Communications Assistance for Law Enforcement Act (CALEA), 47 U.S.C. ss 1001-1010
- All Writs Act, 28 U.S.C. ss 1651
- Electronic Communications Privacy Act, 18 U.S.C. ss 2510-2522
- Foreign Intelligence Surveillance Act, 50 U.S.C. ss 1801 et seq.
- Communications Act of 1934, Section 230, 47 U.S.C. ss 230
- Abelson, Harold et al. "Keys Under Doormats." MIT CSAIL (2015)
- Anderson, Ross et al. "Bugs in Our Pockets: The Risks of Client-Side Scanning." (2021)
- National Academies. "Decrypting the Encryption Debate." (2018)
- EARN IT Act, S. 3398, 116th Congress (2020); S. 3538, 117th Congress (2022)
- Lawful Access to Encrypted Data Act, S. 4051, 116th Congress (2020)
- Secure Data Act, H.R. 5823, 116th Congress (2020)
- ENCRYPT Act, H.R. 5823, 116th Congress (2020)
- Australia Telecommunications and Other Legislation Amendment (TOLA) Act (2018)
- United Kingdom Online Safety Act (2023)
- Office of the Director of National Intelligence, "Vulnerabilities Equities Policy and Process" (2017)
- Federal Tort Claims Act, 28 U.S.C. ss 2671 et seq.

## Related Topics

- [Government Surveillance: Legislation](../government-surveillance/07-solutions.md) - Surveillance reform legislation
- [Communications Privacy: Legislation](../communications-privacy/01-overview.md) - Communications privacy legal framework
- [Law Enforcement Access](../law-enforcement-access/01-overview.md) - Law enforcement data access
- [Privacy Overview](../01-overview.md) - Broader privacy legislative framework
- [International Privacy](../international-privacy/01-overview.md) - International encryption policy

## Document Navigation

- Previous: [Actions](10-actions.md)
- Next: [Perspectives](12-perspectives.md)
