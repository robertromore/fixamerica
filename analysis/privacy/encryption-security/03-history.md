# Encryption and Security: History

## Overview

The battle over encryption is one of the longest-running technology policy conflicts in American history. Since the early 1970s, when public-key cryptography was invented, the US government has attempted to maintain a monopoly on strong encryption -- first through export controls, then through key escrow mandates, and now through legislative proposals targeting end-to-end encryption. Each round of this conflict has been resolved in favor of strong encryption, but each generation of policymakers has revived the same arguments, often apparently unaware of the technical and policy lessons of previous rounds.

---

## Era 1: Government Monopoly on Cryptography (Pre-1976)

### Origins

For most of the 20th century, strong encryption was the exclusive province of governments and military organizations:

- The National Security Agency (NSA), established in 1952, was the world's leading cryptographic authority
- Encryption technology was classified as a "munition" under the International Traffic in Arms Regulations (ITAR)
- Private use of strong encryption was effectively prohibited or severely constrained
- The NSA exerted control over encryption research, attempting to suppress academic publication

### Key Developments

| Year | Event | Significance |
|------|-------|-------------|
| 1952 | NSA established | Centralized US government cryptographic capabilities |
| 1967 | David Kahn publishes *The Codebreakers* | First public history of cryptography; NSA attempted to suppress |
| 1970 | Horst Feistel develops Lucifer cipher at IBM | Precursor to DES; private sector cryptographic capability |
| 1973-1974 | NBS (NIST) solicits public encryption standard | Government acknowledged need for civilian encryption |

---

## Era 2: The Birth of Public Cryptography (1976-1992)

### The Cryptographic Revolution

The invention of public-key cryptography by Whitfield Diffie and Martin Hellman in 1976, and the subsequent development of the RSA algorithm by Rivest, Shamir, and Adleman in 1977, fundamentally changed the encryption landscape. For the first time, individuals could encrypt communications without pre-sharing keys -- a capability that had previously been exclusively governmental.

### NSA Opposition

The NSA immediately recognized the threat to its surveillance capabilities:

