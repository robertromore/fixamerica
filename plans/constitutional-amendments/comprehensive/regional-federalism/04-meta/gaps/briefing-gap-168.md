# Briefing: Gap 168 — The Acting Official Loophole (Bypassing Confirmation)

**Prepared for:** External reviewer (Step 2 of Multi-LLM Gap Resolution Protocol)
**Date:** 2026-02-02
**Gap severity:** High
**Source file:** `04-meta/gaps/11-institutional-governance.md`, line 2527

---

## 1. Problem Statement

The Constitution empowers specific offices to exercise critical constitutional powers: the Regional Governor commands Guard forces (Art XI-RF §2(d)) and declares emergencies (Art XVII-RF §1); the IFC certifies equalization formulas (Art X §6); the ARB resolves power-allocation disputes (Art II §7). However, no provisions address officials serving in "Acting," "Interim," or temporary capacity. An unconfirmed acting official can exercise full constitutional powers indefinitely, circumventing the entire checks-and-balances system.

The attack vector: (1) President or Region refuses to nominate a permanent official to avoid a confirmation battle; (2) an "Acting Director" or "Acting Governor" is appointed through informal channels; (3) the acting official exercises full constitutional powers (Guard refusal, equalization certification, emergency declaration) without ever being vetted; (4) the appointing authority weaponizes the vacancy to install a partisan operative who could never survive confirmation.

The constitution already anticipated this gap. Article IV, Section 4-B(i) (Mandatory Confirmation Procedures) explicitly states: "The provisions of this section complement, and shall be construed in coordination with, any limitations on acting officials established elsewhere in this Constitution." **Those limitations were never written.** The cross-reference points to an empty slot.

## 2. Existing Provisions (Overlap ~20-25%, LOW)

### 2.1 Provisions that partially address the concern

| Provision | What it covers | What it misses |
|---|---|---|
| **Art IV §4-B** — Mandatory Confirmation Procedures | 90-day mandatory vote or deemed confirmed; recess appointments limited to genuine recesses >30 days; anti-gaming (withdrawal/re-nomination continues clock); §4-B(i) cross-references acting official limitations | **The referenced limitations don't exist.** The confirmation framework is complete; the acting official complement is the gap. |
| **Art II §7(f)** — ARB Vacancy Filling | "Vacancies shall be filled by the original appointing authority within ninety days. If not filled within ninety days, the Chief Justice shall make a temporary appointment from among retired appellate judges until the original authority acts." | **No time limit** on the temporary appointment. Chief Justice appointee could serve for years exercising power-allocation authority. |
| **Art XI-RF §2(e)** — Guard Refusal During Vacancy | "If the Regional Governor position is vacant or if the Governor has been removed by federal action, the refusal authority under subsection (d) shall be exercised by the acting Governor under Regional succession law, or if none, by the presiding officer of the Regional legislature." | **No time limit.** Acting Governor exercises Guard refusal indefinitely. No confirmation requirement for successor under Regional succession law. |
| **Art IV §5(c)** — Federal Receiver | President appoints Receiver "subject to Senate confirmation within thirty days (or deemed confirmed if the Senate fails to act)." | Receiver is deemed-confirmed, but the Receiver then appoints acting officials and temporary judges with **no time limits, no confirmation, no removal procedures** (§5(d)(2)-(3)). |

### 2.2 Provisions with NO vacancy-filling procedures

| Provision | Constitutional Powers | What's Missing |
|---|---|---|
| **Art X §6** — Independent Fiscal Council | Certifies equalization formulas, determines Small Region qualification, measures fiscal capacity, determines subsistence wage floors (Art II §4(h)(3)) | **No vacancy-filling procedure at all.** If an IFC member dies or resigns, there is no process. A depleted IFC could lose quorum, halting equalization certification. |
| **Art XVII-RF §1** — Regional Emergency Authority | Governor declares emergencies with category-specific powers | **No provision** for who exercises emergency powers if Governor position is vacant beyond succession law reference |

