# Fiscal Equalization Act

## Recommended Implementation for Regional Federalism

> **Purpose:** To establish transfer formulas and the Independent Fiscal Council as required by Article XVII of the Regional Federalism Constitution.

This Act operationalizes the fiscal architecture described in [05-fiscal-architecture.md](../02-design/05-fiscal-architecture.md) by providing formula specifications, institutional structures, and accountability mechanisms.

---

## Table of Contents

1. Overview and Constitutional Basis
2. The Independent Fiscal Council
3. Fiscal Capacity Measurement
4. The Equalization Formula
5. Transfer Mechanisms
6. Countercyclical Stabilization
7. Transparency and Accountability
8. Anti-Coercion Safeguards
9. Transition Provisions
10. Review and Amendment Procedures

---

## 1. Overview and Constitutional Basis

### 1.1 Constitutional Mandate

Article XVII, Section 1 requires Congress to enact "a Fiscal Equalization Act establishing transfer formulas and the Independent Fiscal Council."

Article XVII, Section 2(b) provides default rules if Congress fails to act within three years: "equalization transfers shall be calculated as flat per-capita grants at a baseline level equal to five percent of federal revenues, distributed to Regions with below-median fiscal capacity. This default rate shall decline by one percentage point per year beginning in year six, reaching a floor of two percent, to incentivize congressional action rather than reward inaction."

### 1.2 Purpose

This Act ensures:

- Regions have baseline capacity to provide public services regardless of tax base
- Market-driven regional divergence does not destabilize democracy
- Fiscal relationships are transparent, automatic, and non-coercive
- No level of government can govern by starving another

### 1.3 Guiding Principles

Per the design documents:

1. **Authority follows money**: Whoever funds a program controls it
2. **Money follows responsibility**: Funding matches assigned duties
3. **No governance by insolvency**: Adequate resources for allocated powers
4. **Automatic and formula-based**: No discretionary bargaining

---

## 2. The Independent Fiscal Council

### 2.1 Establishment

There is hereby established the Independent Fiscal Council (IFC) as an independent agency of the United States.

### 2.2 Composition

The Council shall consist of 9 members:

| Appointing Authority | Number | Selection Process |
|---------------------|--------|-------------------|
| President | 3 | Nomination with Senate confirmation |
| Senate | 3 | Selection by Senate majority and minority leaders jointly |
| Regional Governors | 3 | Selection by Regional Governors acting by majority vote |

### 2.3 Qualifications

Members must have:

- Demonstrated expertise in public finance, economics, or fiscal policy
- At least 10 years of relevant professional experience
- No current elected office or political party leadership position
- No employment by any government receiving equalization transfers (5-year lookback)

### 2.4 Terms and Tenure

**Terms:**
- 10-year staggered terms
- No member may serve more than one full term
- Initial appointments: 3 members serve 6 years, 3 serve 8 years, 3 serve 10 years

**Removal:**
- Members may be removed only for:
  - Incapacity (physical or mental inability to perform duties)
  - Serious misconduct (criminal conviction, ethics violation, conflict of interest)
  - Neglect of duty (persistent failure to participate)
- Policy disagreement is explicitly NOT grounds for removal
- Removal requires two-thirds vote of the Senate
- Removed member may appeal to the D.C. Circuit within 30 days

### 2.5 Independence Protections

- Council budget is mandatory spending (not subject to annual appropriation)
- Member compensation may not be reduced during term
- Council sets its own rules of procedure
- No other agency may direct Council actions

### 2.6 Powers and Duties

The Council shall:

1. Calculate annual fiscal capacity for each Region
2. Determine equalization transfer amounts using the statutory formula
3. Certify transfer calculations to Treasury for disbursement
4. Publish quarterly reports on regional fiscal conditions
5. Recommend formula adjustments to Congress
6. Conduct audits of transfer recipient compliance
7. Resolve disputes regarding capacity measurement

### 2.7 Limitations

The Council may NOT:

- Condition transfers on policy outcomes
- Withhold transfers for non-fiscal reasons
- Modify the statutory formula without Congressional authorization
- Make loans or provide credit to any government

---

## 3. Fiscal Capacity Measurement

### 3.1 Definition

"Fiscal capacity" means the ability of a Region to raise revenue from its own sources at standard tax effort.

### 3.2 Capacity Components

Fiscal capacity is measured across five revenue bases:

| Component | Weight | Measurement |
|-----------|--------|-------------|
| **Personal income** | 35% | Adjusted gross income of residents |
| **Property wealth** | 25% | Assessed value of real and personal property |
| **Consumption base** | 20% | Retail sales and service transactions |
| **Corporate presence** | 15% | Corporate income apportioned to Region |
| **Natural resources** | 5% | Severance taxes and resource royalties |

### 3.3 Standard Tax Effort

"Standard tax effort" means the average effective tax rate applied by all Regions weighted by population.

Capacity is calculated as:

```
Regional Capacity = Σ (Component Base × Component Weight × Standard Rate)
```

### 3.4 Per Capita Capacity

For equalization purposes:

```
Per Capita Capacity = Regional Capacity ÷ Regional Population
```

### 3.5 National Median

The "national median per capita capacity" is the population-weighted median of all Regional per capita capacities.

### 3.6 Data Sources

The Council shall use:

- IRS Statistics of Income (personal income)
- Census Bureau property value estimates (property)
- Bureau of Economic Analysis consumption data (consumption)
- State corporate tax apportionment data (corporate)
- Department of Interior resource data (natural resources)

### 3.7 Calculation Timeline

| Date | Action |
|------|--------|
| January 15 | Preliminary capacity estimates published |
| March 15 | Public comment period closes |
| April 15 | Final capacity determinations |
| July 1 | Transfer amounts certified to Treasury |
| October 1 | First quarterly transfer disbursed |

---

## 4. The Equalization Formula

### 4.1 Eligibility

A Region is eligible for equalization transfers if its per capita fiscal capacity is below the national median.

### 4.2 Transfer Amount

The equalization transfer for each eligible Region is:

```
Transfer = (Median Capacity - Regional Capacity) × Population × Equalization Rate
```

Where:
- Median Capacity = national median per capita capacity
- Regional Capacity = Region's per capita capacity
- Population = Region's population
- Equalization Rate = percentage of gap to be closed (see below)

### 4.3 Equalization Rate

The equalization rate determines what percentage of the capacity gap is closed by transfers:

| Capacity Gap | Equalization Rate |
|--------------|-------------------|
| 0-10% below median | 50% |
| 10-20% below median | 60% |
| 20-30% below median | 70% |
| >30% below median | 80% |

This graduated structure provides more support to Regions with greater need.

### 4.4 Transfer Cap

No Region may receive equalization transfers exceeding 15% of its own-source revenue. This prevents dependency and preserves incentives for fiscal effort.

### 4.5 Minimum Transfer

No eligible Region receives less than $50 per capita (inflation-adjusted to 2025 dollars).

### 4.6 Worked Example

**Region X Profile:**
- Population: 12 million
- Per capita capacity: $8,000
- National median: $10,000
- Capacity gap: 20%

**Calculation:**
- Gap amount: $10,000 - $8,000 = $2,000 per capita
- Equalization rate: 60% (10-20% gap tier)
- Transfer per capita: $2,000 × 60% = $1,200
- Total transfer: $1,200 × 12 million = $14.4 billion

---

## 5. Transfer Mechanisms

### 5.1 Disbursement Schedule

Transfers are disbursed quarterly:
- October 1 (25%)
- January 1 (25%)
- April 1 (25%)
- July 1 (25%)

### 5.2 Automatic Disbursement

Upon Council certification, Treasury shall disburse transfers without further Congressional action. Transfers are mandatory spending.

### 5.3 Use of Funds

Regions may use equalization transfers for any lawful governmental purpose. Transfers are NOT:
- Conditioned on specific policies
- Subject to federal program requirements
- Restricted to particular spending categories

### 5.4 Accountability

Regions receiving transfers shall:
- Publish annual reports on use of funds
- Maintain auditable financial records
- Cooperate with Council audits
- Report material changes in fiscal condition

### 5.5 Clawback Provisions

Transfers may be reduced or recovered only if:
- The Region provided false information affecting capacity calculation
- Calculation errors exceeded 5% of transfer amount
- The Region fails to maintain basic financial accountability

Clawbacks require Council determination and are subject to judicial review.

---

## 6. Countercyclical Stabilization

### 6.1 Purpose

The countercyclical stabilization mechanism ensures Regions can maintain services during economic downturns without pro-cyclical budget cuts.

### 6.2 Stabilization Triggers

Automatic stabilization activates when:
- National unemployment rate exceeds 6.5% for two consecutive quarters, OR
- Regional unemployment rate exceeds 8% for two consecutive quarters, OR
- GDP declines for two consecutive quarters (recession)

