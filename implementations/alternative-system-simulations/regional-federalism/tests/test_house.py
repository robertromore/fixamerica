"""Tests for House proportional representation simulation module."""

import pytest
from src.electoral.house import HouseSimulator, HouseAnalysis


class TestHouseSimulator:
    """Tests for HouseSimulator class."""

    @pytest.fixture
    def simulator(self):
        return HouseSimulator()

    def test_analyze_2016(self, simulator):
        """2016 analysis completes without errors."""
        analysis = simulator.analyze_house(2016)
        assert analysis.year == 2016
        assert analysis.total_seats > 0

    def test_analyze_2020(self, simulator):
        """2020 analysis completes without errors."""
        analysis = simulator.analyze_house(2020)
        assert analysis.year == 2020
        assert analysis.total_seats > 0

    def test_analyze_2024(self, simulator):
        """2024 analysis completes without errors."""
        analysis = simulator.analyze_house(2024)
        assert analysis.year == 2024
        assert analysis.total_seats > 0

    def test_total_seats_equals_435(self, simulator):
        """Total seats equals 435 (constitutional requirement)."""
        analysis = simulator.analyze_house(2020)
        assert analysis.total_seats == 435

    def test_all_regions_represented(self, simulator):
        """All 7 regions are represented in results."""
        analysis = simulator.analyze_house(2020)
        assert len(analysis.results_by_region) == 7

    def test_seats_sum_to_total(self, simulator):
        """Sum of regional seats equals total."""
        analysis = simulator.analyze_house(2020)
        regional_sum = sum(r.seats_allocated for r in analysis.results_by_region)
        assert regional_sum == analysis.total_seats

    def test_party_seats_sum_to_region_total(self, simulator):
        """Party seat allocations sum to region total."""
        analysis = simulator.analyze_house(2020)
        for result in analysis.results_by_region:
            party_sum = sum(result.party_seats.values())
            assert party_sum == result.seats_allocated

    def test_gallagher_index_range(self, simulator):
        """Gallagher index is in valid range (0-100)."""
        analysis = simulator.analyze_house(2020)
        assert 0 <= analysis.national_gallagher_index <= 100

    def test_gallagher_index_lower_than_current(self, simulator):
        """RF Gallagher index should be lower than current system."""
        analysis = simulator.analyze_house(2020)
        # PR systems typically have Gallagher < 5
        # Current US system is typically 10-15
        assert analysis.national_gallagher_index < 10

    def test_current_comparison_populated(self, simulator):
        """Comparison to current system is populated."""
        analysis = simulator.analyze_house(2020)
        assert 'current_total' in analysis.comparison_to_current
        assert 'rf_total' in analysis.comparison_to_current
        assert analysis.comparison_to_current['current_total'] == 435

    def test_threshold_default(self, simulator):
        """Default threshold is 3%."""
        analysis = simulator.analyze_house(2020)
        assert analysis.threshold_pct == 3.0  # Stored as percentage (3.0%)


class TestDHondtAlgorithm:
    """Tests for D'Hondt seat allocation algorithm."""

    @pytest.fixture
    def simulator(self):
        return HouseSimulator()

    def test_dhondt_simple_case(self, simulator):
        """D'Hondt allocates correctly in simple case."""
        votes = {'A': 100, 'B': 80, 'C': 30}
        seats = 8
        allocation = simulator.allocate_seats_dhondt(votes, seats, threshold=0.0)

        # With 210 total votes:
        # A (100): quotients 100, 50, 33.3, 25, 20...
        # B (80): quotients 80, 40, 26.7, 20...
        # C (30): quotients 30, 15...
        # Top 8: 100, 80, 50, 40, 33.3, 30, 26.7, 25
        # A=4, B=3, C=1
        assert allocation['A'] == 4
        assert allocation['B'] == 3
        assert allocation['C'] == 1

    def test_dhondt_respects_threshold(self, simulator):
        """D'Hondt filters parties below threshold."""
        votes = {'A': 100, 'B': 80, 'C': 5}  # C is < 3% of 185
        seats = 8
        allocation = simulator.allocate_seats_dhondt(votes, seats, threshold=0.03)

        # C should be filtered out
        assert allocation['C'] == 0
        # A and B should get all seats
        assert allocation['A'] + allocation['B'] == 8

    def test_dhondt_all_seats_allocated(self, simulator):
        """All seats are allocated."""
        votes = {'A': 100, 'B': 80, 'C': 30}
        seats = 10
        allocation = simulator.allocate_seats_dhondt(votes, seats, threshold=0.0)

        assert sum(allocation.values()) == seats

    def test_dhondt_single_party(self, simulator):
        """Single party above threshold gets all seats."""
        votes = {'A': 100, 'B': 1}  # B is < 3%
        seats = 5
        allocation = simulator.allocate_seats_dhondt(votes, seats, threshold=0.03)

        assert allocation['A'] == 5
        assert allocation['B'] == 0