### 2.3 The §4-B(i) coordination gap

Article IV §4-B(i) reads: "Coordination with Acting Official Limitations. The provisions of this section complement, and shall be construed in coordination with, any limitations on acting officials established elsewhere in this Constitution."

This is the constitutional equivalent of a TODO comment. The drafters knew acting official limitations were needed, built the hook, and never filled it. The new provision must:

- Fulfill the §4-B(i) cross-reference
- Coordinate with the 90-day deemed confirmation timeline (§4-B(b))
- Address both federal and Regional acting officials
- Cover the IFC vacancy gap

## 3. Proposed Placement

### Primary option: Art IV §4-C (Acting Official Limitations)

- Art IV §4-B already contains confirmation procedures with the §4-B(i) cross-reference
- A new §4-C would be the natural complement — §4-B addresses confirmation, §4-C addresses what happens when confirmation doesn't occur
- §4-B(i) would then point to §4-C instead of an empty reference

### Alternative A: Art II §7-B (alongside ARB provisions)

- Pro: Close to the ARB vacancy provision it modifies
- Con: Too narrow — the acting official problem is system-wide, not ARB-specific

### Alternative B: New standalone Article (general governance)

- Pro: Visibility as a standalone provision
- Con: Unnecessary when §4-B(i) already created the hook in Art IV

### Alternative C: Distribute across affected articles (Art II §7, Art X §6, Art XI-RF §2, Art XVII-RF)

- Pro: Addresses each body's specific circumstances
- Con: Fragments a single principle across multiple locations; risks inconsistency

### Recommendation: Art IV §4-C — Acting Official Limitations

Fulfills the §4-B(i) hook. Establishes general principle (time limits, power restrictions, reset prohibition, mandatory nomination, enforcement) that applies to all constitutional offices, with specific provisions for IFC vacancy-filling. Cross-references Art XI-RF §2(e) for Regional Governor succession.

## 4. Design Questions

### D1. What time limit for acting officials exercising constitutional powers?

The proposal uses 120 days. Consider the interaction with §4-B's 90-day deemed confirmation:

- (A) **120 days** — as proposed; provides 30-day buffer after deemed confirmation kicks in
- (B) **90 days** — aligns with §4-B timeline; if deemed confirmation occurs at 90 days, acting period ends simultaneously
- (C) **180 days** — more generous; accounts for genuine confirmation difficulties
- (D) **Tiered**: 90 days for "critical" constitutional powers (Guard, emergency, equalization); 180 days for other constitutional offices

### D2. Where should the provision be placed?

- (A) **Art IV §4-C** — next to §4-B confirmation procedures; fulfills §4-B(i) cross-reference
- (B) **Art II §7-B** — alongside ARB provisions
- (C) **Standalone section** in a general governance article
- (D) **Distributed** across Art II §7, Art X §6, Art XI-RF, Art XVII-RF

### D3. What happens when the time limit expires and no confirmed officer exists?

The proposal uses a panel of three confirmed officers selected by the Chief Justice. Options:

- (A) **Panel mechanism** — as proposed; three confirmed officers from other Regions (Regional) or agencies (federal), selected by Chief Justice
- (B) **Next confirmed officer in succession** — power passes to the next person in the statutory line who HAS been confirmed; panel only as fallback
- (C) **Power suspended** — the constitutional power simply cannot be exercised until a confirmed officer is in place (creates urgency to confirm)
- (D) **Combination**: succession first (B), panel fallback if no confirmed officer exists (A), power suspension only for non-emergency powers (C)

### D4. Should the time limit apply to Regional acting officials (Governors, etc.) or only federal?

The proposal's scope is ambiguous. Options:

- (A) **Federal only** — Regional succession is a Regional constitution matter
- (B) **Both federal and Regional** — any official exercising constitutional powers under this Constitution is covered, regardless of level
- (C) **Federal for federal offices; mandate that Regional constitutions include equivalent provisions** — respects Regional autonomy while ensuring coverage
- (D) **Federal for federal offices; constitutional floor for Regional** — Regional acting officials may not exercise constitutional powers (Guard refusal, emergency declaration) beyond the time limit, but Regional constitutions may set stricter limits

