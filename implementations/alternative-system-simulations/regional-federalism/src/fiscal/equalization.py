"""
Equalization transfer calculator under Regional Federalism.

Implements the equalization formula from the Fiscal Equalization Act, Section 4:

    Transfer = (Median Capacity - Regional Capacity) × Population × Equalization Rate

With graduated equalization rates based on the size of the capacity gap.
"""

from dataclasses import dataclass
from typing import Dict, List, Optional, Tuple

from ..regions import RegionConfig, load_regions
from .capacity import FiscalCapacityCalculator, CapacityAnalysis, RegionalCapacity


@dataclass
class EqualizationResult:
    """Equalization transfer results for a region."""
    region: str
    population: int  # thousands

    # Capacity metrics
    per_capita_capacity: float
    median_capacity: float
    capacity_gap_pct: float

    # Transfer calculation
    equalization_rate: float
    raw_transfer_per_capita: float
    raw_transfer_total: float  # billions

    # Constraints applied
    transfer_cap_applied: bool
    transfer_floor_applied: bool

    # Final transfer
    final_transfer_per_capita: float
    final_transfer_total: float  # billions

    # Context
    is_recipient: bool
    own_source_revenue: float  # billions (estimated)


@dataclass
class EqualizationAnalysis:
    """Complete equalization analysis."""
    year: int
    results: List[EqualizationResult]
    total_transfers: float  # billions
    total_recipients: int
    total_donors: int
    average_transfer_per_capita: float  # for recipients
    net_fiscal_impact: Dict[str, float]  # region -> net position


