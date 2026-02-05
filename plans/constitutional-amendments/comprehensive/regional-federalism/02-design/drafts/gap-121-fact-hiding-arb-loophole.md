# Gap 121: Fact-Hiding ARB Loophole — Mixed Question Review Doctrine

## Status

- **Gap:** 121 — Fact-Hiding ARB Loophole
- **Category:** Electoral/Judicial Systems
- **Severity:** Medium
- **Current Version:** v3 (FINAL)
- **Target:** Article II, Section 7-B (new section, supplements Section 7)
- **File:** `02-design/constitution/02-powers-and-rights.md`

---

## Problem Statement

Article II, Section 7(k) provides that ARB decisions are "final on factual matters," with Section 7(j) limiting Supreme Court review to "errors of constitutional interpretation" and "violation of due process." A hostile ARB could exploit the undefined boundary between "factual findings" and "constitutional interpretation" by recharacterizing constitutional boundary disputes as factual determinations — e.g., characterizing a power-allocation conclusion as a factual finding about "administrative capacity" or "historical practice" — effectively insulating unconstitutional actions from judicial review.

The vulnerability is structural: the ARB determines whether a matter involves power allocation (§7(p)(3)), and its factual findings are both final (§7(k)) and non-remandable (§7(m)). A factual finding that covertly resolves a constitutional boundary question becomes unreviewable, non-remandable, and immediately binding (§7(i)). The Supreme Court's only recourse — identifying the question as "constitutional interpretation" — fails when the ARB packages the constitutional conclusion inside factual language.

---

## Pre-Existing Coverage Analysis

8 provisions analyzed; none address the law/fact boundary characterization for ARB power-allocation determinations:

| # | Provision | What It Covers | What Remains Uncovered |
|---|-----------|----------------|------------------------|
| 1 | Art II §7(j) Supreme Court Review Scope | Reviews only for errors of constitutional interpretation and due process violations; SC cannot reweigh factual evidence | No mechanism to identify mixed questions where a factual finding determines a constitutional boundary |
| 2 | Art II §7(k) Factual Finality | ARB decisions final on factual matters; constitutional interpretation appealable | No definition of "factual matter" vs. "constitutional interpretation"; no mixed question doctrine; boundary entirely undefined |
| 3 | Art II §7(m) No Factual Remand | SC cannot remand for further factual findings, reconsideration of evidence, or new factual standard | Compounds the problem: a mischaracterized constitutional question becomes both unreviewable AND non-remandable |
| 4 | Art II §7(n) Reversal or Affirmance Only | SC affirms or reverses, specifies correct constitutional interpretation; ARB applies to existing record | Only functions when SC recognizes the question as "constitutional interpretation"; fails when constitutional conclusion is hidden in factual packaging |
| 5 | Art II §7(p)(2)-(3) Self-Determination | Transfers power-allocation filings to ARB; ARB determines whether a matter involves power allocation | Related self-characterization power — ARB controls its own jurisdictional framing, which compounds the characterization vulnerability |
| 6 | Art II §7(aa) Bias Finding | De novo review triggered by statistically significant bias (p<0.05 over rolling 3-year period) | System-level remedy only; requires 3 years of data accumulation; does not address individual case-level characterization gaming |
| 7 | Art II §7-A(g) Factual Finding Limitation | Factual findings are "final" only when based on disclosed data and transparent methodology; algorithmic methodology remains reviewable | Addresses data transparency and methodology, not the fundamental law/fact boundary characterization |
| 8 | Art XIV §9(a)-(c) De Novo Review Mandate | All questions of law reviewed de novo; no deference to agency legal interpretations; factual deference preserved for substantial evidence | Establishes the de novo principle but explicitly preserves factual deference; does not define where the law/fact boundary falls for ARB power-allocation determinations specifically |

**Coverage gap:** No provision defines what constitutes a "factual matter" versus a "constitutional interpretation" in the ARB context, establishes a mixed question doctrine for power-allocation disputes, requires the ARB to identify the nature of its findings, or provides a challenge procedure when constitutional conclusions are packaged as factual findings.

---

## Constitutional Text

### Section 7-B. Mixed Question Review Doctrine

*Resolves Gap 121 — The "Fact-Hiding" ARB Loophole.*

#### Definitions and Scope

