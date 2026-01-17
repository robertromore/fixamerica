"""
Region configuration and state-to-region mapping.

This module provides utilities for loading region configurations and
mapping states to their assigned regions under Regional Federalism.
"""

from pathlib import Path
from typing import Dict, List, Optional
import yaml


# All US states and territories
US_STATES = {
    'AL': 'Alabama', 'AK': 'Alaska', 'AZ': 'Arizona', 'AR': 'Arkansas',
    'CA': 'California', 'CO': 'Colorado', 'CT': 'Connecticut', 'DE': 'Delaware',
    'FL': 'Florida', 'GA': 'Georgia', 'HI': 'Hawaii', 'ID': 'Idaho',
    'IL': 'Illinois', 'IN': 'Indiana', 'IA': 'Iowa', 'KS': 'Kansas',
    'KY': 'Kentucky', 'LA': 'Louisiana', 'ME': 'Maine', 'MD': 'Maryland',
    'MA': 'Massachusetts', 'MI': 'Michigan', 'MN': 'Minnesota', 'MS': 'Mississippi',
    'MO': 'Missouri', 'MT': 'Montana', 'NE': 'Nebraska', 'NV': 'Nevada',
    'NH': 'New Hampshire', 'NJ': 'New Jersey', 'NM': 'New Mexico', 'NY': 'New York',
    'NC': 'North Carolina', 'ND': 'North Dakota', 'OH': 'Ohio', 'OK': 'Oklahoma',
    'OR': 'Oregon', 'PA': 'Pennsylvania', 'RI': 'Rhode Island', 'SC': 'South Carolina',
    'SD': 'South Dakota', 'TN': 'Tennessee', 'TX': 'Texas', 'UT': 'Utah',
    'VT': 'Vermont', 'VA': 'Virginia', 'WA': 'Washington', 'WV': 'West Virginia',
    'WI': 'Wisconsin', 'WY': 'Wyoming', 'DC': 'District of Columbia'
}


class RegionConfig:
    """
    Manages region configuration for Regional Federalism simulations.

    Attributes:
        regions: Dict mapping region names to lists of state codes
        state_to_region: Dict mapping state codes to region names
        dc_assignment: Region to which DC is assigned
    """

    def __init__(self, config_path: Optional[Path] = None):
        """
        Initialize region configuration.

        Args:
            config_path: Path to YAML configuration file. If None, uses default.
        """
        if config_path is None:
            config_path = self._get_default_config_path()

        self._config = self._load_config(config_path)
        self.regions = self._parse_regions()
        self.state_to_region = self._build_state_mapping()
        self.dc_assignment = self._config.get('dc_assignment', 'Northeast')

    @staticmethod
    def _get_default_config_path() -> Path:
        """Get path to default region configuration."""
        return Path(__file__).parent.parent / 'config' / 'regions' / 'default.yaml'

    def _load_config(self, path: Path) -> dict:
        """Load YAML configuration file."""
        with open(path, 'r') as f:
            return yaml.safe_load(f)

    def _parse_regions(self) -> Dict[str, List[str]]:
        """Parse regions from configuration."""
        regions = {}
        for region_name, region_data in self._config.get('regions', {}).items():
            regions[region_name] = region_data.get('states', [])
        return regions

    def _build_state_mapping(self) -> Dict[str, str]:
        """Build state-to-region mapping."""
        mapping = {}
        for region_name, states in self.regions.items():
            for state in states:
                mapping[state] = region_name
        return mapping

    def get_region(self, state_code: str) -> str:
        """
        Get the region for a state.

        Args:
            state_code: Two-letter state code (e.g., 'CA', 'TX')

        Returns:
            Region name

        Raises:
            KeyError: If state is not found in configuration
        """
        if state_code == 'DC':
            return self.dc_assignment
        return self.state_to_region[state_code]

    def get_states(self, region_name: str) -> List[str]:
        """
        Get all states in a region.

        Args:
            region_name: Name of the region

        Returns:
            List of state codes
        """
        states = self.regions.get(region_name, [])
        if region_name == self.dc_assignment:
            states = states + ['DC']
        return states

    def get_region_names(self) -> List[str]:
        """Get list of all region names."""
        return list(self.regions.keys())

    def get_population_estimate(self, region_name: str) -> int:
        """
        Get estimated population for a region.

        Args:
            region_name: Name of the region

        Returns:
            Population estimate
        """
        region_data = self._config.get('regions', {}).get(region_name, {})
        return region_data.get('population_estimate', 0)

    def validate(self) -> List[str]:
        """
        Validate the region configuration.

        Returns:
            List of validation errors (empty if valid)
        """
        errors = []

        # Check all 50 states are assigned
        assigned_states = set()
        for states in self.regions.values():
            assigned_states.update(states)

        expected_states = set(US_STATES.keys()) - {'DC'}  # DC handled separately
        missing = expected_states - assigned_states
        extra = assigned_states - expected_states

        if missing:
            errors.append(f"States not assigned to any region: {missing}")
        if extra:
            errors.append(f"Unknown state codes in configuration: {extra}")

        # Check for duplicate assignments
        seen = set()
        duplicates = set()
        for states in self.regions.values():
            for state in states:
                if state in seen:
                    duplicates.add(state)
                seen.add(state)

        if duplicates:
            errors.append(f"States assigned to multiple regions: {duplicates}")

        # Check dc_assignment points to a valid region
        if self.dc_assignment not in self.regions:
            errors.append(
                f"dc_assignment '{self.dc_assignment}' is not a valid region. "
                f"Valid regions: {list(self.regions.keys())}"
            )

        return errors

    def summary(self) -> str:
        """Generate a summary of the region configuration."""
        lines = ["Region Configuration Summary", "=" * 40]

        for region_name in sorted(self.regions.keys()):
            states = self.regions[region_name]
            pop = self.get_population_estimate(region_name)
            lines.append(f"\n{region_name}:")
            lines.append(f"  States: {', '.join(sorted(states))}")
            lines.append(f"  Population: {pop:,}")

        lines.append(f"\nDC assigned to: {self.dc_assignment}")
        lines.append(f"Total regions: {len(self.regions)}")
        lines.append(f"Total states: {sum(len(s) for s in self.regions.values())}")

        return "\n".join(lines)


def load_regions(config_name: str = 'default') -> RegionConfig:
    """
    Load a region configuration by name.

    Args:
        config_name: Name of the configuration (without .yaml extension)

    Returns:
        RegionConfig instance
    """
    config_dir = Path(__file__).parent.parent / 'config' / 'regions'
    config_path = config_dir / f'{config_name}.yaml'
    return RegionConfig(config_path)


if __name__ == '__main__':
    # Test the region configuration
    config = load_regions()
    errors = config.validate()

    if errors:
        print("Validation errors:")
        for error in errors:
            print(f"  - {error}")
    else:
        print("Configuration valid!")

    print()
    print(config.summary())
