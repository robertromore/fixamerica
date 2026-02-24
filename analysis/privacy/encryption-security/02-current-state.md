---
last_updated: 2026-02-20
status: current
confidence: high
---

# Encryption and Security: Current State

## Encryption Landscape

### Deployment of End-to-End Encryption

| Platform/Service | E2EE Status | Users | Notes |
|-----------------|-------------|-------|-------|
| **WhatsApp** | Default E2EE for all messages since 2016 | 2+ billion | Signal Protocol; owned by Meta |
| **Signal** | E2EE by design | 40+ million MAU (est.) | Gold standard; open-source protocol |
| **iMessage** | E2EE for Apple-to-Apple | 1+ billion Apple devices | Not E2EE for cross-platform SMS |
| **Apple iCloud** | Advanced Data Protection (opt-in E2EE) since 2022 | Available to all users | Major shift; previously accessible to Apple |
| **Google Messages** | RCS with E2EE (default since 2023) | Hundreds of millions | Android default messaging |
| **Telegram** | E2EE in "Secret Chats" only; default chats are cloud-encrypted | 900+ million | Criticized for not defaulting to E2EE |
| **Facebook Messenger** | Default E2EE rolled out 2023 | 1+ billion | Previously opt-in; now default |
| **Zoom** | E2EE available (opt-in) since 2020 | 300+ million | Not default; reduces some features |
| **Microsoft Teams** | E2EE for 1:1 calls (opt-in) | 320+ million MAU | Limited E2EE support |
| **ProtonMail** | E2EE by design | 100+ million accounts | Based in Switzerland |
| **iPhone/iOS** | Full-disk encryption default since iOS 8 (2014) | 1+ billion | Key to Apple-FBI dispute |
| **Android** | Full-disk encryption default since Android 6 (2015) | 3+ billion | Varies by manufacturer |

### Encryption Standards

| Standard | Use | Status |
|----------|-----|--------|
| **AES-256** | Symmetric encryption for data at rest and in transit | Industry standard; no known practical attacks |
| **RSA-2048/4096** | Public key cryptography | Widely used; quantum computing poses future threat |
| **TLS 1.3** | Transport layer security for web traffic | Current standard (2018); adopted by major browsers |
| **Signal Protocol** | End-to-end encrypted messaging | Used by Signal, WhatsApp, Facebook Messenger |
| **WireGuard** | VPN protocol | Modern, lightweight; growing adoption |
| **Post-quantum cryptography** | Quantum-resistant algorithms | NIST finalized first standards (2024); migration beginning |

## Legislative Landscape

### US Federal Proposals

| Proposal | Year(s) | Sponsor(s) | Status | Key Provisions |
|----------|---------|------------|--------|----------------|
| **EARN IT Act** | 2020, 2022, 2023 | Graham (R-SC), Blumenthal (D-CT) | Not enacted; reintroduced | Strips Section 230 liability protection for platforms that use E2EE; enables states to mandate scanning |
| **Lawful Access to Encrypted Data Act (LAEDA)** | 2020 | Graham (R-SC), Cotton (R-AR), Blackburn (R-TN) | Not enacted | Mandates "assistance capability" (backdoor) for E2EE services with 1M+ users |
| **STOP CSAM Act** | 2023 | Durbin (D-IL), Graham (R-SC) | Committee passage | Creates liability for E2EE platforms that cannot detect CSAM; effectively mandates scanning |
| **Kids Online Safety Act (KOSA)** | 2024 | Blumenthal (D-CT), Blackburn (R-TN) | Passed Senate 2024 | Age verification provisions may undermine encryption |
| **RESTRICT Act** | 2023 | Warner (D-VA) | Stalled | Broad authority over "ICTS transactions"; encryption implications unclear |

### Encryption-Protective Proposals

| Proposal | Year | Sponsor(s) | Status | Key Provisions |
|----------|------|------------|--------|----------------|
| **Secure Data Act** | 2018, 2020 | Zoe Lofgren (D-CA), Thomas Massie (R-KY) | Not enacted | Prohibits government from mandating backdoors in encryption |
| **ENCRYPT Act** | 2020 | Eshoo (D-CA), Lofgren (D-CA) | Not enacted | Prevents states from mandating encryption backdoors; federal preemption |
| **Warrant-Proof Encryption Act** | Various | Ron Wyden (D-OR) | Not enacted | Protects right to use encryption; prohibits backdoor mandates |

