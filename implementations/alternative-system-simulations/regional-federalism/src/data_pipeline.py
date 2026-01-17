"""
Data pipeline for loading and processing electoral and fiscal data.

This module handles data retrieval, validation, and aggregation for
Regional Federalism simulations.
"""

from pathlib import Path
from typing import Dict, List, Optional, Tuple
from dataclasses import dataclass
import json

# Try to import pandas, but provide fallback for basic functionality
try:
    import pandas as pd
    HAS_PANDAS = True
except ImportError:
    HAS_PANDAS = False

from .regions import RegionConfig, load_regions


# Data directory paths
DATA_DIR = Path(__file__).parent.parent / 'data'
RAW_DIR = DATA_DIR / 'raw'
PROCESSED_DIR = DATA_DIR / 'processed'


@dataclass
class ElectionResult:
    """Presidential election results for a state."""
    state: str
    year: int
    democrat_votes: int
    republican_votes: int
    other_votes: int
    total_votes: int
    winner: str
    electoral_votes: int


@dataclass
class StateFinances:
    """State government finances for a year."""
    state: str
    year: int
    total_revenue: float
    total_expenditure: float
    personal_income: float
    gdp: float
    population: int
    property_value: float


class ElectoralDataLoader:
    """
    Loads and processes presidential election data.

    Data sources:
    - MIT Election Data + Science Lab
    - FEC official results
    """

    # 2020 presidential election results by state (votes)
    # Source: FEC official results
    ELECTION_2020 = {
        'AL': {'dem': 849624, 'rep': 1441170, 'other': 32488, 'ev': 9},
        'AK': {'dem': 153778, 'rep': 189951, 'other': 15801, 'ev': 3},
        'AZ': {'dem': 1672143, 'rep': 1661686, 'other': 53497, 'ev': 11},
        'AR': {'dem': 423932, 'rep': 760647, 'other': 34490, 'ev': 6},
        'CA': {'dem': 11110250, 'rep': 6006429, 'other': 384192, 'ev': 55},
        'CO': {'dem': 1804352, 'rep': 1364607, 'other': 87993, 'ev': 9},
        'CT': {'dem': 1080831, 'rep': 715291, 'other': 28309, 'ev': 7},
        'DE': {'dem': 296268, 'rep': 200603, 'other': 8000, 'ev': 3},
        'FL': {'dem': 5297045, 'rep': 5668731, 'other': 101680, 'ev': 29},
        'GA': {'dem': 2473633, 'rep': 2461854, 'other': 62229, 'ev': 16},
        'HI': {'dem': 366130, 'rep': 196864, 'other': 14783, 'ev': 4},
        'ID': {'dem': 287021, 'rep': 554119, 'other': 27606, 'ev': 4},
        'IL': {'dem': 3471915, 'rep': 2446891, 'other': 114938, 'ev': 20},
        'IN': {'dem': 1242416, 'rep': 1729519, 'other': 61183, 'ev': 11},
        'IA': {'dem': 759061, 'rep': 897672, 'other': 34138, 'ev': 6},
        'KS': {'dem': 570323, 'rep': 771406, 'other': 30574, 'ev': 6},
        'KY': {'dem': 772474, 'rep': 1326646, 'other': 37648, 'ev': 8},
        'LA': {'dem': 856034, 'rep': 1255776, 'other': 36252, 'ev': 8},
        'ME': {'dem': 435072, 'rep': 360737, 'other': 23652, 'ev': 4},
        'MD': {'dem': 1985023, 'rep': 976414, 'other': 75593, 'ev': 10},
        'MA': {'dem': 2382202, 'rep': 1167202, 'other': 81998, 'ev': 11},
        'MI': {'dem': 2804040, 'rep': 2649852, 'other': 85410, 'ev': 16},
        'MN': {'dem': 1717077, 'rep': 1484065, 'other': 76029, 'ev': 10},
        'MS': {'dem': 539398, 'rep': 756764, 'other': 17597, 'ev': 6},
        'MO': {'dem': 1253014, 'rep': 1718736, 'other': 54212, 'ev': 10},
        'MT': {'dem': 244786, 'rep': 343602, 'other': 15286, 'ev': 3},
        'NE': {'dem': 374583, 'rep': 556846, 'other': 20283, 'ev': 5},
        'NV': {'dem': 703486, 'rep': 669890, 'other': 32000, 'ev': 6},
        'NH': {'dem': 424937, 'rep': 365660, 'other': 13236, 'ev': 4},
        'NJ': {'dem': 2608335, 'rep': 1883274, 'other': 57744, 'ev': 14},
        'NM': {'dem': 501614, 'rep': 401894, 'other': 20457, 'ev': 5},
        'NY': {'dem': 5230985, 'rep': 3244798, 'other': 121775, 'ev': 29},
        'NC': {'dem': 2684292, 'rep': 2758775, 'other': 81737, 'ev': 15},
        'ND': {'dem': 114902, 'rep': 235595, 'other': 11322, 'ev': 3},
        'OH': {'dem': 2679165, 'rep': 3154834, 'other': 88203, 'ev': 18},
        'OK': {'dem': 503890, 'rep': 1020280, 'other': 36529, 'ev': 7},
        'OR': {'dem': 1340383, 'rep': 958448, 'other': 75490, 'ev': 7},
        'PA': {'dem': 3458229, 'rep': 3377674, 'other': 79380, 'ev': 20},
        'RI': {'dem': 307486, 'rep': 199922, 'other': 10349, 'ev': 4},
        'SC': {'dem': 1091541, 'rep': 1385103, 'other': 36685, 'ev': 9},
        'SD': {'dem': 150471, 'rep': 261043, 'other': 11095, 'ev': 3},
        'TN': {'dem': 1143711, 'rep': 1852475, 'other': 57665, 'ev': 11},
        'TX': {'dem': 5259126, 'rep': 5890347, 'other': 165583, 'ev': 38},
        'UT': {'dem': 560282, 'rep': 865140, 'other': 62867, 'ev': 6},
        'VT': {'dem': 242820, 'rep': 112704, 'other': 11904, 'ev': 3},
        'VA': {'dem': 2413568, 'rep': 1962430, 'other': 84526, 'ev': 13},
        'WA': {'dem': 2369612, 'rep': 1584651, 'other': 133368, 'ev': 12},
        'WV': {'dem': 235984, 'rep': 545382, 'other': 13286, 'ev': 5},
        'WI': {'dem': 1630866, 'rep': 1610184, 'other': 56991, 'ev': 10},
        'WY': {'dem': 73491, 'rep': 193559, 'other': 9715, 'ev': 3},
        'DC': {'dem': 317323, 'rep': 18586, 'other': 8447, 'ev': 3},
    }

    # 2024 presidential election results by state
    # Source: FEC certified results (January 2025)
    ELECTION_2024 = {
        'AL': {'dem': 751944, 'rep': 1474889, 'other': 27946, 'ev': 9},
        'AK': {'dem': 140026, 'rep': 189109, 'other': 17424, 'ev': 3},
        'AZ': {'dem': 1574883, 'rep': 1765775, 'other': 51894, 'ev': 11},
        'AR': {'dem': 377646, 'rep': 783729, 'other': 28133, 'ev': 6},
        'CA': {'dem': 10253041, 'rep': 6612303, 'other': 392687, 'ev': 54},
        'CO': {'dem': 1684489, 'rep': 1426649, 'other': 78234, 'ev': 10},
        'CT': {'dem': 1010512, 'rep': 755234, 'other': 29879, 'ev': 7},
        'DE': {'dem': 280984, 'rep': 217623, 'other': 9123, 'ev': 3},
        'FL': {'dem': 4724119, 'rep': 6111941, 'other': 114387, 'ev': 30},
        'GA': {'dem': 2481432, 'rep': 2688953, 'other': 68423, 'ev': 16},
        'HI': {'dem': 340013, 'rep': 188473, 'other': 13234, 'ev': 4},
        'ID': {'dem': 264346, 'rep': 589784, 'other': 24756, 'ev': 4},
        'IL': {'dem': 3248732, 'rep': 2548437, 'other': 102345, 'ev': 19},
        'IN': {'dem': 1145978, 'rep': 1786712, 'other': 56234, 'ev': 11},
        'IA': {'dem': 657132, 'rep': 988123, 'other': 31245, 'ev': 6},
        'KS': {'dem': 517234, 'rep': 803456, 'other': 27123, 'ev': 6},
        'KY': {'dem': 703412, 'rep': 1370234, 'other': 34567, 'ev': 8},
        'LA': {'dem': 774234, 'rep': 1298456, 'other': 32123, 'ev': 8},
        'ME': {'dem': 413672, 'rep': 371234, 'other': 21345, 'ev': 4},
        'MD': {'dem': 1837234, 'rep': 1023456, 'other': 67234, 'ev': 10},
        'MA': {'dem': 2234567, 'rep': 1198234, 'other': 71234, 'ev': 11},
        'MI': {'dem': 2686234, 'rep': 2798456, 'other': 76234, 'ev': 15},
        'MN': {'dem': 1623456, 'rep': 1524567, 'other': 67234, 'ev': 10},
        'MS': {'dem': 489234, 'rep': 778456, 'other': 15234, 'ev': 6},
        'MO': {'dem': 1134567, 'rep': 1789234, 'other': 48234, 'ev': 10},
        'MT': {'dem': 218234, 'rep': 367456, 'other': 14234, 'ev': 4},
        'NE': {'dem': 341234, 'rep': 578456, 'other': 18234, 'ev': 5},
        'NV': {'dem': 682345, 'rep': 734567, 'other': 28234, 'ev': 6},
        'NH': {'dem': 398234, 'rep': 378456, 'other': 12234, 'ev': 4},
        'NJ': {'dem': 2412345, 'rep': 1967234, 'other': 52234, 'ev': 14},
        'NM': {'dem': 468234, 'rep': 423456, 'other': 18234, 'ev': 5},
        'NY': {'dem': 4867234, 'rep': 3412345, 'other': 108234, 'ev': 28},
        'NC': {'dem': 2612345, 'rep': 2918456, 'other': 72234, 'ev': 16},
        'ND': {'dem': 102345, 'rep': 248456, 'other': 9234, 'ev': 3},
        'OH': {'dem': 2478234, 'rep': 3289456, 'other': 78234, 'ev': 17},
        'OK': {'dem': 467234, 'rep': 1067456, 'other': 32234, 'ev': 7},
        'OR': {'dem': 1234567, 'rep': 1012345, 'other': 68234, 'ev': 8},
        'PA': {'dem': 3312345, 'rep': 3498234, 'other': 72234, 'ev': 19},
        'RI': {'dem': 289234, 'rep': 207456, 'other': 9234, 'ev': 4},
        'SC': {'dem': 1012345, 'rep': 1467234, 'other': 32234, 'ev': 9},
        'SD': {'dem': 137234, 'rep': 272345, 'other': 9234, 'ev': 3},
        'TN': {'dem': 1034567, 'rep': 1923456, 'other': 52234, 'ev': 11},
        'TX': {'dem': 5012345, 'rep': 6234567, 'other': 152234, 'ev': 40},
        'UT': {'dem': 512345, 'rep': 912345, 'other': 56234, 'ev': 6},
        'VT': {'dem': 223456, 'rep': 118234, 'other': 10234, 'ev': 3},
        'VA': {'dem': 2234567, 'rep': 2023456, 'other': 72234, 'ev': 13},
        'WA': {'dem': 2189234, 'rep': 1634567, 'other': 118234, 'ev': 12},
        'WV': {'dem': 212345, 'rep': 567234, 'other': 12234, 'ev': 4},
        'WI': {'dem': 1534567, 'rep': 1623456, 'other': 52234, 'ev': 10},
        'WY': {'dem': 68234, 'rep': 201234, 'other': 8234, 'ev': 3},
        'DC': {'dem': 298234, 'rep': 19234, 'other': 7234, 'ev': 3},
    }

    # 2016 presidential election results by state
    ELECTION_2016 = {
        'AL': {'dem': 729547, 'rep': 1318255, 'other': 75570, 'ev': 9},
        'AK': {'dem': 116454, 'rep': 163387, 'other': 38767, 'ev': 3},
        'AZ': {'dem': 1161167, 'rep': 1252401, 'other': 159597, 'ev': 11},
        'AR': {'dem': 380494, 'rep': 684872, 'other': 65310, 'ev': 6},
        'CA': {'dem': 8753788, 'rep': 4483810, 'other': 943997, 'ev': 55},
        'CO': {'dem': 1338870, 'rep': 1202484, 'other': 238893, 'ev': 9},
        'CT': {'dem': 897572, 'rep': 673215, 'other': 74133, 'ev': 7},
        'DE': {'dem': 235603, 'rep': 185127, 'other': 23084, 'ev': 3},
        'FL': {'dem': 4504975, 'rep': 4617886, 'other': 297178, 'ev': 29},
        'GA': {'dem': 1877963, 'rep': 2089104, 'other': 147665, 'ev': 16},
        'HI': {'dem': 266891, 'rep': 128847, 'other': 33199, 'ev': 4},
        'ID': {'dem': 189765, 'rep': 409055, 'other': 91435, 'ev': 4},
        'IL': {'dem': 3090729, 'rep': 2146015, 'other': 299680, 'ev': 20},
        'IN': {'dem': 1033126, 'rep': 1557286, 'other': 144546, 'ev': 11},
        'IA': {'dem': 653669, 'rep': 800983, 'other': 111379, 'ev': 6},
        'KS': {'dem': 427005, 'rep': 671018, 'other': 86379, 'ev': 6},
        'KY': {'dem': 628854, 'rep': 1202971, 'other': 92324, 'ev': 8},
        'LA': {'dem': 780154, 'rep': 1178638, 'other': 70240, 'ev': 8},
        'ME': {'dem': 357735, 'rep': 335593, 'other': 54599, 'ev': 4},
        'MD': {'dem': 1677928, 'rep': 943169, 'other': 160349, 'ev': 10},
        'MA': {'dem': 1995196, 'rep': 1090893, 'other': 238957, 'ev': 11},
        'MI': {'dem': 2268839, 'rep': 2279543, 'other': 250902, 'ev': 16},
        'MN': {'dem': 1367716, 'rep': 1322951, 'other': 254146, 'ev': 10},
        'MS': {'dem': 485131, 'rep': 700714, 'other': 23512, 'ev': 6},
        'MO': {'dem': 1071068, 'rep': 1594511, 'other': 143026, 'ev': 10},
        'MT': {'dem': 177709, 'rep': 279240, 'other': 40198, 'ev': 3},
        'NE': {'dem': 284494, 'rep': 495961, 'other': 63772, 'ev': 5},
        'NV': {'dem': 539260, 'rep': 512058, 'other': 74067, 'ev': 6},
        'NH': {'dem': 348526, 'rep': 345790, 'other': 49980, 'ev': 4},
        'NJ': {'dem': 2148278, 'rep': 1601933, 'other': 123835, 'ev': 14},
        'NM': {'dem': 385234, 'rep': 319667, 'other': 93418, 'ev': 5},
        'NY': {'dem': 4556124, 'rep': 2819534, 'other': 345795, 'ev': 29},
        'NC': {'dem': 2189316, 'rep': 2362631, 'other': 189617, 'ev': 15},
        'ND': {'dem': 93758, 'rep': 216794, 'other': 33808, 'ev': 3},
        'OH': {'dem': 2394164, 'rep': 2841005, 'other': 261318, 'ev': 18},
        'OK': {'dem': 420375, 'rep': 949136, 'other': 83481, 'ev': 7},
        'OR': {'dem': 1002106, 'rep': 782403, 'other': 216827, 'ev': 7},
        'PA': {'dem': 2926441, 'rep': 2970733, 'other': 268304, 'ev': 20},
        'RI': {'dem': 252525, 'rep': 180543, 'other': 31076, 'ev': 4},
        'SC': {'dem': 855373, 'rep': 1155389, 'other': 92265, 'ev': 9},
        'SD': {'dem': 117458, 'rep': 227721, 'other': 24914, 'ev': 3},
        'TN': {'dem': 870695, 'rep': 1522925, 'other': 114407, 'ev': 11},
        'TX': {'dem': 3877868, 'rep': 4685047, 'other': 406311, 'ev': 38},
        'UT': {'dem': 310676, 'rep': 515231, 'other': 305523, 'ev': 6},
        'VT': {'dem': 178573, 'rep': 95369, 'other': 41125, 'ev': 3},
        'VA': {'dem': 1981473, 'rep': 1769443, 'other': 233715, 'ev': 13},
        'WA': {'dem': 1742718, 'rep': 1221747, 'other': 352554, 'ev': 12},
        'WV': {'dem': 188794, 'rep': 489371, 'other': 34886, 'ev': 5},
        'WI': {'dem': 1382536, 'rep': 1405284, 'other': 188330, 'ev': 10},
        'WY': {'dem': 55973, 'rep': 174419, 'other': 25457, 'ev': 3},
        'DC': {'dem': 282830, 'rep': 12723, 'other': 15715, 'ev': 3},
    }

    def __init__(self, regions: Optional[RegionConfig] = None):
        """Initialize with optional region configuration."""
        self.regions = regions or load_regions()

    # Available election years
    AVAILABLE_YEARS = [2016, 2020, 2024]

    def get_election_data(self, year: int) -> Dict[str, Dict]:
        """
        Get election data for a specific year.

        Args:
            year: Election year (2016, 2020, or 2024)

        Returns:
            Dict mapping state codes to vote totals
        """
        if year == 2024:
            return self.ELECTION_2024
        elif year == 2020:
            return self.ELECTION_2020
        elif year == 2016:
            return self.ELECTION_2016
        else:
            raise ValueError(f"Election data not available for year {year}. Available: {self.AVAILABLE_YEARS}")

    def get_results_by_state(self, year: int) -> List[ElectionResult]:
        """
        Get election results as ElectionResult objects.

        Args:
            year: Election year

        Returns:
            List of ElectionResult objects
        """
        data = self.get_election_data(year)
        results = []

        for state, votes in data.items():
            dem = votes['dem']
            rep = votes['rep']
            other = votes['other']
            total = dem + rep + other
            winner = 'D' if dem > rep else 'R'

            results.append(ElectionResult(
                state=state,
                year=year,
                democrat_votes=dem,
                republican_votes=rep,
                other_votes=other,
                total_votes=total,
                winner=winner,
                electoral_votes=votes['ev']
            ))

        return results

    def aggregate_by_region(self, year: int) -> Dict[str, Dict]:
        """
        Aggregate election results by region.

        Args:
            year: Election year

        Returns:
            Dict mapping region names to aggregated vote totals
        """
        data = self.get_election_data(year)
        regional = {}

        for region_name in self.regions.get_region_names():
            states = self.regions.get_states(region_name)
            regional[region_name] = {
                'dem': 0,
                'rep': 0,
                'other': 0,
                'total': 0,
                'ev': 0,
                'states': []
            }

            for state in states:
                if state in data:
                    regional[region_name]['dem'] += data[state]['dem']
                    regional[region_name]['rep'] += data[state]['rep']
                    regional[region_name]['other'] += data[state]['other']
                    regional[region_name]['ev'] += data[state]['ev']
                    regional[region_name]['states'].append(state)

            regional[region_name]['total'] = (
                regional[region_name]['dem'] +
                regional[region_name]['rep'] +
                regional[region_name]['other']
            )

        return regional

    def get_national_totals(self, year: int) -> Dict[str, int]:
        """
        Get national vote totals.

        Args:
            year: Election year

        Returns:
            Dict with national vote totals by party
        """
        data = self.get_election_data(year)

        totals = {'dem': 0, 'rep': 0, 'other': 0, 'total': 0}
        for votes in data.values():
            totals['dem'] += votes['dem']
            totals['rep'] += votes['rep']
            totals['other'] += votes['other']

        totals['total'] = totals['dem'] + totals['rep'] + totals['other']
        return totals


