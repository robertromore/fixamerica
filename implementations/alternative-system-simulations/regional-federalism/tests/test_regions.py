"""Tests for region configuration module."""

import pytest
from src.regions import RegionConfig, load_regions, US_STATES


class TestRegionConfig:
    """Tests for RegionConfig class."""

    def test_load_default_config(self):
        """Default config loads without errors."""
        config = load_regions()
        assert config is not None
        assert len(config.regions) == 7

    def test_all_states_assigned(self):
        """All 50 states are assigned to a region."""
        config = load_regions()
        errors = config.validate()
        assert errors == [], f"Validation errors: {errors}"

    def test_no_duplicate_assignments(self):
        """No state is assigned to multiple regions."""
        config = load_regions()
        all_states = []
        for states in config.regions.values():
            all_states.extend(states)
        assert len(all_states) == len(set(all_states))

    def test_get_region_for_state(self):
        """Can retrieve region for any state."""
        config = load_regions()
        assert config.get_region('CA') == 'Pacific'
        assert config.get_region('TX') == 'Southwest'
        assert config.get_region('NY') == 'Northeast'

    def test_get_region_for_dc(self):
        """DC is assigned to its configured region."""
        config = load_regions()
        assert config.get_region('DC') == config.dc_assignment

    def test_get_states_for_region(self):
        """Can retrieve states for any region."""
        config = load_regions()
        pacific_states = config.get_states('Pacific')
        assert 'CA' in pacific_states
        assert 'WA' in pacific_states
        assert 'OR' in pacific_states

    def test_dc_in_assigned_region_states(self):
        """DC appears in its assigned region's state list."""
        config = load_regions()
        assigned_region_states = config.get_states(config.dc_assignment)
        assert 'DC' in assigned_region_states

    def test_region_names(self):
        """Expected region names are present."""
        config = load_regions()
        names = config.get_region_names()
        expected = ['Northeast', 'Southeast', 'Midwest', 'Great_Plains',
                    'Southwest', 'Pacific', 'Mountain']
        assert sorted(names) == sorted(expected)

    def test_population_estimates(self):
        """Population estimates are positive."""
        config = load_regions()
        for region in config.get_region_names():
            pop = config.get_population_estimate(region)
            assert pop > 0, f"{region} has zero or negative population"

    def test_invalid_dc_assignment_detected(self):
        """Invalid dc_assignment is caught by validation."""
        config = load_regions()
        config.dc_assignment = 'NonexistentRegion'
        errors = config.validate()
        assert any('dc_assignment' in e for e in errors)

    def test_unknown_state_in_region(self):
        """Unknown state code is caught by validation."""
        config = load_regions()
        config.regions['Pacific'].append('XX')
        errors = config.validate()
        assert any('Unknown state codes' in e for e in errors)

    def test_summary_generation(self):
        """Summary can be generated without errors."""
        config = load_regions()
        summary = config.summary()
        assert 'Region Configuration Summary' in summary
        assert 'Pacific' in summary
