# Immigration Corridor System: System Architecture

---

## End-to-End Flow

The ICS operates through a four-phase progression from entry to citizenship, with clear benchmarks and off-ramps at each stage.

```text
┌──────────────────────────────────────────────────────────────────────────────┐
│                         SYSTEM ARCHITECTURE OVERVIEW                          │
└──────────────────────────────────────────────────────────────────────────────┘

   ENTRY                    INTEGRATION                    COMPLETION
     │                          │                              │
     ▼                          ▼                              ▼
┌─────────┐    ┌─────────┐    ┌─────────┐    ┌─────────┐    ┌─────────┐
│ Phase 0 │───▶│ Phase 1 │───▶│ Phase 2 │───▶│ Phase 3 │───▶│ Phase 4 │
│ Intake  │    │ Hub (A) │    │Corridor │    │ Tier C  │    │Citizen  │
│         │    │         │    │  (B)    │    │         │    │  Track  │
└─────────┘    └─────────┘    └─────────┘    └─────────┘    └─────────┘
   ≤90 days     6-12 mo       12-36 mo       Benchmarks      Eligible
                                               met
```

---

## Phase 0: Entry and Intake

### Location and Access

| Entry Point | Description |
|-------------|-------------|
| **Hub city intake centers** | Primary processing in designated hub cities |
| **Border processing points** | Intake initiation at designated border facilities |
| **Remote registration sites** | Alternative access for qualifying applicants |

### Status During Intake

- **Provisional lawful presence** during intake processing
- **CLP granted** after biometrics completion
- **Work authorization** within 7 days (provisional); converts to CLP work authorization after biometrics

### Intake Functions

| Function | Purpose |
|----------|---------|
| **Identity screening** | Biometric capture; database checks |
| **Health screening** | Medical evaluation; vaccination status |
| **Skills assessment** | Education verification; credential evaluation |
| **Language intake** | Baseline English proficiency assessment |
| **Housing placement** | Algorithm-based placement assignment |

### Screening Outcomes

| Outcome | Result | Next Step |
|---------|--------|-----------|
| **Pass** | CLP issuance | Phase 1 placement |
| **Conditional pass** | Medical follow-up required | Provisional status continues; CLP after clearance |
| **Fail** | Disqualifying factor identified | Written notice; 30-day appeal; referral to existing immigration process |

### Timeline

- **Target duration:** ≤90 days from intake to Phase 1 placement
- **Housing lag contingency:** Temporary reception centers (30-day stay cap maximum)
- **Interim housing:** Transition placement if reception center cap reached

---

## Phase 1: Hub Residency (Tier A)

### Purpose

Stabilization and orientation in high-capacity hub cities with intensive support services.

### Core Features

| Feature | Description |
|---------|-------------|
| **Time-limited housing assistance** | Subsidy decays over 6-9 months |
| **Structured daily routine** | Mandatory but supportive; opt-outs for disability/caregiving |
| **Employment or training** | Immediate legal work authorization |
| **Cohort-based integration** | Group activities and peer support |
| **Social anchoring** | Community connections and mentorship |
| **Crime prevention** | Routine and belonging reduce risk factors |

### Mobility

- Restricted to assigned hub city
- Exceptions for documented employment, family, or medical needs

### Key Incentive Structure

**Benefits decay automatically after 6-9 months:**

- Housing subsidy reduces
- Bonus benefits (enhanced services) phase out
- Legal status continues regardless
- Progress incentivized through relocation opportunity

### Duration and Review

| Milestone | Timing | Action |
|-----------|--------|--------|
| **Initial placement** | Day 1 | Hub city assignment; services begin |
| **Mid-point review** | 6 months | Progress assessment; Tier B eligibility check |
| **Tier A review** | 12 months | Individualized plan; benefits may decay; status continues |
| **Maximum stay** | 18 months | Must relocate to Tier B or remain with reduced benefits |

---

## Phase 2: Corridor Residency (Tier B)

### Purpose

Assimilation acceleration in lower-cost corridor cities with continued integration support.

### Core Features

| Feature | Description |
|---------|-------------|
| **Lower-cost relocation** | Move to corridor cities with better affordability |
| **Apprenticeships** | Structured career pathways |
| **Credential pipelines** | Professional licensing support |
| **Community embedding** | Deeper local integration |
| **Faster residency clocks** | Accelerated path to Tier C |
| **Housing stability** | Longer-term housing arrangements |

### Mobility

- Unrestricted within assigned corridor region
- May relocate between corridor cities within region
- Cannot relocate to hub cities or other regions without approval

### Duration and Review

| Milestone | Timing | Action |
|-----------|--------|--------|
| **Tier B entry** | After Tier A completion | Corridor city placement |
| **Combined review** | 36 months (A+B total) | Full assessment; Tier C eligibility |
| **Extension pathway** | If benchmarks not met | Documented barriers required; appeal available |
| **Failure handling** | After extension | Status adjustment or removal proceedings |

---

## Phase 3: National Mobility (Tier C)