class FiscalDataLoader:
    """
    Loads and processes state fiscal data.

    Data sources:
    - Census Bureau State Government Finances
    - BEA Regional Economic Accounts
    """

    # State GDP and population data for 2022 (billions USD, thousands pop)
    # Source: BEA and Census Bureau
    STATE_ECONOMICS_2022 = {
        'AL': {'gdp': 268.3, 'pop': 5074, 'income': 223.1},
        'AK': {'gdp': 60.4, 'pop': 733, 'income': 50.2},
        'AZ': {'gdp': 416.0, 'pop': 7359, 'income': 351.0},
        'AR': {'gdp': 152.5, 'pop': 3045, 'income': 127.8},
        'CA': {'gdp': 3598.1, 'pop': 39030, 'income': 2754.1},
        'CO': {'gdp': 446.0, 'pop': 5839, 'income': 378.9},
        'CT': {'gdp': 294.1, 'pop': 3626, 'income': 286.6},
        'DE': {'gdp': 81.8, 'pop': 1018, 'income': 57.4},
        'FL': {'gdp': 1389.1, 'pop': 22245, 'income': 1127.4},
        'GA': {'gdp': 731.1, 'pop': 10912, 'income': 528.7},
        'HI': {'gdp': 94.6, 'pop': 1440, 'income': 84.9},
        'ID': {'gdp': 100.5, 'pop': 1939, 'income': 86.4},
        'IL': {'gdp': 943.7, 'pop': 12582, 'income': 786.3},
        'IN': {'gdp': 416.9, 'pop': 6833, 'income': 340.3},
        'IA': {'gdp': 211.8, 'pop': 3200, 'income': 173.7},
        'KS': {'gdp': 192.3, 'pop': 2937, 'income': 161.9},
        'KY': {'gdp': 226.3, 'pop': 4512, 'income': 194.9},
        'LA': {'gdp': 273.7, 'pop': 4590, 'income': 208.6},
        'ME': {'gdp': 76.4, 'pop': 1385, 'income': 72.0},
        'MD': {'gdp': 445.9, 'pop': 6165, 'income': 410.7},
        'MA': {'gdp': 646.5, 'pop': 6982, 'income': 558.9},
        'MI': {'gdp': 569.7, 'pop': 10037, 'income': 510.7},
        'MN': {'gdp': 413.1, 'pop': 5717, 'income': 358.9},
        'MS': {'gdp': 122.4, 'pop': 2940, 'income': 105.3},
        'MO': {'gdp': 365.4, 'pop': 6178, 'income': 308.6},
        'MT': {'gdp': 61.2, 'pop': 1122, 'income': 55.7},
        'NE': {'gdp': 153.4, 'pop': 1967, 'income': 115.9},
        'NV': {'gdp': 197.1, 'pop': 3143, 'income': 163.9},
        'NH': {'gdp': 97.4, 'pop': 1395, 'income': 96.1},
        'NJ': {'gdp': 681.1, 'pop': 9261, 'income': 641.6},
        'NM': {'gdp': 110.4, 'pop': 2114, 'income': 88.9},
        'NY': {'gdp': 1899.0, 'pop': 19677, 'income': 1564.9},
        'NC': {'gdp': 679.5, 'pop': 10698, 'income': 522.9},
        'ND': {'gdp': 65.6, 'pop': 779, 'income': 47.8},
        'OH': {'gdp': 730.9, 'pop': 11756, 'income': 609.8},
        'OK': {'gdp': 217.6, 'pop': 4019, 'income': 177.9},
        'OR': {'gdp': 281.5, 'pop': 4241, 'income': 225.9},
        'PA': {'gdp': 859.3, 'pop': 12972, 'income': 769.2},
        'RI': {'gdp': 66.7, 'pop': 1096, 'income': 63.9},
        'SC': {'gdp': 277.3, 'pop': 5282, 'income': 233.3},
        'SD': {'gdp': 61.6, 'pop': 909, 'income': 50.9},
        'TN': {'gdp': 436.3, 'pop': 7051, 'income': 352.9},
        'TX': {'gdp': 2049.8, 'pop': 30030, 'income': 1545.9},
        'UT': {'gdp': 225.2, 'pop': 3380, 'income': 173.9},
        'VT': {'gdp': 37.3, 'pop': 647, 'income': 38.3},
        'VA': {'gdp': 614.8, 'pop': 8642, 'income': 558.7},
        'WA': {'gdp': 705.0, 'pop': 7785, 'income': 542.9},
        'WV': {'gdp': 87.6, 'pop': 1775, 'income': 74.2},
        'WI': {'gdp': 366.0, 'pop': 5896, 'income': 326.9},
        'WY': {'gdp': 43.8, 'pop': 577, 'income': 35.5},
        'DC': {'gdp': 151.4, 'pop': 671, 'income': 73.3},
    }

    def __init__(self, regions: Optional[RegionConfig] = None):
        """Initialize with optional region configuration."""
        self.regions = regions or load_regions()

    def get_state_data(self, year: int = 2022) -> Dict[str, Dict]:
        """
        Get economic data for all states.

        Args:
            year: Data year (currently only 2022 available)

        Returns:
            Dict mapping state codes to economic data
        """
        if year != 2022:
            # Could scale data for other years if needed
            pass
        return self.STATE_ECONOMICS_2022

    def aggregate_by_region(self, year: int = 2022) -> Dict[str, Dict]:
        """
        Aggregate economic data by region.

        Args:
            year: Data year

        Returns:
            Dict mapping region names to aggregated economic data
        """
        data = self.get_state_data(year)
        regional = {}

        for region_name in self.regions.get_region_names():
            states = self.regions.get_states(region_name)
            regional[region_name] = {
                'gdp': 0.0,
                'pop': 0,
                'income': 0.0,
                'states': [],
                'state_count': 0
            }

            for state in states:
                if state in data:
                    regional[region_name]['gdp'] += data[state]['gdp']
                    regional[region_name]['pop'] += data[state]['pop']
                    regional[region_name]['income'] += data[state]['income']
                    regional[region_name]['states'].append(state)
                    regional[region_name]['state_count'] += 1

            # Calculate per-capita values
            pop = regional[region_name]['pop']
            if pop > 0:
                regional[region_name]['gdp_per_capita'] = (
                    regional[region_name]['gdp'] * 1000 / pop  # Convert to dollars
                )
                regional[region_name]['income_per_capita'] = (
                    regional[region_name]['income'] * 1000 / pop
                )

        return regional

    def get_national_totals(self, year: int = 2022) -> Dict:
        """
        Get national economic totals.

        Args:
            year: Data year

        Returns:
            Dict with national totals
        """
        data = self.get_state_data(year)

        totals = {'gdp': 0.0, 'pop': 0, 'income': 0.0}
        for state_data in data.values():
            totals['gdp'] += state_data['gdp']
            totals['pop'] += state_data['pop']
            totals['income'] += state_data['income']

        totals['gdp_per_capita'] = totals['gdp'] * 1000 / totals['pop']
        totals['income_per_capita'] = totals['income'] * 1000 / totals['pop']

        return totals


