# MCF Editorial Review: Internal Consistency and Strategic Audit

**Date:** 2026-01-30

**Scope:** Cross-document consistency, status accuracy, authority conflicts, terminology alignment, strategic gaps, operational feasibility

**Status:** All 22 findings resolved. 11 design decisions implemented.

---

## Summary

Twenty-two findings identified across the framework, all resolved. Part I covers eight internal consistency issues. Part II covers seven strategic and operational concerns raised by external review. Part III covers three structural vulnerability findings from a second external review. Part IV covers three systemic dependency findings from a third external review, unified under the Operational Autarky Principle. Part V covers one criminal justice gap from a fourth external review. Eleven design decisions were made across Parts I-V.

| Section | Severity | Count | Status |
|---------|----------|-------|--------|
| Part I: Consistency | High | 3 | All resolved |
| Part I: Consistency | Medium | 3 | All resolved |
| Part I: Consistency | Low | 2 | All resolved |
| Part II: Strategic | High | 2 | All resolved |
| Part II: Strategic | Medium | 3 | All resolved |
| Part II: Strategic | Low | 2 | All resolved |
| Part III: Structural | High | 2 | All resolved |
| Part III: Structural | Medium | 1 | All resolved |
| Part IV: Systemic | Medium-High | 2 | All resolved |
| Part IV: Systemic | Medium | 1 | All resolved |
| Part V: Criminal Justice | Medium-High | 1 | All resolved |

---

## Part I: Internal Consistency Findings

### Finding 1 -- Status Labels Contradictory

**Severity:** High

**Problem:** README.md (line 191) claims "All documents are in Final Draft status, representing a complete framework ready for stakeholder review and refinement." Section-level overviews contradict this: Phase 0 overview (lines 46-54), Phase 1 overview (lines 69-79), and Phase 3 overview (lines 165-176) all mark core documents as "Draft." Multiple annexes across the JSVC charter (line 975) and phase transitions document (line 672) are explicitly "[To be developed]."

**Files:**

- `README.md` (line 191)
- `01-phase-0-institutions/00-overview.md` (lines 46-54)
- `02-phase-1-civic-membership/00-overview.md` (lines 69-79)
- `03-phase-3-voluntary-convergence/00-overview.md` (lines 165-176)
- `01-phase-0-institutions/02-jsvc-charter.md` (line 975)
- `08-operational-procedures/02-phase-transitions.md` (line 672)

**Recommendation:** Replace the README status section with language that reflects the actual state:

> Core framework documents are in **Draft** status. Section overviews are Complete. Annexes with operational detail (templates, calibration methodology, detailed procedures) remain to be developed. See individual section overviews for per-document status.

Alternatively, promote all documents to "Final Draft" in the section overviews if the body text is considered substantively complete. But the undeveloped annexes are non-trivial (metric calibration methodology, commissioner selection procedures, investigation SOPs), so calling the whole package "ready for stakeholder review" overstates readiness.

---

### Finding 2 -- Phase Transition Certification Authority Inconsistent

**Severity:** High

**Problem:** Three different descriptions of who certifies the Phase 0 to Phase 1 transition:

| Source | Says |
|--------|------|
| Phase 0 overview (line 40) | "verified by external guarantors" |
| Phase transitions document (lines 85-94) | JSVC is the certification authority |
| JSVC charter (lines 777-810) | JSVC certifies; does not decide |

The detailed documents (phase transitions + JSVC charter) are internally consistent: JSVC certifies, guarantors observe and verify data but do not certify. The Phase 0 overview is the outlier.

**Files:**

- `01-phase-0-institutions/00-overview.md` (line 40)
- `08-operational-procedures/02-phase-transitions.md` (lines 85-94)
- `01-phase-0-institutions/02-jsvc-charter.md` (lines 777-810)

**Recommendation:** Fix Phase 0 overview line 40 to align with the authoritative documents:

> The transition to Phase 1 occurs when Phase 0 success criteria are met and certified by the JSVC, with guarantor data verification and assessment review.

---

### Finding 3 -- De Facto Guarantor Veto Despite "No Veto" Language

**Severity:** High

**Problem:** The framework simultaneously claims:

- "Guarantors do NOT have veto power over certification itself" (02-phase-transitions.md, line 158)
- Phase 0 to 1 requires "Positive stability rating from all guarantors" (02-phase-transitions.md, line 209)
- Phase 2 to 3 requires "Guarantor formal endorsement (stronger than concurrence)" (02-phase-transitions.md, line 447)

A requirement for unanimous positive assessment is functionally indistinguishable from individual veto power. If one guarantor gives a negative stability rating, the criterion is not met and JSVC cannot certify the transition.

**Files:**

- `08-operational-procedures/02-phase-transitions.md` (lines 158, 209, 447)

**Design decision required.** See Open Question 1.

**Recommendation (pending decision):** If de facto veto is acceptable, stop calling it "no veto" and add accountability mechanisms for guarantors who withhold positive assessments. Suggested replacement for Section 2.4:

> Guarantor assessments are a substantive criterion, not a procedural veto. Guarantors do not vote on whether to certify; JSVC certifies. However, because a positive stability rating from all guarantors is a criterion for Phase 0 to 1, and formal endorsement is required for Phase 2 to 3, guarantors have effective blocking authority over these transitions. This is intentional: transitions that proceed without guarantor confidence lack the external credibility and enforcement capacity needed to succeed.
>
> To prevent abuse: A guarantor that withholds a positive assessment must publish its reasoning within 14 days. A pattern of unexplained negative assessments may trigger the guarantor coordination review process.

If de facto veto is not acceptable, the guarantor stability rating must be changed from a hard criterion to a weighted input (e.g., "JSVC considers guarantor assessments; negative assessments are documented but do not independently block certification").

---

### Finding 4 -- Referendum Sequencing Mismatch

**Severity:** Medium

**Problem:** Phase 3 overview (line 106) says "Phase 3 is the first phase requiring referendum approval." Phase 1 to 2 transition criteria (line 348) include a SAZ selection referendum with thresholds (>=50% participation, >=55% approval, >=30% approval in each community present).

These are genuinely different kinds of referenda:

| Dimension | SAZ site selection (Phase 1 to 2) | Phase 3 referendum |
|-----------|-----------------------------------|-------------------|
| Scope | Affected local communities only | All CMS holders framework-wide |
| Question | "Should this location become an SAZ?" | "Should MCF pursue political convergence?" |
| Consequence | One SAZ established | Framework political trajectory changes |
| Repeatable | Yes, for each SAZ site | No, framework-wide decision |

But the Phase 3 overview's claim is factually wrong if the SAZ site-selection vote counts as a referendum.

**Files:**

- `03-phase-3-voluntary-convergence/00-overview.md` (line 106)
- `08-operational-procedures/02-phase-transitions.md` (line 348)

**Recommendation:** Clarify the Phase 3 overview (line 106):

> Phase 3 is the first phase requiring a **framework-wide referendum** among all CMS holders on the political direction of MCF. (Phase 1 to 2 includes localized site-selection referenda for specific SAZ locations, which are community-level consent processes rather than framework-level political mandates.)

Add a label in the Phase 1 to 2 section (around line 348): "**SAZ site-selection referendum** (distinct from Phase 3 framework referendum)."

---

### Finding 5 -- Diaspora CMS Status Ambiguity

**Severity:** Medium

**Problem:** Two different models for diaspora participation coexist without reconciliation:

| Source | Status offered | Rights |
|--------|---------------|--------|
| CMS framework Section 2.9 (lines 351-383) | Full CMS with diaspora benefit limitations | Full CMS eligibility, limited by physical presence |
| Diaspora engagement framework Section 2.1 (lines 57-79) | CMS-D (distinct subtype) | Limited institutional access, observer-only governance, annual renewal with activity requirement |

The CMS framework says diaspora can get full CMS but certain benefits require physical presence. The diaspora engagement framework introduces a separate CMS-D status with structurally limited rights. These are different models, not different descriptions of the same thing.

**Files:**

- `02-phase-1-civic-membership/01-cms-framework.md` (lines 351-383)
- `07-economic-architecture/07-diaspora-engagement.md` (lines 57-79)

**Design decision required.** See Open Question 2.

**Recommendation (pending decision):** Make CMS-D the canonical diaspora status. In CMS framework Section 2.9, replace the current diaspora eligibility text with a pointer:

> Diaspora populations are eligible for CMS Diaspora Status (CMS-D), a subtype of CMS with rights and limitations specific to the diaspora context. See Diaspora Engagement Framework Section 2.1 for full CMS-D eligibility, benefits, and limitations.

In the diaspora engagement framework, add: "CMS-D is a formally defined subtype of CMS under the CMS Framework. CMS-D holders are CMS holders with diaspora-specific scope limitations."

---

### Finding 6 -- "No Mutual Agreement" Claim vs. Vetting Dependencies

**Severity:** Medium

