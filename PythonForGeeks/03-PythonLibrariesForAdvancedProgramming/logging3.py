"""
    logging3.py
    
    Created by Jean-François Ndi @ 09/01/2024

    In this example, we create a logger object using a built-in handler and a custom formatter.
"""
import logging

logger = logging.getLogger("my_logger")
#
# We can configure the logger in one call to basicConfig()
#
logging.basicConfig(handlers=[logging.StreamHandler()],
                    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
                    level=logging.INFO)
# or do it the long way as below.
#
#my_handler = logging.StreamHandler()
#my_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
#my_handler.setFormatter(my_formatter)
#logger.addHandler(my_handler)
#logger.setLevel(logging.INFO)
logger.warning("This is a warning message.")
logger.info("This is an info message.")
logger.debug("This is a debug message.")
