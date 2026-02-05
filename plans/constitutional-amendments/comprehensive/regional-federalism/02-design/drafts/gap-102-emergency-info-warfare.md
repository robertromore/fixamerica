# Gap 102: Emergency Loophole for Information Warfare — Cyber Operations with Domestic Effect

## Status

- **Gap:** 102 — Emergency Loophole for Information Warfare
- **Category:** Emergency Powers & Military
- **Severity:** Medium
- **Current Version:** v3 FINAL
- **Target:** Article XI-RF, Section 7 (new section, supplements Section 6)
- **File:** `02-design/constitution/10-armed-forces.md`

---

## Problem Statement

Article XVI (Cyber Defense) allows the President to conduct cyber defense operations against "nation-state cyber adversaries" and declare cyber emergencies. A President could exploit the undefined boundary between foreign cyber defense and domestic information control by: (1) designating domestic political opposition or independent media as "proxies" of a foreign power, obtaining foreign intelligence authorization under Article XVI, Section 3(e) to target their communications; (2) seizing or directing communications platforms under cyber emergency authority (Article XVI, Section 6(e)); (3) labeling domestic cyber operations as "administrative" or "defensive" to bypass the Two-Key authorization requirement referenced in the compatibility clause; or (4) targeting journalists under the pretext of "protecting" them from foreign exploitation.

The vulnerability is structural: Article XVI, Section 3(e) prohibits targeting US persons "except pursuant to lawful warrant or foreign intelligence authorization" — but the "foreign intelligence authorization" exception swallows the rule when the executive can unilaterally designate any domestic entity as a "foreign proxy." The compatibility clause references "digital force equivalence" requiring Two-Key authorization for cyber-kinetic operations, but this is a compatibility note without operative constitutional text implementing it.

---

## Pre-Existing Coverage Analysis

8 provisions analyzed; warrant requirements and surveillance limits exist but leave the foreign proxy designation loophole, the "administrative bypass" of Two-Key, and the absence of press/platform/election-period protections unclosed:

| # | Provision | What It Covers | What Remains Uncovered |
|---|-----------|----------------|------------------------|
| 1 | Art XVI §3(e) Domestic Targeting Prohibition | No cyber operations targeting US persons without warrant or foreign intelligence authorization | "Foreign intelligence authorization" available after proxy designation — no limitation on who can be designated a "proxy" or judicial review of the designation itself |
| 2 | Art XVI §6 Cyber Emergency Authority | 30-day emergency limit; temporary infrastructure operation for 72 hours after restoration | During ongoing emergency, government can operate critical infrastructure including communications platforms; no platform-specific protections |
| 3 | Art XVI §7 Mass Surveillance Prohibition | Mass surveillance prohibited; FISA warrant required for foreign intelligence; minimization procedures | FISA warrant available after proxy designation; "foreign intelligence" label converts domestic targets into foreign intelligence targets |
| 4 | Art XI-RF Compatibility Clause (line 20) | States "digital force equivalence (cyber-kinetic operations require two-key authorization)" | Compatibility note only — no operative constitutional text implementing Two-Key for cyber operations with domestic effect |
| 5 | Art XI-RF §2(h)(1) Emergency Response for Cyber-Physical Attack | 48-hour Governor response for Two-Key when cyber-physical attack on critical infrastructure | Covers defensive response to infrastructure attacks only — does NOT extend to offensive cyber operations targeting domestic communications |
| 6 | Art XI-RF §4(a)(5) Inherently Governmental Function | Intelligence operations involving surveillance of US persons restricted to sworn officers | Prevents privatization of surveillance but doesn't prevent government itself from conducting surveillance under "foreign intelligence" authority |
| 7 | Art III §4(a)(6) Right to Speak on Public Concerns | Unwaivable core right to speak on matters of public concern, report unlawful conduct | General right without specific protection against cyber operations targeting political speech or journalism |
| 8 | Art II §23(h) First Amendment Preservation | Nothing prohibits criticism of government, reporting on government actions, or political opinion | General preservation clause; no specific prohibition on using cyber operations to suppress speech or target journalists |

