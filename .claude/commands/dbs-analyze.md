# DBS Analyze

Analyze DBS assessment results across time and topics. Generate trend reports, comparisons, alerts, and dashboards.

## Usage

```text
/dbs-analyze <topic> [options]
/dbs-analyze <topic> --trend              # Score history and trajectory
/dbs-analyze <topic> --compare <topic2>   # Side-by-side comparison
/dbs-analyze <topic> --alerts             # Check alert conditions
/dbs-analyze --dashboard                  # All active topics summary
/dbs-analyze --watchlist                  # Topics with DBS >= 50 or recent alerts
```

## Commands

### Trend Analysis

```text
/dbs-analyze trump --trend
/dbs-analyze trump --trend --since 2025-01-01
/dbs-analyze trump --trend --last 5        # Last 5 runs
```

Outputs:
- Score trajectory (table and ASCII chart)
- Tier transitions
- Red-line activation/deactivation history
- Flag emergence patterns
- Velocity analysis
- Checkpoint-level changes

### Topic Comparison

```text
/dbs-analyze trump --compare putin
/dbs-analyze america --compare hungary turkey russia
```

Outputs:
- Side-by-side score comparison (most recent run)
- Pathway mode comparison
- Category saturation comparison
- Common vs divergent flags
- Red-line status comparison

### Alert Check

```text
/dbs-analyze trump --alerts
/dbs-analyze --alerts --all               # Check all topics
```

Checks for:
- Red-line activation (any checkpoint)
- High-velocity escalation (Δ > 12 in 30 days)
- New diagnostic flags since last run
- Tier transition (especially upward)
- Guardrail attrition patterns
- Approaching thresholds (score 2 on red-line checkpoints)

### Dashboard

```text
/dbs-analyze --dashboard
```

Generates summary of all topics with runs:
- Current score and tier for each topic
- Most recent run date
- Trend direction (↑ ↓ →)
- Active red-lines
- Alert count

### Watchlist

```text
/dbs-analyze --watchlist
```

Filtered view showing only:
- Topics with DBS >= 50
- Topics with any red-line active
- Topics with alerts in last 30 days
- Topics with high-velocity flag

## Instructions

When the user runs this command with arguments `$ARGUMENTS`:

### 1. Parse Arguments

Extract from `$ARGUMENTS`:
- `topic`: Primary topic for analysis (optional for --dashboard/--watchlist)
- `--trend`: Generate trend analysis
- `--compare <topics>`: Compare with other topics (space-separated)
- `--alerts`: Check alert conditions
- `--dashboard`: Generate all-topics dashboard
- `--watchlist`: Show high-concern topics only
- `--since <date>`: Filter runs after date
- `--last <n>`: Limit to last n runs
- `--output <file>`: Write report to file

### 2. Load Run Data

For each topic being analyzed:

```
monitoring/threat-tracking/democratic-backsliding/dbs/runs/<topic>/*/run.json
```

Parse each run.json to extract:
- `run_metadata.run_date`
- `scores.dbs`
- `scores.tier`
- `scores.pathway_mode`
- `scores.red_lines_triggered`
- `scores.diagnostic_flags`
- `categories[].score`
- `velocity_tracking` (if present)
- `attrition_tracking` (if present)

Sort runs by date (ascending).

### 3. Trend Analysis (--trend)

#### 3.1 Score Trajectory Table

```markdown
## Score Trajectory: [topic]

| Run Date | DBS | Δ | Tier | Pathway | Red-Lines | Key Flags |
|----------|-----|---|------|---------|-----------|-----------|
| 2025-01-15 | 42 | — | Elevated | exec | None | — |
| 2025-02-15 | 47 | +5 | Elevated | exec+sec | None | expertise_void |
| 2025-03-15 | 58 | +11 | Backsliding | exec+sec | F6 | sword_shield |
```

#### 3.2 ASCII Trend Chart

```
DBS Score Trend: trump (last 6 runs)

100 |
 90 |
 80 |
 70 |--------------------------------------------[Severe]
 60 |                              *
 50 |--------------------*----*----[Backsliding]
 40 |          *----*
 30 |----*-----------------------------[Elevated]
 20 |
 10 |
  0 +----+----+----+----+----+----+
    Jan  Feb  Mar  Apr  May  Jun
```

#### 3.3 Tier Transition Analysis

```markdown
## Tier Transitions

- 2025-01-15: Entered "Elevated Concern" (31-50)
- 2025-03-15: Entered "Democratic Backsliding Active" (51-70)
- Days in current tier: 45
```

#### 3.4 Red-Line History

```markdown
## Red-Line Activation History

| Checkpoint | First Triggered | Status | Duration |
|------------|-----------------|--------|----------|
| F6 | 2025-03-15 | ACTIVE | 45 days |
| C1 | — | Never triggered | — |
| D5 | — | Never triggered | — |
```

#### 3.5 Flag Emergence Pattern

