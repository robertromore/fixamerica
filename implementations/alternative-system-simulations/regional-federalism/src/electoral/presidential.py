"""
Presidential election simulation under Regional Federalism.

This module compares Electoral College outcomes with National Popular Vote,
and analyzes how Regional Federalism's electoral system would affect results.

Key RF provisions (from the Constitution):
- Direct national popular vote with majority requirement
- If no majority: Ranked Choice Voting instant runoff
- No swing states; every vote counts equally
"""

from dataclasses import dataclass, field
from typing import Dict, List, Optional, Tuple
from enum import Enum

from ..regions import RegionConfig, load_regions
from ..data_pipeline import ElectoralDataLoader


class ElectionSystem(Enum):
    """Election system types."""
    ELECTORAL_COLLEGE = "Electoral College"
    NATIONAL_POPULAR_VOTE = "National Popular Vote"
    REGIONAL_FEDERALISM = "Regional Federalism (NPV + RCV)"


@dataclass
class CandidateResult:
    """Results for a single candidate."""
    party: str
    name: str
    popular_votes: int
    popular_percent: float
    electoral_votes: int
    regions_won: List[str] = field(default_factory=list)


@dataclass
class ElectionAnalysis:
    """Complete analysis of an election under different systems."""
    year: int
    total_votes: int
    candidates: List[CandidateResult]

    # Electoral College outcome
    ec_winner: str
    ec_margin: int

    # National Popular Vote outcome
    npv_winner: str
    npv_margin: int
    npv_margin_percent: float
    npv_has_majority: bool

    # Regional Federalism outcome (NPV + RCV if no majority)
    rf_winner: str
    rf_required_rcv: bool
    rf_rcv_note: str  # Explanation of RCV outcome

    # Regional analysis
    regional_results: Dict[str, Dict]
    regions_won: Dict[str, int]  # party -> count

    # Key insights
    outcome_differs: bool
    swing_state_effect: Dict[str, float]


