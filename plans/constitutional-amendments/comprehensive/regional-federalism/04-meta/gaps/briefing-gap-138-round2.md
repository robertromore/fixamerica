# Gap 138 -- Round 2 Validation Briefing

*Generated 2026-02-19 for Round 2 review. Both reviewers' Round 1 findings have been verified against source files, design decisions have been made, and revised constitutional text is ready for validation.*

---

## Round 1 Summary

### What Round 1 Found

Two independent reviewers identified the following critical issues in the original Gap 138 proposal:

1. **Art I Section 10(hh)-(ii) already contains a partial anti-double-tax framework** for remote workers, including a credit and rate cap. The original briefing missed this, raising overlap from ~12-15% to ~35-40%. (Both reviewers identified; verified against `01-regional-structure.md` lines 2380-2391.)

2. **The "Inter-Regional Fiscal Court" is a phantom institution** -- referenced in Art I Section 10(ii) and Art X Section 14(b) but never constitutionally established. No composition, appointment, or jurisdiction clause exists. (Reviewer A identified; verified -- zero results in crosswalk, only 2 references in entire constitution.)

3. **Enforcement was under-specified.** The original proposal said only "automatic equalization transfer adjustment" with no formula, duration, floor, or cap. Existing enforcement models (e.g., predatory subsidy at Art X Section 3(v)) specify amount, duration (3 years), and cap (200% annualized). (Both reviewers; verified at `04-fiscal-system.md` line 278.)

4. **Tax label gaming is a real vector.** "All forms of income taxation" would not catch gross receipts taxes, occupational privilege fees, or parafiscal levies structured to fall on earned income. (Both reviewers.)

5. **Forum architecture conflict.** ARB has exclusive initial jurisdiction for power-allocation disputes and prohibits parallel proceedings (`02-powers-and-rights.md` lines 862, 870). Proposed IFC role needed to be deconflicted. (Reviewer A.)

### Design Decisions Made

| ID | Decision | Selection |
|----|----------|-----------|
| D1 | Placement | New Art X Section 22 (standalone) |
| D2 | Credit mechanism | Source-first model with explicit Residence Region top-up |
| D3 | Rate cap | Higher of the two Regions' rates |
| D4 | Worker scope | All workers with income taxable in more than one Region |
| D5 | Tax types | Functional definition: any compulsory levy on earned income regardless of label |
| D6 | Dispute forum | IFC for technical determinations, ARB for enforcement/review |
| D7 | Enforcement | Graduated: 30-day cure -> 150% equalization adjustment -> ARB intervention with personal liability |
| D8 | Art I Section 10(hh)-(ii) | Repeal and migrate; leave forward reference; retain Section 10(ff), (gg), renumbered (jj)->(ii) |
| D9 | Phantom court | Replace all "Inter-Regional Fiscal Court" references with IFC |
| D10 | Cash-flow timing | Constitutional provisional credit at withholding; annual true-up delegated to implementing legislation |

### Coordinator's Round 1 Refinements

After verifying all reviewer claims, the coordinator (with codebase access) identified 6 additional issues and incorporated fixes:

- **M1:** Added explicit Residence Region top-up clause so bedroom communities can collect the rate differential
- **M2:** Migrated Section 10(ii) multi-Region apportionment functionality to Section 22(g), assigned to IFC
- **M3:** Quantified enforcement: 30-day cure, 150% for up to 3 years, Section 3-A floor preserved, personal liability after 3 strikes in 5 years
- **L1:** Retained bilateral treaty framework from original Part 3 as optional mechanism
- **L2:** Added explicit pass-through entity coverage (S-Corps, LLCs, partnerships)
- **L3:** Scoped Art I repeal to only Section 10(hh) and (ii); retained (ff), (gg), and (jj)

---

## Revised Constitutional Text for Validation

### Article X, Section 22: Protection of Cross-Regional Labor Mobility

*Resolves Gap 138. Consolidates and supersedes Art I Section 10(hh)-(ii).*

#### Source-First Taxation and Mandatory Credit

**(a) Primary Taxing Jurisdiction.** The Region in which labor is physically performed, or in the case of remote work, the Region in which the worker is physically present while performing the labor, shall have the primary right to tax income derived from that labor ("Source Region").

**(b) Residence Region Top-Up.** The Region of the worker's tax residence as determined under Article I, Section 10(ff) ("Residence Region") may impose its own tax on income earned in another Region, but shall provide a dollar-for-dollar credit against that tax for any tax, fee, or compulsory levy on earned income paid to the Source Region on the same income. If the Residence Region's rate exceeds the Source Region's rate, the worker owes the Residence Region only the difference. If the Residence Region's rate is equal to or lower than the Source Region's rate, the Residence Region may not collect additional tax on that income.

