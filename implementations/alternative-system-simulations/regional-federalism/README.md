# Regional Federalism Simulation Suite

Data-driven simulations modeling how U.S. elections and fiscal systems would operate under the Regional Federalism constitutional proposal.

## Overview

This package provides simulations to validate Regional Federalism design claims about:

1. **Electoral outcomes** - Comparing Electoral College vs Regional Federalism (NPV + RCV)
2. **Fiscal equalization** - Calculating transfer flows between regions

## Installation

```bash
pip install -r requirements.txt
```

## Usage

### Electoral Simulations

```python
from src.electoral.presidential import PresidentialSimulator

sim = PresidentialSimulator()

# Analyze a single election
analysis = sim.analyze_election(2020)
print(f"EC Winner: {analysis.ec_winner}")
print(f"RF Winner: {analysis.rf_winner}")
print(f"RCV Required: {analysis.rf_required_rcv}")
print(f"Outcome differs: {analysis.outcome_differs}")

# Generate comparison report
report = sim.compare_systems(2020)
print(report)
```

### Fiscal Simulations

```python
from src.fiscal.capacity import FiscalCapacityCalculator
from src.fiscal.equalization import EqualizationCalculator

# Calculate regional fiscal capacity
cap_calc = FiscalCapacityCalculator()
analysis = cap_calc.analyze_all_regions()
print(f"Median capacity: ${analysis.national_median_per_capita:,.0f}/capita")

# Calculate equalization transfers
eq_calc = EqualizationCalculator()
transfers = eq_calc.analyze_equalization()
print(f"Total transfers: ${transfers.total_transfers:.2f}B")
```

### Running from Command Line

```bash
# Test region configuration
python -m src.regions

# Test data pipeline
python -m src.data_pipeline

# Run presidential simulation
python -m src.electoral.presidential

# Run fiscal capacity analysis
python -m src.fiscal.capacity

# Run equalization transfer analysis
python -m src.fiscal.equalization
```

## Directory Structure

```text
regional-federalism/
├── config/
│   └── regions/
│       └── default.yaml    # Constitutional 7-region configuration
├── data/
│   ├── raw/               # Original data sources
│   └── processed/         # Processed datasets
├── outputs/
│   └── reports/           # Generated analysis reports
├── src/
│   ├── regions.py         # Region configuration loader
│   ├── data_pipeline.py   # Electoral and fiscal data
│   ├── electoral/
│   │   └── presidential.py # Presidential election simulation
│   └── fiscal/
│       ├── capacity.py    # Fiscal capacity calculator
│       └── equalization.py # Transfer calculator
└── tests/
```

## Data Sources

**Electoral:**

- Embedded 2016 and 2020 presidential results (FEC official)
- State-level vote totals and electoral votes

**Fiscal:**

- State GDP, population, and income (BEA/Census 2022)
- Fiscal capacity component estimates

## Regional Configuration

The default configuration uses the 7-region structure from Schedule A of the Regional Federal Constitution:

| Region | States | Est. Population |
|--------|--------|-----------------|
| Northeast | CT, DE, ME, MD, MA, NH, NJ, NY, PA, RI, VT | 65M |
| Southeast | AL, AR, FL, GA, KY, LA, MS, NC, SC, TN, VA, WV | 87M |
| Midwest | IL, IN, IA, MI, MN, OH, WI | 56M |
| Great Plains | KS, MO, NE, ND, OK, SD | 17M |
| Southwest | AZ, CO, NV, NM, TX, UT | 52M |
| Pacific | AK, CA, HI, OR, WA | 53M |
| Mountain | ID, MT, WY | 4M |

Alternative configurations can be created in `config/regions/` for scenario testing.

## Key Formulas

### Fiscal Capacity (Fiscal Equalization Act Section 3)

```text
Capacity = Σ (Component Base × Weight × Standard Rate)

Components:
- Personal income (35%)
- Property wealth (25%)
- Consumption base (20%)
- Corporate presence (15%)
- Natural resources (5%)
```

### Equalization Transfers (Section 4)

```text
Transfer = (Median Capacity - Regional Capacity) × Population × Rate

Graduated rates:
- 0-10% below median: 50%
- 10-20% below median: 60%
- 20-30% below median: 70%
- >30% below median: 80%

Constraints:
- Cap: 15% of own-source revenue
- Floor: $50/capita
```

## Related Documents

- [Regional Federal Constitution](../../plans/constitutional-amendments/comprehensive/regional-federalism/02-design/constitution/00-index.md)
- [Fiscal Equalization Act](../../plans/constitutional-amendments/comprehensive/regional-federalism/05-implementation/04-fiscal-equalization-act.md)
- [Elections Implementation Act](../../plans/constitutional-amendments/comprehensive/regional-federalism/05-implementation/05-elections-implementation-act.md)
