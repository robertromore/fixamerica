# Appendix Y: Metrics Dashboard Specifications

---

## Overview

This appendix provides detailed specifications for ICS performance dashboards, including KPI definitions, data collection protocols, visualization requirements, and reporting templates. These dashboards support operational management, accountability, and public transparency.

---

## Dashboard Hierarchy

### Dashboard Levels

| Level | Audience | Refresh | Access |
|-------|----------|---------|--------|
| **Executive** | Director; Congress | Daily | Restricted |
| **Operational** | Regional managers | Real-time | Staff |
| **Hub** | Hub directors | Real-time | Hub staff |
| **Public** | General public | Weekly | Open |

### Dashboard Structure

```
EXECUTIVE DASHBOARD
├── System-wide KPIs
├── Trend analysis
├── Exception alerts
└── Strategic indicators

OPERATIONAL DASHBOARD
├── Regional performance
├── Processing metrics
├── Compliance tracking
└── Resource utilization

HUB DASHBOARD
├── Hub-specific KPIs
├── Caseload management
├── Service delivery
└── Staff performance

PUBLIC DASHBOARD
├── Aggregate statistics
├── Processing times
├── Outcome data
└── Geographic distribution
```

---

## KPI Definitions

### Processing Metrics

#### KPI-001: Average Intake Processing Time

| Attribute | Value |
|-----------|-------|
| **Definition** | Calendar days from complete application submission to CLP issuance |
| **Formula** | SUM(Issue Date - Submission Date) / COUNT(Applications) |
| **Data source** | Case management system |
| **Measurement frequency** | Daily |
| **Target** | ≤30 days |
| **Threshold (Yellow)** | 31-45 days |
| **Threshold (Red)** | >45 days |
| **Drill-down** | By hub, by track (standard/legacy/asylum), by month |

#### KPI-002: Tier Advancement Processing Time

| Attribute | Value |
|-----------|-------|
| **Definition** | Calendar days from tier advancement application to decision |
| **Formula** | SUM(Decision Date - Application Date) / COUNT(Applications) |
| **Data source** | Case management system |
| **Measurement frequency** | Daily |
| **Target** | ≤45 days |
| **Threshold (Yellow)** | 46-60 days |
| **Threshold (Red)** | >60 days |
| **Drill-down** | By tier (A→B, B→C), by hub, by month |

#### KPI-003: Application Backlog

| Attribute | Value |
|-----------|-------|
| **Definition** | Number of pending applications older than target processing time |
| **Formula** | COUNT(Applications WHERE Days Pending > Target) |
| **Data source** | Case management system |
| **Measurement frequency** | Daily |
| **Target** | <5% of total pending |
| **Threshold (Yellow)** | 5-10% |
| **Threshold (Red)** | >10% |
| **Drill-down** | By application type, by hub, by age cohort |

### Integration Metrics

#### KPI-101: Employment Rate

| Attribute | Value |
|-----------|-------|
| **Definition** | Percentage of working-age participants (18-64) employed |
| **Formula** | (Employed Participants / Working-Age Participants) × 100 |
| **Data source** | Employment verification system |
| **Measurement frequency** | Monthly |
| **Target** | ≥75% at 6 months; ≥85% at 12 months |
| **Threshold (Yellow)** | 65-74% (6 mo); 75-84% (12 mo) |
| **Threshold (Red)** | <65% (6 mo); <75% (12 mo) |
| **Drill-down** | By hub, by tier, by time in program, by industry |

#### KPI-102: English Proficiency Gain

| Attribute | Value |
|-----------|-------|
| **Definition** | Average CEFR level improvement per year of program participation |
| **Formula** | (Post-Level - Pre-Level) / Years in Program |
| **Data source** | Language assessment records |
| **Measurement frequency** | Quarterly |
| **Target** | ≥1 CEFR level per year |
| **Threshold (Yellow)** | 0.5-0.99 levels |
| **Threshold (Red)** | <0.5 levels |
| **Drill-down** | By initial level, by hub, by age group |

