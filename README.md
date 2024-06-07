# Log Handler

Created a logging function that can be used in other files. See official Python logging [https://docs.python.org/3/library/logging.html](documentation) for extra guidance

## log_handler.py
Uses the Python logging module to create a logging instance. Imports JSON file with configuration settings.
If changes need to be made, change the config file


## log_handler_config.py
This file holds the configuration for the logger.
[https://www.youtube.com/watch?v=9L77QExPmI0](video) and [https://docs.python.org/3/library/logging.config.html#configuration-dictionary-schema](documentation) about logging with JSON file

### version
required and needs to be one for backwards compatability reasons.

### disable_existing_loggers
disables all other loggers not specified in this file. Think of loggers of imported modules.

### formatters
Allows for multiple formatting styles which can be used. See Python logging [https://docs.python.org/3.11/library/logging.html](documentation) for options


### handlers
Allows to create logging handlers. See Python logging handlers [https://docs.python.org/3/library/logging.handlers.html](documentation)