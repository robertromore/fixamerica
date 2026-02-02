# Briefing: Gap 199 — The Family Fracture (Status Portability)

**Prepared for:** External reviewer (Step 2 of Multi-LLM Gap Resolution Protocol)
**Date:** 2026-02-02
**Gap severity:** High
**Source file:** `04-meta/gaps/13-intergovernmental.md`, line 6052

---

## 1. Problem Statement

Regions control family law within their Exclusive Domains (Art II §1(e)(2)(iv)). A Region could refuse to recognize marriages, adoptions, or parentage established in other Regions, effectively dissolving families when they cross Regional borders. A couple legally married in Region A moves to Region B for employment; Region B refuses recognition. The couple loses spousal healthcare benefits, inheritance rights, hospital visitation, joint tax filing, and parental rights over shared children. The family is legally dissolved by crossing a Regional border.

The adoption variant is more severe: a parent legally adopts a child in Region A; Region B refuses to recognize the adoption; the parent loses legal parental rights; the child becomes a legal orphan.

Pre-*Obergefell*, same-sex couples faced exactly this reality. The Regional Federalism framework could recreate it for any family structure a Region wishes to target.

## 2. Existing Provisions (Overlap ~50-55%, MODERATE)

### 2.1 Provisions that partially address the concern

| Provision | What it covers | What it misses |
|---|---|---|
| **Art I §9(a)** — Full Faith and Credit | "Each jurisdiction shall give full faith and credit to the public acts, records, and judicial proceedings of every other jurisdiction" | General principle; does not specifically enumerate family status or define scope of recognition |
| **Art I §9(b)** — Legal Status Recognition | "Marriages, divorces, adoptions, name changes, powers of attorney, corporate registrations, and property titles established under any jurisdiction's law shall be recognized in all other jurisdictions" | **Does NOT list** civil unions, domestic partnerships, parentage determinations, surrogacy agreements; **does NOT specify** that all *incidents* of status (benefits, visitation, custody, inheritance) must be honored |
| **Art I §9(e)** — Prohibited Refusal Grounds | "No jurisdiction may refuse recognition based on religious or moral objection, political disagreement, economic protectionism, or retaliation" | **Does NOT enumerate** sex, sexual orientation, race, ethnicity, religion of the *parties* as protected characteristics; a Region could claim a non-religious, non-moral basis for refusal |
| **Art I §9(f)** — Self-Execution | "This section is self-executing and does not require implementing legislation" | No specific enforcement mechanisms (jurisdiction, damages, DOJ authority) for family status violations |
| **Art I §10(a)(4)** — Vital Statistics as Critical Data | "birth, death, marriage" classified as Critical Governance Data with interoperability mandate | Does NOT cover divorce, adoption, parentage records; no inter-Regional verification system |
| **Art I §8(a)-(b)** — Freedom of Movement | Right to travel, establish residence, seek employment; no discrimination based on Region of origin | Protects mobility rights generally; silent on whether family status survives relocation |

### 2.2 Provision that ENABLES the vulnerability

| Provision | How it enables the attack vector |
|---|---|
| **Art II §1(e)(2)(iv)** — Family Law Exclusive Domain | "Family law (marriage, divorce, custody, adoption)" is Exclusive Regional Domain. A Region could argue that its exclusive authority over family law includes the power to define what constitutes a valid marriage or adoption — and therefore to refuse recognition of arrangements that don't meet its definition. The domain allocation is about *creating* family law, but the text doesn't explicitly say it excludes *refusing recognition*. |

### 2.3 Provision that creates TENSION

| Provision | Tension |
|---|---|
| **Art I §9(b) vs. Art II §1(e)(2)(iv)** | §9(b) mandates recognition of "marriages... established under any jurisdiction's law." §1(e)(2)(iv) gives Regions "exclusive" authority over family law. A Region could argue its exclusive domain includes defining what counts as a "marriage" for purposes of its own law, and that §9(b) only requires recognizing the *fact* of the legal status without requiring honor of all its *incidents*. This is the core tension: recognition of status vs. recognition of incidents. |
| **Art I §9(e) scope** | §9(e) prohibits refusal based on "religious or moral objection." This covers the most likely attack vector (ideological opposition to same-sex marriage, interfaith marriage). But a sophisticated Region could construct a non-religious, non-moral basis — e.g., "public policy" grounds, "child welfare" rationale for refusing adoption recognition, or "procedural irregularity" claims. |

## 3. Proposed Placement

### Primary option: Amend Art I §9(b) and add new subsections to Art I §9