#### KPI-103: Tier A→B Advancement Rate

| Attribute | Value |
|-----------|-------|
| **Definition** | Percentage of Tier A participants advancing to Tier B within 12 months |
| **Formula** | (Advanced to B / Eligible for Advancement) × 100 |
| **Data source** | Status history |
| **Measurement frequency** | Monthly |
| **Target** | ≥80% |
| **Threshold (Yellow)** | 70-79% |
| **Threshold (Red)** | <70% |
| **Drill-down** | By hub, by cohort, by reason for non-advancement |

#### KPI-104: Tier B→C Advancement Rate

| Attribute | Value |
|-----------|-------|
| **Definition** | Percentage of Tier B participants advancing to Tier C within 24 months |
| **Formula** | (Advanced to C / Eligible for Advancement) × 100 |
| **Data source** | Status history |
| **Measurement frequency** | Monthly |
| **Target** | ≥70% |
| **Threshold (Yellow)** | 60-69% |
| **Threshold (Red)** | <60% |
| **Drill-down** | By corridor, by cohort, by reason for non-advancement |

### Compliance Metrics

#### KPI-201: Geographic Compliance Rate

| Attribute | Value |
|-----------|-------|
| **Definition** | Percentage of participants residing in assigned geographic area |
| **Formula** | (Compliant Participants / Total Active) × 100 |
| **Data source** | Address verification; check-in data |
| **Measurement frequency** | Weekly |
| **Target** | ≥98% |
| **Threshold (Yellow)** | 95-97.9% |
| **Threshold (Red)** | <95% |
| **Drill-down** | By hub, by tier, by violation type |

#### KPI-202: Reporting Compliance Rate

| Attribute | Value |
|-----------|-------|
| **Definition** | Percentage of required reports/check-ins submitted on time |
| **Formula** | (Timely Reports / Required Reports) × 100 |
| **Data source** | Compliance tracking system |
| **Measurement frequency** | Weekly |
| **Target** | ≥95% |
| **Threshold (Yellow)** | 90-94.9% |
| **Threshold (Red)** | <90% |
| **Drill-down** | By report type, by hub, by participant |

#### KPI-203: Criminal Conviction Rate

| Attribute | Value |
|-----------|-------|
| **Definition** | Percentage of participants with criminal convictions (annual) |
| **Formula** | (Participants with Convictions / Total Active) × 100 |
| **Data source** | Criminal history checks; court notifications |
| **Measurement frequency** | Quarterly |
| **Target** | <2% |
| **Threshold (Yellow)** | 2-3% |
| **Threshold (Red)** | >3% |
| **Drill-down** | By offense type, by hub, by tier |

### Community Impact Metrics

#### KPI-301: Host Community Satisfaction

| Attribute | Value |
|-----------|-------|
| **Definition** | Percentage of surveyed residents with favorable view of ICS |
| **Formula** | (Favorable Responses / Total Responses) × 100 |
| **Data source** | Annual community survey |
| **Measurement frequency** | Annual |
| **Target** | ≥60% favorable |
| **Threshold (Yellow)** | 50-59% |
| **Threshold (Red)** | <50% |
| **Drill-down** | By hub, by demographics, by length of residence |

#### KPI-302: RID Distribution Accuracy

| Attribute | Value |
|-----------|-------|
| **Definition** | Percentage of RID payments correctly calculated and distributed |
| **Formula** | (Correct Payments / Total Payments) × 100 |
| **Data source** | Payment system |
| **Measurement frequency** | Monthly |
| **Target** | ≥99% |
| **Threshold (Yellow)** | 97-98.9% |
| **Threshold (Red)** | <97% |
| **Drill-down** | By hub, by error type |

#### KPI-303: School Capacity Utilization

