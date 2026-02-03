# Briefing: Gap 205 — The Regulatory Sediment (Legislative Entropy)

**Prepared for:** External reviewer (Step 2 of Multi-LLM Gap Resolution Protocol)
**Date:** 2026-02-02
**Gap severity:** High
**Source file:** `04-meta/gaps/11-institutional-governance.md`, line 2645

---

## 1. Problem Statement

Over decades, federal regulations accumulate without systematic review. Each regulation is individually reasonable; collectively they paralyze. The Code of Federal Regulations has grown from 10,000 pages (1950) to 180,000+ pages today — compound growth of ~2.5% annually. At this rate, the CFR would exceed 1 million pages by 2100.

The entropy problem: each regulation has a constituency defending it; sunset provisions are routinely extended via voice vote; courts interpret regulations expansively over time; new regulations pile on top of old without consolidation; no mechanism forces comprehensive review. The system seizes up through sclerosis — not tyranny, but paralysis.

The Regional Federalism framework makes this worse: with multiple levels of government (federal, Regional, State, local), regulatory accumulation occurs at every level. A business operating across Regions navigates not just federal regulations but potentially seven different Regional regulatory regimes, each accumulating independently.

## 2. Existing Provisions (Overlap ~35-40%, MODERATE)

### 2.1 Provisions that partially address the concern

| Provision | What it covers | What it misses |
|---|---|---|
| **Art XIV-RF §9** — De Novo Review Mandate | Eliminates Chevron deference; courts must decide questions of law de novo without deference to agency interpretations | Passive — requires case-by-case litigation; doesn't force systematic review or impose expiration |
| **Art II §18(i)** — Secret Law Sunset | Unpublished legal interpretations expire after 5 years; programs under expired interpretations must be reauthorized | Only covers unpublished/secret interpretations, not the vast body of published regulations |
| **Art IV §3(b)-(d)** — Compliance Cost Review | CBO estimates 10-year compliance costs; pre-enactment fiscal adequacy certification; post-enactment challenges if costs exceed estimates by >20% | Pre-enactment review only; no periodic post-enactment reassessment; no aggregate compliance budget |
| **Art IV §6(b)** — IFC/ARB Reauthorization | IFC and ARB statutory authorities sunset every 12 years unless reauthorized | Covers institutional authorities, not regulations generally |
| **Art XVII-RF** — Emergency Power Auto-Termination | Emergency powers auto-expire without reauthorization | Sector-specific to emergency powers |
| **Art XI-RF §6(k)** — Security Compact Review | Congress reviews all inter-Regional security compacts every 2 years; unreauthorized compacts automatically sunset | Sector-specific to military compacts |
| **Art IV §4(e)** — Maintenance of Effort Sunset | MOE requirements expire after 5 years unless explicitly renewed | Narrow fiscal mechanism |
| **Art X §13(c)(3)** — Legacy Burden Factor Decline | Legacy Burden Factor declines to zero over 60 years | Sector-specific fiscal adjustment |

### 2.2 The pattern

The constitution demonstrates extensive use of sunset mechanisms for **specific domains** (emergency powers, secret law, security compacts, institutional authorities, MOE requirements, fiscal adjustments). But it **never applies the concept universally** to the general regulatory stock. Gap 205 proposes universalizing what the constitution already does in pieces.

### 2.3 Provisions that create TENSION

| Provision | Tension |
|---|---|
| **Art II §4(k)(1)** — Constitutional Labor Minimums: Permanence | Art II §4(k)(1) explicitly exempts constitutional labor minimums from sunset AND variance. A universal regulatory sunset must carve out constitutional provisions and provisions explicitly marked permanent. |
| **Art IV §3** — Unfunded Mandates Protection | §3 requires compliance cost estimation before enactment. A regulatory sunset that causes regulations to lapse could create its own compliance disruption — businesses that invested in compliance lose that investment. |
| **Art XIV-RF §9** — De Novo Review | De novo review already allows courts to challenge outdated regulatory interpretations. A sunset mechanism adds a legislative path alongside the judicial path — but if Congress routinely rubber-stamps reauthorization, the sunset becomes ceremonial. |
| **Art II §4(d)-(g)** — Concurrent Authority Sunset | Art II §4 already has a 10-year sunset for congressional floors in concurrent domains. A new universal sunset must coordinate with these existing domain-specific timelines. |

