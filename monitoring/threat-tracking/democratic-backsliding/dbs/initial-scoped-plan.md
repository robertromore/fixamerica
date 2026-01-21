# Democratic Backsliding Scorecard (DBS)

## Concept Overview, Implementation Guide, and Final LLM Prompt

**Version:** DBS-v1.1e (Backward-Compatible with DBS-v1.1d and earlier)

---

## 1. What This Is (High-Level Overview)

The **Democratic Backsliding Scorecard (DBS)** is a structured, evidence-based framework for detecting **early authoritarian drift** without relying on vibes, partisan framing, or single shocking events.

It is designed to answer one question rigorously:

> *Are observable political events crossing identifiable thresholds that historically precede authoritarian consolidation?*

The system:

- Breaks authoritarian drift into **categories of state power**
- Defines **checkpoints** with explicit scoring rules
- Aggregates scores into a **0–100 index**
- Preserves **historical comparability** while allowing higher resolution
- Forces **auditability** (every score must be tied to a specific event and source)

This is **not** a prediction model and **not** a moral judgment.
It is a **diagnostic instrument**.

---

## 2. Design Principles

### 2.1 Conservative by default

- Rhetoric alone scores low
- High scores require **institutional action**
- Multiple independent categories must move together

### 2.2 Evidence-first

- Every scored item must be tied to:

    - a concrete event
    - reputable sources
    - an explicit rubric checkpoint
- Unverifiable claims are **unscored**

### 2.3 Backward-compatible

- DBS-v1.1e is a **strict superset** of DBS-v1, v1.1a, v1.1b, v1.1c, and v1.1d
- Older scores remain meaningful
- New resolution adds signal without redefining thresholds

### 2.4 Non-partisan application

- The same methodology applies regardless of political affiliation
- Indicator definitions are established before application to specific actors
- Equivalent actions by different actors receive equivalent treatment

### 2.5 Jurisdiction-agnostic

- DBS is a **general democratic backsliding framework** with a US reference implementation
- All institution-specific references (e.g., Insurrection Act, DoD, state certification) are **illustrative, not limiting**
- Checkpoints are written at the **function level**, not the agency-name level
- International application requires substituting **local institutional equivalents** that perform the same democratic function
- See **Section 4.7** for international adaptation guidance

---

## 3. Conceptual Model (How Authoritarian Drift Actually Happens)

Authoritarianism does **not** arrive all at once.
Historically, it consolidates when **three systems align**:

1. **Coercive power** (police, military, enforcement)
2. **Legitimacy control** (courts, elections, narratives)
3. **Institutional compliance** (civil service, watchdogs, media)

The DBS tracks **each system separately**, then checks when they reinforce each other.

---

## 3.1 Temporal Model (What Time Window DBS Measures)

DBS is a **rolling-window diagnostic with memory and decay**. It is not a single point-in-time snapshot, nor a fully cumulative historical ledger. It is a time-weighted system that emphasizes recent behavior while retaining structural memory.

DBS measures **current regime trajectory**, not lifetime sins. That means:

- Recent actions matter most
- Older actions matter only if they were institutionalized or never reversed
- Repetition and persistence are more important than age

Think of DBS as asking: *"Given what has happened recently, and what structures remain in place, where is the system now?"*

### The Three Temporal Layers

DBS operates across three temporal layers, each with different rules:

**Layer 1 — Primary Scoring Window (Rolling 30–90 days)**

- **Purpose:** Detect active probing, escalation, and normalization
- **Rules:**
    - This is where most candidate events come from
    - Events in this window are eligible for full scoring and can raise or lower category totals
    - This window is rolling, not fixed to calendar periods
- **Why 30–90 days?** <30 days is too noisy; >90 days risks anchoring to stale behavior. 30–90 days captures repetition, institutional response, and whether pushback stuck.
- **This layer answers:** *"What is being attempted right now?"*

**Layer 2 — Structural Memory (No Decay if Still in Effect)**

- **Purpose:** Preserve institutionalized or entrenched actions
- **Rules:** Events older than 90 days may still count **if and only if** they resulted in:
    - formal policy
    - standing orders
    - personnel changes
    - legal reinterpretations
    - ...and those structures **remain in effect**
- **Examples:**
    - A regulation issued 2 years ago that remains active → still scores
    - A court-defying policy never reversed → still scores
    - A loyalist appointment still in office → still scores
- **This layer answers:** *"What power structures are still active?"*

**Layer 3 — Historical Context (Non-Scoring, Interpretive)**

- **Purpose:** Pattern recognition, not mathematical scoring
- **Rules:** Events from years ago are not scored directly, but may be cited as background or precedent to explain escalation, contextualize repetition, or justify persistence modifiers
- **Explicit rule:** Historical events do not add points unless their effects persist today.
- **This layer answers:** *"Have we seen this move before?"*

### Decay Rules

**Core principle:** Decay reflects loss of effect, not passage of time alone.

After 90 days, non-institutionalized actions may decay partially or fully based on their current operational status. This prevents permanent inflation while accurately modeling partial retreats, cosmetic compliance, and negotiated rollbacks.

#### Decay States

| State | Description | Effect on Score |
| ----- | ----------- | --------------- |
| D0 — No decay | Policy/action fully in force | No change |
| D1 — Partial decay | Action narrowed, paused, or partially reversed | −1 |
| D2 — Substantial decay | Action mostly reversed, effects limited | −2 |
| D3 — Full decay | Action rescinded, blocked, or abandoned | Score → 0 |

**Floor rule:** Scores cannot drop below 1 for a checkpoint if related rhetoric or posture remains active. Scores cannot drop below 0.

**D3/Floor interaction:** D3 (→0) and the floor rule are mutually exclusive. D3 applies only when the action is *completely* abandoned—formally rescinded with no active rhetoric, posture, or residual threat maintaining the concern. If related rhetoric or posture remains active, D3 cannot be applied; use D1 or D2 instead and apply the floor rule (≥1). In practice: a policy withdrawn but defended in speeches → D2 with floor = 1; a policy withdrawn, denounced, and structurally dismantled → D3 → 0.

#### Determining Decay State

**D0 — No decay:** Use when policy or structure remains fully operative; reversal claims are cosmetic; effects persist despite nominal changes.

- Examples: Policy "clarified" but still applied; court compliance delayed but enforcement continues; official reassigned but retains real authority

**D1 — Partial decay (−1):** Use when scope is reduced; enforcement becomes discretionary; authority is narrowed but not removed.

- Examples: Policy narrowed to fewer jurisdictions; military deployment reduced but posture remains; court order complied with in letter but not spirit

**D2 — Substantial decay (−2):** Use when core effect is removed; remaining impact is marginal or symbolic.

- Examples: Regulation rescinded but guidance remains; official reinstated without decision-making authority; enforcement suspended pending review

**D3 — Full decay (→0):** Use when action is formally rescinded; structure dismantled; courts fully enforce reversal.

- Examples: Policy withdrawn; personnel change undone; emergency powers expire and are not renewed

#### Institutionalization Test

**Core principle:** Institutionalization is about durable constraint on future behavior, not paperwork permanence. A thing can exist on paper and be dead in practice; a thing can also be formally reversible yet functionally entrenched. DBS must detect both.

**Actions are exempt from decay only when they satisfy both tests:**

**1. Formal Institutionalization Test** — *Is it formally in place?*

An action is formally institutionalized if embedded in:

- (a) Statute, binding regulation, or standing policy with delegated authority; OR
- (b) Personnel placement with ongoing authority; OR
- (c) Court ruling with binding effect

**2. Functional Institutionalization Test** — *Does it still shape incentives or power?*

An action is functionally institutionalized if **at least one** of the following is true:

| Criterion | Description |
| --------- | ----------- |
| Operational effect | Continues to constrain or enable behavior in practice, even if enforcement is selective, dormant, or uneven |
| Dependency creation | Other policies, personnel, or procedures rely on it; removal would require affirmative unwind |
| Credible threat | Routinely cited, invoked, or relied upon even if not recently enforced ("sword of Damocles" effect) |
| Procedural lock-in | Removal requires court reversal, legislative action, or supermajority—not just executive discretion |

**Decay eligibility based on institutionalization status:**

| Status | Decay Eligibility |
| ------ | ----------------- |
| Formal ✓ + Functional ✓ | No decay (D0) |
| Formal ✓ + Functional ✗ | Partial decay eligible (D1/D2) |
| Formal ✗ + Functional ✓ | Partial decay eligible (D1/D2) |
| Formal ✗ + Functional ✗ | Full decay eligible (D3) |

**Edge cases:**

- *Policy memo never rescinded but never enforced:* Formal ✓, Functional ✗ → partial decay eligible
- *Personnel change where replacement was later fired:* Institutionalization undone → decay resumes
- *Court ruling under active appeal:* If stayed or unenforced → partial decay; if operative pending appeal → no decay

**Justification requirement:** When claiming non-decay for a formally institutionalized action, document the functional criterion that applies. This makes decay decisions reviewable without hardcoding every edge case.

Discretionary enforcement, executive statements, and one-off events are **not** institutionalized and may decay.

#### Application Order

1. Determine base score (0–5)
2. Apply modifiers (M, P), respecting base caps
3. Apply decay adjustment (−1, −2, or →0)
4. Re-cap at 0–5

**Decay review timing:** Decay is assessed at each scoring run, not on a fixed calendar. The 90-day clock starts from the original event date.

#### Red-Line Decay Interaction

If decay reduces a red-line checkpoint below the ≥3 threshold (e.g., C1 from 3 to 2 via D1), the red-line multiplier **deactivates** for that checkpoint. Red-line status reflects current state, not historical peak. Re-escalation triggers re-assessment.

#### C1 Compliance Decay Matrix

For court contempt/compliance scenarios:

| Situation | Decay State |
| --------- | ----------- |
| Prompt, full compliance | D3 |
| Delayed but full compliance | D2 |
| Partial / bad-faith compliance | D1 |
| Continued defiance | D0 |

This allows DBS to show de-escalation without erasing the record of attempted overreach.

### Interaction with Modifiers

**Persistence modifier (P):** Persistence does not mean age alone. It means continued effect, repeated application, or survival across resistance. A 6-month-old policy still enforced = P2; a 6-month-old proposal never repeated = P0.

**Scope modifier (M):** Scope is spatial or institutional, not temporal. But older actions can justify M1/M2 if they still apply nationally or across agencies.

### Is DBS Cumulative?

**No** — and intentionally so. DBS does not sum all historical abuses. Instead:

- It reflects current system state
- It allows scores to go **down** if behavior de-escalates
- It avoids the trap of moral accounting

This is essential if DBS is to remain **diagnostic** rather than accusatory. DBS measures trajectory, not memory.

---

## 3.2 Run Modes & Temporal Consistency

This section operationalizes the temporal model defined in Section 3.1 for practical run scheduling and comparison.

### First Principle

DBS supports two legitimate purposes: **trend detection** and **point-in-time assessment**. They answer different questions and must not be mixed silently.

### Operational Tempo

DBS operates at two speeds:

| Mode | Question Answered | Trigger |
| ---- | ----------------- | ------- |
| **Scheduled** (primary) | Where is the system trending? | Fixed cadence (monthly default) |
| **Event-triggered** (exceptional) | Did something just change the risk regime? | Red-line reassessment rule (below) |

DBS is a periodic structural risk diagnostic with an event-triggered reassessment mechanism. It is not a live crisis command tool, but it must be able to react promptly when structural boundaries are crossed.

### Run Modes

| Mode | Window | Decay | Use Case |
| ---- | ------ | ----- | -------- |
| **Rolling DBS** (default) | Fixed trailing (60 days recommended) | Yes | Early warning, trend tracking |
| **Ad hoc DBS** | Variable | Yes | Event-driven analysis |
| **Snapshot DBS** | None | No* | Point-in-time comparison, historical reconstruction |

*Snapshot includes all currently-operative policies, standing orders, and institutionalized structures—regardless of when enacted. Snapshot does **not** include events that have fully decayed (D3) or been reversed.

### Rolling DBS (Default Mode)

**Recommended default:** 60-day trailing window. Use 30 days for rapid-escalation monitoring; use 90 days for quarterly institutional assessments.

For regular monitoring (weekly/monthly):

- Use a fixed cadence
- Use consistent window length
- Anchor runs to a fixed end date (e.g., last calendar day of month)

**Non-default window rule:** Any non-default window must be stated in the output header.

This ensures comparability, interpretable deltas, and reduced analyst discretion.

### Ad Hoc DBS

A non-scheduled DBS run conducted in response to specific events, using a non-standard window. Ad hoc runs should not be used for longitudinal trend comparison.

Ad hoc runs must be labeled:

> "Ad hoc run — non-standard window."

### Snapshot DBS

Snapshot DBS assesses democratic condition at a specific moment, ignoring rolling windows but respecting institutionalization status.

**Use cases:**

- Constitutional moments
- Election certification
- Government transition
- Comparative cross-country analysis
- Historical reconstruction (see Appendix D)

**Label requirement:**

> "DBS Snapshot — point-in-time assessment."

Snapshot DBS must not be trended directly against rolling DBS.

### Comparing Runs Over Time

Do not compare absolute DBS values in isolation—compare trajectories and drivers.

**For each run, record:**

- DBS score + confidence band
- Category subscores
- Active checkpoints
- Red-line status
- Intent profile
- Top 3 contributing events

**Compare across runs:**

- Δ DBS (change in score)
- Δ by category (which categories moved)
- New vs. expired events
- Escalation vs. decay patterns

**Reporting guidance:**

Instead of: "DBS went from 62 → 67"

Use: "DBS increased from 62 to 67, driven by new Category D legislative actions; Category B remained stable."

Trend analysis is mechanistic, not just numeric.

### Temporal Consistency Rules

**Rule 1 — Never mix modes silently.** Every DBS output must state: mode, window length (if rolling), run date, DBS version.

**Rule 2 — Trends require ≥3 standardized runs.** One delta is noise. Two is suggestive. Three establishes direction.

**Rule 3 — Snapshots override rolling for their moment.** If snapshot and rolling DBS differ materially, snapshot interpretation controls only for that specific assessment point.

### Red-Line Reassessment Rule

If any red-line checkpoint is **newly triggered** (crosses from <3 to ≥3), an out-of-cycle DBS run should be conducted within 72 hours, using the same window and mode as the prior run.

**Key constraints:**

- This is a procedural trigger, not an output signal — it does not auto-generate public alerts or emergency framing
- It does not change scoring methodology
- It does not bypass confidence or review rules
- Escalation within an already-triggered red line (e.g., 3→4) does not require out-of-cycle reassessment but should be noted in the next scheduled run

**Cooldown rule:** After an out-of-cycle red-line reassessment is performed, additional red-line-triggered reassessments are suppressed for **14 days** to prevent oscillation-driven retriggering. This cooldown may be overridden if:

- A *new* red-line checkpoint enters ≥3 that was not ≥3 in the last out-of-cycle run
- A *new* multiplier combination becomes eligible (e.g., combo rule now met)
- Confidence gating changes from Low to Medium/High in a way that newly activates a multiplier
- A legally binding, immediately operative, difficult-to-reverse action occurs

**Hysteresis rule:** A red-line checkpoint is considered to exit the ≥3 state only after it remains ≤2 across two consecutive scheduled runs (or ≤2 for at least 7 days). This prevents threshold oscillation (e.g., 3→2→3) from being treated as multiple independent regime changes when it reflects scoring noise rather than genuine escalation/de-escalation.

**Purpose:** Ensures the next published assessment reflects structural boundary crossings promptly while maintaining analytic restraint and preventing noisy retriggering from decay or interpretation churn.

---

## 4. Scorecard Structure (DBS-v1.1e)

### 4.1 Categories (What Is Measured)

| Category                                     | What It Captures                                      | Checkpoints |
| -------------------------------------------- | ----------------------------------------------------- | ----------- |
| **A — Emergency Narrative & Delegitimation** | Crisis framing that justifies rule-breaking           | A1–A4       |
| **B — Coercive State Power**                 | Use of law enforcement or military for political ends | B1–B7       |
| **C — Rule of Law & Courts**                 | Compliance with or defiance of legal constraints      | C1–C8       |
| **D — Elections & Transfer of Power**        | Integrity and neutrality of elections                 | D1–D12      |
| **E — Information Environment**              | Media retaliation and narrative control               | E1–E4       |
| **F — Security Services & Loyalty**          | Politicization of military/civil service              | F1–F7       |

Full checkpoint definitions are in **Appendix A**.

---

### 4.2 Checkpoint Scoring Scale

Each checkpoint is scored **0–5**:

| Score | Meaning                  |
| ----: | ------------------------ |
|     0 | Not observed             |
|     1 | Rhetorical / speculative |
|     2 | Isolated action          |
|     3 | Repeated or expanded     |
|     4 | Institutionalized        |
|     5 | Entrenched / systemic    |

---

### 4.3 Modifiers (Scope & Persistence)

**Scope Modifier (M):**

| Modifier | Meaning                        |
| -------- | ------------------------------ |
| M0       | Local / single agency          |
| M1       | Multi-state or multi-agency    |
| M2       | National or federal-wide       |

**Persistence Modifier (P):**

| Modifier | Meaning                              |
| -------- | ------------------------------------ |
| P0       | ≤14 days or one-off                  |
| P1       | 15–60 days OR 2–3 repeated instances |
| P2       | >60 days OR formally ongoing         |

**Modifier Values:**

| Level | Value |
| ----- | ----: |
| M0/P0 | 0     |
| M1/P1 | +1    |
| M2/P2 | +2    |

**Effective Score Formula (pre-decay):**

```text
raw = base score + scope modifier + persistence modifier
cap_by_base = {1→2, 2→4, 3→5, 4→5, 5→5}
effective = min(cap_by_base[base score], raw)
```

Example: An isolated action (base 2) that becomes national (M2 = +2) and persists >60 days (P2 = +2) has raw = 6, but cap_by_base[2] = 4, so effective = 4.

**Modifier Gating Rule (Anti-Gaming):**

Modifiers may raise a checkpoint score but may not change the underlying event class. This prevents an isolated action from being "promoted" to entrenched/systemic status purely through scope and persistence modifiers.

| Base Score | Maximum Effective Score |
| ---------: | ----------------------: |
| 1          | 2                       |
| 2          | 4                       |
| 3+         | 5                       |

```text
raw = base + M + P
cap_by_base = {1→2, 2→4, 3→5, 4→5, 5→5}
effective = min(cap_by_base[base], raw)
```

Example: A base-1 action (rhetoric only) with M2 + P2 modifiers has raw = 1+2+2 = 5, but cap_by_base[1] = 2, so effective = 2.

---

### 4.4 Severity Anchors (Inter-Rater Reliability)

To ensure consistent scoring, apply this **general anchor rule** to all checkpoints:

| Score | Anchor Meaning                                           |
| ----: | -------------------------------------------------------- |
|     1 | Rhetoric, proposals, or isolated statements              |
|     2 | Single concrete action, limited scope                    |
|     3 | Repeated actions or multi-agency adoption                |
|     4 | Formal policy, directive, regulation, or budget          |
|     5 | Structural lock-in (personnel, courts bypassed, permanence) |

**Example — A1 (Permanent Emergency Framing):**

| Score | Specific Anchor                                              |
| ----: | ------------------------------------------------------------ |
|     1 | Emergency rhetoric in speeches, single policy domain         |
|     2 | Emergency framing in official policy documents               |
|     3 | Multiple agencies adopt crisis framing                       |
|     4 | Emergency posture embedded in regulations/orders             |
|     5 | Permanent or open-ended emergency normalized across government |

**Instruction:** When scoring, explicitly justify why the anchor fits, not just the number.

---

### 4.5 Actor Tagging (Required Metadata)

DBS tracks effects on democratic safeguards **regardless of branch**. Every scored event must include actor tags:

| Tag | Meaning |
| --- | ------- |
| [EXEC] | Executive branch |
| [LEG] | Legislative branch |
| [JUD] | Judicial branch |
| [MIXED] | Coordinated across branches or ambiguous |
| [SUBNAT] | State or local government (use with DBS-State or when state actions affect federal DBS) |
| [FOREIGN] | Foreign state or non-state actor (primarily for D8 events) |
| [OTHER] | Non-governmental actor or unclear attribution |

**Examples:**

- Congress interfering with certification → D5 [LEG]
- Executive pressuring Congress → D5 [EXEC]
- Both coordinating → D5 [MIXED]
- State legislature changing certification rules → D6 [SUBNAT]
- Foreign government providing campaign assistance → D8 [FOREIGN]

Scores are unaffected by tags, but analysis gains precision.

---

### 4.6 Cross-Checkpoint Scoring Rules

**Rule: Independent Harm Principle**

An event may score multiple checkpoints **only if** it independently degrades multiple democratic safeguards.

**Examples:**

- Firing an IG investigating allies:
    - C4 (undermining watchdogs) ✓
    - F4 (security agencies for personal goals) ✓
    - Both valid because oversight and enforcement integrity are harmed separately.

- Federalizing Guard to police protests:
    - B1 (federal LE vs protests) ✓
    - B5 (domestic military use/prep) ✓
    - Distinct coercive mechanisms are engaged.

**Guardrail:** A single event **may not score more than one checkpoint within the same category** unless explicitly justified. This prevents score inflation.

**Boundary Rule (D2 vs. E1):**

- If intimidation targets journalists **because they are journalists** → E1
- If intimidation targets election processes **regardless of profession** → D2
- If both apply, score the primary target, note the overlap, and score only one.

**Boundary Rule (B6 vs. C6):**

- If enrichment flows to the **officeholder or immediate family** → C6
- If enrichment flows to **political allies, donors, or supporters** → B6
- If both apply, score the primary beneficiary, note the overlap, and score only one.

**Boundary Rule (D8 vs. E3):**

- If foreign actors **amplify domestic propaganda** without incumbent coordination → E3
- If incumbents **coordinate with foreign actors** to influence domestic processes → D8
- Key test: Does evidence show **domestic actors soliciting or coordinating**, or merely foreign actors acting independently?
- If both apply, score D8 (coordination is more severe than amplification).

---

### 4.7 International Adaptation

DBS is not US-only. References to US-specific laws or institutions are **illustrative examples**, not requirements.

#### Functional Substitution Rule

When applying DBS outside the United States:

1. Identify the **local institutional equivalent** that performs the same democratic function
2. Score based on **function and effect**, not legal form or agency name
3. If an action in another country would plausibly be the local analogue of the US example, score it under the same checkpoint

#### Functional Substitution Table

| Democratic Function | US Instantiation | Non-US Equivalents |
| ------------------- | ---------------- | ------------------ |
| Domestic military deployment | Insurrection Act | Emergency powers acts, martial law provisions, state of siege |
| Election certification | State certification boards | Electoral commissions, constitutional courts, electoral tribunals |
| Independent prosecution | DOJ / Special Counsel | Procuracy, Crown Prosecution Service, Fiscalía, independent prosecutors |
| Federal law enforcement | DHS / FBI / ICE | National police, gendarmerie, federal investigative agencies |
| Civil service protections | US merit system | Career bureaucracy statutes, civil service commissions |
| Military neutrality | DoD constitutional norms | Armed forces constitutional role, military codes of conduct |
| Judicial review | Federal courts / SCOTUS | Constitutional courts, supreme courts, council of state |
| Legislative oversight | Congressional committees | Parliamentary committees, inquiry commissions |

#### What DBS Does NOT Assume

DBS does **not** require:

- A written constitution
- Federalism
- Judicial review identical to the US model
- A presidential system
- Two-party politics
- US civil-military doctrine
- A specific legal doctrine name

DBS **does** assume:

- Some mechanism of political accountability
- Some distinction between civilian authority and coercive force
- Some procedural concept of elections or succession

If those baseline assumptions don't exist, DBS will naturally score high — which is appropriate.

#### Red-Line Logic Works Internationally

The red-line checkpoints are **institutional, not legalistic**:

| Red Line | Universal Meaning |
| -------- | ----------------- |
| C1 ≥ 3 | Courts repeatedly fail to bind the executive |
| B5 ≥ 3 | Military is deployed or persistently prepared for domestic coercion |
| D5/D6/D11 ≥ 3 | Elections are structurally compromised, not merely tested |
| F2 ≥ 3 | Armed forces show patterned loyalty reshaping |
| F6 ≥ 3 | Leader is functionally immune from legal accountability |

These are regime-agnostic thresholds. Every authoritarian transition crosses them, regardless of system type. The ≥3 threshold ensures red lines trigger on **demonstrated failure**, not isolated probing.

#### Optional: Jurisdiction Tag

For clarity in comparative analyses, include a jurisdiction tag in metadata:

`[US]` `[EU]` `[UK]` `[DE]` `[BR]` `[IN]` `[MX]` `[TR]` `[HU]` `[Hybrid]`

This does not affect scoring — it improves interpretability.

#### D9/D10 International Adaptation

**D9 (Legislative nullification)** applies across regime types:

- **Parliamentary systems:** D9 captures legislative actions that neutralize *judicial* functions, since the executive is typically fused with the legislature. Focus on court-stripping, defunding of independent tribunals, or legislative override of constitutional court rulings. The Garland-style confirmation blockade has no parliamentary equivalent, but attacks on judicial independence through legislative means do.
- **Examples:** Hungary's constitutional court restructuring (2010–2012); Poland's tribunal capture via legislative maneuver; UK Parliament Act overriding Lords on constitutional matters without Lords consent.

**D10 (Governance hostage-taking)** requires adaptation:

- **Parliamentary systems:** Government shutdown and debt ceiling mechanisms are largely US-specific. In parliamentary systems, score D10 when the legislature threatens governance collapse to extract unrelated concessions—e.g., threatening no-confidence votes unless unrelated policy demands are met, or blocking essential budgets for leverage on non-fiscal matters.
- **Non-US presidential systems:** Many have debt-ceiling equivalents or shutdown mechanisms; apply D10 directly.
- **Example adaptations:** Italy's government crises where coalition partners threaten collapse over unrelated demands; UK prorogation controversies where parliamentary function was suspended for political advantage.

---

### 4.8 Subnational Scoring (DBS-State)

DBS (unqualified) measures **federal-level** democratic trajectory. State-level actions are included in federal DBS only insofar as they materially affect federal democratic functions.

#### Scope Clarification

**Actions that affect federal DBS directly:**

- State certification law changes (Category D)
- State actions that determine congressional representation (gerrymandering with federal impact)
- State-level voter suppression with national electoral impact
- Coordinated multi-state entrenchment tactics

**Actions that do NOT fully resolve at federal level:**

- Lame-duck power grabs affecting only state governance
- State court packing unrelated to federal elections
- State-level civil service politicization without federal spillover

These should be flagged as subnational concerns, not absorbed into federal DBS.

#### DBS-State Variant

**DBS-State** applies the same categories, checkpoints, anchors, and decay rules to a **single state government**, treated as a democratic system in its own right.

**Key parameters:**

- Same scoring rules (0–5 scale, modifiers, decay)
- Same red-line logic (adapted to state equivalents)
- Same confidence and IRR standards
- Jurisdiction tag required: `DBS-State[WI]`, `DBS-State[NC]`, etc.

**Checkpoint adaptations for DBS-State:**

| Federal Checkpoint | State Equivalent | Notes |
| ------------------ | ---------------- | ----- |
| B5 (domestic military) | State police militarization; Guard used against state political opposition | Routine Guard use under gubernatorial control is NOT equivalent to federal B5 |
| D8 (foreign coordination) | Rarely applies | Omit unless federal-level evidence implicates state actors |
| F2 (military loyalty) | State law enforcement politicization | No direct equivalent; substitute or omit |
| D1–D6 (elections) | Apply directly | State-level election manipulation is the core use case |

DBS-State uses the same checkpoint structure with functional equivalents. Checkpoints B5, D8, and F2 require state-specific adaptation or may be omitted where no equivalent exists.

#### Subnational Non-Double-Count Rule

When a state action materially affects federal democratic functions, it may be included in the **federal DBS only** for the federal-function impact. The DBS-State score for that state may also include the same event, but only for **residual state-specific harm** not already captured in the federal attribution.