**(c) Aggregate Rate Cap.** In no case shall the aggregate effective tax rate imposed on a cross-Regional worker by all Regions combined exceed the higher of the applicable rates of the Source Region and the Residence Region.

**(d) Provisional Credit.** The credit under subsection (b) shall be applied provisionally at the time of tax withholding or estimated payment to ensure neutrality in worker cash flow. No worker may be required to pay the full tax to both Regions and await a refund. The Independent Fiscal Council shall establish uniform procedures for provisional withholding coordination between Regions within two (2) years of ratification; annual true-up shall be provided by implementing legislation.

#### Scope

**(e) Functional Definition of Covered Tax.** This Section applies to any compulsory levy predicated on the pursuit of labor or the generation of earned income, regardless of statutory label. "Covered tax" includes income taxes, payroll taxes, professional privilege fees, occupational licensing premiums, gross receipts taxes on individual earners, and any other assessment whose incidence falls on the worker's earned income.

**(f) Covered Workers.** This Section protects any natural person who owes or may owe tax on earned income to more than one Region, including:

- (1) workers who physically commute across Regional boundaries;
- (2) workers who perform remote work while physically present in a Region other than the employer's or client's Region;
- (3) workers who earn income from multiple Regions through multi-site employment, consulting, or contracting;
- (4) owners of pass-through entities (including S-corporations, partnerships, and limited liability companies) to the extent their distributive share constitutes earned income for services personally performed.

#### Apportionment

**(g) Multi-Regional Income Apportionment.** When a worker earns income in three or more Regions, the Independent Fiscal Council shall promulgate and maintain uniform rules for apportioning income among Regions. These rules shall:

- (1) prevent both double taxation and tax avoidance through artificial arrangements;
- (2) apportion income based on the proportion of working days or hours physically spent in each Region, unless an alternative allocation is agreed by bilateral treaty under subsection (l);
- (3) apply to individuals who maintain genuine residences in multiple Regions, earn income from sources in multiple Regions, or operate a business with substantial activities in multiple Regions.

IFC apportionment rules are binding on all Regions. Disputes over apportionment are resolved under subsection (h).

#### Dispute Resolution and Enforcement

**(h) IFC Technical Arbitration.** The Independent Fiscal Council shall serve as the exclusive technical arbitrator for disputes regarding:

- (1) apportionment of income among Regions under subsection (g);
- (2) classification of a levy as a "covered tax" under subsection (e);
- (3) calculation of credits under subsection (b); and
- (4) determination of primary taxing jurisdiction under subsection (a).

Workers, employers, and Regions may petition the IFC for resolution. IFC determinations are binding on all parties.

**(i) ARB Enforcement and Review.** Purely legal challenges regarding the scope or constitutionality of this Section, and enforcement actions against non-compliant Regions, shall be within the jurisdiction of the Allocation Review Board:

- (1) A Region that fails to apply credits as directed by the IFC within sixty (60) days of a binding determination shall be subject to graduated enforcement;
- (2) The ARB shall hear enforcement petitions on an expedited basis with a determination within ninety (90) days.

**(j) Graduated Enforcement.**

- (1) **Stage 1: IFC Finding and Cure Period.** Upon finding that a Region has failed to comply with an IFC determination under subsection (h), the IFC shall issue a Non-Compliance Finding and provide the Region thirty (30) days to cure.
- (2) **Stage 2: Equalization Adjustment.** If the Region fails to cure within thirty (30) days, the Region's equalization transfers shall be reduced by one hundred fifty percent (150%) of the disputed tax amount, for a period not exceeding three (3) years from the date of the Finding. The adjustment shall not reduce equalization below the Section 3-A floor.
- (3) **Stage 3: ARB Intervention.** If a Region accumulates three or more Non-Compliance Findings within any five (5) year period, the ARB may:
    - (A) assume direct administration of the Region's cross-Regional withholding and credit systems;
    - (B) impose personal liability on Regional tax officials who willfully directed or substantially participated in the non-compliance; and
    - (C) order the Region to reimburse affected workers for excess taxes paid, with interest at the Federal Funds Rate plus two percent.

**(k) Anti-Circumvention.**

