"""
Senate composition simulation under Regional Federalism.

Models the 14-seat regional Senate (7 regions × 2 senators) plus DC representation,
compared to the current 100-seat state-based Senate.
"""

from dataclasses import dataclass
from typing import Dict, List, Optional

from ..regions import RegionConfig, load_regions
from ..data_pipeline import ElectoralDataLoader


@dataclass
class SenateRegionResult:
    """Senate results for a single region."""
    region: str
    population: int  # thousands
    senators: int  # Always 2 per region
    party_control: str  # 'D', 'R', or 'Split'
    dem_votes: int
    rep_votes: int
    vote_margin: float  # Positive = D lead, negative = R lead
    dem_senators: int
    rep_senators: int


@dataclass
class SenateAnalysis:
    """Complete Senate composition analysis."""
    year: int
    total_senators: int  # 14 regional + 2 DC = 16
    regional_results: List[SenateRegionResult]
    party_balance: Dict[str, int]  # D, R totals
    dc_senators: Dict[str, int]  # DC representation
    majority_party: str
    comparison_to_current: Dict[str, any]


class SenateSimulator:
    """
    Simulates Senate composition under Regional Federalism.

    Under RF, the Senate has 14 seats (2 per region) plus 2 DC senators,
    compared to the current 100-seat state-based Senate.
    """

    # Senators per region (constitutional)
    SENATORS_PER_REGION = 2

    # DC gets 2 senators under RF
    DC_SENATORS = 2

    # Current Senate composition by state (118th Congress, 2023-2025)
    # Format: (D, R) - Independents caucusing with D counted as D
    CURRENT_SENATE_BY_STATE = {
        'AL': (0, 2), 'AK': (0, 2), 'AZ': (1, 1), 'AR': (0, 2), 'CA': (2, 0),
        'CO': (2, 0), 'CT': (2, 0), 'DE': (2, 0), 'FL': (0, 2), 'GA': (2, 0),
        'HI': (2, 0), 'ID': (0, 2), 'IL': (2, 0), 'IN': (0, 2), 'IA': (0, 2),
        'KS': (0, 2), 'KY': (0, 2), 'LA': (0, 2), 'ME': (1, 1), 'MD': (2, 0),
        'MA': (2, 0), 'MI': (2, 0), 'MN': (2, 0), 'MS': (0, 2), 'MO': (0, 2),
        'MT': (1, 1), 'NE': (0, 2), 'NV': (2, 0), 'NH': (2, 0), 'NJ': (2, 0),
        'NM': (2, 0), 'NY': (2, 0), 'NC': (0, 2), 'ND': (0, 2), 'OH': (1, 1),
        'OK': (0, 2), 'OR': (2, 0), 'PA': (1, 1), 'RI': (2, 0), 'SC': (0, 2),
        'SD': (0, 2), 'TN': (0, 2), 'TX': (0, 2), 'UT': (0, 2), 'VT': (2, 0),
        'VA': (2, 0), 'WA': (2, 0), 'WV': (0, 2), 'WI': (1, 1), 'WY': (0, 2),
        'DC': (0, 0),  # DC has no senators currently
    }

    def __init__(self, regions: Optional[RegionConfig] = None):
        """Initialize with optional region configuration."""
        self.regions = regions or load_regions()
        self.data = ElectoralDataLoader(self.regions)

    def get_current_senate_by_region(self) -> Dict[str, Dict[str, int]]:
        """
        Aggregate current Senate seats by region.

        Returns:
            Region -> {'D': count, 'R': count, 'total': count}
        """
        result = {}

        for region_name in self.regions.get_region_names():
            states = self.regions.get_states(region_name)
            d_total = 0
            r_total = 0

            for state in states:
                d, r = self.CURRENT_SENATE_BY_STATE.get(state, (0, 0))
                d_total += d
                r_total += r

            result[region_name] = {
                'D': d_total,
                'R': r_total,
                'total': d_total + r_total,
            }

        return result

    def analyze_region(self, region_name: str, year: int) -> SenateRegionResult:
        """
        Analyze Senate composition for a single region.

        Under RF, regions elect 2 senators. We model this as winner-take-all
        (majority party gets both seats), which is the most common approach
        in regional/at-large elections.

        Args:
            region_name: Name of region
            year: Election year (for vote data)

        Returns:
            SenateRegionResult for the region
        """
        # Get regional vote totals
        regional_data = self.data.aggregate_by_region(year)
        region_votes = regional_data.get(region_name, {})

        # Get population (convert to thousands)
        pop = self.regions.get_population_estimate(region_name) // 1000

        dem_votes = region_votes.get('dem', 0)
        rep_votes = region_votes.get('rep', 0)
        total_votes = dem_votes + rep_votes

        # Calculate margin (positive = D lead)
        margin = 0
        if total_votes > 0:
            margin = (dem_votes - rep_votes) / total_votes

        # Determine party control and seat allocation
        # Winner-take-all: majority party gets both senators
        if dem_votes > rep_votes:
            party_control = 'D'
            dem_senators = 2
            rep_senators = 0
        elif rep_votes > dem_votes:
            party_control = 'R'
            dem_senators = 0
            rep_senators = 2
        else:
            # Exact tie - split
            party_control = 'Split'
            dem_senators = 1
            rep_senators = 1

        return SenateRegionResult(
            region=region_name,
            population=pop,
            senators=self.SENATORS_PER_REGION,
            party_control=party_control,
            dem_votes=dem_votes,
            rep_votes=rep_votes,
            vote_margin=margin,
            dem_senators=dem_senators,
            rep_senators=rep_senators,
        )

    def analyze_composition(self, year: int) -> SenateAnalysis:
        """
        Perform complete Senate composition analysis.

        Args:
            year: Election year to analyze

        Returns:
            SenateAnalysis with complete results
        """
        # Analyze each region
        results = []
        for region_name in self.regions.get_region_names():
            result = self.analyze_region(region_name, year)
            results.append(result)

        # Calculate party totals (excluding DC)
        regional_d = sum(r.dem_senators for r in results)
        regional_r = sum(r.rep_senators for r in results)

        # DC gets 2 senators - assumed D based on voting patterns
        # (DC votes ~90% Democratic in presidential elections)
        dc_senators = {'D': 2, 'R': 0}

        total_d = regional_d + dc_senators['D']
        total_r = regional_r + dc_senators['R']
        total_senators = total_d + total_r

        party_balance = {'D': total_d, 'R': total_r}
        majority_party = 'D' if total_d > total_r else ('R' if total_r > total_d else 'Tie')

        # Get current Senate for comparison
        current_by_region = self.get_current_senate_by_region()
        current_d = sum(r['D'] for r in current_by_region.values())
        current_r = sum(r['R'] for r in current_by_region.values())

        comparison = {
            'current_total': 100,
            'rf_total': total_senators,
            'current_d': current_d,
            'current_r': current_r,
            'rf_d': total_d,
            'rf_r': total_r,
            'current_majority': 'D' if current_d > current_r else 'R',
            'rf_majority': majority_party,
            'majority_changes': (current_d > current_r) != (total_d > total_r),
            'representation_ratio': {
                'current': 100 / 330,  # ~0.30 senators per million
                'rf': total_senators / 330,  # senators per million population
            },
        }

        return SenateAnalysis(
            year=year,
            total_senators=total_senators,
            regional_results=results,
            party_balance=party_balance,
            dc_senators=dc_senators,
            majority_party=majority_party,
            comparison_to_current=comparison,
        )

    def generate_report(self, year: int) -> str:
        """
        Generate markdown report for Senate composition analysis.

        Args:
            year: Election year

        Returns:
            Markdown-formatted report
        """
        analysis = self.analyze_composition(year)
        comp = analysis.comparison_to_current

        lines = [
            f"# Senate Composition Analysis ({year})",
            "",
            "## Overview",
            "",
            "This analysis models Senate composition under Regional Federalism:",
            "- **7 regions × 2 senators = 14 regional senators**",
            "- **DC representation: 2 senators**",
            "- **Total: 16 senators** (vs. 100 in current system)",
            "",
            "## Senate Balance",
            "",
            "| Metric | Current (100) | RF (16) |",
            "|--------|---------------|---------|",
            f"| Democratic | {comp['current_d']} | {analysis.party_balance['D']} |",
            f"| Republican | {comp['current_r']} | {analysis.party_balance['R']} |",
            f"| Majority | {comp['current_majority']} | {analysis.majority_party} |",
            "",
        ]

        if comp['majority_changes']:
            lines.append("**Note:** Majority control would differ under RF.")
        else:
            lines.append("**Note:** Majority control would be the same under RF.")

        lines.extend([
            "",
            "## Regional Results",
            "",
            "| Region | Population | D Votes | R Votes | Margin | Control | D | R |",
            "|--------|------------|---------|---------|--------|---------|---|---|",
        ])

        for r in sorted(analysis.regional_results, key=lambda x: x.population, reverse=True):
            margin_str = f"{r.vote_margin:+.1%}"
            lines.append(
                f"| {r.region} | {r.population/1000:.1f}M | "
                f"{r.dem_votes:,} | {r.rep_votes:,} | {margin_str} | "
                f"{r.party_control} | {r.dem_senators} | {r.rep_senators} |"
            )

        # Add DC row
        lines.append(
            f"| DC | 0.7M | - | - | +86.8% | D | "
            f"{analysis.dc_senators['D']} | {analysis.dc_senators['R']} |"
        )

        lines.extend([
            "",
            "## Comparison to Current Senate",
            "",
            "### Structural Differences",
            "",
            "| Aspect | Current | Regional Federalism |",
            "|--------|---------|---------------------|",
            "| Total senators | 100 | 16 |",
            "| Selection basis | State | Region |",
            "| Smallest unit | Wyoming (580K) | Mountain (3M) |",
            "| Largest unit | California (39M) | Southeast (78M) |",
            "| DC representation | None | 2 senators |",
            "",
            "### Population Representation",
            "",
            f"- **Current:** {comp['representation_ratio']['current']:.3f} senators per million people",
            f"- **RF:** {comp['representation_ratio']['rf']:.3f} senators per million people",
            "",
            "The RF Senate is more compact but still over-represents smaller regions.",
            "",
            "### Regional vs State Results",
            "",
        ])

        # Compare current state-based to RF regional
        current_by_region = self.get_current_senate_by_region()

        lines.extend([
            "| Region | Current D | Current R | RF D | RF R | Change |",
            "|--------|-----------|-----------|------|------|--------|",
        ])

        for r in analysis.regional_results:
            curr = current_by_region.get(r.region, {'D': 0, 'R': 0})
            d_change = r.dem_senators - curr['D']
            r_change = r.rep_senators - curr['R']

            if d_change > 0:
                change_str = f"D +{d_change}"
            elif r_change > 0:
                change_str = f"R +{r_change}"
            else:
                change_str = "Same"

            lines.append(
                f"| {r.region} | {curr['D']} | {curr['R']} | "
                f"{r.dem_senators} | {r.rep_senators} | {change_str} |"
            )

        lines.extend([
            "",
            "## Key Findings",
            "",
            f"1. **Size reduction:** The RF Senate has {analysis.total_senators} seats "
            f"vs. 100 currently ({analysis.total_senators/100:.0%} of current size).",
            "",
            f"2. **Party balance:** Under RF, Democrats would hold "
            f"{analysis.party_balance['D']}/{analysis.total_senators} seats "
            f"({analysis.party_balance['D']/analysis.total_senators:.0%}).",
            "",
            "3. **Winner-take-all effect:** Regional elections magnify margins - "
            "the party winning a region gets both senators.",
            "",
            "4. **DC representation:** DC gains 2 senators, adding reliable "
            "Democratic seats.",
            "",
            "## Senate Powers Under RF",
            "",
            "The RF Senate has limited powers compared to the current Senate:",
            "",
            "- Treaty ratification",
            "- Confirmation of judicial/constitutional officers",
            "- Constitutional amendments",
            "- Intergovernmental dispute adjudication",
            "",
            "**Not included:** Routine federal legislation (House only), "
            "budget/appropriations, most confirmations.",
        ])

        return "\n".join(lines)


def run_senate_analysis():
    """Run Senate composition analysis and print report."""
    simulator = SenateSimulator()
    for year in [2016, 2020]:
        report = simulator.generate_report(year)
        print(report)
        print("\n" + "=" * 80 + "\n")


if __name__ == '__main__':
    run_senate_analysis()
