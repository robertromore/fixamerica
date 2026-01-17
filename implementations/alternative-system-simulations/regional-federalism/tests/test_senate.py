"""Tests for Senate composition simulation module."""

import pytest
from src.electoral.senate import SenateSimulator, SenateAnalysis


class TestSenateSimulator:
    """Tests for SenateSimulator class."""

    @pytest.fixture
    def simulator(self):
        return SenateSimulator()

    def test_analyze_2016(self, simulator):
        """2016 analysis completes without errors."""
        analysis = simulator.analyze_composition(2016)
        assert analysis.year == 2016
        assert analysis.total_senators > 0

    def test_analyze_2020(self, simulator):
        """2020 analysis completes without errors."""
        analysis = simulator.analyze_composition(2020)
        assert analysis.year == 2020
        assert analysis.total_senators > 0

    def test_analyze_2024(self, simulator):
        """2024 analysis completes without errors."""
        analysis = simulator.analyze_composition(2024)
        assert analysis.year == 2024
        assert analysis.total_senators > 0

    def test_total_senators_equals_16(self, simulator):
        """Total senators equals 16 (14 regional + 2 DC)."""
        analysis = simulator.analyze_composition(2020)
        # 7 regions × 2 senators + 2 DC senators = 16
        assert analysis.total_senators == 16

    def test_all_regions_represented(self, simulator):
        """All 7 regions are represented in results."""
        analysis = simulator.analyze_composition(2020)
        assert len(analysis.regional_results) == 7

    def test_each_region_has_two_senators(self, simulator):
        """Each region has exactly 2 senators."""
        analysis = simulator.analyze_composition(2020)
        for result in analysis.regional_results:
            assert result.senators == 2

    def test_dc_has_two_senators(self, simulator):
        """DC has 2 senators under RF."""
        analysis = simulator.analyze_composition(2020)
        dc_total = analysis.dc_senators['D'] + analysis.dc_senators['R']
        assert dc_total == 2

    def test_dc_is_democratic(self, simulator):
        """DC senators are Democratic (based on voting patterns)."""
        analysis = simulator.analyze_composition(2020)
        assert analysis.dc_senators['D'] == 2
        assert analysis.dc_senators['R'] == 0

    def test_party_balance_sums_to_total(self, simulator):
        """Party balance sums to total senators."""
        analysis = simulator.analyze_composition(2020)
        total = analysis.party_balance['D'] + analysis.party_balance['R']
        assert total == analysis.total_senators

    def test_majority_party_determined(self, simulator):
        """Majority party is determined."""
        analysis = simulator.analyze_composition(2020)
        assert analysis.majority_party in ('D', 'R', 'Tie')

    def test_majority_party_is_larger(self, simulator):
        """Majority party has more senators (unless tie)."""
        analysis = simulator.analyze_composition(2020)
        if analysis.majority_party == 'D':
            assert analysis.party_balance['D'] > analysis.party_balance['R']
        elif analysis.majority_party == 'R':
            assert analysis.party_balance['R'] > analysis.party_balance['D']
        else:
            assert analysis.party_balance['D'] == analysis.party_balance['R']


class TestRegionalResults:
    """Tests for regional Senate results."""

    @pytest.fixture
    def simulator(self):
        return SenateSimulator()

    def test_region_vote_data(self, simulator):
        """Regional results include vote data."""
        analysis = simulator.analyze_composition(2020)
        for result in analysis.regional_results:
            assert result.dem_votes >= 0
            assert result.rep_votes >= 0
            assert result.population > 0

    def test_party_control_valid(self, simulator):
        """Party control is D, R, or Split."""
        analysis = simulator.analyze_composition(2020)
        for result in analysis.regional_results:
            assert result.party_control in ('D', 'R', 'Split')

    def test_winner_take_all(self, simulator):
        """Winner-take-all: majority party gets both senators."""
        analysis = simulator.analyze_composition(2020)
        for result in analysis.regional_results:
            if result.party_control == 'D':
                assert result.dem_senators == 2
                assert result.rep_senators == 0
            elif result.party_control == 'R':
                assert result.dem_senators == 0
                assert result.rep_senators == 2
            else:  # Split
                assert result.dem_senators == 1
                assert result.rep_senators == 1

    def test_vote_margin_sign(self, simulator):
        """Vote margin sign matches party control."""
        analysis = simulator.analyze_composition(2020)
        for result in analysis.regional_results:
            if result.party_control == 'D':
                assert result.vote_margin > 0  # Positive = D lead
            elif result.party_control == 'R':
                assert result.vote_margin < 0  # Negative = R lead


