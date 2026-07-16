"""
ORI Command Line Interface.

Routes commands to ORI intelligence modules.
"""

import argparse

from ori.commands import analyze, health


def main() -> None:
    parser = argparse.ArgumentParser(
        prog="ori",
        description="ORI - Repository Intelligence Engine",
    )

    parser.add_argument(
        "--version",
        action="version",
        version="ORI 1.1.0",
    )

    subparsers = parser.add_subparsers(
        dest="command",
        help="Available commands",
    )

    # ---------------------------------------------------------------
    # Analyze Command
    # ---------------------------------------------------------------

    analyze_parser = subparsers.add_parser(
        "analyze",
        help="Run complete repository analysis",
    )

    analyze_parser.add_argument(
        "repository",
        help="GitHub repository URL to analyze",
    )

    # ---------------------------------------------------------------
    # Health Command
    # ---------------------------------------------------------------

    health_parser = subparsers.add_parser(
        "health",
        help="Analyze repository health",
    )

    health_parser.add_argument(
        "repository",
        help="GitHub repository URL to analyze",
    )

    args = parser.parse_args()

    # ---------------------------------------------------------------
    # Command Routing
    # ---------------------------------------------------------------

    if args.command == "analyze":
        analyze.run(args.repository)

    elif args.command == "health":
        health.run(args.repository)

    else:
        parser.print_help()


if __name__ == "__main__":
    main()