## 3. Proposed Placement

### Primary option: Art II §24 in `02-design/constitution/02-powers-and-rights.md`

- Art II constrains federal power exercise; §18 already has a sunset for secret law; §4 has concurrent authority sunsets
- A universal regulatory sunset is fundamentally a constraint on how federal regulatory power accumulates over time
- Keeps all power-constraint provisions in one article
- Current last section is §23 (Authenticity of Official Acts); §24 is available

### Alternative A: New section in `05-safeguards.md` (e.g., Art XII-A or Art XIII §11)

- Pro: Frames regulatory sunset as a structural safeguard, like secession prohibition or amendment process
- Con: Safeguards file deals with constitutional structure (secession, amendments, eternity clause), not regulatory process

### Alternative B: New standalone article (Art XXVI-RF or similar)

- Pro: Emphasizes the importance of regulatory review as a foundational principle
- Con: Creates yet another article for what is fundamentally a constraint on existing power

### Alternative C: Art IV (Governance) in `03-regional-governance.md`

- Pro: Art IV already has compliance cost review (§3), MOE sunset (§4(e)), IFC/ARB reauthorization (§6(b))
- Con: Art IV in the file's numbering is about governance structure; the fiscal provisions in the same file are Art X

### Recommendation: Art II §24

Natural extension of Art II's power constraints. Coordinates with §4 concurrent authority sunsets and §18 secret law sunset. Keeps the universal regulatory review framework alongside the existing piecemeal approaches it subsumes.

## 4. Design Questions

### D1. What is the right sunset duration?

The proposal uses 20 years. Consider the existing framework's range:

- Art II §18(i): 5 years (secret law interpretations)
- Art IV §4(e): 5 years (MOE requirements)
- Art II §4: 10 years (concurrent authority floors)
- Art IV §6(b): 12 years (IFC/ARB statutory authorities)
- Art XI-RF §6(k): 2 years (security compacts)

Options:

- (A) 20 years — as proposed; long enough for regulations to prove value, short enough for generational review
- (B) 15 years — more aggressive review cycle; three Presidential terms
- (C) 25 years — more conservative; balances stability with review
- (D) Tiered: 10 years for regulations with compliance costs above a threshold, 20 years for others
- (E) Match the existing §4 mechanism: 10 years, consistent with concurrent authority sunsets

### D2. What is the scope — regulations only, or statutes too?

The proposal covers "Federal regulations, administrative rules, and agency guidance documents." Consider:

- (A) Regulations, administrative rules, and agency guidance only — statutes are Congress's domain and have their own democratic accountability through elections
- (B) Include statutes that delegate regulatory authority — the enabling legislation expires alongside the regulations it spawns
- (C) Include all statutory provisions that have not been affirmatively amended or reenacted within the sunset period
- (D) Regulations and guidance only; statutes exempt but statutory delegations of rulemaking authority expire

### D3. Should there be a regulatory budget?

The proposal includes a compliance cost cap as a percentage of GDP. Consider:

- (A) Constitutional mandate for regulatory budget with GDP cap (requires supermajority to exceed)
- (B) Constitutional mandate for compliance cost tracking and reporting, but no hard cap — transparency mechanism only
- (C) Statutory implementation: Congress shall establish a regulatory budget by legislation; constitutional text provides the principle
- (D) No regulatory budget — the sunset mechanism alone is sufficient to control accumulation
- (E) Hybrid: constitutional mandate for tracking; statutory cap adjustable by Congress without supermajority

### D4. Who calculates compliance costs?

The proposal says "independent agency." The framework already has:

- CBO (Art IV §3(b)) — estimates compliance costs for new mandates
- IFC — independent fiscal monitoring, actuarial standards, pension oversight

Options:

- (A) CBO — already handles pre-enactment cost estimates; extend to post-enactment tracking
- (B) IFC — independent, constitutionally established, has compliance monitoring expertise
- (C) New independent body — dedicated Regulatory Review Commission
- (D) CBO estimates pre-enactment; IFC monitors post-enactment; both report to Congress

### D5. How should staggered implementation work?

The proposal divides existing regulations into 20 cohorts, one expiring each year. Consider:

- (A) 20 cohorts by subject matter — as proposed
- (B) 20 cohorts by date of enactment — oldest first, giving newest regulations full 20 years
- (C) Prioritized review: highest-cost regulations first, regardless of age
- (D) Congressional discretion: Congress determines cohort assignment and review sequence
- (E) Risk-based: IFC or CBO identifies highest-burden regulatory clusters; those are reviewed first

### D6. What happens to regulations that Congress fails to reauthorize?

The proposal says automatic expiration. But mass expiration creates its own risks. Consider:

- (A) Automatic expiration with no grace period — forces Congress to act
- (B) Automatic expiration with 1-year grace period — gives Congress time to act on must-retain regulations
- (C) Automatic provisional extension (6 months) upon petition showing significant disruption; Congress must act during extension
- (D) Lapse to non-enforcement: regulation remains on books but may not be enforced until reauthorized — preserves voluntary compliance while removing coercive power
- (E) Graduated: first failure triggers 1-year extension with mandatory review; second failure triggers automatic expiration

### D7. Should the judicial interpretation sunset be adopted?

The proposal says judicial interpretations expanding regulatory scope expire with the underlying regulation unless Congress codifies them. Consider:

- (A) Yes — interpretations expanding scope expire; interpretations narrowing scope survive (asymmetric sunset)
- (B) Yes — all judicial interpretations of regulations expire with the regulation; clean slate upon reauthorization
- (C) No — judicial interpretations are independent legal authority; they survive unless explicitly overruled
- (D) Modified: judicial interpretations survive reauthorization unless Congress explicitly repudiates them in the reauthorization

### D8. Should this apply to Regional regulations?

The proposal addresses federal regulations only. But regulatory sediment accumulates at every level. Consider:

- (A) Federal only — Regions manage their own regulatory burden through their own democratic processes
- (B) Constitutional floor: Regions must adopt some form of regulatory review, but design is Regional
- (C) Mandatory Regional application — same sunset period applies to Regional regulations
- (D) Federal mandate plus Regional opt-in: Regions may adopt the federal sunset framework by Regional law

### D9. What categories should be exempt or have modified treatment?

Some regulations are different in kind. Consider:

- (A) No exemptions — the whole point is forcing review of everything
- (B) Exempt constitutional provisions (Art II §4(k)(1) permanence clause, rights floors) but not statutory/regulatory implementations
- (C) Exempt: constitutional provisions, treaty obligations, international agreements; modified treatment (longer sunset) for: financial system regulations, nuclear safety, environmental baseline standards
- (D) Exempt constitutionally-mandated minimums; all other regulations subject to sunset regardless of subject matter

### D10. How does this interact with Art II §4 concurrent authority sunsets?

Art II §4 already has 10-year sunsets for congressional floors in concurrent domains. A universal 20-year sunset would create two overlapping timelines. Consider:

- (A) Coordination clause: the universal sunset subsumes §4 sunsets; use the shorter period
- (B) Independent operation: §4 sunsets apply to concurrent authority floors; §24 sunset applies to all other regulations; if both apply, shorter period governs
- (C) §4 sunset governs concurrent authority regulations specifically; §24 governs everything else; no overlap
- (D) Harmonize: change §4 sunset to match §24 sunset period (both 20 years or both 10 years)

### D11. What reauthorization process — full legislative or simplified?

The proposal requires majority vote + Presidential signature + cost-benefit analysis + public comment. Consider:

- (A) Full legislative process — identical to original enactment; prevents rubber-stamping
- (B) Simplified reauthorization: single up-or-down vote on each cohort; no amendments; forces clean retain-or-expire decision
- (C) Tiered: regulations above a compliance cost threshold require full legislative process; below threshold, simplified reauthorization
- (D) Default reauthorization upon affirmative cost-benefit showing; Congress votes only on regulations flagged by the reviewing body as net-negative or outdated
- (E) Negative option: regulation survives unless Congress affirmatively votes to expire it — reverses the default but still forces a vote