**Problem:** Phase 1 overview (line 15) says Phase 1 "does not require...mutual governmental agreement." CMS vetting (lines 127-128) covers "Security service records (both parties, with appropriate access agreements)" with no fallback described for non-cooperation. The CMS Vetting Unit makes "independent determinations" (line 143), but the document does not describe what happens when party records are unavailable.

**Files:**

- `02-phase-1-civic-membership/00-overview.md` (line 15)
- `02-phase-1-civic-membership/01-cms-framework.md` (lines 127-128, 143)

**Recommendation:** Add a non-cooperation fallback provision to CMS framework Section 2.3 (around line 143):

> **Non-cooperation fallback:** Where a party declines to share security records, the Vetting Unit proceeds using available sources: international databases, open-source review, guarantor-provided intelligence, and the cooperating party's records. Non-availability of one party's records is documented but does not automatically disqualify applicants. The Vetting Unit may impose enhanced monitoring conditions for applicants whose background could not be fully verified due to party non-cooperation.

This preserves the "no mutual agreement required" design principle while honestly acknowledging the limitation.

---

### Finding 7 -- JSVC Authority Wording vs. Regression Mechanics

**Severity:** Low

**Problem:** JSVC charter Section 8.7 (line 939) says "JSVC's phase authority flows in one direction: certifying readiness to expand rights and participation, not suspending them." Lines 947-952 say JSVC may NOT "Suspend CRC rights / Halt civilian protections / Freeze CMS benefits / Close PCCs unilaterally." Phase regression procedures (lines 434-437) then suspend CMS benefits, confederal arbitration courts, and employment programs.

The intended distinction is that JSVC certifies a regression trigger; the regression process (automatic upon certification) suspends benefits. JSVC does not directly suspend anything. This is logically coherent but the wording obscures it.

**Files:**

- `01-phase-0-institutions/02-jsvc-charter.md` (lines 939, 947-952)
- `08-operational-procedures/03-phase-regression.md` (lines 434-437)

**Recommendation:** Add a clarifying sentence to JSVC charter Section 8.7 (around line 939):

> When JSVC certifies a regression trigger, the resulting benefit suspension is an automatic consequence of the regression protocol, not a JSVC order. JSVC certifies conditions; it does not direct operational changes.

---

### Finding 8 -- Directory Numbering Duplication

**Severity:** Low

**Problem:** Both Phase 2 and Phase 3 directories use the `03-` prefix: `03-phase-2-saz/` and `03-phase-3-voluntary-convergence/`. This can confuse ordering or automation tools.

**Files:**

- `README.md` (lines 71, 80)
- All cross-references to `03-phase-3-voluntary-convergence/`

**Recommendation:** Renumber to `04-phase-3-voluntary-convergence/`. This requires updating cross-references across the framework. Low priority but should be addressed to avoid confusion.

---

## Part II: Strategic and Operational Findings

*These findings were raised by external LLM review. Each has been assessed against the actual document content. Findings are included where they identify genuine gaps or under-specifications; findings that misread the framework or attack capabilities the framework does not claim are noted in the Rejected Findings section.*

### Finding 9 -- Physical Deployment Mechanism Under-Specified ("Day One" Paradox)

**Severity:** High

**Problem:** The UVB charter (01-uvb-charter.md) describes legal authority to operate without mutual consent: guarantor authorization, unilateral consent from either party, and international law basis (lines 29-47). It describes site access request procedures (lines 286-307) and consequences for access denial (lines 302-307). However, the charter does not address the prior question: how do UVB international personnel physically enter the mandate area if one party (most likely Israel) blocks entry at airports and border crossings?

The charter's access procedures assume UVB personnel are already in-country. Access denial consequences (documentation, guarantor diplomatic response) assume the framework is operational enough to document and report. But if Israel denies visas to UVB staff or blocks entry at Ben Gurion/Jordan River crossings, these mechanisms never activate.

The framework's design logic (begin with cooperating party's territory, scale from there) partially mitigates this: if the PA consents, UVB could deploy through Jordan crossings or Egypt/Rafah. But this entry-point dependency is not documented, and deployment through non-Israeli-controlled crossings has its own constraints (Gaza closure, Jordan crossing under Israeli security control).

**Files:**

- `01-phase-0-institutions/01-uvb-charter.md` (lines 29-47, 286-307)
- `00-introduction.md` (Framework Entry Point section)

**Recommendation:** Add a "Deployment Logistics" section to the UVB charter (or a new annex) that addresses:

1. **Primary entry routes** and fallbacks if one party blocks entry
2. **Guarantor facilitation** of personnel entry (diplomatic pressure, transit agreements)
3. **Minimum viable deployment** -- what the UVB can accomplish if confined to one party's territory
4. **Asymmetric start** -- explicit acknowledgment that UVB may initially operate on one side only, with entry to the other side as a later objective

This does not require solving the problem completely. It requires acknowledging the problem and specifying the framework's response to it.

---

### Finding 10 -- Relative Deprivation and the "Collaborator" Class Risk

**Severity:** High

**Problem:** The framework is aware of the collaborator/normalizer risk. The anti-intimidation architecture (03-anti-intimidation.md) explicitly addresses "Social pressure, economic retaliation, and violence against 'collaborators' or 'normalizers'" (line 16) and provides layered confidentiality, graduated response, and protection for vulnerable populations. The No Worse Off guarantee (05-no-worse-off-guarantee.md) distinguishes between absolute conditions (protected) and relative conditions (not guaranteed), and explicitly permits MCF-only benefits as incentive structure (lines 214-223).

However, the framework under-addresses the economic externality problem: as MCF grows, CMS holders get access to employment programs, commercial courts, credential portability, and (in Phase 2) SAZ residency and civic dividends. Non-participants retain what they had, but the MCF economy may pull talent, employers, and economic activity toward CMS-linked sectors. This creates relative deprivation even without absolute degradation.

The No Worse Off guarantee (Section 4.1, line 223) says: "MCF may create new programs available only to CMS holders -- this is the incentive structure, not a penalty for non-participation." This is technically defensible but politically vulnerable. If the best jobs, the functioning courts, and the quality housing are all MCF-linked, non-participation becomes an increasingly costly choice regardless of the guarantee's technical provisions.

This is the historical failure mode of the Village Leagues (1980s) -- though MCF's design is fundamentally different (voluntary, no proxy governance role, no security function for participants, individual protections). The framework should address the parallel explicitly rather than leaving it to critics.

**Files:**

- `02-phase-1-civic-membership/05-no-worse-off-guarantee.md` (lines 214-223)
- `02-phase-1-civic-membership/04-incentive-structure.md`
- `02-phase-1-civic-membership/03-anti-intimidation.md` (line 16)

**Design decision required.** See Open Question 4.

**Recommendation (pending decision):** Options include:

1. **Acknowledge and accept:** Add a section to No Worse Off that explicitly addresses relative deprivation, acknowledges it as a design tradeoff (incentives require differential benefits), and explains why MCF's structure differs from historical collaborator-class dynamics.
2. **Mitigate through community-level spillovers:** Design some MCF economic benefits to create positive externalities for non-participants (e.g., PCC infrastructure benefits all users; MCF-funded medical facilities serve non-CMS patients; employer participation in MCF improves workplace standards for all workers).
3. **National endowment framing:** A portion of MCF economic activity funds a community trust accessible regardless of CMS status, allowing participants to frame involvement as contributing to collective benefit.

Options 2 and 3 can be combined. Option 1 is the minimum.

---

### Finding 11 -- Jerusalem PCC Routing Gap

**Severity:** Medium

**Problem:** Jerusalem is explicitly excluded from MCF territorial governance (02-jerusalem.md). The exclusion is deliberate, well-reasoned, and includes an exception for transit ("Transit through Jerusalem (practical necessity)" at line 409). However, the PCC protocols (03-pcc-protocols.md) do not address the routing implications.

Jerusalem sits between the northern and southern West Bank. PCCs connecting Ramallah to Bethlehem, or any north-south West Bank corridor, must either traverse Jerusalem or bypass it. The existing Israeli bypass road network (Route 60, tunnel roads) provides physical alternatives, but the framework does not specify whether PCCs use these existing routes, require new infrastructure, or rely on Jerusalem transit exception.

The external review overstated this as a fatal flaw ("economic integration will fail"). The existing road network functions now, and the Jerusalem transit exception in the exclusion document covers passage. But the gap is real: the PCC protocols need to specify routing for north-south connections.

**Files:**

- `06-sensitive-issues/02-jerusalem.md` (lines 399-410)
- `01-phase-0-institutions/03-pcc-protocols.md`

**Recommendation:** Add a section to PCC protocols addressing Jerusalem bypass routing:

1. **Identify primary PCC routes** that connect northern and southern West Bank without entering excluded Jerusalem territory
2. **Specify transit corridor treatment** for cases where routing through Jerusalem municipal boundaries is the only practical option (leveraging the existing transit exception)
3. **Infrastructure investment requirements** if bypass routes require upgrades to meet PCC standards

