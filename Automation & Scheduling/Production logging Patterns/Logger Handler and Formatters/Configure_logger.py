'''Task: Configure a logger that has two handlers:

A StreamHandler that shows INFO and higher level messages on the console.
A FileHandler that saves ERROR and higher level messages to a file named errors.log.
Use a different format for each handler.'''
import logging
#  create a logger
logger = logging.getLogger('dual_handle_logger')
logger.setLevel(logging.INFO)

# 1 - stream handler / console handler
s_handler = logging.StreamHandler()
s_format = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
s_handler.setFormatter(s_format)
logger.addHandler(s_handler)

# 2 -file handler 
f_handler = logging.FileHandler("error.log")
f_format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
f_handler.setLevel(logging.ERROR) # we need only ERROR log 
f_handler.setFormatter(f_format)
logger.addHandler(f_handler)

logger.info("Application is running smoothly.")
logger.warning("User attempted to access a restricted page.")
logger.error("Failed to write user session to cache.")


# Rotating logs 
from logging.handlers import RotatingFileHandler
import logging

logger = logging.getLogger("etl")
handler = RotatingFileHandler("etl.log", maxBytes=5*1024*1024, backupCount=3)
formatter = logging.Formatter("%(asctime)s [%(levelname)s] %(message)s")
handler.setFormatter(formatter)
logger.addHandler(handler)
logger.setLevel(logging.INFO)
