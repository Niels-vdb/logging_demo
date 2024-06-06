import logging


class LoggerDemo:
    def sample_logger(self):
        # create logger
        logger = logging.getLogger(__name__)
        logger.setLevel(logging.DEBUG)

        # create console or file handler and set the log level
        console_handler = logging.StreamHandler()
        file_handler = logging.FileHandler("logs/app.log")

        # create formatter
        formatter = logging.Formatter(
            "%(asctime)s - %(name)s - %(levelname)s : %(message)s",
            datefmt="%d/%m/%Y %I:%M:%S %p",
        )

        # add formatter to file or console handler
        console_handler.setFormatter(formatter)
        file_handler.setFormatter(formatter)

        # add console handler to logger
        logger.addHandler(console_handler)
        logger.addHandler(file_handler)

        # application code
        logger.debug("This is a debug message")
        logger.info("This is an info message")
        logger.warning("This is a warning message")
        logger.error("This is an error message")
        logger.critical("This is a critical message")


ld = LoggerDemo()
ld.sample_logger()


# logging.basicConfig(
#     # Enables to show logging messages from a level or up
#     level=logging.DEBUG,
#     # file name where logs will be written to
#     filename="logs/app.log",
#     # Appends the new logs
#     filemode="a",
#     # Replaces old log file
#     # filemode="w",
#     format="%(asctime)s - %(levelname)s : %(message)s",
#     datefmt="%d/%m/%Y %I:%M:%S %p",
# )
