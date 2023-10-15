# epchecker/__main__.py

import pathlib
import sys

from epchecker.checker import site_is_online
from epchecker.cli import display_check_result, read_user_cli_args
from epchecker.logger import log


def main():
    """Run endpoint checker."""

    user_args = read_user_cli_args()
    urls = _get_endpoint_urls(user_args)
    if not urls:
        log.error("No URLs provided")
        sys.exit(1)
    _synchronous_check(urls)


def _get_endpoint_urls(user_args):
    urls = user_args.url
    if user_args.input_file:
        urls += _read_urls_from_file(user_args.input_file)
    return urls


def _read_urls_from_file(file):
    file_path = pathlib.Path(file)
    if file_path.is_file():
        with file_path.open() as urls_file:
            urls = [url.strip() for url in urls_file]
            if urls:
                return urls
            log.error(f"Empty input file, {file}")
    else:
        log.error("Input file not found")
    return []


def _synchronous_check(urls: str):
    for url in urls:
        error = ""
        try:
            result = site_is_online(url)
        except Exception as err:
            result = False
            error = str(err)
        display_check_result(result, url, error)


if __name__ == "__main__":
    main()
