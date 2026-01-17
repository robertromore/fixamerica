"""
Regional Federalism Simulation Suite - Unified CLI Runner.

Usage:
    python -m src --all                     # Run all simulations
    python -m src --presidential 2016 2020  # Run specific presidential years
    python -m src --house 2020              # Run House allocation sim
    python -m src --senate 2020             # Run Senate composition sim
    python -m src --fiscal                  # Run fiscal analysis
    python -m src --convergence 20          # Run N-year convergence projection
    python -m src --output ./reports        # Specify output directory
"""

import argparse
import sys
from pathlib import Path
from typing import List, Optional


def run_presidential(years: List[int], output_dir: Path) -> None:
    """Run presidential election simulations."""
    from .electoral.presidential import PresidentialSimulator

    sim = PresidentialSimulator()
    output_dir.mkdir(parents=True, exist_ok=True)

    for year in years:
        print(f"\n{'='*60}")
        print(f"PRESIDENTIAL SIMULATION: {year}")
        print('='*60)

        try:
            report = sim.compare_systems(year)
            print(report)

            # Write report
            output_file = output_dir / f"presidential_{year}_analysis.md"
            output_file.write_text(report)
            print(f"\nReport written to: {output_file}")

        except ValueError as e:
            print(f"Error: {e}")
            continue

    # Multi-year comparison if multiple years
    if len(years) > 1:
        print(f"\n{'='*60}")
        print("MULTI-YEAR PRESIDENTIAL COMPARISON")
        print('='*60)

        comparison = sim.multi_year_comparison(years)
        print(comparison)

        output_file = output_dir / "presidential_comparison.md"
        output_file.write_text(comparison)
        print(f"\nComparison report written to: {output_file}")


def run_house(years: List[int], output_dir: Path) -> None:
    """Run House seat allocation simulations."""
    from .electoral.house import HouseSimulator

    sim = HouseSimulator()
    output_dir.mkdir(parents=True, exist_ok=True)

    for year in years:
        print(f"\n{'='*60}")
        print(f"HOUSE ALLOCATION SIMULATION: {year}")
        print('='*60)

        try:
            report = sim.generate_report(year)
            print(report)

            output_file = output_dir / f"house_{year}_analysis.md"
            output_file.write_text(report)
            print(f"\nReport written to: {output_file}")

        except ValueError as e:
            print(f"Error: {e}")
            continue


def run_senate(years: List[int], output_dir: Path) -> None:
    """Run Senate composition simulations."""
    from .electoral.senate import SenateSimulator

    sim = SenateSimulator()
    output_dir.mkdir(parents=True, exist_ok=True)

    for year in years:
        print(f"\n{'='*60}")
        print(f"SENATE COMPOSITION SIMULATION: {year}")
        print('='*60)

        try:
            report = sim.generate_report(year)
            print(report)

            output_file = output_dir / f"senate_{year}_analysis.md"
            output_file.write_text(report)
            print(f"\nReport written to: {output_file}")

        except ValueError as e:
            print(f"Error: {e}")
            continue


def run_fiscal(output_dir: Path) -> None:
    """Run fiscal capacity and equalization analysis."""
    from .fiscal.capacity import FiscalCapacityCalculator
    from .fiscal.equalization import EqualizationCalculator

    output_dir.mkdir(parents=True, exist_ok=True)

    # Fiscal capacity
    print(f"\n{'='*60}")
    print("FISCAL CAPACITY ANALYSIS")
    print('='*60)

    cap_calc = FiscalCapacityCalculator()
    cap_report = cap_calc.generate_report()
    print(cap_report)

    output_file = output_dir / "fiscal_capacity_baseline.md"
    output_file.write_text(cap_report)
    print(f"\nReport written to: {output_file}")

    # Equalization transfers
    print(f"\n{'='*60}")
    print("EQUALIZATION TRANSFER ANALYSIS")
    print('='*60)

    eq_calc = EqualizationCalculator()
    eq_report = eq_calc.generate_report()
    print(eq_report)

    output_file = output_dir / "equalization_transfers.md"
    output_file.write_text(eq_report)
    print(f"\nReport written to: {output_file}")


