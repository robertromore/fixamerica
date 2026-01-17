# Regional Federal Constitution

## Overview

This directory contains the constitutional text for the Regional Federalism proposal. The constitution has been organized into focused documents for easier navigation.

## Core Regional Constitution

These documents contain provisions that are inherently tied to the regional structure:

| Document | Content |
|----------|---------|
| [01-regional-structure.md](01-regional-structure.md) | Article I: Regions, boundaries, regional constitutions |
| [02-powers-and-rights.md](02-powers-and-rights.md) | Articles II-III: Allocation of powers, rights floors, subsidiarity |
| [03-regional-governance.md](03-regional-governance.md) | Articles IV-V: Regional legislatures and executives |
| [04-fiscal-system.md](04-fiscal-system.md) | Article X: Fiscal architecture and equalization |
| [05-safeguards.md](05-safeguards.md) | Articles XII-XIII: Secession, amendments |
| [06-supremacy.md](06-supremacy.md) | Articles XVIII-XX: Supremacy, transition, non-state entities |
| [07-implementation.md](07-implementation.md) | Articles XXI-XXII: Defaults and definitions |

## Modular Architecture for Companion Reforms

Regional Federalism uses a **modular architecture** for companion reforms:

**Decision Rule:** If a provision relies on regions to function or creates a regional institution, it belongs in this directory. If it could operate with the existing federal/state system, it stays as a standalone amendment in `single-topic/`.

**One-Way Dependencies:** RF can rely on standalone amendments; standalone amendments do NOT rely on RF.

### RF Supplements (Region-Dependent Pieces Only)

These files contain ONLY the region-dependent provisions. They require adoption of the corresponding standalone amendment.

| RF Supplement | Content | Requires |
|---------------|---------|----------|
| [09-judiciary.md](09-judiciary.md) | Regional courts tier, specialized courts (ARB, Water Court) | [Judicial Reform Amendment](../../../../single-topic/judicial-reform/) |
| [10-armed-forces.md](10-armed-forces.md) | Regional Guard Forces, federalization rules | [Military Civilian Control Amendment](../../../../single-topic/military-civilian-control/) |
| [11-emergency-powers.md](11-emergency-powers.md) | Regional Governor declaration authority | [Emergency Powers Reform Amendment](../../../../single-topic/emergency-powers-reform/) |

### Standalone Amendments (No RF Supplement Needed)

These reforms work equally well with the existing federal/state system OR with Regional Federalism. No RF-specific version is needed.

| Topic | Standalone Plan | Notes |
|-------|-----------------|-------|
| Elections | [election-reform/](../../../../single-topic/election-reform/) | National popular vote, certification timelines work same with States or Regions |
| Impeachment | [impeachment-reform/](../../../../single-topic/impeachment-reform/) | General reform, not region-dependent |
| Lobbying/Anti-Corruption | [lobbying-reform/](../../../../single-topic/lobbying-reform/) | General reform, not region-dependent |
| Federal Reserve | [federal-reserve-reform/](../../../../single-topic/federal-reserve-reform/) | Monetary policy reform, not region-dependent |
| Cyber Defense | [cyber-defense/](../../../../single-topic/cyber-defense/) | General reform, not region-dependent |

## How the Pieces Fit Together

**If adopting Regional Federalism:**

1. Adopt the Core Regional Constitution (Articles I-V, X, XII-XIII, XVIII-XXII)
2. Adopt desired standalone amendments from `single-topic/`
3. The RF supplements automatically apply when both RF and the standalone amendment are adopted
4. Substitute "Regional Governors" for "State Governors" in standalone amendments where applicable

**If adopting reforms separately (without RF):**

- Each standalone plan can be adopted independently
- Standalone versions work with existing federal/state structure
- No RF supplements apply

## Implementing Proposals

These proposals provide detailed implementation procedures for constitutional provisions. The constitution establishes principles; these proposals provide operational detail:

| Proposal | Implements | Key Functions |
|----------|------------|---------------|
| [De-Escalation Procedures Act](../../proposals/de-escalation-procedures-act.md) | Article XII, Section 3 | 4-level de-escalation ladder, judicial enforcement, federal intervention |
| [Regional Boundary Review Act](../../proposals/boundary-review-act.md) | Article I, Section 4 | Commission structure, review criteria, referendum procedures |
| [Water Resources Coordination Act](../../proposals/water-resources-coordination-act.md) | Article I, Section 7 | Board structure, equitable apportionment, dispute resolution |
| [D.C. Status Determination Act](../../proposals/dc-status-determination-act.md) | Article XX, Section 1 | Congressional representation, status options, Regional assignment |
| [Interregional Coordination Review Act](../../proposals/interregional-coordination-review-act.md) | Article IV, Section 5 | Senate review criteria, determination procedures, timelines |
| [National Common Market Access Act](../../proposals/national-common-market-access-act.md) | Article I, Section 6 | Transit rights, fee standards, blockade enforcement |
| [Interstate Professional Licensing Act](../../proposals/interstate-professional-licensing-act.md) | Article I, Section 9 | Credential portability, fee limits, supplementary requirements |
| [Transboundary Environmental Protection Act](../../proposals/transboundary-environmental-protection-act.md) | Article I, Section 10 | Pollution prohibition, EPA monitoring, federal enforcement |
| [Interstate Law Enforcement Cooperation Act](../../proposals/interstate-law-enforcement-cooperation-act.md) | Article I, Section 11 | Extradition, hot pursuit, mutual legal assistance |
| [Territories Status Act](../../proposals/territories-status-act.md) | Article XX, Section 2 | Election participation, Regional assignment, status paths |

Each proposal includes a hostile reinterpretation stress test analyzing potential misuse and countermeasures.

## Proposed Constitutional Enhancements

These proposals suggest optional additions to the Regional Federal Constitution that may be adopted before or after the core constitution:

| Proposal | Would Add | Purpose |
|----------|-----------|---------|
| [Senate Safeguard Concurrence Amendment](../../proposals/senate-safeguard-concurrence-act.md) | Article IV, Section 4-A | Targeted Senate concurrence for safeguard legislation (emergency powers, military, elections, judiciary, de-escalation, allocation) to provide additional check against authoritarian consolidation while preserving House majority rule for ordinary legislation |

## Original Complete Document

The original complete constitutional text (all 22 articles combined) is preserved at:

- [constitution.md](../constitution.md) - Complete constitutional text

This combined document is useful for:

- Reading the constitution as a unified whole
- Understanding how provisions interact
- Reference during implementation

## Navigation

- [Back to Regional Federalism Design](../)
- [Back to Regional Federalism Overview](../../)
- [All Plans](../../../../)
