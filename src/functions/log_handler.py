import json
import logging.config
import pathlib

def setup_logging():
    config_file = pathlib.Path("config/config_logging.json")
    with open(config_file) as f_in:
        config = json.load(f_in)

    logging.config.dictConfig(config)
