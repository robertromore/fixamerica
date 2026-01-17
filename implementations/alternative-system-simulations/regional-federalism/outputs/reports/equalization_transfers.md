# Regional Equalization Transfer Analysis (2022)

## Overview

This analysis calculates equalization transfers under the Regional Federalism proposal, using the formula from the Fiscal Equalization Act.

### Equalization Formula

```text
Transfer = (Median Capacity - Regional Capacity) × Population × Equalization Rate
```

### Graduated Equalization Rates

| Capacity Gap | Equalization Rate |
|--------------|-------------------|
| 0-10% below median | 50% |
| 10-20% below median | 60% |
| 20-30% below median | 70% |
| >30% below median | 80% |

### Constraints

- **Transfer Cap:** 15% of own-source revenue
- **Transfer Floor:** $50/capita (2025 dollars)

## Summary Statistics

- **Total Transfers:** $9.65 billion
- **Recipient Regions:** 4
- **Donor Regions:** 3
- **Average Transfer (recipients):** $59 per capita

## Transfer Recipients

| Region | Population | Gap % | Rate | Transfer | Per Capita | Constraints |
|--------|------------|-------|------|----------|------------|-------------|
| Southeast | 86.8M | 7.8% | 50% | $6.06B | $70 | - |
| Midwest | 56.0M | 2.2% | 50% | $2.63B | $47 | Floor |
| Great_Plains | 16.8M | 5.1% | 50% | $0.79B | $47 | Floor |
| Mountain | 3.6M | 3.4% | 50% | $0.17B | $47 | Floor |

## Net Fiscal Position by Region

Positive values indicate net transfer receipts; negative values indicate net contributions to the equalization pool.

| Region | Net Position | Per Capita | Role |
|--------|--------------|------------|------|
| Southeast | +$6.06B | +$70 | Recipient |
| Midwest | +$2.63B | +$47 | Recipient |
| Great_Plains | +$0.79B | +$47 | Recipient |
| Mountain | +$0.17B | +$47 | Recipient |
| Southwest | $0.00B | $0 | Donor |
| Northeast | $-4.29B | $-66 | Donor |
| Pacific | $-5.36B | $-101 | Donor |

## Detailed Transfer Calculations

### Transfer Breakdown

**Southeast:**

- Per capita capacity: $1,661
- Median capacity: $1,800
- Capacity gap: $140 (7.8%)
- Equalization rate: 50%
- Raw transfer: $6.06B ($70/capita)
- Final transfer: $6.06B ($70/capita)

**Midwest:**

- Per capita capacity: $1,760
- Median capacity: $1,800
- Capacity gap: $40 (2.2%)
- Equalization rate: 50%
- Raw transfer: $1.12B ($20/capita)
- Final transfer: $2.63B ($47/capita)

**Great_Plains:**

- Per capita capacity: $1,708
- Median capacity: $1,800
- Capacity gap: $92 (5.1%)
- Equalization rate: 50%
- Raw transfer: $0.77B ($46/capita)
- Final transfer: $0.79B ($47/capita)

**Mountain:**

- Per capita capacity: $1,739
- Median capacity: $1,800
- Capacity gap: $61 (3.4%)
- Equalization rate: 50%
- Raw transfer: $0.11B ($30/capita)
- Final transfer: $0.17B ($47/capita)

## Key Findings

1. **Transfer Volume:** Total equalization transfers of $9.65 billion would flow annually from 3 donor regions to 4 recipient regions.

2. **Largest Recipient:** Southeast would receive $6.06B ($70/capita).

3. **Largest Contributor:** Pacific would contribute $5.36B to the equalization pool.

## Comparison to Current System

Under the current system, federal transfers to states include:

- Medicaid (formula-based, ~$700B total)
- Highway Trust Fund (~$50B)
- Education grants (~$40B)
- Various categorical grants

The Regional Federalism equalization system would:

1. **Replace** categorical grants with unconditional transfers
2. **Base** transfers on fiscal capacity, not program-specific formulas
3. **Reduce** federal strings attached to funding
4. **Provide** transparent, predictable revenue sharing
