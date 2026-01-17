"""Tests for fiscal convergence projection module."""

import pytest
from src.fiscal.convergence import ConvergenceProjector, ConvergenceAnalysis


class TestConvergenceProjector:
    """Tests for ConvergenceProjector class."""

    @pytest.fixture
    def projector(self):
        return ConvergenceProjector()

    def test_run_projection_default(self, projector):
        """Default projection runs without errors."""
        analysis = projector.run_projection()
        assert analysis is not None
        assert analysis.projection_years == 20

    def test_run_projection_custom_years(self, projector):
        """Custom projection years work."""
        analysis = projector.run_projection(projection_years=10)
        assert analysis.projection_years == 10
        # Should have 11 projections (base year + 10 years)
        assert len(analysis.projections) == 11

    def test_run_projection_custom_growth(self, projector):
        """Custom growth parameters work."""
        analysis = projector.run_projection(
            base_growth=0.03,
            growth_dividend=0.02
        )
        assert analysis.base_growth_rate == 0.03
        assert analysis.growth_dividend == 0.02

    def test_base_year(self, projector):
        """Base year is 2022 by default."""
        analysis = projector.run_projection()
        assert analysis.base_year == 2022

    def test_projections_list_length(self, projector):
        """Projections list has correct length."""
        analysis = projector.run_projection(projection_years=20)
        # Base year + 20 years = 21 projections
        assert len(analysis.projections) == 21


class TestCoefficientOfVariation:
    """Tests for coefficient of variation calculation."""

    @pytest.fixture
    def projector(self):
        return ConvergenceProjector()

    def test_cv_uniform_distribution(self, projector):
        """CV is 0 for uniform distribution."""
        capacities = {'A': 100, 'B': 100, 'C': 100}
        populations = {'A': 1000, 'B': 1000, 'C': 1000}
        cv = projector.calculate_coefficient_of_variation(capacities, populations)
        assert cv == pytest.approx(0.0, abs=0.001)

    def test_cv_positive_for_variation(self, projector):
        """CV is positive when there's variation."""
        capacities = {'A': 100, 'B': 200, 'C': 300}
        populations = {'A': 1000, 'B': 1000, 'C': 1000}
        cv = projector.calculate_coefficient_of_variation(capacities, populations)
        assert cv > 0

    def test_cv_weighted_by_population(self, projector):
        """CV is weighted by population."""
        # Large population at mean, small outliers
        capacities = {'A': 100, 'B': 100, 'C': 200}
        populations_equal = {'A': 1000, 'B': 1000, 'C': 1000}
        populations_weighted = {'A': 10000, 'B': 10000, 'C': 1000}

        cv_equal = projector.calculate_coefficient_of_variation(capacities, populations_equal)
        cv_weighted = projector.calculate_coefficient_of_variation(capacities, populations_weighted)

        # Weighted CV should be lower (outlier has less weight)
        assert cv_weighted < cv_equal

    def test_cv_range(self, projector):
        """CV is in reasonable range for real data."""
        analysis = projector.run_projection()
        initial_cv = analysis.initial_cv
        # Regional fiscal disparities typically produce CV of 10-30%
        assert 0.05 < initial_cv < 0.50


class TestConvergenceBehavior:
    """Tests for convergence behavior over time."""

    @pytest.fixture
    def projector(self):
        return ConvergenceProjector()

    def test_cv_decreases_over_time(self, projector):
        """CV should decrease over the projection period."""
        analysis = projector.run_projection(growth_dividend=0.01)

        initial_cv = analysis.projections[0].coefficient_of_variation
        final_cv = analysis.projections[-1].coefficient_of_variation

        assert final_cv < initial_cv

    def test_higher_dividend_faster_convergence(self, projector):
        """Higher growth dividend leads to faster convergence."""
        analysis_low = projector.run_projection(growth_dividend=0.005)
        analysis_high = projector.run_projection(growth_dividend=0.020)

        # Higher dividend should result in lower final CV
        assert analysis_high.final_cv < analysis_low.final_cv

    def test_zero_dividend_no_convergence(self, projector):
        """Zero growth dividend means no convergence acceleration."""
        analysis = projector.run_projection(growth_dividend=0.0)

        # CV may change slightly due to base growth, but not much
        initial_cv = analysis.initial_cv
        final_cv = analysis.final_cv

        # With 0 dividend, CV change should be minimal
        # (slight change possible from base growth effects)
        cv_change = abs(initial_cv - final_cv)
        assert cv_change < initial_cv * 0.5  # Less than 50% change

    def test_convergence_threshold_detection(self, projector):
        """Convergence threshold detection works."""
        # Run with high dividend to likely achieve convergence
        analysis = projector.run_projection(
            projection_years=50,
            growth_dividend=0.03,
            convergence_threshold=0.15
        )

        if analysis.convergence_achieved:
            assert analysis.years_to_convergence is not None
            assert analysis.years_to_convergence > 0
            assert analysis.years_to_convergence <= 50