### D12. Should there be an anti-gaming mechanism for the reauthorization process?

Congress could game the sunset by:

- Bundling regulations into must-pass omnibus reauthorization bills
- Attaching controversial regulations to popular ones
- Rushing review to prevent meaningful analysis

Options:

- (A) Single-subject rule for reauthorization bills — each regulation or regulatory cluster reauthorized independently
- (B) Anti-bundling: no more than [X] regulations may be reauthorized in a single legislative vehicle
- (C) Mandatory individual cost-benefit analysis for each regulation being reauthorized — no mass reauthorization without individual review
- (D) CBO/IFC must certify that each regulation was individually reviewed before reauthorization; mass reauthorization without certification is void

### D13. How to prevent the "regulatory conversion" gaming vector?

If regulations face sunset but statutes don't, agencies and Congress will convert regulations into statutory text to avoid review. Consider:

- (A) The sunset should apply to statutory provisions that delegate rulemaking authority, not just the rules themselves
- (B) Anti-conversion clause: statutory codification of a regulation during the 2 years preceding its sunset date is subject to the same sunset
- (C) Not a problem — if Congress affirmatively legislates the substance of a regulation, that IS the democratic review the sunset was designed to produce
- (D) Track regulatory substance rather than form: IFC identifies regulatory burden regardless of whether implemented via statute or regulation

### D14. Should there be a constitutional floor for essential regulations?

Some regulations protect fundamental rights (civil rights enforcement, environmental health, financial consumer protection). Consider:

- (A) No floor — the sunset forces review, not repeal; good regulations will be reauthorized
- (B) Constitutional floor: regulations implementing constitutional rights (Art III-RF §§1-8) may not be sunsetted; they can only be repealed through normal legislative process
- (C) Presumptive retention: regulations implementing constitutional provisions are presumed reauthorized unless Congress affirmatively votes to expire them (reversed default)
- (D) Essential regulation registry: IFC maintains a list of regulations essential to constitutional rights; these receive extended sunset (30 years) and presumptive retention

## 5. Gaming Vectors

### From the proposal (4)

| # | Vector | Mechanism |
|---|---|---|
| G1 | The "Safety" Defense | Every regulation justified by harm prevention; no aggregation of compliance costs; death by a thousand paper cuts |
| G2 | The "Extension Habit" | Sunsets routinely extended via voice vote; de facto permanence with theoretical temporariness |
| G3 | The "Regulatory Ratchet" | New regulations never repeal old; selective enforcement creates arbitrary power |
| G4 | The "Capture Sediment" | Incumbent businesses support complex regulations as barrier to entry; regulatory burden becomes competitive advantage |

### Additional gaming vectors (11)

| # | Vector | Mechanism |
|---|---|---|
| G5 | The "Cohort Gaming" | Lobbyists ensure their preferred regulations are grouped with popular regulations (food safety, child protection) so Congress cannot expire one without expiring all |
| G6 | The "Must-Pass Omnibus" | Congress bundles all expiring regulations into a single must-pass reauthorization bill; meaningful review of individual regulations becomes impossible |
| G7 | The "Emergency Classification" | Agencies classify regulations as "emergency" or "safety-critical" to claim exemption; every regulation eventually labeled essential |
| G8 | The "Delegation Reset" | Congress reauthorizes vague statutory authority; agencies re-issue functionally identical regulations under new authorization; the regulations change label but not substance |
| G9 | The "Regulatory Conversion" | As sunset approaches, agency-promulgated regulations are codified into statute to avoid the sunset mechanism; regulatory burden increases because statutes are harder to modify |
| G10 | The "Complexity Shield" | Regulations made deliberately complex so review is impossible within available time; Congress rubber-stamps because the alternative is mass expiration of rules it doesn't understand |
| G11 | The "GDP Manipulation" | If regulatory budget is GDP-linked, gaming the GDP denominator (excluding sectors, changing calculation methodology) allows more or fewer regulations |
| G12 | The "Cost Undercount" | Compliance cost calculation body systematically underestimates costs to stay within budget; agency capture of the cost-estimation process |
| G13 | The "Sunset Cliff" | Opponents of regulation let critical regulations expire to create emergency; emergency then justifies hasty re-enactment without review, plus new emergency regulations |
| G14 | The "Burden Shift" | As federal regulations sunset, federal agencies encourage Regions to adopt equivalent regulations; total regulatory burden unchanged but shifted below the sunset mechanism |
| G15 | The "Guidance Substitution" | Formal regulations sunset; agencies replace them with "informal guidance," "dear colleague letters," "FAQ documents" that carry equivalent coercive weight without triggering the sunset |