- (1) No Region may relabel, restructure, or reclassify a tax on earned income to evade the credit requirement of this Section. The IFC shall look through the statutory label to the economic substance of any levy.
- (2) No Region may shift filing deadlines, tax years, or withholding schedules for the purpose of preventing timely credit calculation. The IFC may establish uniform filing coordination requirements.
- (3) No Region may selectively deny, delay, or condition credits based on the income level, occupation, or Region of origin of the worker. Credits under subsection (b) are mandatory and non-discretionary.

#### Bilateral Agreements

**(l) Bilateral Tax Treaties.** Regions may negotiate bilateral tax treaties that allocate taxing rights differently than the default rules of this Section:

- (1) Bilateral treaties must be registered with the IFC within thirty (30) days of execution;
- (2) No bilateral treaty may impose an aggregate effective rate on cross-Regional workers exceeding the cap of subsection (c);
- (3) The IFC shall publish model tax treaty provisions to facilitate negotiation;
- (4) Bilateral treaties supersede the default apportionment rules of subsection (g) as between the contracting Regions but do not affect the rights of workers under subsections (b) and (c).

#### Savings Clauses

**(m) Non-Coercion Savings Clause.** Enforcement of the credit requirements of this Section by the IFC or the ARB does not constitute federal coercion under Section 4 of this Article. The protections of this Section are self-executing constitutional rights of workers, not conditional spending requirements imposed on Regions.

**(n) Interaction with Existing Provisions.** This Section supplements Section 3(q) (Residence and Domicile Standards) and Section 11-A (Prohibition on Predatory Tax Exportation) of this Article. Tax residency shall continue to be determined under the standards of Article I, Section 10(ff)-(gg). Nothing in this Section affects the Predatory Tax Exportation ceiling of Section 11-A or the corporate tax apportionment standards of Section 3(r).

---

## Conforming Amendments

### 1. Article I, Section 10 -- Repeal Section 10(hh)-(ii)

**Current text being replaced:**

> (hh) **Economic Nexus for Services.** A person who is tax-resident in one Region but performs substantial remote work for employers or clients located in another Region shall:
>
> - (1) owe income tax to their Region of tax residency on all income;
> - (2) be entitled to a credit against their home Region tax for any withholding or income tax paid to the work-source Region, up to the amount of home Region tax on that income; and
> - (3) not be subject to double taxation through cumulative Regional income taxes exceeding the higher of the two Regions' rates.
>
> (ii) **Apportionment for Multi-Regional Activity.** The Inter-Regional Fiscal Court shall promulgate uniform rules for apportioning income among Regions when an individual:
>
> - (1) maintains genuine residences in multiple Regions;
> - (2) earns income from sources in multiple Regions; or
> - (3) operates a business with substantial activities in multiple Regions.
> These rules shall prevent both double taxation and tax avoidance through artificial arrangements.

**Replacement text:**

> (hh) **Cross-Regional Taxation.** For protection against double taxation of cross-Regional workers, including source-first taxation, mandatory reciprocal credits, income apportionment, and dispute resolution, see Article X, Section 22.

**Retained without modification:** Section 10(ff) (Primary Tax Residency Determination), Section 10(gg) (Prohibition on Tax Residency Arbitrage).

**Renumbered:** Existing Section 10(jj) (Regional Benefit Arbitrage) becomes Section 10(ii).

### 2. Article X, Section 14(b) -- Replace Phantom Institution

**Current:** "The Inter-Regional Fiscal Court shall establish a Fiscal Adequacy Review Board..."

**Replacement:** "The Independent Fiscal Council shall establish a Fiscal Adequacy Review Board..."

### 3. Article X, Section 5(c) -- Add IFC Duty

Add after existing item (6):

> (7) promulgate and maintain uniform rules for cross-Regional income apportionment under Section 22(g), and serve as exclusive technical arbitrator for cross-Regional tax disputes under Section 22(h).

### 4. Article X, Section 4(i) -- Non-Coercion Clarification

Add after existing item (3):

> (4) enforcement of the cross-Regional labor mobility protections of Section 22, which constitute self-executing constitutional rights rather than conditional spending requirements.

---

## What Reviewers Should Verify in Round 2

### Scenario Testing

Please verify the source-first + top-up mechanism produces the correct result in each scenario:

**Scenario 1: Source Region rate higher (40%) than Residence Region rate (30%)**
- Worker pays 40% to Source Region
- Residence Region credits 40%, which exceeds its own 30% rate
- Residence Region collects $0 additional
- Worker's effective rate: 40% (correct -- higher of two rates)

**Scenario 2: Residence Region rate higher (40%) than Source Region rate (30%)**
- Worker pays 30% to Source Region
- Residence Region credits 30% against its 40% rate
- Residence Region collects 10% differential
- Worker's effective rate: 40% (correct -- higher of two rates)

