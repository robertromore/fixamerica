# DBS Analyze

Analyze DBS assessment results across time and topics. Generate trend reports, comparisons, alerts, and dashboards.

**Reports are written for a general audience.** All technical terms are explained in plain language, each section includes interpretive context, and every report concludes with a narrative summary accessible to readers without specialized knowledge.

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

Default reports directory: `monitoring/threat-tracking/democratic-backsliding/dbs/reports/`

```
/dbs-analyze trump --trend --output trump-trend-2025.md
/dbs-analyze trump --trend --output reports/trump-trend-2025.md
```

If no directory is specified, write to the default reports directory. If a relative path is given, resolve it from the dbs directory.

**JSON output (--json):**
```
/dbs-analyze trump --trend --json
```

Returns structured data for external processing.

### 9. Report Structure (REQUIRED)

All reports must follow this structure:

1. **Title and metadata** — Topic, date range, report type
2. **How to Read This Report** — Brief explanation for new readers
3. **Data sections** — Tables, charts, and analysis (with section descriptions)
4. **Glossary** — Plain-language explanations of all technical terms used
5. **Executive Summary** — Narrative synthesis accessible to general readers

The glossary and executive summary are mandatory for all reports written to files.

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

## Plain-Language Glossary (REQUIRED IN ALL REPORTS)

Every report must include a glossary section that explains technical terms in accessible language. Use these definitions:

### Diagnostic Flags

| Flag | Technical Name | Plain-Language Explanation |
|------|----------------|---------------------------|
| `sword_shield` | Prosecutorial Sword and Shield | The legal system is being used as both a weapon and a shield—prosecuting opponents while protecting allies from accountability. This creates a two-tiered justice system where the law applies differently depending on political loyalty. |
| `legal_capture_complete` | Legal System Capture Complete | The courts and prosecution system have been sufficiently co-opted that they no longer serve as independent checks on executive power. Legal challenges to government overreach are unlikely to succeed. |
| `expertise_void` | Expertise Void | Career professionals and subject-matter experts have been removed or sidelined from government. Institutional knowledge has been lost, and oversight bodies lack the technical capacity to identify problems or push back effectively. |
| `electoral_exit_blocked` | Electoral Exit Blocked | Multiple mechanisms that would allow voters to change leadership through elections have been compromised. This could include voter suppression, election administration capture, or certification process manipulation. |
| `high_velocity` | High-Velocity Escalation | The pace of democratic erosion has accelerated dramatically—changes that historically took years are happening in weeks or months. Institutions may not have time to adapt or respond. |
| `guardrail_attrition` | Guardrail Attrition | Democratic safeguards are being worn down through sustained pressure. Even when institutions successfully resist, repeated attacks weaken their capacity to continue resisting. |
| `state_of_exception` | State of Exception Pattern | Emergency rhetoric and crisis framing are being used to justify expanding executive power. Historically, this pattern precedes suspension of normal democratic constraints. |
| `foreign_domestic_subversion` | Foreign-Domestic Election Subversion | Foreign interference in elections is being coordinated with or tolerated by domestic actors who benefit from it. |
| `information_preconditioning` | Information Environment Pre-conditioning | Media and information systems are being shaped to make the public more accepting of future anti-democratic actions, such as rejecting election results. |
| `coercion_information_disconnect` | Coercion-Information Disconnect | The government is using visible force or coercion while the media environment remains relatively open—a historically unstable configuration that often precedes either media crackdown or regime change. |
| `institutional_resistance` | Institutional Resistance Active | Democratic institutions are actively pushing back against overreach—courts issuing injunctions, inspectors general publishing reports, or civil servants refusing unlawful orders. This is a positive indicator. |
| `audit_degraded` | Electoral Oversight Compromised | The information environment has degraded to the point where it's difficult to independently verify what's happening with elections. Official claims cannot be reliably fact-checked. |

### Pathway Modes

| Mode | Plain-Language Explanation |
|------|---------------------------|
| `executive-driven` | Power is being concentrated through executive action—presidential orders, agency directives, and personnel changes—rather than through legislation. |
| `legislative-driven` | The legislature is the primary vehicle for democratic erosion, passing laws that entrench the ruling party or restrict opposition. |
| `hybrid` | Both executive and legislative branches are working in concert to concentrate power. |
| `+foreign_enabled` | Foreign actors are providing support, whether through election interference, financial backing, or diplomatic cover. |
| `+capture` | Key institutions have been co-opted to serve partisan rather than public interests. |
| `+kleptocratic` | Corruption and self-enrichment are significant features of the consolidation pattern. |
| `+security_dominant` | The security apparatus (military, police, intelligence) is playing a central role in the power consolidation. |

### Scoring Tiers

