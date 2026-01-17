"""
Fiscal capacity calculator under Regional Federalism.

Implements the fiscal capacity measurement formula from the Fiscal Equalization Act,
Section 3:

    Fiscal capacity = Σ (Component Base × Component Weight × Standard Rate)

Components:
    - Personal income: 35%
    - Property wealth: 25%
    - Consumption base: 20%
    - Corporate presence: 15%
    - Natural resources: 5%
"""

from dataclasses import dataclass
from typing import Dict, List, Optional, Tuple
from enum import Enum

from ..regions import RegionConfig, load_regions


class CapacityComponent(Enum):
    """Fiscal capacity components per Fiscal Equalization Act Section 3.2."""
    PERSONAL_INCOME = ("Personal Income", 0.35)
    PROPERTY_WEALTH = ("Property Wealth", 0.25)
    CONSUMPTION_BASE = ("Consumption Base", 0.20)
    CORPORATE_PRESENCE = ("Corporate Presence", 0.15)
    NATURAL_RESOURCES = ("Natural Resources", 0.05)

    def __init__(self, description: str, weight: float):
        self.description = description
        self.weight = weight


@dataclass
class RegionalCapacity:
    """Fiscal capacity data for a region."""
    region: str
    population: int  # in thousands

    # Component bases (in billions USD)
    personal_income: float
    property_wealth: float
    consumption_base: float
    corporate_presence: float
    natural_resources: float

    # Calculated values
    total_capacity: float = 0.0
    per_capita_capacity: float = 0.0
    capacity_index: float = 0.0  # Relative to national median


@dataclass
class CapacityAnalysis:
    """Complete fiscal capacity analysis."""
    year: int
    regions: List[RegionalCapacity]
    national_median_per_capita: float
    national_average_per_capita: float
    above_median_regions: List[str]
    below_median_regions: List[str]
    capacity_range: Tuple[float, float]  # min, max per capita
    coefficient_of_variation: float