### International Legislation

| Country/Bloc | Law/Proposal | Year | Effect on Encryption |
|-------------|-------------|------|---------------------|
| **United Kingdom** | Online Safety Act | 2023 | Ofcom can require platforms to use "accredited technology" to scan E2EE messages; Apple withdrew Advanced Data Protection from UK |
| **Australia** | Telecommunications and Other Legislation Amendment (TOLA) Act | 2018 | Requires providers to give "technical assistance" and "technical capability" to law enforcement; includes backdoor provisions |
| **European Union** | Chat Control (CSA Regulation proposal) | 2022-present | Would require platforms to scan all messages including E2EE for CSAM; ongoing debate |
| **India** | IT Rules (Traceability requirement) | 2021 | Requires "first originator" identification in E2EE messaging; challenged in court |
| **Russia** | Federal Law on Information | Various | Requires encryption keys to be provided to FSB; VPN restrictions |
| **China** | Cryptography Law | 2020 | Requires commercial encryption products to undergo government review |
| **Brazil** | Court orders to block encrypted services | 2015-2016 | WhatsApp blocked multiple times by courts; resolved legislatively |

## Law Enforcement Claims

### The "Going Dark" Argument

| Claim | Evidence For | Evidence Against |
|-------|-------------|------------------|
| Encryption blocks lawful wiretaps | FBI reported 2,778 devices it could not access in FY 2017 (later revised to ~1,200 due to counting error) | FBI acknowledged the count was inflated by a factor of 2-3 |
| Criminals use encryption to evade detection | Some criminal communications are encrypted | Law enforcement has more digital evidence available than ever (metadata, location, cloud data, social media) |
| Child exploitation hidden by encryption | CSAM distribution moves to encrypted platforms | NCMEC reports increased to 36+ million in 2023 despite encryption; most tips come from hash-matching on unencrypted uploads |
| Terrorism planned via encrypted channels | Some terror plots coordinated on encrypted messaging | Most attackers used unencrypted channels or were known to authorities beforehand |
| Encryption creates "warrant-proof" spaces | Even with a warrant, encrypted data cannot be accessed | No other technology has been required to include government access; physical locks, shredders, and in-person conversations have always been "warrant-proof" |

### FBI and DOJ Statistics

| Metric | Value | Source |
|--------|-------|--------|
| Lawful intercept orders (wiretaps) | 2,023 (2023) | Administrative Office of the US Courts, Wiretap Report |
| Orders encountering encryption | 404 (20%) | AO Wiretap Report (2023) |
| Cases where encryption prevented access | Unclear; FBI does not systematically track | GAO report (2021) |
| Digital evidence available per case | Increasing; metadata, cloud, device forensics | DOJ testimony; academic studies |
| Cellebrite/Graykey device unlock capability | Can access most locked iPhones and Androids with physical access | Industry reports; leaked law enforcement presentations |

### Alternative Investigative Techniques

| Technique | Description | Effectiveness |
|-----------|-------------|---------------|
| **Metadata analysis** | Analyzing communication patterns without accessing content | Highly effective; metadata reveals associations, timing, location |
| **Cloud data access** | Accessing unencrypted cloud backups with warrants | Many users backup messages to unencrypted cloud storage |
| **Device forensics** | Physical device extraction using tools like Cellebrite | Can access most locked devices with sufficient time |
| **Undercover operations** | Infiltrating criminal networks online | Effective for organized crime and terrorism |
| **Cooperating witnesses** | Obtaining access through human sources | Traditional technique remains effective |
| **Endpoint compromise** | Malware or physical access to devices | Used by FBI (NIT) and intelligence agencies |
| **Legal process to providers** | Subpoenas for metadata, account information, unencrypted data | Available for all cloud-based services |

## Cybersecurity Context

### The Cost of Weakening Encryption