**Coverage gap:** No provision (a) extends Two-Key authorization to cyber operations with domestic effect as operative constitutional text, (b) limits the executive's ability to designate domestic entities as "foreign proxies" to obtain foreign intelligence authorization, (c) prohibits government seizure or content control of communications platforms beyond emergency response, (d) creates a specific press and journalist protection floor for cyber operations, or (e) establishes election-period heightened protections against information warfare.

---

## Constitutional Text

### Section 7. Cyber Operations with Domestic Effect

*Resolves Gap 102 — The "Emergency Loophole" for Information Warfare.*

#### Definitions and Scope

(a) **Definitions.** For purposes of this Section and Article XVI: [v1]

(1) A "cyber operation with domestic effect" is any government-directed action using digital means that monitors, intercepts, filters, blocks, degrades, disrupts, or otherwise affects the communications, data, or digital activity of persons within the territory of the United Regions. This definition applies regardless of whether the operation is denominated as "defensive," "administrative," "hygiene," "protective," or any other characterization. [v1]

(2) "Domestic communications" means communications in which at least one party is a United States person located within the territory of the United Regions. [v1]

(3) A "proxy designation" is any determination by the executive branch that a domestic organization, political entity, media organization, or individual is acting as an agent, proxy, or instrumentality of a foreign power or foreign intelligence service. [v1]

#### Two-Key Extension

(b) **Two-Key Authorization for Cyber Operations.** Notwithstanding Article XVI, Section 3(a)-(b) and Section 6: [v1]

(1) Cyber operations with domestic effect are subject to the two-key authorization requirement of Section 2(g) of this Article. No cyber operation with domestic effect may proceed without two-key authorization, except as provided in subsections (b)(3) and (b)(4). [v1]

(2) For purposes of two-key authorization, cyber operations with domestic effect shall be treated as equivalent to domestic deployment of armed forces. The "digital force equivalence" principle stated in the compatibility clause of this Article is hereby given operative constitutional force: cyber capabilities directed at domestic targets receive the same institutional checks as kinetic force. [v1]

(3) **Warrant Exception.** A specific, individualized warrant issued by a court of competent jurisdiction, whose primary purpose is the criminal investigation of identified suspects, pursuant to Article XVI, Section 1(b), satisfies the two-key requirement for the specific target and period identified in the warrant, provided that the operation: [v3: added primary-purpose test and scale constraint]

- (i) is directed solely at specific devices, accounts, or servers identified in the warrant;
- (ii) does not alter the configuration, availability, or integrity of platforms, networks, or services for users other than the named targets;
- (iii) does not constitute strategic information warfare, mass influence operations, or platform-wide disruption.

Warrants issued by the Foreign Intelligence Surveillance Court, or any warrant predicated on foreign intelligence authority rather than criminal investigation, do not satisfy the two-key requirement and must obtain two-key authorization independently. This exception does not apply to mass or bulk operations affecting persons beyond those identified in the warrant. [v2]

(4) **Defensive Operations Carve-Out.** Emergency cyber operations under Article XVI, Section 6 that are purely defensive — limited to blocking incoming attacks against federal networks and critical infrastructure — are not "cyber operations with domestic effect" for purposes of this subsection, provided they do not monitor, intercept, or affect domestic communications. The Director of the Cybersecurity and Infrastructure Security Agency shall certify weekly during any ongoing defensive operation that the operation has not expanded into monitoring, interception, or collection of domestic communications. The CISA Director certification shall be transmitted to the congressional intelligence committees and made available to the National Constitutional Court. Failure to transmit a required weekly certification automatically suspends the defensive operation until the certification is received. An operation that commences as purely defensive but subsequently monitors, intercepts, or collects domestic communications becomes a cyber operation with domestic effect upon such expansion and must obtain two-key authorization before continuing. [v3: added CISA Director weekly certification + automatic suspension]

#### Foreign Proxy Designation Limitations

(c) **Proxy Designation Limitations.** [v1]

(1) The executive branch may not designate a domestic organization, political entity, media organization, or individual as an agent, proxy, or instrumentality of a foreign power except upon a judicial finding by the National Constitutional Court, based on clear and convincing evidence, that the target is a direct agent of a foreign military or intelligence service. [v1]