| Attribute | Value |
|-----------|-------|
| **Definition** | Ratio of enrollment to capacity in schools with CLP students |
| **Formula** | Total Enrollment / Total Capacity |
| **Data source** | School enrollment data |
| **Measurement frequency** | Quarterly (during school year) |
| **Target** | ≤100% |
| **Threshold (Yellow)** | 101-105% |
| **Threshold (Red)** | >105% |
| **Drill-down** | By school, by district, by hub |

### Service Quality Metrics

#### KPI-401: Participant Satisfaction

| Attribute | Value |
|-----------|-------|
| **Definition** | Percentage of surveyed participants satisfied with ICS services |
| **Formula** | (Satisfied + Very Satisfied) / Total Responses × 100 |
| **Data source** | Participant surveys |
| **Measurement frequency** | Annual |
| **Target** | ≥70% |
| **Threshold (Yellow)** | 60-69% |
| **Threshold (Red)** | <60% |
| **Drill-down** | By service type, by hub, by tier |

#### KPI-402: Appointment Wait Time

| Attribute | Value |
|-----------|-------|
| **Definition** | Average days from appointment request to appointment date |
| **Formula** | SUM(Appointment Date - Request Date) / COUNT(Appointments) |
| **Data source** | Scheduling system |
| **Measurement frequency** | Weekly |
| **Target** | ≤14 days |
| **Threshold (Yellow)** | 15-21 days |
| **Threshold (Red)** | >21 days |
| **Drill-down** | By appointment type, by hub, by provider |

#### KPI-403: Complaint Resolution Time

| Attribute | Value |
|-----------|-------|
| **Definition** | Average days from complaint filing to resolution |
| **Formula** | SUM(Resolution Date - Filing Date) / COUNT(Complaints) |
| **Data source** | Complaint management system |
| **Measurement frequency** | Monthly |
| **Target** | ≤30 days |
| **Threshold (Yellow)** | 31-45 days |
| **Threshold (Red)** | >45 days |
| **Drill-down** | By complaint type, by hub, by resolution type |

### Financial Metrics

#### KPI-501: Cost Per Participant

| Attribute | Value |
|-----------|-------|
| **Definition** | Annual program cost divided by number of active participants |
| **Formula** | Annual Program Cost / Average Active Participants |
| **Data source** | Financial system |
| **Measurement frequency** | Quarterly |
| **Target** | ≤$5,000 |
| **Threshold (Yellow)** | $5,001-$6,000 |
| **Threshold (Red)** | >$6,000 |
| **Drill-down** | By cost category, by hub, by tier |

#### KPI-502: Fee Collection Rate

| Attribute | Value |
|-----------|-------|
| **Definition** | Percentage of assessed fees collected |
| **Formula** | (Collected Fees / Assessed Fees) × 100 |
| **Data source** | Financial system |
| **Measurement frequency** | Monthly |
| **Target** | ≥95% |
| **Threshold (Yellow)** | 90-94.9% |
| **Threshold (Red)** | <90% |
| **Drill-down** | By fee type, by hub |

---

## Dashboard Visualizations

### Executive Dashboard Components

| Component | Visualization | Purpose |
|-----------|---------------|---------|
| **KPI Summary** | Scorecard with stoplight | Quick status overview |
| **Trend Charts** | Line charts (12-month) | Direction of performance |
| **Geographic Map** | Heat map | Regional performance comparison |
| **Exception List** | Table with drill-down | Items requiring attention |
| **Volume Metrics** | Bar chart | Processing volumes |

### Operational Dashboard Components

| Component | Visualization | Purpose |
|-----------|---------------|---------|
| **Workload** | Stacked bar chart | Pending work by type |
| **Processing Funnel** | Funnel chart | Application flow stages |
| **Staff Utilization** | Gauge charts | Capacity vs. workload |
| **Daily Operations** | Real-time counters | Today's activity |
| **SLA Tracking** | Progress bars | Service level achievement |

### Hub Dashboard Components