```markdown
## Diagnostic Flag Timeline

| Flag | First Appeared | Current Status | Consecutive Runs |
|------|----------------|----------------|------------------|
| expertise_void | 2025-02-15 | Active | 3 |
| sword_shield | 2025-03-15 | Active | 2 |
| institutional_resistance | 2025-01-15 | Active | 4 |
```

#### 3.6 Velocity Analysis

```markdown
## Velocity Analysis

| Period | Δ DBS | Days | Velocity | Flag |
|--------|-------|------|----------|------|
| Jan-Feb | +5 | 31 | 0.16/day | — |
| Feb-Mar | +11 | 28 | 0.39/day | ⚠️ Approaching threshold |
| Mar-Apr | +3 | 30 | 0.10/day | — |

Peak velocity: +11 in 28 days (Feb-Mar)
Current 30-day velocity: +3
High-velocity threshold: Δ > 12 in 30 days
```

#### 3.7 Checkpoint-Level Changes

```markdown
## Significant Checkpoint Changes (Δ ≥ 2)

| Checkpoint | Start | Current | Δ | Category |
|------------|-------|---------|---|----------|
| F1 | 1 | 4 | +3 | Security |
| C3 | 2 | 4 | +2 | Courts |
| F6 | 1 | 3 | +2 | Security |
```

### 4. Comparison Analysis (--compare)

#### 4.1 Score Comparison Table

```markdown
## Topic Comparison (as of 2025-04-15)

| Metric | trump | putin | hungary |
|--------|-------|-------|---------|
| DBS Score | 58 | 82 | 71 |
| Tier | Backsliding | Severe | Severe |
| Pathway | exec+sec | hybrid+klep | hybrid+capture |
| Red-Lines | F6 | C1,D5,F2,F6 | D5,F6 |
| Active Flags | 3 | 7 | 5 |
```

#### 4.2 Category Saturation Comparison

```markdown
## Category Saturation Comparison

| Category | trump | putin | hungary |
|----------|-------|-------|---------|
| A (Narrative) | 35% | 75% | 55% |
| B (Coercion) | 40% | 80% | 45% |
| C (Courts) | 45% | 70% | 65% |
| D (Elections) | 38% | 85% | 72% |
| E (Information) | 30% | 90% | 60% |
| F (Security) | 55% | 75% | 50% |
```

#### 4.3 Common vs Divergent Patterns

```markdown
## Pattern Analysis

**Common Flags (all topics):**
- expertise_void
- sword_shield

**Divergent Patterns:**
- putin: Full legal capture (C1+C3+F6)
- hungary: Legislative capture pathway
- trump: Executive-focused, courts still checking
```

### 5. Alert Analysis (--alerts)

#### 5.1 Alert Summary

```markdown
## Alert Report: [topic]

### 🔴 CRITICAL ALERTS

1. **Red-Line Activated: F6** (2025-03-15)
   - Leader immunity doctrine operationalized
   - Multiplier: +10 active

### 🟠 HIGH ALERTS

2. **Approaching High-Velocity Threshold**
   - Current 30-day Δ: +11
   - Threshold: Δ > 12
   - One more point triggers velocity flag

3. **New Diagnostic Flag: sword_shield**
   - Triggered: 2025-03-15
   - Condition: C3 ≥ 3 AND F6 ≥ 3

### 🟡 WATCH ALERTS

4. **Tier Transition Imminent**
   - Current: 58 (Backsliding Active)
   - Next tier at: 71 (Severe)
   - Margin: 13 points

5. **Red-Line Proximity: D5**
   - Current score: 2
   - One escalation triggers +15 multiplier
```

#### 5.2 Alert Conditions Checked

| Condition | Status | Details |
|-----------|--------|---------|
| Red-line activation | ✓ TRIGGERED | F6 |
| High-velocity (Δ>12/30d) | ○ WATCH | Δ=11 |
| New flags | ✓ TRIGGERED | sword_shield |
| Tier transition | ○ WATCH | 13 pts to Severe |
| Guardrail attrition | ○ CLEAR | No 3+ run patterns |
| Electoral exit blocked | ○ CLEAR | D5=2, D6=1, D11=0 |

### 6. Dashboard (--dashboard)

```markdown
# DBS Dashboard

Generated: 2025-04-15

## Active Topics Summary

| Topic | DBS | Trend | Tier | Pathway | Red-Lines | Alerts | Last Run |
|-------|-----|-------|------|---------|-----------|--------|----------|
| trump | 58 | ↑ | Backsliding | exec+sec | F6 | 2 | 2025-04-10 |
| putin | 82 | → | Severe | hybrid+klep | C1,D5,F2,F6 | 0 | 2025-04-12 |
| hungary | 71 | ↓ | Severe | hybrid+cap | D5,F6 | 1 | 2025-04-08 |
| turkey | 67 | ↑ | Backsliding | exec | F6 | 3 | 2025-04-05 |
| america | 58 | ↑ | Backsliding | exec+sec | F6 | 2 | 2025-04-10 |

## Trend Legend
- ↑ Rising (Δ > +3 over last 2 runs)
- ↓ Falling (Δ < -3 over last 2 runs)
- → Stable (|Δ| ≤ 3)

## Alert Summary
- **Critical (red-line):** 4 topics
- **High (velocity/new flags):** 2 topics
- **Watch (proximity):** 3 topics

## Topics Requiring Attention
1. **turkey** — 3 alerts, rising trend
2. **trump** — 2 alerts, rising trend, velocity watch
```