### D5. Should the IFC vacancy gap be fixed here or separately?

Art X §6 has no vacancy-filling procedure at all. Options:

- (A) **Fix here** — add IFC vacancy-filling provision to §4-C, mirroring ARB §7(f) (90-day deadline, Chief Justice temporary appointment)
- (B) **Fix in Art X §6 directly** — amend the IFC section to add vacancy procedures
- (C) **Both** — §4-C establishes general acting official limits; Art X §6 amendment adds IFC-specific vacancy-filling
- (D) **Fix here with cross-reference** — §4-C adds general vacancy-filling mandate for all constitutional bodies, with specific provision for IFC

### D6. How should the "reset prohibition" work?

The proposal prohibits resetting the clock by re-designating the same person or appointing a different acting official. Options:

- (A) **As proposed** — clock runs from vacancy date; cannot be reset by any procedural manipulation
- (B) **Clock resets only upon genuine nomination** — submitting a nomination to the confirming body resets the clock (provides incentive to nominate)
- (C) **Clock resets upon Senate action** — Senate vote (confirmation or rejection) resets; mere nomination does not
- (D) **Clock runs from vacancy but tolls during active confirmation proceedings** — if a nominee is pending before the Senate, the clock pauses; it resumes if the nomination is withdrawn or rejected without replacement

### D7. What constitutes "constitutional powers" for the time limit?

The proposal defines constitutional powers as "powers specifically enumerated in this Constitution." Options:

- (A) **Enumerated list** — Guard refusal, emergency declaration, equalization certification, treaty approval, appointments to constitutional bodies, and any other power specifically granted to a named office by the Constitution
- (B) **Functional test** — any power whose exercise is required by or authorized by a specific constitutional provision
- (C) **All powers of the office** — acting officials may continue to exercise routine administrative powers but not constitutional powers
- (D) **Distinguish "critical" and "ordinary" constitutional powers** — critical powers (Guard, emergency, equalization) have shorter limit; ordinary constitutional duties continue

### D8. Should the mandatory nomination timeline coordinate with §4-B?

The proposal requires nomination within 60 days of vacancy, with reporting at 90 days. §4-B's 90-day confirmation clock starts upon nomination. Options:

- (A) **As proposed** — 60-day nomination requirement, 90-day reporting
- (B) **30-day nomination** — aggressive timeline; ensures §4-B's 90-day clock starts promptly
- (C) **45-day nomination with automatic consequences** — if no nomination within 45 days, acting official's constitutional powers are automatically suspended
- (D) **Coordinate with §4-B**: 60-day nomination; if nominated, §4-B's 90-day deemed confirmation runs; if not nominated by Day 60, acting official loses constitutional powers at Day 90 (regardless of whether §4-C's 120-day limit has been reached)

### D9. What about judicial vacancies and temporary judges?

Art IV §5(d)(3) allows Federal Receivers to appoint "temporary judges." The proposal doesn't specifically address judicial acting officials. Options:

- (A) **Include judicial vacancies** — temporary judges subject to same time limits; must be replaced by confirmed judges
- (B) **Exclude judicial vacancies** — judicial independence requires different treatment; judges shouldn't be subject to executive-branch-style time limits
- (C) **Include but with longer timeline** — 180 days for temporary judges (recognizing judicial confirmation is typically slower)
- (D) **Include with Article XIV cross-reference** — coordinate with judicial reform provisions for confirmation timelines

### D10. Should acting officials have restricted powers even within the time limit?

The proposal allows full constitutional powers for 120 days. Options:

- (A) **Full powers for the entire period** — acting official is fully empowered until the limit
- (B) **Full powers for 60 days; restricted powers for days 61-120** — after 60 days, acting official may only exercise emergency/time-sensitive constitutional powers
- (C) **Full powers but no irreversible actions** — acting officials may exercise constitutional powers but may not take actions that permanently bind (e.g., long-term equalization formula changes; Guard deployment commitments >30 days)
- (D) **Full powers with mandatory disclosure** — all exercises of constitutional power by acting officials are publicly reported within 24 hours

