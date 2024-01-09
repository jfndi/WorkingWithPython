"""
    logging2.py
    
    Created by Jean-François Ndi @ 09/01/2024
"""
import logging

#
# Creates the my_logger logger. my_logger is a singleton, meaning that if we call again getLogger with the name
# my_logger, the same instance will be returned.
#
logger1 = logging.getLogger("my_logger")
logging.basicConfig()
logger1.setLevel(logging.INFO)
logger1.warning("This is a warning message.")
logger1.info("This is an info message.")
logger1.debug("This is a debug message.")
logger1.info("This is another info message.")
