# Article VII / VII-RF Integration Map

## Consolidated Electoral Systems Structure

**Purpose:** This document reconciles Gap proposals affecting Article VII (Elections) and Article VII-RF (Regional Electoral Provisions) into a coherent structure with coordinated timelines.

**Date:** 2026-01-25
**Status:** Draft for Review

---

## Overview

Three gaps propose amendments to electoral systems with potentially overlapping timelines:

| Gap | Article | Topic | Key Timeline |
|-----|---------|-------|--------------|
| 48 | Article VII | Certification Escrow | 14-28 day judicial review |
| 84 | Article XXII-RF | Referendum Immunity | 30-day immunity period |
| 95 | Article VII-RF | Certification Deadlock | 7-day Regional court window |

**Key Integration Issue:** Gaps 48 and 95 both address certification disputes but with different triggers and timelines. Gap 95's 7-day Regional court window must coordinate with Gap 48's 14-28 day Certification Escrow process.

**Resolution:** Explicit timeline coordination added to Gap 95 (Section 4(t-v))

---

## Integrated Electoral Timeline

### Federal Election Certification Sequence

```
Day 0:  ELECTION DAY
        |
Day 1-7: REGIONAL COURT WINDOW [Gap 95]
        ├── Regional courts have 7 days to resolve any challenges
        ├── No stays may extend beyond 7 days
        └── Failure to resolve → automatic federal jurisdiction transfer
        |
Day 7:  JURISDICTION TRANSFER POINT
        ├── If Regional court resolved: proceed to certification
        ├── If not resolved: National Election Court assumes jurisdiction
        └── All Regional stays vacated by operation of law
        |
Day 7-21: REGIONAL CERTIFICATION WINDOW [Gap 48]
        ├── Regional Authority must: Certify / Refuse / Place in Escrow
        ├── Escrow requires: 1%+ irregularity finding + Integrity Challenge
        └── Auto-certification if no action by Day 21
        |
Day 21: CERTIFICATION DEADLINE
        ├── Results certified (normal path)
        ├── Results in Escrow (challenged path)
        └── Auto-certification (non-response path)
        |
Day 21-35: INTEGRITY CHALLENGE REVIEW [Gap 48]
        ├── National Election Court emergency panel (48 hours)
        ├── Preliminary determination (14 days)
        └── RCV provisional truncation available if needed
        |
Day 35: HARD DEADLINE FOR RCV
        ├── If mathematically insufficient ballots outstanding: proceed
        ├── If mathematically sufficient + no pending proceeding: exclude
        └── Triggers crisis procedures if outcome-determinative
        |
Day 35-49: FINAL DETERMINATION [Gap 48]
        ├── Court issues final determination
        ├── Adjustments applied to escrowed results
        └── RCV re-tabulation if needed
        |
Day 56: FINAL NATIONAL CERTIFICATION
        └── All results finalized; winner declared
```

---

## Coordination Provisions

### Gap 95, Section 4(t-v) — Coordination with Certification Escrow

```
(t) Escrow Tolling
    - 7-day deadline tolled during Escrow period
    - Regional stays remain vacated
    - NEC jurisdiction upon tolling expiration

(u) Jurisdiction Transfer After Escrow
    - Automatic transfer within 48 hours
    - Consolidation of pending proceedings
    - 28-day final determination timeline applies

(v) Unified Timeline
    - Gap 95's 7-day window runs first
    - Gap 48's Escrow process runs after
    - Combined timeline ≤ 56 days
```

---

## Integrated Article VII Structure

### Article VII (Federal Elections)

**Section [X]: Certification Escrow and Integrity Challenges [Gap 48]**

| Subsection | Topic |
|------------|-------|
| (a) | Certification Options (Certify / Refuse / Escrow) |
| (b) | Certification Escrow requirements |
| (c) | Effect of Escrow (provisional inclusion) |
| (d) | National Election Court Review |
| (e) | Frivolous Challenge Deterrence |
| (f) | Final Certification |

**Section [Y]: Provisional Truncation for RCV [Gap 48]**

