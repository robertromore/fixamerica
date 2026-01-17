# Regional Federalism Simulation Suite

Data-driven simulations modeling how U.S. elections and fiscal systems would operate under the Regional Federalism constitutional proposal.

## Overview

This package provides simulations to validate Regional Federalism design claims about:

1. **Electoral outcomes** - Comparing Electoral College vs Regional Federalism (NPV + RCV)
2. **Fiscal equalization** - Calculating transfer flows between regions

## Installation

```bash
cd implementations/alternative-system-simulations/regional-federalism
pip install -r requirements.txt
```

All commands below assume you are in the `regional-federalism` directory.

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

### Running Tests

```bash
# Run all tests (84 tests)
pytest tests/

# Run with verbose output
pytest tests/ -v

# Run specific test file
pytest tests/test_presidential.py
```

## Directory Structure

```text
regional-federalism/
├── config/
│   └── regions/
│       └── default.yaml        # Constitutional 7-region configuration
├── data/
│   ├── raw/                    # Original data sources
│   └── processed/              # Processed datasets
├── outputs/
│   └── reports/                # Generated analysis reports
├── src/
│   ├── regions.py              # Region configuration loader
│   ├── data_pipeline.py        # Electoral and fiscal data
│   ├── electoral/
│   │   └── presidential.py     # Presidential election simulation
│   └── fiscal/
│       ├── capacity.py         # Fiscal capacity calculator
│       └── equalization.py     # Transfer calculator
└── tests/
    ├── test_regions.py         # Region configuration tests
    ├── test_data_pipeline.py   # Data pipeline tests
    ├── test_presidential.py    # Presidential simulation tests
    └── test_fiscal.py          # Fiscal calculation tests
```

## Generated Reports

Running the simulations produces the following reports in `outputs/reports/`:

| Report | Description |
|--------|-------------|
| `presidential_2016_analysis.md` | 2016 election EC vs RF comparison |
| `presidential_2020_analysis.md` | 2020 election EC vs RF comparison |
| `presidential_comparison.md` | Multi-year comparison across elections |
| `fiscal_capacity_baseline.md` | Regional fiscal capacity analysis |
| `equalization_transfers.md` | Equalization transfer calculations |
| `equalization_analysis.md` | Detailed equalization breakdown |

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
| Northeast | CT, DE, ME, MD, MA, NH, NJ, NY, PA, RI, VT | 66M |
| Southeast | AL, AR, FL, GA, KY, LA, MS, NC, SC, TN, VA, WV | 78M |
| Midwest | IL, IN, IA, MI, MN, OH, WI | 52M |
| Great Plains | KS, MO, NE, ND, OK, SD | 14M |
| Southwest | AZ, CO, NV, NM, TX, UT | 52M |
| Pacific | AK, CA, HI, OR, WA | 55M |
| Mountain | ID, MT, WY | 3M |

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

## Implementation Status

### Completed

**Phase 1: Foundation**

- Region configuration with YAML loader
- Data pipeline with embedded electoral (2016, 2020) and fiscal (2022) data
- Directory structure and test infrastructure

**Phase 2: Electoral Simulations**

- Presidential NPV + RCV simulation
- Electoral College vs Regional Federalism comparison
- Winner-take-all analysis (swing state metrics)
- Multi-year comparison reports

**Phase 3: Fiscal Simulations**

- Fiscal capacity calculator (5-component weighted formula)
- Equalization transfer calculator (graduated rates, caps, floors)
- Donor/recipient analysis

### Planned (Not Yet Implemented)

- House seat allocation model (proportional representation with D'Hondt method)
- Senate composition model (14-seat regional Senate)
- Convergence projection (20-year trajectory modeling)
- 2024 election data integration
