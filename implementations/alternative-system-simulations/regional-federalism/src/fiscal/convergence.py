"""
Fiscal convergence projection under Regional Federalism.

Models the 20-year trajectory of regional fiscal capacity under the equalization
system, projecting how transfers affect regional economic convergence over time.
"""

from dataclasses import dataclass
from typing import Dict, List, Optional, Tuple
import math

from ..regions import RegionConfig, load_regions
from .capacity import FiscalCapacityCalculator, CapacityAnalysis
from .equalization import EqualizationCalculator, EqualizationAnalysis


@dataclass
class YearProjection:
    """Fiscal projection for a single year."""
    year: int
    regional_capacities: Dict[str, float]  # region -> per capita capacity
    coefficient_of_variation: float
    total_transfers: float  # billions
    convergence_rate: float  # year-over-year CV change (negative = converging)
    median_capacity: float
    min_capacity: float
    max_capacity: float
    spread_ratio: float  # max / min


@dataclass
class RegionTrajectory:
    """Trajectory data for a single region."""
    region: str
    initial_capacity: float
    final_capacity: float
    capacity_growth: float  # total growth over projection period
    annualized_growth: float  # compound annual growth rate
    years_as_recipient: int
    total_transfers_received: float  # billions
    initial_gap_pct: float  # gap from median at start
    final_gap_pct: float  # gap from median at end


@dataclass
class ConvergenceAnalysis:
    """Complete convergence analysis."""
    base_year: int
    projection_years: int
    base_growth_rate: float
    growth_dividend: float
    projections: List[YearProjection]
    region_trajectories: List[RegionTrajectory]
    years_to_convergence: Optional[int]  # when CV < threshold, None if not achieved
    final_cv: float
    initial_cv: float
    convergence_threshold: float
    convergence_achieved: bool


