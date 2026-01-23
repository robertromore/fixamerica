# DBS Run

Execute a Democratic Backsliding Scorecard (DBS) assessment for a specified topic and time window.

## Usage

```text
/dbs-run <topic> [options]

# Examples:
/dbs-run trump                           # 60-day rolling window, today's date
/dbs-run trump --window 90               # 90-day rolling window
/dbs-run hungary --date 2025-06-15       # Specific run date
/dbs-run putin --from 2025-01-01 --to 2025-03-31  # Custom date range
/dbs-run america --mode snapshot         # Snapshot mode (point-in-time)
/dbs-run turkey --json                   # Output JSON in addition to markdown
/dbs-run trump --prior                   # Load prior run for velocity/attrition tracking
```

## Parameters

| Parameter | Description | Default |
|-----------|-------------|---------|
| `<topic>` | Subject of assessment (person, country, or region) | Required |
| `--window <days>` | Rolling window length in days | 60 |
| `--date <YYYY-MM-DD>` | Run date (end of window) | Today |
| `--from <YYYY-MM-DD>` | Custom window start date | Computed from window |
| `--to <YYYY-MM-DD>` | Custom window end date | Same as --date |
| `--mode <type>` | Run mode: `rolling`, `adhoc`, `snapshot` | rolling |
| `--json` | Also output JSON (schema-compliant) | false |
| `--prior` | Load most recent prior run for delta calculations | false |
| `--sim` | Include Strategic Intervention Matrix | auto (DBS >= 31) |
| `--no-sim` | Exclude Strategic Intervention Matrix | false |

## Instructions

When the user runs this command with arguments `$ARGUMENTS`:

### 1. Parse Arguments

Extract from `$ARGUMENTS`:
- `topic`: Required first positional argument (e.g., "trump", "hungary", "america")
- `window`: Number of days (default 60)
- `date`: Run date in YYYY-MM-DD format (default today)
- `from`/`to`: Custom date range (overrides window)
- `mode`: rolling (default), adhoc, or snapshot
- `json`: Boolean flag for JSON output
- `prior`: Boolean flag to load prior run
- `sim`/`no-sim`: Force SIM inclusion/exclusion

If no topic provided, ask: "Which topic? (e.g., `trump`, `hungary`, `america`, `putin`)"

### 2. Load Framework Resources

Read the following files:
- `monitoring/threat-tracking/democratic-backsliding/dbs/initial-scoped-plan.md` - Full methodology
- `monitoring/threat-tracking/democratic-backsliding/dbs/templates/prompt.md` - LLM prompt template

Extract from initial-scoped-plan.md:
- Appendix A: Checkpoint definitions and anchors
- Appendix B: Red-line multiplier rules
- Section 6: Scoring formula and pathway classification
- Section 7: Interpretation bands and diagnostic flags

### 3. Load Prior Run (if --prior flag set)

Search for most recent prior run:
```
monitoring/threat-tracking/democratic-backsliding/dbs/runs/<topic>/*/run.md
```

If found, extract:
- Prior DBS score (for velocity calculation)
- Prior run date (for days elapsed)
- Attrition tracking data (for guardrail attrition)
- Prior checkpoint scores (for change detection)

### 4. Gather Current Events

Use WebSearch to find recent news for the topic within the specified window:

**Search queries to execute:**
1. `"<topic>" democracy OR democratic OR authoritarian site:reuters.com OR site:apnews.com` (Tier-1)
2. `"<topic>" court OR judicial OR ruling site:reuters.com OR site:apnews.com` (Category C)
3. `"<topic>" election OR voting OR certification` (Category D)
4. `"<topic>" military OR police OR security forces` (Categories B, F)
5. `"<topic>" press OR media OR journalist` (Category E)
6. `"<topic>" prosecution OR investigation OR indictment` (Categories B, C)

**Source prioritization:**
- Tier-1: Reuters, AP, Bloomberg, NYT, WaPo, WSJ, FT
- Tier-2: BBC, NPR, PBS, Politico, The Hill
- Contrast: Fox News (news), National Review, Vox, Guardian

### 5. Build Event Log

For each relevant event found:
1. Assign unique `event_id` (e.g., `E001`, `E002`)
2. Identify `mapped_checkpoint` (A1-A4, B1-B7, C1-C8, D1-D12, E1-E4, F1-F7)
3. Assess `base_score` (0-5 scale per Appendix A anchors)
4. Apply `scope_modifier` (M0/M1/M2) and `persistence_modifier` (P0/P1/P2)
5. Check for decay (D0-D3) based on event age
6. Tag `intent` (PRO-DEM, ANTI-DEM, AMBIGUOUS)
7. Assign `confidence` (High/Medium/Low)
8. Record `sources` with URLs

### 6. Score Checkpoints

For each checkpoint (A1-F7):
1. Sum contributing events
2. Apply gating rules (Section 4.3)
3. Apply Institutional Resistance modifier if applicable
4. Record effective score

### 7. Calculate DBS Score

Follow Section 6.2 formula:
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

Apply red-line multipliers (Section 6.3):
- C1 ≥ 3 AND B5 ≥ 3 → +10
- D5 ≥ 3 OR D6 ≥ 3 OR D11 ≥ 3 → +15
- F2 ≥ 3 → +10
- F6 ≥ 3 → +10

Cap at 100.

### 8. Classify Pathway Mode

Calculate saturation metrics (Section 6.2):
```
Executive_Saturation = (B/35 + C/40 + F/35) / 3 × 100
D_exec = D1 + D2 + D4 + D5 + D6 + D8 + D11 + D12 (max 40)
D_leg = D3 + D7 + D9 + D10 (max 20)
Legislative_Saturation = D_leg/20 × 100
```