(2) "Direct agent" means a person or entity that receives operational instructions and material compensation from a foreign government or foreign intelligence service for the purpose of advancing that government's policy objectives. The following do not constitute direct agency: [v1]

- (i) sharing policy views or political positions aligned with those of a foreign government;
- (ii) receiving, publishing, or distributing publicly available foreign media or information;
- (iii) engaging in advocacy that happens to align with foreign government preferences;
- (iv) receiving funding from foreign non-governmental sources for lawful purposes;
- (v) maintaining communication with foreign journalists, academics, or civil society organizations.

(3) The judicial finding shall identify the specific foreign power, the specific operational instructions received, and the specific material compensation provided. General allegations of "foreign influence" or "foreign alignment" do not satisfy this requirement. [v1]

(4) Where national security requires classified submissions in support of a proxy designation, the National Constitutional Court shall appoint a cleared special advocate to represent the target's interests in reviewing the classified evidence. No proxy designation may be based solely on evidence that the target has had no opportunity to contest. [v1]

(5) A proxy designation is valid for one hundred eighty (180) days and must be renewed with fresh evidence demonstrating continued direct agency. Each renewal is subject to the same judicial finding requirement. Lapsed designations may not be retroactively extended. [v1]

(6) The executive branch may not apply cyber operations, surveillance authority, or foreign intelligence collection to any domestic target based on a proxy designation that has not been judicially validated under this subsection. Cyber operations conducted against a domestic target whose proxy designation has lapsed or been judicially invalidated are unlawful and subject to the remedies of Article XVI, Section 7(d). [v1]

#### Platform and Communications Protection

(d) **Platform and Communications Protection.** [v1]

(1) No federal, Regional, or State government may seize, commandeer, or assume operational control of communications platforms, social media services, internet service providers, or telecommunications carriers, except: [v1]

- (i) during a declared cyber emergency under Article XVI, Section 6, limited to the specific infrastructure under active attack;
- (ii) for a period not exceeding seventy-two (72) hours after the attack ceases, as determined under clause (iv);
- (iii) control must be returned to the operator immediately upon restoration of functionality;
- (iv) the seventy-two-hour period begins on the earliest of: a cessation finding by the National Constitutional Court, expiration of the cyber emergency declaration, or voluntary executive certification that the attack has ceased. Any party may petition the National Constitutional Court for a cessation finding; the Court shall rule within forty-eight (48) hours of such petition. [v2]

(2) No government may order, direct, or coerce a communications platform or internet service provider to: [v1]

- (i) filter, block, or remove content based on political viewpoint, policy position, or criticism of government;
- (ii) prioritize, suppress, or algorithmically disadvantage content based on its political character;
- (iii) provide the government with the ability to directly modify, delete, or control content visible to users.

(3) Government requests for content removal based on specific legal violations (fraud, incitement to imminent violence, child exploitation, disclosure of classified information) must be made through public legal process, published within thirty (30) days of the request, and subject to judicial review. The National Constitutional Court may authorize a temporary delay in publication, not exceeding an additional thirty (30) days, upon a sealed showing that immediate publication would compromise active intelligence sources or methods or endanger life. No government entity may issue blanket or categorical removal orders. [v3: added NCC-approved delay mechanism]

(4) Communications platforms designated as critical infrastructure under Article XVI, Section 2(a)(4) retain all protections of this subsection. Critical infrastructure designation does not authorize government content control. [v1]

(5) If government control of infrastructure is voluntarily relinquished under paragraph (1), no new seizure, commandeering, or operational control of the same or substantially similar infrastructure may be initiated for seventy-two (72) hours without prior authorization from the National Constitutional Court. [v3]

#### Press and Political Speech Protection

(e) **Press and Political Speech Protection.** [v1]

(1) No cyber operation may target a journalist, media organization, or press entity absent a specific, individualized warrant meeting all requirements of Article XVI, Section 1(b), and additionally demonstrating: [v1]

- (i) that the target is a direct agent of a foreign military or intelligence service as defined in subsection (c)(2) — not merely a recipient of foreign media, a publisher of foreign-sourced information, or a holder of views aligned with foreign positions;
- (ii) that the cyber operation is the least restrictive means of addressing the specific threat identified.