class FiscalCapacityCalculator:
    """
    Calculates fiscal capacity for each region under Regional Federalism.

    Per the Fiscal Equalization Act, fiscal capacity measures "the ability of
    a Region to raise revenue from its own sources at standard tax effort."
    """

    # State-level fiscal capacity component data (2022 estimates)
    # Sources: BEA, Census Bureau, IRS Statistics of Income
    # Values in billions USD unless otherwise noted
    STATE_CAPACITY_DATA = {
        # Personal income from BEA, property wealth estimated from Census/tax data,
        # consumption from BEA PCE, corporate from BEA GDP (industry),
        # natural resources from DOI/EIA
        'AL': {'income': 223.1, 'property': 450, 'consumption': 165, 'corporate': 45, 'resources': 8},
        'AK': {'income': 50.2, 'property': 120, 'consumption': 38, 'corporate': 15, 'resources': 25},
        'AZ': {'income': 351.0, 'property': 850, 'consumption': 280, 'corporate': 75, 'resources': 12},
        'AR': {'income': 127.8, 'property': 280, 'consumption': 100, 'corporate': 28, 'resources': 10},
        'CA': {'income': 2754.1, 'property': 8500, 'consumption': 1850, 'corporate': 650, 'resources': 35},
        'CO': {'income': 378.9, 'property': 900, 'consumption': 260, 'corporate': 85, 'resources': 18},
        'CT': {'income': 286.6, 'property': 450, 'consumption': 140, 'corporate': 70, 'resources': 1},
        'DE': {'income': 57.4, 'property': 120, 'consumption': 35, 'corporate': 30, 'resources': 0.5},
        'FL': {'income': 1127.4, 'property': 3200, 'consumption': 850, 'corporate': 200, 'resources': 5},
        'GA': {'income': 528.7, 'property': 1150, 'consumption': 400, 'corporate': 130, 'resources': 6},
        'HI': {'income': 84.9, 'property': 380, 'consumption': 65, 'corporate': 18, 'resources': 0.5},
        'ID': {'income': 86.4, 'property': 220, 'consumption': 68, 'corporate': 18, 'resources': 8},
        'IL': {'income': 786.3, 'property': 1400, 'consumption': 470, 'corporate': 180, 'resources': 8},
        'IN': {'income': 340.3, 'property': 650, 'consumption': 250, 'corporate': 80, 'resources': 6},
        'IA': {'income': 173.7, 'property': 380, 'consumption': 115, 'corporate': 40, 'resources': 5},
        'KS': {'income': 161.9, 'property': 300, 'consumption': 105, 'corporate': 38, 'resources': 12},
        'KY': {'income': 194.9, 'property': 380, 'consumption': 150, 'corporate': 42, 'resources': 14},
        'LA': {'income': 208.6, 'property': 400, 'consumption': 160, 'corporate': 55, 'resources': 35},
        'ME': {'income': 72.0, 'property': 180, 'consumption': 55, 'corporate': 14, 'resources': 3},
        'MD': {'income': 410.7, 'property': 850, 'consumption': 250, 'corporate': 75, 'resources': 2},
        'MA': {'income': 558.9, 'property': 950, 'consumption': 290, 'corporate': 130, 'resources': 1},
        'MI': {'income': 510.7, 'property': 950, 'consumption': 370, 'corporate': 110, 'resources': 8},
        'MN': {'income': 358.9, 'property': 680, 'consumption': 230, 'corporate': 85, 'resources': 6},
        'MS': {'income': 105.3, 'property': 210, 'consumption': 95, 'corporate': 22, 'resources': 8},
        'MO': {'income': 308.6, 'property': 600, 'consumption': 230, 'corporate': 65, 'resources': 5},
        'MT': {'income': 55.7, 'property': 140, 'consumption': 42, 'corporate': 12, 'resources': 10},
        'NE': {'income': 115.9, 'property': 250, 'consumption': 80, 'corporate': 32, 'resources': 3},
        'NV': {'income': 163.9, 'property': 450, 'consumption': 140, 'corporate': 40, 'resources': 10},
        'NH': {'income': 96.1, 'property': 220, 'consumption': 55, 'corporate': 22, 'resources': 1},
        'NJ': {'income': 641.6, 'property': 1400, 'consumption': 350, 'corporate': 120, 'resources': 1},
        'NM': {'income': 88.9, 'property': 210, 'consumption': 75, 'corporate': 22, 'resources': 20},
        'NY': {'income': 1564.9, 'property': 3600, 'consumption': 800, 'corporate': 380, 'resources': 3},
        'NC': {'income': 522.9, 'property': 1100, 'consumption': 380, 'corporate': 115, 'resources': 5},
        'ND': {'income': 47.8, 'property': 100, 'consumption': 35, 'corporate': 14, 'resources': 18},
        'OH': {'income': 609.8, 'property': 1100, 'consumption': 420, 'corporate': 135, 'resources': 10},
        'OK': {'income': 177.9, 'property': 340, 'consumption': 140, 'corporate': 45, 'resources': 28},
        'OR': {'income': 225.9, 'property': 600, 'consumption': 170, 'corporate': 55, 'resources': 8},
        'PA': {'income': 769.2, 'property': 1400, 'consumption': 480, 'corporate': 160, 'resources': 15},
        'RI': {'income': 63.9, 'property': 130, 'consumption': 42, 'corporate': 14, 'resources': 0.5},
        'SC': {'income': 233.3, 'property': 520, 'consumption': 185, 'corporate': 50, 'resources': 3},
        'SD': {'income': 50.9, 'property': 120, 'consumption': 38, 'corporate': 14, 'resources': 3},
        'TN': {'income': 352.9, 'property': 700, 'consumption': 280, 'corporate': 85, 'resources': 5},
        'TX': {'income': 1545.9, 'property': 3600, 'consumption': 1100, 'corporate': 400, 'resources': 120},
        'UT': {'income': 173.9, 'property': 450, 'consumption': 130, 'corporate': 45, 'resources': 12},
        'VT': {'income': 38.3, 'property': 100, 'consumption': 28, 'corporate': 8, 'resources': 2},
        'VA': {'income': 558.7, 'property': 1100, 'consumption': 340, 'corporate': 110, 'resources': 8},
        'WA': {'income': 542.9, 'property': 1200, 'consumption': 340, 'corporate': 140, 'resources': 8},
        'WV': {'income': 74.2, 'property': 140, 'consumption': 60, 'corporate': 18, 'resources': 12},
        'WI': {'income': 326.9, 'property': 650, 'consumption': 220, 'corporate': 75, 'resources': 4},
        'WY': {'income': 35.5, 'property': 85, 'consumption': 25, 'corporate': 10, 'resources': 18},
        'DC': {'income': 73.3, 'property': 250, 'consumption': 45, 'corporate': 35, 'resources': 0},
    }

    # Population in thousands (2022)
    STATE_POPULATION = {
        'AL': 5074, 'AK': 733, 'AZ': 7359, 'AR': 3045, 'CA': 39030,
        'CO': 5839, 'CT': 3626, 'DE': 1018, 'FL': 22245, 'GA': 10912,
        'HI': 1440, 'ID': 1939, 'IL': 12582, 'IN': 6833, 'IA': 3200,
        'KS': 2937, 'KY': 4512, 'LA': 4590, 'ME': 1385, 'MD': 6165,
        'MA': 6982, 'MI': 10037, 'MN': 5717, 'MS': 2940, 'MO': 6178,
        'MT': 1122, 'NE': 1967, 'NV': 3143, 'NH': 1395, 'NJ': 9261,
        'NM': 2114, 'NY': 19677, 'NC': 10698, 'ND': 779, 'OH': 11756,
        'OK': 4019, 'OR': 4241, 'PA': 12972, 'RI': 1096, 'SC': 5282,
        'SD': 909, 'TN': 7051, 'TX': 30030, 'UT': 3380, 'VT': 647,
        'VA': 8642, 'WA': 7785, 'WV': 1775, 'WI': 5896, 'WY': 577,
        'DC': 671
    }

    # Standard tax rates (population-weighted average effective rates)
    # These are estimates based on national averages
    STANDARD_RATES = {
        'income': 0.045,      # ~4.5% average effective income tax
        'property': 0.012,    # ~1.2% average property tax rate
        'consumption': 0.065, # ~6.5% average sales tax equivalent
        'corporate': 0.048,   # ~4.8% average corporate tax rate
        'resources': 0.085,   # ~8.5% average severance/royalty rate
    }

    def __init__(self, regions: Optional[RegionConfig] = None):
        """Initialize with optional region configuration."""
        self.regions = regions or load_regions()

    def calculate_state_capacity(self, state: str) -> float:
        """
        Calculate fiscal capacity for a single state.

        Args:
            state: Two-letter state code

        Returns:
            Total fiscal capacity in billions USD
        """
        if state not in self.STATE_CAPACITY_DATA:
            return 0.0

        data = self.STATE_CAPACITY_DATA[state]

        capacity = (
            data['income'] * CapacityComponent.PERSONAL_INCOME.weight * self.STANDARD_RATES['income'] +
            data['property'] * CapacityComponent.PROPERTY_WEALTH.weight * self.STANDARD_RATES['property'] +
            data['consumption'] * CapacityComponent.CONSUMPTION_BASE.weight * self.STANDARD_RATES['consumption'] +
            data['corporate'] * CapacityComponent.CORPORATE_PRESENCE.weight * self.STANDARD_RATES['corporate'] +
            data['resources'] * CapacityComponent.NATURAL_RESOURCES.weight * self.STANDARD_RATES['resources']
        )

        return capacity

    def calculate_regional_capacity(self, region_name: str) -> RegionalCapacity:
        """
        Calculate fiscal capacity for a region.

        Args:
            region_name: Name of the region

        Returns:
            RegionalCapacity object with all calculated values
        """
        states = self.regions.get_states(region_name)

        # Aggregate component bases
        total_income = 0.0
        total_property = 0.0
        total_consumption = 0.0
        total_corporate = 0.0
        total_resources = 0.0
        total_population = 0

        for state in states:
            if state in self.STATE_CAPACITY_DATA:
                data = self.STATE_CAPACITY_DATA[state]
                total_income += data['income']
                total_property += data['property']
                total_consumption += data['consumption']
                total_corporate += data['corporate']
                total_resources += data['resources']
            if state in self.STATE_POPULATION:
                total_population += self.STATE_POPULATION[state]

        # Calculate total capacity
        total_capacity = (
            total_income * CapacityComponent.PERSONAL_INCOME.weight * self.STANDARD_RATES['income'] +
            total_property * CapacityComponent.PROPERTY_WEALTH.weight * self.STANDARD_RATES['property'] +
            total_consumption * CapacityComponent.CONSUMPTION_BASE.weight * self.STANDARD_RATES['consumption'] +
            total_corporate * CapacityComponent.CORPORATE_PRESENCE.weight * self.STANDARD_RATES['corporate'] +
            total_resources * CapacityComponent.NATURAL_RESOURCES.weight * self.STANDARD_RATES['resources']
        )

        # Per capita capacity (in dollars, not billions)
        per_capita = (total_capacity * 1_000_000_000) / (total_population * 1000) if total_population > 0 else 0

        return RegionalCapacity(
            region=region_name,
            population=total_population,
            personal_income=total_income,
            property_wealth=total_property,
            consumption_base=total_consumption,
            corporate_presence=total_corporate,
            natural_resources=total_resources,
            total_capacity=total_capacity,
            per_capita_capacity=per_capita
        )

    def analyze_all_regions(self, year: int = 2022) -> CapacityAnalysis:
        """
        Perform complete fiscal capacity analysis for all regions.

        Args:
            year: Analysis year (for labeling)

        Returns:
            CapacityAnalysis with comprehensive results
        """
        # Calculate capacity for each region
        regional_capacities = []
        for region_name in self.regions.get_region_names():
            capacity = self.calculate_regional_capacity(region_name)
            regional_capacities.append(capacity)

        # Sort by per capita capacity for median calculation
        sorted_by_capacity = sorted(regional_capacities, key=lambda x: x.per_capita_capacity)

        # Calculate national median (population-weighted median)
        total_pop = sum(r.population for r in regional_capacities)
        cumulative_pop = 0
        median_capacity = 0.0

        for r in sorted_by_capacity:
            cumulative_pop += r.population
            if cumulative_pop >= total_pop / 2:
                median_capacity = r.per_capita_capacity
                break

        # Calculate national average
        total_capacity = sum(r.total_capacity for r in regional_capacities)
        avg_capacity = (total_capacity * 1_000_000_000) / (total_pop * 1000)

        # Update capacity index for each region
        for r in regional_capacities:
            r.capacity_index = r.per_capita_capacity / median_capacity if median_capacity > 0 else 1.0

        # Identify above/below median regions
        above_median = [r.region for r in regional_capacities if r.per_capita_capacity > median_capacity]
        below_median = [r.region for r in regional_capacities if r.per_capita_capacity <= median_capacity]

        # Capacity range
        capacity_range = (
            min(r.per_capita_capacity for r in regional_capacities),
            max(r.per_capita_capacity for r in regional_capacities)
        )

        # Coefficient of variation
        import math
        mean_capacity = sum(r.per_capita_capacity for r in regional_capacities) / len(regional_capacities)
        variance = sum((r.per_capita_capacity - mean_capacity) ** 2 for r in regional_capacities) / len(regional_capacities)
        cv = math.sqrt(variance) / mean_capacity if mean_capacity > 0 else 0

        return CapacityAnalysis(
            year=year,
            regions=regional_capacities,
            national_median_per_capita=median_capacity,
            national_average_per_capita=avg_capacity,
            above_median_regions=above_median,
            below_median_regions=below_median,
            capacity_range=capacity_range,
            coefficient_of_variation=cv
        )

    def generate_report(self, year: int = 2022) -> str:
        """
        Generate a markdown report of fiscal capacity analysis.

        Args:
            year: Analysis year

        Returns:
            Markdown-formatted report
        """
        analysis = self.analyze_all_regions(year)

        lines = [
            f"# Regional Fiscal Capacity Analysis ({year})",
            "",
            "## Overview",
            "",
            "This analysis calculates fiscal capacity for each region under the Regional "
            "Federalism proposal, using the formula from the Fiscal Equalization Act.",
            "",
            "### Capacity Formula",
            "",
            "Fiscal capacity = Σ (Component Base × Component Weight × Standard Rate)",
            "",
            "| Component | Weight |",
            "|-----------|--------|",
            f"| Personal Income | {CapacityComponent.PERSONAL_INCOME.weight:.0%} |",
            f"| Property Wealth | {CapacityComponent.PROPERTY_WEALTH.weight:.0%} |",
            f"| Consumption Base | {CapacityComponent.CONSUMPTION_BASE.weight:.0%} |",
            f"| Corporate Presence | {CapacityComponent.CORPORATE_PRESENCE.weight:.0%} |",
            f"| Natural Resources | {CapacityComponent.NATURAL_RESOURCES.weight:.0%} |",
            "",
            "## Summary Statistics",
            "",
            f"- **National Median Per Capita Capacity:** ${analysis.national_median_per_capita:,.0f}",
            f"- **National Average Per Capita Capacity:** ${analysis.national_average_per_capita:,.0f}",
            f"- **Capacity Range:** ${analysis.capacity_range[0]:,.0f} - ${analysis.capacity_range[1]:,.0f}",
            f"- **Coefficient of Variation:** {analysis.coefficient_of_variation:.3f}",
            "",
            "## Regional Fiscal Capacity",
            "",
            "| Region | Population (K) | Total Capacity ($B) | Per Capita ($) | Index |",
            "|--------|----------------|---------------------|----------------|-------|",
        ]

        # Sort by per capita capacity (highest first)
        sorted_regions = sorted(analysis.regions, key=lambda x: x.per_capita_capacity, reverse=True)

        for r in sorted_regions:
            index_str = f"{r.capacity_index:.2f}"
            lines.append(
                f"| {r.region} | {r.population:,} | ${r.total_capacity:.2f}B | "
                f"${r.per_capita_capacity:,.0f} | {index_str} |"
            )

        lines.extend([
            "",
            "## Equalization Eligibility",
            "",
            f"Regions with per capita capacity below the national median "
            f"(${analysis.national_median_per_capita:,.0f}) are eligible for equalization transfers.",
            "",
            "**Above Median (Net Contributors):**",
            "",
        ])

        for region in analysis.above_median_regions:
            r = next(x for x in analysis.regions if x.region == region)
            pct_above = ((r.per_capita_capacity / analysis.national_median_per_capita) - 1) * 100
            lines.append(f"- {region}: {pct_above:+.1f}% above median")

        lines.extend([
            "",
            "**Below Median (Transfer Recipients):**",
            "",
        ])

        for region in analysis.below_median_regions:
            r = next(x for x in analysis.regions if x.region == region)
            pct_below = (1 - (r.per_capita_capacity / analysis.national_median_per_capita)) * 100
            lines.append(f"- {region}: {pct_below:.1f}% below median")

        lines.extend([
            "",
            "## Component Breakdown",
            "",
            "| Region | Income | Property | Consumption | Corporate | Resources |",
            "|--------|--------|----------|-------------|-----------|-----------|",
        ])

        for r in sorted_regions:
            lines.append(
                f"| {r.region} | ${r.personal_income:.0f}B | ${r.property_wealth:.0f}B | "
                f"${r.consumption_base:.0f}B | ${r.corporate_presence:.0f}B | ${r.natural_resources:.1f}B |"
            )

        lines.extend([
            "",
            "## Key Findings",
            "",
            f"1. **Regional Inequality:** The coefficient of variation ({analysis.coefficient_of_variation:.3f}) "
            "indicates moderate regional disparity in fiscal capacity.",
            "",
            f"2. **Capacity Range:** The highest-capacity region has "
            f"{analysis.capacity_range[1]/analysis.capacity_range[0]:.1f}x the per capita capacity "
            "of the lowest-capacity region.",
            "",
            f"3. **Eligibility Split:** {len(analysis.below_median_regions)} regions are eligible for "
            f"equalization transfers, while {len(analysis.above_median_regions)} are net contributors.",
        ])

        return "\n".join(lines)


def run_capacity_analysis():
    """Run fiscal capacity analysis and print report."""
    calculator = FiscalCapacityCalculator()
    report = calculator.generate_report()
    print(report)


if __name__ == '__main__':
    run_capacity_analysis()
