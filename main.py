import logging.config
import logging.handlers

from src.functions import log_handler

logger = logging.getLogger(__name__)


def main():
    log_handler.log_handler()

    logger.debug("debug message")
    logger.info("info message")
    logger.warning("warning message")
    logger.error("error message")
    logger.critical("critical message")
    try:
        1 / 0
    except ZeroDivisionError:
        logger.exception("exception message")


if __name__ == "__main__":
    main()