- Art I §9 is the natural home — §9(b) already mandates recognition of marriages, divorces, adoptions
- Expand §9(b) to include civil unions, domestic partnerships, parentage, surrogacy
- Add subsections for full incidents, conflict of laws, children's protection, anti-discrimination, Exclusive Domain limitation, and enforcement
- Keeps all recognition provisions consolidated in §9

### Alternative A: New Art III-RF §8 (as proposed by Gap 199)

- Pro: Frames family status as a rights floor, emphasizing the individual liberty dimension
- Con: Separates family status recognition from the existing §9(b) framework — creates parallel and potentially conflicting provisions
- Con: Art III-RF currently has Sections 1-7; §8 would be an extension, but the substance is about *inter-Regional recognition*, not *individual rights floors*

### Alternative B: Amend Art II §1(e)(2)(iv) to explicitly limit the Exclusive Domain

- Pro: Addresses the enabling provision directly
- Con: Better to solve through §9 (which already mandates recognition) than by carving up the Exclusive Domain

### Recommendation: Amend Art I §9(b) + add §9(v)-(aa), six new subsections

Extends the Legal Status Recognition provision with expanded enumeration, full incidents, conflict of laws, children's protection, anti-discrimination, Exclusive Domain limitation, and enforcement. Keeps all recognition provisions in §9 alongside the professional credential provisions.

## 4. Design Questions

### D1. Is Art I §9(b) already sufficient for basic recognition?

§9(b) mandates recognition of "marriages, divorces, adoptions, name changes." Combined with §9(e) (no religious/moral refusal), this covers the most direct attack. Options:

- (A) Sufficient for recognition — but the "full incidents" and enforcement gaps need new subsections
- (B) Insufficient — §9(b) needs expanded enumeration (civil unions, parentage, surrogacy) and explicit "full incidents" language
- (C) The §9(b)/§9(e) combination is strong enough that only anti-gaming and enforcement need addition

### D2. Should the enumeration in §9(b) be expanded?

§9(b) lists marriages, divorces, adoptions, name changes. The Gap 199 proposal adds civil unions, domestic partnerships, and parentage. Options:

- (A) Expand §9(b) to add: civil unions, domestic partnerships, parentage determinations, surrogacy agreements, custody orders, guardianship orders
- (B) Add a catch-all: "and all other legal determinations of family status or relationship"
- (C) Leave §9(b) as-is — "marriages" broadly construed covers civil unions and domestic partnerships; "adoptions" covers parentage determinations
- (D) Both: expand the enumeration AND add catch-all to prevent future gaps

### D3. What does "recognition" require — status only, or full incidents?

The core gap: does §9(b) "recognition" mean a Region must acknowledge the legal *fact* of a marriage, or must it honor all the *legal incidents* (benefits, visitation, inheritance, custody rights)? Options:

- (A) Explicit "full incidents" clause: recognition includes all rights, benefits, obligations, and privileges attendant to the status under federal law and under the law of the recognizing Region
- (B) Define minimum incidents: enumerate specific incidents that must be honored (spousal benefits, hospital visitation, inheritance, parental rights, testimonial privilege, tax status)
- (C) Status-plus-incidents: Region must recognize both the status AND extend to it the same incidents it extends to domestically-created statuses of the same type
- (D) Leave to courts — "recognition" will be interpreted to include incidents

### D4. How to handle the Exclusive Domain tension?

Art II §1(e)(2)(iv) gives Regions "exclusive" authority over family law. Options:

- (A) Add explicit limitation to §9: "The Exclusive Regional Domain over family law applies to the creation and modification of family law for the Region's own residents; it does not include authority to refuse recognition of family status validly established in other Regions"
- (B) Add cross-reference to Art II §1(e)(2)(iv): "Nothing in the Exclusive Regional Domain over family law shall be construed to override the recognition obligations of this Section"
- (C) No amendment needed — §9(b) already overrides Exclusive Domain for recognition purposes; the two provisions operate in separate spheres
- (D) Amend Art II §1(e)(2)(iv) directly to add "subject to the recognition obligations of Article I, Section 9"

### D5. Should anti-discrimination enumerate protected characteristics?

§9(e) bars "religious or moral objection" but doesn't enumerate sex, sexual orientation, race, etc. Options:

- (A) Add explicit enumeration: "regardless of the sex, gender, sexual orientation, race, ethnicity, religion, national origin, age, disability, or any other characteristic of the parties"
- (B) Cross-reference federal civil rights law: "characteristics that would be prohibited grounds for discrimination under federal civil rights law"
- (C) Add a functional test: "A Region may not refuse recognition of family status based on characteristics of the parties that would not invalidate the status under the law of the establishing Region"
- (D) §9(e) is sufficient — "religious or moral objection" covers the most likely attack vectors

### D6. How to handle the conflict-of-laws framework?

When a family moves between Regions with different family law:

- (A) Validity governed by establishing Region; incidents governed by residence Region (but cannot extinguish fundamental relationship) — this is the proposal's approach
- (B) Validity AND incidents governed by establishing Region — portable but potentially creates perpetual choice-of-law
- (C) Validity governed by establishing Region; incidents governed by residence Region without limitation — respects Regional autonomy but enables the "selective recognition" attack
- (D) Federal uniform framework for interstate family status — preempts Regional variation entirely

### D7. Should children receive special protection?

The proposal includes: "No child shall be rendered a legal orphan or lose a legal parent due to interstate relocation." Options:

- (A) Yes — special protection clause for parent-child relationships, including: no legal orphaning, parent-child relationship travels with relocation, termination only through due process proceedings
- (B) Yes, with stronger language: parent-child relationship established by birth, adoption, parentage determination, or court order is constitutionally protected against Regional non-recognition
- (C) Not needed separately — if full incidents are required, parental rights are included
- (D) Yes, and extend to guardianship and foster care placements that cross Regional borders

### D8. Should there be an emergency relief mechanism?

A family that moves and is immediately denied status recognition faces urgent harm (denied hospital access, child custody). Options:

- (A) Expedited federal court relief within 48 hours upon showing valid out-of-Region civil status
- (B) Automatic provisional recognition upon presentation of valid vital records, pending any challenge
- (C) TRO standard: any federal court may issue immediate relief upon showing valid status and imminent harm
- (D) Combination: automatic provisional recognition PLUS expedited judicial remedy if challenged

### D9. Should selective recognition be explicitly prohibited?

The "cherry-picking" vector: recognize marriage for obligations (debt) but not benefits (inheritance). Options:

- (A) Explicit prohibition: "A Region may not selectively recognize civil status for some legal purposes while denying recognition for others"
- (B) Implicit in "full incidents" — if all incidents must be honored, selective recognition is impossible
- (C) Explicit prohibition needed separately — "full incidents" addresses what must be recognized; "selective recognition" addresses the gaming vector of partial recognition
- (D) Add anti-circumvention: selective recognition, re-characterization (calling a marriage a "civil arrangement"), and functional non-recognition are all prohibited

### D10. Should vital records coordination be constitutionally mandated?

The proposal includes a federal vital records database. Options:

- (A) Constitutional mandate: Congress shall establish a federal vital records database with standardized formats, electronic verification, and privacy protections
- (B) Rely on Art I §10 — vital statistics are already Critical Governance Data with interoperability mandates; expand to cover divorce, adoption, parentage
- (C) Constitutional mandate for interoperability; statutory implementation for specific systems
- (D) Not needed constitutionally — implementing legislation under §9(f) can establish coordination

### D11. Should retroactive recognition be explicit?

The proposal says civil status established before ratification receives the same recognition. Options:

- (A) Explicit retroactivity: "Civil status established prior to the effective date of this section shall receive the same recognition"
- (B) Not needed — §9(b) already says "established under any jurisdiction's law" without temporal limitation
- (C) Explicit retroactivity plus anti-nullification: no Region may retroactively nullify a previously recognized family status

### D12. What enforcement mechanisms?

§9(f) provides self-execution but no specific remedies. Options:

- (A) Full enforcement package: private right of action in federal court, monetary damages, attorney fees, DOJ authority for systematic violations
- (B) Cross-reference §9(o) expedited judicial review (60 days, Constitutional Court) — extend to family status
- (C) Cross-reference Art I §14 enforcement for retaliatory actions against families exercising recognition rights
- (D) Combination: §9(o)-style expedited review PLUS private right of action PLUS DOJ authority

### D13. Should the framework address multi-Regional families?

Families where members reside in different Regions (e.g., military deployment, commuter marriages, shared custody across borders):

- (A) Explicit provision: family status is recognized in all Regions where any family member resides, regardless of which Region established the status
- (B) Not needed — §9(b) recognition is universal; residence is irrelevant
- (C) Address specific multi-Regional scenarios: custody orders enforceable across borders, child support orders enforceable across borders, spousal support orders enforceable across borders

## 5. Gaming Vectors

### From the proposal (5)

| # | Vector | Mechanism |
|---|---|---|
| G1 | The "Traditional Marriage" Attack | Region defines marriage as specific religious/cultural form; refuses recognition of same-sex, interfaith, or civil ceremonies |
| G2 | The "Adoption Nullification" | Region requires adoptive parents meet specific criteria; refuses recognition of single-parent, same-sex parent, or international adoptions |
| G3 | The "Parentage Rejection" | Region refuses recognition of surrogacy agreements or assisted reproduction parentage; intended parents lose legal rights |
| G4 | The "Divorce Non-Recognition" | Region refuses to recognize divorces from other Regions; remarriage becomes bigamy; custody arrangements void |
| G5 | The "Selective Recognition" | Region recognizes marriage for liability/debt but denies benefits/rights; cherry-picks obligations without protections |

