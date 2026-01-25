# Regional Federalism Document Hierarchy

## Purpose

This document establishes the authoritative sources for the Regional Federalism framework and clarifies relationships between different document types.

**Last Updated:** 2026-01-25

---

## Document Authority Levels

### Level 1: AUTHORITATIVE CONSTITUTIONAL TEXT

#### A. RF Core Constitution

**Location:** `/02-design/constitution/`

These files are the **single source of truth** for Regional Federalism-specific constitutional provisions:

| File | Content |
|------|---------|
| `00-index.md` | Overview and navigation |
| `01-regional-structure.md` | Article I: Regional boundaries, interstate relations |
| `02-powers-and-rights.md` | Articles II-III: Powers allocation, rights floors |
| `03-regional-governance.md` | Articles IV-V: Regional legislatures/executives |
| `04-fiscal-system.md` | Article X: Fiscal architecture, equalization |
| `05-safeguards.md` | Articles XII-XIII: Secession prevention, amendments |
| `07-implementation.md` | Articles XXI-XXII: Default rules |
| `09-judiciary.md` | Article XIV-RF: Regional courts (RF Supplement) |
| `10-armed-forces.md` | Article XI-RF: Regional Guard, Two-Key (RF Supplement) |
| `11-emergency-powers.md` | Article XVII-RF: Emergency authority (RF Supplement) |
| `article-crosswalk.md` | Article number mapping |

**Rule:** All RF-specific constitutional text changes must be made here first.

#### B. Single-Topic Standalone Amendments

**Location:** `/02-design/single-topic/`

These are **standalone constitutional amendments** that can be adopted independently of Regional Federalism:

| File | Article | Content | Status |
|------|---------|---------|--------|
| `election-reform.md` | VII | Electoral system reforms, ranked-choice voting | **Draft** |
| `impeachment-reform.md` | VIII | Grounds enumeration, timelines, expedited procedures | **Draft** |
| `lobbying-reform.md` | IX | Disclosure, revolving door, foreign lobbying, anti-corruption | **Draft** |
| `military-civilian-control.md` | XI | Two-key authorization, duty to refuse, counter-key | **Draft** |
| `judicial-reform.md` | XIV | 18-year terms, mandatory jurisdiction, time limits | **Draft** |
| `federal-reserve-reform.md` | XV | Independence, dual mandate, CBDC limits, emergency authority | **Draft** |
| `cyber-defense.md` | XVI | Digital rights, encryption, infrastructure, election security | **Draft** |
| `emergency-powers-reform.md` | XVII | Categorized emergencies, time limits, restoration mandate | **Draft** |

**Relationship to RF Core:**

- Single-topic amendments are **independent** — they work with or without RF adoption
- RF Supplement files (e.g., `09-judiciary.md`) **depend on** their single-topic counterparts
- One-way dependency: RF relies on these; these don't require RF

**Rule:** Core reforms go in single-topic amendments; region-dependent additions go in RF Supplements.

---

### Level 2: AUTHORITATIVE IMPLEMENTATION ACTS

**Location:** `/05-implementation/`

These files are the **single source of truth** for core implementing legislation:

| File | Content | Status |
|------|---------|--------|
| `01-safeguards-playbook.md` | Non-constitutional risk mitigation | Authoritative |
| `02-transition-act.md` | 5-phase, 48-month transition framework | Authoritative |
| `03-allocation-framework-act.md` | Jurisdictional boundaries, spillover criteria | Authoritative |
| `04-fiscal-equalization-act.md` | Transfer formulas, IFC structure | Authoritative |
| `05-elections-implementation-act.md` | Federal election procedures | Authoritative |

**Rule:** These supersede any similar documents in `/proposals/`.

---

### Level 3: GENERATED OUTPUTS

**Location:** `/05-constitutional-package/`

| File | Content | Generated From |
|------|---------|----------------|
| `00-CONSTITUTIONAL-AMENDMENTS-PACKAGE.md` | Consolidated constitutional text | `/02-design/constitution/` + `/04-meta/gaps/` |

**Rule:** This is a **compiled output**, not a source document. Changes should be made to source files, then this document regenerated.

**Note:** The current version (2026-01-25) was generated from the gap analysis and contains provisions that need to be back-integrated into `/02-design/constitution/`.

---

### Level 4: SUPPLEMENTARY PROPOSALS

**Location:** `/proposals/`

These are **domain-specific statutory drafts** that supplement (not duplicate) the core implementation acts.

**Document Type:** Actual legislative text with sections, subsections, definitions, and enforcement mechanisms.

**Included Categories:**

