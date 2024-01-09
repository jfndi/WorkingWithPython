"""
    logging1.py
    
    Created by Jean-François Ndi @ 09/01/2024
"""
import logging

#
# Setting the logging level to DEBUG tos ee all the messages.
#
logging.basicConfig(level=logging.DEBUG)

logging.debug("This is a debug message.")
logging.warning("This is a warning message.")
logging.info("This is an info message.")
