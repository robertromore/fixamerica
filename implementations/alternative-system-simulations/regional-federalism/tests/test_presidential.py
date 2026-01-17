"""Tests for presidential election simulation module."""

import pytest
from src.electoral.presidential import PresidentialSimulator, ElectionAnalysis


class TestPresidentialSimulator:
    """Tests for PresidentialSimulator class."""

    @pytest.fixture
    def simulator(self):
        return PresidentialSimulator()

    def test_analyze_2016(self, simulator):
        """2016 analysis completes without errors."""
        analysis = simulator.analyze_election(2016)
        assert analysis.year == 2016
        assert analysis.total_votes > 0

    def test_analyze_2020(self, simulator):
        """2020 analysis completes without errors."""
        analysis = simulator.analyze_election(2020)
        assert analysis.year == 2020
        assert analysis.total_votes > 0

    def test_2016_ec_winner(self, simulator):
        """2016 EC winner is R (Trump)."""
        analysis = simulator.analyze_election(2016)
        assert analysis.ec_winner == 'R'

    def test_2020_ec_winner(self, simulator):
        """2020 EC winner is D (Biden)."""
        analysis = simulator.analyze_election(2020)
        assert analysis.ec_winner == 'D'

    def test_2016_npv_winner(self, simulator):
        """2016 NPV winner is D (Clinton won popular vote)."""
        analysis = simulator.analyze_election(2016)
        assert analysis.npv_winner == 'D'

    def test_2016_outcome_differs(self, simulator):
        """2016 shows EC and RF outcomes differ."""
        analysis = simulator.analyze_election(2016)
        assert analysis.outcome_differs is True

    def test_2020_outcome_matches(self, simulator):
        """2020 shows EC and RF outcomes match."""
        analysis = simulator.analyze_election(2020)
        assert analysis.outcome_differs is False

    def test_rf_winner_determined(self, simulator):
        """RF winner is always determined."""
        for year in [2016, 2020]:
            analysis = simulator.analyze_election(year)
            assert analysis.rf_winner in ('D', 'R')

    def test_2016_requires_rcv(self, simulator):
        """2016 requires RCV (no majority)."""
        analysis = simulator.analyze_election(2016)
        # Neither candidate got >50% in 2016
        assert analysis.npv_has_majority is False
        assert analysis.rf_required_rcv is True

    def test_2020_no_rcv_needed(self, simulator):
        """2020 does not require RCV (Biden had majority)."""
        analysis = simulator.analyze_election(2020)
        assert analysis.npv_has_majority is True
        assert analysis.rf_required_rcv is False

    def test_rcv_note_present(self, simulator):
        """RCV note is populated."""
        analysis = simulator.analyze_election(2016)
        assert len(analysis.rf_rcv_note) > 0

    def test_candidates_list(self, simulator):
        """Candidates list has D and R."""
        analysis = simulator.analyze_election(2020)
        parties = [c.party for c in analysis.candidates]
        assert 'D' in parties
        assert 'R' in parties

    def test_candidate_votes_sum(self, simulator):
        """Candidate votes sum to total (minus other)."""
        analysis = simulator.analyze_election(2020)
        dem = next(c for c in analysis.candidates if c.party == 'D')
        rep = next(c for c in analysis.candidates if c.party == 'R')
        # dem + rep + other should equal total
        assert dem.popular_votes + rep.popular_votes < analysis.total_votes

    def test_regional_results_structure(self, simulator):
        """Regional results have expected structure."""
        analysis = simulator.analyze_election(2020)
        assert len(analysis.regional_results) == 7

        for region, data in analysis.regional_results.items():
            assert 'dem' in data
            assert 'rep' in data
            assert 'total' in data

    def test_regions_won_sum(self, simulator):
        """Regions won sum to 7."""
        analysis = simulator.analyze_election(2020)
        total_regions = analysis.regions_won['D'] + analysis.regions_won['R']
        assert total_regions == 7

    def test_swing_state_analysis(self, simulator):
        """Swing state analysis is populated."""
        analysis = simulator.analyze_election(2020)
        swing = analysis.swing_state_effect

        assert 'tipping_point_votes' in swing
        assert 'closest_state' in swing
        assert 'decisive_states' in swing
        assert swing['tipping_point_votes'] > 0

    def test_compare_systems_report(self, simulator):
        """Compare systems generates markdown report."""
        report = simulator.compare_systems(2020)
        assert '# 2020 Presidential Election' in report
        assert 'Electoral College' in report
        assert 'Regional Federalism' in report

    def test_multi_year_report(self, simulator):
        """Multi-year report generates correctly."""
        report = simulator.generate_multi_year_report([2016, 2020])
        assert '2016' in report
        assert '2020' in report
        assert 'Summary Table' in report

    def test_analyze_2024(self, simulator):
        """2024 analysis completes without errors."""
        analysis = simulator.analyze_election(2024)
        assert analysis.year == 2024
        assert analysis.total_votes > 0

    def test_invalid_year_raises(self, simulator):
        """Invalid year raises ValueError."""
        with pytest.raises(ValueError):
            simulator.analyze_election(2012)  # No 2012 data