---

### Finding 12 -- SAZ Authority Transfer Mechanism Under-Specified

**Severity:** Medium

**Problem:** The SAZ selection document (06-internal-saz-selection.md) details criteria, process, and consent requirements for choosing SAZ locations. The decision sequence is clear: council recommends, guarantors certify, parties consent, referendum confirms, formal agreement signed (lines 488-503). However, the document does not describe the physical authority transfer: Does the IDF withdraw from the SAZ area? Does the PA dissolve its local council? Who physically assumes security and administrative control? What happens if a local mayor refuses to cede authority?

The framework requires party consent for SAZ establishment (line 492-494), which implicitly means authority transfer terms would be negotiated as part of that consent. But the gap between "agreement signed" and "SAZ operational" is the most operationally dangerous transition moment, and it is not specified.

The SAZ legal framework and SAZ governance documents may address aspects of this, but the selection document -- which defines the end-to-end process -- jumps from referendum approval to implementation without describing the handover mechanics.

**Files:**

- `03-phase-2-saz/06-internal-saz-selection.md` (lines 488-503)
- `03-phase-2-saz/01-saz-legal-framework.md`
- `03-phase-2-saz/02-saz-governance.md`

**Recommendation:** Add a "Transition Implementation" section to the SAZ selection document (or to SAZ governance) covering:

1. **Authority transfer sequence** -- which functions transfer when, in what order
2. **Security transition** -- how existing security forces (IDF, PA security) hand off to SAZ security arrangements
3. **Administrative continuity** -- how municipal services continue during transition
4. **Recalcitrant officials** -- what happens if local officials refuse to cooperate (guarantor mediation, parallel governance structures, legal mechanisms)
5. **Timeline** -- phased transition with defined milestones

---

### Finding 13 -- CRC "Binding on National Courts" Language

**Severity:** Medium

**Problem:** The constitutional floor document (03-constitutional-floor.md) states that CRC operates "parallel to national constitutional law" (line 340) and uses a "more protective standard applies" conflict resolution (line 352). This design is sound. However, line 361 states: "CRC Review Panel interpretation of CRC provisions is binding on national courts."

This binding language is the sharpest legal conflict in the framework. The Israeli High Court of Justice (HCJ) asserts universal jurisdiction and would not accept that an external panel's interpretation is binding. No Israeli Basic Law provides for this subordination, and the Knesset is unlikely to legislate it.