def run_convergence(projection_years: int, output_dir: Path) -> None:
    """Run fiscal convergence projection."""
    from .fiscal.convergence import ConvergenceProjector

    output_dir.mkdir(parents=True, exist_ok=True)

    print(f"\n{'='*60}")
    print(f"{projection_years}-YEAR CONVERGENCE PROJECTION")
    print('='*60)

    projector = ConvergenceProjector()
    report = projector.generate_report(projection_years=projection_years)
    print(report)

    output_file = output_dir / f"convergence_{projection_years}yr_projection.md"
    output_file.write_text(report)
    print(f"\nReport written to: {output_file}")


def main():
    """Main entry point for the simulation suite."""
    parser = argparse.ArgumentParser(
        description='Regional Federalism Simulation Suite',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python -m src --all                     Run all simulations
  python -m src --presidential 2016 2020  Presidential analysis for specific years
  python -m src --house 2020 2024         House allocation analysis
  python -m src --senate 2020             Senate composition analysis
  python -m src --fiscal                  Fiscal capacity and equalization
  python -m src --convergence 20          20-year convergence projection
  python -m src --output ./my-reports     Custom output directory
        """
    )

    parser.add_argument(
        '--presidential',
        nargs='*',
        type=int,
        metavar='YEAR',
        help='Run presidential election simulation for specified years (2016, 2020, 2024)'
    )
    parser.add_argument(
        '--house',
        nargs='*',
        type=int,
        metavar='YEAR',
        help='Run House seat allocation simulation for specified years'
    )
    parser.add_argument(
        '--senate',
        nargs='*',
        type=int,
        metavar='YEAR',
        help='Run Senate composition simulation for specified years'
    )
    parser.add_argument(
        '--fiscal',
        action='store_true',
        help='Run fiscal capacity and equalization analysis'
    )
    parser.add_argument(
        '--convergence',
        type=int,
        metavar='YEARS',
        help='Run N-year fiscal convergence projection'
    )
    parser.add_argument(
        '--all',
        action='store_true',
        help='Run all simulations with default parameters'
    )
    parser.add_argument(
        '--output',
        type=str,
        default='outputs/reports',
        help='Output directory for reports (default: outputs/reports)'
    )
    parser.add_argument(
        '--quiet',
        action='store_true',
        help='Suppress console output (still writes files)'
    )

    args = parser.parse_args()

    # If no simulation specified, show help
    if not any([args.presidential is not None, args.house is not None,
                args.senate is not None, args.fiscal, args.convergence, args.all]):
        parser.print_help()
        return

    # Resolve output directory
    output_dir = Path(args.output)

    print("=" * 60)
    print("REGIONAL FEDERALISM SIMULATION SUITE")
    print("=" * 60)
    print(f"Output directory: {output_dir.absolute()}")

    # Run requested simulations
    if args.all:
        # Run everything with defaults
        default_years = [2016, 2020, 2024]

        run_presidential(default_years, output_dir)
        run_house(default_years, output_dir)
        run_senate(default_years, output_dir)
        run_fiscal(output_dir)
        run_convergence(20, output_dir)

    else:
        # Run specific simulations
        if args.presidential is not None:
            years = args.presidential if args.presidential else [2020]
            run_presidential(years, output_dir)

        if args.house is not None:
            years = args.house if args.house else [2020]
            run_house(years, output_dir)

        if args.senate is not None:
            years = args.senate if args.senate else [2020]
            run_senate(years, output_dir)

        if args.fiscal:
            run_fiscal(output_dir)

        if args.convergence:
            run_convergence(args.convergence, output_dir)

    print("\n" + "=" * 60)
    print("SIMULATION COMPLETE")
    print("=" * 60)
    print(f"Reports saved to: {output_dir.absolute()}")


if __name__ == '__main__':
    main()