### Additional gaming vectors (7)

| # | Vector | Mechanism |
|---|---|---|
| G6 | The "Re-Characterization" | Region "recognizes" the marriage but re-characterizes it as a "civil arrangement" or "domestic contract" with fewer legal incidents; technically not refusal, but functional downgrade |
| G7 | The "Public Policy" Exception | Region claims a "public policy" basis for non-recognition that is neither religious nor moral — e.g., "child welfare" for refusing adoption recognition, "public order" for refusing marriage recognition; circumvents §9(e) |
| G8 | The "Procedural Challenge" | Region demands original vital records, authenticated and apostilled, in specific formats, translated by certified translators — technical compliance with recognition but practical impossibility for most families |
| G9 | The "Waiting Period" | Region "recognizes" the status but imposes a 6-12 month "registration period" before extending incidents; family lives in legal limbo during processing |
| G10 | The "Third-Party Delegation" | Region delegates family law administration to religious courts or private institutions that refuse recognition; Region claims it cannot override "private" religious authority |
| G11 | The "Custody Jurisdiction Grab" | Upon family's relocation, Region asserts jurisdiction over custody and modifies custody order to reflect its own family law preferences — e.g., removing one parent's rights |
| G12 | The "Retroactive Invalidity" | Region passes law retroactively defining certain family structures as invalid; argues §9(b) only covers status "validly established" and its new law renders the status invalid retrospectively |

## 6. Verification Questions

### V1. Does the new text close the "full incidents" gap?

Art I §9(b) says "recognized." The new text must make clear that recognition means honoring all legal incidents — benefits, visitation, inheritance, custody, testimonial privilege, tax status. A Region cannot say "we recognize your marriage" while denying spousal benefits.

### V2. Does the new text address the Exclusive Domain tension?

Art II §1(e)(2)(iv) gives Regions "exclusive" authority over family law. The new text must explicitly state that this domain covers *creation* of family law, not *refusal of recognition* of other Regions' family law determinations. Without this, the Exclusive Domain argument remains available.

### V3. Does the new text protect children from status dissolution?

The adoption and parentage attack vectors are the most severe — a child can lose a legal parent by crossing a Regional border. The new text must contain specific, enforceable protection for parent-child relationships.

### V4. Does the new text prevent the "re-characterization" gaming vector?

A Region that "recognizes" a marriage but re-characterizes it as a lesser legal category is functionally denying recognition. The new text must prohibit functional non-recognition through re-characterization.

### V5. Does the new text provide emergency relief?

A family denied status recognition faces immediate harm (denied hospital access, custody challenges). The new text must provide a mechanism for rapid relief — either automatic provisional recognition or expedited judicial remedy.

---

## 7. Draft Text Direction

The amendments should:

1. **Amend Art I §9(b)** to expand enumeration: add civil unions, domestic partnerships, parentage determinations, surrogacy agreements, custody orders, guardianship orders; add catch-all for "all other legal determinations of family status or relationship"
2. **Add §9(v) — Full Incidents of Recognition** — recognition includes all rights, benefits, obligations, and privileges; enumerate minimum incidents (spousal benefits, inheritance, visitation, parental rights, testimonial privilege, tax status); prohibit selective recognition and re-characterization
3. **Add §9(w) — Children's Status Protection** — parent-child relationship specially protected; no legal orphaning; relationship travels with relocation; termination only through due process; custody and child support orders enforceable across borders
4. **Add §9(x) — Conflict of Laws** — validity governed by establishing Region; incidents governed by residence Region but cannot extinguish fundamental relationship; modifications governed by Region with jurisdiction
5. **Add §9(y) — Anti-Discrimination** — recognition applies regardless of sex, gender, sexual orientation, race, ethnicity, religion, national origin, or any other characteristic; cross-reference federal civil rights law
6. **Add §9(z) — Exclusive Domain Limitation** — Regional Exclusive Domain over family law covers creation and modification of family law; does NOT include authority to refuse recognition of status validly established in other Regions
7. **Add §9(aa) — Enforcement and Emergency Relief** — automatic provisional recognition upon presentation of valid vital records; expedited federal court relief within 48 hours; private right of action with damages and fees; DOJ authority for systematic violations
8. **Expand Art I §10(a)(4)** — add divorce, adoption, parentage to vital statistics classification; mandate inter-Regional verification system
9. **Preserve §9(e)** — existing "religious or moral objection" prohibition remains as base layer; new anti-discrimination clause provides comprehensive protection