| Subsection | Topic |
|------------|-------|
| (a) | Mathematical Insufficiency Standard |
| (b) | Calculation methodology |
| (c) | Provisional Elimination |
| (d) | Hard Deadline with Fallback |

---

### Article VII-RF (Regional Electoral Provisions)

**Section 4: Federal Election Certification [Gap 95]**

| Subsection | Topic |
|------------|-------|
| (g) | Federal Jurisdiction Timeline (7-day window) |
| (h) | National Election Court Authority |
| (i) | Regional Court Deadline |
| (j) | Stay Limitation |
| (k) | Pretextual Stay Finding |
| (l) | Pretextual Finding Consequences |
| (m) | Pattern Monitoring |
| (n) | Default Certification |
| (o) | Post-Certification Remedies |
| (p) | Fraud Standard |
| (q) | Election Panel Requirements |
| (r) | Expedited Procedures |
| (s) | Judicial Recusal Standards |
| (t) | **Escrow Tolling** [Coordination with Gap 48] |
| (u) | **Jurisdiction Transfer After Escrow** [Coordination with Gap 48] |
| (v) | **Unified Timeline** [Coordination with Gap 48] |

---

### Article XXII-RF (Amendment Process)

**Section 6: Referendum Immunity Protocol [Gap 84]**

| Subsection | Topic |
|------------|-------|
| (a) | Referendum Immunity Period (30 days before referendum) |
| (b) | Emergency Power Limitations |
| (c) | Communication Protection |
| (d) | Venue Protection |

**Note:** Gap 84 addresses constitutional amendment referendums, not federal elections. No direct timeline coordination needed with Gaps 48/95, but shares National Election Court oversight.

---

## Decision Points and Branching

### At Day 7: Regional Court Resolution

```
Regional Court Resolved?
├── YES → Proceed to Day 7-21 Certification Window
│         └── Regional Authority certifies/refuses/escrows
│
└── NO  → Automatic Federal Jurisdiction Transfer
          ├── Regional stays vacated
          ├── NEC assumes exclusive authority
          └── 14-day NEC resolution timeline
```

### At Day 21: Certification Status

```
Certification Status?
├── CERTIFIED → Final (subject to post-certification remedies)
│
├── ESCROWED → Integrity Challenge Review
│              ├── Day 23: NEC emergency panel
│              ├── Day 35: Preliminary determination
│              └── Day 49: Final determination
│
├── REFUSED → Article VII, Section 4 procedures
│             └── Investigation of specific deficiencies
│
└── NO ACTION → Auto-certification
               └── Results count as certified
```

### At Day 35: RCV Hard Deadline

```
Mathematically Insufficient Ballots?
├── YES → Proceed with RCV tabulation
│         └── Outstanding ballots cannot change outcome
│
└── NO  → Check for pending proceedings
          ├── Proceeding pending → Wait for resolution
          └── No proceeding → Exclude non-certifying Region
                              └── Trigger crisis procedures if outcome-determinative
```

---

## Relationship Between Gaps

| Primary Gap | Related Gap | Relationship |
|-------------|-------------|--------------|
| Gap 48 | Gap 95 | **Coordinated via Section 4(t-v)** — Gap 95's 7-day window runs before Gap 48's escrow |
| Gap 48 | Gap 84 | Parallel protection — different electoral contexts (federal elections vs. referendums) |
| Gap 95 | Gap 84 | Shared oversight — both use National Election Court |
| Gap 95 | Gap 81 | Related — Gap 81 addresses judicial recusal; Gap 95 includes recusal standards |

---

## Summary of Integration Changes

| Change | Location | Description |
|--------|----------|-------------|
| Added coordination provisions | Gap 95, Section 4(t-v) | Escrow tolling, jurisdiction transfer, unified timeline |
| Added relationship note | Gap 48 | Cross-reference to Gap 95 coordination |
| Added relationship note | Gap 95 | Cross-reference to Gap 48 coordination |
| Verified no collision | Gap 84 | Confirmed separate electoral context (referendums) |

---

## Document History

| Date | Action | Author |
|------|--------|--------|
| 2026-01-25 | Initial integration map | Constitutional Design Audit |

