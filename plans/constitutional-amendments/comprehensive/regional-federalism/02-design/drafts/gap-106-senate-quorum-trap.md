# Gap 106 — Senate Quorum Trap for Federal Emergency Inaction

## Draft Constitutional Text: Article IV, Section 4-E

**Version:** v3 (FINAL)
**Date:** 2026-02-03
**Status:** FINAL — Ready for Integration

---

## Gap Description

The Senate must participate in critical constitutional functions including treaty ratification, officer confirmation, constitutional amendments, and (if Section 4-A is adopted) concurrence for safeguard legislation. Federal emergency oversight — specifically, termination of emergencies by joint resolution (Emergency Powers Reform, Section 4(b)) and Congressional Key Override of Two-Key deployment (Article XI, Section 14) — requires Senate participation as part of Congress.

If a minority of Regions (3 of 7) sympathize with a President who has declared an emergency to expand executive power, their Senators (9 of 21) could refuse to attend sessions. Without a clear quorum definition for non-adjudication Senate functions, or an attendance enforcement mechanism during emergencies, "coordinated absence" could prevent the Senate from convening to vote on emergency termination, deployment disapproval, or other constitutional oversight functions.

The Emergency Powers Reform provides auto-expiration for emergencies not reauthorized by Congress, but this only limits the damage window — the President can re-declare, and the initial abuse period (up to 60 days for national security) allows significant harm. For domestic force deployment, Congressional Key Override requires Senate participation, and absence blockage disables this check entirely.

---

## Pre-Existing Coverage Analysis

| Document | Provision | What It Covers | What Remains Uncovered |
|----------|-----------|----------------|------------------------|
| Art. IV, §4(g) | Adjudication quorum = majority of non-recused Senators | Quorum for intergovernmental dispute adjudication | No quorum rule for legislative votes, treaty ratification, or emergency oversight |
| Art. IV, §4-B(d)(iii) | Quorum failure does not toll confirmation clock | Confirmations proceed via deemed confirmation regardless of quorum | Only covers confirmations; no equivalent for emergency votes |
| Emergency Powers Reform, §4(b) | Congress may terminate emergency by joint resolution | Provides termination mechanism | Joint resolution requires both Houses; Senate quorum failure blocks termination |
| Emergency Powers Reform, §4(c) | Auto-termination upon failure to reauthorize | Time-limited fallback | President can re-declare; 60-day security window allows significant abuse before expiration |
| Emergency Powers Reform, §5(b) | Congress meets within 48 hours of declaration | Creates Congressional obligation | Obligation without quorum enforcement is toothless |
| Emergency Powers Reform, §4(f) | Recorded vote required for emergency renewal | Prevents voice vote evasion | Does not address inability to hold the vote at all |
| Art. XI-RF, §2(h)(2) | Governor supermajority (5/7) overrides Two-Key refusal | Bypass for Governor-side obstruction | No equivalent bypass for Senate-side obstruction of Congressional override |
| Art. IV-RF, §5(d) | Political Institutional Failure (180-day Regional quorum failure) | Regional legislative quorum failure triggers receivership | No federal/Senate equivalent for persistent quorum failure |

**Bottom line:** The constitution addresses adjudication quorum, confirmation quorum (indirectly via deemed confirmation), and Regional legislative quorum failure — but has no mechanism for Senate quorum manipulation during emergency oversight functions. This creates a vulnerability where a minority of Regions can shield a President from Congressional checks during emergencies.

---

## Round 1 Convergence Table