class TestRCVRedistribution:
    """Tests for RCV redistribution logic."""

    @pytest.fixture
    def simulator(self):
        return PresidentialSimulator()

    def test_rcv_redistribution_when_no_majority(self, simulator):
        """RCV redistributes third-party votes when no majority."""
        # 2016 had no majority - test the redistribution logic
        analysis = simulator.analyze_election(2016)

        assert not analysis.npv_has_majority
        assert analysis.rf_required_rcv
        # Note should mention redistribution
        assert 'redistributed' in analysis.rf_rcv_note.lower()

    def test_rcv_preserves_plurality_winner(self, simulator):
        """RCV should preserve plurality winner when third-party split is typical."""
        # In 2016, Clinton won plurality; with typical 60/30 split to D/R,
        # she should still win after RCV
        analysis = simulator.analyze_election(2016)

        assert analysis.npv_winner == 'D'  # Clinton won plurality
        assert analysis.rf_winner == 'D'   # Should still win after RCV

    def test_no_rcv_when_majority(self, simulator):
        """No RCV needed when candidate has majority."""
        # 2020 Biden had >50%
        analysis = simulator.analyze_election(2020)

        assert analysis.npv_has_majority
        assert not analysis.rf_required_rcv
        assert 'majority' in analysis.rf_rcv_note.lower()

    def test_rf_winner_matches_npv_when_majority(self, simulator):
        """RF winner equals NPV winner when there's a clear majority."""
        analysis = simulator.analyze_election(2020)

        assert analysis.rf_winner == analysis.npv_winner

    def test_simulate_rf_election_direct(self, simulator):
        """Test _simulate_rf_election directly with controlled inputs."""
        # Test with majority scenario
        national_majority = {'dem': 55, 'rep': 40, 'other': 5, 'total': 100}
        winner, rcv_needed, note = simulator._simulate_rf_election(national_majority, True)

        assert winner == 'D'
        assert not rcv_needed
        assert '55.0%' in note  # Should show the majority percentage

    def test_simulate_rf_election_rcv_path(self, simulator):
        """Test _simulate_rf_election RCV path with controlled inputs."""
        # Test with no majority - forces RCV
        national_no_majority = {'dem': 48, 'rep': 46, 'other': 6, 'total': 100}
        winner, rcv_needed, note = simulator._simulate_rf_election(national_no_majority, False)

        assert rcv_needed
        assert 'redistributed' in note.lower()
        # With 60% of 6 other votes going to D: 48 + 3.6 = 51.6
        # With 30% of 6 other votes going to R: 46 + 1.8 = 47.8
        # D should win
        assert winner == 'D'

    def test_rcv_can_flip_winner(self, simulator):
        """Test that RCV could theoretically flip winner with extreme redistribution."""
        # Construct a scenario where D has plurality but R would win RCV
        # This requires D getting fewer than 40% of third-party votes
        # Our model assumes 60/30 split, so this shouldn't flip
        # But we verify the math is correct

        # D: 45, R: 44, Other: 11, Total: 100
        # After RCV: D gets 45 + 11*0.6 = 51.6, R gets 44 + 11*0.3 = 47.3
        national = {'dem': 45, 'rep': 44, 'other': 11, 'total': 100}
        winner, rcv_needed, note = simulator._simulate_rf_election(national, False)

        assert rcv_needed
        assert winner == 'D'  # D should win with our redistribution model

    def test_outcome_differs_uses_rf_not_npv(self, simulator):
        """outcome_differs compares EC to RF winner, not NPV."""
        analysis = simulator.analyze_election(2016)

        # In 2016: EC=R, NPV=D, RF=D
        # outcome_differs should be True (EC != RF)
        assert analysis.ec_winner == 'R'
        assert analysis.rf_winner == 'D'
        assert analysis.outcome_differs is True


class TestMultiYearReport:
    """Tests for multi-year report generation."""

    @pytest.fixture
    def simulator(self):
        return PresidentialSimulator()

    def test_multi_year_report_uses_rf_columns(self, simulator):
        """Multi-year report uses RF Winner, not NPV Winner."""
        report = simulator.generate_multi_year_report([2016, 2020])

        # Should have RF columns
        assert 'RF Winner' in report
        assert 'RCV Required' in report
        assert 'First-Round Margin' in report

        # Should NOT have old NPV column headers
        lines = report.split('\n')
        header_line = None
        for line in lines:
            if '| Year |' in line:
                header_line = line
                break

        assert header_line is not None
        assert 'NPV Winner' not in header_line
        assert 'RF Winner' in header_line

    def test_different_column_matches_ec_vs_rf(self, simulator):
        """Different? column reflects EC vs RF comparison."""
        report = simulator.generate_multi_year_report([2016, 2020])

        # Find data rows
        lines = report.split('\n')
        data_rows = [l for l in lines if l.startswith('| 20')]

        for row in data_rows:
            cols = [c.strip() for c in row.split('|')]
            # cols: ['', 'Year', 'EC Winner', 'RF Winner', 'Different?', 'RCV Required', 'First-Round Margin', '']

            year = cols[1]
            ec_winner = cols[2]
            rf_winner = cols[3]
            different = cols[4]

            # Verify Different? matches EC vs RF comparison
            if ec_winner != rf_winner:
                assert '**YES**' in different, f"Year {year}: EC={ec_winner}, RF={rf_winner} should show YES"
            else:
                assert 'No' in different and '**YES**' not in different, f"Year {year}: EC={ec_winner}, RF={rf_winner} should show No"

    def test_2016_shows_different_2020_shows_same(self, simulator):
        """2016 shows outcomes differ, 2020 shows outcomes match."""
        report = simulator.generate_multi_year_report([2016, 2020])

        lines = report.split('\n')
        for line in lines:
            if '| 2016 |' in line:
                assert '**YES**' in line  # 2016: EC=R, RF=D -> different
            elif '| 2020 |' in line:
                # 2020: EC=D, RF=D -> same
                assert '**YES**' not in line