- `01-foundations/` — Administrative procedure, civil service, data integrity (NOT allocation or transition)
- `02-elections-democracy/` — Campaign finance, civic engagement (NOT core election implementation)
- `03-economy-commerce/` — Trade, antitrust, financial regulation (NOT fiscal equalization)
- `04-social-policy-labor/` — Healthcare, education, housing coordination
- `05-environment-infrastructure/` — Energy, transportation, environment
- `06-security-justice/` — Criminal code, immigration, cybersecurity
- `07-intergovernmental-tools/` — Model agreements, coordination templates
- `08-special-jurisdictions/` — Territories, overseas citizens

**Rule:** Proposals must NOT duplicate content in `/05-implementation/`. Domain proposals implement constitutional provisions in specific policy areas.

**Cross-References:** Key proposals link to related conceptual analyses in `/06-policy-applications/`.

---

### Level 5: CONCEPTUAL POLICY ANALYSES

**Location:** `/06-policy-applications/`

These are **conceptual analyses** explaining how Regional Federalism transforms governance in specific policy domains.

**Document Type:** Essays and white papers answering "How would Regional Federalism change [policy area]?"

**Content:**

- Problem analysis for current federal-state structure
- Design rationale for Regional approach
- Implementation considerations
- Strategic vision

**Relationship to Proposals:** Complementary, not duplicative.

- `/06-policy-applications/` = "Why and How" (conceptual framework)
- `/proposals/` = "What Exactly" (statutory implementation)

**Cross-References:** Each policy application document links to its related statutory proposal(s) in `/proposals/`.

---

### Level 6: ANALYSIS AND META-DOCUMENTS

**Location:** `/03-analysis/`, `/04-meta/`

These are analytical documents that inform but do not constitute authoritative text:

- Stress tests
- Historical failure analysis
- Gap analyses (source for constitutional provisions)
- Reconciliation documents
- Implementation prioritization

---

## Conflict Resolution

When documents conflict, authority follows this order:

1. `/02-design/constitution/` (RF Core constitutional text)
2. `/02-design/single-topic/` (standalone amendments — co-equal with RF Core for their topics)
3. `/05-implementation/` (core implementation acts)
4. `/05-constitutional-package/` (generated output — flag for source update)
5. `/proposals/` (domain supplements)
6. `/04-meta/gaps/` (analytical source material)

**Special Rule for RF Supplements vs. Single-Topic:**

- If a topic has both an RF Supplement (e.g., `09-judiciary.md`) and a single-topic amendment (e.g., `judicial-reform.md`), both are authoritative for their respective scope
- Single-topic = core reform (works with or without RF)
- RF Supplement = region-dependent additions only

**If a conflict is found:**

1. Identify which document should be authoritative per this hierarchy
2. Update the non-authoritative document to match
3. Document the change in CHANGELOG.md

---

## Maintenance Rules

### Adding New Constitutional Provisions

1. Draft in `/04-meta/gaps/` as a gap analysis
2. Review and approve
3. Add to appropriate file in `/02-design/constitution/`
4. Regenerate `/05-constitutional-package/`
5. Update CHANGELOG

### Adding New Implementation Acts

1. If core (affects all Regions): Add to `/05-implementation/`
2. If domain-specific: Add to appropriate `/proposals/` subfolder
3. Ensure no duplication with existing core acts
4. Update CHANGELOG

### Reconciling Conflicts

1. Check this hierarchy document
2. Authoritative source wins
3. Update non-authoritative documents
4. Document in CHANGELOG

---

## Known Integration Tasks

Back-integration from `/05-constitutional-package/` to `/02-design/constitution/` completed 2026-01-25:

- [x] Article I-RF Section 6: Full NITS provisions (from Gaps 67, 75) — added subsections (d)-(aa)
- [x] Article I-RF Section 10: Data sovereignty (from Gap 69) — new section with 23 subsections
- [x] Article I-RF Section 14: Professional credential protection (from Gaps 136, 141) — new section
- [x] Article II-RF Section 5: Full ARB provisions (from Gaps 54, 73) — expanded to 31 subsections (a)-(ee)
- [x] Article X-RF Sections 6-7: Debt discipline, conservatorship (from Gaps 94, 147) — two new sections
- [x] Article XI: Expanded Two-Key, Counter-Key (from Gaps 44, 55) — Sections 10-12 added to single-topic
- [x] Article XIV: Quorum restoration, nominating commissions (from Gaps 81, 101) — Sections 12-14 added to single-topic

RF Supplement compatibility clauses updated to reflect new provisions.

---

## Document History

| Date | Action |
|------|--------|
| 2026-01-25 | Removed 3 orphaned placeholders (congressional, executive, tax reform) — structure-dependent, don't fit standalone model |
| 2026-01-25 | Drafted all 8 mapped single-topic amendments |
| 2026-01-25 | Flattened single-topic folder structure (folders → files) |
| 2026-01-25 | Added single-topic amendments to Level 1; clarified RF Supplement dependencies |
| 2026-01-25 | Created hierarchy document; identified duplicates for removal |