(a) **Law/Fact Boundary.** For purposes of Section 7(j) and Section 7(k), and for all proceedings before the Allocation Review Board: [v1]

(1) A "purely factual determination" is a finding that resolves an empirical question without determining the scope, existence, or boundary of a governmental power. Purely factual determinations include: population counts, geographic measurements, economic data, revenue calculations, statistical measurements, and similar empirical findings whose resolution does not depend on the meaning or reach of a constitutional provision. [v1]

(2) A "mixed question of law and fact" is any determination in which the resolution of an empirical question is determinative of a constitutional boundary, power allocation, or the scope of governmental authority. A determination is "constitutionally determinative" if it directly establishes, denies, expands, or contracts a governmental power, or if the factual conclusion can only be reached by implicitly applying a legal standard to the facts. [v1]

(3) The following categories of findings are presumptively mixed questions of law and fact: [v1]

- (i) whether a Region possesses "administrative capacity" to exercise a contested power;
- (ii) whether "historical practice" supports or negates a claimed governmental authority;
- (iii) whether two governmental functions are "functionally equivalent" for allocation purposes;
- (iv) whether spillover effects are "sufficient to trigger concurrent jurisdiction" under Article II, Section 3;
- (v) whether a "regional interest" is "sufficiently distinct" to support exclusive Regional authority;
- (vi) whether federal action constitutes a "legitimate exercise" of an enumerated power, where that determination depends on disputed empirical predicates regarding the action's effects, scope, or reach. [v2: S5 — narrowed to require empirical predicate]

(4) A "pure question of constitutional interpretation" is a question that turns entirely on the meaning, scope, or application of constitutional text without reference to disputed empirical facts. [v1]

#### Standard of Review

(b) **De Novo Review for Mixed Questions.** Notwithstanding Section 7(j)(3) and Section 7(k): [v1]

(1) Mixed questions of law and fact shall be subject to de novo review by the Supreme Court upon appeal. [v1]

(2) The Supreme Court shall independently determine whether a determination constitutes a purely factual determination, a mixed question, or a pure question of constitutional interpretation. [v1]

(3) The prohibition on reweighing factual evidence in Section 7(j)(3) applies only to purely factual determinations as defined in subsection (a)(1). The Supreme Court may examine the factual components of a mixed question to the extent necessary to resolve the constitutional question embedded within it. [v1]

(4) The finality of factual determinations under Section 7(k) applies only to purely factual determinations; mixed questions remain subject to appellate review regardless of their factual content. [v1]

#### ARB Characterization Obligation

(c) **Mandatory Identification.** In every determination: [v1]

(1) The ARB shall explicitly identify each finding as either: (i) a purely factual determination, (ii) a mixed question of law and fact, or (iii) a pure question of constitutional interpretation. [v1]

(2) For each finding identified as a purely factual determination, the ARB shall state in writing why the finding does not determine a constitutional boundary, power allocation, or scope of governmental authority. [v1]

(3) Failure to identify the nature of a finding creates a rebuttable presumption that the finding is a mixed question of law and fact subject to de novo review under subsection (b). [v1]

(4) The ARB may not embed constitutionally determinative conclusions within findings labeled as purely factual. A finding that is labeled "purely factual" but whose substance determines a constitutional boundary shall be treated as a mixed question regardless of its label. [v1]

(5) The Adversarial Review Office, in its Adversarial Report under Section 7(u), shall include a specific assessment of whether each finding in the determination is properly characterized as to its law/fact nature. [v1]

#### Challenge Procedure

(d) **Characterization Challenges.** [v1]

(1) Any party to an ARB proceeding may challenge the ARB's characterization of a finding within fourteen (14) days of the later of: (i) the determination's issuance, or (ii) the Adversarial Review Office's issuance of its Adversarial Report under Section 7(v); provided that the challenge window shall open no later than forty-five (45) days after the determination's issuance regardless of whether the ARO has issued its report. [v3: S9 — added 45-day outer limit to prevent ARO delay as finality lever]

(2) Characterization challenges shall be filed directly with the Supreme Court and resolved on an expedited basis, with decision within thirty (30) days of filing. [v1]

(3) If the Supreme Court determines that one or more findings were improperly characterized as "purely factual," all constitutionally determinative findings in the determination shall be subject to de novo review. The Supreme Court may review the entire determination to the extent that improperly characterized findings affected the outcome. [v1]

