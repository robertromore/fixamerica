# Single-Topic Amendments

## Purpose

This folder contains **standalone constitutional amendments** designed to be adoptable **independently** of the Regional Federalism restructuring. Each amendment addresses a specific area of constitutional reform and can succeed or fail on its own merits.

## Architectural Role

The single-topic amendments serve a critical function in the overall project architecture:

```text
┌─────────────────────────────────────────────────────────────────┐
│                    ADOPTION PATHWAYS                            │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│   PATHWAY A: Full Regional Federalism                          │
│   ─────────────────────────────────────                        │
│   RF Core Constitution + Single-Topic Amendments + RF Supplements│
│                                                                 │
│   PATHWAY B: Incremental Reform                                │
│   ─────────────────────────────────                            │
│   Any Single-Topic Amendment(s) alone                          │
│   (Works with existing federal/state structure)                │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

### Why This Matters

1. **Reduced political barrier**: Individual amendments can be adopted without requiring agreement on the entire RF restructuring
2. **Modular testing**: Reforms can be validated individually before full integration
3. **Fallback pathway**: If RF fails politically, individual reforms can still succeed
4. **Clear dependencies**: One-way dependency—RF can rely on these; these don't require RF

## Document Authority

Per the [Document Hierarchy](../../DOCUMENT-HIERARCHY.md):

- **Single-topic amendments** are **Level 1: Authoritative Constitutional Text**
- They are co-equal with `/02-design/constitution/` for their respective topics
- The RF Core Constitution files contain **supplements** that depend on these amendments

## Relationship to RF Supplements

Several RF Constitution files explicitly depend on single-topic amendments:

| RF Supplement | Depends On | Relationship |
|--------------|------------|--------------|
| `09-judiciary.md` | Judicial Reform | "Presumes adoption" of standalone; adds Regional courts tier |
| `10-armed-forces.md` | Military Civilian Control | "Presumes adoption" of standalone; adds Regional integration |
| `11-emergency-powers.md` | Emergency Powers Reform | "Presumes adoption" of standalone; adds Regional triggers |

These supplements contain **only the region-dependent provisions**. The core reforms are in the single-topic amendments.

## Amendment Status

All 8 standalone amendments are now fully drafted:

| File | Article | Key Provisions |
|------|---------|----------------|
| `election-reform.md` | VII | RCV, popular vote, independent commissions, campaign finance |
| `impeachment-reform.md` | VIII | Grounds enumeration, timelines, expedited procedures |
| `lobbying-reform.md` | IX | Disclosure, 4-year revolving door, foreign lobbying |
| `judicial-reform.md` | XIV | 18-year terms, mandatory jurisdiction, time limits |
| `federal-reserve-reform.md` | XV | Independence, dual mandate, CBDC limits |
| `cyber-defense.md` | XVI | Digital rights, encryption, infrastructure |
| `emergency-powers-reform.md` | XVII | Categories, time limits, restoration mandate |
| `military-civilian-control.md` | XI | Two-key, duty to refuse, counter-key |

### Removed Files

Three placeholder files were removed because they were inherently structure-dependent and did not fit the standalone amendment model:

- `congressional-reform.md` — Legislative structure reforms belong in RF Core (`03-regional-governance.md`)
- `executive-reform.md` — Executive constraints are distributed across Emergency Powers (XVII), Military Control (XI), and Impeachment (VIII)
- `tax-reform.md` — Fiscal architecture is inherently tied to Regional structure (`04-fiscal-system.md`)

## Cross-References

- **Index**: [00-index.md](00-index.md) — Full amendment list with Article numbers
- **Integration Map**: [Article Crosswalk](../constitution/article-crosswalk.md) — How amendments map to RF Articles
- **Hierarchy**: [Document Hierarchy](../../DOCUMENT-HIERARCHY.md) — Authority levels

---

*This folder is retained as an integral part of the modular constitutional architecture.*
