# DBS Monitoring

## Purpose

This folder houses the operational data for DBS-v1.1e runs:

- `event-log.jsonl` is the canonical event log.
- `runs/` stores per-run outputs derived from the log.
- `templates/` contains starter files for log entries, run outputs, and the prompt template.

All methodology and schema rules are defined in `monitoring/threat-tracking/democratic-backsliding/dbs/initial-scoped-plan.md`.

## Workflow (per run)

1. Append verified events to `event-log.jsonl`.
2. Create a new `runs/YYYY-MM-DD/` folder.
3. Generate `run.json` from the event log for the selected window.
4. Write `run.md` using the DBS reporting format.

## Required Fields (high level)

- `run.json` must conform to DBS schema-1.4 and include `run_date`.
- `excluded_events_context` must be derived from `event-log.jsonl` exclusions.
- EX_TA entries require `mapped_checkpoint`, `elements_checked`, and evidence trigger docs.

## Notes

- The event log is the source of truth for runs.
- Runs should be reproducible by re-filtering the log by window and re-applying scoring.