(4) The Supreme Court, not the ARB, is the final arbiter of whether a finding is constitutionally determinative. The ARB's characterization of its own findings is entitled to no deference. [v1]

(5) A characterization challenge under this subsection, whether successful or unsuccessful, does not constitute the "one appeal" under Section 7(o). All parties retain the right to appeal the merits of the determination on constitutional interpretation grounds regardless of the outcome of any characterization challenge. [v2: S2 — clarified all parties retain merits appeal regardless of challenge outcome]

(6) No party that files or succeeds in a characterization challenge shall be subjected to adverse treatment by the ARB in any subsequent proceeding. The ARB may not consider a party's prior characterization challenges when making determinations, assigning priority, or exercising discretion. Alleged violations shall be referred to the Judicial Conduct Board and, if substantiated, constitute grounds for removal for cause under Section 7(e). [v3: OQ-4 resolved — explicit anti-retaliation; closes GV-9]

#### Anti-Gaming Provisions

(e) **Systematic Mischaracterization.** [v1]

(1) A "Characterization Pattern Finding" is established when the Supreme Court reclassifies three (3) or more ARB findings from "purely factual" to "mixed question" within any rolling two-year period. [v1]

(2) Upon a Characterization Pattern Finding, the Judicial Conduct Board and the Adversarial Review Office shall be notified. The ARO shall conduct an investigation into whether the pattern reflects systematic evasion of judicial review. [v1]

(3) During the twelve (12) months following a Characterization Pattern Finding, all findings by the ARB that are challenged carry a rebuttable presumption of mixed-question status. The ARB bears the burden of demonstrating that a challenged finding is purely factual. [v1]

(4) No member of the ARB who participated in a determination containing an improperly characterized finding may participate in the ARB's application of the Supreme Court's interpretation under Section 7(n)(3) for that determination. [v1]

(5) An ARB member who engages in a deliberate pattern of mischaracterization, as determined by the Judicial Conduct Board, is subject to removal for cause under Section 7(e). [v1]

(6) If recusals under subsection (e)(4) reduce the number of eligible ARB members below quorum for application of the Supreme Court's interpretation under Section 7(n)(3), the Chief Justice shall, within seven (7) days, appoint temporary members from among retired federal and state appellate judges who have never held partisan elected office. The Chief Justice shall select from a standing list maintained by the Judicial Conference for this purpose. Temporary members serve only for the specific application proceeding, have no authority over other ARB matters, and their appointment terminates automatically upon completion of the application. [v3: S7 — self-contained appointment procedure with 7-day deadline; removed §7(f) cross-reference]

#### Coordination

(f) **Relationship to Other Provisions.** [v1]

(1) This section supplements Section 7(j) through (o). Where Section 7(j) and (k) reference "factual matters" or "factual evidence," those terms refer to purely factual determinations as defined in subsection (a)(1). [v1]

(2) The No Factual Remand provision of Section 7(m) does not apply to mixed questions. When the Supreme Court determines that a finding is a mixed question and reverses the ARB's constitutional interpretation, the Court shall specify the correct interpretation under Section 7(n)(2), and the ARB shall apply it to the existing factual record under Section 7(n)(3). Where the existing factual record is insufficient to apply the correct interpretation due to the ARB's prior mischaracterization of one or more findings, the Supreme Court may direct the ARB to make additional purely factual findings limited to the matters necessary for application; this exception does not authorize general factual remand or reopening of the evidentiary record beyond what the mischaracterization made necessary. Additional findings directed under this provision shall be based solely on the existing evidentiary record — no new evidence may be introduced — and shall be completed within thirty (30) days of the Supreme Court's direction. [v3: S8 — added no-new-evidence rule and 30-day completion deadline]

(3) The Factual Finding Limitation of Section 7-A(g) applies independently. A finding may satisfy Section 7-A(g)'s transparency requirements while still constituting a mixed question subject to this section. The two provisions address distinct vulnerabilities: Section 7-A(g) ensures data and methodological transparency; this section ensures constitutional questions are not hidden within factual packaging. [v1]

(4) The de novo review standard established by Section 7(aa)(2) for bias-tainted determinations is independent of and cumulative with the de novo review standard for mixed questions established by this section. A determination may be subject to de novo review under both provisions simultaneously. [v1]