### Purpose

Full integration; unrestricted national mobility; permanent residency eligibility.

### Benchmark Requirements

All benchmarks must be met for Tier C certification:

#### Language Proficiency

| Requirement | Standard |
|-------------|----------|
| **Minimum level** | CEFR B1 or equivalent |
| **Verification** | Approved standardized test |
| **Alternative pathway** | Employer + case manager verification (disability/elderly only) |

See [03-geographic-design.md](03-geographic-design.md) for full language verification protocol.

#### Economic Participation

| Requirement | Standard |
|-------------|----------|
| **Employment history** | 12 of last 18 months employed, in training, or full-time caregiving |
| **Income floor** | Local living wage band (updated annually via BLS data) |
| **Documentation** | Tax records; employer verification; training enrollment |

#### Law Compliance

| Requirement | Standard |
|-------------|----------|
| **Felony record** | No violent felony convictions |
| **Misdemeanor threshold** | Disqualifying misdemeanors limited by statute to violent or repeat offenses |
| **Administrative violations** | Traffic/administrative do not block unless unpaid or repeated |
| **Resolved offenses** | Resolved nonviolent misdemeanors do not disqualify |

#### Civic Orientation

| Requirement | Standard |
|-------------|----------|
| **Civics course** | Standardized, non-ideological curriculum |
| **Content** | Rights, responsibilities, local services |
| **Assessment** | Pass/fail on factual comprehension; unlimited retakes |

### Certification Process

| Step | Description |
|------|-------------|
| **Application** | Submit documentation to Corridor Integration Office |
| **Verification** | Automated and manual review of benchmarks |
| **Issuance** | Portable digital credential |
| **Appeals** | 30-day window; automatic review if denied |

### Tier C Outcomes

- **Unrestricted movement** throughout United States
- **Permanent residency eligibility** (path to green card)
- **Corridor identity fades** (no longer tracked as corridor participant)
- **Full labor market access** (no geographic restrictions)

---

## Phase 4: Citizenship Track

### Purpose

Full civic equality; naturalization eligibility; corridor status dissolves entirely.

### Eligibility

| Requirement | Standard |
|-------------|----------|
| **Tier C status** | Must have achieved Tier C certification |
| **Permanent residency** | Must obtain PR status through standard process |
| **Residency period** | Standard naturalization timeline (typically 5 years as PR) |
| **Naturalization requirements** | Standard USCIS requirements apply |

### Outcomes

- Full voting rights
- Unrestricted employment (including federal positions)
- Passport eligibility
- Family sponsorship rights
- Jury service eligibility

---

## Status Tier Summary

| Tier | Status | Mobility | Duration | Key Features |
|------|--------|----------|----------|--------------|
| **Phase 0** | Provisional | Intake center | ≤90 days | Screening; housing assignment |
| **Tier A** | CLP | Hub city | 6-18 months | Stabilization; structured support |
| **Tier B** | CLP | Corridor region | 12-24 months | Integration; apprenticeships |
| **Tier C** | CLP | National | Until PR | Full mobility; PR eligible |
| **Phase 4** | PR → Citizen | National | Standard | Naturalization track |

---

## Failure Handling

### Categories of Failure

| Category | Trigger | Initial Response |
|----------|---------|------------------|
| **Benchmark stagnation** | No progress after extensions | Case review; support assessment |
| **Benefit expiration** | Time limits exceeded | Reduced benefits; status continues |
| **Minor compliance** | Missed appointments; paperwork | Warning; support intervention |
| **Serious non-compliance** | Criminal violation; fraud | Enforcement proceedings |

### Pathways

| Failure Type | Pathway |
|--------------|---------|
| **Stagnation with barriers** | Extended support; accommodation review |
| **Stagnation without barriers** | Status adjustment to limited presence |
| **Criminal (minor)** | Standard justice system; no automatic removal |
| **Criminal (serious)** | Criminal justice + removal proceedings |
| **Fraud** | Benefit termination + removal proceedings |

See [10-enforcement.md](10-enforcement.md) for full removal and return pathways.

---

## System Safeguards

### Anti-Concentration

- Housing algorithm prevents geographic concentration
- Capacity monitoring triggers intake slowdowns
- Surge mode activates for mass influx

### Due Process

- Written notice for all adverse actions
- 30-day appeal windows
- Automatic stays for non-violent cases
- Independent oversight office

### Antifragility

- System slows before breaking
- Reroutes to alternative corridors
- Narrows intake rather than collapsing
- Fails gracefully with individual protections

---

## Related Documents

- [Geographic Design](03-geographic-design.md) - Hub cities, corridors, rural placement
- [Housing](04-housing.md) - Placement algorithm and housing standards
- [Enforcement](10-enforcement.md) - Removal and failure handling
- [Eligibility Matrix](14-eligibility-matrix.md) - Benefits and rights by status

---

## Document Navigation

- Previous: [Overview](01-overview.md)
- Next: [Geographic Design](03-geographic-design.md)
