# Appendix M: Visual Diagrams

---

## Overview

This appendix provides visual representations of key ICS concepts, processes, and structures using Mermaid diagrams.

---

## System Overview

### ICS Status Progression

```mermaid
flowchart LR
    subgraph Entry
        P0[Phase 0<br/>Intake<br/>0-90 days]
    end

    subgraph "Status Progression"
        TA[Tier A<br/>Hub City<br/>6-12 months]
        TB[Tier B<br/>Corridor<br/>12-24 months]
        TC[Tier C<br/>National<br/>12-24 months]
    end

    subgraph "Permanent Status"
        PR[Permanent<br/>Residence]
        CIT[Citizenship<br/>5 years as PR]
    end

    P0 --> TA --> TB --> TC --> PR --> CIT

    P0 -.- P0D[Registration<br/>Screening<br/>Placement<br/>Provisional ID]
    TA -.- TAD[ESL A1-A2<br/>Employment<br/>Hub residence<br/>Basic services]
    TB -.- TBD[ESL A2-B1<br/>Employment<br/>Corridor area<br/>Full services]
    TC -.- TCD[Full mobility<br/>B1 achieved<br/>PR eligible<br/>Advance parole]
```

---

## Geographic Structure

### Hub and Corridor Cities

```mermaid
flowchart TB
    FED[National Federal Oversight]

    FED --> GL[Great Lakes Corridor]
    FED --> HL[Heartland Corridor]
    FED --> OC[Other Corridors]

    subgraph "Great Lakes"
        GL --> BUF[Buffalo<br/>Hub]
        GL --> DET[Detroit<br/>Hub]
        BUF <--> DET
        BUF --> SYR[Syracuse/Rochester<br/>Corridor]
        DET --> GR[Grand Rapids/Lansing<br/>Corridor]
    end

    subgraph "Heartland"
        HL --> DSM[Des Moines<br/>Hub]
        HL --> KC[Kansas City<br/>Hub]
        DSM <--> KC
    end

    OC --> OTHER[Other Hubs<br/>TBD]
```

**Legend:**

- **Hub City:** Initial placement
- **Corridor City:** Secondary placement
- **↔:** Transfer possible within region

---

## Placement Algorithm

### Decision Flow

```mermaid
flowchart TD
    START[New Arrival Registration]
    DATA[Collect Data:<br/>Family size, Skills,<br/>Language, Preferences]
    FAMILY{Family in<br/>hub city?}
    PRIORITY[Priority:<br/>Family city<br/>if capacity]
    SCORE[Score All Eligible Cities:<br/>Capacity 15%<br/>Jobs 25%<br/>Language 20%<br/>Family 30%<br/>Preference 10%]
    SELECT[Select Highest<br/>Scoring City]
    CAPACITY{Capacity<br/>Available?}
    CONFIRM[Confirm Placement]
    QUEUE[Queue for<br/>Next Cycle]

    START --> DATA
    DATA --> FAMILY
    FAMILY -->|Yes| PRIORITY
    FAMILY -->|No| SCORE
    SCORE --> SELECT
    PRIORITY --> CAPACITY
    SELECT --> CAPACITY
    CAPACITY -->|Yes| CONFIRM
    CAPACITY -->|No| QUEUE
```

---

## Benefit Structure

### RID Payment Flow

```mermaid
flowchart TD
    FED[Federal Appropriation]
    TRUST[Treasury Trust Fund]

    FED --> TRUST
    TRUST --> BASE[Base Payment<br/>$200-400/year<br/>per household]
    TRUST --> GRANTS[Local Grants<br/>Stabilization]

    BASE --> EXPOSURE[Exposure Adjustment<br/>$100-300/year<br/>high-impact zones]
    BASE --> BONUS[Participation Bonus<br/>$50-200/activity<br/>Tutoring, Mentoring, Renting]

    EXPOSURE --> CAP[Maximum Cap<br/>$1,500/household/year]
    BONUS --> CAP

    CAP --> RESIDENT[Eligible Resident<br/>US citizen or LPR<br/>in corridor zone]
```

---

## Agency Responsibilities

### Federal Agency Structure