| ID | Type | Source(s) | Issue | Resolution |
|----|------|-----------|-------|------------|
| C1 | Convergent | R1-1 #3 + R1-2 F1 | Scheduling game: leadership schedules pro forma sessions with quorum for other business but never calls the emergency vote, resetting "consecutive" counter | Tie persistent quorum failure to the **specific oversight vote** required by §4-E(e). Auto-schedule votes at deadline by operation of law. Quorum for other business doesn't reset count. |
| S1 | Single-reviewer | R1-1 #1 | Circular quorum: Coordinated Absence vote requires quorum but quorum is what's lacking | Add "notwithstanding any quorum requirement" clause to §4-E(c)(2) |
| S2 | Single-reviewer | R1-1 #2 | No minimum-presence floor: a tiny faction could declare coordinated absence and terminate emergency | Add 1/3 seated Senators minimum-presence threshold |
| S3 | Single-reviewer | R1-1 #4 | Supermajority threshold dilution: treaty/override thresholds computed from present, not seated | Supermajority thresholds computed from total seated Senators during coordinated-absence votes |
| S4 | Single-reviewer | R1-2 F2 | Remote participation catch-22: "by law" can be blocked by allies | Self-executing fallback if Congress hasn't legislated |
| S5 | Single-reviewer | R1-2 F3 | Deployment default 7 days too long for tanks on streets | Reduce to 72 hours |
| S6 | Single-reviewer | R1-2 F4 | Re-declaration gap gaming: intervening quorum resets clock | Clock doesn't reset regardless of intervening quorum if substantially same facts |
| S7 | Single-reviewer | R1-2 F5 | Physician certification too soft | Tighten to objective physical incapacity with NCC review |

## Round 2 Convergence Table

| ID | Type | Source(s) | Issue | Resolution |
|----|------|-----------|-------|------------|
| S8 | Single-reviewer | R2-1 #1 (HIGH) | One legitimately incapacitated Senator blocks entire Coordinated Absence finding because (c)(1)(iii) requires "no Senator among the absent group" to have certification | Text fix: change test to whether uncertified absences alone prevent quorum; certified-incapacitated Senators excluded from finding but don't shield uncertified absentees |
| S9 | Single-reviewer | R2-1 #2 (MEDIUM) | 1/3 minimum-presence floor applies only to finding, not subsequent vote | Text fix: extend 1/3 floor to cover both finding and any vote conducted under §4-E(d) |
| DD-20 | Design Decision | R2-1 #3 (MEDIUM) | Simple-majority votes with 4/21 if only 1/3 present | No text change. Intentional: absent Senators chose not to participate and are counted as abstaining. Requiring higher threshold rewards strategic absence. Default outcomes in §4-E(f) provide same result regardless. |

---

## Proposed Constitutional Text

### Section 4-E. Emergency Session Integrity and Quorum Protection

*Addresses Gap 106: The Senate Quorum Trap for Federal Emergency Inaction. Establishes attendance duties, quorum definitions, and default outcomes to prevent coordinated Senate absence from disabling constitutional oversight of emergency powers and domestic force deployment.*

**(a) General Senate Quorum.**

- (1) For all Senate functions other than adjudication under Section 4(g), quorum shall consist of a majority of Senators who have been certified and seated.
- (2) Vacant seats — whether due to death, resignation, removal, expiration of term without a successor, or failure of a Region to elect or appoint Senators — shall not count against quorum calculation.
- (3) A Senator who has been certified and seated but who is absent shall be counted toward the quorum denominator. Deliberate absence does not reduce the number of Senators from whom a majority must be calculated.

**(b) Emergency Session Attendance Duty.**

- (1) During any declared federal emergency under Article XVII, during any active domestic force deployment requiring Congressional oversight, or during any pending Congressional Key Override proceeding under Article XI, Section 14, all Senators shall attend sessions called for emergency oversight purposes unless physically incapacitated.
- (2) Remote participation through secure, authenticated communication satisfies the attendance requirement. Congress shall provide by law for secure remote participation facilities. If such facilities have not been established by law, or are unavailable during an emergency, the Presiding Officer shall accept any commercially available secure communication method that permits visual identification and real-time participation. *(v2 — S4: self-executing remote fallback)*
- (3) Absence from an emergency oversight session without certification of objective physical incapacity — specifically, hospitalization, strict medical isolation, or incapacity preventing both physical and remote participation — by a licensed physician constitutes a breach of constitutional duty. Any Senator may petition the National Constitutional Court for expedited review of such certifications within forty-eight (48) hours. *(v2 — S7: tightened incapacity standard with NCC review)*
- (4) A Senator who is absent without valid cause from three or more emergency oversight sessions within a single emergency period shall be referred to the Senate Ethics Committee and may be subject to censure.