(5) The De Novo Review Mandate of Article XIV, Section 9 establishes the general principle that courts decide all questions of law de novo. This section applies that principle specifically to the ARB context, where the general mandate's preservation of "factual deference" (Article XIV, Section 9(c)) would otherwise leave the law/fact boundary undefined for power-allocation determinations. [v1]

(6) Nothing in this section alters the Parallel Filing Prevention provisions of Section 7(p)-(q). Characterization challenges under subsection (d) are procedural motions within the appellate process, not parallel filings. [v1]

(7) The expedited timeline of Section 7(r) is tolled during the pendency of a characterization challenge filed under subsection (d). The tolling period begins on the date the challenge is filed and ends on the date the Supreme Court issues its characterization decision. Upon resolution, the remaining time under Section 7(r) resumes. This tolling does not affect the thirty (30) day deadline for Supreme Court decision on the characterization challenge itself. [v3: S6 — §7(r) tolling prevents timing conflict between characterization challenge and global 120-day deadline]

---

## Gaming Vectors

| # | Vector | Attack | Mitigation |
|---|--------|--------|------------|
| 1 | **Micro-Finding Granularity** | ARB decomposes a constitutional conclusion into dozens of individually "factual" sub-findings, each too small to appear constitutionally determinative in isolation | §7-B(c)(4): substance-over-label rule — findings labeled "purely factual" but whose substance determines a constitutional boundary are treated as mixed questions regardless of label; ARO adversarial report (c)(5) reviews characterization of each finding |
| 2 | **Characterization Flooding** | Parties file frivolous characterization challenges to overwhelm the Supreme Court's 30-day expedited timeline | §7-B(d)(2): 30-day deadline creates institutional pressure for efficiency; existing SC authority to sanction frivolous filings applies; 14-day filing window limits volume |
| 3 | **Label-Switching After Determination** | ARB retroactively reclassifies findings to avoid Characterization Pattern Finding threshold | §7-B(e)(1): pattern measured by SC reclassifications, not ARB self-assessment; ARB labels at time of determination control |
| 4 | **Strategic Self-Labeling** | ARB labels everything as "mixed question" to eliminate its own factual finality advantage, flooding the SC with de novo reviews and causing institutional paralysis | §7-B(a)(1): clear definition of "purely factual" with examples (population counts, geographic measurements, economic data); SC independently determines characterization (b)(2), so can reject false self-labeling |
| 5 | **Opacity Through Volume** | ARB issues voluminous determinations with hundreds of findings to make characterization review impractical | §7-B(c)(5): ARO adversarial report includes characterization assessment for each finding, providing institutional counter-party with resources to identify mischaracterization |
| 6 | **Silent Characterization** | ARB omits characterization labels entirely, forcing challengers to identify each finding's nature | §7-B(c)(3): failure to identify nature creates rebuttable presumption of mixed-question status, incentivizing the ARB to label its findings |
| 7 | **Delayed Challenge** | Party waits until characterization challenge deadline expires, then raises characterization issue in merits appeal | §7-B(d)(1): 14-day window from later of determination or ARO report; §7-B(d)(5) preserves the merits appeal right for all parties, so characterization issues that emerge during merits briefing may still be raised (SC independently determines under (b)(2)) |
| 8 | **Member Rotation** | ARB members cycle off before Characterization Pattern Finding accumulates against them | §7-B(e)(1): pattern measured at institutional level (findings reclassified), not individual level; (e)(4) and (e)(5) address individual accountability for participating members |
| 9 | **Retaliation Against Challengers** | ARB retaliates against parties who successfully challenge characterizations in future proceedings | §7-B(d)(6): explicit anti-retaliation prohibition; ARB may not consider prior challenges in subsequent proceedings; violations referred to Judicial Conduct Board with removal-for-cause consequence |
| 11 | **Recusal-Induced Paralysis** | Coordinated mischaracterization followed by mass recusal to prevent §7(n)(3) application | §7-B(e)(6): Chief Justice appoints temporary members from retired appellate judge pool; temporary members serve only for specific application proceeding |
| 10 | **Presumptive Categories Gaming** | ARB avoids using words in the §7-B(a)(3) presumptive list (e.g., uses "operational readiness" instead of "administrative capacity") | §7-B(a)(2): general definition applies regardless of terminology — any determination where factual resolution is "determinative of a constitutional boundary" qualifies; presumptive list is illustrative, not exhaustive |
| 12 | **ARO Delay as Finality Lever** | ARO delays its Adversarial Report to postpone the challenge window opening, preventing timely characterization challenges | §7-B(d)(1): 45-day outer limit — challenge window opens no later than 45 days after determination issuance regardless of ARO report status |
| 13 | **Timing Squeeze** | Party files characterization challenge near end of §7(r) 120-day window, forcing SC to resolve under conflicting deadlines | §7-B(f)(7): §7(r) tolled during pendency of characterization challenge; 30-day SC deadline for challenge decision is independent of §7(r) tolling |

