# Democratic Backsliding Scorecard (DBS)

**Version:** DBS-v1.1e

The Democratic Backsliding Scorecard is a structured, evidence-based framework for detecting early authoritarian drift. It measures observable political events against historical thresholds that precede authoritarian consolidation.

## Quick Start

```bash
# Execute an assessment
/dbs-run trump                    # 60-day rolling window
/dbs-run hungary --window 90      # 90-day window
/dbs-run america --prior          # Include velocity tracking

# Analyze results
/dbs-analyze trump --trend        # Score trajectory over time
/dbs-analyze --dashboard          # All topics summary
/dbs-analyze trump --alerts       # Check alert conditions
```

## Directory Structure

```
dbs/
├── README.md                     # This file
├── initial-scoped-plan.md        # Full methodology and schema (source of truth)
├── templates/
│   ├── prompt.md                 # LLM prompt template for assessments
│   ├── run-template.md           # Output format for run summaries
│   ├── event-log-template.json   # Event log structure
│   └── manifest-template.json    # Evidence integrity manifest
└── runs/
    └── <topic>/
        └── <YYYY-MM-DD>/
            ├── run.md            # Human-readable summary
            ├── run.json          # Schema-compliant JSON output
            ├── event-log.json    # Detailed event log
            └── prompt.md         # Prompt used for this run
```

## Core Concepts

### What DBS Measures

DBS tracks six categories of state power that historically align during authoritarian consolidation:

| Category | Description | Max Points |
|----------|-------------|------------|
| A | Narrative Control | 20 |
| B | Coercive Apparatus | 35 |
| C | Courts and Legal System | 40 |
| D | Elections and Legislative | 60 |
| E | Information Environment | 20 |
| F | Security State | 35 |

**Total possible:** 210 points (capped at 100 for headline score)

### Scoring Tiers

| Score | Tier | Description |
|-------|------|-------------|
| 0-10 | Normal | Standard democratic conflict |
| 11-30 | Concern | Elevated concern warranting monitoring |
| 31-50 | Elevated | Active institutional probing |
| 51-70 | Backsliding | Democratic backsliding active |
| 71-89 | Severe | Severe backsliding, consolidation likely |
| 90-100 | Critical | Transition threshold / consolidated |

### Red-Line Checkpoints

Certain checkpoints trigger score multipliers when they reach threshold (score >= 3):

| Red-Line | Description | Multiplier |
|----------|-------------|------------|
| C1 + B5 >= 3 | Combined unlawful court defiance | +5 |
| D5 >= 3 | Electoral fraud machinery | +15 |
| D6 >= 3 | Certification override | +15 |
| D11 >= 3 | Legislative self-entrenchment | +10 |
| F2 >= 3 | Purged/loyalist commanders | +10 |
| F6 >= 3 | Leader immunity doctrine | +10 |

### Pathway Modes

Every assessment classifies the dominant consolidation pathway:

| Mode | Trigger |
|------|---------|
| `executive-driven` | Executive saturation > 40% AND legislative <= 30% |
| `legislative-driven` | Legislative saturation > 40% AND executive <= 40% |
| `hybrid` | Both executive and legislative > 35% |
| `undetermined` | No clear pattern |

**Subcategory modifiers:** `+foreign_enabled`, `+capture`, `+dysfunction`, `+kleptocratic`, `+security_dominant`

## Workflow

### 1. Execute an Assessment

Use the `/dbs-run` skill:

```bash
/dbs-run <topic> [options]
```

**Parameters:**

| Parameter | Description | Default |
|-----------|-------------|---------|
| `<topic>` | Subject (trump, hungary, america, putin) | Required |
| `--window <days>` | Rolling window length | 60 |
| `--date <YYYY-MM-DD>` | Run date (end of window) | Today |
| `--from / --to` | Custom date range | Computed |
| `--mode <type>` | rolling, adhoc, snapshot | rolling |
| `--json` | Also output JSON | false |
| `--prior` | Load prior run for velocity | false |
| `--sim` | Include Strategic Intervention Matrix | auto |

**Example session:**