### D11. What enforcement mechanism?

The proposal provides judicial enforcement (petition for order requiring nomination or declaring actions void). Options:

- (A) **Judicial enforcement only** — as proposed; petition for order or void declaration
- (B) **Automatic invalidity** — actions taken after the time limit are void ab initio without need for court order
- (C) **Automatic suspension of powers + judicial enforcement** — powers automatically suspend at the limit; court orders available for contested cases
- (D) **Combination**: automatic suspension of constitutional powers at the limit (self-executing); any party with standing may petition for declaration that specific actions taken after the limit are void; mandatory nomination orders available

### D12. Should there be an emergency exception?

What if a genuine crisis occurs on Day 119 and no confirmed officer exists? Options:

- (A) **No exception** — the time limit is absolute; the panel/succession mechanism handles emergencies
- (B) **Emergency extension** — acting official may continue for up to 30 additional days upon certification of genuine emergency by the relevant court
- (C) **Emergency bypass with retroactive review** — acting official may act in genuine emergency; actions subject to ratification by confirmed successor within 60 days of confirmation
- (D) **Emergency only for enumerated powers** — Guard refusal and emergency declaration may continue in genuine emergency; other constitutional powers suspend on schedule

### D13. How should this interact with the new Art V §4-A (Regional Executive Transition Integrity)?

Art V §4-A restricts lame duck Governors. Gap 168 restricts acting officials. These could overlap if an acting Governor is serving during a transition period. Options:

- (A) **Both apply simultaneously** — the stricter restriction governs
- (B) **§4-A supersedes during transition** — if an acting Governor is serving during a defined Transition Period, §4-A restrictions apply (they are stricter); §4-C applies outside transition periods
- (C) **Cross-reference** — §4-C states: "This section applies in addition to the restrictions of Section 4-A. Where both apply, the more restrictive provision governs."

## 5. Gaming Vectors

### From the proposal (5)

| # | Vector | Mechanism |
|---|---|---|
| G1 | Permanent "Temporary" | President/Region never nominates; acting official serves indefinitely exercising full constitutional powers |
| G2 | Weaponized Vacancy | Appointing authority deliberately keeps office vacant to avoid confirmation oversight |
| G3 | Partisan Operative | Acting official chosen for partisan loyalty; could never survive confirmation; exercises constitutional powers without vetting |
| G4 | Confirmation Theater | Nominate an unconfirmable candidate; withdraw after 89 days; nominate another unconfirmable candidate; reset the clock |
| G5 | Shadow Governance | Multiple acting officials across multiple constitutional bodies; none confirmed; entire governance structure operates without democratic accountability |

### Additional gaming vectors (9)

| # | Vector | Mechanism |
|---|---|---|
| G6 | The "Revolving Door" | Appoint Acting Official A for 119 days; replace with Acting Official B on Day 120; B serves 119 days; replace with C; each individual serves within the limit but the office is permanently "acting" |
| G7 | The "Quorum Kill" | Deliberately deplete a multi-member body (IFC, ARB) below quorum through non-replacement; body cannot act; constitutional functions (equalization, power allocation) simply halt |
| G8 | The "Dual Hat" | Acting official simultaneously holds another confirmed position; claims constitutional powers derive from the confirmed position rather than the acting one; circumvents time limit |
| G9 | The "Delegation Dodge" | Acting official formally delegates constitutional powers to a subordinate before the time limit; subordinate exercises powers indefinitely; technically the acting official isn't exercising them |
| G10 | The "Recess Game" | Under §4-B(g), recess appointments expire at end of next Senate session. Coordinate pro forma sessions to prevent recess appointments while also blocking regular confirmation — vacancy persists |
| G11 | The "Chief Justice Capture" | Under ARB §7(f), Chief Justice makes temporary appointments. If the Chief Justice is politically aligned, temporary appointments become permanent partisan placements — no time limit applies |
| G12 | The "IFC Starvation" | No vacancy-filling procedure exists for IFC. Refuse to fill IFC vacancies; IFC loses quorum; equalization certifications halt; fiscal system breaks down without any constitutional violation |
| G13 | The "Emergency Extension" | Acting official declares emergency on Day 119; argues emergency powers cannot be interrupted; uses emergency as pretext to extend acting period indefinitely |
| G14 | The "Regional Succession Shield" | Under Regional succession law, an unelected/unconfirmed Lt. Governor becomes Acting Governor; exercises Guard refusal and emergency powers; Regional succession law provides no time limit or confirmation requirement |

