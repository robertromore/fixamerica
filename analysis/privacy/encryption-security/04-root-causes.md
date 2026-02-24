# Encryption and Security: Root Causes

## Overview

The persistent government effort to weaken encryption is not driven by a single cause. It results from institutional incentives, knowledge gaps, political dynamics, and genuine but misguided policy concerns that together create recurring pressure against strong encryption. Understanding these root causes explains why the same failed arguments resurface in each generation and why they remain politically potent despite the technical consensus against backdoors.

---

## Root Cause 1: Institutional Incentives of the Surveillance State

### Description

Law enforcement and intelligence agencies have deep institutional interests in maintaining and expanding their surveillance capabilities. Encryption threatens those capabilities, and agencies lobby relentlessly for tools to circumvent it.

### Mechanism

- **Budget and mission justification**: Agencies define their mission partly through surveillance capability; losing access threatens institutional relevance
- **Risk aversion**: Officials fear being blamed for an attack that encrypted communications "could have" prevented
- **Revolving door**: Former officials join cybersecurity and surveillance companies, reinforcing the access-first mindset
- **Classified capabilities shape public claims**: Agencies make "going dark" claims publicly while possessing classified capabilities they cannot disclose, distorting the public debate

### Evidence

- FBI Director James Comey's sustained public campaign against encryption (2014-2017), despite FBI's own admission that the "going dark" device count was inaccurately inflated
- NSA's covert BULLRUN program to weaken encryption standards while publicly supporting strong encryption
- DOJ and FBI consistently overstate the operational impact of encryption without providing verifiable data (GAO 2021)

---

## Root Cause 2: Technical Illiteracy Among Policymakers

### Description

Most legislators, judges, and senior government officials lack the technical background to evaluate encryption claims. This knowledge gap allows law enforcement agencies to make technically impossible demands seem reasonable.

### Mechanism

- **"Just make it work" mindset**: Policymakers assume that technology companies can solve any problem, including creating secure backdoors
- **Analogy failure**: Legislators compare encrypted communications to locked safes or sealed envelopes, ignoring the fundamental mathematical differences
- **Information asymmetry**: Law enforcement presents detailed case studies; cryptographers offer abstract mathematical arguments
- **Revolving door expertise**: Technical staff cycle out of government; institutional knowledge is lost

### Evidence

- During the Apple-FBI hearing (2016), multiple senators asked Apple to "just figure out" how to provide access while maintaining security
- Senator Lindsey Graham initially supported the EARN IT Act but admitted in committee that he did not understand the technical implications
- The LAEDA bill mandated a "technical capability" that every major cryptographer has stated is impossible to build securely

---

## Root Cause 3: Emotional Exploitation of Child Safety

### Description

Law enforcement and anti-encryption advocates consistently frame the encryption debate around child sexual abuse material (CSAM) and child exploitation, making it politically radioactive to defend encryption.

### Mechanism

- **Moral framing**: Encryption defenders are cast as protecting child abusers
- **Legislative vehicle**: CSAM is used to justify bills (EARN IT, STOP CSAM) that would undermine encryption for all purposes
- **Bipartisan agreement on the problem**: Unlike most policy areas, child safety has universal support, making it an effective Trojan horse
- **Narrative simplification**: Complex technical tradeoffs are reduced to "encryption protects pedophiles"

### Evidence

- The EARN IT Act explicitly uses CSAM as its justification for creating liability for E2EE platforms
- NCMEC regularly testifies against encryption without acknowledging that 99%+ of its reports come from non-E2EE sources
- Attorney General William Barr's 2019 letter to Facebook explicitly invoked child exploitation to oppose Messenger E2EE

---

## Root Cause 4: National Security Exceptionalism

### Description

National security claims are used to override normal policy analysis, enabling agencies to demand capabilities that would be rejected in any other context.

### Mechanism

- **Classification barrier**: Intelligence agencies can make claims about threats without providing evidence
- **Deference culture**: Congress and courts traditionally defer to intelligence community claims on national security
- **Fear of blame**: No politician wants to be accused of having enabled a terrorist attack by defending encryption
- **Five Eyes coordination**: Allied intelligence agencies coordinate pressure for encryption weakening, creating international momentum

### Evidence

- Five Eyes communiques (2018, 2020) demanded "lawful access" to encrypted communications
- Australia's TOLA Act was passed with minimal debate under national security framing
- UK's Online Safety Act received royal assent despite warnings from cryptographers that it would undermine global encryption standards

---

## Root Cause 5: Regulatory Lag and Path Dependence

### Description

The regulatory framework for communications surveillance was built for telephone networks, where wiretapping was technically straightforward. Institutions have not adapted to a world where strong encryption makes content interception infeasible.

### Mechanism

