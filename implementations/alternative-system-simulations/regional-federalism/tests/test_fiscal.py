"""Tests for fiscal simulation modules."""

import pytest
from src.fiscal.capacity import FiscalCapacityCalculator, CapacityComponent
from src.fiscal.equalization import EqualizationCalculator


class TestFiscalCapacityCalculator:
    """Tests for FiscalCapacityCalculator class."""

    @pytest.fixture
    def calculator(self):
        return FiscalCapacityCalculator()

    def test_component_weights_sum_to_one(self):
        """Capacity component weights sum to 1.0."""
        total = sum(c.weight for c in CapacityComponent)
        assert abs(total - 1.0) < 0.001

    def test_calculate_state_capacity(self, calculator):
        """State capacity can be calculated."""
        ca_capacity = calculator.calculate_state_capacity('CA')
        assert ca_capacity > 0

        # California should have highest capacity
        tx_capacity = calculator.calculate_state_capacity('TX')
        assert ca_capacity > tx_capacity

    def test_unknown_state_returns_zero(self, calculator):
        """Unknown state returns zero capacity."""
        capacity = calculator.calculate_state_capacity('XX')
        assert capacity == 0

    def test_calculate_regional_capacity(self, calculator):
        """Regional capacity calculation works."""
        pacific = calculator.calculate_regional_capacity('Pacific')

        assert pacific.region == 'Pacific'
        assert pacific.population > 0
        assert pacific.total_capacity > 0
        assert pacific.per_capita_capacity > 0

    def test_analyze_all_regions(self, calculator):
        """All regions analysis completes."""
        analysis = calculator.analyze_all_regions()

        assert len(analysis.regions) == 7
        assert analysis.national_median_per_capita > 0
        assert analysis.national_average_per_capita > 0

    def test_median_splits_regions(self, calculator):
        """Median divides regions into above and below."""
        analysis = calculator.analyze_all_regions()

        total = len(analysis.above_median_regions) + len(analysis.below_median_regions)
        assert total == 7

    def test_capacity_range(self, calculator):
        """Capacity range is valid."""
        analysis = calculator.analyze_all_regions()

        min_cap, max_cap = analysis.capacity_range
        assert min_cap > 0
        assert max_cap > min_cap

    def test_coefficient_of_variation(self, calculator):
        """CV is calculated and reasonable."""
        analysis = calculator.analyze_all_regions()

        # CV should be positive and less than 1 for reasonable data
        assert 0 < analysis.coefficient_of_variation < 1

    def test_capacity_index_relative_to_median(self, calculator):
        """Capacity index reflects position vs median."""
        analysis = calculator.analyze_all_regions()

        for r in analysis.regions:
            if r.region in analysis.above_median_regions:
                assert r.capacity_index > 1.0
            elif r.region in analysis.below_median_regions:
                assert r.capacity_index <= 1.0

    def test_generate_report(self, calculator):
        """Report generation works."""
        report = calculator.generate_report()

        assert 'Regional Fiscal Capacity Analysis' in report
        assert 'Personal Income' in report
        assert 'Pacific' in report


class TestEqualizationCalculator:
    """Tests for EqualizationCalculator class."""

    @pytest.fixture
    def calculator(self):
        return EqualizationCalculator()

    def test_equalization_rate_tiers(self, calculator):
        """Equalization rates follow graduated structure."""
        assert calculator.get_equalization_rate(0.05) == 0.50  # 5% gap -> 50%
        assert calculator.get_equalization_rate(0.15) == 0.60  # 15% gap -> 60%
        assert calculator.get_equalization_rate(0.25) == 0.70  # 25% gap -> 70%
        assert calculator.get_equalization_rate(0.35) == 0.80  # 35% gap -> 80%

    def test_analyze_equalization(self, calculator):
        """Equalization analysis completes."""
        analysis = calculator.analyze_equalization()

        assert analysis.total_transfers > 0
        assert analysis.total_recipients > 0
        assert analysis.total_donors > 0
        assert analysis.total_recipients + analysis.total_donors == 7

    def test_recipients_below_median(self, calculator):
        """All recipients have capacity below median."""
        analysis = calculator.analyze_equalization()

        for r in analysis.results:
            if r.is_recipient:
                assert r.per_capita_capacity <= r.median_capacity

    def test_donors_above_median(self, calculator):
        """All donors have capacity at or above median."""
        analysis = calculator.results if hasattr(calculator, 'results') else None
        analysis = calculator.analyze_equalization()

        for r in analysis.results:
            if not r.is_recipient:
                assert r.per_capita_capacity >= r.median_capacity

    def test_transfers_positive_for_recipients(self, calculator):
        """Recipients receive positive transfers."""
        analysis = calculator.analyze_equalization()

        for r in analysis.results:
            if r.is_recipient:
                assert r.final_transfer_total > 0
                assert r.final_transfer_per_capita > 0

    def test_donors_zero_transfer(self, calculator):
        """Donors receive zero transfers."""
        analysis = calculator.analyze_equalization()

        for r in analysis.results:
            if not r.is_recipient:
                assert r.final_transfer_total == 0

    def test_net_impact_sums_to_zero(self, calculator):
        """Net fiscal impacts sum to approximately zero."""
        analysis = calculator.analyze_equalization()

        total_impact = sum(analysis.net_fiscal_impact.values())
        # Should sum to near zero (donors fund recipients)
        assert abs(total_impact) < 0.01  # Allow small rounding error

    def test_donor_burden_proportional_to_excess(self, calculator):
        """Donor burden is proportional to excess capacity above median."""
        analysis = calculator.analyze_equalization()

        donors = [r for r in analysis.results if not r.is_recipient]
        if len(donors) >= 2:
            # Higher excess capacity should mean larger burden
            sorted_by_excess = sorted(
                donors,
                key=lambda r: (r.per_capita_capacity - r.median_capacity) * r.population,
                reverse=True
            )
            sorted_by_burden = sorted(
                donors,
                key=lambda r: abs(analysis.net_fiscal_impact[r.region]),
                reverse=True
            )
            # Top donor by excess should also be top by burden
            assert sorted_by_excess[0].region == sorted_by_burden[0].region

    def test_transfer_floor_applied(self, calculator):
        """Transfer floor is applied where needed."""
        analysis = calculator.analyze_equalization()

        for r in analysis.results:
            if r.is_recipient and r.transfer_floor_applied:
                # Floor is ~$47 in 2022 dollars
                assert r.final_transfer_per_capita >= 45

    def test_generate_report(self, calculator):
        """Report generation works."""
        report = calculator.generate_report()

        assert 'Equalization Transfer Analysis' in report
        assert 'Transfer Recipients' in report
        assert 'Net Fiscal Position' in report


