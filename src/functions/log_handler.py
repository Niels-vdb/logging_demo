import json
import logging.config
import pathlib

def log_handler():
    config_file = pathlib.Path("config/log_handler_config.json")
    with open(config_file) as f_in:
        config = json.load(f_in)

    logging.config.dictConfig(config)