class PresidentialSimulator:
    """
    Simulates presidential elections under different systems.

    Compares Electoral College (current system) with National Popular Vote
    (Regional Federalism's proposed system).
    """

    # Historical election data: {year: {candidate name: party}}
    # Only include years with data in ElectoralDataLoader
    CANDIDATES = {
        2016: {'Clinton': 'D', 'Trump': 'R'},
        2020: {'Biden': 'D', 'Trump': 'R'},
    }

    # Electoral votes needed to win
    ELECTORAL_VOTES_TO_WIN = 270

    def __init__(self, regions: Optional[RegionConfig] = None):
        """Initialize with optional region configuration."""
        self.regions = regions or load_regions()
        self.data = ElectoralDataLoader(self.regions)

    def analyze_election(self, year: int) -> ElectionAnalysis:
        """
        Perform complete election analysis for a given year.

        Args:
            year: Election year (2016 or 2020)

        Returns:
            ElectionAnalysis with results under different systems
        """
        # Get raw data
        national = self.data.get_national_totals(year)
        regional = self.data.aggregate_by_region(year)

        # Build candidate results
        candidates = self._build_candidate_results(year, national, regional)

        # Determine Electoral College outcome
        dem_ev = sum(1 for c in candidates if c.party == 'D' for _ in range(c.electoral_votes))
        rep_ev = sum(c.electoral_votes for c in candidates if c.party == 'R')

        # Actually calculate from regional data
        dem_ev, rep_ev = self._calculate_electoral_votes(year)
        ec_winner = 'D' if dem_ev >= self.ELECTORAL_VOTES_TO_WIN else 'R'
        ec_margin = abs(dem_ev - rep_ev)

        # Determine NPV outcome
        npv_winner = 'D' if national['dem'] > national['rep'] else 'R'
        npv_margin = abs(national['dem'] - national['rep'])
        npv_margin_percent = 100 * npv_margin / national['total']
        npv_has_majority = (max(national['dem'], national['rep']) / national['total']) > 0.5

        # Determine Regional Federalism outcome (NPV + RCV if no majority)
        rf_winner, rf_required_rcv, rf_rcv_note = self._simulate_rf_election(national, npv_has_majority)

        # Regional analysis
        regions_won = {'D': 0, 'R': 0}
        for region, data in regional.items():
            winner = 'D' if data['dem'] > data['rep'] else 'R'
            regions_won[winner] += 1

        # Calculate swing state effect
        swing_effect = self._analyze_swing_states(year)

        return ElectionAnalysis(
            year=year,
            total_votes=national['total'],
            candidates=candidates,
            ec_winner=ec_winner,
            ec_margin=ec_margin,
            npv_winner=npv_winner,
            npv_margin=npv_margin,
            npv_margin_percent=npv_margin_percent,
            npv_has_majority=npv_has_majority,
            rf_winner=rf_winner,
            rf_required_rcv=rf_required_rcv,
            rf_rcv_note=rf_rcv_note,
            regional_results=regional,
            regions_won=regions_won,
            outcome_differs=(ec_winner != rf_winner),
            swing_state_effect=swing_effect
        )

    def _build_candidate_results(
        self, year: int, national: Dict, regional: Dict
    ) -> List[CandidateResult]:
        """Build candidate result objects."""
        candidates = []

        # Get candidate names
        cand_names = self.CANDIDATES.get(year, {'Democrat': 'D', 'Republican': 'R'})
        dem_name = [k for k, v in cand_names.items() if v == 'D'][0]
        rep_name = [k for k, v in cand_names.items() if v == 'R'][0]

        # Calculate electoral votes
        dem_ev, rep_ev = self._calculate_electoral_votes(year)

        # Regions won
        dem_regions = []
        rep_regions = []
        for region, data in regional.items():
            if data['dem'] > data['rep']:
                dem_regions.append(region)
            else:
                rep_regions.append(region)

        candidates.append(CandidateResult(
            party='D',
            name=dem_name,
            popular_votes=national['dem'],
            popular_percent=100 * national['dem'] / national['total'],
            electoral_votes=dem_ev,
            regions_won=dem_regions
        ))

        candidates.append(CandidateResult(
            party='R',
            name=rep_name,
            popular_votes=national['rep'],
            popular_percent=100 * national['rep'] / national['total'],
            electoral_votes=rep_ev,
            regions_won=rep_regions
        ))

        return candidates

    def _simulate_rf_election(
        self, national: Dict, has_majority: bool
    ) -> Tuple[str, bool, str]:
        """
        Simulate Regional Federalism election outcome.

        Under RF, the winner is determined by national popular vote with a
        majority requirement. If no candidate achieves >50%, RCV runoff occurs.

        Args:
            national: National vote totals
            has_majority: Whether leading candidate has >50%

        Returns:
            Tuple of (winner party, required_rcv, explanation note)
        """
        dem_pct = national['dem'] / national['total']
        rep_pct = national['rep'] / national['total']
        other_pct = national['other'] / national['total']

        if has_majority:
            # Clear majority - winner determined by first-round NPV
            winner = 'D' if dem_pct > rep_pct else 'R'
            return (winner, False, f"First-round majority ({max(dem_pct, rep_pct):.1%})")

        # No majority - RCV runoff simulation
        # In RCV, third-party votes are redistributed. We estimate redistribution
        # based on typical patterns: ~60% to D, ~30% to R, ~10% exhaust
        # These ratios are approximations; actual RCV would depend on ballot data
        other_votes = national['other']
        dem_rcv_share = 0.60  # Estimated third-party redistribution to D
        rep_rcv_share = 0.30  # Estimated third-party redistribution to R
        # Remaining 10% assumed to exhaust (no second choice)

        dem_final = national['dem'] + (other_votes * dem_rcv_share)
        rep_final = national['rep'] + (other_votes * rep_rcv_share)

        winner = 'D' if dem_final > rep_final else 'R'
        winner_final_pct = max(dem_final, rep_final) / (dem_final + rep_final)

        note = (
            f"RCV runoff required (no first-round majority). "
            f"Third-party votes ({other_pct:.1%}) redistributed. "
            f"Final: {winner_final_pct:.1%} after redistribution."
        )

        return (winner, True, note)

    def _calculate_electoral_votes(self, year: int) -> Tuple[int, int]:
        """
        Calculate electoral votes won by each party.

        Note: This uses winner-take-all for all states. ME and NE actually split
        EVs by congressional district, but district-level data is not available
        in this dataset. Results may differ slightly from official totals.
        """
        data = self.data.get_election_data(year)

        dem_ev = 0
        rep_ev = 0

        for state, votes in data.items():
            if votes['dem'] > votes['rep']:
                dem_ev += votes['ev']
            else:
                rep_ev += votes['ev']

        return dem_ev, rep_ev

    def _analyze_swing_states(self, year: int) -> Dict[str, float]:
        """
        Analyze the effect of swing states on the outcome.

        Returns dict with:
        - decisive_states: states that determined the outcome
        - margin_in_decisive: combined margin in decisive states
        - votes_vs_outcome: how many votes separated winner from loser
        """
        data = self.data.get_election_data(year)

        # Sort states by margin
        state_margins = []
        for state, votes in data.items():
            total = votes['dem'] + votes['rep'] + votes['other']
            margin = abs(votes['dem'] - votes['rep'])
            margin_pct = 100 * margin / total
            winner = 'D' if votes['dem'] > votes['rep'] else 'R'
            state_margins.append({
                'state': state,
                'margin': margin,
                'margin_pct': margin_pct,
                'winner': winner,
                'ev': votes['ev']
            })

        state_margins.sort(key=lambda x: x['margin_pct'])

        # Find the tipping point state
        dem_ev, rep_ev = self._calculate_electoral_votes(year)
        ec_winner = 'D' if dem_ev >= self.ELECTORAL_VOTES_TO_WIN else 'R'

        # Calculate votes needed to flip the outcome
        if ec_winner == 'D':
            ev_to_flip = dem_ev - 269  # Need to get below 270
            loser_states = [s for s in state_margins if s['winner'] == 'D']
        else:
            ev_to_flip = rep_ev - 269
            loser_states = [s for s in state_margins if s['winner'] == 'R']

        loser_states.sort(key=lambda x: x['margin_pct'])

        # Find minimum states to flip
        flipped_ev = 0
        votes_to_flip = 0
        decisive_states = []

        for state in loser_states:
            if flipped_ev >= ev_to_flip:
                break
            flipped_ev += state['ev']
            votes_to_flip += state['margin'] // 2 + 1  # Votes needed to flip
            decisive_states.append(state['state'])

        return {
            'tipping_point_votes': votes_to_flip,
            'decisive_state_count': len(decisive_states),
            'decisive_states': decisive_states[:5],  # Top 5
            'closest_state_margin_pct': state_margins[0]['margin_pct'],
            'closest_state': state_margins[0]['state'],
        }

    def compare_systems(self, year: int) -> str:
        """
        Generate a comparison report between electoral systems.

        Args:
            year: Election year

        Returns:
            Markdown-formatted report
        """
        analysis = self.analyze_election(year)

        lines = [
            f"# {year} Presidential Election: Electoral System Comparison",
            "",
            "## Summary",
            "",
            f"**Total votes cast:** {analysis.total_votes:,}",
            "",
            "### Candidates",
            ""
        ]

        for c in analysis.candidates:
            lines.append(
                f"- **{c.name}** ({c.party}): {c.popular_votes:,} votes "
                f"({c.popular_percent:.1f}%), {c.electoral_votes} EV"
            )

        # Margin label depends on whether RCV was needed
        margin_label = "First-round margin" if analysis.rf_required_rcv else "Popular vote margin"

        lines.extend([
            "",
            "## Electoral College (Current System)",
            "",
            f"**Winner:** {analysis.ec_winner}",
            f"**Electoral vote margin:** {analysis.ec_margin}",
            "",
            "## Regional Federalism System (NPV + RCV)",
            "",
            f"**Winner:** {analysis.rf_winner}",
            f"**{margin_label}:** {analysis.npv_margin:,} ({analysis.npv_margin_percent:.2f}%)",
            f"**Has majority (>50%):** {'Yes' if analysis.npv_has_majority else 'No'}",
            f"**RCV Required:** {'Yes' if analysis.rf_required_rcv else 'No'}",
            "",
            f"*{analysis.rf_rcv_note}*",
            "",
        ])

        # Outcome comparison
        if analysis.outcome_differs:
            # Determine the specific reason for the difference
            if analysis.npv_winner != analysis.ec_winner:
                reason = "the Electoral College winner **lost** the first-round popular vote"
            elif analysis.rf_required_rcv and analysis.rf_winner != analysis.npv_winner:
                reason = "RCV redistribution **changed** the winner from the first-round plurality leader"
            else:
                reason = "the systems produced different results"

            lines.extend([
                "## ⚠️ OUTCOME DIFFERS",
                "",
                f"Under the Electoral College, {reason}.",
                "",
                "Under Regional Federalism's system (NPV with RCV if no majority), "
                f"**{analysis.rf_winner}** would have won instead of **{analysis.ec_winner}**.",
                "",
            ])
        else:
            lines.extend([
                "## Outcome Match",
                "",
                "Both systems would have produced the same winner.",
                "",
            ])

        # Regional breakdown
        lines.extend([
            "## Regional Analysis",
            "",
            "| Region | D Votes | R Votes | Winner | Margin |",
            "|--------|---------|---------|--------|--------|",
        ])

        for region, data in sorted(analysis.regional_results.items()):
            winner = 'D' if data['dem'] > data['rep'] else 'R'
            margin = abs(data['dem'] - data['rep'])
            margin_pct = 100 * margin / data['total']
            lines.append(
                f"| {region} | {data['dem']:,} | {data['rep']:,} | "
                f"{winner} | {margin_pct:.1f}% |"
            )

        lines.extend([
            "",
            f"**Regions won:** D: {analysis.regions_won['D']}, R: {analysis.regions_won['R']}",
            "",
        ])

        # Swing state analysis
        swing = analysis.swing_state_effect
        lines.extend([
            "## Swing State Analysis",
            "",
            f"**Closest state:** {swing['closest_state']} "
            f"(margin: {swing['closest_state_margin_pct']:.2f}%)",
            "",
            f"**Votes to flip outcome:** ~{swing['tipping_point_votes']:,}",
            "",
            f"**Decisive states (closest to tipping point):** "
            f"{', '.join(swing['decisive_states'])}",
            "",
            "### Key Insight",
            "",
            "Under the Electoral College, the election outcome depends on a small "
            f"number of swing states. In {year}, approximately "
            f"**{swing['tipping_point_votes']:,} votes** in the decisive states "
            "could have changed the outcome.",
            "",
            "Under Regional Federalism, every vote counts equally regardless of "
            "state, eliminating the swing state phenomenon.",
        ])

        return "\n".join(lines)

    def generate_multi_year_report(self, years: List[int]) -> str:
        """
        Generate a report comparing multiple elections.

        Args:
            years: List of election years

        Returns:
            Markdown-formatted report
        """
        analyses = [self.analyze_election(year) for year in years]

        lines = [
            "# Presidential Elections: Electoral College vs Regional Federalism",
            "",
            "## Overview",
            "",
            "This analysis compares outcomes under the current Electoral College "
            "system with outcomes under Regional Federalism (NPV with RCV if no majority).",
            "",
            "## Summary Table",
            "",
            "| Year | EC Winner | RF Winner | Different? | RCV Required | First-Round Margin (%) |",
            "|------|-----------|-----------|------------|--------------|-------------------|",
        ]

        for a in analyses:
            lines.append(
                f"| {a.year} | {a.ec_winner} | {a.rf_winner} | "
                f"{'**YES**' if a.outcome_differs else 'No'} | "
                f"{'Yes' if a.rf_required_rcv else 'No'} | "
                f"{a.npv_margin_percent:.2f}% |"
            )

        # Count outcomes that differed
        differed = sum(1 for a in analyses if a.outcome_differs)

        lines.extend([
            "",
            f"**Elections where outcome differed:** {differed}/{len(analyses)}",
            "",
            "## Key Findings",
            "",
        ])

        if differed > 0:
            diff_years = [a.year for a in analyses if a.outcome_differs]
            lines.append(
                f"In {', '.join(str(y) for y in diff_years)}, the Electoral College "
                "produced a different winner than Regional Federalism's system. "
                "Under RF, the winner is determined by national popular vote "
                "(with RCV runoff if no candidate achieves a majority)."
            )
        else:
            lines.append(
                "In all analyzed elections, both systems would have produced the same "
                "winner. However, the margin dynamics and campaigning incentives would "
                "differ significantly."
            )

        lines.extend([
            "",
            "## Regional Federalism Impact",
            "",
            "Under Regional Federalism's electoral system:",
            "",
            "1. **Every vote counts equally** - No more 'safe state' vs 'swing state' dichotomy",
            "2. **Majority requirement** - If no candidate achieves >50%, RCV runoff triggers",
            "3. **Campaign everywhere** - Candidates must appeal to voters nationwide",
            "4. **Reduced polarization potential** - Less incentive to maximize turnout only in swing states",
            "",
        ])

        return "\n".join(lines)


def run_analysis():
    """Run presidential election analysis."""
    simulator = PresidentialSimulator()

    print("Analyzing 2016 and 2020 presidential elections...")
    print()

    # Generate individual year reports
    for year in [2016, 2020]:
        report = simulator.compare_systems(year)
        print(report)
        print("\n" + "=" * 70 + "\n")

    # Generate multi-year comparison
    multi_report = simulator.generate_multi_year_report([2016, 2020])
    print(multi_report)


if __name__ == '__main__':
    run_analysis()
