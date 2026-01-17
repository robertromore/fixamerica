# Regional Federalism Simulation Suite

Data-driven simulations modeling how U.S. elections and fiscal systems would operate under the Regional Federalism constitutional proposal.

## Overview

This package provides simulations to validate Regional Federalism design claims about:

1. **Electoral outcomes** - Comparing Electoral College vs Regional Federalism (NPV + RCV)
2. **Legislative composition** - House (proportional representation) and Senate (regional) models
3. **Fiscal equalization** - Calculating transfer flows between regions
4. **Convergence projection** - Modeling long-term fiscal capacity convergence

## Installation

```bash
cd implementations/alternative-system-simulations/regional-federalism
pip install -r requirements.txt
```

All commands below assume you are in the `regional-federalism` directory.

## Usage

### Unified CLI Runner

The easiest way to run simulations is via the unified CLI:

```bash
# Run all simulations
python -m src --all

# Run specific simulations
python -m src --presidential 2016 2020 2024
python -m src --house 2020 2024
python -m src --senate 2020
python -m src --fiscal
python -m src --convergence 20

# Custom output directory
python -m src --all --output ./my-reports
```

### Electoral Simulations

```python
from src.electoral.presidential import PresidentialSimulator

sim = PresidentialSimulator()

# Analyze a single election (2016, 2020, or 2024)
analysis = sim.analyze_election(2020)
print(f"EC Winner: {analysis.ec_winner}")
print(f"RF Winner: {analysis.rf_winner}")
print(f"RCV Required: {analysis.rf_required_rcv}")
print(f"Outcome differs: {analysis.outcome_differs}")

# Generate comparison report
report = sim.compare_systems(2020)
print(report)
```

### House Seat Allocation

```python
from src.electoral.house import HouseSimulator

sim = HouseSimulator()

# Analyze House composition under proportional representation
analysis = sim.analyze_house(2020)
print(f"Total seats: {analysis.total_seats}")
print(f"Gallagher index: {analysis.national_gallagher_index:.2f}")

# Generate report
report = sim.generate_report(2020)
print(report)
```

### Senate Composition

```python
from src.electoral.senate import SenateSimulator

sim = SenateSimulator()

# Analyze 16-seat regional Senate (14 regional + 2 DC)
analysis = sim.analyze_composition(2020)
print(f"D: {analysis.party_balance['D']}, R: {analysis.party_balance['R']}")
print(f"Majority: {analysis.majority_party}")

# Generate report
report = sim.generate_report(2020)
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

### Convergence Projection

```python
from src.fiscal.convergence import ConvergenceProjector

projector = ConvergenceProjector()

# Run 20-year projection
analysis = projector.run_projection(projection_years=20)
print(f"Initial CV: {analysis.initial_cv:.2%}")
print(f"Final CV: {analysis.final_cv:.2%}")
print(f"Convergence achieved: {analysis.convergence_achieved}")

# Generate report
report = projector.generate_report()
print(report)
```

### Running Individual Modules

```bash
# Test region configuration
python -m src.regions

# Test data pipeline
python -m src.data_pipeline

# Run presidential simulation
python -m src.electoral.presidential

# Run House allocation simulation
python -m src.electoral.house

# Run Senate composition simulation
python -m src.electoral.senate

# Run fiscal capacity analysis
python -m src.fiscal.capacity

# Run equalization transfer analysis
python -m src.fiscal.equalization

# Run convergence projection
python -m src.fiscal.convergence
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
│   ├── __main__.py             # Unified CLI runner
│   ├── regions.py              # Region configuration loader
│   ├── data_pipeline.py        # Electoral and fiscal data (2016, 2020, 2024)
│   ├── electoral/
│   │   ├── presidential.py     # Presidential election simulation
│   │   ├── house.py            # House PR allocation (D'Hondt)
│   │   └── senate.py           # Senate composition (regional)
│   └── fiscal/
│       ├── capacity.py         # Fiscal capacity calculator
│       ├── equalization.py     # Transfer calculator
│       └── convergence.py      # Convergence projection
└── tests/
    ├── test_regions.py         # Region configuration tests
    ├── test_data_pipeline.py   # Data pipeline tests
    ├── test_presidential.py    # Presidential simulation tests
    ├── test_house.py           # House allocation tests
    ├── test_senate.py          # Senate composition tests
    ├── test_fiscal.py          # Fiscal calculation tests
    └── test_convergence.py     # Convergence projection tests
```

## Generated Reports

Running `python -m src --all` produces the following reports in `outputs/reports/`:

| Report | Description |
|--------|-------------|
| `presidential_2016_analysis.md` | 2016 election EC vs RF comparison |
| `presidential_2020_analysis.md` | 2020 election EC vs RF comparison |
| `presidential_2024_analysis.md` | 2024 election EC vs RF comparison |
| `presidential_comparison.md` | Multi-year comparison across elections |
| `house_2016_analysis.md` | 2016 House PR allocation analysis |
| `house_2020_analysis.md` | 2020 House PR allocation analysis |
| `house_2024_analysis.md` | 2024 House PR allocation analysis |
| `senate_2016_analysis.md` | 2016 Senate composition analysis |
| `senate_2020_analysis.md` | 2020 Senate composition analysis |
| `senate_2024_analysis.md` | 2024 Senate composition analysis |
| `fiscal_capacity_baseline.md` | Regional fiscal capacity analysis |
| `equalization_transfers.md` | Equalization transfer calculations |
| `convergence_20yr_projection.md` | 20-year fiscal convergence projection |

## Data Sources

**Electoral:**

- Embedded 2016, 2020, and 2024 presidential results (FEC official)
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
- Data pipeline with embedded electoral (2016, 2020, 2024) and fiscal (2022) data
- Directory structure and test infrastructure

**Phase 2: Electoral Simulations**

- Presidential NPV + RCV simulation
- Electoral College vs Regional Federalism comparison
- Winner-take-all analysis (swing state metrics)
- Multi-year comparison reports
- House seat allocation model (proportional representation with D'Hondt method)
- Senate composition model (14-seat regional Senate + 2 DC)

**Phase 3: Fiscal Simulations**

- Fiscal capacity calculator (5-component weighted formula)
- Equalization transfer calculator (graduated rates, caps, floors)
- Donor/recipient analysis
- Convergence projection (20-year trajectory modeling)

**Phase 4: Integration**

- Unified CLI runner (`python -m src --all`)
- Comprehensive test suite