class ConvergenceProjector:
    """
    Projects fiscal capacity convergence under Regional Federalism equalization.

    Models how equalization transfers affect regional economic convergence over
    a multi-decade period, using growth dividend assumptions for transfer recipients.
    """

    # Default projection parameters
    DEFAULT_PROJECTION_YEARS = 20
    DEFAULT_BASE_GROWTH = 0.02  # 2% real growth (national baseline)
    DEFAULT_GROWTH_DIVIDEND = 0.01  # 1% additional growth for transfer recipients
    DEFAULT_CONVERGENCE_THRESHOLD = 0.10  # CV < 10% = converged

    # Population is assumed constant for simplicity (could add migration later)

    def __init__(self, regions: Optional[RegionConfig] = None):
        """Initialize with optional region configuration."""
        self.regions = regions or load_regions()
        self.capacity_calc = FiscalCapacityCalculator(self.regions)
        self.equalization_calc = EqualizationCalculator(self.regions)

    def calculate_coefficient_of_variation(
        self, capacities: Dict[str, float], populations: Dict[str, int]
    ) -> float:
        """
        Calculate population-weighted coefficient of variation.

        Args:
            capacities: Per capita capacity by region
            populations: Population (thousands) by region

        Returns:
            Coefficient of variation (std dev / mean)
        """
        total_pop = sum(populations.values())
        if total_pop == 0:
            return 0.0

        # Weighted mean
        weighted_sum = sum(
            capacities[r] * populations[r] for r in capacities
        )
        mean = weighted_sum / total_pop

        if mean == 0:
            return 0.0

        # Weighted variance
        weighted_var_sum = sum(
            populations[r] * (capacities[r] - mean) ** 2
            for r in capacities
        )
        variance = weighted_var_sum / total_pop
        std_dev = math.sqrt(variance)

        return std_dev / mean

    def get_median_capacity(self, capacities: Dict[str, float]) -> float:
        """Calculate median per capita capacity."""
        values = sorted(capacities.values())
        n = len(values)
        if n == 0:
            return 0.0
        if n % 2 == 0:
            return (values[n // 2 - 1] + values[n // 2]) / 2
        return values[n // 2]

    def project_single_year(
        self,
        current_capacities: Dict[str, float],
        populations: Dict[str, int],
        base_growth: float,
        growth_dividend: float,
    ) -> Tuple[Dict[str, float], float, Dict[str, float]]:
        """
        Project capacities forward one year.

        Args:
            current_capacities: Current per capita capacities
            populations: Regional populations
            base_growth: National baseline growth rate
            growth_dividend: Additional growth rate for transfer recipients

        Returns:
            Tuple of (new capacities, total transfers, per-region transfers)
        """
        median = self.get_median_capacity(current_capacities)
        new_capacities = {}
        transfers = {}

        for region, capacity in current_capacities.items():
            # Determine if region is a transfer recipient
            gap_pct = (median - capacity) / median if median > 0 else 0
            is_recipient = capacity < median

            # Calculate growth rate
            if is_recipient and gap_pct > 0:
                # Recipients get growth dividend proportional to their gap
                # Larger gaps -> more benefit from transfers
                dividend_factor = min(gap_pct / 0.30, 1.0)  # Cap at 30% gap
                growth = base_growth + (growth_dividend * dividend_factor)
            else:
                growth = base_growth

            # Project capacity forward
            new_capacities[region] = capacity * (1 + growth)

            # Calculate transfer amount (simplified - based on gap)
            if is_recipient:
                # Use simplified transfer formula
                # Full calculation would use EqualizationCalculator
                eq_rate = 0.50 if gap_pct <= 0.10 else (
                    0.60 if gap_pct <= 0.20 else (
                        0.70 if gap_pct <= 0.30 else 0.80
                    )
                )
                transfer_per_capita = (median - capacity) * eq_rate
                transfers[region] = (transfer_per_capita * populations[region] * 1000) / 1_000_000_000
            else:
                transfers[region] = 0.0

        total_transfers = sum(transfers.values())
        return new_capacities, total_transfers, transfers

    def run_projection(
        self,
        base_year: int = 2022,
        projection_years: int = None,
        base_growth: float = None,
        growth_dividend: float = None,
        convergence_threshold: float = None,
    ) -> ConvergenceAnalysis:
        """
        Run complete convergence projection.

        Args:
            base_year: Starting year for projection
            projection_years: Number of years to project
            base_growth: National baseline growth rate
            growth_dividend: Additional growth for transfer recipients
            convergence_threshold: CV threshold for convergence

        Returns:
            ConvergenceAnalysis with complete results
        """
        projection_years = projection_years or self.DEFAULT_PROJECTION_YEARS
        base_growth = base_growth if base_growth is not None else self.DEFAULT_BASE_GROWTH
        growth_dividend = growth_dividend if growth_dividend is not None else self.DEFAULT_GROWTH_DIVIDEND
        convergence_threshold = convergence_threshold or self.DEFAULT_CONVERGENCE_THRESHOLD

        # Get initial capacity data
        capacity_analysis = self.capacity_calc.analyze_all_regions(base_year)

        # Extract initial capacities and populations
        current_capacities = {
            r.region: r.per_capita_capacity
            for r in capacity_analysis.regions
        }
        populations = {
            r.region: r.population
            for r in capacity_analysis.regions
        }

        # Track initial state
        initial_capacities = current_capacities.copy()
        initial_cv = self.calculate_coefficient_of_variation(current_capacities, populations)
        initial_median = self.get_median_capacity(current_capacities)

        # Track cumulative transfers by region
        cumulative_transfers = {r: 0.0 for r in current_capacities}
        years_as_recipient = {r: 0 for r in current_capacities}

        # Run year-by-year projection
        projections = []
        years_to_convergence = None
        prev_cv = initial_cv

        # Add base year projection
        base_proj = YearProjection(
            year=base_year,
            regional_capacities=current_capacities.copy(),
            coefficient_of_variation=initial_cv,
            total_transfers=0.0,
            convergence_rate=0.0,
            median_capacity=initial_median,
            min_capacity=min(current_capacities.values()),
            max_capacity=max(current_capacities.values()),
            spread_ratio=max(current_capacities.values()) / min(current_capacities.values())
        )
        projections.append(base_proj)

        for year_offset in range(1, projection_years + 1):
            year = base_year + year_offset

            # Project forward one year
            new_capacities, total_transfers, transfers = self.project_single_year(
                current_capacities, populations, base_growth, growth_dividend
            )

            # Update cumulative transfers
            for region, transfer in transfers.items():
                cumulative_transfers[region] += transfer
                if transfer > 0:
                    years_as_recipient[region] += 1

            # Calculate metrics
            cv = self.calculate_coefficient_of_variation(new_capacities, populations)
            convergence_rate = cv - prev_cv  # Negative = converging
            median = self.get_median_capacity(new_capacities)

            # Check for convergence
            if years_to_convergence is None and cv < convergence_threshold:
                years_to_convergence = year_offset

            # Create year projection
            projection = YearProjection(
                year=year,
                regional_capacities=new_capacities.copy(),
                coefficient_of_variation=cv,
                total_transfers=total_transfers,
                convergence_rate=convergence_rate,
                median_capacity=median,
                min_capacity=min(new_capacities.values()),
                max_capacity=max(new_capacities.values()),
                spread_ratio=max(new_capacities.values()) / min(new_capacities.values())
            )
            projections.append(projection)

            current_capacities = new_capacities
            prev_cv = cv

        # Calculate region trajectories
        final_capacities = projections[-1].regional_capacities
        final_median = projections[-1].median_capacity

        trajectories = []
        for region in initial_capacities:
            initial_cap = initial_capacities[region]
            final_cap = final_capacities[region]
            total_growth = (final_cap - initial_cap) / initial_cap if initial_cap > 0 else 0
            cagr = ((final_cap / initial_cap) ** (1 / projection_years) - 1) if initial_cap > 0 else 0

            initial_gap = (initial_median - initial_cap) / initial_median if initial_median > 0 else 0
            final_gap = (final_median - final_cap) / final_median if final_median > 0 else 0

            trajectories.append(RegionTrajectory(
                region=region,
                initial_capacity=initial_cap,
                final_capacity=final_cap,
                capacity_growth=total_growth,
                annualized_growth=cagr,
                years_as_recipient=years_as_recipient[region],
                total_transfers_received=cumulative_transfers[region],
                initial_gap_pct=max(0, initial_gap),  # Only positive gaps
                final_gap_pct=max(0, final_gap),
            ))

        final_cv = projections[-1].coefficient_of_variation

        return ConvergenceAnalysis(
            base_year=base_year,
            projection_years=projection_years,
            base_growth_rate=base_growth,
            growth_dividend=growth_dividend,
            projections=projections,
            region_trajectories=trajectories,
            years_to_convergence=years_to_convergence,
            final_cv=final_cv,
            initial_cv=initial_cv,
            convergence_threshold=convergence_threshold,
            convergence_achieved=final_cv < convergence_threshold,
        )

    def generate_report(
        self,
        base_year: int = 2022,
        projection_years: int = None,
        base_growth: float = None,
        growth_dividend: float = None,
    ) -> str:
        """
        Generate markdown report of convergence projection.

        Args:
            base_year: Starting year
            projection_years: Years to project
            base_growth: Base growth rate
            growth_dividend: Growth dividend for recipients

        Returns:
            Markdown-formatted report
        """
        analysis = self.run_projection(
            base_year=base_year,
            projection_years=projection_years,
            base_growth=base_growth,
            growth_dividend=growth_dividend,
        )

        lines = [
            f"# Fiscal Convergence Projection ({analysis.base_year}-{analysis.base_year + analysis.projection_years})",
            "",
            "## Overview",
            "",
            "This analysis projects how regional fiscal capacity would converge over time "
            "under the Regional Federalism equalization system.",
            "",
            "### Model Assumptions",
            "",
            f"- **Base Year:** {analysis.base_year}",
            f"- **Projection Period:** {analysis.projection_years} years",
            f"- **Baseline Growth Rate:** {analysis.base_growth_rate:.1%} (national real GDP growth)",
            f"- **Growth Dividend:** {analysis.growth_dividend:.1%} (additional growth for transfer recipients)",
            f"- **Convergence Threshold:** CV < {analysis.convergence_threshold:.0%}",
            "",
            "The growth dividend models the economic boost from infrastructure investment, "
            "education funding, and other productive uses of equalization transfers.",
            "",
            "## Summary Results",
            "",
            f"- **Initial CV:** {analysis.initial_cv:.2%}",
            f"- **Final CV:** {analysis.final_cv:.2%}",
            f"- **CV Reduction:** {(analysis.initial_cv - analysis.final_cv):.2%} ({(analysis.initial_cv - analysis.final_cv) / analysis.initial_cv:.0%} improvement)",
        ]

        if analysis.convergence_achieved:
            lines.append(f"- **Convergence Achieved:** Yes, in year {analysis.years_to_convergence}")
        else:
            lines.append(f"- **Convergence Achieved:** No (threshold: CV < {analysis.convergence_threshold:.0%})")

        lines.extend([
            "",
            "## Year-by-Year Trajectory",
            "",
            "| Year | CV | Transfers ($B) | Min Cap | Median | Max Cap | Spread |",
            "|------|-----|----------------|---------|--------|---------|--------|",
        ])

        # Show every 5 years plus first and last
        show_years = set([analysis.base_year, analysis.base_year + analysis.projection_years])
        for i in range(0, analysis.projection_years + 1, 5):
            show_years.add(analysis.base_year + i)

        for proj in analysis.projections:
            if proj.year in show_years:
                lines.append(
                    f"| {proj.year} | {proj.coefficient_of_variation:.1%} | "
                    f"${proj.total_transfers:.1f} | ${proj.min_capacity:,.0f} | "
                    f"${proj.median_capacity:,.0f} | ${proj.max_capacity:,.0f} | "
                    f"{proj.spread_ratio:.1f}x |"
                )

        lines.extend([
            "",
            "## Regional Trajectories",
            "",
            "| Region | Initial | Final | Growth | CAGR | Years Recipient | Transfers |",
            "|--------|---------|-------|--------|------|-----------------|-----------|",
        ])

        # Sort by initial gap (largest gap first)
        sorted_trajectories = sorted(
            analysis.region_trajectories,
            key=lambda x: x.initial_gap_pct,
            reverse=True
        )

        for t in sorted_trajectories:
            lines.append(
                f"| {t.region} | ${t.initial_capacity:,.0f} | ${t.final_capacity:,.0f} | "
                f"{t.capacity_growth:+.1%} | {t.annualized_growth:.2%} | "
                f"{t.years_as_recipient} | ${t.total_transfers_received:.1f}B |"
            )

        lines.extend([
            "",
            "## Gap Analysis",
            "",
            "How regional gaps from median change over time:",
            "",
            "| Region | Initial Gap | Final Gap | Gap Reduction |",
            "|--------|-------------|-----------|---------------|",
        ])

        for t in sorted_trajectories:
            if t.initial_gap_pct > 0:
                gap_reduction = t.initial_gap_pct - t.final_gap_pct
                lines.append(
                    f"| {t.region} | {t.initial_gap_pct:.1%} | {t.final_gap_pct:.1%} | "
                    f"{gap_reduction:+.1%} |"
                )

        lines.extend([
            "",
            "## Key Findings",
            "",
        ])

        # Determine convergence narrative
        cv_reduction_pct = (analysis.initial_cv - analysis.final_cv) / analysis.initial_cv

        if analysis.convergence_achieved:
            lines.append(
                f"1. **Convergence Timeline:** Regional fiscal capacity would converge "
                f"(CV < {analysis.convergence_threshold:.0%}) within {analysis.years_to_convergence} years "
                f"under the equalization system."
            )
        else:
            lines.append(
                f"1. **Partial Convergence:** While CV decreases by {cv_reduction_pct:.0%}, "
                f"full convergence (CV < {analysis.convergence_threshold:.0%}) is not achieved "
                f"within the {analysis.projection_years}-year window."
            )

        lines.append("")

        # Find biggest winner and slowest converger
        biggest_recipient = max(sorted_trajectories, key=lambda x: x.total_transfers_received)
        fastest_grower = max(sorted_trajectories, key=lambda x: x.annualized_growth)

        lines.append(
            f"2. **Largest Beneficiary:** {biggest_recipient.region} receives "
            f"${biggest_recipient.total_transfers_received:.1f}B in cumulative transfers "
            f"over the projection period."
        )
        lines.append("")

        lines.append(
            f"3. **Fastest Growth:** {fastest_grower.region} achieves "
            f"{fastest_grower.annualized_growth:.2%} annualized growth, "
            f"compared to the {analysis.base_growth_rate:.1%} national baseline."
        )
        lines.append("")

        # Spread reduction
        initial_spread = analysis.projections[0].spread_ratio
        final_spread = analysis.projections[-1].spread_ratio
        spread_reduction = (initial_spread - final_spread) / initial_spread

        lines.append(
            f"4. **Spread Compression:** The ratio of highest to lowest capacity "
            f"decreases from {initial_spread:.1f}x to {final_spread:.1f}x "
            f"(a {spread_reduction:.0%} reduction)."
        )

        lines.extend([
            "",
            "## Sensitivity Analysis",
            "",
            "The convergence timeline is sensitive to the growth dividend assumption:",
            "",
            "| Growth Dividend | Expected Effect |",
            "|-----------------|-----------------|",
            "| 0.0% | No convergence acceleration |",
            "| 0.5% | Slow convergence |",
            "| 1.0% | Moderate convergence (baseline) |",
            "| 1.5% | Faster convergence |",
            "| 2.0% | Rapid convergence |",
            "",
            "Empirical studies of fiscal federalism suggest growth dividends in the 0.5-2.0% "
            "range are realistic for well-designed equalization systems.",
            "",
            "## Methodology Notes",
            "",
            "1. **Simplified Model:** This projection uses a simplified growth model. "
            "Full modeling would include population migration, economic shocks, and policy changes.",
            "",
            "2. **Constant Population:** Population is held constant. In practice, economic "
            "convergence may induce population shifts that affect capacity.",
            "",
            "3. **Growth Dividend:** The dividend is modeled as proportional to the capacity gap. "
            "Regions further below median benefit more from transfers.",
            "",
            "4. **Transfer Calculation:** Transfers are recalculated each year based on "
            "updated capacity figures.",
        ])

        return "\n".join(lines)


def run_convergence_projection():
    """Run convergence projection and print report."""
    projector = ConvergenceProjector()

    # Run default projection
    print("=" * 80)
    print("20-YEAR CONVERGENCE PROJECTION (Default Parameters)")
    print("=" * 80)
    print()
    report = projector.generate_report()
    print(report)

    # Run alternative scenario with higher dividend
    print("\n" + "=" * 80)
    print("20-YEAR CONVERGENCE PROJECTION (High Growth Dividend)")
    print("=" * 80)
    print()
    report = projector.generate_report(growth_dividend=0.02)
    print(report)


if __name__ == '__main__':
    run_convergence_projection()