| Risk | Potential Impact | Evidence |
|------|-----------------|----------|
| **State-sponsored attacks** | Foreign intelligence services exploit any backdoor | NSA tools leaked by Shadow Brokers (2016-2017); used in WannaCry attack |
| **Criminal exploitation** | Hackers find and exploit government access mechanisms | Clipper Chip key escrow vulnerability (Blaze, 1994) |
| **Economic harm** | Undermined confidence in US technology products | Post-Snowden: US cloud companies estimated $35 billion in lost revenue |
| **Infrastructure vulnerability** | Critical infrastructure depends on strong encryption | Colonial Pipeline, SolarWinds, and similar attacks already exploit weaknesses |
| **Global precedent** | US backdoor mandates empower authoritarian demands | China, Russia, Saudi Arabia would demand identical access |
| **Data breach amplification** | Weaker encryption increases breach severity | Average breach cost $4.45 million (IBM 2023); would increase |

### Encryption and Critical Infrastructure

| Sector | Encryption Dependence | Backdoor Risk |
|--------|----------------------|---------------|
| **Financial services** | All transactions encrypted (TLS, AES) | Catastrophic if compromised |
| **Healthcare** | Patient data (HIPAA requires encryption) | Life-threatening if compromised |
| **Energy/utilities** | SCADA systems, grid communications | National security risk |
| **Defense** | Classified communications, weapons systems | Existential national security risk |
| **Government** | Federal networks, .gov communications | Government operations compromised |
| **E-commerce** | $6.3 trillion in transactions | Economic devastation |

## Vulnerability Equities Process

### Government Stockpiling of Vulnerabilities

| Aspect | Current State | Concern |
|--------|---------------|---------|
| Vulnerabilities Equities Process (VEP) | Executive order (2017) formalizing process for deciding whether to disclose or exploit vulnerabilities | Opaque; no independent oversight |
| NSA zero-day stockpile | Undisclosed number of unpatched vulnerabilities retained for offensive use | Creates systemic risk; Shadow Brokers leak demonstrated danger |
| FBI use of Network Investigative Techniques (NIT) | Court-authorized hacking of criminal suspects' devices | Legal framework unclear; Rule 41 expansion controversial |
| CIA hacking tools | Extensive arsenal revealed by Vault 7 (WikiLeaks, 2017) | Tools target consumer devices including smartphones and smart TVs |

## The Gap

| What Exists | What Is Needed | Current Status |
|-------------|----------------|----------------|
| No federal law protecting encryption from mandated backdoors | Legal protection for strong encryption | Multiple protective bills introduced; none enacted |
| Repeated legislative attempts to mandate backdoors | Evidence-based policy acknowledging technical consensus | EARN IT Act and similar bills reintroduced each Congress |
| Opaque Vulnerabilities Equities Process | Transparent, accountable vulnerability disclosure policy | Executive order only; no statutory framework |
| Law enforcement claims of "going dark" | Honest assessment of available evidence and alternatives | FBI and DOJ continue unsupported claims |
| International pressure to weaken encryption | US leadership in defense of strong encryption globally | US position ambiguous; allies (UK, Australia) mandate access |
| No funding for alternative investigative techniques | Investment in lawful investigative methods that work with encryption | Minimal federal investment in alternatives |

## Sources

- Administrative Office of the US Courts, "Wiretap Report" (2023)
- Abelson, Harold et al. "Keys Under Doormats: Mandating Insecurity by Requiring Government Access to All Data and Communications." MIT Computer Science and Artificial Intelligence Laboratory (2015)
- Apple, "A Message to Our Customers" (February 2016)
- FBI Director James Comey, Senate Judiciary Committee Testimony (2015-2016)
- IBM Security, "Cost of a Data Breach Report" (2023)
- National Academies of Sciences, Engineering, and Medicine. "Decrypting the Encryption Debate." National Academies Press (2018)
- NIST, "Post-Quantum Cryptography Standardization" (2024)
- Office of the Director of National Intelligence, "Vulnerabilities Equities Policy and Process" (2017)
- Schneier, Bruce. "Click Here to Kill Everybody." W.W. Norton, 2018
- Signal Foundation, Press releases and transparency reports (2024)

## Related Topics

- [Government Surveillance](../government-surveillance/01-overview.md) - Surveillance programs targeting encryption
- [Communications Privacy](../communications-privacy/01-overview.md) - Legal framework for communications
- [Law Enforcement Access](../law-enforcement-access/01-overview.md) - Law enforcement data access issues
- [Privacy Overview](../01-overview.md) - Broader privacy context

## Document Navigation

- Previous: [Overview](01-overview.md)
- Next: [History](03-history.md)