class TestDonorShareLogic:
    """Tests for donor burden share calculation logic."""

    @pytest.fixture
    def calculator(self):
        return EqualizationCalculator()

    def test_donor_share_based_on_excess_not_total(self, calculator):
        """Donor shares are computed from excess capacity above median, not total."""
        analysis = calculator.analyze_equalization()
        capacity_analysis = calculator.capacity_calc.analyze_all_regions()
        median = capacity_analysis.national_median_per_capita

        donors = [r for r in analysis.results if not r.is_recipient]

        # Calculate total excess capacity
        total_excess = sum(
            (r.per_capita_capacity - median) * r.population
            for r in donors
            if r.per_capita_capacity > median
        )

        # Verify each donor's share matches expected ratio
        for r in donors:
            if r.per_capita_capacity > median:
                expected_share = ((r.per_capita_capacity - median) * r.population) / total_excess
                actual_burden = abs(analysis.net_fiscal_impact[r.region])
                expected_burden = analysis.total_transfers * expected_share

                # Allow small rounding tolerance
                assert abs(actual_burden - expected_burden) < 0.001

    def test_region_at_median_pays_nothing(self, calculator):
        """A region exactly at median capacity should pay nothing."""
        analysis = calculator.analyze_equalization()
        capacity_analysis = calculator.capacity_calc.analyze_all_regions()
        median = capacity_analysis.national_median_per_capita

        for r in analysis.results:
            if abs(r.per_capita_capacity - median) < 1:  # Within $1 of median
                # Should have zero or near-zero net impact
                assert abs(analysis.net_fiscal_impact[r.region]) < 0.01

    def test_higher_excess_means_higher_burden(self, calculator):
        """Higher excess capacity above median means proportionally higher burden."""
        analysis = calculator.analyze_equalization()
        capacity_analysis = calculator.capacity_calc.analyze_all_regions()
        median = capacity_analysis.national_median_per_capita

        donors = [r for r in analysis.results if not r.is_recipient and r.per_capita_capacity > median]

        if len(donors) >= 2:
            # Sort by excess capacity
            sorted_by_excess = sorted(
                donors,
                key=lambda r: (r.per_capita_capacity - median) * r.population,
                reverse=True
            )

            # Sort by burden
            sorted_by_burden = sorted(
                donors,
                key=lambda r: abs(analysis.net_fiscal_impact[r.region]),
                reverse=True
            )

            # Order should match (higher excess = higher burden)
            for i in range(len(donors)):
                assert sorted_by_excess[i].region == sorted_by_burden[i].region

    def test_donor_burdens_sum_to_total_transfers(self, calculator):
        """Sum of donor burdens equals total transfers to recipients."""
        analysis = calculator.analyze_equalization()

        donor_burdens = sum(
            abs(impact)
            for region, impact in analysis.net_fiscal_impact.items()
            if impact < 0
        )

        recipient_transfers = sum(
            impact
            for region, impact in analysis.net_fiscal_impact.items()
            if impact > 0
        )

        # These should be equal (conservation of transfers)
        assert abs(donor_burdens - recipient_transfers) < 0.01
        assert abs(donor_burdens - analysis.total_transfers) < 0.01

    def test_year_parameter_affects_median(self, calculator):
        """The year parameter is used consistently in median calculation."""
        # Both calls to analyze_all_regions should use the same year
        # This is a structural test - we verify the analysis uses consistent data
        analysis = calculator.analyze_equalization(2022)

        # All results should reference the same median
        medians = set(r.median_capacity for r in analysis.results)
        assert len(medians) == 1  # All results have same median

    def test_pacific_and_northeast_are_donors(self, calculator):
        """Pacific and Northeast should be donors (above median capacity)."""
        analysis = calculator.analyze_equalization()

        donor_regions = [r.region for r in analysis.results if not r.is_recipient]

        assert 'Pacific' in donor_regions
        assert 'Northeast' in donor_regions

    def test_southeast_is_recipient(self, calculator):
        """Southeast should be a recipient (below median capacity)."""
        analysis = calculator.analyze_equalization()

        recipient_regions = [r.region for r in analysis.results if r.is_recipient]

        assert 'Southeast' in recipient_regions