**Audit log guidance:** Event logs may reference the same source event in both federal and state runs. Point attribution must not double-count the same mechanism—each entry specifies whether points are for `federal_function` impact or `state_residual` impact.

**Example (Georgia SB 202):**

- **Federal DBS:** D5/D6 points for provisions affecting presidential election certification and administration
- **DBS-State[GA]:** Points only for provisions affecting state-only races, state governance, or local administration not captured federally

This rule prevents inflated totals while preserving interpretability: federal DBS measures federal democratic function; DBS-State measures what federal rollup intentionally omits.

#### Federalization Rule

State-level actions may influence the **federal DBS score** only when:

1. They directly affect federal elections or certification; OR
2. Similar actions are adopted by multiple states in a coordinated or patterned way

**Federalization triggers (any one sufficient):**

| Trigger | Condition | Timing |
| ------- | --------- | ------ |
| **(1) EC Trigger** | Similar measures are operative in states totaling **≥15% of Electoral College votes** | Time-independent |
| **(2) Diffusion Trigger** | **≥3 states** adopt similar measures within a rolling 12-month chain | Rolling window |
| **(3) Coordination Trigger** | Credible evidence of coordinated national strategy (party guidance, model legislation, shared funders) | Regardless of timing |

**EC Threshold Independence:**

The ≥15% Electoral College threshold is **cumulative and time-independent**: once similar measures are operative in states totaling ≥15% of Electoral College votes, federalization is warranted regardless of enactment timing, unless measures have fully decayed or been functionally reversed.

*Rationale:* Electoral College impact is structural and cumulative. The harm persists once enacted; timing should not nullify federalization eligibility.

**Rolling Window Definition:**

The "≥3 states within 12 months" threshold uses a **rolling window** measured from each qualifying enactment date. The threshold is met if there exists a sequence of ≥3 qualifying state actions where each action occurs within 12 months of the immediately prior qualifying action. Similarity must be based on **mechanism** (same legislative/administrative change type), not merely broad topic area.

*Example:* State A (January 2025) → State B (November 2025) → State C (February 2026). State C is within 12 months of B, and B is within 12 months of A. The threshold is met, even though C is 13 months after A.

**Operationalization:**

- A single state capture → does **not** spike federal DBS
- 3+ states adopting the same entrenchment tactic → Category D or C at federal level may increase
- National party coordination across states → escalates scope modifier (M1 → M2)

This preserves conservatism while recognizing pattern formation.

**Relationship to Subnational Pattern Flag:** The Subnational Pattern Flag (Section 7, Diagnostic Flags) uses a 24-month window to detect slower structural diffusion across state legislative cycles. The flag is diagnostic only—it identifies recurring state-level mechanisms and does **not** automatically trigger federalization. Federalization requires independent evaluation under this rule, including temporal proximity (≤12 months for Diffusion Trigger) and functional national impact.

#### Reporting Standard

When subnational context is relevant, report both scores:

```text
DBS (Federal): 44 (40–49)
DBS-State[WI]: 68 (63–72)
Note: State-level entrenchment contributing to elevated federal election risk.
```

#### Historical Calibration Note

DBS-State enables retrospective analysis of state-level democratic regression that federal-only DBS would underweight. Examples:

- Mississippi 1890 (constitutional convention disenfranchisement)
- Alabama 1901 (poll taxes, literacy tests)
- Wisconsin 2018 (lame-duck power stripping)
- North Carolina 2016 (HB2 era entrenchment)

These cases demonstrate that state-level backsliding can be severe and durable even when federal DBS remains moderate.

---

### 4.9 Intent / Direction Metadata

DBS deliberately measures **capacity and constraint**, not moral valence. This is why democracy-expanding interventions (Early Reconstruction, Civil Rights Act enforcement, desegregation via federal troops) can score high on coercive or institutional dimensions despite being pro-democratic.

That is correct behavior for the score—but interpretation needs structure.

The solution is **orthogonal metadata**, not score adjustment.

#### Intent / Direction Tag (Required)

Each **scored event** must be tagged with one of the following:

| Tag | Meaning |
| --- | ------- |
| [PRO-DEM] | Action expands democratic participation, equal protection, or accountability |
| [ANTI-DEM] | Action restricts participation, accountability, or pluralism |
| [AMBIGUOUS] | Direction unclear, mixed, or contested |

**Critical rule:** Intent/Direction **NEVER changes the numeric score**.

- The DBS score answers: *"How much coercive or institutional power is being exercised?"*
- The intent tag answers: *"Toward what end?"*

**Tagging level:** Intent tags apply to **events**, not checkpoint definitions. Checkpoint definitions are neutral instruments—it is the specific *use* that has direction.

#### Justification Requirement

Every intent tag must include a one-sentence justification grounded in **observable effects**, not rhetoric.

- ❌ "Leader says it's for democracy"
- ✅ "Action expanded franchise / removed barriers / enforced equal protection"

This prevents "good intentions" from becoming an escape hatch.

#### Hindsight Bias Warning (Retroactive Scoring)

For historical periods, intent tags must reflect **contemporaneous justifications and observable effects**, not modern historical judgment about outcomes. Score what was visible and defensible at the time.

#### Intent Does Not Override Red Lines or Diagnostic Flags

Even [PRO-DEM] actions can:

- Trigger red-line multipliers
- Activate diagnostic flags
- Warrant caution in interpretation

Diagnostic flags indicate **structural conditions** regardless of intent. A [PRO-DEM] action that meets flag criteria still triggers the flag—the combination surfaces democratic risk even from well-intentioned consolidation.

Example: Permanent emergency powers with [PRO-DEM] justification → still structurally risky.

#### Intent Can Change Over Time

Intent tags are not inherited across scoring windows. The same policy may shift:

- Initial intervention: [PRO-DEM]
- Continued enforcement without necessity: [AMBIGUOUS]
- Later use to entrench incumbents: [ANTI-DEM]

This captures historical drift accurately.

#### Intent Profile (Aggregated Reporting)

When publishing DBS results, report an Intent Profile using **score-weighted aggregation**:

```text
Intent Profile:
- PRO-DEM: 65% (weighted by score contribution)
- ANTI-DEM: 20%
- AMBIGUOUS: 15%
```

**Calculation:** Weight each event's intent tag by its contribution to the total DBS score. Higher-scoring events drive the profile more than lower-scoring events.

#### Optional: Aggregate Intent Balance (ABI)

For comparative analysis, compute:

```text
Let:
  P = ∑ points from PRO-DEM events
  A = ∑ points from ANTI-DEM events
  U = ∑ points from AMBIGUOUS events

ABI = (P − A) / (P + A + U)
```

**Range:** −1.0 (pure consolidation) to +1.0 (pure expansion)

- Positive ABI → democracy-expanding coercion
- Negative ABI → consolidation risk
- Near zero → balanced or mostly ambiguous

**Denominator includes AMBIGUOUS by design.** This makes ABI an "overall direction of scored activity" measure. Dilution from ambiguous events is intended behavior: periods with substantial unclear power moves should yield lower confidence in any directional claim.

**Optional variant—ABI_clear:** For analysis conditional on clear intent only:

```text
ABI_clear = (P − A) / (P + A)
U_share   = U / (P + A + U)
```

- If P + A = 0, ABI_clear is undefined (report as null)
- Always report U_share alongside ABI_clear so readers understand how much ambiguity exists
- ABI_clear can overstate certainty when U is large

**Recommendation:** Use default ABI and always publish the intent profile percentages (PRO/ANTI/AMBIG). Use ABI_clear only when specifically analyzing clear-intent actions.

**ABI is never added to DBS.** It is a lens, not a lever.

#### Directional Asymmetry Note

A high DBS with strongly positive ABI is still structurally risky, but for **different reasons** than a high DBS with negative ABI:

- **High DBS + negative ABI:** Classic authoritarian consolidation—power accumulated to restrict democracy
- **High DBS + positive ABI:** Capacity accumulation that may become dangerous if intent shifts or successors inherit the tools

This reinforces that **capacity accumulation is dangerous even when well-intentioned**. Intent helps interpret *why* risk exists, not *whether* it exists.

#### Example: Early Reconstruction (1867–1870)

- High B / D / F scores (federal troops, enforcement, restructuring)
- Intent tags overwhelmingly [PRO-DEM]
- ABI strongly positive

**Interpretation:** *"High coercive capacity deployed to expand democracy, not to entrench power."*

No hand-waving. No special pleading. No exception logic.

---

## 5. Backward Compatibility (DBS-v1 → v1.1a → v1.1b → v1.1c → v1.1d → v1.1e)

### 5.1 Score Mapping (v1 → v1.1a/v1.1b)

| DBS-v1 | DBS-v1.1a/v1.1b Equivalent | Rationale                                    |
| -----: | -------------------------- | -------------------------------------------- |
|      0 | 0                          | No change — not observed                     |
|      1 | 1                          | No change — rhetorical/speculative           |
|      2 | 2–3                        | v1 "action" now distinguishes isolated vs. repeated |
|      3 | 4                          | v1 "institutionalized" maps to level 4       |
|    n/a | 5                          | New — entrenched/systemic (no v1 equivalent) |

### 5.2 Usage Notes

- **Score 5 is new** (v1.1a+) and has no v1 equivalent — it captures structural lock-in that v1 could not distinguish
- **Score 3** represents "repeated or expanded" actions — in v1, this was conflated with isolated actions under score 2
- When comparing to older analyses:
    - **Forward mapping (v1 → v1.1e):** Use the table above; v1 score 2 should be treated as score 2 unless evidence shows repetition (→ score 3)
    - **Backward mapping (v1.1e → v1):** Collapse scores 2–3 to v1 score 2; collapse scores 4–5 to v1 score 3
- **New checkpoints** were added in v1.1b/v1.1d and have no v1/v1.1a precedent — exclude them when computing earlier-version-comparable scores: B6, B7, C6, C7, C8, D7, D8, D9, D10, D11, D12, F7
- **v1.1a → v1.1b:** Fully compatible; v1.1b adds checkpoints and refines definitions but does not alter existing scoring semantics
- **v1.1b → v1.1c:** Fully compatible; v1.1c adds F6 red-line multiplier, diagnostic flags, and operational guidance but does not alter checkpoint definitions or base scoring
- **v1.1c → v1.1d:** Fully compatible; v1.1d adds B7 (coordinated private-sector coercion) checkpoint, Asymmetric Information Environment diagnostic flag, subnational scoring clarifications, and checkpoint clarifications (C5/D3 expanded guidance) but does not alter existing checkpoint definitions or base scoring
- **v1.1d → v1.1e:** Fully compatible; v1.1e adds EX_TA mechanical exclusion rules, checkpoint metadata for state-nexus gating, and schema/output additions (run_date, EX_TA fields, excluded_events_context) without changing scoring anchors or thresholds

---

## 6. Aggregation & Formula

### 6.1 Category Maxima

| Category | Checkpoints | Max Score |
| -------- | ----------- | --------- |
| A        | 4 (A1–A4)   | 20        |
| B        | 7 (B1–B7)   | 35        |
| C        | 8 (C1–C8)   | 40        |
| D        | 12 (D1–D12) | 60        |
| E        | 4 (E1–E4)   | 20        |
| F        | 7 (F1–F7)   | 35        |

### 6.2 Final Score Formula

```
DBS = 100 × (
  0.10·A/20 +
  0.18·B/35 +
  0.18·C/40 +
  0.24·D/60 +
  0.10·E/20 +
  0.20·F/35
)
```

**Weight Rationale:**

The weighting draws on comparative politics research on democratic breakdown:

- D (Elections) receives highest weight (24%) — transfer of power is the ultimate safeguard. Schedler (2002) identifies electoral manipulation as the defining feature of competitive authoritarianism.
- F (Security Services) receives elevated weight (20%) — Levitsky & Ziblatt (2018) emphasize that capturing referees (including security services) is a key early consolidation step.
- B and C (Coercion and Courts) receive 18% each — enforcement and legal constraints are co-equal checks. Bermeo (2016) documents "executive aggrandizement" through legal and coercive means as the dominant modern backsliding pathway.
- A and E (Narrative and Information) receive 10% each — enabling conditions but not direct institutional action. V-Dem data shows these typically move *after* institutional capture begins.

**References:**

- Bermeo, Nancy. "On Democratic Backsliding." *Journal of Democracy* 27, no. 1 (2016): 5–19.
- Levitsky, Steven, and Daniel Ziblatt. *How Democracies Die*. Crown, 2018.
- Schedler, Andreas. "The Menu of Manipulation." *Journal of Democracy* 13, no. 2 (2002): 36–50.
- V-Dem Institute. "Democracy Report 2023: Defiance in the Face of Autocratization." University of Gothenburg, 2023.

**Category D Expansion Rationale (D9–D12):**

DBS v1.1b expands Category D from 8 to 12 checkpoints to capture threats that were previously underweighted:

- **D9 (Legislative nullification)** captures legislative overreach that neutralizes coordinate branches—a pattern visible in the Garland nomination blockade, court-stripping proposals, and agency defunding campaigns.
- **D10 (Governance hostage-taking)** captures deliberate governance sabotage—using essential functions as leverage for unrelated demands, as in debt ceiling brinkmanship.
- **D11 (Election infrastructure attacks)** captures cyber and physical attacks on election systems—regardless of attribution. This addresses the gap where foreign-originated or non-attributed attacks on voter registration, tabulation, or reporting systems had no natural scoring home.
- **D12 (Foreign interference, non-collusive)** captures external attacks on democratic processes without incumbent coordination. This fills the gap where D8 (which requires coordination) cannot reach foreign disinformation, covert funding, or legitimacy-undermining operations.

These checkpoints fill gaps: DBS previously captured executive overreach (Categories B, C, F) better than legislative dysfunction, infrastructure-level threats, or external attacks. Adding D9–D12 ensures the framework identifies democratic erosion through *any* branch, *any* attack vector, and *any* origin, not just domestic executive action.

The denominator increase from D/40 to D/60 means each individual D checkpoint contributes proportionally less to the category total, reducing the risk that any single tactic dominates the score. This reinforces the conservative design principle: high Category D scores require *multiple* forms of electoral or transfer-of-power dysfunction, not just one prominent case.

**Legislative Pathway Dominance Rule (Interpretive):**

When interpreting DBS results, scorers should assess whether legislative actions are driving the score disproportionately relative to their democratic impact. If Category D score is elevated primarily by legislative checkpoints (D7, D9, D10) while electoral integrity checkpoints (D1–D6, D8, D11, D12) remain low, identify the dominant pathway:

| Pathway Mode | Trigger | Mechanism |
| ------------ | ------- | --------- |
| `legislative_capture` | D7 ≥ 3 and/or D9 ≥ 3 | Legal/procedural manipulation that entrenches power and reduces future reformability |
| `legislative_dysfunction` | D10 ≥ 3 (primary driver) | Chronic paralysis/hostage-taking that degrades governance and shifts power to non-legislative channels |
| `mixed` | Both patterns present | Multiple pathways simultaneously active at material levels |

This does not affect the score mathematically but clarifies the nature of the threat for response planning. Legislative capture signals strategic anti-democratic entrenchment; legislative dysfunction signals governance breakdown that can enable executive power accumulation.

### 6.3 Red-Line Multipliers (Hard Thresholds)

Red-line multipliers normally activate only when the **effective score (after modifiers, gating, and decay) is ≥3** and the **base score is ≥3** (repeated, expanded, or procedurally binding) for the relevant checkpoint(s). Isolated actions (base 2) do **not** trigger red lines via modifiers alone.

- If **C1 ≥ 3 AND B5 ≥ 3** → +10
    - Courts are repeatedly defied AND military is actually deployed or persistently prepared
- If **D5 ≥ 3 OR D6 ≥ 3 OR D11 ≥ 3** → +15
    - Electoral legitimacy is being structurally undermined, not merely tested
    - D11 (election infrastructure attacks) qualifies because material compromise of election systems undermines outcome legitimacy regardless of voter intent or downstream certification
- If **F2 ≥ 3** → +10
    - Military neutrality shows patterned loyalty reshaping, not isolated personnel change
- If **F6 ≥ 3** → +10
    - Leader-above-law doctrine is operationalized, not merely asserted
    - Once leaders are functionally immune from law, all other safeguards depend on voluntary restraint

Cap final score at **100**.

**Exception Rule (Narrow):** A base score of 2 may trigger a red-line **only if** the action is:

- legally binding
- immediately operative
- difficult to reverse without extraordinary measures

Examples: An executive order permanently restructuring certification authority; a completed military deployment assuming policing authority; a court order explicitly ignored after final appeal.

**Instruction:** If invoking the exception, explicitly justify why the action is structurally irreversible.

**Precedence Rule:** The modifier gating rule (Section 4.3) limits numerical severity escalation but does not block red-line activation when the base-score threshold or exception is met. A base-2 action that qualifies for the exception may trigger red-line multipliers even though its effective score remains capped at 4.

**Stacking Rule:** Red-line multipliers are **cumulative by design**. If all four conditions are met, the total multiplier is +45. This is intentional: the simultaneous breach of courts, elections, military neutrality, *and* legal accountability represents a qualitatively different threat than any single breach. The 100-point cap prevents mathematical overflow while preserving the signal that multiple existential safeguards have failed together.

These multipliers prevent **false reassurance** from averaged scores when existential safeguards are breached.

**Note on D8 (Foreign Coordination):** D8 is intentionally excluded from standalone red-line multiplier triggers. While incumbent coordination with foreign actors represents a severe democratic breach, it does not by itself invalidate electoral outcomes or collapse institutional safeguards. D8 is a *catalyst checkpoint*—its danger is realized through combination with effect-based checkpoints (election infrastructure attacks, certification interference, emergency powers, or immunity doctrines). Elevated D8 scores substantially increase concern when paired with any red-line checkpoint affecting electoral integrity, certification, or accountability, even if D8 itself does not trigger a multiplier.

---

## 7. Interpretation Bands

|  Score | Meaning                                   |
| -----: | ----------------------------------------- |
|   0–24 | Normal democratic conflict                |
|  25–39 | Elevated stress / norm breaking           |
|  40–54 | Backsliding underway                      |
|  55–69 | Severe backsliding                        |
|  70–84 | Authoritarian transition zone             |
| 85–100 | Consolidated authoritarian control likely |

**Baseline note:** A score of 0 is mathematically achievable but empirically rare. Functioning democracies typically score 10–20 due to inherent structural features (emergency powers on the books, coercive enforcement capacity, legacy surveillance authorities, imperfect electoral mechanisms). DBS measures structural exposure to democratic backsliding, not the absence of all risk.

### Standard Interpretation Language

When communicating DBS results, use these standard formulations to maintain consistency and prevent misinterpretation:

**0–24 (Normal democratic conflict):**

> A DBS score in this range indicates normal democratic functioning with routine political conflict. Structural safeguards are intact and operating. No special interpretation is required.

**25–39 (Elevated stress / norm breaking):**

> A DBS score in this range indicates elevated institutional stress and norm erosion, but democratic safeguards remain functional. This warrants monitoring but not alarm. Many democracies experience periods in this range without lasting damage.

**40–54 (Backsliding underway):**

> A DBS score in this range indicates active democratic backsliding—structural safeguards are under coordinated pressure across multiple categories. Reversal remains straightforward through normal political processes if addressed. Trend direction over the next 6–12 months is critical.

**55–69 (Severe backsliding):**

> A DBS score in this range indicates severe democratic backsliding—multiple safeguards are failing or have been neutralized. Reversal remains possible but requires sustained institutional resistance. At this level, the system is vulnerable to shocks that could accelerate transition.

**70–84 (Authoritarian transition zone):**

> A DBS score in this range indicates a system in the authoritarian transition zone—where multiple democratic safeguards are under strain, but outcomes are not yet fixed. Scores in this range warrant close monitoring and institutional scrutiny, not alarmist conclusions. Uncertainty remains material, and reversal remains possible through extraordinary mobilization.

**85–100 (Consolidated authoritarian control likely):**

> A DBS score in this range indicates that democratic reversal through normal electoral and institutional means is structurally unlikely. This does not mean reversal is impossible, but it would require external pressure, elite defection, or regime collapse rather than routine democratic processes. If DBS = 100, see Section 7.2 for DBS-A and ES band reporting.

### Diagnostic Flags (Non-Scoring)

In addition to interpretation bands and red-line multipliers, DBS reports diagnostic flags that surface patterns without affecting the score.

**Kleptocratic Consolidation Warning:**

If **C6 ≥ 3** AND (**C3 ≥ 3** OR **C4 ≥ 3**), flag: *"Kleptocratic capture underway."*

This indicates personal enrichment is occurring alongside neutralized oversight (politicized prosecution or suppressed watchdogs). The flag is diagnostic—it does not add to the score but must be reported in the interpretation section.

**Sovereignty Risk Flag:**

If **D8 ≥ 3**, flag: *"Foreign coordination documented."*

This indicates that foreign actors have documented, systematic influence over domestic political processes. The flag is diagnostic—it does not add to the score but signals that democratic self-governance is being compromised by external actors.

If **D8 ≥ 3** AND (**D5 ≥ 2** OR **D6 ≥ 2**), flag: *"Sovereignty and electoral integrity both compromised."*

This compound flag indicates the intersection of foreign coordination with election subversion or certification manipulation—a particularly dangerous combination where external actors may be influencing who holds power.

**Accountability Collapse Flag:**

If **C7 ≥ 3** AND (**C1 ≥ 3** OR **C3 ≥ 3** OR **C4 ≥ 3**), flag: *"Accountability collapse accelerating."*

This indicates pardon abuse is occurring alongside court defiance, politicized prosecution, or neutralized oversight—the three escape hatches from accountability operating together. The flag is diagnostic—it does not add to the score but signals that the normal mechanisms for holding power accountable are being systematically bypassed.

**Subnational Pattern Flag:**

If **≥3 states** show **D7 ≥ 3** (legislative self-entrenchment) with similar mechanisms within 24 months, flag: *"Coordinated subnational entrenchment detected."*

This surfaces coordinated state-level anti-democratic action without mechanically inflating the federal score. The flag is diagnostic—it signals that state-level backsliding may be forming a national pattern that warrants closer federal-level attention. See Section 4.8 for full subnational scoring guidance.

**Timing rationale:** The 24-month window captures structural diffusion across staggered state legislative cycles. State-level entrenchment (gerrymandering, court-stripping, voting restrictions) often unfolds over multiple sessions—this window detects diffusion, not just synchronization.

**Relationship to Federalization Rule:** This flag does **not** automatically trigger federalization. Triggering this flag creates eligibility for review under the Federalization Rule (Section 4.8), which requires independent evaluation including temporal proximity (≤12 months) and functional national impact. The flag answers "Is a known failure mode spreading?" while the Federalization Rule answers "Does this now constrain national democratic choice?"

**Latent Coercive Capacity Flag:**

If **F7 ≥ 3** AND (**F4 ≥ 3** OR **C3 ≥ 3** OR **C4 ≥ 3**), flag: *"Latent coercive capacity activated."*

This indicates mass surveillance infrastructure exists alongside either political weaponization of security agencies (F4), politicized prosecution (C3), or neutralized oversight (C4). The combination represents a fully operational apparatus for targeted persecution—surveillance to identify targets, prosecution or enforcement to act on them, and compromised oversight to prevent accountability. The flag is diagnostic—it does not add to the score but signals that the infrastructure for systematic political persecution is in place.

**Legislative Dysfunction Flag:**

If (**D7 ≥ 3** OR **D9 ≥ 3** OR **D10 ≥ 3**) AND (**D1 + D2 + D3 + D4 + D5 + D6 ≤ 6**), flag: *"Legislative dysfunction driving Category D elevation."*

This indicates that Category D score is elevated primarily by legislative entrenchment (D7), nullification (D9), or hostage-taking (D10) rather than by direct electoral integrity threats (D1–D6). The flag is diagnostic—it does not add to the score but clarifies that the nature of the threat is *governance dysfunction* rather than *electoral capture*. This distinction matters for response: legislative dysfunction may be addressable through electoral accountability mechanisms, while electoral capture makes such mechanisms unreliable.

**State of Exception Flag (Schmitt Pattern):**

If **A1 ≥ 3** AND **A4 ≥ 3** AND **F6 ≥ 3**, flag: *"State of exception pattern active."*

This indicates the classic Carl Schmitt "state of exception" playbook: persistent emergency framing (A1), normalization of exceptional measures (A4), and operationalized leader-above-law doctrine (F6). The combination represents a meta-pattern where normal legal constraints are systematically suspended under claimed necessity. The flag is diagnostic—it does not add to the score but signals that constitutional order is being displaced by permanent emergency governance.

**Why this flag matters:** Individual checkpoint elevations may not reach red-line thresholds, but the *combination* represents a coherent authoritarian logic: the sovereign is who decides the exception. This pattern is historically associated with democratic collapse even when formal institutions remain nominally intact.

**When triggered, the interpretation section must:**

1. **Name the pattern explicitly** — identify it as state-of-exception consolidation
2. **List the events supporting each checkpoint** (A1, A4, F6) with dates and evidence
3. **Add specific watchpoints** for exception-entrenchment:
   - Removal or indefinite extension of sunset clauses on emergency powers
   - Assertions that courts lack jurisdiction over emergency actions
   - Permanent security posture justified by ongoing "exceptional" threat
   - Executive action explicitly bypassing legislative authorization under claimed necessity

**Coordinated Foreign–Domestic Election Subversion Flag:**

If **D8 ≥ 3** AND (**D5 ≥ 3** OR **D6 ≥ 3** OR **D11 ≥ 3**), flag: *"Coordinated foreign–domestic election subversion detected."*

This indicates documented incumbent coordination with foreign actors (D8) intersecting with outcome-determinative mechanisms—election interference (D5), certification manipulation (D6), or infrastructure compromise (D11). The combination represents the highest-risk intent + effect pattern short of outright coup mechanics. The flag is diagnostic—it does not add to the score or trigger additional multipliers but distinguishes betrayal-enabled subversion from background interference.

**When triggered, the interpretation section must:**

1. **Identify the coordinating channel(s)** — funding, cyber, narrative, logistics, or intelligence
2. **Specify which integrity mechanism(s) are affected** — D5 (certification interference), D6 (certification control), or D11 (infrastructure attack)
3. **Assess whether mitigation pathways still exist** — courts, certification bodies, reversibility of technical compromise

**Red-line interaction:** This flag does not add a new multiplier but strongly elevates concern when any integrity red line (D5/D6/D11) is already active.

**External Attack on Electoral Legitimacy Flag:**

If **D12 ≥ 3** AND (**D5 ≥ 3** OR **D6 ≥ 3** OR **D11 ≥ 3**), flag: *"External attack on electoral legitimacy detected."*

This indicates non-collusive foreign interference (D12) is materially degrading elections while domestic systems that normally absorb shocks—administration, certification, or infrastructure—are also compromised. The flag is diagnostic—it does not add to the score or trigger additional multipliers but separates external pressure + internal fragility from collusion-based subversion.

**Why this flag matters:** This pattern matches modern hybrid-warfare scenarios where harm occurs without domestic coordination. It avoids misattributing blame while still recognizing systemic danger. The distinction from the Foreign–Domestic Subversion Flag is critical: this flag captures *vulnerability exploited by external actors*, not *betrayal by domestic actors*.

**When triggered, the interpretation section must:**

1. **Distinguish origin (external) from vulnerability (internal)** — foreign actors are attacking, domestic systems are failing to absorb
2. **Identify whether failures are technical (D11), procedural (D5/D6), or both**
3. **Highlight resilience gaps rather than culpability** — focus on what defenses failed, not who to blame

**Red-line interaction:** This flag does not add a new multiplier but should elevate urgency in reassessment scheduling and watchpoint generation.

**Asymmetric Information Environment Flag:**

If **E3 ≤ 2** AND at least ONE of the following evidentiary conditions is met:

- (a) Platform takedown action identifying coordinated inauthentic behavior favoring incumbents
- (b) Peer-reviewed or institutional research documenting AI-scale information operations favoring incumbents
- (c) Official investigation findings documenting systematic information operations favoring incumbents