class TestCurrentSenateComparison:
    """Tests for comparison to current Senate."""

    @pytest.fixture
    def simulator(self):
        return SenateSimulator()

    def test_current_senate_by_region(self, simulator):
        """Current Senate aggregates to regions."""
        current = simulator.get_current_senate_by_region()
        assert len(current) == 7

        for region, data in current.items():
            assert 'D' in data
            assert 'R' in data
            assert 'total' in data

    def test_current_senate_total_is_100(self, simulator):
        """Current Senate total is approximately 100."""
        current = simulator.get_current_senate_by_region()
        total_d = sum(r['D'] for r in current.values())
        total_r = sum(r['R'] for r in current.values())
        # DC currently has 0 senators
        assert total_d + total_r == 100

    def test_comparison_populated(self, simulator):
        """Comparison to current includes expected fields."""
        analysis = simulator.analyze_composition(2020)
        comp = analysis.comparison_to_current

        assert 'current_total' in comp
        assert 'rf_total' in comp
        assert 'current_d' in comp
        assert 'current_r' in comp
        assert 'rf_d' in comp
        assert 'rf_r' in comp
        assert 'majority_changes' in comp

    def test_size_comparison(self, simulator):
        """Current has 100 seats, RF has 16."""
        analysis = simulator.analyze_composition(2020)
        comp = analysis.comparison_to_current

        assert comp['current_total'] == 100
        assert comp['rf_total'] == 16


class TestSenateReport:
    """Tests for Senate report generation."""

    @pytest.fixture
    def simulator(self):
        return SenateSimulator()

    def test_report_generation(self, simulator):
        """Report generates without errors."""
        report = simulator.generate_report(2020)
        assert len(report) > 0

    def test_report_has_title(self, simulator):
        """Report has title."""
        report = simulator.generate_report(2020)
        assert '# Senate Composition' in report

    def test_report_has_balance(self, simulator):
        """Report includes party balance."""
        report = simulator.generate_report(2020)
        assert 'Balance' in report or 'balance' in report
        assert 'Democratic' in report
        assert 'Republican' in report

    def test_report_has_regional_breakdown(self, simulator):
        """Report includes regional breakdown."""
        report = simulator.generate_report(2020)
        assert 'Region' in report
        assert 'Control' in report

    def test_report_has_comparison(self, simulator):
        """Report includes comparison to current."""
        report = simulator.generate_report(2020)
        assert 'Current' in report or 'current' in report
        assert '100' in report  # Current Senate size

    def test_report_has_dc(self, simulator):
        """Report mentions DC representation."""
        report = simulator.generate_report(2020)
        assert 'DC' in report

    def test_report_has_powers(self, simulator):
        """Report mentions RF Senate powers."""
        report = simulator.generate_report(2020)
        assert 'Powers' in report or 'powers' in report


class TestSenateDataIntegrity:
    """Tests for data integrity in Senate simulation."""

    @pytest.fixture
    def simulator(self):
        return SenateSimulator()

    def test_all_states_assigned(self, simulator):
        """All 50 states + DC are in current Senate data."""
        all_states = set(simulator.CURRENT_SENATE_BY_STATE.keys())
        assert len(all_states) == 51  # 50 states + DC

    def test_current_senate_seats_valid(self, simulator):
        """Current Senate seat allocations are valid (0, 1, or 2)."""
        for state, (d, r) in simulator.CURRENT_SENATE_BY_STATE.items():
            assert d + r == 2 or state == 'DC'  # DC has 0 currently
            assert d >= 0 and d <= 2
            assert r >= 0 and r <= 2

    def test_regional_votes_consistent(self, simulator):
        """Regional vote totals are consistent across analyses."""
        analysis_2020 = simulator.analyze_composition(2020)
        analysis_2016 = simulator.analyze_composition(2016)

        # Same number of regions
        assert len(analysis_2020.regional_results) == len(analysis_2016.regional_results)

        # Same region names
        regions_2020 = {r.region for r in analysis_2020.regional_results}
        regions_2016 = {r.region for r in analysis_2016.regional_results}
        assert regions_2020 == regions_2016
