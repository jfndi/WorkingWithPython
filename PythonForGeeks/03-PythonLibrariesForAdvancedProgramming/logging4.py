"""
    logging4.py
    
    Created by Jean-François Ndi @ 09/01/2024

    This example show how to use a file handler.
"""
import logging
import os.path

path = './logs'
if not os.path.exists(path):
    os.mkdir(path)

logging.basicConfig(filename='logs/logging4.log', level=logging.DEBUG)
logger = logging.getLogger('my_logger')
logger.setLevel(logging.DEBUG)
logger.warning("This is a warning message.")
logger.info("This is an info message.")
logger.debug("This is a debug message.")