```mermaid
flowchart TB
    CONGRESS[Congress<br/>Appropriations & Oversight]

    CONGRESS --> DHS[DHS<br/>Status, Border<br/>E-Verify, Enforce]
    CONGRESS --> HHS[HHS<br/>Health, Mental Health<br/>UC care]
    CONGRESS --> DOL[DOL<br/>Workforce<br/>Apprentice]
    CONGRESS --> HUD[HUD<br/>Housing<br/>Placement, RID]
    CONGRESS --> ED[ED<br/>EL surge<br/>School coord]

    DHS --> IIOO
    HHS --> IIOO
    DOL --> IIOO
    HUD --> IIOO
    ED --> IIOO

    IIOO[Independent Integration<br/>Oversight Office<br/>IIOO<br/>Audits, Appeals<br/>Public reporting]
```

---

## Timeline

### Implementation Timeline

```mermaid
gantt
    title ICS Implementation Timeline
    dateFormat YYYY
    axisFormat %Y

    section Legislation
    Enact & Rulemaking           :y0, 2025, 1y

    section Hub Cities
    Pilot (3-5 hubs)             :y1, 2026, 1y
    Expand (10-15 hubs)          :y2, 2027, 1y
    Scale (15-20 hubs)           :y3, 2028, 1y
    Full (all hubs)              :y4, 2029, 1y

    section Corridor Cities
    Pilot (6-10 corridors)       :y1, 2026, 1y
    Expand (20-40 corridors)     :y2, 2027, 1y
    Scale (40-60 corridors)      :y3, 2028, 1y
    Full (60-80 corridors)       :y4, 2029, 1y

    section Evaluation
    5-Year Review                :y5, 2030, 1y
```

**Milestones:**

- **Year 0:** Legislation enacted, rulemaking begins
- **Year 1:** First CLP participants placed in pilot cities
- **Year 2:** First cohort advances to Tier B; lessons learned applied
- **Year 3:** First cohort advances to Tier C; national expansion begins
- **Year 4:** Full national coverage; interstate compact operational
- **Year 5:** Comprehensive evaluation; first PR applications from early cohorts

---

## Participant Journey

### Individual Timeline

```mermaid
gantt
    title Participant Journey (10-Year Path to Citizenship)
    dateFormat YYYY-MM-DD
    axisFormat %Y

    section Status
    Phase 0 (Intake)              :p0, 2025-01-01, 90d
    Tier A (Hub City)             :ta, after p0, 365d
    Tier B (Corridor)             :tb, after ta, 730d
    Tier C (National)             :tc, after tb, 1095d
    Permanent Residence           :pr, after tc, 1825d
    Citizenship Eligible          :cit, after pr, 1d
```

| Phase | Duration | Key Activities |
|-------|----------|----------------|
| **P0** | 90 days | Registration |
| **Tier A** | 1 year | Work, ESL A1, Hub only |
| **Tier B** | 2 years | Work/train, ESL B1, Corridor access |
| **Tier C** | 3-4 years | Full mobility, Advance parole |
| **PR** | 3-5 years | Apply for PR, Family sponsorship |
| **Citizenship** | 5+ years after PR | Apply for citizenship, Vote |

---

## Enforcement Escalation

### Compliance Response Levels

```mermaid
flowchart TD
    VIOLATION[Violation Detected]

    VIOLATION --> L1{Level 1:<br/>Minor/First}
    L1 -->|Yes| WARNING[Written Warning<br/>Counseling]
    L1 -->|No| L2{Level 2:<br/>Repeated/Moderate}

    L2 -->|Yes| RESTRICT[Mobility Restriction<br/>Benefit Reduction]
    L2 -->|No| L3{Level 3:<br/>Serious}

    L3 -->|Yes| SUSPEND[Status Suspension<br/>Hearing Required]
    L3 -->|No| L4[Level 4:<br/>Criminal/Severe]

    L4 --> REMOVE[Removal Proceedings<br/>Full Due Process]

    WARNING --> COMPLY{Compliance<br/>Restored?}
    RESTRICT --> COMPLY
    COMPLY -->|Yes| CONTINUE[Continue<br/>in Program]
    COMPLY -->|No| ESCALATE[Escalate to<br/>Next Level]
    ESCALATE --> L2
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
