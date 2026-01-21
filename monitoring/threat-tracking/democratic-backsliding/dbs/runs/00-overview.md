# DBS Runs

## Purpose

Each run folder captures a single DBS assessment for a defined window and run date, organized by topic.

## Naming

Use topic folders with ISO dates for run folders:

- `<topic>/YYYY-MM-DD/` (run date)

Examples:

- `trump/2026-02-28/`
- `orban/2026-02-28/`

## Contents

Each run folder should contain:

- `run.json` (machine-readable, schema-1.4)
- `run.md` (human-readable summary)

## Reproducibility

`run.json` should be derivable from `event-log.jsonl` (or topic-specific logs, if used) using the run window and scoring rules in `monitoring/threat-tracking/democratic-backsliding/dbs/initial-scoped-plan.md`.