**(c) Coordinated Absence Finding.**

- (1) The Senate Presiding Officer, or in the Presiding Officer's absence the most senior Senator present, may find "Coordinated Absence" when:
    - (i) Senators from two or more Regions are simultaneously absent from an emergency oversight session without certification of physical incapacity meeting the standard of subsection (b)(3); *(v3 — S8: merged Region requirement with uncertified-absence test)*
    - (ii) the uncertified absences under paragraph (i), considered independently of any Senators who have provided valid incapacity certifications, prevent the Senate from achieving quorum; and *(v3 — S8: uncertified absences alone must prevent quorum; certified absences excluded from analysis)*
    - (iii) the absences exhibit a pattern suggesting coordination to defeat constitutional oversight.
- (2) A Coordinated Absence finding may be made by recorded vote of the Senators present, notwithstanding any quorum requirement. A majority of Senators present and voting shall suffice. *(v2 — S1: "notwithstanding any quorum requirement")*
- (3) The Coordinated Absence finding shall specify the names of absent Senators without valid incapacity certification, the session from which they are absent, and the constitutional function the absence prevents. Senators with valid incapacity certifications are excluded from the finding. *(v3 — S8: finding targets only uncertified absentees)*
- (4) No Coordinated Absence finding may be made unless at least one-third of seated Senators are present at the time of the finding. *(v2 — S2: minimum-presence floor)*

**(d) Consequences of Coordinated Absence Finding.**

- (1) Upon a Coordinated Absence finding, absent Senators named in the finding shall be counted as present for quorum purposes.
- (2) The emergency oversight vote shall proceed. Named absent Senators shall be recorded as abstaining, not as absent. Senators excluded from the finding due to valid incapacity certification are not counted as present and are not recorded as abstaining.
- (3) For any vote requiring a simple majority, the threshold shall be a majority of Senators present and voting. For any vote requiring a supermajority threshold specified elsewhere in this Constitution — including but not limited to treaty ratification, constitutional amendment participation, and removal under Section 4-B(f) — the threshold shall be calculated from the total number of seated Senators, not from Senators present and voting. *(v2 — S3: supermajority threshold protection)*
- (4) No emergency oversight vote under this subsection may proceed unless at least one-third of seated Senators are present, including in person and by remote participation. This minimum-presence requirement applies independently of the quorum established by the Coordinated Absence finding. *(v3 — S9: minimum-presence floor extended to vote)*
- (5) A vote conducted under this subsection has the same legal force and effect as a vote conducted with all Senators present.
- (6) The Coordinated Absence finding and the resulting vote shall be published in the official Senate record and transmitted to each Region's Governor and legislature within twenty-four (24) hours.
- (7) A Senator affected by a Coordinated Absence finding may petition the National Constitutional Court for review after the emergency oversight vote has been conducted. The Court shall review only whether the finding was procedurally regular and whether the criteria of subsection (c)(1) were met. No petition shall stay, suspend, or invalidate the vote conducted under this subsection pending review. *(v2 — Q2 resolved: post-hoc appeal)*

**(e) Emergency Oversight Vote Guarantees.**

- (1) **Emergency Termination Vote.** During any declared federal emergency, the Senate shall hold a recorded vote on a joint resolution of termination:
    - (i) within seventy-two (72) hours of the emergency declaration, or within seventy-two (72) hours of a request by any Senator or by the House of Representatives;
    - (ii) at intervals of not more than thirty (30) days thereafter for the duration of the emergency;
    - (iii) these votes may not be delayed, tabled, or prevented by procedural motions, scheduling actions, or adjournment.