### 6.3 Stabilization Transfers

During stabilization periods:

| Trigger Level | Additional Transfer |
|---------------|---------------------|
| National unemployment 6.5-8% | +15% of baseline equalization |
| National unemployment 8-10% | +25% of baseline equalization |
| National unemployment >10% | +35% of baseline equalization |
| Regional unemployment >8% | +20% to affected Region |
| GDP decline >2% | +10% to all Regions |

### 6.4 Duration

Stabilization transfers continue until:
- Triggering condition no longer met for two consecutive quarters
- 24 months have elapsed (automatic review required)

### 6.5 Funding

Stabilization transfers are funded through:
- Federal borrowing authority (automatic)
- No offsetting cuts required during stabilization period

---

## 7. Transparency and Accountability

### 7.1 Public Reporting

The Council shall publish:

**Quarterly:**
- Regional fiscal capacity estimates
- Transfer calculations and disbursements
- Stabilization trigger status

**Annually:**
- Comprehensive regional fiscal profiles
- Formula performance assessment
- Recommendations for formula adjustment

### 7.2 Open Data

All Council data shall be:
- Machine-readable
- Downloadable without restriction
- Updated within 30 days of collection

### 7.3 Public Deliberations

All Council meetings shall be:
- Open to the public (except personnel matters)
- Live-streamed and archived
- Accompanied by published agendas and materials

### 7.4 Formula Changes

Any proposed formula change must include:
- 90-day public comment period
- Published economic impact analysis
- Congressional notification
- Phase-in period of at least 2 years

---

## 8. Anti-Coercion Safeguards

### 8.1 Prohibition on Conditions

No federal agency may condition equalization transfers on:
- Adoption of specific policies
- Participation in federal programs
- Political alignment or cooperation
- Waiver of constitutional rights

### 8.2 Prohibition on Withholding

No federal official may:
- Delay certified transfers
- Reduce transfers for non-fiscal reasons
- Threaten transfer reduction to influence policy

### 8.3 Enforcement

Violations of anti-coercion provisions:
- Create private right of action for affected Regions
- Subject violating officials to removal
- Trigger automatic disbursement by Treasury

### 8.4 Judicial Review

Regions may challenge:
- Capacity calculations (substantial evidence review)
- Formula application (de novo legal review)
- Coercive conditions (strict scrutiny)

---

## 9. Transition Provisions

### 9.1 Phase-In Period

**Year 1:**
- Council established and members confirmed
- Initial capacity measurements conducted
- Preliminary formula calculations published

**Year 2:**
- First transfers at 50% of formula amount
- Baseline data refined

**Year 3:**
- Transfers at 75% of formula amount
- Formula adjustments based on experience

**Year 4+:**
- Full formula implementation

### 9.2 Existing Programs

Federal grant programs to States that are superseded by equalization transfers shall be:
- Consolidated into equalization system
- Phased out over 3-year period
- Converted to unrestricted transfers

### 9.3 Hold-Harmless Provision

No Region shall receive less in combined transfers during Years 1-5 than it received in federal grants during the baseline year (last full fiscal year before enactment).

---

## 10. Review and Amendment Procedures

### 10.1 Periodic Review

The Council shall conduct comprehensive formula review every 5 years, including:
- Assessment of capacity measurement accuracy
- Evaluation of equalization effectiveness
- Analysis of regional fiscal trends
- Recommendations for adjustment

### 10.2 Congressional Amendment

Congress may amend the formula through regular legislative process. Amendments take effect:
- No sooner than 2 years after enactment
- With phase-in period for significant changes

### 10.3 Emergency Modifications

The Council may request emergency formula modifications from Congress when:
- External shocks create capacity measurement distortions
- Natural disasters affect regional fiscal conditions
- Financial crises disrupt normal operations

Emergency modifications are temporary (maximum 2 years) and require Congressional ratification.

---

## Relationship to Other Documents

- **Constitutional basis**: [09-constitution.md](../02-design/09-constitution.md), Article XVII
- **Design rationale**: [05-fiscal-architecture.md](../02-design/05-fiscal-architecture.md)
- **Power alignment**: [03-allocation-framework-act.md](03-allocation-framework-act.md)
- **Transition framework**: [02-transition-act.md](02-transition-act.md)

---

*This document provides recommended statutory language and implementation guidance. Actual legislation would require refinement through the legislative process.*