| Component | Visualization | Purpose |
|-----------|---------------|---------|
| **Caseload** | Pie chart | Cases by status |
| **Daily Activities** | Calendar heat map | Appointment density |
| **Queue Monitor** | Real-time list | Current wait times |
| **Staff Dashboard** | Individual metrics | Personal performance |
| **Alerts** | Notification panel | Action items |

### Public Dashboard Components

| Component | Visualization | Purpose |
|-----------|---------------|---------|
| **Program Statistics** | Large number displays | Key counts |
| **Processing Times** | Range indicator | Current processing times |
| **Outcome Rates** | Donut charts | Success rates |
| **Geographic Distribution** | US map | Participant locations |
| **Trend Summary** | Sparklines | Performance direction |

---

## Data Collection Protocols

### Automated Data Collection

| Data Type | Source | Frequency | Method |
|-----------|--------|-----------|--------|
| **Application status** | Case system | Real-time | Database trigger |
| **Employment verification** | E-Verify | Daily batch | API call |
| **Address verification** | USPS | Weekly | API call |
| **Criminal records** | FBI | Event-driven | Push notification |
| **Language assessments** | Test providers | Weekly | File upload |

### Manual Data Collection

| Data Type | Source | Frequency | Method |
|-----------|--------|-----------|--------|
| **Participant surveys** | Participants | Annual | Online survey |
| **Community surveys** | Residents | Annual | Mixed mode |
| **Service quality audits** | Quality team | Quarterly | Observation |
| **Employer feedback** | Employers | Semi-annual | Online survey |

### Data Quality Rules

| Rule | Implementation |
|------|----------------|
| **Completeness** | Required fields enforced; null checks |
| **Validity** | Range checks; format validation |
| **Consistency** | Cross-field validation; referential integrity |
| **Timeliness** | Staleness alerts; refresh monitoring |
| **Accuracy** | Sample verification; reconciliation |

---

## Report Templates

### Weekly Operations Report

```
ICS WEEKLY OPERATIONS REPORT
Week of: [Date Range]
Prepared: [Date]

EXECUTIVE SUMMARY
• Total active participants: XXX,XXX
• Week-over-week change: +/-X.X%
• Critical issues: [Number]

PROCESSING METRICS
| Metric                    | This Week | Last Week | Target | Status |
|---------------------------|-----------|-----------|--------|--------|
| New intakes               | XXX       | XXX       | XXX    | [G/Y/R]|
| CLP issuances             | XXX       | XXX       | XXX    | [G/Y/R]|
| Tier advancements         | XXX       | XXX       | XXX    | [G/Y/R]|
| Average intake time (days)| XX        | XX        | 30     | [G/Y/R]|
| Backlog (>30 days)        | XXX       | XXX       | <5%    | [G/Y/R]|

COMPLIANCE SUMMARY
• Geographic compliance: XX.X%
• Reporting compliance: XX.X%
• Violations this week: XX

ISSUES & ACTIONS
1. [Issue description] - [Action taken]
2. [Issue description] - [Action taken]

NEXT WEEK OUTLOOK
• Expected volume: XXX intakes
• Staffing: [Status]
• Known issues: [Description]
```

### Monthly Performance Report

```
ICS MONTHLY PERFORMANCE REPORT
Month: [Month Year]
Prepared: [Date]

SECTION 1: EXECUTIVE SUMMARY
[Narrative summary of month's performance]

SECTION 2: KPI DASHBOARD
[Full KPI table with trend indicators]

SECTION 3: HUB PERFORMANCE COMPARISON
[Ranked list of hubs by composite score]

SECTION 4: INTEGRATION OUTCOMES
• Employment rate: XX.X%
• English proficiency gains: X.X levels
• Tier advancement rates: A→B XX.X%, B→C XX.X%

SECTION 5: COMPLIANCE
• Geographic compliance: XX.X%
• Violation trends: [Chart]
• Removal proceedings initiated: XX

SECTION 6: COMMUNITY IMPACT
• RID payments distributed: $X.XM
• School enrollment: XX,XXX CLP students
• Community feedback summary: [Narrative]

SECTION 7: FINANCIAL
• Monthly expenditure: $X.XM
• Budget variance: +/-X.X%
• Cost per participant: $X,XXX

SECTION 8: ISSUES AND RISKS
[Table of significant issues with mitigation status]

SECTION 9: NEXT MONTH PRIORITIES
1. [Priority 1]
2. [Priority 2]
3. [Priority 3]
```