---

## Design Decisions

| # | Decision | Rationale |
|---|----------|-----------|
| DD-1 | **Placed as Section 7-B** | Follows Section 7-A (Algorithmic Governance Transparency) pattern; supplements §7(j)-(o) without modifying their text; self-contained section with clear cross-references |
| DD-2 | **Three-category taxonomy** (purely factual / mixed question / pure constitutional interpretation) | Maps to established legal doctrine (*Pullman-Standard*, *Ornelas v. United States*); provides clear definitions for each category; avoids ambiguous two-way classification |
| DD-3 | **Presumptive mixed question categories** (administrative capacity, historical practice, functional equivalence, spillover effects, regional interest, legitimate exercise) | These are the most common vehicles for disguising constitutional conclusions as factual findings; presumption is rebuttable, not conclusive; list is illustrative to prevent terminological evasion (GV-10) |
| DD-4 | **De novo review for mixed questions** (not intermediate standard) | Clear error or substantial evidence standards would still leave substantial room for characterization gaming; de novo is consistent with the De Novo Review Mandate (Art XIV §9(a)) general principle; mixed questions by definition contain constitutional content requiring judicial independence |
| DD-5 | **ARB characterization obligation with rebuttable presumption** | Forces ARB to affirmatively identify findings' nature; presumption incentivizes labeling; rebuttable (not conclusive) preserves ARB ability to demonstrate genuine factual findings |
| DD-6 | **Substance-over-label rule** (c)(4) | Prevents micro-finding granularity gaming (GV-1); ARB cannot disguise constitutional conclusions by labeling them differently; mirrors tax law "substance over form" doctrine |
| DD-7 | **14-day challenge window from later of determination or ARO report** | Short enough to maintain expedited timeline (§7(r): 120 days total); long enough for parties to analyze characterizations; ARO alignment gives parties the characterization assessment before the window opens; mandatory but not exclusive (SC can independently determine under (b)(2)) |
| DD-8 | **SC as final arbiter of characterization** (d)(4) | Prevents ARB self-insulation; consistent with separation of powers; the body whose review is being defined cannot control the scope of that review |
| DD-9 | **Characterization challenge distinct from one-appeal limit** (d)(5) | Characterization is a procedural/threshold question, not a merits appeal; forcing parties to "spend" their one appeal on characterization would chill challenges |
| DD-10 | **Characterization Pattern Finding at 3+ reclassifications within 2 years** | Bright-line trigger avoids discretion in identifying patterns; 3 is high enough to filter random disagreements; 2-year rolling window prevents slow-drip evasion |
| DD-11 | **ARO mandate to assess characterization** (c)(5) | Leverages existing institutional adversary; ARO already reviews all major determinations (§7(u)); adding characterization assessment is incremental, not structural |
| DD-12 | **Limited exception to No Factual Remand tied to ARB error** (f)(2) | §7(m) prevents remand for "further factual findings," but mixed-question reversal may require additional purely factual findings to apply the correct interpretation; exception is narrow (limited to matters made necessary by the ARB's mischaracterization); prevents parties from using mixed-question classification as backdoor to general factual remand |
| DD-13 | **"Legitimate exercise" presumption narrowed to empirical predicates** (a)(3)(vi) | Pure legal questions (does the text of the enumerated power reach this action?) should not carry mixed-question presumption; presumption applies only when the determination depends on disputed empirical predicates about the action's effects, scope, or reach |
| DD-14 | **Merits appeal preserved for all parties regardless of challenge outcome** (d)(5) | Prevents chilling effect where parties avoid characterization challenges for fear of "spending" their merits appeal; characterization is procedural/threshold, distinct from the substantive appeal |
| DD-15 | **Challenge window aligned with ARO report** (d)(1) | Parties receive the ARO's characterization assessment before the challenge window opens; reduces protective/premature challenges; aligns with §7(v) which already prevents determinations from taking effect before ARO completion |
| DD-16 | **Recusal quorum protection via self-contained Chief Justice appointment** (e)(6) | Prevents recusal-induced paralysis (GV-11); 7-day appointment deadline; Judicial Conference standing list; temporary members limited to specific application proceeding; self-contained procedure avoids dangling §7(f) cross-reference |
| DD-17 | **§7(r) tolling during characterization challenges** (f)(7) | Prevents timing conflict between characterization challenge path and 120-day global deadline (GV-13); tolling is limited to SC characterization decision period; 30-day SC deadline operates independently to prevent indefinite tolling |
| DD-18 | **No-new-evidence rule for directed additional findings** (f)(2) | Prevents §7-B(f)(2) from becoming a backdoor to general factual remand; additional findings must use existing evidentiary record only; 30-day completion deadline prevents indefinite reopening |
| DD-19 | **45-day outer limit on challenge window** (d)(1) | Prevents ARO delay as finality lever (GV-12); preserves ARO alignment for normal cases (ARO typically reports well within 45 days under §7(v)); ensures challenge window opens even if ARO is delayed |
| DD-20 | **Anti-retaliation with Judicial Conduct Board referral** (d)(6) | Closes GV-9; explicit prohibition on considering prior challenges; Judicial Conduct Board referral provides enforcement mechanism; removal-for-cause consequence creates deterrent proportional to severity |
| DD-21 | **Presumptive categories are illustrative** (a)(3) | Resolves OQ-1 — illustrative approach confirmed; exhaustive list risks terminological evasion; general definition in (a)(2) captures all variations regardless of vocabulary |

---

## Open Questions

| # | Question | Options | Implication |
|---|----------|---------|-------------|
| OQ-2 | Should there be a materiality threshold for the Characterization Pattern Finding? | A: Any 3 reclassifications trigger (current draft); B: Only reclassifications that affected the outcome count; C: Only reclassifications where the ARB's characterization was "clearly unreasonable" count | Lower threshold provides stronger deterrent; higher threshold reduces false positives |
| OQ-3 | Should challenging parties face any threshold requirement (e.g., bond, threshold showing) before filing a characterization challenge? | A: No threshold (current draft); B: Require "colorable claim" showing; C: Require bond forfeited if challenge fails | No threshold maximizes access; bond/threshold requirements may deter legitimate challenges |

---

## Changelog

- **v1**: Initial draft. 6 subsections (a)-(f) in new Section 7-B. 10 gaming vectors, 12 design decisions, 5 open questions.
- **v2**: Round 1 review (2 reviewers, 5 findings: 0 convergent, 0 complementary, 0 contradictions, 5 single-reviewer accepted). S1 (HIGH): recusal quorum protection via Chief Justice temporary appointment (e)(6). S2 (MEDIUM): clarified all parties retain merits appeal regardless of challenge outcome (d)(5). S3 (MEDIUM): challenge window aligned with ARO report issuance (d)(1); resolves OQ-5. S4 (MEDIUM): tightened factual remand gate to require ARB mischaracterization as predicate (f)(2). S5 (LOW): narrowed "legitimate exercise" presumption to require disputed empirical predicates (a)(3)(vi). 11 gaming vectors (+1), 16 design decisions (+4), 4 open questions (-1 resolved).
- **v3 (FINAL)**: Round 2 review (2 reviewers, 4 findings: 0 convergent, 0 complementary, 0 contradictions, 4 single-reviewer accepted + 2 OQ resolutions). S6 (HIGH): §7(r) tolling during characterization challenge pendency (f)(7). S7 (MEDIUM): self-contained temporary appointment procedure with 7-day deadline and Judicial Conference standing list (e)(6); removed dangling §7(f) cross-reference. S8 (MEDIUM): no-new-evidence rule and 30-day completion deadline for directed additional findings (f)(2). S9 (LOW): 45-day outer limit on challenge window opening regardless of ARO report status (d)(1). OQ-1 resolved: illustrative (confirmed, DD-21). OQ-4 resolved: explicit anti-retaliation with Judicial Conduct Board referral (d)(6); closes GV-9. 13 gaming vectors (+2), 21 design decisions (+5), 2 open questions (-2 resolved).