(2) Incidental collection of journalist communications during lawful cyber operations shall be subject to enhanced minimization procedures. Journalist communications identified during minimization shall be automatically purged within forty-eight (48) hours of identification unless the government obtains a retention warrant from the National Constitutional Court specifically authorizing retention of that journalist's communications. No journalist communications may be disseminated or used for any purpose prior to obtaining a retention warrant. [v2: added 48-hour auto-purge default]

(3) **Election Period Protection.** During the period beginning ninety (90) days before any federal or Regional election — including elections for Regional Governor, Regional Legislature, and federal offices elected from within a Region — and ending thirty (30) days after certification of results: [v2: extended to Regional elections]

- (i) no new cyber operation with domestic effect may be initiated without specific judicial authorization from the National Election Court, in addition to any other authorization required by this Section;
- (ii) existing cyber operations with domestic effect must be reauthorized by the National Election Court, which shall presume against authorization absent clear and convincing evidence of imminent threat to electoral integrity or national security;
- (iii) the National Election Court shall publish a public summary (with classified details redacted) of all cyber operations authorized or denied during the election period, within sixty (60) days after certification;
- (iv) the National Election Court's jurisdiction under this subsection is limited to the authorization or prohibition of cyber operations with domestic effect and does not extend to the adjudication of election results, which remain subject to Regional and State law. [v3]

#### Coordination

(f) **Relationship to Other Provisions.** [v1]

(1) This Section supplements Article XVI. Where Article XVI, Section 3(e) references "lawful warrant or foreign intelligence authorization," the authorization must comply with the proxy designation requirements of subsection (c) of this Section if the target is a domestic entity. [v1]

(2) This Section supplements Article XVII-RF. A cyber emergency declared under Article XVI, Section 6 does not suspend the requirements of subsections (b) through (e). The emergency powers of Article XVI, Section 6(b) are limited to the defensive measures described in Article XVI, Section 6(b)(1)-(4) and do not authorize offensive cyber operations against domestic targets. [v1]

(3) Except as provided in subsection (b)(3), the two-key authorization requirement of subsection (b) applies in addition to, and not in lieu of, the warrant requirements of Article XVI, Section 1(b) and Section 7(b). Where subsection (b)(3) does not apply, both two-key authorization and a warrant must be obtained. [v2: added (b)(3) exception to resolve internal conflict]

(4) The "administrative" characterization of a cyber operation does not exempt it from the requirements of this Section. Any operation meeting the definition of subsection (a)(1) is subject to this Section regardless of organizational assignment — military, intelligence, civilian agency, or contractor. [v1]

(5) The autonomous lethal systems provisions of Section 5 apply independently. Cyber operations that direct autonomous systems to target persons or infrastructure within the United Regions are subject to both Section 5 and this Section. [v1]

(6) Nothing in this Section restricts the authority of federal law enforcement agencies to conduct criminal investigations pursuant to individualized warrants issued by courts of competent jurisdiction under Article XVI, Section 1(b), provided such investigations target specific identified suspects and do not constitute bulk surveillance or mass monitoring of domestic communications. Routine criminal investigation of specific suspects is distinct from cyber defense operations directed at categories of persons, organizations, or communications. [v1]

---

## Gaming Vectors