## 6. Verification Questions

### V1. Does the new text establish a genuine sunset, not ceremonial review?

The critical question: will Congress actually review regulations, or will reauthorization become routine? The text must make rubber-stamping structurally difficult — through individual review requirements, cost-benefit certification, or single-subject rules.

### V2. Does the new text coordinate with existing sunset mechanisms?

Art II §4 (10-year concurrent authority), Art IV §6(b) (12-year IFC/ARB), Art II §18(i) (5-year secret law), Art XI-RF §6(k) (2-year security compacts) — the new text must specify how these interact with the universal sunset.

### V3. Does the new text prevent the "regulatory conversion" vector?

If the sunset applies only to regulations but not statutes, the entire regulatory stock will be converted to statutory text, defeating the purpose. The text must address this migration path.

### V4. Does the new text protect constitutional provisions from accidental sunset?

Art II §4(k)(1) explicitly exempts constitutional labor minimums from sunset. The new text must ensure that constitutionally mandated protections and rights-implementing regulations are not swept up in the general sunset.

### V5. Does the new text address Regional regulatory accumulation?

If the sunset only applies federally, Regions become the new site of regulatory sediment accumulation. The text should at least establish a principle that Regions adopt some form of periodic regulatory review.

### V6. Does the new text prevent the "guidance substitution" vector?

Agencies that lose formal regulations may replace them with informal guidance that carries equivalent practical force. The text must cover all forms of regulatory authority — formal rules, informal guidance, enforcement policies, interpretive letters — not just notice-and-comment regulations.

---

## 7. Draft Text Direction

The amendment should:

1. **Art II §24(a) — Regulatory Sunset Mandate** — all federal regulations, administrative rules, agency guidance documents, and interpretive letters shall expire after [duration] unless affirmatively reauthorized by Congress through legislative action; coordinate with existing sector-specific sunsets
2. **Art II §24(b) — Reauthorization Requirements** — define what reauthorization entails: cost-benefit analysis, public comment, individual or clustered review; anti-bundling protections
3. **Art II §24(c) — Staggered Implementation** — existing regulatory stock divided into cohorts; one cohort reviewed each year; congressional discretion on sequencing with IFC/CBO prioritization recommendation
4. **Art II §24(d) — Compliance Cost Tracking** — IFC/CBO ongoing monitoring of aggregate regulatory compliance costs; annual public reporting; define role of cost-estimation body
5. **Art II §24(e) — Anti-Circumvention** — regulatory conversion prohibition (substance-over-form); guidance substitution prohibition (all forms of regulatory authority covered); delegation reset prohibition (vague reauthorization of rulemaking authority doesn't restart the clock for functionally identical regulations)
6. **Art II §24(f) — Constitutional Protection** — constitutionally mandated provisions exempt; rights-implementing regulations receive presumptive retention; Art II §4(k)(1) permanence respected
7. **Art II §24(g) — Judicial Interpretation** — define treatment of judicial interpretations upon regulation expiration; coordinate with Art XIV-RF §9 de novo review
8. **Art II §24(h) — Regional Application** — establish principle for Regional regulatory review; minimum standard or opt-in framework
9. **Art II §24(i) — Enforcement and Transition** — self-executing; staggered transition for existing regulations; grace period mechanics; standing to challenge non-compliance
