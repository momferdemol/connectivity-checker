# epchecker/logger.py

import logging
import os
import sys


class LogFilter(logging.Filter):
    """Used by `initialize_logger` to redirect errors to `stderr`."""

    def filter(self, rec):
        return rec.levelno in (logging.DEBUG, logging.INFO, logging.WARNING)


class CustomFormatter(logging.Formatter):
    """Custom formatter for log records. Formats log messages with different
    colors based on the log level.
    """

    GREEN = "\x1b[38;5;76m"
    GREY = "\x1b[38;21m"
    YELLOW = "\x1b[38;5;226m"
    RED = "\x1b[38;5;196m"
    BOLD_RED = "\x1b[31;1m"
    RESET = "\x1b[0m"

    def __init__(self, fmt) -> None:
        super().__init__()
        self.fmt = fmt
        self.FORMATS = {
            logging.DEBUG: self.GREY + self.fmt + self.RESET,
            logging.INFO: self.GREEN + self.fmt + self.RESET,
            logging.WARNING: self.YELLOW + self.fmt + self.RESET,
            logging.ERROR: self.RED + self.fmt + self.RESET,
            logging.CRITICAL: self.BOLD_RED + self.fmt + self.RESET,
        }

    def format(self, record):
        log_fmt = self.FORMATS.get(record.levelno)
        formatter = logging.Formatter(log_fmt, datefmt="%Y-%m-%d %H:%M:%S")
        return formatter.format(record)


def initialize_logger() -> logging.Logger:
    """Initialize the logger."""
    levels = {
        "DEBUG": logging.DEBUG,
        "INFO": logging.INFO,
        "WARNING": logging.WARNING,
        "ERROR": logging.ERROR,
    }
    custom_name = "epchecker"

    env_lvl = os.getenv("LOGGER_LVL", "INFO").upper()

    # Mitigate non-existing value using try/except
    try:
        log_level = levels[env_lvl]
    except KeyError:
        msg = f"ERROR: LOGGER_LVL set to an invalid level: {env_lvl}"
        raise SystemExit(msg)

    logger = logging.getLogger(custom_name)

    log_fmt_string = "%(asctime)-19s %(name)s: [%(levelname)s] - %(message)s"
    formatter = CustomFormatter(fmt=log_fmt_string)

    stdout_handler = logging.StreamHandler(sys.stdout)
    stdout_handler.setLevel(logging.DEBUG)
    stdout_handler.addFilter(LogFilter())
    stdout_handler.setFormatter(formatter)

    stderr_handler = logging.StreamHandler(sys.stderr)
    stderr_handler.setLevel(logging.ERROR)
    stderr_handler.setFormatter(formatter)

    logger.propagate = False
    logger.addHandler(stdout_handler)
    logger.addHandler(stderr_handler)
    logger.setLevel(log_level)

    return logger


log: logging.Logger = initialize_logger()