### Quarterly Impact Report

```
ICS QUARTERLY IMPACT REPORT
Quarter: [Q# FY####]
Prepared: [Date]

EXECUTIVE OVERVIEW
[High-level narrative with key achievements and challenges]

PROGRAM SCALE
• Total participants (end of quarter): XXX,XXX
• Net growth: +XX,XXX (X.X%)
• Participants by tier: A: XX%, B: XX%, C: XX%
• Geographic distribution: [Map visualization]

INTEGRATION OUTCOMES
Employment
• Overall employment rate: XX.X%
• Median wage: $XX.XX/hour
• Top industries: [List]

Language
• Participants completing ESL: X,XXX
• Average CEFR improvement: X.X levels
• B1+ achievement rate: XX.X%

Civic Integration
• Civic modules completed: X,XXX
• Community participation rate: XX.X%

COMPLIANCE AND ENFORCEMENT
• Compliance rate: XX.X%
• Violations by type: [Chart]
• Removals: XXX
• Appeals: XXX (XX% success rate)

COMMUNITY IMPACT
Financial Flows
• RID distributed: $XX.XM
• Wages earned: $XXX.XM (estimated)
• Taxes paid: $XX.XM (estimated)

Community Indicators
• School performance: [Summary]
• Housing market: [Summary]
• Crime rates: [Summary]

ECONOMIC ANALYSIS
• GDP contribution (estimated): $X.XB
• Labor force impact: [Analysis]
• Fiscal impact: [Analysis]

LOOKING AHEAD
• Next quarter projections
• Emerging issues
• Policy recommendations
```

---

## Access and Security

### Access Control Matrix

| Dashboard | Public | Participant | Staff | Manager | Executive |
|-----------|--------|-------------|-------|---------|-----------|
| Public    | View   | View        | View  | View    | View      |
| Hub       | -      | Limited     | View  | View    | View      |
| Operations| -      | -           | -     | View    | View      |
| Executive | -      | -           | -     | -       | View      |

### Data Sensitivity

| Data Type | Classification | Display Rules |
|-----------|----------------|---------------|
| **Aggregate counts** | Public | No restrictions |
| **Processing times** | Public | No restrictions |
| **Hub-level metrics** | Internal | Staff access only |
| **Individual cases** | Confidential | Case access only |
| **PII** | Restricted | Never displayed |

---

## Technical Specifications

### Dashboard Platform

| Component | Specification |
|-----------|---------------|
| **Platform** | Power BI; Tableau; or custom |
| **Refresh rate** | Real-time to daily depending on metric |
| **Mobile support** | Responsive design |
| **Export** | PDF, Excel, CSV |
| **Embedding** | API for portal integration |

### Performance Requirements

| Metric | Target |
|--------|--------|
| **Page load** | <3 seconds |
| **Filter response** | <1 second |
| **Export** | <30 seconds |
| **Concurrent users** | 1,000+ |

---

## Related Documents

- [Metrics and Evaluation](../29-metrics-evaluation.md) - Evaluation framework
- [Oversight](../12-oversight.md) - Accountability structure
- [Appendix X: Technology Specifications](X-technology-specifications.md) - Technical architecture

---

## Document Navigation

- Previous: [Appendix X: Technology Specifications](X-technology-specifications.md)
- Next: [Appendix Z: Implementation Checklist](Z-implementation-checklist.md)