The external review overstated this by claiming the CRC "supersedes local law" generally -- the framework actually uses a parallel/most-protective model. But line 361 specifically does claim binding authority over national courts, which requires either enabling legislation (which the framework doesn't discuss) or restructuring to advisory authority.

**Files:**

- `03-phase-2-saz/03-constitutional-floor.md` (lines 340-362)
- `03-phase-2-saz/01-saz-legal-framework.md`

**Recommendation:** Two options:

1. **Require enabling legislation:** Add explicit acknowledgment that CRC binding authority within SAZs requires enabling legislation from both parties as part of SAZ establishment consent. This is already implicitly required (party consent for SAZ includes legal framework), but should be stated explicitly.
2. **Restructure to advisory authority with practical supremacy:** Change "binding on national courts" to a model where CRC Review Panel opinions are authoritative within SAZ jurisdiction, national courts defer as a matter of comity (not binding authority), and guarantor enforcement provides the backstop if national courts override CRC protections. This avoids the constitutional confrontation while achieving the same practical result.

Option 2 is more realistic. Option 1 may be technically cleaner but politically harder to achieve.

---

### Finding 14 -- Spoiler Attribution in Post-Truth Environments

**Severity:** Low

**Problem:** The external review claimed that the spoiler response framework (04-spoiler-response.md) relies on "naming and shaming" that fails in post-truth environments. This mischaracterizes the framework's approach. The spoiler response protocols explicitly state that MCF does not try to "defeat" spoilers directly but instead "changes the cost-benefit equation" (line 30). The mechanism is documentation leading to guarantor action (financial measures, sanctions, security measures), not reputational costs alone (lines 43-44).

However, the critique has a residual point: the documentation-to-guarantor-action pipeline depends on guarantors acting on the documentation. If guarantors are politically paralyzed, undermined by their own domestic post-truth dynamics, or simply fatigued, MCF documentation becomes an archive rather than a trigger. This loops back to the guarantor commitment concern.

**Files:**

- `08-operational-procedures/04-spoiler-response.md` (lines 30-65)

**Recommendation:** Low priority. The framework's spoiler response design is coherent. Consider adding a sentence to the spoiler response document acknowledging that the pipeline's effectiveness depends on guarantor willingness to act, with a cross-reference to guarantor withdrawal procedures as the backstop.

---

### Finding 15 -- Guarantor Legal Exposure Gap

**Severity:** Low

**Problem:** The external review raised a valid operational concern: MCF officials and guarantor-state nationals working in the framework could face legal challenges in guarantor countries. Activists could sue MCF officials in US/EU courts for "supporting occupation" or "funding terrorism," or seek discovery of CMS data through foreign legal proceedings.

The framework does not address legal shielding for MCF personnel in guarantor jurisdictions. This is an operational risk that could impose significant costs (legal defense, staff reluctance to serve) without threatening the framework's existence.

**Files:**

- `04-guarantor-architecture/00-overview.md`
- `08-operational-procedures/12-personnel-standards.md`

**Recommendation:** Add a provision to the guarantor architecture requiring guarantor states to provide legal protections for MCF personnel and data within their jurisdictions, similar to protections afforded to international organization staff (e.g., UN immunity provisions). This could be addressed in guarantor coordination or as a personnel standards annex.

---

---

## Part III: Structural Vulnerability Findings

*These findings were raised by a second external review examining the interplay between Economic Architecture, Security Protocols, and Phase Transitions. Each has been assessed against actual document content.*

### Finding 16 -- Monetary Choke Point (ILS Clearing Dependency)

**Severity:** High

**Problem:** The MCF economic architecture mandates Israeli Shekel (ILS) as one of two mandatory-acceptance currencies (01-economic-integration.md Section 4.1) and operates a "corridor-based digital settlement layer" for multi-currency clearing (Section 4.2). The banking access protocols (Section 3) are extensive and well-designed: they prohibit blanket de-risking, category-based denial, and emergency freezes based on party authority requests (Sections 3.3-3.4).

However, these protections operate within the MCF banking system. They prevent MCF-licensed banks from discriminating. They do not address the structural dependency: ILS clearing requires interface with Bank of Israel payment infrastructure. If Israel severs that interface -- refusing to process MCF-related Shekel transactions through the national clearing system, or pressuring Israeli correspondent banks to de-risk MCF-licensed institutions under national security regulations -- ILS-denominated transactions within MCF domains would seize up regardless of MCF's internal rules.

The economic crisis response framework (06-economic-crisis-response.md) covers "Banking system failure" (Scenario E) and "Currency crisis" as scenarios, but frames them as market events or institutional failures, not as deliberate state-level clearing denial. The distinction matters: a bank failure triggers liquidity substitution; a sovereign clearing cutoff is a category of state-level interference that the economic architecture's internal protections cannot remedy on their own.

**Mitigating factors already in the framework:**

- USD is also mandatory acceptance, providing a non-Israeli-controlled currency for essential transactions
- The corridor settlement layer (Section 4.2) could theoretically process USD-only transactions
- MCF-licensed banks include "International banks" and "MCF-chartered financial institutions" (Section 3.8), not just Israeli banks
- Guarantor enforcement tools include financial sanctions against state-level spoilers (02-guarantor-roles.md Section 1)

**Files:**

- `07-economic-architecture/01-economic-integration.md` (Sections 3, 4)
- `04-guarantor-architecture/06-economic-crisis-response.md` (Section 8.1 Scenario E)
- `04-guarantor-architecture/02-guarantor-roles.md` (Sections 1, 4)

**Recommendation:** Add provisions addressing infrastructure-level financial resilience:

1. **Clearing redundancy:** Specify that the corridor settlement layer must be capable of operating in USD-only mode if ILS clearing is severed. Define minimum MCF operational capacity under USD-only settlement.
2. **Correspondent banking diversification:** Require MCF-licensed banks to maintain non-Israeli correspondent banking relationships for essential services.
3. **State-level clearing denial as a spoiler action:** Add this scenario to the spoiler response framework (04-spoiler-response.md, Section 2.2) and the economic crisis response (Scenario F or expansion of Scenario E). Specify guarantor response: diplomatic pressure, alternative clearing arrangements, and escalation to sanctions if systematic.
4. **Guarantor bridge banking:** Guarantor states commit to providing emergency clearing access through their own financial institutions if Israel severs MCF-related clearing.

**Design decision (resolved):** Implement a clearing-independent digital ledger (MCF Value Transfer Protocol). See Decision 5 below.

---

### Finding 17 -- Dual-Use Logistics Trap (Construction Material Supply Chain)

**Severity:** Medium

**Problem:** Israel historically classifies cement, steel rebar, and construction aggregates as dual-use materials subject to import restrictions in Palestinian territories (under security justifications related to tunnel construction and fortification). The MCF customs protocols (01-economic-integration.md Section 2) are designed to prevent exactly this kind of blocking: "presumptive permission" (Section 2.1), classification by MCF Corridor Authority (Section 2.2), time-limited inspections with mandatory release (Section 2.3), and prohibited inspection triggers including "Generalized security concerns" (Section 2.4).

Under the MCF classification system, construction materials would fall under Tier 1 ("Industrial inputs: Raw materials, components, machinery") with only documentation verification and random sampling required. MCF explicitly does not list cement or steel as Tier 2 dual-use.

The gap is pre-corridor: goods must enter the territory before they reach MCF corridors. The infrastructure coordination document (05-infrastructure-coordination.md) acknowledges the supply chain dependency: "No Palestinian deep-water port; Gaza port non-operational; Goods through Israeli ports; Dependency and delays." The same document states MCF "cannot override Israeli or Egyptian border controls." Israeli customs at ports of entry applies Israeli classification (which does list construction materials as dual-use or restricted), before goods ever reach MCF jurisdiction.

**Mitigating factors already in the framework:**

- MCF customs within corridors would fully protect construction material flows
- Presumptive permission principle directly counters dual-use over-classification
- MCF Corridor Authority (not national authorities) controls classification within MCF domains
- Infrastructure coordination identifies the dependency but doesn't claim to resolve it

**Files:**

- `07-economic-architecture/01-economic-integration.md` (Section 2)
- `07-economic-architecture/05-infrastructure-coordination.md` (Ports section, Gaza Transportation)

**Recommendation:**

1. **Port-to-corridor transition protocol:** Specify how goods transition from national customs jurisdiction (at ports) to MCF customs jurisdiction (in corridors). This is the critical handoff that currently has no documented procedure.
2. **Alternative supply routes:** Identify non-Israeli supply chain paths: Jordanian land crossings (King Hussein/Allenby Bridge), Egyptian crossings (for southern territory), and guarantor-facilitated direct imports. Prioritize these for construction materials during SAZ build-out.
3. **Pre-positioned material reserves:** Require MCF to maintain strategic reserves of key construction materials within MCF domains to buffer against supply disruption.
4. **Guarantor procurement channel:** Guarantor states procure and ship construction materials through their own logistics, bypassing Israeli port customs for MCF-designated projects. This leverages the guarantor architecture's existing facilitation obligations.

This is medium severity rather than high because the MCF internal protections are robust -- the vulnerability is at the boundary, and multiple alternative supply routes exist that the framework could formalize.

---

### Finding 18 -- Local vs. Central Veto (Sub-National SAZ Participation Blocking)

**Severity:** High

**Problem:** The SAZ establishment process requires party consent at two points: pre-referendum consent to allow the vote (06-internal-saz-selection.md Section 5.1, Step 3) and post-referendum formal agreement (Step 5). The SAZ Legal Framework (01-saz-legal-framework.md) provides multiple establishment paths (bilateral agreement, unilateral offer, guarantor facilitation, community petition), but all paths ultimately require party non-objection or consent.

The Community Petition Model (SAZ Legal Framework Section 2.4) includes a 90-day silence rule ("silence = non-objection after 90 days"), which is a partial mitigation. However, this is easily defeated: a central authority need only file an active objection within 90 days. The framework does not specify what happens when a community petition is actively blocked.

This creates a structural vulnerability: local communities may strongly support SAZ participation, but PA/Hamas (or the Israeli government) can block the process from even reaching a referendum. The framework's emphasis on local demand ("Site selection begins with demand, not with geographic logic" -- 06-internal-saz-selection.md Section 1) is undermined if central authorities can suppress that demand at the authorization stage.

Additionally, the framework provides no protection for local leaders who express SAZ interest. A Palestinian mayor who publicly supports SAZ could face dismissal by the PA, funding cuts, or worse. An Israeli settlement council leader who supports SAZ could face political ostracism. The anti-intimidation architecture (02-phase-1-civic-membership/03-anti-intimidation.md) protects CMS participants but does not extend to pre-SAZ political advocacy by local officials.

The spoiler response framework (04-spoiler-response.md Section 2.3) does cover "Internal Obstruction" including "Discouraging participation through unofficial channels" and "Bureaucratic harassment; social pressure." But this operates as documentation and escalation after the fact. It does not provide proactive protection or an override mechanism for the pre-referendum blocking scenario.

**Mitigating factors already in the framework:**

- Multiple establishment paths (not just bilateral)
- Community petition model with silence rule
- Guarantor facilitation for "deadlock scenarios" (SAZ Legal Framework Section 2.1)
- Spoiler response protocols cover internal obstruction
- Unilateral offer model allows one party to proceed without bilateral agreement

**Files:**

- `03-phase-2-saz/06-internal-saz-selection.md` (Section 5.1 Steps 3, 5)
- `03-phase-2-saz/01-saz-legal-framework.md` (Sections 2.1-2.4)
- `08-operational-procedures/04-spoiler-response.md` (Section 2.3)
- `02-phase-1-civic-membership/03-anti-intimidation.md`

**Recommendation:**

1. **Blocked-petition escalation pathway:** When a community petition meets thresholds (Section 2.4 requirements) and the central authority files an active objection, the matter escalates to the Guarantor Forum for mediation. If mediation fails within 120 days, guarantors may authorize the referendum to proceed under guarantor facilitation (Section 2.1), with the central authority's objection documented but not dispositive.
2. **Pre-SAZ advocacy protection:** Extend anti-intimidation protections to local officials and community leaders who publicly express interest in SAZ participation during the candidate generation and consultation phases. This requires expanding the anti-intimidation architecture's scope to cover pre-CMS political advocacy related to SAZ establishment.
3. **Anonymous interest signaling:** Create a mechanism for communities to signal SAZ interest to the MCF Secretariat without public exposure. The MCF Secretariat assesses demand through confidential surveys before any public process begins. This gives communities a way to demonstrate demand without requiring leaders to stick their necks out.
4. **Sub-national consent distinction:** Explicitly address the possibility that local authorities support SAZ while central authorities oppose. The framework should specify whether "party consent" means national government consent, or whether local government consent (backed by local referendum) can substitute when national authorities block without substantive grounds.

**Design decision (resolved):** Maintain central consent but apply conditionality of aid ("Non-Interference Conditionality"). See Decision 7 below.

---

### Rejected External Findings

The following findings from external review were assessed and determined to be misreadings of the framework, attacks on capabilities the framework does not claim, or strategic concerns already addressed:

**UVB drone operations / Iron Dome:** The external review claimed the UVB cannot "unilaterally fly drones" because they would be shot down. The UVB charter does not propose operating drones. "Unilateral" refers to governance structure (operating without mutual consent), not to surveillance methods. The UVB uses guarantor-provided satellite imagery (01-uvb-charter.md, line 68), field team deployment, witness interviews, and open-source monitoring (lines 270-284). This finding is based on a capability the framework does not claim.

**No Worse Off guarantee "technically impossible":** The external review claimed the guarantee cannot be kept "in economic terms." The framework explicitly addresses this: Section 4.1 (lines 214-223) distinguishes between protecting absolute conditions (what non-participants had before MCF) and not guaranteeing relative conditions (parity with MCF participants). The guarantee is not a promise of economic equality -- it is a promise that MCF existence will not reduce pre-existing access. The relative deprivation concern IS valid (see Finding 10) but the guarantee is not "technically impossible" as framed.

**Guarantor attention span / 50-year commitment:** This is a legitimate strategic risk but is already addressed in the framework. The guarantor architecture includes withdrawal procedures (05-guarantor-withdrawal.md), economic crisis response (06-economic-crisis-response.md), and the concrete scenarios include a guarantor reversal walkthrough (15-concrete-scenarios/06-guarantor-reversal.md). The framework's phase regression design explicitly anticipates guarantor withdrawal as a survivable event. This is a concern, not a gap.

**CRC "supersedes local law":** The external review claimed CRC is "legally incompatible with Israeli Basic Law" because it "supersedes local law in SAZs." The constitutional floor document (03-constitutional-floor.md) actually uses a parallel/most-protective model: "CRC operates parallel to national constitutional law, not in replacement of it" (line 340), "Israeli Basic Laws continue to apply to Israeli citizens within SAZ" (line 342), "More protective standard applies" (line 352). The specific binding-on-national-courts language at line 361 IS a genuine issue (see Finding 13), but the broader claim of CRC superseding local law mischaracterizes the framework's approach.

---

---

## Part IV: Systemic Dependency Findings

*These findings were raised by a third external review examining the physical and institutional infrastructure dependencies that could cause the framework to degrade gradually rather than fail acutely. These are not spoiler attack vectors but structural parasites -- slow-moving risks that could erode MCF viability over time. Each has been assessed against actual document content.*

### Finding 19 -- Spectrum Sovereignty Void (Telecom Physical Layer Dependency)

**Severity:** Medium-High

**Problem:** The MCF framework relies heavily on digital infrastructure for core operations: Digital CMS enrollment and benefit delivery, MVTP payment settlement (01-economic-integration.md Section 4.4), Digital Phase -1 engagement, PCC monitoring, and JSVC incident documentation. The data architecture (09-data-it-systems.md) is well-designed: the primary data center is in neutral territory (line 445), multiple ISP connections provide redundancy (line 461), and satellite backup exists for emergency communications (line 464).

The infrastructure coordination document (05-infrastructure-coordination.md) explicitly acknowledges the telecom dependency: Palestinian telecommunications suffer from "Limited spectrum access," "Infrastructure constraints," and "Dependency on Israeli connections" (lines 79-83). The framework prohibits "No jamming or interference with civilian communications" and "No communication shutoffs as coercion" (lines 105-107). Spectrum coordination facilitates technical discussions but explicitly states "MCF does not allocate spectrum" (line 123).

The gap is between prohibition and physical independence. Israel controls the physical telecom layer in the West Bank: frequency allocation, 4G/5G bandwidth, and fiber optic backbones. MCF's non-interference rules are enforceable as violations (triggering documentation, guarantor escalation, and spoiler response), but they do not provide an alternative pipe. If Israel throttles bandwidth to SAZ areas or denies frequency allocation for MCF secure communications, the "shutoff" prohibition may not even apply -- bandwidth degradation is not a binary shutoff. The satellite backup in the IT architecture is for MCF institutional emergency communications, not for mass CMS holder access to digital services. The MVTP, which was designed to survive a financial clearing severance, could itself be rendered inoperable by a telecom infrastructure severance.

**Mitigating factors already in the framework:**

- Primary data center hosted in neutral territory, not dependent on Israeli infrastructure
- Satellite backup for MCF institutional emergency communications
- Non-interference and non-weaponization rules documented with spoiler response escalation
- "Access denial" explicitly identified as a political risk in IT risk management (09-data-it-systems.md line 626)
- Multiple ISP connections and dedicated circuits specified
- Gaza telecom section addresses infrastructure protection and equipment import

**Files:**

- `08-operational-procedures/09-data-it-systems.md` (Infrastructure Requirements, Risk Management)
- `07-economic-architecture/05-infrastructure-coordination.md` (Telecommunications section, lines 67-165)

**Recommendation:**

1. **MCF Dedicated Connectivity:** Specify that MCF operational systems (MVTP settlement, CMS registry access, JSVC reporting) must have connectivity independent of commercial Israeli telecom. Options: guarantor-provided VSAT terminals at MCF institutional sites, dedicated microwave links between MCF facilities, or leased fiber on non-Israeli-controlled routes (e.g., through Jordan).
2. **Spectrum Lease Protocol:** Guarantors negotiate a dedicated frequency block for MCF operations, managed by the Infrastructure Coordination Unit, ensuring that MCF digital services have guaranteed bandwidth independent of Israeli commercial spectrum allocation decisions.
3. **Degradation-as-Interference:** Extend the non-interference prohibition to explicitly cover systematic bandwidth throttling and frequency denial, not just binary shutoffs. Define measurable connectivity thresholds below which degradation constitutes a spoiler action.
4. **Offline-Capable Design:** Specify that critical MCF systems (CMS verification, basic MVTP transactions) must be capable of operating in degraded-connectivity mode with local caching and periodic synchronization, so that telecom degradation slows but does not halt operations.

**Design decision (resolved):** Mandate Satellite-First Connectivity Architecture with LEO satellite as primary MCF institutional uplink. See Decision 8 below.

---

### Finding 20 -- Institutional Cannibalization Risk (Human Capital Drain)

**Severity:** Medium

**Problem:** The MCF creates employment conditions significantly better than the surrounding Palestinian economy. The MCF minimum wage is set at the higher of Israeli minimum wage, PA minimum wage, or $12/hour equivalent (02-labor-mobility.md line 212). MCF labor standards include comprehensive worker protections, dispute resolution, and social insurance (Sections 3-5). MCF-funded facilities (healthcare, education, training) operate at higher standards than PA equivalents.

The labor mobility framework restricts public sector employment to "MCF institutions only" in Phase 1 and "SAZ administration" in Phase 2 (02-labor-mobility.md Section 2.1, line 80). MCF does not directly recruit PA public servants for PA-equivalent roles. However, the market pressure effect is real: private employers operating under MCF conditions in corridors and SAZs offer better wages, protections, and working conditions than PA institutions. Skilled professionals -- doctors, engineers, teachers, administrators -- face a rational incentive to leave PA service for the private sector within MCF domains, not because MCF recruited them, but because the economic conditions are objectively better.

The Community Spillover Design (04-incentive-structure.md Section 10.2a, lines 625-659) ensures MCF healthcare facilities serve all patients, training centers serve non-CMS community members, and the Community Development Fund channels revenue back to communities. The No Worse Off guarantee (05-no-worse-off-guarantee.md) protects individual access to pre-existing services (Section 4.2). However, neither addresses institutional capacity: if PA hospitals lose their best doctors to better-paying MCF-area clinics, the guarantee that non-participants retain "same access as before MCF" to healthcare becomes hollow -- the hospital still exists, but the quality of care has degraded because the talent left.

**Mitigating factors already in the framework:**

- Public sector employment restricted to MCF institutions only (not PA substitution)
- Community Spillover Design ensures MCF facilities serve all residents
- Community Development Fund channels MCF revenue to non-CMS communities
- No Worse Off guarantee monitors non-participant conditions (Section 4.4)
- Phased approach limits exposure: full labor mobility develops gradually
- This dynamic already exists with UNRWA, World Bank, and international NGO employment in Palestine; it is not unique to MCF

**Files:**

- `07-economic-architecture/02-labor-mobility.md` (Sections 2.1, 3.1, 4.2)
- `02-phase-1-civic-membership/04-incentive-structure.md` (Section 10.2a)
- `02-phase-1-civic-membership/05-no-worse-off-guarantee.md` (Sections 4.1-4.4)

**Recommendation:**

1. **Institutional Impact Monitoring:** Add a monitoring obligation to the No Worse Off guarantee (Section 4.4) that tracks not just individual access to services but institutional capacity indicators: PA hospital staffing levels, school teacher-student ratios, and ministry vacancy rates in MCF operational areas. If institutional capacity degrades beyond a threshold, this triggers mitigation obligations.
2. **Human Capital Replacement Levy:** When MCF-registered employers hire workers who were employed in public sector institutions (PA, municipal government, UNRWA) within the preceding 12 months, the employer pays a one-time transition fee to the originating institution sufficient to fund recruitment and training of a replacement. This internalizes the externality rather than ignoring it.
3. **Rotation Secondments:** Create a structured secondment program where PA public sector workers can work in MCF-area facilities for fixed terms (6-12 months) and return to PA service with enhanced skills and a re-integration stipend. This converts permanent extraction into temporary capacity building.
4. **PA Institutional Support:** Guarantee states include PA institutional capacity maintenance in their development assistance obligations, ensuring that PA service delivery is supported as MCF economic conditions create wage differential pressure.

This is medium severity because the risk is gradual, partially mitigated by existing spillover design, moderated by the phased approach, and mirrors an existing dynamic in Palestinian development economics. The framework's exposure is limited in Phase 1 when MCF employment is restricted to registered employers within corridors.

**Resolved:** No structural change required. Human Capital Replacement Levy, Rotation Secondment Protocol, and Institutional Capacity Monitoring implemented. See Decision 10 below.

---

### Finding 21 -- Grid Monopoly Veto (Utility Connection Denial for New SAZ Sites)

**Severity:** Medium-High

**Problem:** The infrastructure coordination document (05-infrastructure-coordination.md) establishes robust protections for existing utility infrastructure: "Infrastructure shutoffs as economic coercion prohibited" (line 49), "Maintenance access guaranteed" (line 51), minimum reliability standards for electricity (line 369), and "Power infrastructure protected" (line 376). The water resources document (06-sensitive-issues/01-water-resources.md) classifies "Coercive supply cutoff affecting civilian population" as a high-severity violation (line 318) with guarantor escalation.

However, these protections are designed for shutoffs and degradation of existing service, not for refusal to establish new connections. In the West Bank, water supply is controlled by Mekorot (Israeli national water company) and electricity by the Israel Electric Corporation (IEC). These are statutory monopolies that function as state instruments. They frequently deny or delay connection requests for Palestinian development using "technical" justifications (grid capacity, master plan review, security zone restrictions) that are functionally political.

When a new SAZ is designated and construction begins, it needs water mains, electrical grid connections, and sewage infrastructure. If Mekorot refuses to lay a pipe or IEC refuses a grid connection -- citing "the distribution master plan is under review" or "grid capacity in this area is insufficient" -- the SAZ has no water or power. The framework's protection against shutoffs does not apply because there was never a connection to shut off. The infrastructure coordination document states "No prejudice to future development" for ports and airports (lines 279, 344) but does not apply this principle to utility self-generation. The water resources document explicitly defers infrastructure development to the political track (lines 255-258: "These require political agreements MCF cannot provide").

The economic model of the SAZ depends on functioning utilities. Relying on trucked water and diesel generators is not economically viable at scale and would undermine the SAZ's attractiveness as a living and working environment.

**Mitigating factors already in the framework:**

- Infrastructure shutoff prohibition covers existing connections
- Response ladder for utility-related violations (water resources, lines 340-348)
- Guarantor escalation for systematic denial of access
- Infrastructure Coordination Unit facilitates technical coordination (lines 519-533)
- Jordan Corridor (Finding 17 resolution) establishes precedent for alternative supply routes
- Guarantor funding architecture could finance independent infrastructure
- "No prejudice to future development" principle exists for other infrastructure categories

**Files:**

- `07-economic-architecture/05-infrastructure-coordination.md` (Utilities section, lines 361-403; Design Principles, lines 19-64)
- `06-sensitive-issues/01-water-resources.md` (Enforcement section, lines 312-348; Phased Approach, lines 262-309)

**Recommendation:**

1. **Connection Refusal as Interference:** Extend the infrastructure protection framework to explicitly cover refusal to establish new utility connections for MCF-designated sites. Define a timeline: if a utility provider does not provide a connection plan within 90 days of a formal MCF request, this constitutes obstruction subject to documentation and guarantor escalation.
2. **Independent Utility Provisioning Authority:** Grant SAZ governance the explicit right to develop independent power generation (solar, wind, battery storage) and independent water treatment (desalination, rainwater harvesting, recycled water) when the national grid provider refuses connection. This right should be specified in the SAZ Legal Framework, not just implied.
3. **Off-Grid Default Design:** Specify that SAZ site planning must include independent utility capacity as the default infrastructure design, not as a backup. Solar micro-grids and water treatment facilities should be part of baseline SAZ construction, with grid connection as a supplement rather than a dependency. This inverts the vulnerability: the SAZ is self-sufficient, and grid connection becomes a convenience rather than a chokepoint.
4. **Guarantor Utility Provisioning:** Guarantor states commit to providing utility infrastructure technology (solar panels, desalination units, water treatment systems) as part of SAZ construction support. This is a procurement obligation, not a political negotiation with Mekorot/IEC.

**Design decision (resolved):** Mandate Off-Grid Primary Design as default SAZ standard, eliminating the monopoly veto entirely. See Decision 9 below.

---

---

## Part V: Criminal Justice Gap

*This finding was raised by a fourth external review examining the interface between SAZ Security, Dispute Resolution, and SAZ Governance -- specifically the "Day 2" reality of inter-communal violence within operational SAZs.*

### Finding 22 -- Criminal Prosecution Gap and "Revolving Door" Impunity Risk

**Severity:** Medium-High

**Problem:** The external review identified a "Criminal Jurisdiction Void" in the SAZ framework. This characterization overclaims -- the framework IS NOT a void on criminal jurisdiction. SAZ Governance (02-saz-governance.md) defines criminal jurisdiction tiers: offenses with maximum penalty ≤2 years are tried by single judge, >2 to ≤10 years by 3-judge panel, and >10 years are reserved to national courts (Section 3.1, lines 465-471). The SAZ Legal Framework (01-saz-legal-framework.md Section 7.1) codifies this division, reserving national security offenses and serious criminal offenses to national courts. The forum assignment for serious offenses specifies: Israeli-origin defendants → Israeli courts, Palestinian-origin defendants → Palestinian courts (02-saz-governance.md, lines 626-634). And the "Serious Offense Coordination" section specifies SAZ police investigate, transfer case files to national prosecutors, with JSVC monitoring (lines 635-641).

However, three genuine gaps exist within this structure:

**Gap 1: No SAZ Prosecution Office.** SAZ courts have defined criminal jurisdiction for offenses ≤10 years, but no prosecutor or prosecution office is described. Who brings criminal charges? Who represents the public interest? Courts without prosecutors do not function.

**Gap 2: No Applicable Criminal Law Specified.** The choice-of-law hierarchy (Section 3.2) covers civil matters. For criminal cases in SAZ courts, the document does not specify which penal code applies. If an Israeli and a Palestinian are both SAZ residents and one assaults the other, which criminal code does the SAZ court apply?

**Gap 3: The "Revolving Door" -- No Accountability for National Court Failures.** This is the critical gap. For serious offenses (>10 years) transferred to national courts, the framework says "JSVC monitors to prevent double jeopardy" and "Guarantor oversight of fair trial standards" but provides no mechanism for what happens when:

- A national prosecutor declines to file charges
- A national court conducts a sham prosecution (acquittal against overwhelming evidence, trivially lenient sentence)
- A pattern of non-prosecution emerges from one national system

The "Revolving Door" scenario: a Palestinian assaults an Israeli in an SAZ, is handed to PA courts, and is released without prosecution (or vice versa with Israeli courts). SAZ police become a "taxi service" delivering suspects to national systems that may not prosecute them. This destroys SAZ legitimacy immediately because residents see that inter-communal violence carries no consequences.

The Arbitration Courts (01-arbitration-courts.md) explicitly exclude criminal matters: "Criminal matters remain outside MCF jurisdiction" (line 30). Post-Conflict Justice (07-post-conflict-justice.md) addresses only historical crimes and explicitly states "MCF does not conduct criminal investigations" (line 49). Neither fills the gap.

**Mitigating factors already in the framework:**

- Criminal jurisdiction tiers ARE defined (SAZ courts for ≤10 years, national courts for >10 years)
- Forum assignment by defendant origin IS specified for serious offenses
- SAZ police investigation and case file transfer IS described
- JSVC monitoring and guarantor oversight ARE mentioned
- SAZ court structure (Local Court, Appeals Court, Judicial Appointments Committee) IS operational
- CRC protections apply as constitutional floor for all proceedings

**Files:**

- `03-phase-2-saz/02-saz-governance.md` (Sections 1, 3.1)
- `03-phase-2-saz/01-saz-legal-framework.md` (Section 7.1)
- `03-phase-2-saz/04-saz-security.md` (Integrated Police Force section)
- `05-dispute-resolution/01-arbitration-courts.md` (line 30)
- `06-sensitive-issues/07-post-conflict-justice.md` (line 49)

**Recommendation:**

1. **SAZ Public Prosecutor:** Establish an SAZ Public Prosecutor's Office within the judicial branch, appointed by the Judicial Appointments Committee, with prosecutorial jurisdiction over all criminal matters within SAZ court competence (≤10 years). Community balance requirement (no more than 60% from either community). Victim petition right for declination review.
2. **Applicable Criminal Law Rule:** Specify that SAZ courts apply the defendant's national criminal law for offense definition and penalty range, SAZ procedural rules, and CRC protections as constitutional minimum. SAZ Council may define regulatory offenses (≤2 years) for SAZ-specific matters.
3. **Transfer Indictment Requirement:** SAZ police do not release serious offense suspects to national custody without a prima facie indictment from the national authority. 14-day deadline; default is release on SAZ-supervised conditions with case referral to monitoring.
4. **SAZ Justice Monitor:** JSVC-appointed monitor with legal standing to observe all national court proceedings arising from SAZ offenses. Files amicus briefs. Reports publicly on prosecution adequacy.
5. **Prosecution Failure as Spoiler Action:** Systematic failure to prosecute inter-communal violence classified as spoiler action, triggering guarantor escalation and conditionality review.

**Design decision (resolved):** Implement Prosecution Accountability Model. See Decision 11 below.

---

## Design Decisions (Resolved)

### Decision 1: Guarantor Veto Power (was Open Question 1)

**Question:** Do you want guarantor assessments to be advisory (no veto), or is a de facto veto acceptable in practice?

**Decision:** Accept the de facto veto and rename it. "No veto" language replaced with "Guarantor Confidence Requirement." Guarantors have effective blocking authority. Accountability mechanism added: guarantors must publish reasoning within 14 days if withholding Confidence Statement.

**Implementation:** Section 2.4 of `08-operational-procedures/02-phase-transitions.md` rewritten. Phase-specific confidence standards documented (Confidence Statement for 0→1, concurrence for 1→2, formal endorsement for 2→3).

### Decision 2: CMS-D as CMS Subtype (was Open Question 2)

**Question:** Is CMS-D meant to be a subtype of CMS, or should the CMS framework's diaspora eligibility be narrowed to align with CMS-D?

**Decision:** CMS-D is a distinct subtype of CMS. Standard CMS reserved for physical residents. CMS framework Section 2.9 narrowed to point to CMS-D as the canonical diaspora status.

**Implementation:** `02-phase-1-civic-membership/01-cms-framework.md` Section 2.9 rewritten. `07-economic-architecture/07-diaspora-engagement.md` Section 2.1 cross-referenced to CMS framework.

### Decision 3: Referendum Terminology (was Open Question 3)

**Question:** Should the Phase 1→2 SAZ referendum be described as a site-selection referendum so Phase 3 stays "first"?

**Decision:** Yes. Phase 1→2 vote renamed to "SAZ Local Consent Plebiscite." Word "referendum" reserved exclusively for the Phase 2→3 framework-wide vote.

**Implementation:** `08-operational-procedures/02-phase-transitions.md` Section 4.3.4 relabeled. `04-phase-3-voluntary-convergence/00-overview.md` referendum section clarified.

### Decision 4: Relative Deprivation (was Open Question 4)

**Question:** How should the framework address economic externalities where MCF success creates relative deprivation for non-participants?

**Decision:** Options 2 + 3 combined. Community spillover benefits designed (PCC infrastructure for all users, MCF medical facilities serve all patients, employer standards apply to all workers). Community Development Fund established (percentage of MCF revenue, accessible regardless of CMS status). Village Leagues parallel explicitly addressed.

**Implementation:** New Section 4.1a added to `02-phase-1-civic-membership/05-no-worse-off-guarantee.md`. New Section 10.2a added to `02-phase-1-civic-membership/04-incentive-structure.md`.

### Decision 5: Clearing-Independent Digital Ledger (Finding 16)

**Question:** Should the framework specify a clearing-independent payment instrument or rely on USD-only fallback?

**Decision:** Implement the MCF Value Transfer Protocol (MVTP) -- a closed-loop digital ledger backed 1:1 by hard currency held in Guarantor Central Bank accounts. USD-only fallback is insufficient because USD transfers still require correspondent banking relationships that can be severed by political pressure. MVTP provides financial sovereignty for internal MCF operations without requiring a new national currency.

**Implementation:** New Sections 4.4 (MVTP) and 4.5 (Correspondent Banking Resilience) added to `07-economic-architecture/01-economic-integration.md`. New Scenario F (State-Level Clearing Denial) added to `04-guarantor-architecture/06-economic-crisis-response.md`. Financial infrastructure denial added as spoiler category in `08-operational-procedures/04-spoiler-response.md`.

### Decision 6: Jordan Corridor (Finding 17)

**Question:** How should the framework address construction material supply chain vulnerability at pre-corridor entry points?

**Decision:** Formalize the Jordan Route. Designate the King Hussein Bridge (Allenby Bridge) as the Primary Material Entry Point for West Bank SAZs, under UVB inspection, bypassing Israeli port customs protocols. This leverages Jordan's role as a regional guarantor with direct border access.

**Implementation:** New Section 1a (Jordan Corridor) added to `07-economic-architecture/05-infrastructure-coordination.md` with alternative supply routes table and pre-positioned material reserves. New Section 4b (Port-to-Corridor Transition Protocol) added to `07-economic-architecture/01-economic-integration.md`.

### Decision 7: Non-Interference Conditionality (Finding 18)

**Question:** Should the framework allow SAZ establishment over central authority objection, or maintain central consent as a hard requirement?

**Decision:** Maintain central consent but apply conditionality of aid. Guarantors do not force central authorities to say "yes." However, guarantors condition general budget support to the blocking authority (PA budgetary aid, Israeli security cooperation packages) on non-interference with verified community SAZ petitions. This applies only when the Guarantor Forum has determined the objection is non-substantive (political veto without security/feasibility/legal basis). The mechanism preserves sovereign consent while making the cost of blocking a democratic local vote economically significant.

**Implementation:** Blocked-Petition Escalation pathway and Non-Interference Conditionality added to `03-phase-2-saz/01-saz-legal-framework.md` Section 2.4. Confidential interest signaling and blocked-petition reference added to `03-phase-2-saz/06-internal-saz-selection.md`. New Section 11.5 (Pre-SAZ Advocacy Protection) added to `02-phase-1-civic-membership/03-anti-intimidation.md`.

### Decision 8: Satellite-First Connectivity Architecture (Finding 19)

**Question:** Should the framework mandate independent MCF connectivity infrastructure or rely on commercial telecom with enhanced protections?

**Decision:** Mandate Satellite-First Connectivity Architecture. Primary MCF institutional uplink via LEO satellite constellation contracted through Guarantor states (not through Israeli or Palestinian telecom providers). Local distribution via private 5G/Wi-Fi 6 on unlicensed ISM bands. Commercial telecom treated as tertiary supplement. Bandwidth throttling and frequency denial explicitly classified as interference with measurable thresholds. Critical systems designed for offline-capable operation with local caching and periodic synchronization.

**Rationale:** Prohibitions against interference are necessary but insufficient. A LEO constellation is harder to jam than a fiber optic cable is to throttle. Physical independence eliminates the dependency rather than managing it.

**Implementation:** New Section 5 (MCF Independent Connectivity) added to `07-economic-architecture/05-infrastructure-coordination.md` with LEO satellite backbone, private local networks, degradation-as-interference thresholds, and offline-capable systems. Network Infrastructure section of `08-operational-procedures/09-data-it-systems.md` rewritten with Satellite-First Architecture, satellite infrastructure table, and offline-capable design table. Cross-reference added to Operational Autarky Principle.

### Decision 9: Off-Grid Primary Design (Finding 21)

**Question:** Should SAZ utility infrastructure be designed grid-first with independent fallback, or independent-first with grid as supplement?

**Decision:** Mandate Off-Grid Primary Design as default SAZ standard. Default power: islandable microgrids (solar + battery storage + waste-to-energy). Default water: on-site desalination, rainwater harvesting, atmospheric water generation, mandatory greywater recycling. National grid/water connection treated as supplementary "nice-to-have." Connection refusal explicitly classified as obstruction on a defined 90-day timeline. SAZ Legal Framework grants explicit Utility Provisioning Authority to SAZ governance.

**Rationale:** Same structural logic as Decision 8. Designing for independence eliminates the monopoly veto entirely. Grid connection becomes a convenience, not a chokepoint.

**Implementation:** New Section 1a (Off-Grid Primary Design) added to `07-economic-architecture/05-infrastructure-coordination.md` with default SAZ power design table and connection refusal timeline. New Section 4 (Independent Water Provisioning) added to `06-sensitive-issues/01-water-resources.md` with default SAZ water design table and connection refusal classification. Utility Provisioning Authority added to SAZ Establishment Agreement Content in `03-phase-2-saz/01-saz-legal-framework.md` Section 2.5.

### Decision 10: Institutional Cannibalization Mitigation (Finding 20)

**Question:** How should the framework address human capital drain from PA institutions to MCF-area employment?

**Decision:** No structural design change required. Implement three mitigation mechanisms: (1) Human Capital Replacement Levy -- one-time fee of 3 months salary when MCF employers hire workers from PA public sector within preceding 12 months, with levy revenue restricted to recruitment, training, and salary competitiveness at the originating institution. (2) Rotation Secondment Protocol -- 6-12 month fixed-term secondments with one renewal permitted (24 months maximum), 12-month cooling-off period, and mandatory knowledge transfer handover. (3) Institutional Capacity Monitoring -- No Worse Off guarantee extended to track PA institutional staffing levels with >15% degradation threshold triggering graduated mitigation response.

**Implementation:** New Section 10.2b (Human Capital Replacement Levy) added to `02-phase-1-civic-membership/04-incentive-structure.md`. New Section 4a (Rotation Secondment Protocol) added to `08-operational-procedures/12-personnel-standards.md`. New Section 4.4a (Institutional Capacity Monitoring) added to `02-phase-1-civic-membership/05-no-worse-off-guarantee.md`.

### Unifying Principle: Operational Autarky

Findings 16, 19, and 21 share a common structural pattern: MCF's protections were framed as prohibitions ("you may not shut off X") rather than as independence ("we can operate without X"). Decisions 5 (MVTP), 8 (Satellite-First), and 9 (Off-Grid Primary) resolve this pattern through a unifying design principle:

> **Operational Autarky Principle:** MCF systems (Finance, Connectivity, Utilities) must be capable of sustaining critical functions without the active cooperation of Host State infrastructure. Connection to national systems is preferred for efficiency, but independence is required for resilience.

**Implementation:** Added as Design Principle 5 in `07-economic-architecture/05-infrastructure-coordination.md` with an instantiations table mapping each domain (Finance, Connectivity, Electricity, Water, Materials) to its Normal Mode and Autarky Mode implementations.

### Decision 11: Prosecution Accountability Model (Finding 22)

**Question:** How should the framework prevent impunity for inter-communal violence within SAZs without claiming criminal sovereignty?

**Decision:** Implement a three-layer Prosecution Accountability Model that fills the gaps in the existing criminal jurisdiction structure:

1. **SAZ Public Prosecutor's Office** for offenses within SAZ court competence (≤10 years). Appointed by Judicial Appointments Committee. Community balance requirement. Victim petition right for declination review.
2. **Applicable Criminal Law Rule:** Defendant's national criminal law for offense definition and penalty range. SAZ procedural rules. CRC protections as constitutional minimum. SAZ Council may define regulatory offenses (≤2 years).
3. **Transfer Custody Protocol and Justice Monitor** for serious offenses (>10 years) transferred to national courts:
   - Transfer Indictment requirement: national authority must present prima facie indictment within 14 days or suspect released on SAZ-supervised conditions
   - SAZ Justice Monitor (JSVC-appointed) with legal standing to observe national proceedings, file amicus briefs, and report publicly
   - Prosecution failure classified as spoiler action: declination (90 days, guarantor engagement), sham prosecution (spoiler documentation and escalation), systematic failure (3+ in 24 months triggers full spoiler protocol and conditionality)

**Rationale:** Personal jurisdiction preserves sovereignty. Observation standing and spoiler classification ensure accountability. The framework cannot force a national court to convict, but it ensures that systematic prosecution failures carry political costs that make impunity economically irrational. This prevents the "Revolving Door" where SAZ police arrest, national courts release, and inter-communal violence goes unaddressed.

**Implementation:** SAZ Public Prosecutor (Section 1.4), Applicable Criminal Law for SAZ Courts, Transfer Custody Protocol, SAZ Justice Monitor, and Prosecution Failure Accountability added to `03-phase-2-saz/02-saz-governance.md`.

---

## Action Matrix

### Part I: Internal Consistency

| # | Severity | Fix type | Status | Files changed |
|---|----------|----------|--------|---------------|
| 1 | High | Text revision | RESOLVED | `README.md` |
| 2 | High | Text revision | RESOLVED | `01-phase-0-institutions/00-overview.md` |
| 3 | High | Section rewrite (Decision 1) | RESOLVED | `08-operational-procedures/02-phase-transitions.md` |
| 4 | Medium | Text revision + rename (Decision 3) | RESOLVED | `04-phase-3-voluntary-convergence/00-overview.md`, `08-operational-procedures/02-phase-transitions.md` |
| 5 | Medium | Section rewrite (Decision 2) | RESOLVED | `02-phase-1-civic-membership/01-cms-framework.md`, `07-economic-architecture/07-diaspora-engagement.md` |
| 6 | Medium | Added fallback provision | RESOLVED | `02-phase-1-civic-membership/01-cms-framework.md` |
| 7 | Low | Added clarifying sentence | RESOLVED | `01-phase-0-institutions/02-jsvc-charter.md` |
| 8 | Low | Directory renamed + cross-refs updated | RESOLVED | `README.md`, `08-operational-procedures/06-exit-conditions.md`, filesystem |

### Part II: Strategic and Operational

| # | Severity | Fix type | Status | Files changed |
|---|----------|----------|--------|---------------|
| 9 | High | New Section 9 (deployment logistics) | RESOLVED | `01-phase-0-institutions/01-uvb-charter.md` |
| 10 | High | New sections (Decision 4: spillovers + CDF) | RESOLVED | `02-phase-1-civic-membership/05-no-worse-off-guarantee.md`, `02-phase-1-civic-membership/04-incentive-structure.md` |
| 11 | Medium | New Section 8.4 (Jerusalem bypass routing) | RESOLVED | `01-phase-0-institutions/03-pcc-protocols.md` |
| 12 | Medium | New section (transition implementation) | RESOLVED | `03-phase-2-saz/06-internal-saz-selection.md` |
| 13 | Medium | Restructured to comity model | RESOLVED | `03-phase-2-saz/03-constitutional-floor.md` |
| 14 | Low | Added guarantor dependency note | RESOLVED | `08-operational-procedures/04-spoiler-response.md` |
| 15 | Low | New section (legal protection) | RESOLVED | `04-guarantor-architecture/00-overview.md` |

### Part III: Structural Vulnerabilities

| # | Severity | Fix type | Status | Files changed |
|---|----------|----------|--------|---------------|
| 16 | High | New sections (Decision 5: MVTP, clearing resilience, spoiler scenario) | RESOLVED | `07-economic-architecture/01-economic-integration.md`, `04-guarantor-architecture/06-economic-crisis-response.md`, `08-operational-procedures/04-spoiler-response.md` |
| 17 | Medium | New sections (Decision 6: Jordan Corridor, port-to-corridor protocol, material reserves) | RESOLVED | `07-economic-architecture/01-economic-integration.md`, `07-economic-architecture/05-infrastructure-coordination.md` |
| 18 | High | New sections (Decision 7: Non-Interference Conditionality, blocked-petition escalation, pre-SAZ advocacy protection) | RESOLVED | `03-phase-2-saz/01-saz-legal-framework.md`, `03-phase-2-saz/06-internal-saz-selection.md`, `02-phase-1-civic-membership/03-anti-intimidation.md` |

### Part IV: Systemic Dependencies

| # | Severity | Fix type | Status | Files changed |
|---|----------|----------|--------|---------------|
| 19 | Medium-High | New sections (Decision 8: Satellite-First Connectivity, Operational Autarky Principle) | RESOLVED | `07-economic-architecture/05-infrastructure-coordination.md`, `08-operational-procedures/09-data-it-systems.md` |
| 20 | Medium | New sections (Decision 10: Human Capital Replacement Levy, Rotation Secondment Protocol, Institutional Capacity Monitoring) | RESOLVED | `02-phase-1-civic-membership/04-incentive-structure.md`, `08-operational-procedures/12-personnel-standards.md`, `02-phase-1-civic-membership/05-no-worse-off-guarantee.md` |
| 21 | Medium-High | New sections (Decision 9: Off-Grid Primary Design, Independent Water Provisioning, Utility Provisioning Authority) | RESOLVED | `07-economic-architecture/05-infrastructure-coordination.md`, `06-sensitive-issues/01-water-resources.md`, `03-phase-2-saz/01-saz-legal-framework.md` |

### Part V: Criminal Justice

| # | Severity | Fix type | Status | Files changed |
|---|----------|----------|--------|---------------|
| 22 | Medium-High | New sections (Decision 11: SAZ Public Prosecutor, Applicable Criminal Law, Transfer Custody Protocol, Justice Monitor, Prosecution Failure Accountability) | RESOLVED | `03-phase-2-saz/02-saz-governance.md` |

### Resolution Summary

All 22 findings resolved. All 11 design decisions implemented. Directory rename completed. Operational Autarky Principle established as unifying design principle for Findings 16, 19, and 21.

**Files modified (27 total):**

- `README.md` (Findings 1, 8)
- `01-phase-0-institutions/00-overview.md` (Finding 2)
- `01-phase-0-institutions/01-uvb-charter.md` (Finding 9)
- `01-phase-0-institutions/02-jsvc-charter.md` (Finding 7)
- `01-phase-0-institutions/03-pcc-protocols.md` (Finding 11)
- `02-phase-1-civic-membership/01-cms-framework.md` (Findings 5, 6)
- `02-phase-1-civic-membership/03-anti-intimidation.md` (Finding 18)
- `02-phase-1-civic-membership/04-incentive-structure.md` (Findings 10, 20)
- `02-phase-1-civic-membership/05-no-worse-off-guarantee.md` (Findings 10, 20)
- `03-phase-2-saz/01-saz-legal-framework.md` (Findings 18, 21)
- `03-phase-2-saz/02-saz-governance.md` (Finding 22)
- `03-phase-2-saz/03-constitutional-floor.md` (Finding 13)
- `03-phase-2-saz/06-internal-saz-selection.md` (Findings 12, 18)
- `04-guarantor-architecture/00-overview.md` (Finding 15)
- `04-guarantor-architecture/06-economic-crisis-response.md` (Finding 16)
- `04-phase-3-voluntary-convergence/00-overview.md` (Finding 4; directory renamed from `03-` per Finding 8)
- `06-sensitive-issues/01-water-resources.md` (Finding 21)
- `07-economic-architecture/01-economic-integration.md` (Findings 16, 17)
- `07-economic-architecture/05-infrastructure-coordination.md` (Findings 17, 19, 21 + Operational Autarky Principle)
- `07-economic-architecture/07-diaspora-engagement.md` (Finding 5)
- `08-operational-procedures/02-phase-transitions.md` (Findings 3, 4)
- `08-operational-procedures/04-spoiler-response.md` (Findings 14, 16)
- `08-operational-procedures/06-exit-conditions.md` (Finding 8 cross-ref update)
- `08-operational-procedures/09-data-it-systems.md` (Finding 19)
- `08-operational-procedures/12-personnel-standards.md` (Finding 20)