```
User: /dbs-run trump --window 60 --prior

Claude: [Searches for recent events within the 60-day window]
        [Scores each event against checkpoints]
        [Loads prior run for velocity calculation]
        [Generates run summary]

Output:
DBS-v1.1e Rolling (60-day window, run date: 2026-01-22) — Topic: trump: 47 (confidence band: ±5)
Tier: Elevated concern (31-50)
Pathway: executive-driven+security_dominant
Red-lines: None triggered

## Trend Drivers
- **Driver** (High) [F1]: Mass dismissals of career officials...
- **Driver** (Medium) [C3]: Selective prosecution pattern...

## Watchpoints
- **Watchpoint** (High) [D5]: Certification review panels...
...
```

### 2. Analyze Results

Use the `/dbs-analyze` skill:

```bash
/dbs-analyze <topic> [options]
```

**Commands:**

| Command | Description |
|---------|-------------|
| `--trend` | Score trajectory, tier transitions, velocity |
| `--compare <topic2>` | Side-by-side comparison |
| `--alerts` | Check alert conditions |
| `--dashboard` | All topics summary |
| `--watchlist` | High-concern topics (DBS >= 50 or alerts) |

**Example: Trend Analysis**

```
User: /dbs-analyze trump --trend --last 5

Claude:
## Score Trajectory: trump (last 5 runs)

| Run Date   | DBS | Delta | Tier        | Pathway      | Red-Lines |
|------------|-----|-------|-------------|--------------|-----------|
| 2025-11-15 | 42  | -     | Elevated    | exec         | None      |
| 2025-12-15 | 44  | +2    | Elevated    | exec         | None      |
| 2026-01-15 | 47  | +3    | Elevated    | exec+sec     | None      |
| 2026-01-31 | 52  | +5    | Backsliding | exec+sec     | None      |
| 2026-02-15 | 58  | +6    | Backsliding | exec+sec     | F6        |

Trend: Rising (+16 over 5 runs)
```

**Example: Dashboard**

```
User: /dbs-analyze --dashboard

Claude:
# DBS Dashboard (2026-01-22)

| Topic   | DBS | Trend | Tier        | Pathway     | Red-Lines   | Alerts |
|---------|-----|-------|-------------|-------------|-------------|--------|
| trump   | 58  | up    | Backsliding | exec+sec    | F6          | 2      |
| hungary | 71  | down  | Severe      | hybrid+cap  | D5,F6       | 1      |
| turkey  | 67  | up    | Backsliding | exec        | F6          | 3      |
```

**Example: Alerts**

```
User: /dbs-analyze trump --alerts

Claude:
## Alert Report: trump

### CRITICAL ALERTS
1. **Red-Line Activated: F6** (2026-02-15)
   - Leader immunity doctrine operationalized
   - Multiplier: +10 active

### HIGH ALERTS
2. **Approaching High-Velocity Threshold**
   - Current 30-day delta: +11
   - Threshold: delta > 12

### WATCH ALERTS
3. **Red-Line Proximity: D5**
   - Current score: 2
   - One escalation triggers +15 multiplier
```

### 3. Comparison Analysis

```
User: /dbs-analyze trump --compare hungary turkey

Claude:
## Topic Comparison (as of 2026-01-22)

| Metric      | trump | hungary | turkey |
|-------------|-------|---------|--------|
| DBS Score   | 58    | 71      | 67     |
| Tier        | Backsliding | Severe | Backsliding |
| Pathway     | exec+sec | hybrid+cap | exec |
| Red-Lines   | F6    | D5,F6   | F6     |
| Active Flags| 3     | 5       | 4      |

## Category Saturation Comparison

| Category     | trump | hungary | turkey |
|--------------|-------|---------|--------|
| A (Narrative)| 35%   | 55%     | 45%    |
| B (Coercion) | 40%   | 45%     | 50%    |
| C (Courts)   | 45%   | 65%     | 55%    |
| D (Elections)| 38%   | 72%     | 48%    |
| E (Info)     | 30%   | 60%     | 65%    |
| F (Security) | 55%   | 50%     | 45%    |
```

## Output Formats

### Run Summary (run.md)

Human-readable markdown with:

- Header (score, tier, pathway, red-lines)
- Trend Drivers (scored factors actively contributing)
- Watchpoints (credible near-term risks not yet scored)
- Diagnostic Flags (pattern indicators)
- Criticality Map (sensitivity analysis)
- Strategic Intervention Matrix (DBS >= 31)
- Category Scores
- Pathway Saturation
- Excluded Events
- Intent Profile
- Velocity Tracking (if prior run loaded)

