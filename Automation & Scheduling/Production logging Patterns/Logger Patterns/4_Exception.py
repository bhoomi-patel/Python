''' Exception Logging
When an error occurs, you must log the full traceback 
so you know exactly where in the code the error happened.'''

import logging
logger = logging.getLogger(__name__)

try:
    result = 1 / 0
except ZeroDivisionError:
    logger.error("An error occurred during calculation.") # Bad - no context!

try:
    result = 1 / 0
except ZeroDivisionError:
    logger.exception("An error occurred during calculation.") # GOOD - includes traceback!