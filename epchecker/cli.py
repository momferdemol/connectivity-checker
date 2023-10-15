# epchecker/cli.py

import argparse
from typing import Any

from epchecker.logger import log


def read_user_cli_args() -> Any:
    """Handle the CLI arguments and options."""

    parser = argparse.ArgumentParser(
        prog="epchecker", description="Check the availability of endpoints"
    )
    parser.add_argument(
        "-u",
        "--url",
        metavar="URLs",
        nargs="+",
        type=str,
        default=[],
        help="Enter one or more endpoint URLs",
    )
    parser.add_argument(
        "-f",
        "--input-file",
        metavar="FILE",
        type=str,
        default="",
        help="Read URLs from a file",
    )
    parser.add_argument(
        "-a",
        "--asynchronous",
        action="store_true",
        help="Run the connectivity check asynchronously",
    )

    return parser.parse_args()


def display_check_result(result: bool, url: str, error: str) -> None:
    """Display the result of a connectivity check."""

    if result:
        log.info(f"The status of '{url}' is: OK ")
    else:
        log.error(f"The status of '{url}' is: NOT OK \n '{error}' ")
