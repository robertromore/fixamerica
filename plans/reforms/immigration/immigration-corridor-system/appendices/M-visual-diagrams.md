# Appendix M: Visual Diagrams

---

## Overview

This appendix provides visual representations of key ICS concepts, processes, and structures in ASCII/text format suitable for documentation.

---

## System Overview

### ICS Status Progression

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                     IMMIGRATION CORRIDOR SYSTEM                              │
│                        Status Progression                                    │
└─────────────────────────────────────────────────────────────────────────────┘

     ENTRY                                                           EXIT
       │                                                               │
       ▼                                                               ▼
┌─────────────┐    ┌─────────────┐    ┌─────────────┐    ┌─────────────┐
│   PHASE 0   │───▶│   TIER A    │───▶│   TIER B    │───▶│   TIER C    │
│   Intake    │    │  Hub City   │    │  Corridor   │    │  National   │
│  (0-90 days)│    │ (6-12 mo)   │    │ (12-24 mo)  │    │ (12-24 mo)  │
└─────────────┘    └─────────────┘    └─────────────┘    └─────────────┘
       │                  │                  │                  │
       │                  │                  │                  │
       ▼                  ▼                  ▼                  ▼
  • Registration     • ESL A1-A2       • ESL A2-B1       • Full mobility
  • Screening        • Employment      • Employment      • B1 achieved
  • Placement        • Hub residence   • Corridor area   • PR eligible
  • Provisional ID   • Basic services  • Full services   • Advance parole
                                                               │
                                                               ▼
                                                    ┌─────────────────┐
                                                    │   PERMANENT     │
                                                    │   RESIDENCE     │
                                                    │   (Application) │
                                                    └────────┬────────┘
                                                             │
                                                             ▼
                                                    ┌─────────────────┐
                                                    │   CITIZENSHIP   │
                                                    │  (5 years as PR)│
                                                    └─────────────────┘
```

---

## Geographic Structure

### Hub and Corridor Cities

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                         GEOGRAPHIC STRUCTURE                                 │
└─────────────────────────────────────────────────────────────────────────────┘

                              ┌─────────────────┐
                              │   NATIONAL      │
                              │   FEDERAL       │
                              │   OVERSIGHT     │
                              └────────┬────────┘
                                       │
              ┌────────────────────────┼────────────────────────┐
              │                        │                        │
              ▼                        ▼                        ▼
     ┌─────────────────┐     ┌─────────────────┐     ┌─────────────────┐
     │  GREAT LAKES    │     │   HEARTLAND     │     │   OTHER         │
     │  CORRIDOR       │     │   CORRIDOR      │     │   CORRIDORS     │
     └────────┬────────┘     └────────┬────────┘     └────────┬────────┘
              │                       │                       │
    ┌─────────┴─────────┐   ┌────────┴────────┐              │
    │                   │   │                 │              │
    ▼                   ▼   ▼                 ▼              ▼
┌───────┐         ┌───────┐ ┌───────┐   ┌───────┐     ┌───────────┐
│BUFFALO│◀───────▶│DETROIT│ │  DES  │◀─▶│KANSAS │     │  [OTHER   │
│ (Hub) │         │ (Hub) │ │MOINES │   │ CITY  │     │   HUBS]   │
└───┬───┘         └───┬───┘ │ (Hub) │   │ (Hub) │     └───────────┘
    │                 │     └───────┘   └───────┘
    │                 │
    ▼                 ▼
┌───────┐         ┌───────┐
│Syracuse│         │Grand  │      LEGEND:
│Rochester        │Rapids │      ═══════
│(Corridor)       │Lansing│      Hub City: Initial placement
└───────┘         │(Corridor)    Corridor City: Secondary placement
                  └───────┘      ◀──▶ : Transfer possible within region
```

---

## Placement Algorithm