| # | Vector | Attack | Mitigation |
|---|--------|--------|------------|
| 1 | **Proxy Label Bootstrapping** | President declares opposition is a "foreign proxy" using classified evidence; obtains foreign intelligence authorization to target communications | §7(c)(1): judicial finding required (NCC, clear and convincing evidence); (c)(2): "direct agent" = instructions AND compensation; (c)(4): cleared special advocate for classified evidence; (c)(6): no operations without judicial validation |
| 2 | **Administrative Bypass** | Labels cyber operations "administrative" or "defensive" to avoid Two-Key | §7(a)(1): definition applies regardless of characterization; §7(f)(4): explicit "administrative" characterization prohibition |
| 3 | **Platform Seizure via Permanent Emergency** | Declares permanent cyber emergency to maintain control of communications platforms | §7(d)(1): 72-hour limit after attack ceases; Art XVI §6(c): 30-day emergency limit; §7(f)(2): emergency doesn't suspend (b)-(e); §7(d)(5): 72-hour anti-cycling bar on re-seizure [v3] |
| 4 | **Content Control via Coercion** | Government "requests" platforms suppress content; technically voluntary but backed by regulatory threat | §7(d)(2): prohibits ordering, directing, OR coercing content actions based on political viewpoint; (d)(3): legal removal via public process only |
| 5 | **Journalist Targeting as "Protection"** | Labels journalists "unwitting foreign agents" and monitors to "protect" from exploitation | §7(e)(1): requires same "direct agent" standard; merely receiving foreign media or publishing foreign-sourced information doesn't qualify; least restrictive means required |
| 6 | **Election-Period Information Operations** | Launches domestic cyber operations before elections to suppress opposition communications | §7(e)(3): 90-day pre-election / 30-day post-certification protection; NEC authorization required; presumption against authorization |
| 7 | **Defensive-Offensive Blur** | Claims domestic cyber operations are "defensive" against incoming foreign attacks | §7(b)(4): defensive carve-out limited to blocking incoming attacks; may not monitor/intercept/collect domestic communications; expansion triggers Two-Key; CISA Director weekly certification provides institutional check [v2] |
| 8 | **FISA Court Shopping** | Seeks foreign intelligence authorization from FISC to bypass NCC proxy designation review | §7(b)(3): FISC warrants do not satisfy Two-Key (only criminal investigation warrants do); §7(f)(1): foreign intelligence authorization must comply with proxy designation requirements regardless of which court issues it [v2] |
| 9 | **Contractor Intermediary** | Uses private contractors to conduct domestic cyber operations, claiming not "government-directed" | §7(a)(1): covers "government-directed" operations; §7(f)(4): organizational assignment (including contractor) irrelevant; Art XI-RF §4(a)(5): surveillance of US persons is Inherently Governmental Function |
| 10 | **Incidental Collection Retention** | Collects journalist communications "incidentally" and retains for intelligence purposes | §7(e)(2): 48-hour auto-purge default; NCC retention warrant required; may not be disseminated or used prior to warrant [v2] |
| 11 | **Proxy Designation Renewal Abuse** | Renews proxy designation indefinitely with recycled evidence | §7(c)(5): renewal requires "fresh evidence demonstrating continued direct agency"; same judicial finding requirement; lapsed designations cannot be retroactively extended |
| 12 | **Bulk Warrant Abuse** | Obtains single warrant covering hundreds of targets to circumvent warrant exception limit | §7(b)(3): warrant exception for "specific, individualized" warrants only; does not apply to "mass or bulk operations affecting persons beyond those identified" |
| 13 | **CISA Director Capture** | Appoints compliant CISA Director who certifies defensive operations despite domestic monitoring expansion | Art XVI §4(c): CISA Director removable only for cause; weekly certification transmitted to congressional intelligence committees and NCC; false certification constitutes grounds for removal [v2] |
| 14 | **Cessation Finding Delay** | Delays acknowledging attack cessation to extend platform control beyond 72 hours | §7(d)(1)(iv): any party may petition NCC for cessation finding; NCC 48-hour ruling deadline; 72-hour clock starts on earliest of NCC finding, emergency expiration, or voluntary executive certification [v2] |
| 15 | **Criminal Pretext Relabeling** | Labels strategic cyber operation as "criminal investigation" to bypass Two-Key via warrant exception | §7(b)(3): primary-purpose test; directed solely at warrant-identified devices/accounts; no platform/network-level effects beyond named targets; explicit prohibition on strategic information warfare disguised as criminal enforcement [v3] |
| 16 | **Voluntary Cessation Cycling** | Voluntarily terminates platform control to avoid NCC scrutiny, then re-seizes under new claim | §7(d)(5): 72-hour anti-cycling bar; no re-seizure of same/substantially similar infrastructure without NCC prior authorization [v3] |

---

## Design Decisions