- (2) **Domestic Deployment Oversight Vote.** During any active domestic force deployment:
    - (i) the Senate shall hold a recorded vote on disapproval within forty-eight (48) hours of the deployment or within forty-eight (48) hours of a request by any Senator or by the House;
    - (ii) disapproval by majority vote of the Senate, combined with House action as required by law, shall terminate the deployment within seventy-two (72) hours;
    - (iii) these votes may not be delayed, tabled, or prevented by procedural motions, scheduling actions, or adjournment.
- (3) **Congressional Key Override Vote.** When the House has voted to activate the Congressional Key Override under Article XI, Section 14:
    - (i) the Senate shall hold a recorded vote within forty-eight (48) hours;
    - (ii) no procedural motion may delay the vote;
    - (iii) the vote threshold is as specified in Article XI, Section 14(d).
- (4) **Auto-Scheduling.** If a vote required by this subsection has not been scheduled by the Presiding Officer by the deadline specified herein, the vote shall be deemed scheduled by operation of law for noon on the next calendar day. No act of the Presiding Officer, Majority Leader, or any other Senator is required for the vote to occur at the deemed-scheduled time. *(v2 — C1: anti-scheduling-game provision)*

**(f) Default Outcomes upon Persistent Quorum Failure.**

- (1) **Emergency Termination Default.** If the Senate cannot hold the specific emergency termination vote required by subsection (e)(1) — whether due to quorum failure, failure to schedule, or adjournment before voting — for three (3) consecutive required vote occasions or for thirty (30) consecutive calendar days, whichever occurs first, the emergency shall be deemed terminated by operation of law. The holding of quorum for other legislative business does not reset this count. *(v2 — C1: tied to specific oversight vote; quorum for other business doesn't reset)*
- (2) **Deployment Disapproval Default.** If the Senate cannot hold the specific deployment oversight vote required by subsection (e)(2) — whether due to quorum failure, failure to schedule, or adjournment before voting — within seventy-two (72) hours of the required vote, the deployment shall be deemed disapproved and shall terminate within seventy-two (72) hours. *(v2 — S5: reduced from 7 days to 72 hours)*
- (3) **Re-Declaration Limitation.** An emergency terminated under paragraph (1) or a deployment terminated under paragraph (2) may be re-declared or re-authorized by the President, but the same default rules apply to each subsequent declaration or deployment. No re-declaration or re-authorization resets the persistent quorum failure clock, regardless of any intervening period of quorum or legislative session, if the new declaration relies on substantially the same underlying facts or circumstances. *(v2 — S6: strengthened re-declaration hardening)*
- (4) **Interaction with Emergency Powers Reform.** The default termination provisions of this subsection operate in addition to, and do not replace, the auto-expiration provisions of Article XVII, Section 4(c). Where this subsection provides a shorter timeline to termination than Article XVII, this subsection controls.

**(g) Transparency and Accountability.**

- (1) The Senate shall publish, in real time to the extent practicable:
    - (i) quorum status for all emergency oversight sessions;
    - (ii) attendance records for all Senators during emergency periods, including reasons provided for any absences;
    - (iii) the dates and outcomes of all Coordinated Absence findings.
- (2) Within thirty (30) days of the termination of any federal emergency, the Senate shall publish a complete report of attendance, quorum status, and votes during the emergency period.
- (3) The Comptroller General shall include Senate emergency session attendance and quorum data in the post-emergency audit required by Article XVII, Section 5(d).

**(h) Coordination.**

- (1) This section supplements the adjudication quorum provisions of Section 4(g), which continue to govern quorum for intergovernmental dispute adjudication. Where both this section and Section 4(g) could apply, the more specific provision governs.
- (2) The attendance duty and quorum provisions of this section do not modify the confirmation procedures of Section 4-B, which provide independent protection against quorum manipulation through deemed confirmation.
- (3) The emergency oversight vote guarantees of subsection (e) operate in coordination with, and do not replace, the Congressional oversight obligations established in Article XVII, Section 5 (Emergency Powers Reform). Where this section establishes shorter timelines for Senate action, this section controls for the Senate; the House shall act according to its own rules and any applicable provisions of Article XVII.

---

## Gaming Vector Analysis

| # | Vector | Mechanism | How §4-E Addresses |
|---|--------|-----------|---------------------|
| 1 | Sympathetic Absence | 3 Regions' Senators don't attend emergency sessions | §4-E(b): attendance duty; §4-E(c)-(d): Coordinated Absence finding counts uncertified absent as present; §4-E(c)(4): 1/3 minimum-presence floor prevents abuse |
| 2 | Quorum Shield | President ensures allies absent whenever termination vote called | §4-E(f)(1): 30-day persistent quorum failure triggers automatic emergency termination tied to specific oversight vote |
| 3 | Two-Key Bypass | Senate absence prevents disapproval of deployment | §4-E(e)(2): mandatory 48-hour deployment vote; §4-E(f)(2): 72-hour quorum failure triggers deemed disapproval |
| 4 | Rolling Absence | Different Senators absent at different times to prevent quorum without pattern | §4-E(a)(3): absent Senators count toward quorum denominator; §4-E(c): pattern trigger |
| 5 | Physical Incapacity Pretext | Senators claim illness to justify absence | §4-E(b)(3): requires objective physical incapacity with physician certification; NCC review available; §4-E(b)(2): remote participation minimizes legitimate need |
| 6 | Presiding Officer Complicity | Presiding Officer refuses to make Coordinated Absence finding | §4-E(c)(1): most senior Senator fallback; §4-E(e)(4): auto-scheduling; §4-E(f): default outcomes operate regardless |
| 7 | Procedural Delay | Using motions to table or delay emergency votes | §4-E(e)(1)-(3): votes may not be delayed by procedural motions, scheduling, or adjournment |
| 8 | Re-Declaration Cycle | President re-declares after default termination | §4-E(f)(3): clock doesn't reset regardless of intervening quorum if substantially same facts |
| 9 | Senate Recess During Emergency | Senate adjourns to prevent emergency sessions | §4-E(e): votes required within specified timelines regardless of adjournment; §4-E(b)(1): attendance duty triggered by emergency declaration |
| 10 | Override Threshold Gaming | Senate meets quorum but partisan majority blocks override vote | §4-E(e)(3): mandatory vote within 48 hours; cannot be blocked by procedural motions |
| 11 | Scheduling Game | Majority Leader schedules pro forma session with quorum for other business, adjourns without calling emergency vote | §4-E(f)(1): quorum for other business doesn't reset count; §4-E(e)(4): auto-scheduling by operation of law |
| 12 | Circular Quorum Trap | Can't vote to find Coordinated Absence without quorum | §4-E(c)(2): finding may be made notwithstanding quorum requirement |
| 13 | Tiny Faction Exploitation | 1-2 Senators declare coordinated absence, terminate emergency alone | §4-E(c)(4): 1/3 seated Senators minimum-presence floor; §4-E(d)(4): 1/3 floor also applies to vote *(v3 — S9)* |
| 14 | Supermajority Dilution | Coordinated-absence vote on treaty/amendment with lowered effective threshold | §4-E(d)(3): supermajority thresholds computed from total seated Senators |
| 15 | Remote Participation Blockade | President's allies block legislation establishing remote facilities | §4-E(b)(2): self-executing fallback — Presiding Officer accepts secure commercial communication |
| 16 | Incapacity Shield | One legitimately incapacitated Senator provides cover for strategic absentees | §4-E(c)(1)(ii): uncertified absences analyzed independently; certified incapacities excluded *(v3 — S8)* |

---

## Design Decisions

| # | Decision | Rationale |
|---|----------|-----------|
| DD-1 | Placed as §4-E (not new Section 5 subsections as original proposal suggested) | Section 5 is Federal Lawmaking with existing subsections (a)-(g). §4-E follows the §4-B/§4-C/§4-D pattern for Senate procedural protections. |
| DD-2 | General quorum definition in §4-E(a) covers all non-adjudication functions | §4(g) already covers adjudication quorum. The gap is for all other Senate functions. Confirmed by both R1 reviewers (Q1). |
| DD-3 | Coordinated Absence requires 2+ Regions, not 3+ | Two Regions combined with legitimate single-Senator absences could break quorum. Lower threshold catches more gaming. |
| DD-4 | Presiding Officer has primary authority with most-senior-Senator fallback | Prevents Presiding Officer complicity from disabling the entire mechanism. |
| DD-5 | 30-day persistent quorum failure threshold for emergency default termination | Matches emergency renewal interval in Emergency Powers Reform §5. |
| DD-6 | 72-hour threshold for deployment deemed disapproval *(v2 — S5)* | Domestic force deployment creates immediate civil liberties risk; aligns with 48-hour initial vote deadline. |
| DD-7 | Default outcomes operate independently of Coordinated Absence finding | Belt and suspenders. Confirmed by both R1 reviewers (Q5). |
| DD-8 | Censure (not removal) as maximum consequence for breach of attendance duty | Removal creates gaming vectors (opposition triggers vacancies). |
| DD-9 | Objective physical incapacity standard with NCC review *(v2 — S7)* | Hospitalization/strict isolation/incapacity preventing both physical and remote participation. NCC reviews certifications on petition. |
| DD-10 | "Any Senator" can request termination or disapproval vote | Prevents leadership from not scheduling votes. |
| DD-11 | Interaction with Emergency Powers Reform defaults to shorter timeline | No conflict between §4-E and Art. XVII auto-expiration. |
| DD-12 | "Notwithstanding quorum" for Coordinated Absence finding *(v2 — S1)* | The finding is the mechanism to establish quorum. Minimum-presence floor provides legitimacy check instead. |
| DD-13 | 1/3 seated Senators minimum-presence floor *(v2 — S2)* | With 21 Senators, 1/3 = 7 (at least 3 Regions). Prevents tiny faction exploitation. |
| DD-14 | Supermajority thresholds computed from total seated *(v2 — S3)* | Prevents threshold dilution for treaties (2/3 of seated = 14 vs. 2/3 of 7 present = 5). |
| DD-15 | Self-executing remote participation fallback *(v2 — S4)* | Prevents "provide by law" from becoming silent veto on attendance duty. |
| DD-16 | Auto-scheduling by operation of law *(v2 — C1)* | Vote deemed scheduled at noon next day after deadline. No affirmative act required. |
| DD-17 | Persistent quorum failure tied to specific oversight vote *(v2 — C1)* | Quorum for other business doesn't reset counter. |
| DD-18 | Re-declaration hardening regardless of intervening quorum *(v2 — S6)* | One day of quorum between re-declarations doesn't reset protection. |
| DD-19 | Post-hoc appeal to NCC, no stay on vote *(v2 — Q2)* | Vote proceeds; post-hoc challenge preserves due process without delay. |
| DD-20 | Simple-majority threshold with 1/3 present is intentional *(v3 — R2-1 #3)* | Absent Senators chose not to participate. Requiring higher threshold rewards strategic absence. Default outcomes in §4-E(f) provide same result regardless. |
| DD-21 | Uncertified absences analyzed independently of certified incapacities *(v3 — S8)* | Legitimate incapacity should not provide cover for strategic absentees. If uncertified absences alone prevent quorum, finding proceeds; certified Senators excluded from finding and not counted as present. |
| DD-22 | 1/3 minimum-presence floor applies to both finding and vote *(v3 — S9)* | Prevents Senators who participated in the finding from departing before the vote, leaving a smaller group to decide the outcome. |

---

## Open Questions Resolved

All five open questions from v1 were resolved by reviewer consensus in Round 1:

| Q# | Question | Resolution | Rationale |
|----|----------|------------|-----------|
| Q1 | Scope of general quorum | A — All non-adjudication functions | Structural necessity; emergency-only creates future vulnerability |
| Q2 | Coordinated Absence appealability | C — Post-hoc only, no stay | Vote proceeds immediately; post-hoc recourse preserves due process |
| Q3 | Nuclear option (ARB supervision) | B — Default outcomes sufficient | Self-executing defaults are cleaner; ARB supervising Senate creates separation-of-powers crisis |
| Q4 | Absent Senators' vote attribution | A — Deemed abstaining | Deeming votes violates democratic representation; abstaining enables vote without fabrication |
| Q5 | Presiding Officer + senior Senator both refuse | B — Default backstop only | Default outcomes in §4-E(f) provide essential protection regardless of finding |

Round 2 question (R2-1): Should Coordinated Absence be available when uncertified absences alone block quorum, even if some Senators are legitimately incapacitated? **Resolved: Yes.** See DD-21.

---

## Relationship to Other Gaps

| Gap | Relationship |
|-----|-------------|
| Gap 82 (Two-Key Collusion) | Resolved. Gap 106 addresses the Senate component: Congressional Key Override can't function without Senate quorum. §4-E(e)(3) and §4-E(f) ensure override votes occur or default outcomes apply. |
| Gap 90 (Blue-Slipping) | Resolved. §4-D addresses confirmation gaming; §4-E addresses quorum gaming. Different attack vectors on the same institution. |
| Gap 168 (Acting Officials) | Resolved. §4-C time limits + §4-B deemed confirmation address vacancy exploitation. §4-E prevents quorum manipulation from extending vacancy periods. |
| Gap 222 (Confirmation Blockade) | Resolved. §4-B provides deemed confirmation regardless of quorum failure (§4-B(d)(iii)). §4-E provides parallel protection for emergency oversight functions. |
| Gap 169 (Serial Emergency Loophole) | Resolved. Anti-ratcheting provisions address re-declaration. §4-E(f)(3) adds: re-declaration doesn't reset the persistent quorum failure clock. |
| Gap 227 (Emergency Zombie) | Resolved. Emergency Powers Reform time limits + §4-E default termination provide redundant protection. |

---

## Version History

| Version | Date | Changes |
|---------|------|---------|
| v1 | 2026-02-03 | Initial draft. Eight subsections (a)-(h): general quorum, attendance duty, coordinated absence, consequences, vote guarantees, default outcomes, transparency, coordination. 10 gaming vectors, 11 design decisions, 5 open questions. |
| v2 | 2026-02-03 | Round 1 convergence: 1 convergent fix (C1: scheduling game — auto-scheduling + specific-vote-tied quorum failure counter), 7 single-reviewer fixes (S1: notwithstanding quorum; S2: 1/3 minimum-presence floor; S3: supermajority threshold protection; S4: self-executing remote fallback; S5: deployment default 72h; S6: re-declaration hardening; S7: objective incapacity + NCC review). All 5 open questions resolved. Gaming vectors 11-15, design decisions 12-19. |
| v3 | 2026-02-03 | Round 2 convergence: 2 single-reviewer text fixes (S8: uncertified absences analyzed independently — certified incapacities don't block finding; S9: 1/3 minimum-presence floor extended to vote). 1 design decision (DD-20: simple-majority with 1/3 present is intentional). Gaming vector 16, design decisions 20-22. R2-2 confirms Gap 106 CLOSED. **FINAL.** |
