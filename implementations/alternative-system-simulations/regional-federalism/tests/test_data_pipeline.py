"""Tests for data pipeline module."""

import pytest
from src.data_pipeline import ElectoralDataLoader, FiscalDataLoader
from src.regions import load_regions


class TestElectoralDataLoader:
    """Tests for ElectoralDataLoader class."""

    @pytest.fixture
    def loader(self):
        return ElectoralDataLoader()

    def test_2016_data_available(self, loader):
        """2016 election data is available."""
        data = loader.get_election_data(2016)
        assert len(data) == 51  # 50 states + DC

    def test_2020_data_available(self, loader):
        """2020 election data is available."""
        data = loader.get_election_data(2020)
        assert len(data) == 51

    def test_2024_data_available(self, loader):
        """2024 election data is available."""
        data = loader.get_election_data(2024)
        assert len(data) == 51  # 50 states + DC

    def test_invalid_year_raises(self, loader):
        """Invalid year raises ValueError."""
        with pytest.raises(ValueError):
            loader.get_election_data(2012)  # No 2012 data

    def test_state_data_structure(self, loader):
        """State data has required fields."""
        data = loader.get_election_data(2020)
        for state, votes in data.items():
            assert 'dem' in votes
            assert 'rep' in votes
            assert 'other' in votes
            assert 'ev' in votes

    def test_national_totals_sum(self, loader):
        """National totals equal sum of state totals."""
        data = loader.get_election_data(2020)
        totals = loader.get_national_totals(2020)

        expected_dem = sum(v['dem'] for v in data.values())
        expected_rep = sum(v['rep'] for v in data.values())

        assert totals['dem'] == expected_dem
        assert totals['rep'] == expected_rep

    def test_electoral_votes_sum_to_538(self, loader):
        """Total electoral votes equal 538."""
        data = loader.get_election_data(2020)
        total_ev = sum(v['ev'] for v in data.values())
        assert total_ev == 538

    def test_aggregate_by_region(self, loader):
        """Regional aggregation produces all regions."""
        regional = loader.aggregate_by_region(2020)
        assert len(regional) == 7

    def test_regional_votes_sum_to_national(self, loader):
        """Regional vote sums equal national totals."""
        regional = loader.aggregate_by_region(2020)
        national = loader.get_national_totals(2020)

        regional_dem = sum(r['dem'] for r in regional.values())
        regional_rep = sum(r['rep'] for r in regional.values())

        assert regional_dem == national['dem']
        assert regional_rep == national['rep']

    def test_results_by_state(self, loader):
        """get_results_by_state returns ElectionResult objects."""
        results = loader.get_results_by_state(2020)
        assert len(results) == 51

        for r in results:
            assert r.state in loader.get_election_data(2020)
            assert r.total_votes == r.democrat_votes + r.republican_votes + r.other_votes
            assert r.winner in ('D', 'R')


class TestFiscalDataLoader:
    """Tests for FiscalDataLoader class."""

    @pytest.fixture
    def loader(self):
        return FiscalDataLoader()

    def test_state_data_available(self, loader):
        """State economic data is available."""
        data = loader.get_state_data()
        assert len(data) == 51  # 50 states + DC

    def test_state_data_structure(self, loader):
        """State data has required fields."""
        data = loader.get_state_data()
        for state, econ in data.items():
            assert 'gdp' in econ
            assert 'pop' in econ
            assert 'income' in econ

    def test_aggregate_by_region(self, loader):
        """Regional aggregation produces all regions."""
        regional = loader.aggregate_by_region()
        assert len(regional) == 7

    def test_regional_population_sum(self, loader):
        """Regional populations sum to national total."""
        regional = loader.aggregate_by_region()
        national = loader.get_national_totals()

        regional_pop = sum(r['pop'] for r in regional.values())
        assert regional_pop == national['pop']

    def test_per_capita_calculations(self, loader):
        """Per capita values are calculated correctly."""
        regional = loader.aggregate_by_region()

        for region, data in regional.items():
            if data['pop'] > 0:
                expected_gdp_pc = data['gdp'] * 1000 / data['pop']
                assert abs(data['gdp_per_capita'] - expected_gdp_pc) < 1

    def test_national_totals(self, loader):
        """National totals are reasonable."""
        totals = loader.get_national_totals()
        assert totals['gdp'] > 20000  # > $20 trillion
        assert totals['pop'] > 300000  # > 300 million (in thousands)