| # | Decision | Rationale |
|---|----------|-----------|
| DD-1 | **Placed as Art XI-RF §7** | Implements "digital force equivalence" principle from compatibility clause; follows §4 (PMC), §5 (autonomous systems), §6 (confederations) pattern for specific force categories |
| DD-2 | **Two-Key for all cyber operations with domestic effect** | Cyber capabilities directed at domestic communications can be as destructive to civil liberties as kinetic force; same institutional check (Governor approval) required |
| DD-3 | **"Direct agent" standard: instructions AND compensation** | Prevents broad labeling — merely sharing foreign government views, receiving foreign media, or engaging in aligned advocacy doesn't qualify; mirrors established espionage law standards |
| DD-4 | **Cleared special advocate for classified proxy evidence** | Prevents classified evidence from being unchallengeable; borrowed from UK special advocate system and FISA amicus; target's interests represented without compromising classified sources |
| DD-5 | **180-day proxy designation with judicial renewal** | Prevents indefinite designations based on stale evidence; renewal requires fresh evidence; each renewal subject to same judicial finding standard |
| DD-6 | **Warrant exception to Two-Key for individualized warrants** | Specific, judicially supervised warrants against identified targets don't require the same institutional check as broad operations; prevents over-proceduralization of legitimate criminal investigation |
| DD-7 | **Defensive operations carve-out** | Blocking incoming attacks on federal networks/critical infrastructure is genuinely defensive; shouldn't require Two-Key; bounded by prohibition on monitoring domestic communications |
| DD-8 | **Election period heightened protection via NEC** | Elections are period of maximum vulnerability to information warfare; NEC has expertise in electoral integrity; presumption against authorization shifts burden |
| DD-9 | **Content removal via public legal process only** | Prevents secret government censorship; 30-day publication ensures transparency; covers legitimate categories (fraud, incitement, child exploitation, classified information) |
| DD-10 | **Cumulative authorization (Two-Key + warrant)** | Neither alone is sufficient; Two-Key provides institutional check (Governors), warrant provides judicial check; both needed for operations targeting domestic persons |
| DD-11 | **Definition covers all characterizations** | "Administrative," "defensive," "hygiene," "protective" — no label exempts an operation that meets the functional definition; prevents definitional evasion |
| DD-12 | **Expansion trigger for defensive operations** | Operation that begins as defensive but expands to monitor domestic communications must obtain Two-Key before continuing; prevents scope creep from defensive to offensive |
| DD-13 | **"Direct agent" limited to foreign military/intelligence** (OQ-1 → Option A) | Broader definitions (state-owned enterprises, foreign political parties) would sweep in legitimate commercial and diplomatic contacts; espionage law standard provides clearest boundary; false positive risk outweighs marginal coverage gain [v2] |
| DD-14 | **No safe harbor for unauthorized operations** (OQ-2 → Rejected) | Defensive carve-out in §7(b)(4) already covers genuine emergencies; a safe harbor would create a perverse incentive to act first and seek forgiveness later; Two-Key Regional Governor mechanism is designed for rapid response [v2] |
| DD-15 | **Election protection extended to Regional elections** (OQ-3 → Option B modified) | Regional Governors hold Two-Key authority; interference in Regional elections could compromise the Two-Key check itself; coverage includes Governor, Legislature, and federal offices elected from within a Region [v2] |
| DD-16 | **Warrant exception narrowed to criminal investigations** | FISC warrants predicated on foreign intelligence authority do not substitute for Two-Key because the foreign intelligence pathway is the precise vulnerability Gap 102 addresses; criminal investigation warrants involve different institutional actors and judicial standards [v2] |
| DD-17 | **NCC cessation finding with 48-hour deadline** | "Ceases" in (d)(1)(ii) was undefined, allowing executive to indefinitely delay acknowledging cessation; NCC finding provides independent determination; any-party petition prevents executive monopoly on triggering the clock [v2] |
| DD-18 | **CISA Director weekly certification** | For-cause-protected CISA Director (Art XVI §4(c)) provides institutional check independent of executive; weekly cadence balances oversight burden with monitoring need; transmission to intelligence committees and NCC creates accountability trail [v2] |
| DD-19 | **48-hour auto-purge for journalist communications** | Reverses default from "retain unless prohibited" to "purge unless warranted"; 48 hours provides operational window for identifying relevant communications; NCC retention warrant requirement ensures judicial gatekeeping [v2] |
| DD-20 | **Primary-purpose test for criminal warrant exception** (C1) | Prevents relabeling strategic information warfare as criminal investigation; "primary purpose" qualifier requires criminal investigation to be genuine, not pretextual; mirrors established legal standards for warrant exceptions [v3] |
| DD-21 | **Scale constraint on criminal warrant operations** (C1/Q1) | Named-target devices/accounts/servers only; no platform/network-level effects beyond named targets; explicit prohibition on strategic information warfare, mass influence operations, or platform-wide disruption disguised as criminal enforcement [v3] |
| DD-22 | **Anti-cycling rule for voluntary cessation** (C2) | 72-hour bar on re-seizure of same/substantially similar infrastructure after voluntary relinquishment; NCC prior authorization required; retains voluntary certification as executive incentive to end operations but prevents terminate-and-re-seize gaming [v3] |
| DD-23 | **Automatic suspension for missed CISA certification** (C4) | Self-executing; no discretionary trigger; failure to transmit weekly certification suspends the operation until certification received; removes incentive to skip certification during scope expansion [v3] |
| DD-24 | **NCC-approved publication delay for content removal requests** (C5, resolves OQ-2) | 30-day default confirmed; NCC-approved delay up to additional 30 days (max 60 total) upon sealed showing of sources/methods or endangerment; balances transparency default with operational reality; resolves OQ-2 by maintaining 30-day default while addressing operational friction [v3] |
| DD-25 | **NEC jurisdiction limited to cyber-op authorization** (C3) | Prevents jurisdictional conflict with Regional courts; NEC reviews the cyber operation, not the election result; election adjudication remains subject to Regional and State law [v3] |
| DD-26 | **Journalist minimization: auto-purge constitutional, details statutory** (resolves OQ-1) | 48-hour auto-purge default in constitutional text provides constitutional floor; additional minimization procedure details (handling, chain of custody, technical implementation) delegated to implementing legislation for technological adaptability [v3] |