- **CALEA model**: The 1994 Communications Assistance for Law Enforcement Act established the precedent that communications providers must build in surveillance capabilities -- but explicitly excluded internet services
- **Expectation of access**: Law enforcement has come to expect real-time access to communications content, treating it as a right rather than a technical capability
- **Institutional inertia**: Agencies resist developing alternative investigative techniques when they believe they can force access through legislation
- **Legal framework gap**: No law clearly protects the right to use strong encryption, creating recurring legislative threats

### Evidence

- FBI continues to seek CALEA-like mandates for internet services despite 30 years of exemption
- Law enforcement investment in alternative investigative techniques remains minimal compared to advocacy for backdoors
- The Vulnerabilities Equities Process remains executive-order-based, not statutory, reflecting reluctance to formalize encryption protections

---

## Root Cause 6: Misaligned Incentives Between Offense and Defense

### Description

Within the US government, offensive agencies (NSA, CIA) that benefit from exploiting vulnerabilities have more political power than defensive agencies (CISA, NIST) that benefit from strong encryption.

### Mechanism

- **Budget asymmetry**: NSA's budget ($11+ billion) dwarfs CISA's ($2.9 billion), reflecting institutional priorities
- **Offensive preference**: Stockpiling vulnerabilities for offensive use is prioritized over patching them for defense
- **Dual NSA mission**: NSA is responsible for both signals intelligence (breaking encryption) and information assurance (securing US systems), creating an inherent conflict
- **VEP weakness**: The Vulnerabilities Equities Process lacks independent oversight and favors retention for offensive use

### Evidence

- Shadow Brokers leak (2016-2017) released NSA offensive tools that were then used in the WannaCry and NotPetya attacks
- Dual_EC_DRBG backdoor was inserted by NSA into a NIST encryption standard, undermining trust in US standards bodies
- Former NSA Director Michael Hayden stated: "America is more secure with unbreakable encryption" -- contradicting his own agency's offensive mission

---

## Root Cause 7: Absence of Constitutional or Statutory Protection

### Description

Unlike the First Amendment's protection of speech or the Fourth Amendment's protection against unreasonable searches, there is no explicit constitutional or statutory right to use encryption. This creates a persistent vulnerability to legislative attack.

### Mechanism

- **No affirmative right**: While *Bernstein v. United States* recognized encryption code as speech, no law affirms the right to use encryption
- **Legislative vacuum**: Without a protective statute, each Congress can introduce bills mandating backdoors
- **Recurring threat**: The Secure Data Act and similar protective bills have been introduced but never enacted
- **Political asymmetry**: Opposing encryption is framed as "pro-safety"; defending encryption requires explaining technical concepts

### Evidence

- Encryption-protective bills (Secure Data Act, ENCRYPT Act) have been introduced in multiple Congresses but never enacted
- Anti-encryption bills (EARN IT Act, LAEDA) receive committee hearings and markup despite technical impossibility
- No court has definitively ruled that individuals have a right to use encryption without government-mandated backdoors

---

## Root Cause Summary

| Root Cause | Category | Severity | Reform Difficulty |
|------------|----------|----------|-------------------|
| Institutional surveillance incentives | Institutional | Critical | Very high -- requires cultural change |
| Technical illiteracy among policymakers | Knowledge | High | Medium -- education and advisory bodies |
| Emotional exploitation of child safety | Political | High | High -- politically dangerous to counter |
| National security exceptionalism | Political | High | High -- deference culture is entrenched |
| Regulatory lag and path dependence | Structural | Medium | Medium -- legislative reform |
| Offense-defense misalignment | Institutional | High | High -- requires restructuring |
| Absence of legal protection | Legal | Critical | Medium -- requires legislative action |

## Interaction Effects

1. **Technical illiteracy + child safety framing**: Policymakers who do not understand encryption are especially susceptible to emotional arguments about CSAM
2. **Institutional incentives + national security claims**: Agencies use classification to prevent scrutiny of their claims about encryption's impact
3. **Absence of legal protection + recurring bills**: Without a protective statute, encryption advocates must fight defensively in every Congress
4. **Offense-defense misalignment + vulnerability stockpiling**: NSA's dual mission creates government-wide conflicts about encryption strength
5. **Regulatory lag + expectation of access**: Law enforcement's expectation of wiretap-era capabilities drives demands for encryption weakening

## Related Topics

- [Privacy: Root Causes](../04-root-causes.md) - Broader privacy root cause analysis
- [Government Surveillance](../government-surveillance/01-overview.md) - Surveillance state root causes
- [Technology](../../technology/01-overview.md) - Technology regulation root causes

## Document Navigation

- Previous: [History](03-history.md)
- Next: [Stakeholders](05-stakeholders.md)