### Decision Flow

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                     PLACEMENT ALGORITHM FLOW                                 │
└─────────────────────────────────────────────────────────────────────────────┘

                        ┌─────────────────┐
                        │  NEW ARRIVAL    │
                        │  REGISTRATION   │
                        └────────┬────────┘
                                 │
                                 ▼
                        ┌─────────────────┐
                        │ COLLECT DATA:   │
                        │ • Family size   │
                        │ • Skills        │
                        │ • Language      │
                        │ • Preferences   │
                        └────────┬────────┘
                                 │
                                 ▼
              ┌─────────────────────────────────────┐
              │     CHECK FAMILY CONNECTIONS        │
              │     (Existing family in hub city?)  │
              └──────────────┬──────────────────────┘
                             │
                ┌────────────┴────────────┐
                │                         │
               YES                        NO
                │                         │
                ▼                         ▼
        ┌───────────────┐       ┌───────────────────┐
        │ PRIORITY:     │       │  SCORE ALL        │
        │ Family city   │       │  ELIGIBLE CITIES  │
        │ if capacity   │       │                   │
        └───────┬───────┘       │  • Capacity (15%) │
                │               │  • Jobs (25%)     │
                │               │  • Language (20%) │
                │               │  • Family (30%)   │
                │               │  • Preference(10%)│
                │               └─────────┬─────────┘
                │                         │
                │                         ▼
                │               ┌───────────────────┐
                │               │  SELECT HIGHEST   │
                │               │  SCORING CITY     │
                │               └─────────┬─────────┘
                │                         │
                └────────────┬────────────┘
                             │
                             ▼
                    ┌─────────────────┐
                    │  CAPACITY       │
                    │  AVAILABLE?     │
                    └────────┬────────┘
                             │
                ┌────────────┴────────────┐
                │                         │
               YES                        NO
                │                         │
                ▼                         ▼
        ┌───────────────┐       ┌───────────────────┐
        │ CONFIRM       │       │ QUEUE FOR NEXT    │
        │ PLACEMENT     │       │ CYCLE             │
        └───────────────┘       └───────────────────┘
```

---

## Benefit Structure

### RID Payment Flow

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    RESIDENT INTEGRATION DIVIDEND (RID)                       │
│                           Payment Structure                                  │
└─────────────────────────────────────────────────────────────────────────────┘

    FEDERAL APPROPRIATION
            │
            ▼
    ┌───────────────────┐
    │     TREASURY      │
    │   Trust Fund      │
    └─────────┬─────────┘
              │
              ├────────────────────────────────────┐
              │                                    │
              ▼                                    ▼
    ┌─────────────────────┐              ┌─────────────────────┐
    │   BASE PAYMENT      │              │  LOCAL GRANTS       │
    │   $200-400/year     │              │  (Stabilization)    │
    │   per household     │              │                     │
    └─────────┬───────────┘              └─────────────────────┘
              │
              ├───────────────────────┐
              │                       │
              ▼                       ▼
    ┌─────────────────────┐  ┌─────────────────────┐
    │ EXPOSURE ADJUSTMENT │  │ PARTICIPATION BONUS │
    │ $100-300/year       │  │ $50-200/activity    │
    │ (high-impact zones) │  │ • Tutoring          │
    └─────────────────────┘  │ • Mentoring         │
                             │ • Renting           │
                             └─────────────────────┘
                                       │
                                       ▼
                             ┌─────────────────────┐
                             │  MAXIMUM CAP        │
                             │  $1,500/household   │
                             │  per year           │
                             └─────────────────────┘
                                       │
                                       ▼
                             ┌─────────────────────┐
                             │  ELIGIBLE RESIDENT  │
                             │  (US citizen or LPR │
                             │  in corridor zone)  │
                             └─────────────────────┘
```

---

## Agency Responsibilities

### Federal Agency Structure

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                      FEDERAL AGENCY RESPONSIBILITIES                         │
└─────────────────────────────────────────────────────────────────────────────┘

                              ┌─────────────────┐
                              │   CONGRESS      │
                              │ (Appropriations,│
                              │  Oversight)     │
                              └────────┬────────┘
                                       │
     ┌──────────────────┬──────────────┼──────────────┬──────────────────┐
     │                  │              │              │                  │
     ▼                  ▼              ▼              ▼                  ▼