Determine primary mode:
- `executive-driven`: Exec > 40% AND Leg ≤ 30%
- `legislative-driven`: Leg > 40% AND Exec ≤ 40%
- `hybrid`: Exec > 35% AND Leg > 35%
- `undetermined`: Otherwise

Add subcategory modifiers as applicable.

### 9. Evaluate Diagnostic Flags

Check all 23 diagnostic flag conditions (Section 7 of prompt template).

### 10. Calculate Temporal Metrics (if --prior)

**Velocity:**
- `delta_dbs` = current DBS - prior DBS
- `days_elapsed` = current run date - prior run date
- If delta > 12 in ≤30 days → "High-velocity escalation" flag

**Attrition:**
- For each checkpoint with Institutional Resistance Active in both runs
- Increment consecutive run counter
- If ≥3 consecutive runs with base ≥ 2 → "Guardrail attrition" flag

### 11. Check High-Opacity Protocol

If Audit Degradation flag active AND DBS ≥ 70:
- Calculate Opacity Index
- If OI > 50, prepare DBS-V and DBS-S bifurcation
- If OI ≥ 76, prepare Dark Zone declaration

### 12. Generate Output

**Create output directory:**
```
monitoring/threat-tracking/democratic-backsliding/dbs/runs/<topic>/<YYYY-MM-DD>/
```

**Write run.md:**

```markdown
# DBS Run Summary

DBS-v1.1e [mode] ([window], run date: YYYY-MM-DD) — Topic: <topic>: [score] (confidence band: ±N)
Tier: [tier label]
Pathway: [pathway_mode][+subcategories]
Red-lines: [list or "None triggered"]

## Trend Drivers

- **Driver** (High) [checkpoint]: [description]
- **Driver** (Medium) [checkpoint]: [description]
...

## Watchpoints

- **Watchpoint** (High) [checkpoint]: [description]
...

## Diagnostic Flags

- [flag 1]
- [flag 2]
...

## Criticality Map

| Checkpoint | Score | +1 Effect | -1 Effect | Structural Impact |
|------------|-------|-----------|-----------|-------------------|
| ... | ... | ... | ... | ... |

## Strategic Intervention Matrix

(if DBS ≥ 31 and not --no-sim)

Tier: [tier]
Pathway: [pathway]
Priority Checkpoints: [list]

Actor Priorities:
- Courts: [action]
- Watchdogs: [action]
- Media: [action]
- NGOs: [action]
- International: [action]

## Event Log Summary

[count] events scored across [checkpoint count] checkpoints.
[excluded count] events excluded (context only).

## Excluded Events (Context)

| Event ID | Exclusion Reason | Checkpoint | Evidence Types |
|----------|------------------|------------|----------------|
| ... | ... | ... | ... |

## Category Scores

| Category | Score | Max | Saturation |
|----------|-------|-----|------------|
| A | ... | 20 | ...% |
| B | ... | 35 | ...% |
| C | ... | 40 | ...% |
| D | ... | 60 | ...% |
| E | ... | 20 | ...% |
| F | ... | 35 | ...% |

## Notes

- [any methodology notes, confidence caveats, or source limitations]
```

**Write run.json (if --json):**

Full schema-compliant JSON per Appendix F.

### 13. Report Results

Display to user:
- Header line with score, tier, pathway
- Red-line status
- Top 3 diagnostic flags (if any)
- Top 3 trend drivers
- Top 3 watchpoints
- Delta from prior run (if --prior)
- Link to full output file

## Topic Guidelines

### Person-Focused Topics

For individual leaders (trump, putin, orban, erdogan, etc.):
- Focus on actions taken by the individual and their administration
- Score based on the country they lead
- Use their name as topic identifier

### Country-Focused Topics

For countries (america, hungary, turkey, russia, etc.):
- Assess the overall democratic health of the country
- Include actions by all branches and levels of government
- Consider both domestic and foreign policy dimensions

### Naming Conventions

Use lowercase, single-word identifiers:
- `trump` (not "Trump" or "donald-trump")
- `america` or `usa` (either acceptable)
- `hungary` (not "Hungary" or "HUN")

## Error Handling

- **Insufficient sources**: If fewer than 3 Tier-1 sources found, warn user and widen search
- **No events found**: If no scorable events in window, return DBS 0 with explanation
- **Prior run not found**: If --prior flag but no prior run exists, proceed without delta calculations
- **Date parsing errors**: Request clarification on date format

## Example Session

```
User: /dbs-run trump --window 90 --prior

Claude: Running DBS assessment for topic: trump
Window: 90-day rolling (2024-10-23 to 2026-01-22)
Loading prior run from 2024-12-15...

[Gathering sources from Reuters, AP, court filings...]
[Scoring 47 events across 31 checkpoints...]

---

DBS-v1.1e Rolling (90-day window, run date: 2026-01-22) — Topic: trump: 52 (confidence band: ±6)
Tier: Democratic Backsliding Active (51–70)
Pathway: executive-driven+security_dominant
Red-lines: None triggered

Δ from prior run: +8 points (44 → 52) over 38 days

Top Diagnostic Flags:
- Prosecutorial sword and shield active (C3=3, F6=3)
- Expertise void (F1=3, C4=3)
- Institutional resistance active (C1, D3)

Top Trend Drivers:
- **Driver** (High) F1: Mass firings of senior civil servants
- **Driver** (High) C3: Selective prosecution pattern emerging
- **Driver** (Medium) F6: Immunity claims expanding

Top Watchpoints:
- **Watchpoint** (High) C1: Pending court rulings on executive authority
- **Watchpoint** (High) D5: Certification procedures under review
- **Watchpoint** (Medium) F2: Military leadership appointments pending

Full assessment: monitoring/threat-tracking/democratic-backsliding/dbs/runs/trump/2026-01-22/run.md
```