class TestYearProjection:
    """Tests for year-by-year projections."""

    @pytest.fixture
    def projector(self):
        return ConvergenceProjector()

    def test_projection_year_sequence(self, projector):
        """Projection years are sequential."""
        analysis = projector.run_projection(base_year=2022, projection_years=10)

        years = [p.year for p in analysis.projections]
        expected = list(range(2022, 2033))
        assert years == expected

    def test_projection_has_capacities(self, projector):
        """Each projection has regional capacities."""
        analysis = projector.run_projection()

        for proj in analysis.projections:
            assert len(proj.regional_capacities) == 7  # 7 regions
            for cap in proj.regional_capacities.values():
                assert cap > 0

    def test_capacities_grow_over_time(self, projector):
        """Capacities grow over time (positive base growth)."""
        analysis = projector.run_projection(base_growth=0.02)

        for region in analysis.projections[0].regional_capacities.keys():
            initial = analysis.projections[0].regional_capacities[region]
            final = analysis.projections[-1].regional_capacities[region]
            assert final > initial

    def test_median_grows_over_time(self, projector):
        """Median capacity grows over time."""
        analysis = projector.run_projection()

        initial_median = analysis.projections[0].median_capacity
        final_median = analysis.projections[-1].median_capacity
        assert final_median > initial_median

    def test_spread_ratio_decreases(self, projector):
        """Spread ratio (max/min) decreases with convergence."""
        analysis = projector.run_projection(growth_dividend=0.01)

        initial_spread = analysis.projections[0].spread_ratio
        final_spread = analysis.projections[-1].spread_ratio

        # Spread should decrease (convergence)
        assert final_spread < initial_spread


class TestRegionTrajectories:
    """Tests for region trajectory tracking."""

    @pytest.fixture
    def projector(self):
        return ConvergenceProjector()

    def test_trajectory_count(self, projector):
        """Trajectory exists for each region."""
        analysis = projector.run_projection()
        assert len(analysis.region_trajectories) == 7

    def test_trajectory_growth_positive(self, projector):
        """All regions experience growth."""
        analysis = projector.run_projection()

        for traj in analysis.region_trajectories:
            assert traj.final_capacity > traj.initial_capacity
            assert traj.capacity_growth > 0
            assert traj.annualized_growth > 0

    def test_recipient_trajectories(self, projector):
        """Recipients receive transfers over time."""
        analysis = projector.run_projection()

        # At least one region should be a recipient
        recipients = [t for t in analysis.region_trajectories if t.years_as_recipient > 0]
        assert len(recipients) > 0

        # Recipients should have positive cumulative transfers
        for traj in recipients:
            assert traj.total_transfers_received > 0

    def test_gap_reduction_for_recipients(self, projector):
        """Recipients see gap reduction over time."""
        analysis = projector.run_projection(growth_dividend=0.01)

        for traj in analysis.region_trajectories:
            if traj.initial_gap_pct > 0:
                # Gap should decrease
                assert traj.final_gap_pct <= traj.initial_gap_pct


class TestConvergenceReport:
    """Tests for convergence report generation."""

    @pytest.fixture
    def projector(self):
        return ConvergenceProjector()

    def test_report_generation(self, projector):
        """Report generates without errors."""
        report = projector.generate_report()
        assert len(report) > 0

    def test_report_has_title(self, projector):
        """Report has title."""
        report = projector.generate_report()
        assert '# Fiscal Convergence Projection' in report

    def test_report_has_assumptions(self, projector):
        """Report includes model assumptions."""
        report = projector.generate_report()
        assert 'Assumption' in report or 'assumption' in report
        assert 'Growth' in report or 'growth' in report

    def test_report_has_summary(self, projector):
        """Report includes summary results."""
        report = projector.generate_report()
        assert 'CV' in report or 'coefficient' in report.lower()

    def test_report_has_trajectory_table(self, projector):
        """Report includes trajectory table."""
        report = projector.generate_report()
        assert '| Year |' in report or '| Region |' in report

    def test_report_has_findings(self, projector):
        """Report includes key findings."""
        report = projector.generate_report()
        assert 'Finding' in report or 'finding' in report


class TestTransferCalculations:
    """Tests for transfer calculations in projections."""

    @pytest.fixture
    def projector(self):
        return ConvergenceProjector()

    def test_total_transfers_positive(self, projector):
        """Total transfers are positive each year."""
        analysis = projector.run_projection()

        # Skip base year (no transfers)
        for proj in analysis.projections[1:]:
            assert proj.total_transfers >= 0

    def test_transfers_to_recipients_only(self, projector):
        """Only below-median regions receive transfers."""
        analysis = projector.run_projection()

        for traj in analysis.region_trajectories:
            # If never a recipient, should have zero transfers
            if traj.years_as_recipient == 0:
                assert traj.total_transfers_received == 0

    def test_cumulative_transfers_reasonable(self, projector):
        """Cumulative transfers are in reasonable range."""
        analysis = projector.run_projection()

        # Total cumulative transfers across all regions
        total = sum(t.total_transfers_received for t in analysis.region_trajectories)

        # Should be in billions, reasonable for 20-year period
        # (A few hundred billion total would be expected)
        assert 0 < total < 10000  # Less than $10 trillion cumulative