| Tier | Score Range | What It Means |
|------|-------------|---------------|
| Normal | 0-10 | Standard democratic politics. Disagreements and conflicts exist but are resolved through legitimate institutional channels. |
| Concern | 11-30 | Some warning signs warrant monitoring, but institutions remain functional and independent. |
| Elevated | 31-50 | Active probing of institutional limits. Democratic norms are being tested, and some safeguards are under pressure. |
| Backsliding | 51-70 | Democratic erosion is actively occurring. Multiple institutions have been weakened or captured. Reversing course becomes increasingly difficult. |
| Severe | 71-89 | Advanced consolidation of power. Most institutional checks have failed or been neutralized. Electoral path to change may be compromised. |
| Critical | 90-100 | Transition threshold. Democratic governance has effectively ended or is about to end. |

### Red-Lines

Red-lines are specific thresholds that, when crossed, dramatically accelerate democratic breakdown:

| Red-Line | What It Means |
|----------|---------------|
| D5 (Electoral Fraud Machinery) | Infrastructure for manipulating election results is being put in place—not just rhetoric, but actual systems, personnel, or procedures. |
| D6 (Certification Override) | Mechanisms to override or reject legitimate election results are being established. |
| F6 (Leader Immunity) | The leader is being placed above the law through formal or de facto immunity from prosecution or accountability. |
| F2 (Loyalist Commanders) | Military or security leadership is being purged and replaced with personal loyalists rather than professional officers. |

## Section Descriptions (REQUIRED)

Each section of the report must include a brief explanation of what it shows and why it matters:

**Score Trajectory:** "This table shows how the DBS score has changed over time. The 'Delta' column shows the change from the previous assessment. Rising scores indicate democratic institutions are coming under increasing pressure."

**Tier Transitions:** "Tiers represent meaningful thresholds in democratic health. Moving from 'Elevated' to 'Backsliding' isn't just a number change—it indicates that erosion has progressed from testing limits to actively weakening institutions."

**Red-Line History:** "Red-lines are tripwires that, once crossed, make democratic recovery much harder. This section tracks which critical thresholds have been breached and when."

**Diagnostic Flags:** "Flags identify dangerous patterns that emerge from combinations of factors. A single concerning indicator might be manageable; when multiple problems combine in specific ways, they create compounding risks."

**Velocity Analysis:** "Speed matters. Gradual erosion gives institutions time to adapt and resist. Rapid escalation can overwhelm defensive capacity before it can organize."

## Executive Summary (REQUIRED)

Every report must conclude with an **Executive Summary** section written in plain language for a general audience. This section should:

1. **State the bottom line first** — What is the current state of democratic health for this topic?

2. **Explain the trajectory** — Is it getting better, worse, or stable? How quickly?

3. **Identify the key concerns** — What 2-3 factors most warrant attention?

4. **Provide historical context** — How does the current situation compare to historical patterns of democratic erosion?

5. **Note positive indicators** — Are there signs of institutional resistance or democratic resilience?

6. **Offer a forward-looking assessment** — Based on current trends, what developments should observers watch for?

Example Executive Summary:

```markdown
## Executive Summary

**Bottom Line:** Democratic institutions in [topic] are under significant and increasing pressure, with the DBS score rising from 42 to 58 over the past four months—moving from "Elevated Concern" into "Active Backsliding" territory.

**What This Means:** The score increase reflects real-world changes: mass dismissals of career officials, selective prosecution of political opponents, and the establishment of effective immunity for leadership from legal accountability. These aren't just political conflicts—they represent structural changes to how power is exercised and checked.

**Key Concerns:**
1. **The "sword and shield" pattern is now active** — The legal system is simultaneously being used to prosecute opponents while shielding allies. This two-tiered justice undermines the rule of law.
2. **Expertise has been gutted** — The removal of career professionals means oversight bodies lack the knowledge to identify problems, and institutional memory has been lost.
3. **Velocity is concerning** — The pace of change (+16 points in 4 months) is faster than typical democratic erosion, leaving less time for institutions to adapt.

**Historical Context:** The current trajectory resembles early-stage patterns seen in Hungary (2010-2014) and Turkey (2014-2016), where initial executive consolidation was followed by more aggressive moves once resistance proved weak. The key difference: [topic] starts with stronger institutional traditions, but those are being tested.

**Positive Signs:** Courts have issued several injunctions that temporarily blocked executive actions, and some civil servants have refused to implement potentially unlawful orders. These acts of resistance, tracked through the "institutional resistance" indicator, show the system retains some self-corrective capacity.

**What to Watch:** The next critical threshold is D5 (Electoral Fraud Machinery), currently at score 2. If preparations for the next election cycle include changes to election administration, certification processes, or voter access that advantage the incumbent, this red-line could trigger—which would add +15 to the score and signal that the electoral path to change is being foreclosed.
```

## Error Handling

- **No runs found:** "No DBS runs found for topic '[topic]'. Run `/dbs-run [topic]` first."
- **Single run (no trend):** "Only one run found for '[topic]'. Need 2+ runs for trend analysis."
- **Invalid topic:** "Topic '[topic]' not found. Available topics: [list]"
- **Date parsing error:** "Invalid date format. Use YYYY-MM-DD."