### JSON Output (run.json)

Schema-compliant structured data for programmatic processing:

```json
{
  "schema_version": "schema-1.4",
  "dbs_version": "DBS-v1.1e",
  "run_id": "uuid",
  "topic": "trump",
  "run_date": "2026-01-22",
  "scores": {
    "dbs_capped": 58,
    "tier_label": "Democratic backsliding active",
    "red_lines_triggered": ["F6"],
    "diagnostic_flags": ["sword_shield", "expertise_void"]
  },
  "categories": [...],
  "events": [...],
  "interpretation": {...}
}
```

### Event Log (event-log.json)

Detailed event-level data:

```json
{
  "events": [
    {
      "event_id": "E001",
      "date": "2026-01-15",
      "description": "...",
      "mapped_checkpoint": "F1",
      "base_score": 3,
      "scope_modifier": "M0",
      "persistence_modifier": "P0",
      "decay_state": "D0",
      "effective_score": 3,
      "sources": [...]
    }
  ],
  "excluded_events": [...]
}
```

## Diagnostic Flags

Pattern indicators that trigger when specific checkpoint combinations are met:

| Flag | Condition |
|------|-----------|
| `sword_shield` | C3 >= 3 AND F6 >= 3 |
| `legal_capture_complete` | C3 >= 3 AND F6 >= 3 AND (C1 >= 3 OR C2 >= 3) |
| `expertise_void` | (F1 >= 3 OR F3 >= 3) AND C4 >= 3 |
| `electoral_exit_blocked` | (D5 >= 3 AND D6 >= 3) OR (D5 >= 3 AND D11 >= 3) |
| `high_velocity` | Delta > 12 points in 30 days |
| `guardrail_attrition` | Resistance active 3+ consecutive runs with base >= 2 |

## Alert Conditions

| Level | Condition | Description |
|-------|-----------|-------------|
| Critical | Red-line activated | Any checkpoint at >= 3 |
| Critical | Electoral exit blocked | D5 >= 3 AND D6 >= 3 |
| Critical | Legal capture complete | C3 >= 3 AND F6 >= 3 AND (C1 >= 3 OR C2 >= 3) |
| High | High-velocity | Delta > 12 in 30 days |
| High | New red-line breach | Red-line newly >= 3 this run |
| Watch | Velocity approaching | 10 <= delta <= 12 in 30 days |
| Watch | Red-line proximity | Score = 2 on red-line checkpoint |
| Watch | Tier transition imminent | Within 5 points of next tier |

## High-Opacity Environment Protocol

When information environment degrades significantly (OI > 50), the framework reports two scores:

- **DBS-V (Verified):** Based only on Tier-1/corroborated Tier-2 sources
- **DBS-S (Structural):** Includes structural floor inference

Output format:

```
DBS-v1.1e Rolling (60-day, run date: 2026-01-22) — Topic: [subject]: DBS-V: 45 / DBS-S: 62 (OI: 58)
Tier: Democratic backsliding active
Pathway: executive-driven
Red-lines: F6
Opacity: High - wider confidence bands; some indicators unreliable
```

## Source Tiers

| Tier | Sources | Weight |
|------|---------|--------|
| Tier-1 | Reuters, AP, Bloomberg, NYT, WaPo, WSJ, FT, official documents | Full |
| Tier-2 | BBC, NPR, PBS, Politico, The Hill, academic sources | Corroboration required |
| Tier-3 | Single-source, partisan, unverified | Cannot directly increase scores |

## Key Files

| File | Purpose |
|------|---------|
| `initial-scoped-plan.md` | Full methodology, checkpoint definitions, scoring rules |
| `templates/prompt.md` | LLM prompt template for executing assessments |
| `templates/run-template.md` | Output format specification |
| `.claude/commands/dbs-run.md` | /dbs-run skill definition |
| `.claude/commands/dbs-analyze.md` | /dbs-analyze skill definition |

## References

- Appendix A (initial-scoped-plan.md): Checkpoint definitions and anchor examples
- Appendix B: Red-line multiplier rules
- Appendix F: JSON schema specification (schema-1.4)
- Appendix I: DBS-Exchange Federation Protocol

---

*DBS-v1.1e is designed for non-partisan application. The same methodology applies regardless of political affiliation.*