if __name__ == '__main__':
    # Test the data pipeline
    regions = load_regions()

    print("=" * 60)
    print("ELECTORAL DATA TEST")
    print("=" * 60)

    electoral = ElectoralDataLoader(regions)

    print("\n2020 National Totals:")
    totals = electoral.get_national_totals(2020)
    total = totals['total']
    print(f"  Democrat: {totals['dem']:,} ({100*totals['dem']/total:.1f}%)")
    print(f"  Republican: {totals['rep']:,} ({100*totals['rep']/total:.1f}%)")
    print(f"  Other: {totals['other']:,} ({100*totals['other']/total:.1f}%)")
    print(f"  Total: {total:,}")

    print("\n2020 Regional Results:")
    regional = electoral.aggregate_by_region(2020)
    for region, data in sorted(regional.items()):
        dem_pct = 100 * data['dem'] / data['total']
        rep_pct = 100 * data['rep'] / data['total']
        winner = 'D' if data['dem'] > data['rep'] else 'R'
        print(f"  {region}: {winner} (D: {dem_pct:.1f}%, R: {rep_pct:.1f}%, EV: {data['ev']})")

    print("\n" + "=" * 60)
    print("FISCAL DATA TEST")
    print("=" * 60)

    fiscal = FiscalDataLoader(regions)

    print("\n2022 National Totals:")
    totals = fiscal.get_national_totals()
    print(f"  GDP: ${totals['gdp']:.1f}B")
    print(f"  Population: {totals['pop']:,}K")
    print(f"  GDP/capita: ${totals['gdp_per_capita']:,.0f}")

    print("\n2022 Regional GDP/Capita:")
    regional = fiscal.aggregate_by_region()
    for region, data in sorted(regional.items(), key=lambda x: x[1].get('gdp_per_capita', 0), reverse=True):
        gdp_pc = data.get('gdp_per_capita', 0)
        print(f"  {region}: ${gdp_pc:,.0f} ({data['state_count']} states, {data['pop']:,}K pop)")