Flag: *"Asymmetric information environment detected; coordination unproven."*

This flag surfaces large-scale information operations that benefit incumbents but lack the provable state coordination required to score E3 ≥ 3. The flag is diagnostic—it does not add to the score but alerts analysts that the information environment may be asymmetrically influenced even absent direct government involvement.

**Evidentiary sources (any one sufficient):**

- Platform transparency reports or takedown announcements (Meta, X, Google)
- Research from credible institutions (Stanford Internet Observatory, DFRLab, Oxford Internet Institute, etc.)
- Official findings from FEC, DOJ, or equivalent bodies
- Academic peer-reviewed publications

**What this flag does NOT capture:**

- Organic grassroots movements with genuine support
- Traditional media bias (editorial choices without coordination)
- Foreign interference (covered by D12)
- Proven state coordination (would elevate E3 instead)

**Why this flag matters:** Modern influence operations increasingly use deniable cutouts and AI-generated content at scale. The effect on democratic discourse can be substantial even without provable state coordination. This flag preserves E3's strict evidentiary standard while ensuring such patterns are surfaced for interpretation and watchpoint generation.

---

## 7.1 International Calibration Examples

To ground the interpretation bands empirically, the following estimates show how select countries would score at key moments in their democratic trajectories. These are **illustrative approximations** based on publicly documented events, not rigorous assessments.

| Country | Period | Estimated DBS | Key Drivers | Notes |
| ------- | ------ | ------------: | ----------- | ----- |
| **Hungary** | 2010–2014 | 45–55 | D7 (constitutional entrenchment), C2 (court-packing), E3 (media capture), F1 (civil service loyalty) | Early consolidation phase under Orbán; democratic institutions formally intact but increasingly hollowed out |
| **Hungary** | 2020–present | 65–75 | Above + C4 (watchdog elimination), D3 (electoral system manipulation), E1 (media retaliation) | Competitive authoritarianism; elections occur but playing field severely tilted |
| **Poland** | 2015–2019 | 40–50 | C2 (judicial attacks), C4 (prosecutor politicization), F1 (civil service changes), E3 (state media alignment) | Constitutional Tribunal captured; EU rule-of-law conflicts |
| **Turkey** | 2013–2016 | 50–60 | B2 (targeting Gülenists), C3 (politicized prosecution), E1 (journalist arrests), F2 (military purges begin) | Post-Gezi, pre-coup attempt; accelerating executive aggrandizement |
| **Turkey** | 2017–present | 75–85 | Above + B5 (post-coup military operations), C1 (decree rule bypassing courts), D4 (conditional legitimacy), F2 (mass military purges) | Post-coup emergency; red-line multipliers likely triggered |
| **Venezuela** | 2015–2017 | 60–70 | C1 (Supreme Court overriding legislature), D5 (Constituent Assembly bypassing elections), C5 (rule by decree) | Maduro consolidating after Chávez; National Assembly neutralized |
| **Venezuela** | 2019–present | 85–95 | Above + D6 (parallel government/Guaidó crisis), B1/B5 (security forces against protests), F2 (military loyalty tests) | Near-complete consolidation; multiple red lines crossed |
| **United States** | Pre-2016 baseline | 10–20 | D7 (gerrymandering), some B3 (disparate enforcement) | Normal democratic conflict range; structural issues present but institutions functional |

**Usage guidance:**

- These calibrations help users interpret what a given score *means* in comparative terms
- A score of 50 does not mean "half authoritarian"—it means institutions are under serious, sustained stress comparable to Hungary circa 2012 or Poland circa 2017
- Scores above 70 indicate that reversal through normal electoral means is becoming structurally difficult
- The calibrations are approximate; rigorous country assessments would require the full DBS methodology applied systematically

---

## 7.2 DBS-A (Analytical) and Extreme Severity Bands

### The Ceiling Compression Problem

The 100-point cap serves an important function: it signals "maximum danger" without implying false precision about degrees of catastrophe. Once multiple red lines are active, the system has crossed into territory where qualitative differences dominate and numeric distinctions become less meaningful.

However, the cap sacrifices analytical resolution useful for:

- Historical calibration (distinguishing Weimar 1932 from 1934)
- Cross-country comparisons of consolidated authoritarianism
- Tracking deterioration after the transition point

### Solution: Capped Headline + Uncapped Analytical Score

DBS reports two values when the headline score reaches 100:

| Metric | Definition | Use |
| ------ | ---------- | --- |
| **DBS** | Score capped at 100 | Public communication, tier assignment |
| **DBS-A** | Score computed without cap (Analytical) | Research, calibration, extreme-case tracking |

**DBS-A** is computed identically to DBS (base scores + modifiers + red-line multipliers) but without applying the 100-point cap. It is reported **only when DBS = 100**.

### Extreme Severity Bands

When DBS = 100, the DBS-A value determines an **Extreme Severity (ES) band** that provides interpretive granularity:

| Band | DBS-A Range | Meaning |
| ---- | ----------- | ------- |
| **ES1** | 100–114 | Transition zone; 1–2 red-line multipliers active |
| **ES2** | 115–134 | Full red-line activation (+35); pre-multiplier aggregate 80–99 |
| **ES3** | 135+ | Extreme multi-category saturation; pre-multiplier aggregate ≥100 |

**Interpretation:**

- **ES1** indicates a system that has crossed into authoritarian transition but retains some structural constraints. Reversal remains possible through extraordinary mobilization.
- **ES2** indicates full consolidation underway—all major safeguards (courts, elections, military neutrality) have failed simultaneously. Reversal requires external pressure or regime collapse.
- **ES3** indicates totalitarian-level saturation where even before red-line multipliers, category scores alone would exceed 100. This is historically rare and corresponds to regimes with no remaining institutional constraints.

### Reporting Format

When DBS = 100, report:

```text
DBS (headline): 100
DBS-A (analytical): [value]
ES Band: [ES1/ES2/ES3]
Red lines triggered: [list]
```

### Usage Warning

**DBS-A is for analytical use only.** Public communication should use capped DBS. Reporting "DBS-A is 147" in public contexts implies false precision and invites misinterpretation. The ES bands provide sufficient granularity for non-specialist audiences.

---

## 7.3 Trend Drivers and Watchpoints

DBS runs should conclude with **Trend Drivers** (factors actively contributing to the current score) and **Watchpoints** (credible near-term risks not yet scored). These provide interpretive context and forward-looking guidance.

### Definitions

**Trend Driver:**
A factor actively contributing to the current DBS score (≥2 points) or explaining a material change (±3 points) relative to the prior run using the same mode and window length (see Section 3.2 temporal consistency rules).

- Backward-looking (what is driving the score)
- Evidence-based (already occurred or ongoing)
- Mechanistic (explains why the score is what it is)

**Watchpoint:**
A credible near-term risk that has not yet materially affected the score but could contribute ≥2 points or trigger a red-line checkpoint if it materializes.

- Forward-looking (what might matter next)
- Conditional (depends on future action)
- Explicitly non-scored
- **Horizon:** Watchpoints should focus on risks credibly materializing within the next scoring window (typically 60–90 days), not long-term or speculative scenarios.

### Risk Level Definitions

| Risk Level | Definition |
| ---------- | ---------- |
| **High** | ≥3 points contribution (driver) or would trigger a red-line checkpoint (watchpoint) |
| **Medium** | 2 points contribution (driver) or ≥2 points potential (watchpoint) |
| **Low** | <2 points but mechanistically relevant or contextually important |

**Important:** Risk level reflects impact on democratic risk, not likelihood or media salience.

### Required Format

Each bullet must include:

- **Type:** Driver or Watchpoint
- **Risk level:** High / Medium / Low
- **Checkpoint reference(s):** At least one checkpoint ID (drivers cite active checkpoints; watchpoints cite potential checkpoints)
- **Mechanism:** One sentence explaining how it affects democratic risk

**Status indicators** (Active / Escalating / Stabilized / Resolved for drivers; Pending / Uncertain for watchpoints) are optional but recommended for multi-run tracking.

### Quantity and Ordering

Provide **6–10 bullets total**, split as:

- 3–6 trend drivers
- 2–4 watchpoints

If fewer than 6 are warranted, state so explicitly ("Only four material drivers identified this period"). Do not pad to reach the target.

**Ordering:** Bullets must be ordered by risk contribution, not chronology:

1. High-risk trend drivers
2. Medium-risk trend drivers
3. High-risk watchpoints
4. Medium-risk watchpoints
5. Low-risk items (only if space allows)

### Examples

> **Driver (High):** Repeated executive noncompliance with court orders (C1=3) continues to elevate Category C; persistence modifier applied due to unresolved injunctions.
>
> **Driver (Medium):** Legislative maneuvering around election certification procedures (D5=2) triggered a red line but has not yet expanded in scope.
>
> **Watchpoint (High):** Public statements signaling potential invocation of emergency powers (A1/F2) could escalate rapidly if formalized.
>
> **Watchpoint (Medium):** Draft state legislation altering certification timelines may activate D6 if enacted.

---

## 8. How This Should Be Used

- **Weekly or monthly runs**, not reactive doom-scrolling
- Track **trend lines**, not single spikes
- Watch for **cross-category alignment**
- Treat results as **diagnostic signals**, not conclusions

---

## 8.1 Governance & Oversight

DBS assessments may be conducted by individual analysts or panels. Analysts exercise bounded discretion in event selection, constrained by checkpoint definitions and evidence standards. Disagreement is expected and should be documented via confidence bands and audit logs. DBS does not enforce consensus; it enforces transparency. Reviews are triggered by material disagreement, new evidence, or contested red-line activation and result in documented re-scoring rather than adjudication.

### Design Principles

DBS governance should:

- Preserve analytical independence
- Minimize discretion creep
- Surface disagreement rather than suppress it
- Avoid "authority by fiat"

DBS is not a court, regulator, or oracle. It is a structured analytical instrument. Governance reflects that.

### Who Runs DBS Assessments

**Primary Analyst (required):**

Responsible for event selection, scoring, confidence ratings, intent tags, and documentation. May be a single human analyst, an LLM operating under the DBS prompt, or a human–LLM hybrid. DBS is usable by a single qualified analyst by design.

**Validation Analysts (recommended, not required):**

One or more independent scorers used for IRR testing, quarterly validation, or high-stakes/public releases. This preserves accessibility while allowing rigor when stakes are higher.

**Analyst Qualification:**

Familiarity with DBS methodology, demonstrated by completing at least one full scoring run with documented audit log. For panel participation, achieving Δ ≤ 7 on at least one IRR validation against an established scorer is recommended.

### Event Scorability

An event is **scorable** if it plausibly maps to a defined checkpoint and is supported by at least one Tier-1 or corroborated Tier-2 source.

Analysts have initial discretion, constrained by checkpoint definitions, confidence requirements, and audit logs. There is no central gatekeeper deciding what "counts." Transparency replaces permission.

### Event Log (Anti-Cherry-Picking)

Each scoring window requires an **Event Log** documenting all considered events:

| Field | Required | Description |
| ----- | -------- | ----------- |
| Event ID | Yes | Unique identifier |
| Event description | Yes | Brief summary |
| Status | Yes | Scored / Excluded / Deferred |
| If Excluded: reason | Yes | Reason code (see below) |
| If Deferred: pending | Yes | What evidence is awaited |
| Mapped checkpoint | Conditional | Required for EX_TA entries |
| Elements checked | Conditional | Required for EX_TA entries |
| Evidence trigger docs | Conditional | Required for EX_TA entries |

**Standard exclusion reasons (codes):**

- **INSUFFICIENT_CORROBORATION** — Evidence does not meet Tier-1 or corroborated Tier-2 standards
- **FAILS_EXCLUDES_CLAUSE** — Excluded by checkpoint-specific Excludes list
- **OUTSIDE_SCORING_WINDOW** — Event falls outside the active window and has no institutional persistence
- **PURELY_RHETORICAL** — Rhetoric with no institutional action
- **DUPLICATE_EVENT** — Duplicate of an already logged event
- **CRISIS_LEGITIMACY_FILTER** — Excluded under CLF (see below)
- **EX_TA** — Technology-Amplified, Failed Nexus (see EX-TA rule below)

This ensures completeness, defensibility, and post hoc auditability.

**EX_TA — Technology-Amplified, Failed Nexus (mechanical exclusion)**

Use **EX_TA** only when **all** conditions are met:

- `mapped_checkpoint` has `requires_state_nexus = true` (Appendix A metadata)
- The event satisfies all non-NX elements for the checkpoint (`elements_checked` E# = true)
- The NX element is false (`elements_checked` NX = false)
- **No `unknown` values are permitted** in `elements_checked` (any `unknown` → EX_TA ineligible)
- At least one admissible evidence trigger document is present (see allowed doc types below)

**EX_TA is prohibited** for checkpoints with `requires_state_nexus = false` (e.g., D11, D12).

**Required fields for EX_TA entries:**

- `mapped_checkpoint`
- `elements_checked` (E# booleans + NX where applicable; no `unknown`)
- `evidence_trigger_doc_types` (one or more allowed doc types)
- `evidence_trigger_docs` (issuer, date, reference ID, and optional URL)

**Allowed evidence trigger document types (closed set):**

- `PLATFORM_ENFORCEMENT_NOTICE` — Official platform enforcement notice or transparency entry
- `PLATFORM_TRANSPARENCY_REPORT_ENTRY` — Platform transparency report entry
- `COURT_EXHIBIT_TECHNICAL` — Court-filed exhibit labeled as technical/forensic
- `COURT_FINDING_FACT` — Court finding of fact referencing technical evidence
- `REGULATOR_ORDER_OR_FINDING` — Regulator order or finding
- `CARRIER_STATUTORY_DISCLOSURE` — Carrier disclosure filed under statutory authority

#### Crisis Legitimacy Filter (CLF)

**Core principle:** Emergencies justify extraordinary action; they do not justify extraordinary permanence. DBS should neither penalize governments for responding to real disasters nor grant blank checks during crises.

**When CLF applies:** Only when a widely recognized genuine emergency exists (pandemic, natural disaster, armed conflict, large-scale terrorist attack). An event qualifies for CLF consideration if **at least two** of the following are true:

| Criterion | Description |
| --------- | ----------- |
| Objective external shock | Recognized by independent authorities (WHO, FEMA, UN, courts, scientific consensus) |
| Cross-partisan acknowledgment | Emergency recognized by opposition parties, governors, courts, or independent media |
| Time-bounded threat | Clear onset and plausible end conditions |
| Precedent-aligned response | Comparable democracies respond similarly |

If fewer than two criteria are met, score normally without CLF consideration.

**Three-part test for exclusion:** Even in genuine emergencies, actions must pass all three tests to qualify for exclusion or mitigation.

| Test | Question | Fails if... |
| ---- | -------- | ----------- |
| **Necessity** | Is the action plausibly required to address the emergency? | Action targets political opposition, media, or elections unrelated to emergency response |
| **Proportionality** | Does scope align with the scale of threat? | Measures exceed what's needed or exceed peer-democracy responses |
| **Reversibility** | Is there a practical path to rollback? | Powers are indefinite, entrenched, or insulated from judicial review |

**Scoring outcomes:**

| CLF Result | Scoring Treatment |
| ---------- | ----------------- |
| Passes all three tests | Exclude (or score at 0–1 with CLF note) |
| Passes necessity & proportionality, fails reversibility | Score normally, apply decay scrutiny |
| Passes necessity only | Score with −1 mitigation |
| Fails necessity | Score fully (no emergency mitigation) |

**Burden-shifting rule:** As an emergency continues, the burden of proof shifts toward reversibility. Early emergency actions get deference; prolonged ones do not.

**Cross-checkpoint amplification:** CLF does not suppress related abuses. Emergency-adjacent power grabs often appear in C1 (court bypass), E3 (information control), or F2 (emergency powers entrenchment)—these should be scored normally even when primary response actions are excluded.

**Documentation requirement:** Every CLF application must include a one-line justification in the Event Log:

> "Excluded under CLF: necessary, proportionate, reversible disaster response."

This makes exclusions auditable and prevents blanket immunity.

### Event Identification & Coverage

DBS prioritizes **completeness first, then correctness, then confidence**. Events may be tentatively identified but must be continuously re-evaluated as evidence evolves.

**Event Unit Rule (Deduplication):**

Create **one event record per real-world occurrence** (policy, order, firing, court action, deployment, etc.). Attach all supporting coverage to that single event via the `sources[]` list. Do not create separate events per outlet or per article. This prevents double-counting and makes reruns comparable.

**When to split into separate events:**

Only create separate events when at least one of these conditions is true:

| Condition | Example |
| --------- | ------- |
| Different action dates / distinct acts | "Announced" vs "implemented" vs "renewed" |
| Different legal instruments | Policy memo → executive order → implementing regulation |
| Substantive escalation or reversal | "Pilot program" becomes "nationwide mandate"; policy narrowed or repealed |
| Separate actors / jurisdictions | Same tactic used by different states or agencies with independent decisions |

**Escalation threshold:** An event qualifies as "substantive escalation" if its scope modifier would change (e.g., regional→national) or its base score would increase by ≥2 levels.

When splitting, keep events separate but link them using `cluster_id` to group related sagas (e.g., `state-certification-laws-q1-2026`).

**Mandatory Sector Sweep:**

For each scoring window, analysts must explicitly assess all governance domains, even if no events are found. Required domains with primary category mappings:

| Domain | Primary Categories |
| ------ | ------------------ |
| Executive actions | B, C, F |
| Legislative actions | C, D |
| Courts and legal compliance | C |
| Elections and certification | D |
| Security services / law enforcement | B, F |
| Media, information control, surveillance | E, F |
| Oversight institutions | C |
| Foreign interaction | D |

**Note:** Mappings are primary, not exclusive—events may legitimately score under multiple categories. The mapping guides attention; it does not constrain scoring.

For each domain, state either (a) candidate events identified or (b) no scorable events detected. This prevents selective attention, narrative-driven omission, and overfocus on a single branch.

### Non-English Sources

Non-English sources should be included when they provide material facts unavailable or underreported in English-language sources, or when the jurisdiction's primary media is non-English.

**Rules:**

- **Tier-1 status applies independent of language.** Reuters, AP, and major newspapers of record (Le Monde, Der Spiegel, El País, etc.) retain Tier-1 status regardless of publication language.
- Non-English sources may be used when reporting originates locally, primary documents are in another language, or corroboration strengthens confidence.
- When using non-English sources, identify language and outlet, provide translated summary.
- Downgrade confidence by one level (High → Medium, Medium → Low, Low → Low floor) unless corroborated by Tier-1 source or primary documents.

### Provisional Scoring

Events reported by credible sources but not yet confirmed may be scored with **Low confidence** and marked as **provisional**.

**Provisional events:**

- May not trigger red-line multipliers alone
- May not achieve effective scores ≥4 regardless of scope or persistence (cap applies after modifiers but before final capping)

This prevents provisional evidence from ever appearing "institutionalized" or "entrenched."

### Debunking Protocol

If an event is later shown to be false or materially misleading:

| Outcome | Action |
| ------- | ------ |
| Fully debunked | Score → 0; event marked "Retracted" with citation |
| Partially incorrect | Re-score with corrected facts |
| Facts true, interpretation contested | Adjust score/intent as warranted; retain event |

**Critical rule:** Do not delete the event from the log. Mark it as retracted with citation to the debunking source. This preserves auditability, credibility, and resistance to hindsight bias.

### Classified Information

Events are scored **when they become publicly knowable**, not when they secretly occurred.

**Publicly knowable** means: official declassification, credible reporting by Tier-1 sources, FOIA release, testimony under oath, or official government acknowledgment. Unverified leaks do not qualify.

**Implications:**

- No scoring based on unverified leaks
- No "secret history" scoring
- When classified actions are later confirmed, they enter the DBS timeline at the date of confirmation
- Earlier periods may be annotated but not retroactively re-scored

**Optional retrospective annotation (allowed, not required):**

> "Subsequent disclosures indicate earlier undisclosed activity consistent with this checkpoint."

Do not retroactively inflate past DBS scores unless conducting explicit historical re-analysis clearly labeled as retrospective recalibration (see Appendix D).

### Constitutional Rulings & Legal Doctrine

Constitutional rulings, landmark court decisions, and novel legal doctrines are scored based on their **operational impact on democratic safeguards**, not their doctrinal novelty or formal legality.

DBS does not judge jurisprudence; it measures whether constraints on power were weakened, removed, or rendered unenforceable.

**Scoring approach:**

A ruling that expands executive immunity, limits judicial review, or narrows enforcement authority should be scored through the checkpoints it affects:

| Effect | Relevant Checkpoints |
| ------ | -------------------- |
| Enforcement or prosecution becomes structurally impossible | C1, C4 |
| Immunity becomes operationally broad | F6 |
| Oversight or accountability mechanisms neutralized | C4, C5 |
| Emergency or discretionary powers expanded without constraint | B3, F6 |

**Example:** A Supreme Court ruling granting broad immunity from criminal prosecution would not score as a single event in one checkpoint. Instead, its effects would flow to C1 (if courts cannot compel compliance), F6 (if leader-above-law doctrine is reinforced), and C4 (if prosecutorial oversight is neutralized).

**Key principle:** Score the structural effect, not the legal event. This keeps DBS neutral on legal interpretation while remaining sensitive to power shifts.

### Review Process (Non-Adversarial)

DBS does not have "appeals" in a legal sense. It has review and revision.

**Review triggers:**

- Δ > 10 in IRR testing (see Appendix E for remediation protocol)
- A red-line is contested
- New evidence materially alters an event
- A score is challenged with substantive justification

**Review steps:**

1. Identify disputed elements (specific events, checkpoints, modifiers, intent tags)
2. State grounds for dispute (factual error, anchor misapplication, source credibility, boundary-rule confusion)
3. Independent re-score by second analyst or fresh LLM run, without reference to original score
4. Document outcome: score upheld, score revised, or uncertainty increased (wider confidence band)

No votes. No arbitration. The record speaks for itself.

### Handling Analyst Disagreement

**Principle:** Disagreement is signal, not failure. DBS surfaces disagreement rather than forcing consensus.

**When analysts disagree (Δ ≤ 7):**

Publish midpoint score, confidence band, and list of disputed checkpoints. This is normal and expected.

**When analysts disagree significantly (Δ > 10):**

Follow the remediation protocol in Appendix E. If disagreement persists after remediation, publish range (not point estimate) and explicitly note "high analytical uncertainty."

### Panel vs. Single-Analyst Models

**Single analyst** is valid for exploratory analysis, internal tracking, and early warning. Must include confidence bands and disclosure of uncertainty sources.

**Panel (2–5 analysts)** is recommended for public reporting, historical calibration, and high-stakes claims. Panel does not vote; panel publishes median score, min–max range, and points of disagreement. This avoids groupthink while increasing robustness.

### LLM-Based Scoring

When LLMs are used as analysts:

- Prompts must be versioned and disclosed
- Source lists must be logged
- Independent runs count as independent raters
- Human review is recommended for red-line activation

LLMs are treated as analysts, not authorities.

#### Prompt Versioning Scheme

Prompt version is **separate from DBS version**. A prompt change can materially alter LLM outputs even if scoring rules are unchanged.

| Version stream | What it tracks |
| -------------- | -------------- |
| `dbs_version` | Methodology (checkpoints, anchors, formula, decay, red-lines) |
| `prompt_version` | Implementation (instructions, output format, source strategy, ordering, wording) |

**Prompt versioning format:** Use semantic versioning: `Prompt-vMAJOR.MINOR.PATCH`

| Component | When to increment |
| --------- | ----------------- |
| MAJOR | Changes that can alter scoring outcomes or cross-run comparability |
| MINOR | Clarifications or additions that should not materially change scoring but reduce ambiguity |
| PATCH | Typos, formatting, non-substantive cleanup |

**Examples:**

- `Prompt-v1.2.0`: Adds CLF instructions (operationalizes existing rule) → MINOR
- `Prompt-v2.0.0`: Restructures event identification logic → MAJOR
- `Prompt-v1.2.1`: Fixes mislabeled checkpoint reference → PATCH

**Compatibility rule:** If `dbs_version` changes in a way that requires prompt changes, bump prompt MINOR or MAJOR and document compatibility (e.g., "Prompt-v1.3.0 is compatible with DBS-v1.1e and later").

**Disclosure requirement:** Each published run should disclose:

- `dbs_version`
- `prompt_version`
- Model name and version
- Tool access (web search enabled/disabled)
- Window and mode

#### LLM Scoring Revalidation

LLM behavior can shift across model versions, retrieval changes, and prompt updates. Explicit revalidation guidance ensures scoring stability over time.

**Trigger-based revalidation (always required):**

Revalidate whenever any of the following change:

- Model family or version (e.g., GPT-4 → GPT-5, Claude 3 → Claude 4)
- Browsing or tool access changes (web on/off, different retrieval systems)
- Prompt MAJOR or MINOR version change
- Schema or output format change that could affect scoring behavior

**Scheduled revalidation (baseline):**

- **Quarterly** for ongoing programs, even without configuration changes
- **After major news-cycle shocks** (elections, wars, major court rulings) if event mix shifts dramatically and comparability is needed

**Benchmark packet:**

Revalidation should use a fixed benchmark consisting of:

| Window type | Purpose |
| ----------- | ------- |
| Low backsliding (historical) | Tests baseline calibration |
| Medium backsliding (historical) | Tests mid-range discrimination |
| High backsliding (historical) | Tests upper-range sensitivity and red-line detection |
| Ambiguous/disputed window | Tests confidence grading and exclusion handling |
| Crisis (genuine emergency) window | Tests Crisis Legitimacy Filter application |

**Retest procedure:**

1. Run 3 independent LLM runs (same prompt, same source set, same model)
2. Compare checkpoint-level outputs and total DBS across runs
3. Assess inter-run reliability

**Acceptable drift thresholds:**

| Metric | Acceptable | Investigation required |
| ------ | ---------- | ---------------------- |
| DBS total | ±5 points | ±10 points |
| Red-line checkpoint | No flips across 3-threshold | Any flip across ≥3 threshold |
| Top 5 drivers/watchpoints | ≥60% overlap across runs | <60% overlap |

**Remediation if drift exceeds thresholds:**

1. Inspect disagreement log to identify divergence sources
2. Refine anchors and clarifying notes (adjust instructions before touching score math)
3. Bump `prompt_version` and document the change
4. Re-run benchmark packet to confirm remediation

### Accountability Without Central Authority

There is no single "DBS authority." Credibility comes from transparent methods, documented evidence, visible disagreement, and reproducible scoring. If multiple groups run DBS independently, that is a feature, not a bug.

### Publication Guidance

Before public release, analysts should allow reasonable time for factual correction by affected parties. DBS scores should not be released as "breaking news" without confidence bands and source disclosure.

### Version Consistency

A scoring window should use a single DBS version throughout. If methodology is updated mid-assessment, document the version used and note any checkpoints that would score differently under the new version.

---

## 8.2 Publication & Communication Protocol

DBS is a diagnostic instrument, not an alarm system or call-to-action. A high score does not mean a coup is imminent, democracy has failed, or emergency measures are justified. It means multiple structural safeguards are under strain, reversal is still possible, and trend matters more than the point estimate. Everything in this section reinforces that framing.

### Publication Levels

DBS assessments may be published at three levels, with increasing scrutiny requirements. These publication levels are distinct from source tiers (Section 9, Source Strategy), which refer to evidence reliability.

| Publication Level | Audience | When to Use | Requirements |
| ----------------- | -------- | ----------- | ------------ |
| **Level 1** (Internal) | Internal analysts, NGOs, watchdogs | Default for all assessments | Single analyst acceptable; full DBS + DBS-A (when DBS=100); unresolved disputes noted |
| **Level 2** (Expert brief) | Researchers, journalists, policymakers | After panel validation OR single analyst with Δ ≤ 7 on prior IRR | Written brief with category breakdown, drivers, uncertainty notes, trend comparison |
| **Level 3** (Public summary) | Informed general public | Level 2 requirements + trend confirmation (≥3 standardized runs showing the same pattern) + editorial review | Headline band + simplified explanation + explicit uncertainty language + historical/international comparison; no raw tables |

**Rationale:** This prevents one-off spikes from becoming headlines while preserving accessibility for expert audiences.

**Terminology note:** Publication levels (1-3) describe publication scrutiny. Source tiers (1-2) describe evidence reliability. These are distinct concepts.

### Intended Audiences

DBS has three intended audiences, in priority order:

1. **Analysts & institutions (primary):** Political scientists, journalists covering democracy, NGOs, election monitors, courts/legislative staff. DBS is designed for them.

2. **Informed public (secondary):** Civically engaged citizens, educators, policy-interested readers. They should see interpretation (not raw numbers) and ranges (not point certainty).

3. **Decision-makers (indirect):** DBS does not issue recommendations, but it informs oversight priorities, investigative focus, and risk awareness. If decision-makers react, that is their responsibility, not DBS's mandate.

### Theory of Change

DBS is **diagnostic and anticipatory**, not prescriptive. Its theory of change is indirect:

- **Visibility:** Structural erosion is often invisible until too late. DBS makes it legible earlier.
- **Common language:** It gives disparate actors a shared vocabulary for discussing risk without panic.
- **Constraint through scrutiny:** When erosion is documented, contested, and tracked, overreach becomes harder to normalize, justifications face friction, and institutional actors hesitate.
- **Timing advantage:** The "transition zone" is where reversal is still possible. DBS aims to shift attention into that window.

DBS does **not** call for protests, justify extraordinary measures, or replace political judgment. It informs judgment.

### Communicating Uncertainty

Uncertainty communication is **mandatory** for any public-facing release.

**Always publish a band, never a naked point:**

> DBS: 70 (confidence band: 65–75)

**Explain why uncertainty exists—specific causes, not generic hedging:**

> "Uncertainty is driven primarily by contested scoring of Category D legislative actions and unresolved court outcomes."

**Emphasize trend over threshold:**

> "The trajectory over the past 6–12 months is more informative than the current point estimate."

**Use intent/direction metadata to prevent misreading:**

> "While the score is elevated, a significant share of Category B activity is tagged [PRO-DEM], indicating federal enforcement rather than power entrenchment."

### Contested Score Response

If a published score is publicly challenged with substantive justification:

1. Acknowledge receipt within 48 hours
2. Conduct independent re-score per Section 8.1 review process
3. Publish findings regardless of outcome
4. Do not retract pending review; note "under review" status if necessary

**Substantive justification** includes factual disputes, misapplication of scoring anchors, source credibility challenges, or boundary-rule disagreements. It does not include disagreement with conclusions alone.

See Section 8.1 Publication Guidance for pre-release factual correction requirements.

### Score-Specific Communication Guidance

Different score thresholds warrant different communication emphasis:

| Threshold | Communication Focus |
| --------- | ------------------- |
| First entry into 40+ | "Backsliding underway"—explain which categories are driving; emphasize reversibility |
| First red-line activation | Explain what red line means; note that single red-line ≠ consolidated authoritarianism |
| Crossing into 55+ | "Severe backsliding"—emphasize trend direction; compare to historical cases if available |
| Crossing into 70+ | "Authoritarian transition zone"—use standard interpretation language (see Section 7); emphasize that reversal remains possible |
| DBS = 100 | Report DBS-A and ES band; use ES band guidance for interpretation |

---

## 9. Final LLM Prompt (Drop-In)

The following prompt is designed to be pasted directly into another LLM.

---

### FINAL LLM PROMPT

You are an **evidence-first political systems analyst**. Your task is to apply the **Democratic Backsliding Scorecard (DBS-v1.1e)** to **recent news events**, producing a **transparent, auditable scoring log**.

If the run is **topic-specific** (e.g., a single leader or country), constrain the event log and scoring to that topic, set `topic` in the JSON output, and label the run header accordingly.

---

### SOURCE STRATEGY (MANDATORY)

Use a **layered source approach**. You are NOT limited to these sources, but must prioritize them.

**Tier-1 — Factual anchors (use first):**

- Reuters, Associated Press (AP), Bloomberg
- NYT, Washington Post, Wall Street Journal, Financial Times
- NPR, PBS, BBC (secondary)
- Primary documents: court orders, filings, statutes, agency releases, official transcripts
- Legal analysis: SCOTUSblog, Lawfare, Just Security (facts must still be corroborated)

**Contrast sources (for framing contrast; not a reliability tier):**

- Right-leaning: Fox News (news), National Review, The Dispatch, WSJ Opinion
- Left-leaning: MSNBC (news), Vox, Guardian (US), Mother Jones

These sources provide editorial contrast only; reliability tiers are defined under **Confidence Rating Standard**.

**Requirements:**

- Every scored event must cite **at least one Tier-1 source or corroborated Tier-2 sources** (consistent with Section 8.1 Event Scorability)
- When possible, include **one contrasting source** from a different editorial ecosystem
- Single-source Tier-2 claims without corroboration → **Unscored**

---

### CHECKPOINT DEFINITIONS (MANDATORY)

When scoring any checkpoint, you MUST use the definitions in **Appendix A** of this document. If an event does not clearly meet the definition, it must be scored conservatively or marked **Unscored**.

---

### TEMPORAL SCORING RULES (MANDATORY)

DBS is a **rolling-window assessment**, not a lifetime cumulative score.

- The **primary scoring window** is the last 30–90 days, rolling
- Events older than 90 days may be scored **only if their effects are still in force** (policies, personnel, standing orders, legal interpretations)
- Non-institutionalized events decay after 90 days using graduated decay states (see Section 3.1):
    - D0: No decay (fully in effect)
    - D1: Partial decay (−1)
    - D2: Substantial decay (−2)
    - D3: Full decay (score → 0)
- Historical events may be cited as **context** but do not add points unless institutionalized
- Scores may **rise or fall** over time based on repetition, reversal, or enforcement
- If decay reduces a red-line checkpoint below ≥3, the red-line multiplier deactivates

---

### INTERNATIONAL ADAPTATION (MANDATORY FOR NON-US CONTEXTS)

DBS is not US-only. References to US-specific laws or institutions are **illustrative examples**, not requirements.

- Identify the **local institutional equivalent** that performs the same democratic function
- Score based on **function and effect**, not legal form or agency name
- If an action would plausibly be the local analogue of the US example, score it under the same checkpoint

**Examples:**

- Invocation of emergency powers allowing military policing → B5
- Executive interference with an electoral commission → D1 / D5
- Prosecutorial action guided by partisan loyalty → C3
- Purge of senior military officers for political reasons → F2
- State-aligned media coordinating enforcement narratives → E3

**Do not require:** A written constitution, federalism, judicial review identical to the US, or a specific legal doctrine name. **Score what happens, not what it's called.**

---

### SCORING RULES

**Base Scale:**

| Score | Meaning                  |
| ----: | ------------------------ |
|     0 | Not observed             |
|     1 | Rhetorical / speculative |
|     2 | Isolated action          |
|     3 | Repeated or expanded     |
|     4 | Institutionalized        |
|     5 | Entrenched / systemic    |

**Modifiers:**

- Scope: M0 (local) / M1 (multi-state/agency) / M2 (national)
- Persistence: P0 (≤14 days) / P1 (15–60 days or 2–3 instances) / P2 (>60 days or ongoing)

**Effective score (pre-decay):**

```text
raw = base + M + P
cap_by_base = {1→2, 2→4, 3→5, 4→5, 5→5}
effective = min(cap_by_base[base], raw)
```

Where M0/P0 = 0, M1/P1 = 1, M2/P2 = 2.

**Modifier Gating Rule (Conservative):**

Modifiers (scope M and persistence P) may raise a checkpoint score, but may not change the underlying event class. This prevents an isolated action from being "promoted" to entrenched/systemic purely through extent.

| Base Score | Max Effective Score |
| ---------: | ------------------: |
| 1 | 2 |
| 2 | 4 |
| 3 | 5 |
| 4 | 5 |
| 5 | 5 |

**Formula:**

```text
raw = base + M + P
cap_by_base = {1→2, 2→4, 3→5, 4→5, 5→5}
effective = min(cap_by_base[base], raw)
```

**Rationale:**

- Score 5 (entrenched/systemic) requires base ≥3 (repeated/expanded action)
- Score 4 (institutionalized) is the maximum for an isolated action (base 2), regardless of scope or persistence
- Sustained national rhetoric (base 1) can rise to score 2 (isolated signal level) but not higher

If an action is truly structural and irreversible, it should be scored at base 4+ from the start—the gate does not hide real dangers, it prevents miscategorization.

---

### COURT CONTEMPT RULE (C1)

A formal court contempt finding against executive actors automatically sets **C1 ≥ 3**.

- Escalate to **C1 = 4** if compliance is delayed, coerced, or repeated across agencies
- Escalate to **C1 = 5** if contempt orders are ignored, courts are declared non-binding, or sanctions fail
- Appeals with stays and good-faith compliance do **not** trigger contempt scoring

---

### HIGH-STAKES CHECKPOINT ANCHORS (MANDATORY FOR ALL RED-LINE CHECKPOINTS)

When scoring **B5, C1, D5, D6, D11, F2, or F6**, analysts must:

- Cite the **specific anchor row** from the checkpoint's severity anchor table
- Explain why the observed behavior **meets that anchor**
- Score **conservatively** if ambiguity remains between anchor levels

These seven checkpoints are red-line indicators. Anchor citation is mandatory to ensure inter-rater reliability and audit transparency. Generic scoring rules may not override these anchors.

---

### ACTOR TAGGING (REQUIRED)

Every scored event must include an actor tag:

- [EXEC] — Executive branch
- [LEG] — Legislative branch
- [JUD] — Judicial branch
- [MIXED] — Coordinated across branches or ambiguous
- [SUBNAT] — State or local government (use with DBS-State or when state actions affect federal DBS)
- [FOREIGN] — Foreign state or non-state actor (primarily for D8 events)
- [OTHER] — Non-governmental actor or unclear attribution

---

### CROSS-CHECKPOINT RULES

- An event may score multiple checkpoints only if it **independently degrades multiple safeguards**
- A single event may NOT score multiple checkpoints **within the same category** unless explicitly justified
- When checkpoints overlap (e.g., D2 vs E1), score the **primary target** and note the overlap

---

### WORKFLOW (REQUIRED)

#### Step 1 — Identify candidate events

**Temporal Access Check (REQUIRED):**

Before identifying candidate events, determine whether you have access to current news or real-time information.

- **If you do:** Proceed normally with the sector sweep below.
- **If you do not:** Explicitly state your knowledge cutoff and request that the user provide event summaries, timelines, or source links for the scoring window. Do not infer or fabricate post-cutoff events.

---

From the last **30–90 days**, perform a **mandatory sector sweep** across all governance domains:

| Domain | Primary Categories | Look for |
| ------ | ------------------ | -------- |
| Executive actions | B, C, F | Enforcement posture, emergency powers, loyalty demands |
| Legislative actions | C, D | Entrenchment, obstruction, certification interference |
| Courts and legal compliance | C | Defiance, manipulation, packing |
| Elections and certification | D | Suppression, fraud claims, certification disputes |
| Security services / law enforcement | B, F | Domestic deployment, politicization, surveillance |
| Media, information control, surveillance | E, F | Retaliation, platform pressure, propaganda coordination |
| Oversight institutions | C | Watchdog suppression, IG removal, ethics violations |
| Foreign interaction | D | Coordination, solicitation, leverage |

**Note:** Mappings are primary, not exclusive—events may legitimately score under multiple categories.

For each domain, state either (a) candidate events identified or (b) no scorable events detected. This prevents selective attention and narrative-driven omission.

**Event Identification Rules:**

- Maintain an Event Log listing scored, excluded (with reason), and deferred (pending evidence) events
- **Deduplication rule:** Record one event per real-world action. List all confirming coverage in `sources[]`. Do not create multiple events for the same action. Create a new event only for: a new legal instrument, new action date, substantive escalation/reversal, or a distinct actor/jurisdiction. Use `cluster_id` to group related events.
- Provisional events may be scored at Low confidence but must not alone trigger red lines and cannot achieve effective scores ≥4
- If an event is later debunked, mark as "Retracted" and adjust score—do not delete from log
- Classified actions are scored only upon public confirmation (official declassification, Tier-1 reporting, FOIA, sworn testimony, or government acknowledgment)

#### Step 2 — Decide scorable vs unscorable

If evidence is insufficient or uncorroborated → mark **Unscored** and explain why.

#### Step 3 — Score checkpoints

For each scored checkpoint, provide:

- Checkpoint ID
- Actor tag ([EXEC], [LEG], [JUD], [MIXED])
- Intent tag ([PRO-DEM], [ANTI-DEM], [AMBIGUOUS]) with one-sentence justification based on observable effects
- Base score (0–5)
- Modifiers (M0–M2, P0–P2)
- Effective score
- Justification (why this anchor level fits)
- Confidence (High / Medium / Low)

**Confidence Rating Standard:**

| Level | Definition |
| ----- | ---------- |
| **High** | ≥2 Tier-1 sources corroborate the event; no material factual disputes among sources; event clearly fits a single checkpoint with unambiguous anchor match |
| **Medium** | 1 Tier-1 source OR 2+ Tier-2 sources; minor factual disputes that do not affect checkpoint selection; OR the event fits a checkpoint but anchor selection involves one borderline judgment |
| **Low** | Tier-2 sources only; significant factual dispute or evolving story; OR anchor selection involves 2+ borderline judgments; OR classification depends on interpretive inference about intent or scope |

**Source Tiers:**

| Tier | Examples |
| ---- | -------- |
| Tier-1 | Court filings, official government documents, primary-source recordings/transcripts, published investigative journalism from outlets with fact-checking standards (AP, Reuters, major broadsheets) |
| Tier-2 | Single-source reporting, opinion-adjacent news analysis, leaked documents not independently verified |

**Non-English Sources:**

- **Tier-1 status applies independent of language.** Reuters, AP, and major newspapers of record (Le Monde, Der Spiegel, El País, etc.) retain Tier-1 status regardless of publication language.
- Include non-English sources when they provide material facts unavailable in English-language coverage or when the jurisdiction's primary media is non-English.
- When using non-English sources: identify language and outlet, provide translated summary.
- Downgrade confidence by one level (High → Medium, Medium → Low, Low → Low floor) for non-Tier-1 non-English sources unless corroborated by Tier-1 source or primary documents.

**Primary document caveat:** Primary documents (court filings, official transcripts, signed orders) establish what was said or done, not the interpretation of those actions. A court filing is Tier-1 evidence that a filing occurred, but the legal or political significance of that filing may still require interpretive judgment.

#### Source Archiving Policy

URLs decay over time (link rot, paywalls, page edits). To maintain long-term auditability, DBS uses a tiered preservation policy.

**Preservation tiers:**

Preservation tiers are distinct from Source Tiers (Tier-1/Tier-2). They indicate archival rigor, not evidentiary reliability.

| Preservation tier | Requirement | What to preserve |
| ----------------- | ----------- | ---------------- |
| **Tier 0** (always) | Metadata for all sources | Outlet, title, author, published_at, access date, URL |
| **Tier 1** (recommended) | Archive for scored events | Web archive snapshot or PDF capture for any source supporting a scored event, red-line trigger, or disputed/low-confidence case |
| **Tier 2** (required) | Mandatory capture for critical evidence | Primary documents (executive orders, statutes, court filings), official press releases, anything triggering a multiplier or anchor-level change |

**Acceptable archival methods:**

| Method | Description |
| ------ | ----------- |
| `web_archive` | Snapshot via archive.org or similar service |
| `pdf_capture` | PDF print-to-file of the web page |
| `official_pdf` | Downloaded official PDF document |
| `screenshot_capture` | Screenshot of key content |
| `text_excerpt` | Short excerpt (≤50 words) of the specific text relied upon |

**Content hashing:** For Preservation tier 2 sources, compute and store a SHA-256 hash of the captured content. This allows later verification that evidence has not been altered.

**Workflow:**

1. When scoring an event, collect 2–5 sources as usual
2. For any source used to justify scoring: create an archive snapshot or capture PDF
3. For Preservation tier 2 critical evidence: always capture PDF/screenshot and hash it
4. For evolving stories: archive the first version relied upon; add new source items for updates (don't overwrite)

**Paywalled content:** Don't distribute full copyrighted text. Instead:

- Archive publicly viewable metadata
- Store a short excerpt (≤50 words) of the specific text used for scoring
- Cite corroborating accessible sources where available

**Privacy guardrail:** Don't archive personal data unnecessarily. Prefer archiving official documents and public reporting.

**Confidence and Red-Lines:** A red-line checkpoint scored at ≥3 with Low confidence does not trigger the multiplier unless corroborated by at least one other red-line checkpoint at Medium or High confidence. This prevents unstable sources from driving escalation signals. **Low-confidence red-line checkpoints do not corroborate one another.** Corroboration requires at least one additional red-line checkpoint scored at Medium or High confidence; two Low-confidence signals cannot mutually validate.

**Confidence Inheritance:** When an event's underlying facts are revised (e.g., a report is corrected or debunked), confidence must be reassessed. Confidence downgrades may trigger re-scoring of affected checkpoints.

**BJC Integration:** Confidence ratings are additive with anchor-based borderline judgments (see Appendix E.6). A Medium confidence rating signals at least one borderline judgment; a Low rating signals two or more. This informs the single-rater confidence band calculation.

#### Step 4 — Audit log table

Create a table with:

| Field | Description |
| ----- | ----------- |
| Event ID | Unique identifier |
| Event title | Brief description |
| Date | When it occurred |
| Actor | [EXEC]/[LEG]/[JUD]/[MIXED] |
| Intent | [PRO-DEM]/[ANTI-DEM]/[AMBIGUOUS] + justification |
| Checkpoint | ID (e.g., C1, D5) |
| Base Score | 0–5 |
| Modifiers | M#, P# |
| Decay State | D0/D1/D2/D3 (if applicable) |
| Effective Score | Apply gating rule (Section 4.3), then decay; formula: `max(floor, gated_score + decay_delta)` where floor=1 if rhetoric active, else 0; D3 overrides to 0 |
| Confidence | High/Medium/Low |
| Evidence | Quote/paraphrase + source |
| Rationale | Why this checkpoint and score |

#### Step 5 — Aggregate

- Sum category totals (cap at maxima)
- Compute DBS using the formula
- Apply red-line multipliers if thresholds met
- Cap at 100

#### Step 6 — Interpretation

**Output header format:**

```text
DBS-v1.1e [Run Mode] ([Window], run date: YYYY-MM-DD) — Topic: [topic]: [Score] (confidence band: [±N])
```

- **Run Mode**: Rolling (default), Ad hoc, or Snapshot
- **Window**: State explicitly (e.g., "60-day window," "2025-01-01 to 2025-02-15")
- **Run date**: ISO date (YYYY-MM-DD) or full timestamp if needed
- **Topic**: Required if the run is topic-specific; omit if the run is general
- **Non-default window rule**: Any non-default window (not 60 days) must be stated; omission implies 60-day rolling

Example: `DBS-v1.1e Rolling (60-day window, run date: 2026-02-28) — Topic: trump: 47 (confidence band: 43–52)`

Provide:

- Final DBS score (with header as shown above)
- Risk tier (from interpretation bands)
- Red-line status (which, if any, were triggered)
- **If DBS = 100:** Also report DBS-A (analytical, uncapped) and ES band (ES1/ES2/ES3)
- Diagnostic flags:
    - "Kleptocratic capture underway" if C6 ≥ 3 AND (C3 ≥ 3 OR C4 ≥ 3)
    - "Foreign coordination documented" if D8 ≥ 3
    - "Sovereignty and electoral integrity both compromised" if D8 ≥ 3 AND (D5 ≥ 2 OR D6 ≥ 2)
    - "Accountability collapse accelerating" if C7 ≥ 3 AND (C1 ≥ 3 OR C3 ≥ 3 OR C4 ≥ 3)
    - "Coordinated subnational entrenchment detected" if ≥3 states show D7 ≥ 3 with similar mechanisms within 24 months
    - "Latent coercive capacity activated" if F7 ≥ 3 AND (F4 ≥ 3 OR C3 ≥ 3 OR C4 ≥ 3)
    - "Legislative dysfunction driving Category D elevation" if (D7 ≥ 3 OR D9 ≥ 3 OR D10 ≥ 3) AND (D1 + D2 + D3 + D4 + D5 + D6 ≤ 6)
    - "State of exception pattern active" if A1 ≥ 3 AND A4 ≥ 3 AND F6 ≥ 3
    - "Coordinated foreign–domestic election subversion detected" if D8 ≥ 3 AND (D5 ≥ 3 OR D6 ≥ 3 OR D11 ≥ 3)
    - "External attack on electoral legitimacy detected" if D12 ≥ 3 AND (D5 ≥ 3 OR D6 ≥ 3 OR D11 ≥ 3)
    - "Asymmetric information environment detected; coordination unproven" if E3 ≤ 2 AND (platform takedown action identifying coordinated inauthentic behavior favoring incumbents OR peer-reviewed/institutional research documenting AI-scale operations favoring incumbents OR official investigation findings documenting systematic information operations)
- Intent Profile (score-weighted percentages for PRO-DEM, ANTI-DEM, AMBIGUOUS)
- Optional: Aggregate Intent Balance (ABI) if useful for comparative context
- **Trend Drivers and Watchpoints (REQUIRED):** Provide 6–10 bullets identifying (a) Trend Drivers—factors actively contributing to the current DBS score (≥2 points) or explaining a material change (±3 points) relative to the prior run using the same mode and window length—and (b) Watchpoints—credible near-term risks (within 60–90 days) not yet scored but that could contribute ≥2 points or trigger a red-line checkpoint if realized.
- **Excluded events (context) (REQUIRED):** Derived view of Event Log entries with `exclusion_reason` codes starting with `EX_` (e.g., EX_TA), listing `event_id`, `exclusion_reason`, `mapped_checkpoint`, and `evidence_trigger_doc_types`.

  Each bullet must:
    - Be labeled **Driver** or **Watchpoint**
    - Include a risk level (**High**: ≥3 points or red-line trigger; **Medium**: 2 points; **Low**: <2 points but mechanistically relevant)
    - Reference relevant checkpoint IDs
    - Explain the mechanism of risk

  Order bullets by risk significance (High drivers → Medium drivers → High watchpoints → Medium watchpoints → Low items). Do not include speculative or non-mechanistic items. If fewer than 6 are warranted, state so explicitly.

---

### CONSTRAINTS

- Do not infer intent
- Do not exaggerate uncertainty
- If sources conflict, score conservatively
- Explicitly note ambiguities
- Justify anchor fit, not just numbers
- **D8 evidentiary standard:** Score D8 ≥ 2 requires documentary evidence (communications, financial records, testimony under oath, official findings). Circumstantial evidence alone caps D8 at 1.
- **Clarifying note consultation:** When scoring any checkpoint, consult its Clarifying note in Appendix A to verify boundary conditions are met and the event is not excluded.
- **JSON output:** When JSON output is requested, produce valid JSON conforming to DBS schema-1.4 (see Appendix F). Do not include markdown code fences or commentary outside the JSON object.

Tone: **neutral, analytical, transparent**

---

## 10. Closing Note

This framework is intentionally **hard to trigger** and **easy to audit**.
If it ever indicates severe risk, it will be because **multiple independent systems have moved together**, not because of one alarming headline.

---

## Appendix A — Canonical Checkpoint Definitions

This appendix defines **all checkpoints** referenced in DBS-v1.1e.
No checkpoint may be used, scored, or referenced without applying these definitions.

### Checkpoint Structure Rule

Each checkpoint follows a standardized four-part structure:

| Section | Purpose | Required |
| ------- | ------- | -------- |
| **Definition** | What behavior triggers the checkpoint | Yes |
| **Includes** | Concrete examples and escalation paths | Yes |
| **Excludes** | What does not trigger (false positives to avoid) | Yes |
| **Clarifying note** | Boundary guidance, overlap with adjacent checkpoints, interpretive caveats | Yes |

**Standard minimal clarification:** For checkpoints with no special boundary issues beyond the Includes/Excludes lists:

> *Clarifying note: No special exclusions beyond those listed above. Routine lawful actions consistent with historical precedent and subject to normal oversight do not trigger this checkpoint.*

This structure ensures consistent interpretive guidance across all checkpoints and prevents asymmetric weighting by analysts or LLMs.

---

### Checkpoint Metadata (EX_TA)

Each checkpoint includes metadata used for **EX_TA** eligibility. This metadata is **additive** and does not change scoring.

Metadata fields:

- `requires_state_nexus`: `true` or `false`
- `elements`: minimal checklist for EX_TA (E1, E2)
- `NX`: state/institution nexus element (only when `requires_state_nexus = true`)

#### Checkpoint Metadata Index (Minimal)

A1

- requires_state_nexus: true
- elements:
    - E1: Sustained emergency framing
    - E2: Ordinary democratic resolution framed as insufficient
    - NX: State/institution nexus

A2

- requires_state_nexus: true
- elements:
    - E1: Opposition framed as illegitimate or treasonous
    - E2: Delegitimization is systematic, not isolated
    - NX: State/institution nexus

A3

- requires_state_nexus: true
- elements:
    - E1: Institutions framed as illegitimate or corrupt
    - E2: Claims are systemic, not limited to a single ruling
    - NX: State/institution nexus

A4

- requires_state_nexus: true
- elements:
    - E1: Exceptional measures justified
    - E2: Justification includes bypassing normal legal limits
    - NX: State/institution nexus

B1

- requires_state_nexus: true
- elements:
    - E1: Federal law enforcement used in protest context
    - E2: Target is political activity, not specific crimes
    - NX: State/institution nexus

B2

- requires_state_nexus: true
- elements:
    - E1: Enforcement targets organizers, donors, or associations
    - E2: Targeting based on political association
    - NX: State/institution nexus

B3

- requires_state_nexus: true
- elements:
    - E1: Differential enforcement by political alignment
    - E2: Pattern evidence beyond isolated cases
    - NX: State/institution nexus

B4

- requires_state_nexus: true
- elements:
    - E1: Militarized deployment of force
    - E2: Primary purpose is political theater
    - NX: State/institution nexus

B5

- requires_state_nexus: true
- elements:
    - E1: Domestic military deployment or preparation
    - E2: Operational posture is credible (not rhetorical)
    - NX: State/institution nexus

B6

- requires_state_nexus: true
- elements:
    - E1: Economic or regulatory action confers benefits or penalties
    - E2: Political favoritism or retaliation is primary driver
    - NX: State/institution nexus

B7

- requires_state_nexus: true
- elements:
    - E1: Private-sector coercion with political effects
    - E2: Coordination or encouragement by state actors
    - NX: State/institution nexus

C1

- requires_state_nexus: true
- elements:
    - E1: Binding court order exists
    - E2: Executive noncompliance or defiance
    - NX: State/institution nexus

C2

- requires_state_nexus: true
- elements:
    - E1: Retaliation or threats against judges or courts
    - E2: Retaliation linked to rulings or oversight
    - NX: State/institution nexus

C3

- requires_state_nexus: true
- elements:
    - E1: Prosecutorial actions influenced by political loyalty
    - E2: Pattern or directive beyond isolated case
    - NX: State/institution nexus

C4

- requires_state_nexus: true
- elements:
    - E1: Watchdog or oversight bodies neutralized
    - E2: Investigative/reporting capacity impaired
    - NX: State/institution nexus

C5

- requires_state_nexus: true
- elements:
    - E1: Assertion of unilateral power beyond prior bounds
    - E2: Bypasses normal checks (legislative or judicial)
    - NX: State/institution nexus

C6

- requires_state_nexus: true
- elements:
    - E1: Officeholder or family gains material benefits
    - E2: Accountability mechanisms neutralized or bypassed
    - NX: State/institution nexus

C7

- requires_state_nexus: true
- elements:
    - E1: Pardon power used to protect allies or obstruct
    - E2: Signals impunity or blocks investigations
    - NX: State/institution nexus

C8

- requires_state_nexus: true
- elements:
    - E1: Structural changes to judiciary
    - E2: Changes reduce independence or entrench control
    - NX: State/institution nexus

D1

- requires_state_nexus: true
- elements:
    - E1: Federal interference in election administration
    - E2: Overrides or supplants state/independent processes
    - NX: State/institution nexus

D2

- requires_state_nexus: true
- elements:
    - E1: Intimidation targets voters or election officials
    - E2: Intimidation affects election conduct or access
    - NX: State/institution nexus

D3

- requires_state_nexus: true
- elements:
    - E1: Policies or actions restrict voting access
    - E2: Systematic or demographic-targeted pattern
    - NX: State/institution nexus

D4

- requires_state_nexus: true
- elements:
    - E1: Legitimacy accepted only if favored outcome occurs
    - E2: Preemptive fraud narrative tied to losing
    - NX: State/institution nexus

D5

- requires_state_nexus: true
- elements:
    - E1: Attempts to delay, nullify, or refuse certification
    - E2: Extra-legal obstruction beyond lawful challenges
    - NX: State/institution nexus

D6

- requires_state_nexus: true
- elements:
    - E1: Politicized control of certification or electors
    - E2: Authority shifted to partisan or executive control
    - NX: State/institution nexus

D7

- requires_state_nexus: true
- elements:
    - E1: Legislative changes entrench power
    - E2: Reversibility via normal processes reduced
    - NX: State/institution nexus

D8

- requires_state_nexus: true
- elements:
    - E1: Coordination between domestic actors and foreign entities
    - E2: Coordination aims to influence domestic processes
    - NX: State/institution nexus

D9

- requires_state_nexus: true
- elements:
    - E1: Legislature neutralizes executive or judicial authority
    - E2: Target branch cannot perform its constitutional role
    - NX: State/institution nexus

D10

- requires_state_nexus: true
- elements:
    - E1: Threat or blocking of essential governance functions
    - E2: Demands are unrelated leverage
    - NX: State/institution nexus

D11

- requires_state_nexus: false
- elements:
    - E1: Attack on election infrastructure (cyber, physical, or operational)
    - E2: Material compromise risk or disruption

D12

- requires_state_nexus: false
- elements:
    - E1: Foreign interference action (information, cyber, or funding)
    - E2: Intended to influence domestic process or legitimacy

E1

- requires_state_nexus: true
- elements:
    - E1: Retaliation against media organizations or journalists
    - E2: Retaliation linked to coverage or content
    - NX: State/institution nexus

E2

- requires_state_nexus: true
- elements:
    - E1: Government pressure on platforms
    - E2: Leverage or threats to alter moderation outcomes
    - NX: State/institution nexus

E3

- requires_state_nexus: true
- elements:
    - E1: Coordinated propaganda or narrative ecosystem
    - E2: Operational coordination or quid pro quo evidence
    - NX: State/institution nexus

E4

- requires_state_nexus: true
- elements:
    - E1: Misinformation law enforcement actions
    - E2: Selective application against opponents
    - NX: State/institution nexus

F1

- requires_state_nexus: true
- elements:
    - E1: Civil service loyalty tests
    - E2: Merit protections bypassed
    - NX: State/institution nexus

F2

- requires_state_nexus: true
- elements:
    - E1: Purges or politicization of military command
    - E2: Loyalty-based pattern beyond isolated changes
    - NX: State/institution nexus

F3

- requires_state_nexus: true
- elements:
    - E1: Professionals replaced with loyalists
    - E2: Competence criteria overridden across roles
    - NX: State/institution nexus

F4

- requires_state_nexus: true
- elements:
    - E1: Security agencies used for political goals
    - E2: Targeting opponents or shielding allies
    - NX: State/institution nexus

F5

- requires_state_nexus: true
- elements:
    - E1: Parallel enforcement structures created or used
    - E2: Bypasses normal oversight and chain of command
    - NX: State/institution nexus

F6

- requires_state_nexus: true
- elements:
    - E1: Leader-above-law doctrine asserted
    - E2: Operationalized to block accountability
    - NX: State/institution nexus

F7

- requires_state_nexus: true
- elements:
    - E1: Mass domestic surveillance infrastructure exists
    - E2: Oversight constraints are insufficient or absent
    - NX: State/institution nexus

---

### Category A — Emergency Narrative & Delegitimation (A1–A4)

#### A1 — Permanent emergency framing

**Definition:**
Sustained framing of political conditions as an ongoing existential crisis that cannot be resolved through ordinary democratic means.

**Includes:**

- Repeated use of terms like "invasion," "war," "collapse," "existential threat"
- Claims that the crisis is open-ended or worsening
- Emergency language used across multiple policy domains

**Excludes:**

- Time-limited crisis responses
- Rhetorical emphasis tied to a single discrete event

**Clarifying note:**
The key discriminator is *sustained* framing across contexts, not isolated rhetorical flourishes. A single heated speech does not trigger this checkpoint; consistent crisis language across multiple domains over weeks does.

---

#### A2 — Opposition is illegitimate

**Definition:**
Portrayal of political opponents as inherently disloyal, subversive, or unfit to participate in governance.

**Includes:**

- "Enemies within," "traitors," "not real Americans"
- Claims opposition victories are illegitimate by nature
- Framing dissent as sabotage rather than disagreement

**Excludes:**

- Harsh criticism of policies or competence
- Ordinary partisan rhetoric without delegitimization

**Clarifying note:**
Distinguish between attacking *what opponents do* (normal politics) and attacking *who opponents are* (delegitimization). "Their policies are wrong" is excluded; "they are enemies of the people" is included.

---

#### A3 — Institutions are illegitimate

**Definition:**
Systematic claims that courts, elections, media, or oversight bodies are structurally corrupt or invalid.

**Includes:**

- Assertions courts have no authority
- Claims elections are rigged absent evidence
- Blanket dismissal of press as inherently false

**Excludes:**

- Criticism of specific rulings or outlets
- Good-faith institutional reform arguments

**Clarifying note:**
Scoring requires *systematic* claims across institutions, not targeted criticism. Saying "this ruling was wrong" is excluded; saying "courts have no legitimate authority over me" is included.

---

#### A4 — Exceptional measures justified

**Definition:**
Arguments that normal legal or democratic constraints must be bypassed to address the claimed emergency.

**Includes:**

- "Normal rules don't apply"
- Calls to suspend norms, rights, or procedures
- Justification of force or coercion as necessary

**Excludes:**

- Lawful emergency powers with clear limits
- Actions clearly bounded by statute and oversight

**Clarifying note:**
The key discriminator is whether the proposed measures operate *within* legal constraints or argue they must operate *despite* them. Invoking statutory emergency authority with oversight is excluded; arguing that courts cannot constrain emergency action is included.

---

### Category B — Coercive State Power Used Politically (B1–B7)

#### B1 — Federal law enforcement used against protest activity

**Definition:**
Use of federal policing agencies against protest movements rather than specific criminal acts.

**Includes:**

- Crowd control, surveillance, or arrests targeting protests
- Federal deployment overriding local authorities
- Protesters treated as security threats

**Excludes:**

- Enforcement against clearly defined violent crimes
- Assistance requested by state/local governments

**Clarifying note:**
The distinction is between enforcement targeting *criminal conduct* (excluded) and enforcement targeting *political activity* (included). Federal assistance invited by local authorities is excluded unless the federal deployment exceeds or contradicts local requests.

---

#### B2 — Targeting of organizers, donors, or associations

**Definition:**
Law enforcement actions directed at movement infrastructure rather than individual criminal behavior.

**Includes:**

- Investigations of organizers or funding networks
- Guilt by association
- Patterned enforcement against aligned groups

**Excludes:**

- Individual prosecutions with clear evidence
- Neutral enforcement applied across ideologies

**Clarifying note:**
Scoring requires evidence that enforcement is directed at *movement infrastructure* (organizers, donors, networks) rather than individual criminal acts. Prosecuting an organizer for unrelated tax fraud is excluded; investigating donors solely because of their political giving is included.

---

#### B3 — Disparate enforcement

**Definition:**
Unequal application of law favoring allies and disadvantaging opponents.

**Includes:**

- Selective charging or non-charging
- Differential penalties for similar conduct
- Explicit favoritism acknowledged by officials

**Excludes:**

- Case-specific prosecutorial discretion
- Differences explained by evidence or jurisdiction

**Clarifying note:**
Proving disparate enforcement requires *pattern* evidence, not single-case comparisons. Isolated discretionary decisions are excluded; systematic favorable treatment of political allies alongside harsh treatment of opponents is included. Compare similar factual circumstances across political alignment.

---

#### B4 — Militarized deployments as political theater

**Definition:**
Use of heavily militarized force to signal dominance rather than respond to necessity. Deployments emphasizing optics, photo-ops, or symbolic dominance over operational necessity.

**Includes:**

- Armored vehicles, tactical gear for optics
- Deployments timed for political messaging
- Public spectacle emphasized over function

**Excludes:**

- Tactical escalation justified by credible threat
- Disaster or humanitarian missions

**Clarifying note:**
The key question is whether the *optics* are the primary purpose. Armored vehicles responding to an active shooter incident are excluded; armored vehicles deployed for a political leader's photo opportunity are included. Timing and communications help distinguish operational necessity from political theater.

---

#### B5 — Domestic military use or credible preparation *(Red-line checkpoint)*

**Definition:**
The use of active-duty military forces for domestic law enforcement purposes **or** concrete, operationally credible preparation to do so.

**Includes:**

- Invocation or attempted invocation of the Insurrection Act
- Formal standby orders or deployment readiness for domestic operations
- Public acknowledgment by DoD or executive officials that troops are prepared for internal enforcement
- Operational planning beyond tabletop exercises
- Federalization of National Guard for domestic law enforcement purposes

**Excludes:**

- National Guard activity under gubernatorial control
- Disaster response or humanitarian missions
- Purely rhetorical threats without operational posture

**Why this is a red line:**
Domestic military enforcement is historically one of the strongest predictors of authoritarian consolidation.

**B5 Severity Anchors:**

| Score | Anchor |
| ----: | ------ |
| **1** | Rhetorical threats or speculative discussion of domestic military use |
| **2** | Formal planning, standby orders, or readiness posture for domestic deployment |
| **3** | Limited domestic deployment or direct military support for law enforcement |
| **4** | Sustained or multi-region military deployment for internal security |
| **5** | Military normalized as routine domestic enforcement arm |

**Key discriminator:** Whether the military is **prepared for** (≤2), **used for** (3–4), or **normalized in** (5) domestic coercion.

**Clarifying note:**
This is a red-line checkpoint. The critical distinction is between *preparation* (score 1–2) and *actual deployment* (score 3+). Purely rhetorical threats without operational posture are excluded. National Guard under gubernatorial control is excluded because it does not represent federal military power directed at citizens.

---

#### B6 — Economic/regulatory capture for political ends

**Definition:**
Selective use of taxation, licensing, regulatory enforcement, or government contracting to reward allies and punish opponents.

**Includes:**

- Tax audits or investigations disproportionately targeting political opponents or their donors
- Regulatory enforcement actions that systematically favor allied businesses or penalize critical ones
- Government contracts awarded or withheld based on political alignment
- Licensing decisions (broadcast, banking, professional) used as political leverage
- Antitrust or securities enforcement selectively applied against political adversaries
- Credible threats of the above used to coerce compliance or silence

**Excludes:**

- Neutral enforcement of tax or regulatory law, even if politically inconvenient
- Policy changes that affect industries broadly (e.g., new environmental regulations)
- Enforcement actions initiated before targets became politically relevant
- Routine audits within normal statistical parameters

**Activation threshold:**
This checkpoint requires a **pattern** of selective enforcement or credible evidence of political motivation (e.g., statements by officials, timing correlated with political activity, statistical anomalies in enforcement). A single enforcement action against a political figure is insufficient absent contextual evidence of targeting.

**Clarifying note:**
B6 overlaps with C3 (politicized prosecution) but focuses on *regulatory and economic* tools rather than criminal prosecution. If the weapon is the IRS, FTC, or licensing boards, score B6; if the weapon is federal prosecutors, score C3. Both may apply in coordinated campaigns.

---

#### B7 — Coordinated private-sector coercion

**Definition:**
State signaling, encouragement, or coordination that induces private-sector actors (banks, employers, platforms, insurers, landlords, service providers) to penalize political opponents, critics, or disfavored groups without direct government enforcement action.

**Includes:**

- Government officials publicly or privately "flagging" individuals/organizations to private sector
- Pattern of private-sector actions against political figures following government statements
- Regulatory leniency for private actors who cooperate in exclusion
- Retaliation against private actors who refuse to participate
- Coordinated deplatforming, debanking, or de-employment across multiple private entities

**Excludes:**

- Independent private-sector decisions without credible state signaling
- Organic boycotts or market responses to speech
- Private entities enforcing their own published policies neutrally
- Industry-wide regulatory guidance that does not target specific political actors (e.g., broad guidance on high-risk industries applies to B6, not B7)
- Formal regulatory enforcement (score B6 instead)

**B7 Severity Anchors:**

| Score | Anchor |
| ----: | ------ |
| **1** | Rhetorical attacks or implicit warnings by officials suggesting that private actors should reconsider relationships with disfavored individuals or groups, without evidence of follow-through |
| **2** | Discrete instances where private actors take adverse action plausibly linked to state signaling, but deniability remains high and actions are isolated |
| **3** | Repeated or coordinated private-sector penalties following state signaling, creating a credible chilling effect on political activity |
| **4** | Systematic use of private-sector actors as enforcement proxies, where access to essential services or economic participation is conditioned on political alignment or silence |
| **5** | Private sector functions as a de facto enforcement arm of the state, with widespread economic or digital exclusion of political opponents and no realistic avenue for redress |

**Key discriminator:** Whether private-sector penalties appear **isolated and deniable** (≤2) or **coordinated and systematically aligned with state objectives** (≥3).

**Clarifying note:**
B7 captures outsourced coercion — private actors functioning as enforcement proxies. Formal regulatory enforcement scores B6, not B7. Coordination does not require written orders or explicit threats. Evidence may include: pattern timing, insider reporting, selective enforcement correlations, cross-sector consistency.

---

### Category C — Rule of Law & Courts (C1–C8)

#### C1 — Noncompliance with court orders *(Red-line checkpoint)*

**Definition:**
Failure by the executive branch or its agencies to comply with binding judicial orders, either openly or through deliberate evasion.

**Includes:**

- Ignoring injunctions or stays
- Continuing prohibited actions while litigation is pending
- Narrow or bad-faith "compliance theater"
- Arguing courts lack legitimacy or authority to bind the executive
- Materially delayed compliance without good-faith justification

**Excludes:**

- Good-faith appeals with compliance during review
- Genuine ambiguity resolved promptly by courts

**Why this is a red line:**
Authoritarianism begins when courts cease to function as binding constraints.

**Court Contempt Scoring Rule:**

A formal court contempt finding against executive actors is strong evidence of C1 and triggers mandatory scoring:

| Condition | C1 Score | Meaning |
| --------- | -------: | ------- |
| Formal contempt finding issued | ≥3 (mandatory floor) | Courts still bind, but only after confrontation |
| Compliance delayed, coerced, or repeated across agencies | 4 | Defiance becoming routine |
| Contempt orders ignored, courts declared non-binding, or sanctions fail | 5 | Courts no longer function as constraints |

**What does NOT trigger contempt scoring:**

- Threats of contempt without a formal finding
- Adverse rulings without noncompliance
- Appeals where the order is stayed and respected
- Ambiguous orders resolved in good faith
- Legislative contempt findings (score separately)

**C1 Severity Anchors:**

| Score | Anchor |
| ----: | ------ |
| **1** | Executive rhetoric criticizing courts; no defiance |
| **2** | Single instance of delayed, ambiguous, or partial compliance |
| **3** | Formal contempt finding OR repeated noncompliance resolved only after confrontation |
| **4** | Patterned defiance across agencies or jurisdictions; compliance only after sanctions |
| **5** | Open refusal to comply; courts declared non-binding; sanctions ineffective |

**Key discriminator:** Whether compliance is **voluntary** (≤2) or **coerced** (≥3).

**Clarifying note:**
This is a red-line checkpoint. The core question is whether courts can bind executive action. Criticism of rulings is excluded; defiance of rulings is included. Good-faith appeals with stayed orders are excluded. Time delays that are administratively necessary are excluded; delays designed to outlast litigation are included.

---

#### C2 — Retaliation against judges or courts

**Definition:**
Use or threat of political, financial, or personal consequences against the judiciary.

**Includes:**

- Impeachment threats tied to rulings
- Budget cuts or jurisdiction stripping
- Intimidation or harassment campaigns

**Excludes:**

- Lawful appeals or constitutional critiques
- Good-faith reform proposals

**Clarifying note:**
The distinction is between *disagreement with rulings* (excluded) and *punishment for rulings* (included). Criticizing a judge's reasoning is excluded; threatening a judge's position because of their ruling is included.

---

#### C3 — Politicized DOJ or prosecutors

**Definition:**
Law enforcement leadership acting on loyalty or partisan criteria rather than legal standards.

**Includes:**

- Explicit loyalty expectations
- Selective prosecution aligned with politics
- Interference in prosecutorial independence

**Excludes:**

- Policy priority shifts within legal bounds
- Personnel changes with documented cause

**Clarifying note:**
C3 overlaps with B6 (regulatory capture). C3 focuses on *criminal prosecution* used politically; B6 focuses on *regulatory enforcement* used politically. Both may score for coordinated campaigns. The key question is whether prosecution decisions are driven by evidence and law or by political alignment.

---

#### C4 — Undermining independent watchdogs

**Definition:**
Weakening or neutralizing inspectors general, ethics offices, or oversight bodies.

**Includes:**

- Firings without cause
- Budget starvation
- Restricting investigative authority

**Excludes:**

- Lawful restructuring with safeguards
- Performance-based removals

**Clarifying note:**
The key question is whether oversight bodies retain the *capacity* to investigate and report. Removing a single IG for documented misconduct is excluded; firing multiple IGs across agencies without cause is included. Budget cuts that affect all agencies equally are excluded; targeted cuts to oversight functions are included.

---

#### C5 — Expansion of unilateral executive power

**Definition:**
Legal reinterpretations that concentrate power in the executive beyond historical precedent.

**Includes:**

- Broad emergency power claims
- Refusal to recognize statutory limits
- Novel theories of unchecked authority

**Excludes:**

- Powers explicitly granted by statute
- Narrow interpretations upheld by courts

**Clarifying note:**
Distinguish between *using* existing executive power (excluded) and *claiming* new power not previously recognized (included). Courts upholding an interpretation after adversarial review suggests the claim was within bounds. Assertions of power that bypass judicial review or contradict binding precedent are included.

**Expanded guidance — Patterned use of emergency/exceptional authorities:**

Routine or repeated use of emergency or exceptional statutory powers for non-emergency purposes may score under C5 only when a **pattern of circumvention** is present, even if individual uses are technically authorized by statute.

Scoring requires **all of the following:**

1. **Pattern:** Repeated use of emergency or exceptional authorities (≥2 within 12 months, OR ≥3 across distinct policy domains), not a single aggressive invocation.

2. **Predicate mismatch:** The factual predicates contemplated by the statute (e.g., suddenness, temporariness, necessity) are materially absent or contradicted by available evidence.

3. **Bypass effect:** The use has the practical effect of bypassing congressional deliberation or substituting executive discretion for legislative choice on matters Congress has not affirmatively delegated in updated form.

**Exclusions:**

- A single aggressive use of existing authority, absent a pattern, does **not** trigger this checkpoint.
- Court review upholding a use does not automatically preclude scoring if the pattern demonstrates systematic legislative circumvention.

**Relationship to other checkpoints:** A1/A4 capture the narrative justification for emergency framing; C5 captures the structural effect of substituting executive discretion for legislative deliberation. These often co-occur but measure different phenomena.

---

#### C6 — Personal enrichment through office with impunity

**Definition:**
Use of public authority to generate personal or familial financial benefit, combined with the failure, suppression, or neutralization of oversight, disclosure, or enforcement mechanisms.

This checkpoint measures **impunity-backed self-dealing**, not corruption alone. The democratic harm arises when enrichment persists because accountability mechanisms no longer function.

**Includes:**

- Self-dealing contracts benefiting the officeholder or family
- Refusal to divest from businesses affected by policy decisions
- Steering government spending to owned or affiliated entities
- Family members receiving state roles, contracts, or access without merit
- Suppression, delay, or non-enforcement of financial disclosure requirements, emoluments rules, or conflict-of-interest statutes
- Retaliation against auditors, inspectors, or investigators examining finances

**Excludes:**

- Lawful private business activity unrelated to official action
- Passive investments disclosed and managed under ethics rules
- Allegations without corroboration or formal findings
- One-off ethics violations that are investigated and remedied
- Gray-area conflicts addressed through established compliance mechanisms

**International adaptation:** "Emoluments" and "conflict-of-interest statutes" refer to whatever local anti-corruption, financial disclosure, or public integrity mechanisms exist. Score based on whether those mechanisms bind the executive.

**C6 Severity Anchors:**

| Score | Anchor |
| ----: | ------ |
| **1** | Allegations or reporting of conflicts; disclosures incomplete but contested |
| **2** | Documented conflicts or self-dealing; investigations opened or oversight active |
| **3** | Repeated enrichment with weak, stalled, or politicized enforcement |
| **4** | Oversight bodies neutralized; disclosure requirements bypassed or ignored |
| **5** | Kleptocracy normalized; office treated as revenue-generating asset |

**Key discriminator:** Whether financial abuse is **constrained by law** (≤2) or **enabled by power** (≥3).

**Clarifying note:**
C6 requires the *combination* of enrichment and impunity. Enrichment alone (with functioning oversight) does not score highly; it is the neutralization of accountability that elevates scores. C6 overlaps with C4 (watchdog neutralization)—if C4 is high, C6 is more likely.

---

#### C7 — Use of pardon power to obstruct accountability

**Definition:**
Use of pardon or clemency powers to prevent, deter, or nullify lawful accountability for political allies or co-conspirators, or to signal that unlawful actions taken in service of power will not be punished.

This checkpoint measures **impunity**, not mercy. The democratic harm arises when pardons are used to obstruct justice, reward loyalists for unlawful conduct, or signal that power-serving misconduct will be shielded from consequences.

**Includes:**

- Pardoning individuals implicated in wrongdoing that benefits the officeholder
- Preemptive pardons issued to obstruct ongoing or anticipated investigations
- Self-pardons or pre-announced intent to self-pardon for conduct related to official duties
- Patterns of pardons disproportionately benefiting political allies or enforcers
- Public statements linking pardons to loyalty or service
- Clemency used to undermine court judgments or prosecutorial outcomes

**Excludes:**

- Ordinary clemency for humanitarian reasons
- Pardons following transparent review processes
- Pardons unconnected to the officeholder's personal or political interests
- Isolated controversial pardons without a pattern or signaling effect
- Clemency constrained by judicial or legislative oversight (where applicable)

**International adaptation:** Score functional equivalents (royal prerogative, amnesty decrees, prosecutorial immunity grants) that achieve the same accountability-blocking effect.

**C7 Severity Anchors:**

| Score | Anchor |
| ----: | ------ |
| **1** | Rhetoric or speculation about using pardons defensively |
| **2** | Isolated pardon with plausible political implications; accountability mechanisms still active |
| **3** | Repeated pardons of allies or co-conspirators; clear signaling effect |
| **4** | Preemptive pardons issued to block ongoing investigations or prosecutions; systematic use to shield allies from accountability |
| **5** | Pardon power normalized as enforcement shield; impunity expected; self-pardon attempted or announced |

**Key discriminator:** Whether pardons are **exceptional** (≤2) or **structural tools of protection** (≥3).

**Red-line status:** C7 is **not** a standalone red-line trigger. Pardon abuse can coexist with partial democratic forms. The existential danger arises when pardon abuse combines with enforcement failure, captured in the diagnostic flag below.

**Clarifying note:**
The key question is whether pardons function as *mercy* (excluded) or *impunity infrastructure* (included). A pardon for a terminally ill drug offender is excluded; a pardon for a political ally who refused to testify is included. The signaling effect matters—pardons that communicate "protect me and you will be protected" elevate scores.

---

#### C8 — Proactive judicial capture

**Definition:**
Systematic actions to preemptively control the judiciary by altering appointment processes, accelerating confirmations, expanding courts, lowering qualification thresholds, or otherwise reshaping judicial composition in ways that undermine independence—even absent retaliation for specific rulings.

**Why this matters:**
Independent courts are a core constraint on executive and legislative power. Their capture enables downstream abuses across all categories. Modern authoritarianism rarely fires judges en masse—it reprograms the courts. This checkpoint captures forward-looking judicial capture that C2 (retaliation) misses.

**Includes:**

- Norm-breaking acceleration of judicial appointments or confirmations
- Rule changes to appointment procedures that systematically advantage one coalition
- Court expansion designed to dilute existing judicial composition
- Lowering qualification standards to enable partisan appointments
- Mandatory retirement rule changes to create vacancies
- Restructuring court jurisdictions to sideline independent panels
- Creation of parallel court systems that bypass independent judiciary

**Excludes:**

- Ordinary appointments within established norms, even if ideologically consistent
- Legislative expansion of courts for legitimate workload reasons (with neutral implementation)
- Judicial reform with bipartisan support and transparent process
- Appointment of qualified judges who happen to share the appointer's judicial philosophy
- Filling vacancies at normal pace through established procedures

**C8 Severity Anchors:**

| Score | Anchor |
| ----: | ------ |
| **1** | Norm-breaking but lawful acceleration of appointments or confirmations, without procedural changes or overt partisan restructuring |
| **2** | Coordinated acceleration or rule reinterpretation that significantly advantages one coalition in judicial appointments, but remains reversible |
| **3** | Structural changes to appointment rules, court size, tenure norms, or qualification standards that reliably produce partisan-aligned courts |
| **4** | Institutionalized capture such that independent judicial review is predictably compromised across major issue areas |
| **5** | Effective elimination of judicial independence; courts function as regime instruments rather than checks on power |

**Key discriminator:** Whether judicial composition is being reshaped to **prevent future constraint** (≥3) versus **opportunistic advantage-taking within norms** (≤2).

**Clarifying note:**
C8 is distinct from C2 (retaliation after rulings) and D7 (electoral self-entrenchment). C8 captures proactive capture—reshaping courts *before* adverse rulings occur. If capture also blocks electoral accountability, score both C8 and D7. Lawfulness does not preclude scoring: lifetime appointments are high-risk instruments when strategically concentrated. The Hungary/Poland pattern (judicial capture preceding overt electoral manipulation) is the canonical example.

---

### Category D — Elections & Transfer of Power (D1–D12)

#### D1 — Federal interference in election administration

**Definition:**
Executive intrusion into state-run election processes.

**Includes:**

- Federal takeover or coercion of election officials
- DOJ/DHS overriding state authority
- Conditional funding tied to election control

**Excludes:**

- Court-ordered federal involvement
- Neutral compliance with voting rights law

**Clarifying note:**
The key distinction is between federal involvement that *protects* voting rights (excluded) and federal involvement that *overrides* state election authority (included). DOJ enforcement of the Voting Rights Act is excluded; DOJ pressure on state officials to change election outcomes is included.

---

#### D2 — Intimidation at polling or election offices

**Definition:**
Use or tolerance of threats, surveillance, or force around election operations.

**Includes:**

- Armed presence near polling sites
- Harassment of election workers
- Failure to prevent known intimidation

**Excludes:**

- Lawful security with clear neutrality
- Isolated non-systemic incidents

**Clarifying note:**
Scoring requires either direct involvement or *tolerance* of intimidation. Government failure to act against known intimidation is included. The key question is whether the intimidation affects the conduct of elections. Isolated incidents distant from polling places are excluded.

---

#### D3 — Systematic voter suppression

**Definition:**
Patterned policies that restrict voting access with partisan effect.

**Includes:**

- Selective ID requirements
- Polling place closures targeting demographics
- Aggressive purging without safeguards

**Excludes:**

- Neutral administrative changes
- Court-approved reforms

**Clarifying note:**
"Systematic" requires *pattern* evidence—multiple instances, jurisdictions, or coordinated policies. A single polling place closure for administrative reasons is excluded; closures targeting specific demographics across multiple locations are included. Partisan effect can be inferred from disparate impact data.

**Expanded guidance — Technology-enabled suppression:**

Technology-enabled suppression mechanisms (including algorithmic targeting, data-driven mass challenges, registration or poll-book system failures, and automated misinformation) may score under D3 only when suppression is **systematic and disparate in effect** and the state either causes, enables, or fails to remediate the harm.

Scoring requires **one of the following:**

1. **State nexus:** Deployment by state actors, contractors, or private actors acting with state encouragement or coordination meeting the B7 threshold; OR

2. **Failure to remediate:** Demonstrated, repeated, disparate impact on voter access where the state is on notice (via complaints, audits, litigation, or reporting) and does not promptly correct the failure.

**Exclusions:**

- Purely private technology-driven suppression without state nexus or state failure to remediate does **not** trigger D3 but may warrant watchpoints.
- Isolated technical failures that are promptly corrected are excluded.
- One-off glitches without disparate impact are excluded.

**Relationship to other checkpoints:** E3 captures coordinated narrative control; D12 captures foreign interference; B7 captures private enforcement proxies. D3 (with this expansion) captures systemic access failure via technology when governance fails to prevent or correct it.

---

#### D4 — Conditional legitimacy claims

**Definition:**
Claims that election outcomes are valid only if the incumbent or ruling party wins.

**Includes:**

- Preemptive fraud claims
- Refusal to commit to accepting results
- Delegitimization of opposition victories

**Excludes:**

- Legal challenges with evidence
- Post-election recount advocacy

**Clarifying note:**
The key question is whether the claim is *contingent* on winning. "If I lose, it's fraud" is included; "we have evidence of irregularities in this county" is excluded. Preemptive claims before votes are counted are strong evidence.

---

#### D5 — Attempts to delay, nullify, or refuse certification *(Red-line checkpoint)*

**Definition:**
Any attempt by executive actors, legislatures, or aligned institutions to prevent lawful certification of election results.

**Includes:**

- Pressuring officials not to certify results (public or private pressure)
- Legislative maneuvers to discard valid ballots
- Refusal to certify absent evidence of fraud
- Emergency justifications to suspend or delay certification

**Excludes:**

- Lawful recounts
- Court-ordered review processes conducted in good faith

**Why this is a red line:**
Certification is the final procedural safeguard of electoral legitimacy.

**D5 Severity Anchors:**

| Score | Anchor |
| ----: | ------ |
| **1** | Rhetoric questioning certification legitimacy; no action taken |
| **2** | Single official pressured or single locality targeted; effort fails or is abandoned |
| **3** | Multi-official pressure campaign OR certification delayed pending litigation resolved in good faith |
| **4** | Certification blocked or voided in one or more jurisdictions; legal basis contested |
| **5** | National-level certification refused or circumvented; alternative slates submitted or accepted |

**Key discriminator:** Whether certification proceeds **normally** (≤2) or requires **judicial or political intervention to complete** (≥3).

**Clarifying note:**
This is a red-line checkpoint. Distinguish between *challenging* results (legal, excluded) and *blocking* certification (extra-legal, included). Lawful recounts with deadlines are excluded; indefinite delays designed to prevent certification are included.

---

#### D6 — Politicized control over certification or electors *(Red-line checkpoint)*

**Definition:**
Efforts to assert partisan or executive control over elector selection, certification bodies, or vote transmission mechanisms.

**Includes:**

- Attempts to substitute alternate electors
- Executive interference in state certification authority
- Restructuring certification bodies for partisan control
- Federal override of state election administration

**Excludes:**

- Neutral administrative reforms
- Court-mandated procedural changes

**Why this is a red line:**
Once partisan actors control who certifies elections and under what rules, electoral outcomes become contestable regardless of actual votes cast.

**D6 Severity Anchors:**

| Score | Anchor |
| ----: | ------ |
| **1** | Rhetorical or exploratory discussion of altering certification authority without formal action; isolated statements by officials without procedural follow-through |
| **2** | Discrete procedural actions affecting certification authority (e.g., rule reinterpretations, personnel changes, or guidance) that advantage a partisan outcome but remain reversible and contested |
| **3** | Repeated or coordinated actions that consolidate partisan control over certification bodies or processes across jurisdictions or election cycles |
| **4** | Institutionalized control of certification mechanisms that materially constrains neutral administration or judicial review, making reversal difficult |
| **5** | Systemic politicization of certification machinery such that electoral outcomes can be overridden or nullified without meaningful legal remedy |

**Key discriminator:** Whether actions are **exploratory or contested** (≤2) or **coordinated and institutionalizing** (≥3).

**Clarifying note:**
This is a red-line checkpoint. D6 captures *control over certification machinery* (who certifies and under what rules), not interference with specific certification decisions (which is D5). The key question is whether partisan actors can determine who certifies elections and under what rules. Routine administrative changes, neutral modernization, or legally mandated restructuring with bipartisan support do not trigger this checkpoint absent evidence of partisan intent or effect. D6 is forward-looking (changing the rules); D5 is present-tense (refusing to certify). Both may score for the same event sequence.

---

#### D7 — Legislative self-entrenchment

**Definition:**
Changes to electoral rules, legislative procedures, or constitutional provisions designed to insulate incumbents from electoral accountability or make future reform structurally difficult.

**Includes:**

- Gerrymandering that produces durable, non-responsive seat distributions
- Supermajority requirements for electoral or procedural reform that lock in current advantages
- Quorum manipulation (e.g., changing quorum rules to prevent minority blocking power)
- Changes to ballot access requirements that disadvantage challengers or new parties
- Lame-duck power stripping (removing powers from incoming officials of opposing party)
- Court-packing or jurisdiction-stripping to protect electoral advantages
- Constitutional amendments designed primarily to entrench current majorities

**Excludes:**

- Neutral redistricting by independent commissions
- Good-faith procedural reforms with bipartisan support
- Supermajority requirements for genuinely fundamental changes (e.g., constitutional amendments) that apply symmetrically
- Standard legislative rules applied consistently across parties

**Scoring note:**
This checkpoint captures **structural entrenchment**, not ordinary legislative maneuvering. The key question is whether the change makes it materially harder for future majorities to reverse course through normal democratic means. Score higher when multiple entrenchment mechanisms are combined or when changes are rushed through with minimal deliberation.

**Expanded guidance — Gerrymanders:**
Gerrymandering alone scores D7 ≤2 unless it produces **structural lock-in**: seat distributions that remain unresponsive to vote share swings of 5+ percentage points, or that guarantee supermajorities despite minority vote share. Extreme partisan gerrymanders that meet these criteria may score 3–4. Score 5 requires gerrymandering combined with other entrenchment mechanisms (e.g., supermajority requirements, quorum manipulation) that together make reversal structurally implausible through normal electoral processes.

**Expanded guidance — Court-stripping:**
Jurisdiction-stripping that targets specific case categories to protect incumbents or entrenchment mechanisms scores D7 3–4 depending on scope. Court-packing combined with jurisdiction-stripping to immunize entrenchment from judicial review may score 5. Neutral changes to court jurisdiction with legitimate procedural rationale do not score D7.

**Clarifying note:**
D7 captures *structural* entrenchment (making it harder to lose power), not routine legislative advantage-seeking. The test is whether changes make reversal through normal democratic processes materially harder. Partisan bills that can be repealed by normal majorities are excluded; supermajority locks, gerrymandered safe majorities, and court-stripping that immunizes entrenchment are included.

---

#### D8 — Foreign coordination in domestic political processes

**Definition:**
Soliciting, accepting, or coordinating with foreign state or non-state actors to influence domestic elections, governance decisions, or political outcomes in ways that advantage incumbents or disadvantage opponents.

**Includes:**

- Soliciting foreign government assistance in election campaigns (intelligence, opposition research, direct support)
- Coordinating campaign strategy or messaging with foreign actors
- Accepting foreign campaign contributions or in-kind support
- Sharing non-public government information with foreign actors for political benefit
- Conditioning U.S. policy (aid, sanctions, investigations) on foreign actions benefiting domestic political interests
- Using diplomatic channels to pressure foreign governments to take actions affecting domestic opponents

**Excludes:**

- Routine foreign policy conducted through official channels
- Diplomatic negotiations that happen to have domestic political salience
- Private citizens' legal engagement with foreign entities
- Academic or journalistic exchanges
- Publicly disclosed meetings with foreign officials

**Evidentiary standard:**
Due to the difficulty of proving coordination and the sensitivity of allegations, scoring above 1 requires **documentary evidence** (communications, financial records, testimony under oath, or official findings by courts, congressional committees, or inspectors general). Circumstantial evidence alone is insufficient for scores ≥2.

**Clarifying note:**
This checkpoint captures **sovereignty compromise**—foreign actors gaining inappropriate influence over domestic political processes. The key question is whether domestic actors are trading policy, access, or electoral advantage for foreign assistance. Score higher when coordination is systematic, concealed, or involves hostile foreign powers.

**Severity anchors:**

| Score | Anchor |
| ----: | ------ |
| 1 | Credible allegation under investigation; no documentary proof yet |
| 2 | Isolated instance with documentary evidence (single meeting, communication, or transaction) |
| 3 | Pattern of coordination documented; multiple instances or ongoing relationship |
| 4 | Systematic coordination affecting policy decisions or electoral outcomes; official findings confirm |
| 5 | Sustained foreign influence operation with active incumbent participation; sovereignty materially compromised |

**Key discriminator:** Whether coordination is **alleged but unproven** (≤1), **documented but isolated** (2), or **systematic and ongoing** (≥3).

---

#### D9 — Legislative nullification of executive or judicial authority

**Definition:**
Legislative actions that void, defund, or structurally neutralize lawful executive or judicial functions—not through policy disagreement, but through mechanisms designed to prevent those branches from operating at all.

**Includes:**

- Refusal to hold hearings or votes on judicial nominees beyond normal delay (systematic blockade rather than case-by-case opposition)
- Defunding courts, agencies, or enforcement mechanisms to prevent them from functioning
- Legislative override of specific judicial rulings outside normal appellate processes
- Removing officials through mechanisms designed to circumvent constitutional removal procedures
- Declaring executive actions void without judicial process

**Excludes:**

- Normal legislative-executive policy disputes (e.g., refusing to fund a program)
- Confirmation delays based on specific nominee qualifications
- Lawful oversight, including subpoenas and investigations
- Impeachment proceedings conducted through constitutional processes
- Budget negotiations that affect agency priorities without eliminating core functions

**Scoring note:**
This checkpoint captures **legislative overreach**—attempts by the legislature to absorb or neutralize the constitutional functions of other branches. The key question is whether the action prevents a coordinate branch from performing its constitutional role, not whether the legislature disagrees with how that role is being performed. Score higher when nullification is systematic, targets constitutional functions (not policy choices), or when judicial remedies are themselves blocked.

**D9 Severity Anchors:**

| Score | Anchor |
| ----: | ------ |
| **1** | Rhetoric advocating nullification; no concrete action |
| **2** | Isolated nullification action (single nominee blockade, single agency defunding) that does not prevent branch function |
| **3** | Pattern of nullification actions OR single action that materially impairs branch function |
| **4** | Systematic nullification campaign; target branch operating in degraded capacity |
| **5** | Target branch unable to perform constitutional role; separation of powers functionally collapsed |

**Key discriminator:** Whether nullification is **isolated and symbolic** (≤2) or **materially impairs constitutional function** (≥3).

**Clarifying note:**
D9 captures *legislative overreach*—the legislature absorbing or neutralizing other branches' constitutional functions. Normal legislative-executive conflict (policy disagreements, funding disputes) is excluded. The test is whether the action prevents the target branch from performing its constitutional role.

---

#### D10 — Governance hostage-taking

**Definition:**
Deliberate creation of systemic crises to extract concessions unrelated to the crisis mechanism—weaponizing essential government functions as leverage.

**Includes:**

- Debt ceiling brinkmanship tied to unrelated policy demands
- Government shutdown threats to extract concessions on non-appropriations matters
- Threatening default or credit downgrade as negotiating leverage
- Blocking emergency funding (disaster relief, pandemic response) for political advantage
- Using must-pass legislation as vehicle for unrelated structural changes

**Excludes:**

- Normal budget negotiations, even contentious ones
- Policy riders on appropriations bills (standard legislative practice)
- Filibusters or procedural delays on individual bills
- Refusing to pass legislation the majority opposes on substance
- Shutdown disputes over appropriations levels or priorities

**Scoring note:**
This checkpoint captures **governance sabotage**—using essential functions as hostages rather than engaging in normal legislative bargaining. The key question is whether the demanded concession bears a reasonable relationship to the leverage mechanism. Demanding spending cuts in a budget negotiation is normal; demanding constitutional amendments in exchange for not defaulting is hostage-taking. Score higher when the threatened harm is systemic (default, prolonged shutdown), when demands are unrelated to the mechanism, or when the pattern is repeated.

**D10 Severity Anchors:**

| Score | Anchor |
| ----: | ------ |
| **1** | Rhetoric threatening governance hostage-taking; no concrete action |
| **2** | Single hostage-taking episode; crisis averted through negotiation before material harm |
| **3** | Hostage-taking causes material governance disruption (short shutdown, credit rating warning) OR repeated episodes |
| **4** | Prolonged disruption or pattern of escalating hostage-taking; governance capacity degraded |
| **5** | Hostage-taking causes systemic damage (default, extended shutdown with cascading effects); governance function fundamentally compromised |

**Key discriminator:** Whether hostage-taking is **averted or symbolic** (≤2) or **causes material governance harm** (≥3).

**Clarifying note:**
D10 captures *governance sabotage*—using essential functions as leverage for unrelated demands. The test is whether the demanded concession is reasonably related to the mechanism. Debt ceiling disputes about spending levels are excluded (related); debt ceiling threats to extract constitutional amendments are included (unrelated leverage).

---

#### D11 — Election infrastructure attacks

**Definition:**
Cyber or physical actions that compromise, degrade, or threaten the integrity, availability, or reliability of election infrastructure—including voter registration systems, voting machines, tabulation systems, or election reporting networks.

**Includes:**

- Intrusion into voter registration databases
- Malware deployment on voting machines or tabulation systems
- DDoS attacks on election night reporting
- Physical tampering with voting equipment
- Ransomware attacks on election administration systems
- Supply chain compromises targeting election technology vendors

**Excludes:**

- Routine IT security incidents unrelated to election systems
- Disinformation about election processes (score under E3)
- Policy disputes about election technology choices
- Procedural interference through legal channels (score under D1–D6)

**Why this matters:**
Election infrastructure is a prerequisite for democratic legitimacy. Attacks that materially undermine its integrity can invalidate outcomes regardless of voter intent. This checkpoint captures the threat regardless of attribution—foreign, domestic, or unknown actors all qualify.

**D11 Severity Anchors:**

| Score | Anchor |
| ----: | ------ |
| **1** | Probing, scanning, or low-level intrusion attempts without demonstrated impact or persistence |
| **2** | Confirmed intrusion or disruption affecting limited components, rapidly mitigated, with no evidence of data manipulation |
| **3** | Successful attack degrading voter rolls, tabulation, or reporting in one or more jurisdictions, requiring significant remediation |
| **4** | Coordinated or repeated attacks across multiple jurisdictions that materially impair election administration or delay certification |
| **5** | Systemic attack capable of altering, invalidating, or rendering election outcomes unreliable at scale |

**Key discriminator:** Whether the attack creates **material doubt about election integrity** (≥3) versus **technical inconvenience without integrity impact** (≤2).

**Clarifying note:**
Attribution is not required to score D11. Scoring is based on effect, not intent or sponsorship. If incumbent coordination exists, score both D11 and D8. D11 + D5/D6 (certification interference) signals extremely high concern. D11 + E3 (information capture) indicates integrity attack combined with narrative exploitation.

**Red-line status:** D11 is a conditional red-line checkpoint, activating at ≥3. At that threshold, material compromise of election infrastructure undermines outcome legitimacy regardless of voter intent or downstream certification processes. Lower scores (1–2) represent technical incidents without integrity impact and do not trigger red-line multipliers.

---

#### D12 — Foreign interference (non-collusive)

**Definition:**
Actions by foreign states or state-linked actors that intentionally disrupt, manipulate, or degrade democratic processes without evidence of coordination with domestic incumbents—including attacks on elections, public trust, participation, or institutional legitimacy.

**Why this matters:**
DBS measures democratic vulnerability, not moral blame. Harm to democratic processes matters even when the government is not responsible for it. This checkpoint captures external attacks on democracy that D8 (which requires incumbent coordination) cannot reach.

**Includes:**

- Disinformation campaigns targeting voters or turnout
- Covert funding of political movements or candidates
- Cyber operations against election-related systems below D11 thresholds
- Harassment or intimidation campaigns against election officials or civil society
- Narrative operations designed to delegitimize election outcomes
- Hack-and-leak operations timed to influence elections

**Excludes:**

- Foreign interference with incumbent coordination (score under D8)
- Election infrastructure attacks meeting D11 criteria (score under D11)
- Ordinary foreign government statements or diplomatic criticism
- Legitimate foreign media coverage of US elections
- Academic or policy exchanges, even if critical

**D12 Severity Anchors:**

| Score | Anchor |
| ----: | ------ |
| **1** | Isolated or low-level foreign influence attempts (e.g., sporadic disinformation, minor funding, limited cyber activity) with negligible demonstrated impact on participation, administration, or trust |
| **2** | Sustained foreign efforts affecting political discourse or participation in limited contexts (e.g., specific states, demographic groups, or platforms), but without clear institutional disruption |
| **3** | Coordinated foreign campaigns that materially degrade voter confidence, turnout, or election administration in one or more jurisdictions, requiring active mitigation |
| **4** | Large-scale or repeated foreign interference that undermines national election legitimacy, governance stability, or public trust across multiple jurisdictions or election cycles |
| **5** | Systemic foreign interference that renders democratic outcomes broadly contested, non-credible, or functionally non-determinative, even absent domestic collusion |

**Key discriminator:** Whether foreign actions produce **material democratic harm** (confidence, participation, administration, legitimacy) at ≥3, not whether domestic incumbents coordinated or benefited. This keeps D12 cleanly separated from D8 (collusion) and D11 (infrastructure attack).

**Clarifying note:**
Attribution to a specific foreign government is not required if credible evidence supports foreign-origin interference. Scoring is based on observed effects. If incumbent coordination or knowing facilitation is established, score both D12 and D8. If interference is primarily technical against election systems, also consider D11. The distinction: D8 captures *betrayal*, D11 captures *infrastructure compromise*, D12 captures *external attack*.

**Red-line status:** D12 is not a standalone red-line trigger. However, D12 ≥3 combined with D5/D6/D11 should be flagged as a compound legitimacy threat in interpretation.

---

#### D7/D9 Boundary Rule

D7 and D9 address different pathologies:

- **D7** captures **self-dealing entrenchment**—legislators changing rules to benefit themselves or their party
- **D9** captures **separation-of-powers collapse**—legislators absorbing or neutralizing other branches

When an action could score under either checkpoint, apply the **primary purpose test**:

- If the primary purpose is **incumbency protection or electoral advantage**, score D7
- If the primary purpose is **preventing another branch from functioning**, score D9
- If both purposes are clearly present, score the higher-scoring checkpoint and note the secondary in rationale

Example: Court-packing to protect gerrymandering → D7 (entrenchment is primary purpose; court manipulation is means)
Example: Defunding all federal courts to prevent ruling on executive actions → D9 (nullification is primary purpose)

---

### Category E — Information Environment Capture (E1–E4)

#### E1 — Retaliation against media

**Definition:**
State action punishing or threatening critical journalism.

**Includes:**

- License revocations
- Arrests or prosecutions
- Access bans tied to coverage

**Excludes:**

- Neutral enforcement of general laws
- Defamation rulings via courts

**Clarifying note:**
The key question is whether state action targets *journalism* or *criminal conduct*. Prosecution of a journalist for unrelated crimes is excluded; prosecution tied to reporting is included. Access bans must be connected to coverage content, not security or logistics.

---

#### E2 — State pressure on platforms

**Definition:**
Government coercion of digital platforms to suppress opposition content.

**Includes:**

- Threats of regulation tied to content
- Informal pressure campaigns
- Selective enforcement threats

**Excludes:**

- Lawful takedown requests
- Transparency-based moderation laws

**Clarifying note:**
E2 requires *government coercion*, not voluntary platform decisions. Platform content moderation decisions are excluded; government threats conditioning regulatory treatment on moderation outcomes are included. The key question is whether the government is using leverage.

---

#### E3 — State-aligned propaganda ecosystem

**Definition:**
Operational fusion of government messaging with supportive media outlets, characterized by **quid pro quo relationships** or **access dependency** that compromises editorial independence.

**Includes:**

- Coordinated talking points with evidence of state direction or pre-arrangement
- Preferential access explicitly conditioned on favorable coverage
- Media acting as enforcement adjuncts (e.g., publishing leaked investigation details to pressure targets)
- Coordinated amplification of enforcement narratives timed to state action
- Government funding or contracts contingent on editorial alignment
- Exclusive leaks weaponized against political opponents
- Synthetic media (deepfakes, voice clones) deployed at scale with state coordination or benefit
- Industrialized content farms using automated generation for state-aligned narratives
- Microtargeted persuasion or harassment campaigns driven by AI with state coordination
- Coordinated "flooding" attacks that degrade the information environment (availability disruption, not just persuasion)

**Excludes:**

- Normal press-government relationships (press briefings, interviews, press releases)
- Independent editorial alignment without coordination (outlets may share views with government without state direction)
- Routine access journalism without demonstrated quid pro quo
- Ideological affinity absent operational coordination

**Activation threshold:**
This checkpoint requires evidence of **bidirectional benefit**: the state gains favorable coverage, and the outlet gains access, funding, or protection not available to competitors. Mere ideological alignment is insufficient.

**Clarifying note:**
E3 captures *coordinated propaganda*, not ideological affinity. Fox News being favorable to a Republican administration is excluded (independent editorial choice); Fox News receiving exclusive leaks in exchange for attacking administration opponents is potentially included (operational coordination). Evidence of quid pro quo is required.

**Key discriminator:**
E3 scores based on whether the system enables coordinated, coercive narrative control (or legitimacy sabotage), **not** whether the content is AI-generated. AI tools are production and targeting accelerators; the checkpoint captures the propaganda ecosystem function regardless of production method. Score based on coordination and impact, not format.

---

#### E4 — Selective misinformation criminalization

**Definition:**
Use of misinformation laws to punish dissent selectively.

**Includes:**

- Vague definitions applied asymmetrically
- Criminal penalties for political speech
- National security framing for dissent

**Excludes:**

- Narrow, content-neutral laws
- Fraud or defamation enforcement

**Clarifying note:**
E4 captures *selective* criminalization—misinformation laws applied against political opponents but not allies. Content-neutral enforcement is excluded; asymmetric enforcement is included. The key evidence is whether similar speech by government allies faces prosecution.

---

### Category F — Security Services & Loyalty (F1–F7)

#### F1 — Civil service loyalty tests

**Definition:**
Requirement of political loyalty for career officials.

**Includes:**

- Ideological screening
- Removal for insufficient loyalty
- Reclassification to bypass protections

**Excludes:**

- Routine background checks and security clearances
- Standard ethics training or compliance reviews
- Performance evaluations tied to job duties
- Removals for documented misconduct or incompetence

**Clarifying note:**
Scoring requires political or ideological loyalty as an explicit or implicit condition of continued service.

---

#### F2 — Purges or politicization of military command *(Red-line checkpoint)*

**Definition:**
Removal, sidelining, or replacement of senior military leadership **based on political loyalty**, or pressure on commanders to align with partisan objectives.

**Includes:**

- Loyalty tests for generals or senior officers
- Politically motivated firings or forced retirements
- Public statements subordinating military duty to a leader rather than the Constitution
- Appointment of explicitly partisan loyalists to senior command roles

**Excludes:**

- Routine personnel rotations
- Performance-based removals with documented cause

**Why this is a red line:**
Once military leadership becomes partisan, democratic reversal becomes extraordinarily difficult.

**F2 Severity Anchors:**

| Score | Anchor |
| ----: | ------ |
| **1** | Executive rhetoric demanding military loyalty; no personnel action |
| **2** | Single senior officer removed or sidelined under contested circumstances |
| **3** | Multiple senior officers replaced in short succession; pattern emerges |
| **4** | Command structure systematically reorganized around loyalty criteria; dissenters marginalized |
| **5** | Military leadership publicly aligned with incumbent; constitutional role subordinated to personal loyalty |

**Key discriminator:** Whether command changes are **routine/performance-based** (≤2) or **systematically loyalty-driven** (≥3).

**Clarifying note:**
This is a red-line checkpoint. F2 captures *military* politicization specifically—civilian agencies are covered by F1 and F3. The critical question is whether military leadership is selected for professional competence or political loyalty. Routine personnel changes and documented performance issues are excluded.

---

#### F3 — Replacement of professionals with loyalists

**Definition:**
Systematic replacement of neutral experts with partisan appointees.

**Includes:**

- Rapid turnover tied to ideology
- Skill-irrelevant appointments
- Parallel loyalist chains of command

**Excludes:**

- Normal transition-period appointments
- Merit-based reorganization or restructuring
- Policy-aligned but professionally qualified appointees
- Changes with transparent selection criteria

**Clarifying note:**
This checkpoint activates when professional competence is subordinated to loyalty, not when leadership simply changes.

---

#### F4 — Security agencies used for personal political goals

**Definition:**
Use of intelligence or enforcement bodies for leader-specific interests.

**Includes:**

- Surveillance of opponents
- Protection of allies
- Retaliatory investigations

**Excludes:**

- Lawful counterintelligence investigations
- Court-authorized surveillance
- Neutral enforcement of criminal law
- Investigations initiated before political relevance

**Clarifying note:**
The key discriminator is personal or partisan benefit, not national security or public interest.

---

#### F5 — Parallel enforcement structures

**Definition:**
Tolerance or creation of irregular enforcement aligned with power.

**Includes:**

- Deputized militias
- Vigilante tolerance
- Irregular forces performing state functions

**Excludes:**

- Lawful deputization with statutory oversight
- Community policing programs
- Civilian auxiliary forces with clear accountability
- Emergency volunteer coordination for disasters

**Clarifying note:**
This checkpoint requires erosion of the state monopoly on legitimate force.

---

#### F6 — Leader-above-law doctrine

**Definition:**
Explicit claims that the leader is not bound by law.

**Includes:**

- Absolute immunity claims
- Open disregard for legality
- Personal authority superseding institutions

**Excludes:**

- Standard executive privilege claims within precedent
- Qualified immunity arguments adjudicated by courts
- Article II interpretations bounded by judicial review
- Temporary immunity claims subject to appeal

**Clarifying note:**
This is a red-line checkpoint. F6 activates only when claims assert that the leader cannot be investigated, prosecuted, or constrained even by courts. Standard executive privilege claims within precedent and qualified immunity arguments subject to judicial review do not trigger this checkpoint. The checkpoint is intentionally narrow: it captures *leader-above-law* doctrines, not ordinary separation-of-powers disputes.

**F6 Severity Anchors:**

| Score | Anchor |
| ----: | ------ |
| **1** | Rhetoric asserting broad executive authority; no specific immunity claims |
| **2** | Legal arguments for expanded immunity in specific contexts (e.g., during litigation) |
| **3** | Claims of absolute immunity from investigation or prosecution while in office |
| **4** | Actions taken on explicit theory that law does not bind the executive; courts challenged but not defied |
| **5** | Open assertion that courts cannot constrain the leader; immunity treated as permanent and total |

**Key discriminator:** Whether immunity claims are **contextual and subject to judicial review** (≤2) or **categorical and court-defying** (≥3).

---

#### F7 — Mass domestic surveillance infrastructure

**Definition:**
Deployment or systematic use of surveillance infrastructure against the domestic population at scale, without individualized suspicion or judicial oversight.

**Includes:**

- Warrantless bulk collection of domestic communications
- Mass facial recognition deployment at public gatherings, protests, or transit
- Social media monitoring programs targeting political content or dissent
- Cell-site simulators (IMSI-catchers) deployed without warrants at protests
- AI-driven behavioral prediction or "threat scoring" applied to citizens
- Location tracking databases covering general population movements

**Excludes:**

- Court-authorized surveillance of specific individuals
- Surveillance of foreign communications under FISA with proper oversight
- Routine security camera systems with access controls and retention limits
- Opt-in biometric systems (e.g., airport PreCheck, phone unlock)
- Law enforcement databases limited to persons under investigation or supervision

**Clarifying note:**
F7 measures surveillance *infrastructure and capability*, not targeting or motive (which is F4). The critical question is whether population-scale surveillance exists without meaningful judicial oversight. Court-authorized surveillance of specific individuals and surveillance of foreign communications under proper FISA oversight are excluded. F4 and F7 are not mutually exclusive—mass surveillance weaponized against political opponents scores on both.

**International Adaptation:**

In authoritarian contexts, score infrastructure directly (CCTV density, social credit systems, internet monitoring capacity) rather than waiting for specific targeting. In democracies, focus on deployment against political activity.

**Interaction note (F4/F7):**

F4 (Security agencies used for personal political goals) and F7 (Mass surveillance infrastructure) are **NOT mutually exclusive** and may both score on the same events. A mass surveillance system (F7) that is directed against political opponents (F4) scores on both checkpoints. The key distinction:

- F7 measures **infrastructure and capability** — the existence of population-scale surveillance capacity
- F4 measures **targeting and motive** — whether security apparatus serves personal/partisan rather than public interests

A surveillance state that exists but isn't politically weaponized scores on F7 only. Targeted surveillance of opponents without mass infrastructure scores on F4 only. Most dangerous: both score highly simultaneously.

**F7 Severity Anchors:**

| Score | Anchor |
| ----: | ------ |
| **1** | Surveillance expansion proposed or funded; no operational deployment against domestic population |
| **2** | Isolated deployment (single program, limited scope) without clear judicial oversight; OR revelation of existing surveillance exceeding legal authorization |
| **3** | Multiple surveillance systems operational against domestic population; OR mass surveillance deployed specifically at political gatherings/protests |
| **4** | Integrated surveillance ecosystem across programs; minimal judicial oversight in practice; chilling effect on political activity documented |
| **5** | Comprehensive domestic surveillance normalized; real-time population monitoring capability; surveillance data used for political purposes; oversight effectively non-existent |

**Key discriminator:** Whether surveillance is **targeted with judicial oversight** (≤1) or **mass-scale without meaningful constraints** (≥3).

---

## Appendix B — Red-Line Multiplier Logic

Red-line multipliers activate **only** when these **defined checkpoints** reach the specified thresholds.

**Default threshold:** Effective score ≥3 **and** base score ≥3 (repeated, expanded, or procedurally binding)

| Condition | Multiplier | Rationale |
| --------- | ---------- | --------- |
| C1 ≥ 3 AND B5 ≥ 3 | +10 | Courts repeatedly defied AND military actually deployed or persistently prepared |
| D5 ≥ 3 OR D6 ≥ 3 OR D11 ≥ 3 | +15 | Electoral legitimacy structurally undermined, not merely tested |
| F2 ≥ 3 | +10 | Military neutrality shows patterned loyalty reshaping |
| F6 ≥ 3 | +10 | Leader-above-law doctrine operationalized; accountability collapse |

**Exception Rule:** A base score of 2 may trigger a red-line only if the action is legally binding, immediately operative, and difficult to reverse. Such invocation must be explicitly justified.

These multipliers exist to prevent **false reassurance** from averaged scores when existential safeguards are breached.

---

## Appendix C — Version History

| Version | Date | Summary |
| ------- | ---- | ------- |
| v1.0 | — | Original framework |
| v1.1 | — | Expanded 0–5 scale, scope modifiers |
| v1.1a | 2025-01 | Persistence modifiers, actor tagging, severity anchors, cross-checkpoint rules, complete checkpoint definitions |
| v1.1b | 2026-01 | Major expansion: new checkpoints, temporal model, governance framework (see detailed changelog below) |
| v1.1c | 2026-01 | Red-line refinements, diagnostic flags, operational guidance (see detailed changelog below) |
| v1.1d | 2026-01 | Added B7 checkpoint, Asymmetric Information Environment flag, subnational scoring clarifications, C5/D3 expanded guidance |
| v1.1e | 2026-02 | EX_TA mechanical exclusion rules, checkpoint metadata, schema-1.4 output updates |

### v1.1e Detailed Changelog (2026-02)

**EX_TA Mechanical Exclusion (new):**

- Added EX_TA exclusion reason with mechanical eligibility checks (requires_state_nexus, elements_checked, NX=false, admissible evidence trigger doc types)
- Added checkpoint metadata (requires_state_nexus, elements list, NX element) to make EX_TA decidable

**Schema / Output Updates:**

- Added required `run_date` field and EX_TA fields (`mapped_checkpoint`, `elements_checked`, `evidence_trigger_doc_types`, `evidence_trigger_docs`)
- Added `excluded_events_context` derived output view
- Bumped JSON schema version to `schema-1.4`
- Added optional `topic` field to run output (for topic-specific runs)

### v1.1d Detailed Changelog (2026-01-20)

**New Checkpoint:**

- Added B7 (Coordinated private-sector coercion) for state-signaled enforcement through private entities

**New Diagnostic Flag:**

- Added Asymmetric Information Environment flag for AI-scale operations without proven coordination

**Scoring Changes:**

- Category B max increased from 30 to 35 (7 checkpoints)
- Formula updated: B denominator 30 → 35

**Subnational Scoring Clarifications (Section 4.8):**

- Added Subnational Non-Double-Count Rule: federal DBS captures federal-function harm; DBS-State captures residual state-specific harm; same event may appear in both logs with different point attribution
- Rewrote Federalization Rule with explicit 3-trigger format (EC Trigger, Diffusion Trigger, Coordination Trigger)
- Added EC Threshold Independence: ≥15% EC threshold is cumulative and time-independent (subject to decay/reversal)
- Added Rolling Window Definition: ≥3 states threshold uses rolling 12-month chain with mechanism-similarity requirement
- Added `attribution_scope` field to JSON schema event log for Non-Double-Count Rule enforcement

**Checkpoint Clarifications:**

- C5: Added expanded guidance for patterned use of emergency/exceptional authorities — allows scoring when pattern of circumvention is present (≥2 uses in 12 months or ≥3 across domains), predicate mismatch exists, and bypass effect on congressional deliberation is demonstrated; single aggressive uses explicitly excluded
- D3: Added expanded guidance for technology-enabled suppression — covers algorithmic targeting, system failures, and automated mechanisms when state nexus exists (via B7 threshold) or state fails to remediate demonstrated disparate harm; purely private suppression without state nexus excluded

**Backward Compatibility:**

- v1.1c → v1.1d: Fully compatible; v1.1d adds B7 checkpoint, Asymmetric Information Environment diagnostic flag, subnational scoring clarifications, and checkpoint clarifications but does not alter existing checkpoint definitions or base scoring
- B7 = 0 for historical runs (checkpoint did not exist)
- Subnational clarifications formalize implicit rules; no re-scoring required for existing runs

---

### v1.1c Detailed Changelog (2026-01-20)

**Red-Line Multipliers:**

- Added F6 as red-line checkpoint with +10 multiplier
- Updated stacking rule maximum from +35 to +45
- Updated international adaptation red-line table to include D11 and F6

**Diagnostic Flags (new):**

- State of Exception Flag (Schmitt Pattern) — A1 ≥ 3 AND A4 ≥ 3 AND F6 ≥ 3
- Coordinated Foreign–Domestic Election Subversion Flag — D8 ≥ 3 AND (D5/D6/D11 ≥ 3)
- External Attack on Electoral Legitimacy Flag — D12 ≥ 3 AND (D5/D6/D11 ≥ 3)

**Scoring Methodology Refinements:**

- Added modifier gating precedence rule (red-line exception overrides gating)
- Added institutionalization test (formal + functional) with decay eligibility matrix
- Clarified ABI formula (AMBIGUOUS included in denominator by design); added ABI_clear variant
- Enhanced D12 severity anchors with detailed examples and thresholds
- Expanded E3 to cover AI-generated content (deepfakes, content farms, microtargeting, flooding attacks)

**Operational Guidance:**

- Added LLM Scoring Revalidation guidance (trigger-based, scheduled, benchmark packet, drift thresholds)
- Added cooldown (14 days) and hysteresis rules for red-line reassessment

**Backward Compatibility:**

- v1.1b → v1.1c: Fully compatible; v1.1c adds red-line multipliers and diagnostic flags but does not alter checkpoint definitions or base scoring

---

### v1.1b Detailed Changelog (2026-01)

**New Checkpoints:**

- B6 (economic/regulatory capture)
- C6 (personal enrichment with impunity) with severity anchors, B6/C6 boundary rule
- C7 (pardon power abuse for impunity) with severity anchors, self-pardon guidance
- D7 (legislative self-entrenchment)
- D8 (foreign coordination in domestic political processes) with severity anchors, evidentiary standard
- D9 (legislative nullification of executive/judicial authority) with severity anchors
- D10 (governance hostage-taking) with severity anchors
- F7 (mass domestic surveillance infrastructure) with severity anchors, F4/F7 interaction note

**Checkpoint Refinements:**

- Tightened E3 definition
- Expanded D7 guidance for gerrymanders and court-stripping with explicit scoring thresholds
- Added D7/D9 boundary rule with primary purpose test
- Enhanced D6 severity anchors with detailed threshold conditions
- Standardized checkpoint structure (Definition, Includes, Excludes, Clarifying note) across all 41 checkpoints
- Added Clarifying notes to all checkpoints lacking them

**Scoring Methodology:**

- Raised red-line activation threshold from ≥2 to ≥3 with narrow exception
- Added modifier gating rule (base-dependent caps: 1→2, 2→4, 3+→5)
- Added modifier gating precedence rule (red-line exception overrides gating)
- Completed severity anchors for all red-line checkpoints (B5, C1, D5, D6, D11, F2, F6)
- Added F6 as red-line checkpoint with +10 multiplier; updated stacking rule (+35 → +45)
- Added C1 court contempt scoring rule with mandatory floor
- Replaced binary decay with graduated decay system (D0–D3 states)
- Added institutionalization test (formal + functional) with decay eligibility matrix
- Added formal confidence rating standard (High/Medium/Low) with source tiers
- Updated Category C formula from C/35 to C/40
- Added C8 (Proactive judicial capture) for forward-looking court control without retaliation
- Updated Category D formula from D/40 to D/60
- Added D11 (Election infrastructure attacks) for cyber/physical attacks on election systems
- Added D11 as conditional red-line checkpoint (activates at ≥3)
- Added D12 (Foreign interference, non-collusive) with detailed severity anchors
- Clarified ABI formula (AMBIGUOUS included in denominator by design); added ABI_clear variant
- Expanded E3 to cover AI-generated content (deepfakes, content farms, microtargeting, flooding attacks)

**Temporal Model:**

- Added Section 3.1 (three-layer temporal framework, decay rules)
- Added Section 3.2 (Run Modes & Temporal Consistency) with Rolling/Ad hoc/Snapshot modes
- Added Operational Tempo subsection (two-speed model: scheduled + event-triggered)
- Added Red-Line Reassessment Rule (72-hour trigger when red-line crosses <3→≥3)
- Added cooldown (14 days) and hysteresis rules to prevent oscillation-driven retriggering

**Governance & Operations:**

- Added Section 8.1 (Governance & Oversight) with analyst standards, event scorability, Event Log schema
- Added Section 8.2 (Publication & Communication Protocol) with tier model
- Added Event Unit Rule (Deduplication) with split criteria
- Added Constitutional Rulings & Legal Doctrine guidance
- Added Temporal Access Check for LLM knowledge cutoff handling
- Added Crisis Legitimacy Filter (CLF) for genuine emergency scoring guidance
- Added prompt versioning scheme (Prompt-vMAJOR.MINOR.PATCH) separate from DBS version
- Added `prompt_version` and `prompt_hash` fields to JSON schema
- Added LLM Scoring Revalidation guidance (trigger-based, scheduled, benchmark packet, drift thresholds)
- Added Source Archiving Policy with tiered preservation requirements
- Added archiving fields to JSON schema sources array (accessed_at, archived_url, archive_method, content_hash, quote_excerpt)

**Interpretation & Output:**

- Added Section 7 baseline risk note (10-20 typical for functioning democracies)
- Added Section 7.2 (DBS-A and Extreme Severity Bands) for ceiling compression resolution
- Added Section 7.3 (Trend Drivers and Watchpoints) with formal definitions
- Added Standard Interpretation Language for all six bands
- Added Appendix F (JSON Output Schema) with validation rules

**Diagnostic Flags:**

- Kleptocratic Consolidation Warning (C6 + C3/C4)
- Sovereignty Risk Flag (D8 ≥ 3)
- Accountability Collapse Flag (C7 + C1/C3/C4)
- Subnational Pattern Flag (≥3 states with D7 ≥ 3)
- Latent Coercive Capacity Flag (F7 + F4/C3/C4)
- Legislative Dysfunction Flag (D7/D9/D10 dominance)
- State of Exception Flag (Schmitt Pattern) — A1 ≥ 3 AND A4 ≥ 3 AND F6 ≥ 3
- Coordinated Foreign–Domestic Election Subversion Flag — D8 ≥ 3 AND (D5/D6/D11 ≥ 3)
- External Attack on Electoral Legitimacy Flag — D12 ≥ 3 AND (D5/D6/D11 ≥ 3)

**International & Historical:**

- Added Section 4.7 (international adaptation) with functional substitution table
- Added Section 4.8 (subnational scoring) with DBS-State variant
- Added Section 4.9 (Intent/Direction metadata) with tagging rules
- Added Appendix D (historical calibration methodology)
- Added Appendix E (inter-rater reliability protocol)

**LLM Prompt Updates:**

- Integrated intent tagging in Steps 3, 4, 6
- Added sector sweep table and event identification rules
- Added anchor citation rule for red-line checkpoints
- Added Clarifying note consultation constraint
- Added JSON output requirement
- Added trend drivers/watchpoints guidance

---

## Appendix D — Historical Calibration Methodology

DBS can be applied **retrospectively** to historical periods as a structured reconstruction. This is methodologically valuable for calibration (what score ranges actually mean) and validation (whether known authoritarian transitions cross red lines first).

### What Retroactive DBS Is and Isn't

Retroactive DBS is:

- Scoring what was **observable at the time**, using only contemporaneous evidence
- Applying the same rules, modifiers, and decay logic
- A way to ground modern score interpretation

Retroactive DBS is **not**:

- Using hindsight to inflate scores
- Outcome-based reasoning ("we now know he intended X")
- Scoring entire eras as single units

### Formal Method for Historical Application

**Step 1 — Define the temporal unit**

Pick a rolling window, just like modern use. Monthly or quarterly windows work best. Avoid "entire era" scoring. Ask: *"If DBS existed then, what would it have said at this moment?"*

**Step 2 — Use only contemporaneous sources**

This prevents hindsight bias.

*Allowed:*

- Newspapers of the time
- Court rulings and congressional records
- Official statements and proclamations
- Diaries/memoirs only for context, not scoring

*Disallowed:*

- Later interpretations or historical consensus
- Declassified information unknown at the time
- Outcome-based reasoning

**Step 3 — Apply decay and reversal rules**

Even historically:

- One-off actions that didn't repeat → decay
- Failed power grabs → lower future scores
- Institutional pushback matters

This is where many frameworks cheat. DBS doesn't.

**Step 4 — Record scores before known outcomes**

Do not score "end of era" first. Score trajectories through time, then compare to outcomes.

### Historical Calibration Cases

The following are **expected qualitative score bands**, not precise numbers. The value is in pattern, not exactitude.

#### Case 1: Nixon (1969–1974)

| Period | Est. DBS | Key Checkpoints | Interpretation |
| ------ | -------: | --------------- | -------------- |
| Early Nixon (1969–71) | 25–35 | A rising (enemy framing), C3/C4 low but nonzero (DOJ pressure, wiretaps) | Elevated stress, not drift |
| Peak Watergate (1973) | 45–55 | C1/C3/C4 spike (Saturday Night Massacre), A2/A3 high, B/F remain low | Backsliding underway |
| Resolution (1974) | ↓30–40 | Courts held, Congress acted, military stayed neutral | System recovered |

**Validation signal:** DBS should never label Nixon authoritarian — and it doesn't. He likely crosses into "backsliding underway" but never crosses authoritarian transition because courts held, Congress acted, and military stayed neutral.

#### Case 2: Reconstruction → Redemption (1865–1877)

| Period | Est. DBS | Key Checkpoints | Interpretation |
| ------ | -------: | --------------- | -------------- |
| Early Reconstruction (1866–70) | 40–50 | High B/D due to federal intervention | Pro-democracy intervention (see note) |
| Redemption rollback (1873–77) | 65–75 | D3/D5 spike (voter suppression), F5 (paramilitary tolerance), E1/E3 | Authoritarian retrenchment at state level |

**Important note:** DBS measures *risk to democratic constraints*, not intent. Early Reconstruction scores high because of federal coercion, even though the direction was pro-democracy. This forces a necessary interpretive layer.

**Key insight:** DBS correctly flags authoritarian retrenchment at the state level during Redemption, even as federal power retreats. This is a strength, not a flaw.

#### Case 3: Weimar Germany (1929–1933)

| Period | Est. DBS | Key Checkpoints | Interpretation |
| ------ | -------: | --------------- | -------------- |
| Pre-collapse (1929) | 45–55 | A1/A4 high (emergency decrees), C5 rising, elections functional | Severe stress |
| 1932 (pre-Hitler) | 65–75 | D4/D5 active, F1/F3 rising, courts weakening | Authoritarian transition zone |
| 1933 (Enabling Act) | 85+ | C1, D5/D6, F2/F5 — red lines triggered | Consolidated |

**Critical validation:** DBS should cross authoritarian transition *before* full dictatorship — and it does. Red-line checkpoints trigger first; averages lag behind; institutions fail before elections disappear.

### What Calibration Teaches

**1. Score ranges become meaningful**

After back-testing, you can say with grounding:

- "55 looks like late Watergate"
- "70 looks like late Weimar"
- "35 looks like rough but intact democracy"

**2. Red lines are validated**

In every historical authoritarian collapse, red-line checkpoints trigger first. This supports DBS's design choices.

**3. False positives get tested**

Check whether DBS would have flagged:

- Britain in the 1970s (economic crisis, emergency powers)
- U.S. during the Civil Rights era (federal intervention)
- France during the Algerian War

If scores later receded and democracy survived, that's calibration, not confirmation bias.

### Best Practice

- Treat historical cases as **benchmark profiles**, not training data
- Publish score trajectories, category breakdowns, and points of reversal or failure
- Use them to interpret current scores **conservatively**

Example: *"Current DBS ~42 resembles Nixon 1971, not Weimar 1932."*

A framework this explicit invites falsification — which is exactly what makes it credible.

### ES Band Historical Calibration

For cases where DBS = 100 and DBS-A (analytical) is reported, the following historical examples provide illustrative calibration for Extreme Severity bands. **These comparisons are illustrative; they should not be used to assert equivalence between contemporary and historical cases.**

| ES Band | DBS-A Range | Historical Examples |
| ------- | ----------- | ------------------- |
| **ES1** | 100–114 | Late Weimar 1933 (Enabling Act period); early Orbán consolidation (2012–2014) |
| **ES2** | 115–134 | Nazi Germany 1934 (Night of Long Knives through Nuremberg Laws); Venezuela 2017–2019 |
| **ES3** | 135+ | Nazi Germany 1938+ (Kristallnacht onward); Stalin's USSR; North Korea |

**Interpretation guidance:**

- ES1 represents the immediate post-transition period where formal democratic structures may still exist but are no longer constraining
- ES2 represents active consolidation where opposition is being systematically eliminated
- ES3 represents totalitarian saturation where all institutional constraints have collapsed and the state exercises arbitrary power

These calibrations are approximate and should be updated as more rigorous historical DBS applications are conducted.

---

## Appendix E — Inter-Rater Reliability & Robustness Protocol

This appendix defines how DBS scores are validated, what variance is acceptable, how often validation occurs, and what to do when agreement fails.

### E.1 Two Validation Tests (Both Required)

#### Test A — Controlled IRR (Reliability Test)

**Question:** Do different analysts score the same evidence the same way?

**Setup:**

- Identical source corpus
- Same jurisdiction and rolling window
- Raters: Human–human, LLM–LLM, or Human–LLM

**Goal:** Test scoring rules, anchors, and judgment consistency

**Interpretation:** Disagreement reflects scoring ambiguity, not information asymmetry

This is the **minimum standard** for claiming DBS is reliable.

#### Test B — Open-Corpus Convergence (Robustness Test)

**Question:** Does DBS converge even when analysts choose different credible sources?

**Setup:**

- Different but overlapping source sets
- Each rater's source set must share **≥50% Tier-1 sources** for comparability
- Each rater must use ≥1 Tier-1 source per scored event

**Goal:** Test whether DBS depends on which outlet you read

**Interpretation:** Disagreement reflects model fragility or source bias sensitivity

This is the **stronger validity test** for public or comparative use.

---

### E.2 Reliability Standards by Rater Type

| Pairing | Target Δ | Acceptable Δ | Red-Line Agreement | Failure Signal |
| ------- | -------: | -----------: | ------------------ | -------------- |
| Human–Human | ≤ ±5 | ≤ ±7 | 100% required | Δ > 7 repeatedly |
| LLM–LLM | ≤ ±4 | ≤ ±6 | 100% required | Δ > 6 or inconsistent checkpoint ID |
| Human–LLM | ≤ ±6 | ≤ ±8 | 100% required | Systematic bias in one direction |

**LLM test constraint:** Temperature and other generation parameters must be held constant across runs.

**Red-line rule:** Red-line activation must agree 100% for publication. Any red-line disagreement triggers mandatory remediation before release.

**Tier-crossing rule:** Disagreements that cross interpretation tiers (e.g., one rater at 38, another at 42) trigger mandatory review regardless of Δ magnitude.

---

### E.3 Acceptable Variance

| Δ DBS | Interpretation |
| ----: | -------------- |
| 0–4 | Excellent agreement |
| 5–7 | Good / acceptable |
| 8–10 | Marginal — investigate |
| >10 | Unacceptable — remediation required |

**Note:** A Δ of 6 where both raters land in the same tier is far less concerning than a Δ of 6 that crosses tiers or red-lines.

---

### E.4 Validation Frequency

IRR validation is required:

- **Quarterly**, or
- **After any methodological update** (anchors, thresholds, modifiers), or
- **Before publishing DBS scores externally**

DBS may not be published externally without at least one successful IRR validation with Δ ≤ 7.

---

### E.5 Remediation Protocol (When Δ > 10)

When unacceptable divergence occurs:

**Step 1 — Freeze publication**

No DBS score is released until reconciliation occurs.

**Step 2 — Identify disputed checkpoints**

Create a table of checkpoints scored differently, score deltas, and evidence cited.

**Step 3 — Classify the disagreement**

Each dispute must fall into one category:

- Anchor ambiguity
- Source interpretation
- Modifier application
- Checkpoint misclassification

**Step 4 — Refine guidance**

If ambiguity is systemic: tighten anchors, add an exclude, or clarify modifier thresholds.

**Step 5 — Re-score independently**

Repeat the scoring with updated guidance.

**Step 6 — Document the fix**

Record what changed, why, and how it reduced variance. This turns disagreement into framework improvement.

---

### E.6 Single-Rater Confidence Bands

When only one scorer is available, compute a principled confidence band using the **Borderline Judgment Count (BJC)**.

**Definition:** A judgment is borderline if anchor descriptions for **adjacent scores both partially fit** the observed behavior (e.g., score 2 vs 3, or P1 vs P2).

**Formula:**

```text
Confidence band = ± (2 + number of borderline judgments)
Cap at ±7
```

**Examples:**

- 1 borderline judgment → ±3
- 3 borderline judgments → ±5
- 5+ borderline judgments → ±7 (max)

**Integration with Confidence Ratings:** The per-checkpoint confidence ratings (High/Medium/Low) defined in the LLM Prompt (Step 3) are additive inputs to the BJC calculation:

- **High confidence** checkpoints contribute 0 borderline judgments to the count
- **Medium confidence** checkpoints contribute 1 borderline judgment (by definition, Medium indicates one borderline call)
- **Low confidence** checkpoints contribute 2 borderline judgments (by definition, Low indicates 2+ borderline calls)

This ensures the confidence band reflects both anchor ambiguity and source quality in a unified metric.

**Mandatory disclosure:** When publishing a single-rater DBS, list which checkpoints were borderline and explain why.

---

### E.7 Recommended Reporting Format

```text
DBS-v1.1e Rolling (60-day window, run date: 2026-02-28): 47 (confidence band: 43–52)
Tier: Backsliding underway
Red-lines: None triggered
Borderline checkpoints: B4 (2/3), A1 (3/4), P-modifier for B1
```

This format communicates:

- The run mode and temporal window
- Where the score sits
- How solid it is
- Where disagreement would likely arise

---

## Appendix F — JSON Output Schema

When machine-readable output is required, DBS runs should produce valid JSON conforming to this schema. This enables automated tracking, inter-rater reliability validation, and trend analysis.

### F.1 Schema Version

- **Schema version:** `schema-1.4` (format structure)
- **DBS version:** `DBS-v1.1e` (methodology)

Update `schema_version` when field structure changes. Update `dbs_version` when scoring rules or anchors change.

### F.2 JSON Schema (Draft 2020-12)

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "https://dbs.example/schema/dbs-run.v1.4.json",
  "title": "DBS Run Output",
  "type": "object",
  "required": [
    "schema_version",
    "dbs_version",
    "prompt_version",
    "run_id",
    "run_date",
    "mode",
    "window",
    "jurisdiction",
    "capability",
    "scores",
    "categories",
    "events",
    "excluded_events_context",
    "audit",
    "interpretation"
  ],
  "properties": {
    "schema_version": {
      "type": "string",
      "description": "Version of this JSON schema.",
      "pattern": "^schema-\\d+\\.\\d+(?:\\.\\d+)?$"
    },
    "dbs_version": {
      "type": "string",
      "description": "DBS methodology version (e.g., DBS-v1.1e).",
      "pattern": "^DBS-v\\d+\\.\\d+(?:[a-z])?$"
    },
    "prompt_version": {
      "type": "string",
      "description": "Version of the LLM prompt used to generate this run (e.g., Prompt-v1.2.0).",
      "pattern": "^Prompt-v\\d+\\.\\d+\\.\\d+$"
    },
    "prompt_hash": {
      "type": ["string", "null"],
      "description": "Optional SHA-256 hash of the exact prompt text for reproducibility verification.",
      "pattern": "^[a-f0-9]{64}$"
    },
    "topic": {
      "type": ["string", "null"],
      "description": "Optional topic label for subject-specific runs (e.g., a leader or country)."
    },
    "run_id": {
      "type": "string",
      "description": "Unique ID for this run (UUID recommended)."
    },
    "run_date": {
      "type": "string",
      "format": "date",
      "description": "Run date used for header reporting (YYYY-MM-DD)."
    },
    "created_at_utc": {
      "type": "string",
      "format": "date-time"
    },
    "mode": {
      "type": "string",
      "enum": ["rolling", "snapshot", "ad_hoc"],
      "description": "Temporal mode of the run."
    },
    "window": {
      "type": "object",
      "required": ["start_date", "end_date", "days"],
      "properties": {
        "start_date": { "type": "string", "format": "date" },
        "end_date": { "type": "string", "format": "date" },
        "days": { "type": "integer", "minimum": 1 }
      },
      "additionalProperties": false
    },
    "jurisdiction": {
      "type": "object",
      "required": ["type", "name"],
      "properties": {
        "type": { "type": "string", "enum": ["federal", "state", "international"] },
        "name": { "type": "string" },
        "subunit": { "type": "string", "description": "Optional, e.g., state code WI" }
      },
      "additionalProperties": false
    },
    "capability": {
      "type": "object",
      "required": ["has_web_access", "knowledge_cutoff"],
      "properties": {
        "has_web_access": { "type": "boolean" },
        "knowledge_cutoff": {
          "type": ["string", "null"],
          "description": "If has_web_access=false, state cutoff date (YYYY-MM).",
          "pattern": "^\\d{4}-\\d{2}$"
        },
        "notes": { "type": "string" }
      },
      "additionalProperties": false
    },
    "scores": {
      "type": "object",
      "required": ["dbs_capped", "confidence_band", "red_lines_triggered", "diagnostic_flags"],
      "properties": {
        "dbs_capped": { "type": "integer", "minimum": 0, "maximum": 100 },
        "dbs_uncapped": {
          "type": ["number", "null"],
          "minimum": 0,
          "description": "Only required when dbs_capped=100; otherwise null."
        },
        "confidence_band": {
          "type": "object",
          "required": ["low", "high", "basis"],
          "properties": {
            "low": { "type": "integer", "minimum": 0, "maximum": 100 },
            "high": { "type": "integer", "minimum": 0, "maximum": 100 },
            "basis": {
              "type": "string",
              "enum": ["single_rater_borderline", "inter_rater_envelope", "mixed"]
            }
          },
          "additionalProperties": false
        },
        "tier_label": {
          "type": "string",
          "enum": [
            "Normal democratic conflict",
            "Elevated stress / norm breaking",
            "Backsliding underway",
            "Severe backsliding",
            "Authoritarian transition zone",
            "Consolidated authoritarian control likely"
          ],
          "description": "Human-readable tier label matching Section 7 interpretation bands."
        },
        "es_band": {
          "type": ["string", "null"],
          "enum": [null, "ES1", "ES2", "ES3"],
          "description": "Extreme severity band; only valid when dbs_capped=100."
        },
        "red_lines_triggered": {
          "type": "array",
          "items": { "type": "string", "pattern": "^[A-F]\\d{1,2}$" },
          "description": "List of red-line checkpoint IDs that triggered (e.g., C1, D5, D11)."
        },
        "diagnostic_flags": {
          "type": "array",
          "items": {
            "type": "string",
            "enum": [
              "kleptocratic_capture",
              "foreign_coordination_documented",
              "sovereignty_electoral_compromise",
              "accountability_collapse_accelerating",
              "subnational_entrenchment_detected",
              "latent_coercive_capacity_activated",
              "legislative_dysfunction_driving_D",
              "state_of_exception_pattern",
              "foreign_domestic_subversion",
              "external_legitimacy_attack",
              "asymmetric_information_environment"
            ]
          },
          "description": "Active diagnostic flags for this run."
        }
      },
      "additionalProperties": false
    },
    "categories": {
      "type": "array",
      "description": "Category totals and drivers.",
      "items": {
        "type": "object",
        "required": ["id", "max", "score", "drivers"],
        "properties": {
          "id": { "type": "string", "pattern": "^[A-F]$" },
          "max": { "type": "integer", "minimum": 1 },
          "score": { "type": "integer", "minimum": 0 },
          "drivers": {
            "type": "array",
            "items": {
              "type": "object",
              "required": ["checkpoint_id", "points"],
              "properties": {
                "checkpoint_id": { "type": "string", "pattern": "^[A-F]\\d{1,2}$" },
                "points": { "type": "number", "minimum": 0 }
              },
              "additionalProperties": false
            }
          }
        },
        "additionalProperties": false
      }
    },
    "events": {
      "type": "array",
      "description": "Event consideration log (scored/excluded/deferred). One entry per event; multiple sources listed within.",
      "items": {
        "type": "object",
        "required": ["event_id", "title", "date", "status", "sources", "tags"],
        "properties": {
          "event_id": {
            "type": "string",
            "description": "Unique ID (hash of canonical_title + primary_action_date + primary_instrument_type recommended for deduplication)."
          },
          "title": { "type": "string" },
          "date": { "type": "string", "format": "date" },
          "status": {
            "type": "string",
            "enum": ["scored", "excluded", "deferred", "retracted"]
          },
          "exclusion_reason": {
            "type": ["string", "null"],
            "enum": [
              null,
              "INSUFFICIENT_CORROBORATION",
              "FAILS_EXCLUDES_CLAUSE",
              "OUTSIDE_SCORING_WINDOW",
              "PURELY_RHETORICAL",
              "DUPLICATE_EVENT",
              "CRISIS_LEGITIMACY_FILTER",
              "EX_TA"
            ],
            "description": "Reason code for excluded events."
          },
          "mapped_checkpoint": {
            "type": ["string", "null"],
            "pattern": "^[A-F]\\d{1,2}$",
            "description": "Checkpoint this event maps to for exclusion reasoning (required for EX_TA)."
          },
          "elements_checked": {
            "type": ["object", "null"],
            "description": "Element checklist per Appendix A metadata (required for EX_TA). Unknown values disqualify EX_TA.",
            "patternProperties": {
              "^(E\\d+|NX)$": {
                "type": ["boolean", "string"],
                "enum": [true, false, "unknown"]
              }
            },
            "additionalProperties": false
          },
          "evidence_trigger_doc_types": {
            "type": ["array", "null"],
            "description": "Allowed EX_TA trigger document types (required for EX_TA).",
            "items": {
              "type": "string",
              "enum": [
                "PLATFORM_ENFORCEMENT_NOTICE",
                "PLATFORM_TRANSPARENCY_REPORT_ENTRY",
                "COURT_EXHIBIT_TECHNICAL",
                "COURT_FINDING_FACT",
                "REGULATOR_ORDER_OR_FINDING",
                "CARRIER_STATUTORY_DISCLOSURE"
              ]
            },
            "minItems": 1
          },
          "evidence_trigger_docs": {
            "type": ["array", "null"],
            "description": "Document metadata for EX_TA evidence triggers.",
            "items": {
              "type": "object",
              "required": ["doc_type", "issuer_type", "issuer_name", "issued_date", "reference_id"],
              "properties": {
                "doc_type": {
                  "type": "string",
                  "enum": [
                    "PLATFORM_ENFORCEMENT_NOTICE",
                    "PLATFORM_TRANSPARENCY_REPORT_ENTRY",
                    "COURT_EXHIBIT_TECHNICAL",
                    "COURT_FINDING_FACT",
                    "REGULATOR_ORDER_OR_FINDING",
                    "CARRIER_STATUTORY_DISCLOSURE"
                  ]
                },
                "issuer_type": {
                  "type": "string",
                  "enum": ["platform", "court", "regulator", "carrier"]
                },
                "issuer_name": { "type": "string" },
                "issued_date": { "type": "string", "format": "date" },
                "reference_id": { "type": "string" },
                "url": { "type": ["string", "null"] },
                "notes": { "type": ["string", "null"] }
              },
              "additionalProperties": false
            }
          },
          "primary_source_ref": {
            "type": ["string", "null"],
            "description": "Index or ID of most authoritative source in sources[] (e.g., primary document)."
          },
          "cluster_id": {
            "type": ["string", "null"],
            "description": "Optional grouping ID for related events (e.g., 'dhs-protest-deployments-2026'). Use lowercase-slug format."
          },
          "attribution_scope": {
            "type": ["string", "null"],
            "enum": ["federal_function", "state_residual", "federal_only", "state_only", null],
            "description": "Scope of point attribution per Non-Double-Count Rule. 'federal_function' = points for federal DBS impact from a state action; 'state_residual' = points for DBS-State impact not captured federally; 'federal_only'/'state_only' = event affects only that level. Null for unambiguous single-scope events."
          },
          "summary": { "type": "string" },
          "tags": {
            "type": "object",
            "required": ["intent_direction", "actor"],
            "properties": {
              "intent_direction": {
                "type": "string",
                "enum": ["PRO-DEM", "ANTI-DEM", "AMBIGUOUS"]
              },
              "actor": {
                "type": "string",
                "enum": ["EXEC", "LEG", "JUD", "MIXED", "SUBNAT", "FOREIGN", "OTHER"]
              }
            },
            "additionalProperties": false
          },
          "confidence": {
            "type": "string",
            "enum": ["High", "Medium", "Low"],
            "description": "Evidence confidence for the event overall."
          },
          "sources": {
            "type": "array",
            "minItems": 1,
            "items": {
              "type": "object",
              "required": ["tier", "outlet", "type"],
              "properties": {
                "tier": { "type": "string", "enum": ["Tier-1", "Tier-2", "Primary"] },
                "outlet": { "type": "string" },
                "type": { "type": "string", "enum": ["news", "document", "court", "transcript", "other"] },
                "language": { "type": "string", "description": "ISO 639-1 preferred (e.g., en, fr)." },
                "title": { "type": "string" },
                "author": { "type": ["string", "null"], "description": "Author name if available." },
                "published_at": { "type": "string", "format": "date-time" },
                "url": { "type": "string" },
                "accessed_at": { "type": ["string", "null"], "format": "date-time", "description": "When the source was accessed for this run." },
                "archived_url": { "type": ["string", "null"], "description": "URL to archived version (e.g., archive.org snapshot)." },
                "archive_method": { "type": ["string", "null"], "enum": ["web_archive", "pdf_capture", "official_pdf", "screenshot_capture", "text_excerpt", null], "description": "How the source was archived." },
                "content_hash": { "type": ["string", "null"], "pattern": "^sha256:[a-f0-9]{64}$", "description": "SHA-256 hash of captured content for verification." },
                "local_capture_ref": { "type": ["string", "null"], "description": "Path or ID for stored PDF/screenshot artifact." },
                "quote_excerpt": { "type": ["string", "null"], "description": "Short excerpt (≤50 words) of specific text relied upon for scoring." }
              },
              "additionalProperties": false
            }
          },
          "checkpoint_scores": {
            "type": "array",
            "description": "Scores for checkpoints triggered by this event.",
            "items": {
              "type": "object",
              "required": [
                "checkpoint_id",
                "base_score",
                "modifiers",
                "decay",
                "effective_score",
                "provisional",
                "notes"
              ],
              "properties": {
                "checkpoint_id": { "type": "string", "pattern": "^[A-F]\\d{1,2}$" },
                "base_score": { "type": "integer", "minimum": 0, "maximum": 5 },
                "modifiers": {
                  "type": "object",
                  "required": ["scope", "persistence"],
                  "properties": {
                    "scope": { "type": "integer", "minimum": 0, "maximum": 2 },
                    "persistence": { "type": "integer", "minimum": 0, "maximum": 2 }
                  },
                  "additionalProperties": false
                },
                "decay": {
                  "type": "object",
                  "required": ["state", "delta"],
                  "properties": {
                    "state": { "type": "string", "enum": ["D0", "D1", "D2", "D3"] },
                    "delta": { "type": "integer", "enum": [0, -1, -2] }
                  },
                  "additionalProperties": false
                },
                "effective_score": { "type": "integer", "minimum": 0, "maximum": 5 },
                "provisional": { "type": "boolean" },
                "confidence": { "type": "string", "enum": ["High", "Medium", "Low"] },
                "notes": { "type": "string" }
              },
              "additionalProperties": false
            }
          }
        },
        "additionalProperties": false
      }
    },
    "excluded_events_context": {
      "type": "array",
      "description": "Derived view of excluded events with exclusion_reason codes starting with EX_.",
      "items": {
        "type": "object",
        "required": ["event_id", "exclusion_reason", "mapped_checkpoint", "evidence_trigger_doc_types"],
        "properties": {
          "event_id": { "type": "string" },
          "exclusion_reason": { "type": "string", "pattern": "^EX_[A-Z0-9_]+$" },
          "mapped_checkpoint": { "type": "string", "pattern": "^[A-F]\\d{1,2}$" },
          "evidence_trigger_doc_types": {
            "type": "array",
            "items": {
              "type": "string",
              "enum": [
                "PLATFORM_ENFORCEMENT_NOTICE",
                "PLATFORM_TRANSPARENCY_REPORT_ENTRY",
                "COURT_EXHIBIT_TECHNICAL",
                "COURT_FINDING_FACT",
                "REGULATOR_ORDER_OR_FINDING",
                "CARRIER_STATUTORY_DISCLOSURE"
              ]
            },
            "minItems": 1
          }
        },
        "additionalProperties": false
      }
    },
    "audit": {
      "type": "object",
      "required": ["domain_sweep", "disagreements"],
      "properties": {
        "domain_sweep": {
          "type": "array",
          "description": "Required sector sweep coverage.",
          "items": {
            "type": "object",
            "required": ["domain", "categories", "result"],
            "properties": {
              "domain": {
                "type": "string",
                "enum": [
                  "Executive actions",
                  "Legislative actions",
                  "Courts and legal compliance",
                  "Elections and certification",
                  "Security services / law enforcement",
                  "Media / information control / surveillance",
                  "Oversight institutions",
                  "Foreign interaction"
                ]
              },
              "categories": {
                "type": "array",
                "items": { "type": "string", "pattern": "^[A-F]$" }
              },
              "result": { "type": "string", "enum": ["events_found", "none_detected"] },
              "notes": { "type": "string" }
            },
            "additionalProperties": false
          }
        },
        "disagreements": {
          "type": "array",
          "description": "Structured disagreement log.",
          "items": {
            "type": "object",
            "required": ["checkpoint_id", "event_id", "range", "boundary", "notes"],
            "properties": {
              "checkpoint_id": { "type": "string", "pattern": "^[A-F]\\d{1,2}$" },
              "event_id": { "type": "string" },
              "range": {
                "type": "object",
                "required": ["low", "high"],
                "properties": {
                  "low": { "type": "integer", "minimum": 0, "maximum": 5 },
                  "high": { "type": "integer", "minimum": 0, "maximum": 5 }
                },
                "additionalProperties": false
              },
              "boundary": {
                "type": "string",
                "description": "E.g., 'rhetoric↔isolated_action' or 'isolated↔repeated'."
              },
              "notes": { "type": "string" }
            },
            "additionalProperties": false
          }
        },
        "scoring_notes": {
          "type": "array",
          "items": { "type": "string" },
          "description": "Run-level notes (e.g., debunked items, missing sources)."
        }
      },
      "additionalProperties": false
    },
    "interpretation": {
      "type": "object",
      "required": ["narrative", "intent_profile", "trend_summary"],
      "properties": {
        "narrative": { "type": "string" },
        "intent_profile": {
          "type": "object",
          "required": ["method", "pro_dem", "anti_dem", "ambiguous"],
          "properties": {
            "method": { "type": "string", "enum": ["score_weighted"] },
            "pro_dem": { "type": "number", "minimum": 0, "maximum": 1 },
            "anti_dem": { "type": "number", "minimum": 0, "maximum": 1 },
            "ambiguous": { "type": "number", "minimum": 0, "maximum": 1 }
          },
          "additionalProperties": false
        },
        "abi": {
          "type": ["number", "null"],
          "minimum": -1,
          "maximum": 1,
          "description": "Aggregate Intent Balance indicator; optional."
        },
        "pathway_dominance": {
          "type": "object",
          "required": ["active", "mode", "notes"],
          "properties": {
            "active": { "type": "boolean" },
            "mode": {
              "type": "string",
              "enum": ["legislative_capture", "legislative_dysfunction", "executive_consolidation", "mixed", "none"],
              "description": "Dominant pathway: legislative_capture (D7/D9 entrenchment), legislative_dysfunction (D10 paralysis/hostage-taking), executive_consolidation (B/C/F centralization), mixed (multiple pathways), none."
            },
            "mode_basis_checkpoints": {
              "type": ["array", "null"],
              "items": { "type": "string", "pattern": "^[A-F]\\d{1,2}$" },
              "description": "Checkpoint IDs that triggered this pathway assessment."
            },
            "notes": { "type": "string" }
          },
          "additionalProperties": false
        },
        "trend_summary": {
          "type": "object",
          "required": ["drivers", "watchpoints"],
          "properties": {
            "drivers": {
              "type": "array",
              "items": {
                "type": "object",
                "required": ["risk", "checkpoints", "text"],
                "properties": {
                  "risk": { "type": "string", "enum": ["High", "Medium", "Low"] },
                  "checkpoints": { "type": "array", "items": { "type": "string", "pattern": "^[A-F]\\d{1,2}$" } },
                  "text": { "type": "string" },
                  "status": { "type": "string", "enum": ["Active", "Escalating", "Stabilized", "Resolved"] }
                },
                "additionalProperties": false
              }
            },
            "watchpoints": {
              "type": "array",
              "items": {
                "type": "object",
                "required": ["risk", "checkpoints", "text"],
                "properties": {
                  "risk": { "type": "string", "enum": ["High", "Medium", "Low"] },
                  "checkpoints": { "type": "array", "items": { "type": "string", "pattern": "^[A-F]\\d{1,2}$" } },
                  "text": { "type": "string" },
                  "status": { "type": "string", "enum": ["Pending", "Uncertain"] }
                },
                "additionalProperties": false
              }
            }
          },
          "additionalProperties": false
        }
      },
      "additionalProperties": false
    }
  },
  "additionalProperties": false
}
```

### F.3 Example Output (Minimal)

```json
{
  "schema_version": "schema-1.4",
  "dbs_version": "DBS-v1.1e",
  "prompt_version": "Prompt-v1.1.0",
  "run_id": "9d3d7f47-ffb8-4f9a-a8b6-1c2d6f6c2a91",
  "topic": "trump",
  "run_date": "2026-01-20",
  "created_at_utc": "2026-01-20T23:10:00Z",
  "mode": "rolling",
  "window": { "start_date": "2025-11-22", "end_date": "2026-01-20", "days": 60 },
  "jurisdiction": { "type": "federal", "name": "United States" },
  "capability": { "has_web_access": true, "knowledge_cutoff": null, "notes": "" },
  "scores": {
    "dbs_capped": 47,
    "dbs_uncapped": null,
    "confidence_band": { "low": 43, "high": 52, "basis": "single_rater_borderline" },
    "tier_label": "Backsliding underway",
    "es_band": null,
    "red_lines_triggered": [],
    "diagnostic_flags": []
  },
  "categories": [
    { "id": "A", "max": 20, "score": 12, "drivers": [{"checkpoint_id": "A1", "points": 4}, {"checkpoint_id": "A2", "points": 4}, {"checkpoint_id": "A3", "points": 2}, {"checkpoint_id": "A4", "points": 2}] },
    { "id": "B", "max": 35, "score": 14, "drivers": [{"checkpoint_id": "B1", "points": 5}, {"checkpoint_id": "B4", "points": 5}, {"checkpoint_id": "B5", "points": 4}] },
    { "id": "C", "max": 40, "score": 16, "drivers": [{"checkpoint_id": "C1", "points": 5}, {"checkpoint_id": "C3", "points": 5}, {"checkpoint_id": "C5", "points": 3}, {"checkpoint_id": "C6", "points": 3}] },
    { "id": "D", "max": 60, "score": 28, "drivers": [{"checkpoint_id": "D5", "points": 5}, {"checkpoint_id": "D7", "points": 5}, {"checkpoint_id": "D9", "points": 5}, {"checkpoint_id": "D10", "points": 5}, {"checkpoint_id": "D11", "points": 4}, {"checkpoint_id": "D12", "points": 4}] },
    { "id": "E", "max": 20, "score": 10, "drivers": [{"checkpoint_id": "E3", "points": 5}, {"checkpoint_id": "E4", "points": 5}] },
    { "id": "F", "max": 35, "score": 16, "drivers": [{"checkpoint_id": "F2", "points": 5}, {"checkpoint_id": "F4", "points": 4}, {"checkpoint_id": "F6", "points": 4}, {"checkpoint_id": "F7", "points": 3}] }
  ],
  "events": [
    {
      "event_id": "evt-2026-01-15-doj-policy",
      "title": "DOJ issues policy memo on prosecution priorities",
      "date": "2026-01-15",
      "status": "scored",
      "exclusion_reason": null,
      "summary": "DOJ memo directing US attorneys to prioritize politically sensitive cases.",
      "tags": { "intent_direction": "ANTI-DEM", "actor": "EXEC" },
      "confidence": "High",
      "sources": [
        { "tier": "Tier-1", "outlet": "Washington Post", "type": "news", "language": "en", "title": "DOJ memo raises concerns", "published_at": "2026-01-15T14:00:00Z", "url": "https://example.com/1", "accessed_at": "2026-01-20T18:00:00Z", "archived_url": "https://web.archive.org/web/20260120/example.com/1", "archive_method": "web_archive" },
        { "tier": "Primary", "outlet": "DOJ", "type": "document", "language": "en", "title": "Prosecution Priorities Memo", "published_at": "2026-01-15T09:00:00Z", "url": "https://example.com/2", "accessed_at": "2026-01-20T18:00:00Z", "archive_method": "official_pdf", "content_hash": "sha256:a1b2c3d4e5f6789012345678901234567890abcdef1234567890abcdef123456" }
      ],
      "checkpoint_scores": [
        {
          "checkpoint_id": "C3",
          "base_score": 2,
          "modifiers": { "scope": 2, "persistence": 0 },
          "decay": { "state": "D0", "delta": 0 },
          "effective_score": 4,
          "provisional": false,
          "confidence": "High",
          "notes": "National scope (M2=+2). Anchor: policy issuance affecting DOJ operations."
        }
      ]
    },
    {
      "event_id": "evt-2026-01-12-platform-takedown",
      "title": "Platform takedown of coordinated disinformation campaign",
      "date": "2026-01-12",
      "status": "excluded",
      "exclusion_reason": "EX_TA",
      "mapped_checkpoint": "E3",
      "elements_checked": { "E1": true, "E2": true, "NX": false },
      "evidence_trigger_doc_types": ["PLATFORM_ENFORCEMENT_NOTICE"],
      "evidence_trigger_docs": [
        {
          "doc_type": "PLATFORM_ENFORCEMENT_NOTICE",
          "issuer_type": "platform",
          "issuer_name": "Example Platform",
          "issued_date": "2026-01-12",
          "reference_id": "ENF-2026-0112",
          "url": "https://example.com/takedown",
          "notes": null
        }
      ],
      "summary": "Platform removed a coordinated campaign that mimicked election office messaging without state nexus.",
      "tags": { "intent_direction": "ANTI-DEM", "actor": "OTHER" },
      "confidence": "Medium",
      "sources": [
        { "tier": "Primary", "outlet": "Example Platform", "type": "document", "language": "en", "title": "Enforcement notice on coordinated inauthentic behavior", "published_at": "2026-01-12T16:00:00Z", "url": "https://example.com/takedown", "accessed_at": "2026-01-20T18:10:00Z", "archived_url": "https://web.archive.org/web/20260120/example.com/takedown", "archive_method": "web_archive" }
      ]
    }
  ],
  "excluded_events_context": [
    { "event_id": "evt-2026-01-12-platform-takedown", "exclusion_reason": "EX_TA", "mapped_checkpoint": "E3", "evidence_trigger_doc_types": ["PLATFORM_ENFORCEMENT_NOTICE"] }
  ],
  "audit": {
    "domain_sweep": [
      { "domain": "Executive actions", "categories": ["B", "C", "F"], "result": "events_found", "notes": "" },
      { "domain": "Legislative actions", "categories": ["C", "D"], "result": "none_detected", "notes": "" },
      { "domain": "Courts and legal compliance", "categories": ["C"], "result": "events_found", "notes": "" },
      { "domain": "Elections and certification", "categories": ["D"], "result": "events_found", "notes": "" },
      { "domain": "Security services / law enforcement", "categories": ["B", "F"], "result": "none_detected", "notes": "" },
      { "domain": "Media / information control / surveillance", "categories": ["E", "F"], "result": "events_found", "notes": "" },
      { "domain": "Oversight institutions", "categories": ["C"], "result": "events_found", "notes": "" },
      { "domain": "Foreign interaction", "categories": ["D"], "result": "none_detected", "notes": "" }
    ],
    "disagreements": [
      { "checkpoint_id": "A1", "event_id": "evt-2026-01-10-speech", "range": { "low": 2, "high": 3 }, "boundary": "isolated↔repeated", "notes": "Borderline on repetition criterion." }
    ],
    "scoring_notes": ["No debunked events in this window."]
  },
  "interpretation": {
    "narrative": "DBS of 47 reflects significant democratic stress across multiple categories. Primary drivers are election integrity concerns (D5, D7, D9–D12), executive-judicial tensions (C1, C3), coercive rhetoric (A1–A4), and security service politicization (B1, B4, B5, F2, F6). No red lines triggered but B5 and D5 approach thresholds. Coordinated state-level entrenchment patterns elevate D category.",
    "intent_profile": { "method": "score_weighted", "pro_dem": 0.05, "anti_dem": 0.85, "ambiguous": 0.10 },
    "abi": -0.80,
    "pathway_dominance": { "active": true, "mode": "mixed", "mode_basis_checkpoints": ["D7", "D9", "C1", "B5"], "notes": "Both legislative entrenchment (D7/D9) and executive consolidation (C1/B5) pathways active; no single dominant mode." },
    "trend_summary": {
      "drivers": [
        { "risk": "High", "checkpoints": ["C1", "C3"], "text": "Repeated executive noncompliance with court orders and DOJ politicization elevate Category C; persistence modifiers applied.", "status": "Active" },
        { "risk": "High", "checkpoints": ["D7", "D9"], "text": "Legislative entrenchment and procedural manipulation patterns in multiple states contributing to elevated D category.", "status": "Active" },
        { "risk": "Medium", "checkpoints": ["B5", "F6"], "text": "Deployment signals and accountability-erosion rhetoric create conditions for rapid escalation.", "status": "Active" }
      ],
      "watchpoints": [
        { "risk": "High", "checkpoints": ["D5", "D11"], "text": "Election certification interference and infrastructure attack indicators require close monitoring; either could trigger red-line multiplier if scored ≥3.", "status": "Pending" },
        { "risk": "Medium", "checkpoints": ["A1", "F2"], "text": "Public statements signaling potential emergency powers invocation could escalate rapidly if formalized.", "status": "Pending" }
      ]
    }
  }
}
```

### F.4 Validation Rules

1. **One entry per event:** Multiple sources covering the same event should be listed in that event's `sources` array, not as separate event entries.

2. **Cross-field constraints:** (Enforce in application logic)
   - If `dbs_capped < 100`, then `dbs_uncapped` must be `null` and `es_band` must be `null`
   - If `dbs_capped = 100`, then `dbs_uncapped` must be a number and `es_band` must be non-null

3. **Event ID stability:** For deduplication across runs, use deterministic IDs (hash of `canonical_title + primary_action_date + primary_instrument_type`). This is source-agnostic—the same real-world action should produce the same event_id regardless of which outlet reported it.

4. **Cluster ID persistence:** Cluster IDs should be stable across runs to enable saga tracking. Use lowercase-slug format (e.g., `state-certification-laws-q1-2026`, `dhs-protest-deployments-2026`).

5. **Category maxima:** Must match current DBS version (v1.1e: A=20, B=35, C=40, D=60, E=20, F=35).

6. **EX_TA field dependency:** If `exclusion_reason = "EX_TA"`, then `mapped_checkpoint`, `elements_checked`, `evidence_trigger_doc_types`, and `evidence_trigger_docs` are required; `elements_checked` must include `NX = false` and no `unknown` values, with all non-NX elements set to `true`.

7. **Excluded events context derivation:** `excluded_events_context` must be a deterministic projection of Event Log entries where `exclusion_reason` matches `^EX_`. Each entry must carry the same `event_id`, `exclusion_reason`, `mapped_checkpoint`, and `evidence_trigger_doc_types` as its source event.

8. **Topic labeling:** If the run is topic-specific, set `topic` to a non-empty string and store outputs under `runs/<topic>/YYYY-MM-DD/`. If the run is general, set `topic` to `null` and use the top-level `runs/YYYY-MM-DD/` convention.

---

**End of document.**
