"""
    logging5.py
    
    Created by Jean-François Ndi @ 09/01/2024

    This example shows how to create a logger with multiple handlers.
"""
import logging
import os

logger = logging.getLogger('my_logger')
logger.setLevel(logging.DEBUG)
console_handler = logging.StreamHandler()
file_handler = logging.FileHandler('logs/logging5.log')

path = './logs'
if not os.path.exists(path):
    os.mkdir(path)

#
# Setting the logging levels at the handler level.
#
console_handler.setLevel(logging.DEBUG)
file_handler.setLevel(logging.INFO)

#
# Creating a separate formatter for two handlers.
#
console_formatter = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
file_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

#
# Adding formatter to handlers.
#
console_handler.setFormatter(console_formatter)
file_handler.setFormatter(file_formatter)

#
# Adding handlers to the logger.
#
logger.addHandler(console_handler)
logger.addHandler(file_handler)

logger.error("This is an error message.")
logger.warning("This is a warning message.")
logger.info("This is an info message.")
logger.debug("This is a debug message.")