### 7. Watchlist (--watchlist)

```markdown
# DBS Watchlist

Topics meeting elevated concern criteria:

## Tier: Severe Democratic Backsliding (71-89)

| Topic | DBS | Trend | Key Concern |
|-------|-----|-------|-------------|
| putin | 82 | → | 4 red-lines active |
| hungary | 71 | ↓ | Electoral exit at risk |

## Tier: Democratic Backsliding Active (51-70)

| Topic | DBS | Trend | Key Concern |
|-------|-----|-------|-------------|
| turkey | 67 | ↑ | 3 alerts, rapid escalation |
| trump | 58 | ↑ | Velocity approaching threshold |
| america | 58 | ↑ | Velocity approaching threshold |

## Recent Alert Activity (Last 30 Days)

| Topic | Alert Type | Date | Details |
|-------|------------|------|---------|
| trump | Red-line | 2025-03-15 | F6 activated |
| turkey | New flag | 2025-04-01 | legal_capture_complete |
| hungary | Tier transition | 2025-03-20 | Entered Severe |
```

### 8. Output Options

**Console (default):** Display formatted markdown

**File output (--output):**
```
/dbs-analyze trump --trend --output reports/trump-trend-2025-04.md
```

**JSON output (--json):**
```
/dbs-analyze trump --trend --json
```

Returns structured data for external processing.

## Alert Condition Definitions

| Alert Level | Condition | Trigger |
|-------------|-----------|---------|
| 🔴 Critical | Red-line activated | Any of: C1+B5≥3, D5/D6/D11≥3, F2≥3, F6≥3 |
| 🔴 Critical | Electoral exit blocked | D5≥3 AND D6≥3, or similar combinations |
| 🔴 Critical | Legal capture complete | C3≥3 AND F6≥3 AND (C1≥3 OR C2≥3) |
| 🟠 High | High-velocity | Δ > 12 in 30 days |
| 🟠 High | New red-line breach | Red-line newly ≥3 this run |
| 🟠 High | New diagnostic flag | Flag not present in prior run |
| 🟡 Watch | Velocity approaching | 10 ≤ Δ ≤ 12 in 30 days |
| 🟡 Watch | Red-line proximity | Score = 2 on red-line checkpoint |
| 🟡 Watch | Tier transition imminent | Within 5 points of next tier |
| 🟡 Watch | Guardrail attrition | 2 consecutive resistance runs |

## Trend Indicators

| Symbol | Meaning | Calculation |
|--------|---------|-------------|
| ↑↑ | Rapid rise | Δ > +8 over last 2 runs |
| ↑ | Rising | +3 < Δ ≤ +8 |
| → | Stable | -3 ≤ Δ ≤ +3 |
| ↓ | Falling | -8 ≤ Δ < -3 |
| ↓↓ | Rapid fall | Δ < -8 |

## Example Session

```
User: /dbs-analyze trump --trend --last 5

Claude:
## Score Trajectory: trump (last 5 runs)

| Run Date | DBS | Δ | Tier | Pathway | Red-Lines |
|----------|-----|---|------|---------|-----------|
| 2025-01-15 | 42 | — | Elevated | exec | None |
| 2025-02-01 | 44 | +2 | Elevated | exec | None |
| 2025-02-15 | 47 | +3 | Elevated | exec+sec | None |
| 2025-03-01 | 52 | +5 | Backsliding | exec+sec | None |
| 2025-03-15 | 58 | +6 | Backsliding | exec+sec | F6 |

Trend: ↑ Rising (+16 over 5 runs, avg +4/run)

DBS Score Trend:
 70 |
 60 |                         *
 50 |--------------*----*----[Backsliding Active]
 40 |----*----*
 30 |
    Jan     Feb     Mar

## Key Changes
- Tier transition: Elevated → Backsliding (2025-03-01)
- Red-line activation: F6 (2025-03-15)
- New flag: sword_shield (2025-03-15)

## Alerts
🔴 Red-line F6 active since 2025-03-15
🟠 Rising trend: +6 last run, +11 last 30 days
🟡 D5 at score 2 (red-line proximity)
```

## Error Handling

- **No runs found:** "No DBS runs found for topic '[topic]'. Run `/dbs-run [topic]` first."
- **Single run (no trend):** "Only one run found for '[topic]'. Need 2+ runs for trend analysis."
- **Invalid topic:** "Topic '[topic]' not found. Available topics: [list]"
- **Date parsing error:** "Invalid date format. Use YYYY-MM-DD."