## 6. Verification Questions

### V1. Does the new text fulfill the §4-B(i) cross-reference?

Art IV §4-B(i) says the confirmation procedures "complement, and shall be construed in coordination with, any limitations on acting officials established elsewhere in this Constitution." The new text must be the provision that §4-B(i) points to. It should explicitly cross-reference §4-B.

### V2. Does the new text close the "revolving door" gaming vector?

If the clock runs per-person rather than per-vacancy, the revolving door circumvention works. The new text must run the clock from the date the vacancy occurred, not from the date the acting official was appointed.

### V3. Does the new text address the IFC vacancy gap?

Art X §6 has no vacancy-filling procedure. The new text must either add one or mandate that all constitutional bodies have vacancy-filling procedures.

### V4. Does the new text address the "quorum kill" gaming vector?

If an appointing authority can deplete a multi-member body below quorum by refusing to fill vacancies, constitutional functions halt. The new text must provide fallback appointment mechanisms when the original appointing authority fails to act.

### V5. Does the new text coordinate with Art V §4-A?

The new acting official limits and the transition integrity provisions could overlap for acting Governors during transition periods. The new text must specify which provision governs and how they interact.

### V6. Does the new text address temporary judges appointed under §5(d)(3)?

Federal Receivers can appoint temporary judges with no time limits or confirmation requirements. The new text must either include judicial vacancies or explicitly address this gap.

---

## 7. Draft Text Direction

The amendment should:

1. **Create Art IV §4-C (Acting Official Limitations)** — fulfilling the §4-B(i) cross-reference, establishing general principles for all constitutional offices

2. **Establish a time limit** on acting officials exercising constitutional powers — coordinated with §4-B's 90-day deemed confirmation timeline (120 days provides 30-day buffer)

3. **Define the succession/panel mechanism** when the time limit expires — next confirmed officer in succession; panel of three confirmed officers (selected by Chief Justice) as fallback; power suspension for non-emergency powers as last resort

4. **Prohibit clock resets** — clock runs from vacancy date; re-designation, replacement acting officials, withdrawal/re-nomination do not reset; tolling only during active confirmation proceedings before the confirming body

5. **Mandate nomination timelines** — 60-day nomination deadline with automatic consequences; coordinate with §4-B's deemed confirmation

6. **Add IFC vacancy-filling** — mirror ARB §7(f) pattern (90-day deadline, Chief Justice temporary appointment from qualified professionals); ensure no constitutional body can be starved below quorum

7. **Address Regional acting officials** — constitutional floor: Regional acting officials may not exercise constitutional powers (Guard refusal, emergency declaration) beyond the time limit; Regional constitutions may set stricter limits

8. **Include anti-circumvention** — revolving door prohibition, delegation prohibition, dual-hat prohibition, quorum protection for multi-member bodies

9. **Provide enforcement** — automatic suspension of constitutional powers at the limit (self-executing); judicial petition for void declaration and mandatory nomination orders; standing for any member of the confirming body, any affected party, and the relevant oversight institution

10. **Cross-reference §4-A and §4-B** — acting official limits are "in addition to" transition integrity restrictions (§4-A) and confirmation procedures (§4-B); where multiple provisions apply, the most restrictive governs
