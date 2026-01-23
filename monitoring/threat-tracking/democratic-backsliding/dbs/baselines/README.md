# DBS Baselines

This directory contains reference baseline assessments used for comparative analysis. Baselines serve two purposes:

1. **Historical Calibrations** — Documented reference points from known cases of democratic backsliding, used to contextualize current assessments
2. **Topic Starting Points** — The initial assessment for each tracked topic, establishing the baseline from which trends are measured

## Baseline Types

### Historical Calibrations

These are synthesized assessments based on scholarly consensus about historical cases. They are not live runs but reference points derived from the DBS calibration table in `initial-scoped-plan.md` Section 7.1.

| Baseline | Period | DBS Range | Purpose |
|----------|--------|-----------|---------|
| `us-pre-2016` | Pre-2016 | 10-20 | US structural baseline before current stress period |
| `hungary-2010` | 2010 | ~25 | Orbán's return; starting point for Hungarian backsliding |
| `hungary-2015` | 2015 | ~50 | Mid-consolidation Hungary |
| `hungary-2020` | 2020 | 65-75 | Competitive authoritarianism established |
| `poland-2017` | 2015-2019 | 40-50 | PiS constitutional tribunal capture |
| `turkey-2014` | 2013-2016 | 50-60 | Post-Gezi, pre-coup |
| `turkey-2018` | 2017-present | 75-85 | Post-coup emergency consolidation |
| `venezuela-2016` | 2015-2017 | 60-70 | National Assembly neutralization |
| `venezuela-2020` | 2019-present | 85-95 | Near-complete consolidation |

### Topic Starting Points

These are actual DBS runs that establish the baseline for trend analysis of active topics.

| Topic | Baseline Date | Rationale |
|-------|---------------|-----------|
| `trump` | 2025-01-20 | Inauguration day; beginning of second term |
| `america` | 2025-01-20 | Country-level assessment starting same date |

## File Structure

```
baselines/
├── README.md                    # This file
├── historical/                  # Historical calibration baselines
│   ├── us-pre-2016.json
│   ├── hungary-2010.json
│   ├── hungary-2015.json
│   ├── hungary-2020.json
│   ├── poland-2017.json
│   ├── turkey-2014.json
│   ├── turkey-2018.json
│   ├── venezuela-2016.json
│   └── venezuela-2020.json
└── topics/                      # Topic starting point references
    ├── trump.json               # Points to runs/trump/2025-01-20
    └── america.json             # Points to runs/america/2025-01-20
```

## Historical Baseline Schema

Historical baselines use a simplified schema since they are reference points, not full runs:

```json
{
  "baseline_id": "hungary-2010",
  "baseline_type": "historical_calibration",
  "description": "Hungary at the start of Orbán's second government",
  "period": "2010",
  "period_notes": "Following Fidesz supermajority election victory",
  "dbs_range": {
    "low": 20,
    "mid": 25,
    "high": 30
  },
  "tier": "Concern",
  "pathway_mode": "hybrid",
  "key_checkpoints": {
    "C2": 2,
    "D3": 2,
    "D7": 2,
    "E1": 1
  },
  "red_lines_triggered": [],
  "diagnostic_flags": [],
  "narrative": "Early-stage consolidation. Constitutional court packing begins. Electoral system modifications proposed. Media pressure emerging but not yet systematic.",
  "scholarly_sources": [
    "Scheppele, Kim Lane. 'Autocratic Legalism.' University of Chicago Law Review (2018)",
    "Bánkuti, Halmai, Scheppele. 'Hungary's Illiberal Turn.' Journal of Democracy (2012)"
  ],
  "comparison_guidance": "Use as reference for early-stage executive consolidation in a parliamentary system with supermajority control."
}
```

## Topic Baseline Schema

Topic baselines are pointers to actual runs:

```json
{
  "topic": "trump",
  "baseline_type": "topic_starting_point",
  "baseline_run": "2025-01-20",
  "baseline_path": "../runs/trump/2025-01-20/run.json",
  "rationale": "Second term inauguration; establishes starting point for administration tracking",
  "notes": "All trend calculations for 'trump' topic use this as the reference point"
}
```

## Usage in Analysis

### Comparing to Historical Baselines

```bash
/dbs-analyze trump --compare hungary-2010 hungary-2015
```

This compares the current trump assessment to Hungary at two points in its backsliding trajectory, helping contextualize where the US currently sits relative to known historical patterns.

### Trend from Topic Baseline

```bash
/dbs-analyze trump --trend
```

Automatically uses the topic baseline (2025-01-20) as the starting point for trend calculations.

### Explicit Baseline Reference

```bash
/dbs-analyze trump --trend --baseline 2025-01-20
```

Forces a specific baseline date for trend calculations (useful if multiple baselines exist).

## Adding New Baselines

### Historical Calibrations

1. Review scholarly literature for the case
2. Map documented events to DBS checkpoints
3. Estimate scores based on checkpoint anchors in Appendix A
4. Document sources and reasoning
5. Create JSON file in `baselines/historical/`

### Topic Starting Points

1. Run `/dbs-run <topic> --date <baseline-date>`
2. Create pointer JSON in `baselines/topics/`
3. Update this README

## Interpretation Notes

- Historical baselines are **approximations** based on retrospective analysis, not contemporaneous assessments
- Score ranges (low/mid/high) reflect uncertainty in historical reconstruction
- Use historical baselines for **pattern matching and context**, not precise numeric comparisons
- Topic baselines are **actual runs** and can be compared directly to subsequent runs
