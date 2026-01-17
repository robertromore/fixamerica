"""
House seat allocation simulation under Regional Federalism.

Compares current single-member district system with regional proportional
representation using the D'Hondt method.
"""

from dataclasses import dataclass, field
from typing import Dict, List, Optional
import math

from ..regions import RegionConfig, load_regions
from ..data_pipeline import ElectoralDataLoader


@dataclass
class HouseAllocationResult:
    """Results for a single region's House allocation."""
    region: str
    population: int  # thousands
    seats_allocated: int
    party_votes: Dict[str, int]
    party_seats: Dict[str, int]  # D, R, Other
    vote_share: Dict[str, float]
    seat_share: Dict[str, float]
    disproportionality: float  # Gallagher index contribution (squared difference)


@dataclass
class HouseAnalysis:
    """Complete House allocation analysis."""
    year: int
    total_seats: int
    threshold_pct: float
    results_by_region: List[HouseAllocationResult]
    national_gallagher_index: float
    party_totals: Dict[str, int]  # national seat totals
    national_vote_share: Dict[str, float]
    national_seat_share: Dict[str, float]
    third_party_seats: int
    comparison_to_current: Dict[str, any]


class HouseSimulator:
    """
    Simulates House seat allocation under Regional Federalism.

    Under RF, regions may choose proportional representation for House elections.
    This simulator compares D'Hondt PR allocation to current single-member districts.
    """

    # Total House seats (constitutional)
    TOTAL_SEATS = 435

    # Default threshold for PR (parties must exceed this to get seats)
    DEFAULT_THRESHOLD = 0.03  # 3%

    # Current House seats by state (118th Congress, 2023-2025)
    # Used for comparison to PR scenario
    CURRENT_SEATS_BY_STATE = {
        'AL': 7, 'AK': 1, 'AZ': 9, 'AR': 4, 'CA': 52,
        'CO': 8, 'CT': 5, 'DE': 1, 'FL': 28, 'GA': 14,
        'HI': 2, 'ID': 2, 'IL': 17, 'IN': 9, 'IA': 4,
        'KS': 4, 'KY': 6, 'LA': 6, 'ME': 2, 'MD': 8,
        'MA': 9, 'MI': 13, 'MN': 8, 'MS': 4, 'MO': 8,
        'MT': 2, 'NE': 3, 'NV': 4, 'NH': 2, 'NJ': 12,
        'NM': 3, 'NY': 26, 'NC': 14, 'ND': 1, 'OH': 15,
        'OK': 5, 'OR': 6, 'PA': 17, 'RI': 2, 'SC': 7,
        'SD': 1, 'TN': 9, 'TX': 38, 'UT': 4, 'VT': 1,
        'VA': 11, 'WA': 10, 'WV': 2, 'WI': 8, 'WY': 1,
        'DC': 0,  # DC has no voting House members
    }

    # Approximate current party breakdown by state (2023)
    # Format: (D seats, R seats)
    CURRENT_PARTY_BY_STATE = {
        'AL': (1, 6), 'AK': (0, 1), 'AZ': (3, 6), 'AR': (0, 4), 'CA': (40, 12),
        'CO': (5, 3), 'CT': (5, 0), 'DE': (1, 0), 'FL': (8, 20), 'GA': (5, 9),
        'HI': (2, 0), 'ID': (0, 2), 'IL': (14, 3), 'IN': (2, 7), 'IA': (1, 3),
        'KS': (1, 3), 'KY': (1, 5), 'LA': (1, 5), 'ME': (2, 0), 'MD': (7, 1),
        'MA': (9, 0), 'MI': (7, 6), 'MN': (4, 4), 'MS': (1, 3), 'MO': (2, 6),
        'MT': (0, 2), 'NE': (0, 3), 'NV': (3, 1), 'NH': (2, 0), 'NJ': (9, 3),
        'NM': (3, 0), 'NY': (15, 11), 'NC': (7, 7), 'ND': (0, 1), 'OH': (4, 11),
        'OK': (0, 5), 'OR': (4, 2), 'PA': (9, 8), 'RI': (2, 0), 'SC': (1, 6),
        'SD': (0, 1), 'TN': (2, 7), 'TX': (13, 25), 'UT': (1, 3), 'VT': (1, 0),
        'VA': (6, 5), 'WA': (8, 2), 'WV': (0, 2), 'WI': (4, 4), 'WY': (0, 1),
        'DC': (0, 0),
    }

    def __init__(self, regions: Optional[RegionConfig] = None):
        """Initialize with optional region configuration."""
        self.regions = regions or load_regions()
        self.data = ElectoralDataLoader(self.regions)

    def allocate_seats_dhondt(
        self, votes: Dict[str, int], seats: int, threshold: float = 0.03
    ) -> Dict[str, int]:
        """
        Allocate seats using D'Hondt method.

        Args:
            votes: Party -> vote count mapping
            seats: Number of seats to allocate
            threshold: Minimum vote share to qualify (0.0 to 1.0)

        Returns:
            Party -> seat count mapping
        """
        total_votes = sum(votes.values())
        if total_votes == 0:
            return {p: 0 for p in votes}

        # Filter parties below threshold
        eligible = {p: v for p, v in votes.items() if v / total_votes >= threshold}

        if not eligible:
            # No party meets threshold - give all seats to plurality winner
            winner = max(votes.items(), key=lambda x: x[1])[0]
            return {p: (seats if p == winner else 0) for p in votes}

        # D'Hondt: create quotients for each party/divisor combination
        quotients = []
        for party, vote_count in eligible.items():
            for divisor in range(1, seats + 1):
                quotients.append((vote_count / divisor, party, divisor))

        # Sort by quotient (descending) and allocate seats
        quotients.sort(reverse=True, key=lambda x: x[0])

        allocation = {p: 0 for p in votes}
        for i in range(min(seats, len(quotients))):
            _, party, _ = quotients[i]
            allocation[party] += 1

        return allocation

    def calculate_gallagher_index(
        self, vote_shares: Dict[str, float], seat_shares: Dict[str, float]
    ) -> float:
        """
        Calculate Gallagher index of disproportionality.

        The Gallagher index (LSq) measures how disproportional seat allocation is.
        Lower is better (0 = perfect proportionality).

        Formula: sqrt(0.5 * sum((vote_share - seat_share)^2))

        Args:
            vote_shares: Party -> vote share (0-1)
            seat_shares: Party -> seat share (0-1)

        Returns:
            Gallagher index (0-100 scale, lower is more proportional)
        """
        all_parties = set(vote_shares.keys()) | set(seat_shares.keys())

        sum_squared_diff = 0
        for party in all_parties:
            v_share = vote_shares.get(party, 0) * 100  # Convert to percentage
            s_share = seat_shares.get(party, 0) * 100
            sum_squared_diff += (v_share - s_share) ** 2

        return math.sqrt(0.5 * sum_squared_diff)

    def apportion_seats_by_population(
        self, populations: Dict[str, int], total_seats: int
    ) -> Dict[str, int]:
        """
        Apportion seats based on population using Huntington-Hill method.

        Args:
            populations: Unit -> population mapping
            total_seats: Total seats to allocate

        Returns:
            Unit -> seat count mapping
        """
        if not populations:
            return {}

        seats_remaining = total_seats

        # Initial allocation: 1 seat per unit (minimum)
        allocation = {r: 1 for r in populations}
        seats_remaining -= len(populations)

        # Huntington-Hill: allocate remaining seats by priority
        while seats_remaining > 0:
            # Priority = population / sqrt(n * (n+1)) where n = current seats
            priorities = {}
            for unit, pop in populations.items():
                n = allocation[unit]
                priorities[unit] = pop / math.sqrt(n * (n + 1))

            # Give seat to highest priority unit
            winner = max(priorities.items(), key=lambda x: x[1])[0]
            allocation[winner] += 1
            seats_remaining -= 1

        return allocation

    def apportion_seats_to_regions(self) -> Dict[str, int]:
        """
        Apportion House seats to regions based on population.

        Uses the Huntington-Hill method (same as U.S. Census).

        Returns:
            Region -> seat count mapping
        """
        populations = {}
        for region_name in self.regions.get_region_names():
            pop = self.regions.get_population_estimate(region_name)
            populations[region_name] = pop

        return self.apportion_seats_by_population(populations, self.TOTAL_SEATS)

    def analyze_region(
        self, region_name: str, year: int, seats: int, threshold: float
    ) -> HouseAllocationResult:
        """
        Analyze House allocation for a single region.

        Args:
            region_name: Name of region
            year: Election year
            seats: Number of seats for this region
            threshold: PR threshold

        Returns:
            HouseAllocationResult for the region
        """
        # Get regional vote totals
        regional_data = self.data.aggregate_by_region(year)
        region_votes = regional_data.get(region_name, {})

        # Get population (convert to thousands)
        pop = self.regions.get_population_estimate(region_name) // 1000

        # Aggregate votes by party category
        party_votes = {
            'D': region_votes.get('dem', 0),
            'R': region_votes.get('rep', 0),
            'Other': region_votes.get('other', 0),
        }

        total_votes = sum(party_votes.values())

        # Calculate vote shares
        vote_share = {}
        for party, votes in party_votes.items():
            vote_share[party] = votes / total_votes if total_votes > 0 else 0

        # Allocate seats using D'Hondt
        party_seats = self.allocate_seats_dhondt(party_votes, seats, threshold)

        # Calculate seat shares
        seat_share = {}
        for party, seat_count in party_seats.items():
            seat_share[party] = seat_count / seats if seats > 0 else 0

        # Calculate disproportionality contribution (squared difference sum)
        disproportionality = 0
        for party in party_votes:
            v = vote_share.get(party, 0) * 100
            s = seat_share.get(party, 0) * 100
            disproportionality += (v - s) ** 2

        return HouseAllocationResult(
            region=region_name,
            population=pop,
            seats_allocated=seats,
            party_votes=party_votes,
            party_seats=party_seats,
            vote_share=vote_share,
            seat_share=seat_share,
            disproportionality=disproportionality,
        )

    def get_current_allocation(self) -> Dict[str, Dict[str, int]]:
        """
        Get current House allocation aggregated by region.

        Returns:
            Region -> {'total': seats, 'D': d_seats, 'R': r_seats}
        """
        allocation = {}

        for region_name in self.regions.get_region_names():
            states = self.regions.get_states(region_name)
            total = 0
            d_seats = 0
            r_seats = 0

            for state in states:
                total += self.CURRENT_SEATS_BY_STATE.get(state, 0)
                party = self.CURRENT_PARTY_BY_STATE.get(state, (0, 0))
                d_seats += party[0]
                r_seats += party[1]

            allocation[region_name] = {
                'total': total,
                'D': d_seats,
                'R': r_seats,
                'Other': 0,  # Currently no third-party House members
            }

        return allocation

    def analyze_allocation(
        self, year: int, threshold: float = None
    ) -> HouseAnalysis:
        """
        Perform complete House allocation analysis.

        Args:
            year: Election year to analyze
            threshold: PR threshold (default 3%)

        Returns:
            HouseAnalysis with complete results
        """
        if threshold is None:
            threshold = self.DEFAULT_THRESHOLD

        # Apportion seats to regions
        regional_seats = self.apportion_seats_to_regions()

        # Analyze each region
        results = []
        for region_name in self.regions.get_region_names():
            seats = regional_seats[region_name]
            result = self.analyze_region(region_name, year, seats, threshold)
            results.append(result)

        # Calculate national totals
        party_totals = {'D': 0, 'R': 0, 'Other': 0}
        national_votes = {'D': 0, 'R': 0, 'Other': 0}

        for r in results:
            for party in party_totals:
                party_totals[party] += r.party_seats.get(party, 0)
                national_votes[party] += r.party_votes.get(party, 0)

        total_votes = sum(national_votes.values())
        total_seats = sum(party_totals.values())

        national_vote_share = {
            p: v / total_votes if total_votes > 0 else 0
            for p, v in national_votes.items()
        }
        national_seat_share = {
            p: s / total_seats if total_seats > 0 else 0
            for p, s in party_totals.items()
        }

        # Calculate national Gallagher index
        gallagher = self.calculate_gallagher_index(national_vote_share, national_seat_share)

        # Get current allocation for comparison
        current = self.get_current_allocation()
        current_totals = {'D': 0, 'R': 0, 'Other': 0}
        for region_data in current.values():
            for party in current_totals:
                current_totals[party] += region_data.get(party, 0)

        current_seat_share = {
            p: s / self.TOTAL_SEATS for p, s in current_totals.items()
        }
        current_gallagher = self.calculate_gallagher_index(
            national_vote_share, current_seat_share
        )

        comparison = {
            'current_total': self.TOTAL_SEATS,
            'rf_total': total_seats,
            'current_seats': current_totals,
            'pr_seats': party_totals,
            'seat_change': {p: party_totals[p] - current_totals[p] for p in party_totals},
            'current_gallagher': current_gallagher,
            'rf_gallagher': gallagher,
            'pr_gallagher': gallagher,  # Alias for compatibility
            'gallagher_improvement': current_gallagher - gallagher,
        }

        return HouseAnalysis(
            year=year,
            total_seats=total_seats,
            threshold_pct=threshold * 100,
            results_by_region=results,
            national_gallagher_index=gallagher,
            party_totals=party_totals,
            national_vote_share=national_vote_share,
            national_seat_share=national_seat_share,
            third_party_seats=party_totals.get('Other', 0),
            comparison_to_current=comparison,
        )

    # Method aliases for API consistency
    def analyze_house(self, year: int, threshold: float = None) -> HouseAnalysis:
        """Alias for analyze_allocation."""
        return self.analyze_allocation(year, threshold)

    def get_current_house_by_region(self) -> Dict[str, Dict[str, int]]:
        """Alias for get_current_allocation."""
        return self.get_current_allocation()

    def generate_report(self, year: int, threshold: float = None) -> str:
        """
        Generate markdown report for House allocation analysis.

        Args:
            year: Election year
            threshold: PR threshold

        Returns:
            Markdown-formatted report
        """
        analysis = self.analyze_allocation(year, threshold)

        lines = [
            f"# House Seat Allocation Analysis ({year})",
            "",
            "## Overview",
            "",
            "This analysis compares House seat allocation under:",
            "1. **Current system:** Single-member districts (winner-take-all)",
            "2. **Regional PR:** D'Hondt proportional representation by region",
            "",
            f"- **Total seats:** {analysis.total_seats}",
            f"- **PR threshold:** {analysis.threshold_pct:.1f}%",
            f"- **Regions:** {len(analysis.results_by_region)}",
            "",
            "## National Results",
            "",
            "### Vote Share vs Seat Share",
            "",
            "| Party | Vote Share | PR Seats | PR Share | Current Seats | Current Share |",
            "|-------|------------|----------|----------|---------------|---------------|",
        ]

        comp = analysis.comparison_to_current
        for party in ['D', 'R', 'Other']:
            v_share = analysis.national_vote_share.get(party, 0) * 100
            pr_seats = analysis.party_totals.get(party, 0)
            pr_share = analysis.national_seat_share.get(party, 0) * 100
            curr_seats = comp['current_seats'].get(party, 0)
            curr_share = curr_seats / analysis.total_seats * 100

            lines.append(
                f"| {party} | {v_share:.1f}% | {pr_seats} | {pr_share:.1f}% | "
                f"{curr_seats} | {curr_share:.1f}% |"
            )

        lines.extend([
            "",
            "### Proportionality Comparison",
            "",
            f"- **PR Gallagher Index:** {analysis.national_gallagher_index:.2f}",
            f"- **Current Gallagher Index:** {comp['current_gallagher']:.2f}",
            f"- **Improvement:** {comp['gallagher_improvement']:.2f} points",
            "",
            "*Lower Gallagher index indicates more proportional representation.*",
            "",
            "### Seat Changes Under PR",
            "",
            "| Party | Current | PR | Change |",
            "|-------|---------|-----|--------|",
        ])

        for party in ['D', 'R', 'Other']:
            curr = comp['current_seats'].get(party, 0)
            pr = analysis.party_totals.get(party, 0)
            change = comp['seat_change'].get(party, 0)
            sign = '+' if change > 0 else ''
            lines.append(f"| {party} | {curr} | {pr} | {sign}{change} |")

        lines.extend([
            "",
            f"**Third-party seats under PR:** {analysis.third_party_seats}",
            "",
            "## Regional Breakdown",
            "",
            "| Region | Population | Seats | D | R | Other | Gallagher |",
            "|--------|------------|-------|---|---|-------|-----------|",
        ])

        for r in sorted(analysis.results_by_region, key=lambda x: x.seats_allocated, reverse=True):
            gallagher_contrib = math.sqrt(0.5 * r.disproportionality)
            lines.append(
                f"| {r.region} | {r.population/1000:.1f}M | {r.seats_allocated} | "
                f"{r.party_seats.get('D', 0)} | {r.party_seats.get('R', 0)} | "
                f"{r.party_seats.get('Other', 0)} | {gallagher_contrib:.2f} |"
            )

        lines.extend([
            "",
            "## Key Findings",
            "",
            f"1. **Proportionality:** Regional PR reduces the Gallagher index from "
            f"{comp['current_gallagher']:.2f} to {analysis.national_gallagher_index:.2f}, "
            f"a {comp['gallagher_improvement']:.1f}-point improvement.",
            "",
        ])

        if analysis.third_party_seats > 0:
            lines.append(
                f"2. **Third-party representation:** PR would give third parties "
                f"{analysis.third_party_seats} seats (currently 0)."
            )
        else:
            lines.append(
                "2. **Third-party representation:** Even under PR, third parties "
                f"fall below the {analysis.threshold_pct:.0f}% threshold in most regions."
            )

        lines.extend([
            "",
            "## Methodology",
            "",
            "### D'Hondt Method",
            "",
            "Seats are allocated by dividing each party's votes by 1, 2, 3, etc., "
            "then awarding seats to the highest quotients until all seats are filled.",
            "",
            "### Gallagher Index",
            "",
            "```text",
            "LSq = sqrt(0.5 * sum((vote_share - seat_share)^2))",
            "```",
            "",
            "Scale: 0 (perfect proportionality) to ~30+ (highly disproportional).",
            "Typical values: <5 very proportional, 5-10 moderately, >10 disproportional.",
        ])

        return "\n".join(lines)


def run_house_analysis():
    """Run House allocation analysis and print report."""
    simulator = HouseSimulator()
    for year in [2016, 2020]:
        report = simulator.generate_report(year)
        print(report)
        print("\n" + "=" * 80 + "\n")


if __name__ == '__main__':
    run_house_analysis()