**Scenario 3: Equal rates (35% each)**
- Worker pays 35% to Source Region
- Residence Region credits 35%, which equals its own rate
- Residence Region collects $0 additional
- Worker's effective rate: 35% (correct)

**Scenario 4: Three-Region worker (home in A at 35%, works in B at 30% and C at 40%)**
- IFC apportions income: 60% to B, 40% to C (by working days)
- Worker pays 30% on 60% of income to B, 40% on 40% of income to C
- Residence Region A credits B's tax (30%) and C's tax (40%) against its 35% rate
- For B-sourced income: A collects 5% differential (35% - 30%)
- For C-sourced income: A collects $0 (C's 40% > A's 35%)
- Worker's effective rate: weighted average of 35% and 40% = 37% (correct -- each portion at higher of two rates)

### Terminology Verification

1. Does "Source Region" conflict with any existing defined term?
2. Does "Residence Region" conflict with Art I Section 10(ff) "primary tax residency" terminology? (It should align -- Section 22(b) explicitly cross-references Section 10(ff).)
3. Does "covered tax" in Section 22(e) conflict with any existing tax-type definitions in Art X?

### Cross-Reference Verification

1. Does the Section 10(jj) -> Section 10(ii) renumbering break any existing cross-references to Section 10(jj)?
2. Does the Section 4(i)(4) addition interact correctly with the existing savings clause structure at Section 4(i)(1)-(3)?
3. Does the Section 5(c)(7) addition fit the existing enumerated duties format?

### Enforcement Proportionality

1. Is 150% of the disputed amount sufficient deterrence, or could a Region find it revenue-positive to non-comply?
2. Is the 30-day cure period adequate for administrative correction?
3. Does the Section 3-A floor protection create a loophole where a Region already at the equalization floor has no enforcement exposure?
4. Is the 3-strikes-in-5-years threshold for Stage 3 too lenient?

### Gaming Vectors (Round 2)

1. **Base mismatch attack**: Source Region defines "income" broadly (including fringe benefits, stock options) while Residence Region defines it narrowly. Worker pays high Source tax but gets only partial Residence credit because the Residence Region doesn't recognize all income components. Does Section 22(e) "functional definition" resolve this, or does "earned income" need explicit definition?

2. **Local levy passthrough**: A State within a Region imposes an income-like tax not subject to the credit. Does "any compulsory levy" in Section 22(e) cover State-level and local-level taxes, or only Regional taxes?

3. **Provisional credit manipulation**: Source Region withholds at an inflated rate, creating a large provisional credit that is later refunded to the worker but has already offset the Residence Region's revenue. Does Section 22(d) address this?

4. **Treaty carve-out abuse**: Two allied Regions negotiate a bilateral treaty under Section 22(l) that disadvantages workers from a third Region passing through. Does Section 22(l)(2) (rate cap) and Section 22(l)(4) (worker rights preserved) close this?

### Silent Deletion Check

Verify that migrating Section 10(hh)-(ii) to Section 22 does not silently delete any feature:

| Feature in Section 10(hh) | Present in Section 22? | Location |
|---|---|---|
| Credit for remote workers | Yes -- expanded to all workers | Section 22(b), (f)(2) |
| Rate cap at higher of two rates | Yes | Section 22(c) |
| Scope: "substantial remote work" | Expanded: all multi-Region workers | Section 22(f) |

| Feature in Section 10(ii) | Present in Section 22? | Location |
|---|---|---|
| Uniform apportionment rules | Yes -- assigned to IFC | Section 22(g) |
| Multiple residences covered | Yes | Section 22(g)(3) |
| Multiple income sources covered | Yes | Section 22(g)(3) |
| Multi-Region businesses covered | Yes | Section 22(g)(3) |
| Anti-avoidance purpose | Yes | Section 22(g)(1) |
| Inter-Regional Fiscal Court reference | Replaced with IFC (D9) | Section 22(g), (h) |

---

## Instructions for Round 2 Reviewer

Please produce:

1. **Findings** -- Verify the revised text against the scenarios, terminology, cross-references, enforcement, and gaming vectors listed above. Flag any new issues introduced by the revisions or any Round 1 issues that remain unaddressed.

2. **Confirm or dispute** the silent deletion check above.

3. **Assessment** -- Is this text ready for integration, or does it require a Round 3?

**Severity levels:**

- **High** -- Contradicts existing constitutional text or creates a new critical vulnerability
- **Medium** -- Ambiguous, undefined, or potentially conflicting; needs clarification
- **Low** -- Minor gaming risk or style issue