class EqualizationCalculator:
    """
    Calculates equalization transfers under Regional Federalism.

    Per the Fiscal Equalization Act, eligible regions receive transfers based
    on the gap between their fiscal capacity and the national median.
    """

    # Graduated equalization rates per Section 4.3
    EQUALIZATION_TIERS = [
        (0.10, 0.50),  # 0-10% below median -> 50%
        (0.20, 0.60),  # 10-20% below median -> 60%
        (0.30, 0.70),  # 20-30% below median -> 70%
        (1.00, 0.80),  # >30% below median -> 80%
    ]

    # Transfer constraints per Sections 4.4 and 4.5
    TRANSFER_CAP_PCT = 0.15  # 15% of own-source revenue
    TRANSFER_FLOOR_PER_CAPITA = 50  # $50 per capita minimum (2025 dollars)

    # Inflation adjustment to 2022 dollars (approximate)
    FLOOR_INFLATION_ADJUSTMENT = 0.94  # ~$47 in 2022 dollars

    # Estimated own-source revenue as % of GDP (for cap calculation)
    OWN_SOURCE_REVENUE_PCT = 0.10  # ~10% of regional GDP

    def __init__(self, regions: Optional[RegionConfig] = None):
        """Initialize with optional region configuration."""
        self.regions = regions or load_regions()
        self.capacity_calc = FiscalCapacityCalculator(self.regions)

    def get_equalization_rate(self, gap_pct: float) -> float:
        """
        Determine the equalization rate based on capacity gap.

        Args:
            gap_pct: Percentage below median (0.0 to 1.0)

        Returns:
            Equalization rate (0.0 to 1.0)
        """
        for threshold, rate in self.EQUALIZATION_TIERS:
            if gap_pct <= threshold:
                return rate
        return self.EQUALIZATION_TIERS[-1][1]  # Max rate

    def estimate_own_source_revenue(self, capacity: RegionalCapacity) -> float:
        """
        Estimate own-source revenue for a region.

        This is a proxy calculation since we don't have actual revenue data.
        Uses the capacity's underlying economic bases as a proxy for GDP.

        Args:
            capacity: Regional capacity data

        Returns:
            Estimated own-source revenue in billions
        """
        # Use personal income as a proxy for GDP (income ≈ 60-70% of GDP)
        estimated_gdp = capacity.personal_income / 0.65
        return estimated_gdp * self.OWN_SOURCE_REVENUE_PCT

    def calculate_region_transfer(
        self, capacity: RegionalCapacity, median_capacity: float
    ) -> EqualizationResult:
        """
        Calculate equalization transfer for a single region.

        Args:
            capacity: Regional capacity data
            median_capacity: National median per capita capacity

        Returns:
            EqualizationResult with transfer calculation details
        """
        # Determine if region is a recipient
        is_recipient = capacity.per_capita_capacity < median_capacity

        if not is_recipient:
            # Donor region - no transfer
            return EqualizationResult(
                region=capacity.region,
                population=capacity.population,
                per_capita_capacity=capacity.per_capita_capacity,
                median_capacity=median_capacity,
                capacity_gap_pct=0,
                equalization_rate=0,
                raw_transfer_per_capita=0,
                raw_transfer_total=0,
                transfer_cap_applied=False,
                transfer_floor_applied=False,
                final_transfer_per_capita=0,
                final_transfer_total=0,
                is_recipient=False,
                own_source_revenue=self.estimate_own_source_revenue(capacity)
            )

        # Calculate capacity gap
        gap_amount = median_capacity - capacity.per_capita_capacity
        gap_pct = gap_amount / median_capacity

        # Get equalization rate
        eq_rate = self.get_equalization_rate(gap_pct)

        # Calculate raw transfer
        raw_transfer_per_capita = gap_amount * eq_rate
        raw_transfer_total = (raw_transfer_per_capita * capacity.population * 1000) / 1_000_000_000  # billions

        # Estimate own-source revenue
        own_source = self.estimate_own_source_revenue(capacity)

        # Apply constraints
        transfer_cap_applied = False
        transfer_floor_applied = False

        final_transfer_total = raw_transfer_total

        # Cap: 15% of own-source revenue
        cap_amount = own_source * self.TRANSFER_CAP_PCT
        if final_transfer_total > cap_amount:
            final_transfer_total = cap_amount
            transfer_cap_applied = True

        # Floor: $50 per capita (inflation-adjusted)
        floor_per_capita = self.TRANSFER_FLOOR_PER_CAPITA * self.FLOOR_INFLATION_ADJUSTMENT
        floor_total = (floor_per_capita * capacity.population * 1000) / 1_000_000_000
        if final_transfer_total < floor_total:
            final_transfer_total = floor_total
            transfer_floor_applied = True

        final_transfer_per_capita = (final_transfer_total * 1_000_000_000) / (capacity.population * 1000)

        return EqualizationResult(
            region=capacity.region,
            population=capacity.population,
            per_capita_capacity=capacity.per_capita_capacity,
            median_capacity=median_capacity,
            capacity_gap_pct=gap_pct,
            equalization_rate=eq_rate,
            raw_transfer_per_capita=raw_transfer_per_capita,
            raw_transfer_total=raw_transfer_total,
            transfer_cap_applied=transfer_cap_applied,
            transfer_floor_applied=transfer_floor_applied,
            final_transfer_per_capita=final_transfer_per_capita,
            final_transfer_total=final_transfer_total,
            is_recipient=True,
            own_source_revenue=own_source
        )

    def analyze_equalization(self, year: int = 2022) -> EqualizationAnalysis:
        """
        Perform complete equalization analysis.

        Args:
            year: Analysis year

        Returns:
            EqualizationAnalysis with comprehensive results
        """
        # Get capacity analysis
        capacity_analysis = self.capacity_calc.analyze_all_regions(year)

        # Calculate transfers for each region
        results = []
        for regional_cap in capacity_analysis.regions:
            result = self.calculate_region_transfer(
                regional_cap,
                capacity_analysis.national_median_per_capita
            )
            results.append(result)

        # Calculate totals
        total_transfers = sum(r.final_transfer_total for r in results)
        recipients = [r for r in results if r.is_recipient]
        donors = [r for r in results if not r.is_recipient]

        avg_transfer_per_capita = 0
        if recipients:
            total_recipient_pop = sum(r.population for r in recipients)
            total_recipient_transfers = sum(r.final_transfer_total for r in recipients)
            avg_transfer_per_capita = (total_recipient_transfers * 1_000_000_000) / (total_recipient_pop * 1000)

        # Calculate net fiscal impact (positive = receives net transfers)
        # For donors, share is proportional to EXCESS capacity above median, not total capacity
        median = capacity_analysis.national_median_per_capita

        donor_excess_capacity = sum(
            (r.per_capita_capacity - median) * r.population
            for r in donors
            if r.per_capita_capacity > median
        )

        net_impact = {}
        for r in results:
            if r.is_recipient:
                net_impact[r.region] = r.final_transfer_total
            else:
                # Donor share proportional to excess capacity above median
                excess = (r.per_capita_capacity - median) * r.population
                if donor_excess_capacity > 0 and excess > 0:
                    share = excess / donor_excess_capacity
                    net_impact[r.region] = -total_transfers * share
                else:
                    net_impact[r.region] = 0

        return EqualizationAnalysis(
            year=year,
            results=results,
            total_transfers=total_transfers,
            total_recipients=len(recipients),
            total_donors=len(donors),
            average_transfer_per_capita=avg_transfer_per_capita,
            net_fiscal_impact=net_impact
        )

    def generate_report(self, year: int = 2022) -> str:
        """
        Generate a markdown report of equalization analysis.

        Args:
            year: Analysis year

        Returns:
            Markdown-formatted report
        """
        analysis = self.analyze_equalization(year)

        lines = [
            f"# Regional Equalization Transfer Analysis ({year})",
            "",
            "## Overview",
            "",
            "This analysis calculates equalization transfers under the Regional Federalism "
            "proposal, using the formula from the Fiscal Equalization Act.",
            "",
            "### Equalization Formula",
            "",
            "```text",
            "Transfer = (Median Capacity - Regional Capacity) × Population × Equalization Rate",
            "```",
            "",
            "### Graduated Equalization Rates",
            "",
            "| Capacity Gap | Equalization Rate |",
            "|--------------|-------------------|",
            "| 0-10% below median | 50% |",
            "| 10-20% below median | 60% |",
            "| 20-30% below median | 70% |",
            "| >30% below median | 80% |",
            "",
            "### Constraints",
            "",
            f"- **Transfer Cap:** {self.TRANSFER_CAP_PCT:.0%} of own-source revenue",
            f"- **Transfer Floor:** ${self.TRANSFER_FLOOR_PER_CAPITA}/capita (2025 dollars)",
            "",
            "## Summary Statistics",
            "",
            f"- **Total Transfers:** ${analysis.total_transfers:.2f} billion",
            f"- **Recipient Regions:** {analysis.total_recipients}",
            f"- **Donor Regions:** {analysis.total_donors}",
            f"- **Average Transfer (recipients):** ${analysis.average_transfer_per_capita:,.0f} per capita",
            "",
            "## Transfer Recipients",
            "",
            "| Region | Population | Gap % | Rate | Transfer | Per Capita | Constraints |",
            "|--------|------------|-------|------|----------|------------|-------------|",
        ]

        # Recipients first
        recipients = sorted(
            [r for r in analysis.results if r.is_recipient],
            key=lambda x: x.final_transfer_total,
            reverse=True
        )

        for r in recipients:
            constraints = []
            if r.transfer_cap_applied:
                constraints.append("Cap")
            if r.transfer_floor_applied:
                constraints.append("Floor")
            constraint_str = ", ".join(constraints) if constraints else "-"

            lines.append(
                f"| {r.region} | {r.population/1000:.1f}M | {r.capacity_gap_pct:.1%} | "
                f"{r.equalization_rate:.0%} | ${r.final_transfer_total:.2f}B | "
                f"${r.final_transfer_per_capita:,.0f} | {constraint_str} |"
            )

        lines.extend([
            "",
            "## Net Fiscal Position by Region",
            "",
            "Positive values indicate net transfer receipts; negative values indicate "
            "net contributions to the equalization pool.",
            "",
            "| Region | Net Position | Per Capita | Role |",
            "|--------|--------------|------------|------|",
        ])

        sorted_results = sorted(analysis.results, key=lambda x: analysis.net_fiscal_impact[x.region], reverse=True)

        for r in sorted_results:
            net = analysis.net_fiscal_impact[r.region]
            net_per_capita = (net * 1_000_000_000) / (r.population * 1000)
            role = "Recipient" if r.is_recipient else "Donor"
            sign = "+" if net > 0 else ""

            lines.append(
                f"| {r.region} | {sign}${net:.2f}B | {sign}${net_per_capita:,.0f} | {role} |"
            )

        lines.extend([
            "",
            "## Detailed Transfer Calculations",
            "",
            "### Transfer Breakdown",
            "",
        ])

        for r in recipients:
            lines.extend([
                f"**{r.region}:**",
                "",
                f"- Per capita capacity: ${r.per_capita_capacity:,.0f}",
                f"- Median capacity: ${r.median_capacity:,.0f}",
                f"- Capacity gap: ${r.median_capacity - r.per_capita_capacity:,.0f} ({r.capacity_gap_pct:.1%})",
                f"- Equalization rate: {r.equalization_rate:.0%}",
                f"- Raw transfer: ${r.raw_transfer_total:.2f}B (${r.raw_transfer_per_capita:,.0f}/capita)",
                f"- Final transfer: ${r.final_transfer_total:.2f}B (${r.final_transfer_per_capita:,.0f}/capita)",
                "",
            ])

        lines.extend([
            "## Key Findings",
            "",
            f"1. **Transfer Volume:** Total equalization transfers of ${analysis.total_transfers:.2f} billion "
            f"would flow annually from {analysis.total_donors} donor regions to "
            f"{analysis.total_recipients} recipient regions.",
            "",
        ])

        # Find largest recipient and donor
        if recipients:
            largest_recipient = max(recipients, key=lambda x: x.final_transfer_total)
            lines.append(
                f"2. **Largest Recipient:** {largest_recipient.region} would receive "
                f"${largest_recipient.final_transfer_total:.2f}B (${largest_recipient.final_transfer_per_capita:,.0f}/capita)."
            )
            lines.append("")

        donors = [r for r in analysis.results if not r.is_recipient]
        if donors:
            largest_donor = min(donors, key=lambda x: analysis.net_fiscal_impact[x.region])
            donor_amount = abs(analysis.net_fiscal_impact[largest_donor.region])
            lines.append(
                f"3. **Largest Contributor:** {largest_donor.region} would contribute "
                f"${donor_amount:.2f}B to the equalization pool."
            )
            lines.append("")

        lines.extend([
            "## Comparison to Current System",
            "",
            "Under the current system, federal transfers to states include:",
            "",
            "- Medicaid (formula-based, ~$700B total)",
            "- Highway Trust Fund (~$50B)",
            "- Education grants (~$40B)",
            "- Various categorical grants",
            "",
            "The Regional Federalism equalization system would:",
            "",
            "1. **Replace** categorical grants with unconditional transfers",
            "2. **Base** transfers on fiscal capacity, not program-specific formulas",
            "3. **Reduce** federal strings attached to funding",
            "4. **Provide** transparent, predictable revenue sharing",
        ])

        return "\n".join(lines)


def run_equalization_analysis():
    """Run equalization analysis and print report."""
    calculator = EqualizationCalculator()
    report = calculator.generate_report()
    print(report)


if __name__ == '__main__':
    run_equalization_analysis()