---

## Open Questions

All open questions resolved.

*Resolved in v2:* OQ-1 (proxy designation scope) → DD-13; OQ-2 (safe harbor) → DD-14; OQ-3 (Regional elections) → DD-15.

*Resolved in v3:* OQ-1 renumbered (journalist minimization codification) → DD-26; OQ-2 renumbered (publication timeline) → DD-24.

---

## Changelog

- **v1**: Initial draft. 6 subsections (a)-(f) in new Section 7. 12 gaming vectors, 12 design decisions, 5 open questions.
- **v2**: Round 1 review integration. 4 single-reviewer findings accepted (S1-S4), 1 complementary finding accepted (C1), 3 open questions resolved (OQ-1→DD-13, OQ-2→DD-14, OQ-3→DD-15), 1 reviewer question resolved (OQ-6→DD-16). Changes: §7(b)(3) narrowed to criminal investigation warrants only (S1/S2/DD-16); §7(b)(4) added CISA Director weekly certification (S4/DD-18); §7(d)(1)(iv) added NCC cessation finding with 48-hour deadline (S3/DD-17); §7(e)(2) added 48-hour auto-purge for journalist communications (C1/DD-19); §7(e)(3) extended to Regional elections (DD-15); §7(f)(3) added (b)(3) exception clause (S1). 14 gaming vectors (+2), 19 design decisions (+7), 2 open questions (−3).
- **v3 FINAL**: Round 2 review integration. 5 convergent findings (C1-C5), 0 complementary, 0 contradictions, 0 single-reviewer. 1 question subsumed by C1. 2 remaining OQs resolved. Changes: §7(b)(3) added primary-purpose test and three-part scale constraint (C1/Q1/DD-20/DD-21); §7(b)(4) added automatic suspension for missed CISA certification (C4/DD-23); §7(d)(3) added NCC-approved publication delay up to 30 additional days (C5/DD-24); new §7(d)(5) anti-cycling rule — 72-hour bar on re-seizure after voluntary relinquishment (C2/DD-22); §7(e)(3)(iv) added NEC jurisdiction limitation to cyber-op authorization only (C3/DD-25). R2-2 structural reorganization not adopted (cross-reference integrity, operational practicality, future-proofing). 16 gaming vectors (+2), 26 design decisions (+7), 0 open questions (−2).