class TestSeatApportionment:
    """Tests for Huntington-Hill seat apportionment."""

    @pytest.fixture
    def simulator(self):
        return HouseSimulator()

    def test_apportion_seats_total(self, simulator):
        """Apportionment totals to requested seats."""
        populations = {
            'R1': 100000,
            'R2': 50000,
            'R3': 30000,
        }
        apportionment = simulator.apportion_seats_by_population(populations, 10)
        assert sum(apportionment.values()) == 10

    def test_apportion_proportional(self, simulator):
        """Larger regions get more seats."""
        populations = {
            'Large': 100000,
            'Medium': 50000,
            'Small': 10000,
        }
        apportionment = simulator.apportion_seats_by_population(populations, 20)

        assert apportionment['Large'] > apportionment['Medium']
        assert apportionment['Medium'] > apportionment['Small']

    def test_apportion_minimum_one_seat(self, simulator):
        """Each region gets at least one seat."""
        populations = {
            'Large': 1000000,
            'Tiny': 1000,
        }
        apportionment = simulator.apportion_seats_by_population(populations, 10)

        assert apportionment['Tiny'] >= 1


class TestHouseReport:
    """Tests for House report generation."""

    @pytest.fixture
    def simulator(self):
        return HouseSimulator()

    def test_report_generation(self, simulator):
        """Report generates without errors."""
        report = simulator.generate_report(2020)
        assert len(report) > 0

    def test_report_has_title(self, simulator):
        """Report has title."""
        report = simulator.generate_report(2020)
        assert '# House Seat Allocation' in report

    def test_report_has_methodology(self, simulator):
        """Report includes methodology section."""
        report = simulator.generate_report(2020)
        assert 'Methodology' in report or "D'Hondt" in report

    def test_report_has_gallagher(self, simulator):
        """Report includes Gallagher index."""
        report = simulator.generate_report(2020)
        assert 'Gallagher' in report

    def test_report_has_regional_breakdown(self, simulator):
        """Report includes regional breakdown."""
        report = simulator.generate_report(2020)
        assert 'Region' in report
        assert 'Seats' in report


class TestCurrentHouseComparison:
    """Tests for comparison to current House."""

    @pytest.fixture
    def simulator(self):
        return HouseSimulator()

    def test_current_house_totals(self, simulator):
        """Current House has 435 seats."""
        current = simulator.get_current_house_by_region()
        total_d = sum(v['D'] for v in current.values())
        total_r = sum(v['R'] for v in current.values())
        # Note: totals may not be exactly 435 due to vacancies
        assert 400 < total_d + total_r <= 435

    def test_current_house_all_regions(self, simulator):
        """Current House covers all regions."""
        current = simulator.get_current_house_by_region()
        assert len(current) == 7

    def test_comparison_structure(self, simulator):
        """Comparison includes expected fields."""
        analysis = simulator.analyze_house(2020)
        comp = analysis.comparison_to_current

        assert 'current_total' in comp
        assert 'rf_total' in comp
        assert 'current_gallagher' in comp
        assert 'rf_gallagher' in comp