- NSA attempted to control the Data Encryption Standard (DES) by limiting key length to 56 bits (suspected to be within NSA's breaking capability)
- NSA pressured universities to submit cryptographic research for pre-publication review
- NSA tried to classify foundational cryptographic research
- Conflict between NSA and the academic cryptography community became public

### Key Developments

| Year | Event | Significance |
|------|-------|-------------|
| 1976 | Diffie-Hellman key exchange published | Made public-key cryptography possible |
| 1977 | RSA algorithm developed | Practical public-key encryption |
| 1977 | DES adopted as federal standard | NSA-influenced 56-bit key length; controversy |
| 1978 | NSA pressures Davida to withdraw paper | Government censorship of cryptography research |
| 1982 | NSA/NSF agreement on research funding | NSA gained influence over academic crypto research |
| 1991 | Phil Zimmermann releases PGP | "Pretty Good Privacy" -- first widely available strong encryption for email |
| 1991 | Senate Bill 266 (Biden) | Proposed requiring electronic communications providers to enable government access to plaintext; withdrawn |

### Phil Zimmermann and PGP

Phil Zimmermann's release of Pretty Good Privacy (PGP) in 1991 was a pivotal moment:

- PGP provided strong encryption for email that anyone could use
- The software spread globally via the internet
- The US government opened a criminal investigation against Zimmermann for "exporting munitions" (encryption)
- The investigation lasted three years before being dropped in 1996
- Zimmermann became a symbol of the right to use encryption

---

## Era 3: Crypto Wars I -- The Clipper Chip (1993-2000)

### The Clipper Chip Proposal

In 1993, the Clinton administration proposed the Clipper Chip -- a government-designed encryption chip for telephone communications that included a key escrow mechanism allowing government access:

- Each chip would have a unique key split into two parts, held by two government escrow agents
- Law enforcement could obtain both parts with a court order
- The proposal was backed by the NSA and supported by the FBI

### The Defeat of Key Escrow

| Year | Event | Significance |
|------|-------|-------------|
| 1993 | Clipper Chip announced | Clinton administration mandated key escrow for telephone encryption |
| 1994 | CALEA enacted | Communications Assistance for Law Enforcement Act required telecom wiretap capabilities; excluded internet |
| 1994 | Matt Blaze discovers LEAF flaw | AT&T researcher found security flaw in Clipper's Law Enforcement Access Field, undermining the system |
| 1995 | NRC study commissioned | National Research Council asked to study encryption policy |
| 1996 | NRC report "Cryptography's Role in Securing the Information Society" | Recommended against key escrow; supported widespread encryption |
| 1996 | Export control reforms begin | Administration began easing encryption export restrictions |
| 1997 | Clipper effectively abandoned | Government dropped mandatory key escrow after broad opposition |
| 1998 | *Bernstein v. United States* | Court ruled encryption source code is protected speech under First Amendment |
| 1999 | Export controls significantly eased | Encryption products could be exported with minimal restrictions |
| 2000 | Crypto Wars I ends | Export controls largely lifted; strong encryption legalized for civilian use |

### Why Key Escrow Failed

1. **Technical vulnerability**: Matt Blaze demonstrated that the key escrow mechanism was flawed
2. **Industry opposition**: Technology companies and the business community opposed mandated backdoors
3. **Civil liberties coalition**: EFF, ACLU, and privacy advocates organized broad opposition
4. **Academic consensus**: Cryptographers unanimously opposed key escrow as insecure
5. **International competition**: Foreign companies could sell strong encryption without US restrictions
6. **First Amendment**: Courts recognized encryption code as protected speech

---

## Era 4: Quiet Interlude and Snowden (2001-2014)

### Post-9/11 Surveillance Expansion

The September 11 attacks shifted the encryption debate from overt mandates to covert capabilities:

- The NSA dramatically expanded its surveillance programs under the Patriot Act and executive authority
- Rather than mandating backdoors, the NSA developed capabilities to circumvent encryption
- The BULLRUN program (revealed 2013) aimed to break or weaken encryption standards
- NSA inserted backdoors into encryption standards (Dual_EC_DRBG random number generator)
- The FBI expanded its wiretapping capabilities under CALEA

### Key Developments

| Year | Event | Significance |
|------|-------|-------------|
| 2001 | Patriot Act enacted | Expanded surveillance authority; encryption debate temporarily muted |
| 2004 | FBI begins "Going Dark" advocacy | FBI Director Robert Mueller raised concerns about encryption |
| 2006 | NSA warrantless wiretapping revealed | *New York Times* exposed NSA surveillance without court orders |
| 2007 | Dual_EC_DRBG standardized by NIST | NSA-influenced random number generator later revealed to contain backdoor |
| 2013 | Snowden revelations | Disclosed NSA programs including BULLRUN (encryption circumvention), PRISM (tech company data collection), and upstream collection |
| 2013 | Dual_EC_DRBG backdoor confirmed | Snowden documents showed NSA deliberately weakened the standard |
| 2013 | RSA Inc. controversy | RSA received $10 million from NSA to make Dual_EC_DRBG default in its products |
| 2014 | Apple enables default iPhone encryption (iOS 8) | Encryption activated by default; Apple cannot unlock devices |

### The Snowden Effect

Edward Snowden's 2013 disclosures had profound effects on encryption:

- Public awareness of government surveillance capabilities increased dramatically
- Technology companies accelerated adoption of encryption to restore user trust
- Apple made device encryption default, positioning itself as a privacy company
- WhatsApp, Google, and others expanded E2EE
- The encryption policy debate shifted from hypothetical to urgent
- International trust in US technology companies and standards bodies was damaged

---

## Era 5: Crypto Wars II -- Apple-FBI and Beyond (2015-Present)

### The Apple-FBI Dispute

The San Bernardino shooting (December 2015) led to the most prominent encryption conflict since the Clipper Chip:

- The FBI obtained a court order under the All Writs Act requiring Apple to create software bypassing iPhone security
- Apple refused, arguing that the order would create a dangerous precedent
- The dispute became a national debate about encryption and security
- The FBI ultimately accessed the phone using a third-party tool (reportedly purchased from an Israeli firm for $1 million+)
- The FBI dropped its legal action, leaving the underlying legal questions unresolved

### Legislative Escalation

| Year | Event | Significance |
|------|-------|-------------|
| 2015-2016 | Apple-FBI dispute | National debate over encryption and government access |
| 2016 | Feinstein-Burr bill (draft) | Would have required companies to provide "intelligible" data on court order; never formally introduced |
| 2018 | Five Eyes statement on encryption | Intelligence alliance demanded "lawful access" to E2EE |
| 2018 | Australia TOLA Act | First Five Eyes nation to mandate encryption backdoors |
| 2020 | EARN IT Act introduced | Would strip Section 230 protections from platforms using E2EE |
| 2020 | LAEDA introduced | Would mandate backdoors for E2EE services with 1M+ users |
| 2021 | Apple CSAM scanning announcement | Proposed client-side scanning of iCloud photos; withdrawn after backlash |
| 2022 | EARN IT Act reintroduced | Modified version passed committee; not enacted |
| 2023 | UK Online Safety Act | Ofcom authorized to require scanning of E2EE messages |
| 2023 | Apple withdraws Advanced Data Protection from UK | Response to UK government pressure |
| 2023 | STOP CSAM Act introduced | Creates liability for E2EE platforms |
| 2023 | Facebook Messenger enables default E2EE | Despite law enforcement opposition |
| 2024 | EU Chat Control debate continues | Proposed regulation to scan all messages; strong opposition |
| 2024 | NIST finalizes post-quantum encryption standards | Preparing for quantum computing threats to current encryption |
| 2025 | Signal threatens UK exit | Would leave market rather than comply with scanning mandates |

### Client-Side Scanning

Apple's 2021 announcement of a client-side scanning system for CSAM detection, and its subsequent abandonment, was a defining moment:

- Apple proposed scanning photos on users' devices before iCloud upload using perceptual hashing (NeuralHash)
- Privacy advocates, cryptographers, and civil liberties organizations condemned the system
- Researchers demonstrated that the hashing system could be manipulated (hash collisions)
- Apple postponed and ultimately canceled the feature
- The episode demonstrated that even well-intentioned surveillance mechanisms cannot be made safe

---

## Key Turning Points

| Date | Event | Why It Mattered |
|------|-------|-----------------|
| 1976 | Diffie-Hellman key exchange | Made strong encryption available to non-government actors |
| 1991 | PGP released | Proved encryption could be widely distributed despite government opposition |
| 1993-1997 | Clipper Chip | First major government attempt to mandate backdoors; defeated |
| 1998 | *Bernstein v. United States* | Encryption code recognized as protected speech |
| 2013 | Snowden revelations | Exposed government efforts to weaken encryption; accelerated E2EE adoption |
| 2014 | Apple default encryption | Made device encryption mainstream; set stage for Apple-FBI fight |
| 2015-2016 | Apple-FBI dispute | Crystallized public debate on encryption vs. access |
| 2018 | Australia TOLA Act | First Five Eyes backdoor mandate; created international precedent |
| 2021 | Apple CSAM scanning abandoned | Client-side scanning shown to be technically and politically unviable |
| 2023 | UK Online Safety Act | Most significant current threat to E2EE |

## Lessons from History

1. **Technical consensus has been consistent for 30 years**: Cryptographers have unanimously opposed backdoors since the Clipper Chip, and no technical development has changed their assessment
2. **Government retreats but returns**: Each generation of policymakers attempts backdoor mandates, apparently unaware of previous failures
3. **Market pressure favors encryption**: After each surveillance scandal, technology companies strengthen encryption to maintain user trust
4. **International precedents matter**: Australia's TOLA Act and the UK's Online Safety Act create models that other governments cite
5. **Emotional framing is powerful**: Child safety concerns are used to justify encryption weakening despite minimal evidence of effectiveness
6. **Covert undermining supplements overt mandates**: When governments cannot mandate backdoors, they attempt to covertly weaken encryption standards (Dual_EC_DRBG)
7. **The First Amendment protects encryption**: Courts have recognized encryption code as protected speech, creating a constitutional barrier to mandates
8. **Every backdoor is eventually exploited**: The NSA's own tools were leaked and used in the WannaCry ransomware attack

## Related Topics

- [Privacy: History](../03-history.md) - Broader history of American privacy rights
- [Government Surveillance](../government-surveillance/01-overview.md) - Surveillance program history
- [Technology](../../technology/01-overview.md) - Technology policy history

## Document Navigation

- Previous: [Current State](02-current-state.md)
- Next: [Root Causes](04-root-causes.md)