┌─────────┐      ┌─────────┐    ┌─────────┐    ┌─────────┐       ┌─────────┐
│   DHS   │      │   HHS   │    │   DOL   │    │   HUD   │       │   ED    │
│         │      │         │    │         │    │         │       │         │
│• Status │      │• Health │    │• Work-  │    │• Housing│       │• EL     │
│• Border │      │• Mental │    │  force  │    │• Place- │       │  surge  │
│• E-Verify      │  health │    │• Appren-│    │  ment   │       │• School │
│• Enforce│      │• UC care│    │  tice   │    │• RID    │       │  coord  │
└────┬────┘      └────┬────┘    └────┬────┘    └────┬────┘       └────┬────┘
     │                │              │              │                  │
     │                │              │              │                  │
     └────────────────┴──────────────┴──────────────┴──────────────────┘
                                       │
                                       ▼
                         ┌─────────────────────────┐
                         │   INDEPENDENT           │
                         │   INTEGRATION           │
                         │   OVERSIGHT OFFICE      │
                         │   (IIOO)                │
                         │                         │
                         │   • Audits              │
                         │   • Appeals             │
                         │   • Public reporting    │
                         └─────────────────────────┘
```

---

## Timeline

### Implementation Timeline

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                       IMPLEMENTATION TIMELINE                                │
└─────────────────────────────────────────────────────────────────────────────┘

YEAR 0         YEAR 1         YEAR 2         YEAR 3         YEAR 4         YEAR 5
   │              │              │              │              │              │
   ▼              ▼              ▼              ▼              ▼              ▼
┌──────┐      ┌──────┐      ┌──────┐      ┌──────┐      ┌──────┐      ┌──────┐
│ENACT │      │PILOT │      │EXPAND│      │SCALE │      │FULL  │      │EVAL  │
│      │      │      │      │      │      │      │      │      │      │      │
│Legis-│      │3-5   │      │10-15 │      │15-20 │      │All   │      │5-yr  │
│lation│─────▶│Hub   │─────▶│Hub   │─────▶│Hub   │─────▶│Hubs  │─────▶│Review│
│passed│      │Cities│      │Cities│      │Cities│      │Active│      │      │
│      │      │      │      │      │      │      │      │      │      │      │
│Rule- │      │6-10  │      │20-40 │      │40-60 │      │60-80 │      │Reform│
│making│      │Corr. │      │Corr. │      │Corr. │      │Corr. │      │as    │
│      │      │Cities│      │Cities│      │Cities│      │Cities│      │needed│
└──────┘      └──────┘      └──────┘      └──────┘      └──────┘      └──────┘

MILESTONES:
───────────
Year 0: Legislation enacted, rulemaking begins
Year 1: First CLP participants placed in pilot cities
Year 2: First cohort advances to Tier B; lessons learned applied
Year 3: First cohort advances to Tier C; national expansion begins
Year 4: Full national coverage; interstate compact operational
Year 5: Comprehensive evaluation; first PR applications from early cohorts
```

---

## Participant Journey

### Individual Timeline

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    PARTICIPANT JOURNEY TIMELINE                              │
└─────────────────────────────────────────────────────────────────────────────┘

DAY 1                                                                    YEAR 10
  │                                                                          │
  ▼                                                                          ▼
  ┌────┬────────┬────────────┬──────────────┬──────────────┬────────────────┐
  │    │        │            │              │              │                │
  │ P0 │ TIER A │   TIER B   │   TIER C     │     PR       │  CITIZENSHIP   │
  │    │        │            │              │              │                │
  └────┴────────┴────────────┴──────────────┴──────────────┴────────────────┘
  │    │        │            │              │              │
  │    │        │            │              │              │
  │    │90 days │  1 year    │   2 years    │  3-4 years   │  8-10 years
  │    │        │            │              │              │
  ▼    ▼        ▼            ▼              ▼              ▼
┌────┐┌────────┐┌───────────┐┌─────────────┐┌─────────────┐┌───────────────┐
│Reg ││Work    ││Work/train ││Full mobility││Apply for PR ││Apply for      │
│    ││ESL A1  ││ESL B1     ││Advance      ││Family       ││citizenship    │
│    ││Hub only││Corridor   ││parole       ││sponsorship  ││Vote           │
└────┘└────────┘└───────────┘└─────────────┘└─────────────┘└───────────────┘
```

---

## Related Documents

- [System Architecture](../02-system-architecture.md) - Detailed structure
- [Geographic Design](../03-geographic-design.md) - Hub/corridor details
- [Implementation](../15-implementation.md) - Agency roles

---

## Document Navigation

- Previous: [Appendix L: Stakeholder Templates](L-stakeholder-templates.md)
- Next: [Appendix N: Research Gaps](N-research-gaps.md)
