"""
    logging6.py
    
    Created by Jean-François Ndi @ 09/01/2024

    Thos example shows how to configure a logger with a configuration file.
"""
import logging
import logging.config

import yaml

with open('logging6.config.yaml', 'r') as f:
    config = yaml.safe_load(f.read())
    logging.config.dictConfig(config)

logger = logging.getLogger('my_logger')

logger.error("This is an error message.")
logger.warning("This is a warning message.")
logger.info("This is an info message.")
logger.debug("This is a debug message.")
