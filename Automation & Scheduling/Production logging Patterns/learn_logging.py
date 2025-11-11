# - logging module records runtime events (info/warn/error), supports formats, handlers, rotation. Use logging to record events with timestamps + levels.
# - Logging is a way to track events that happen when your software runs.
# Level	    | value |     Detail             
# -------------------------------------------------------------------------
# DEBUG	    |   10  | Detailed information for diagnosing problems         
# INFO	    |   20  | Confirmation that things are working as expected         
# WARNING	|   30  | Indication that something unexpected happened                
# ERROR	    |   40  | An error occurred, but the software is still running          
# CRITICAL	|   50  | A serious error, the program may be unable to continue        

# example
import logging

logging.basicConfig(level=logging.DEBUG) # SET lowest level to capture all messages
logging.debug("This is a debug message. Useful for developers.")
logging.info("The application is starting up.")
logging.warning("The API rate limit is almost reached.")
logging.error("Failed to connect to the database.")
logging.critical("The entire system is down!")


# ----- Print vs Logging -----
# problem with print statements:
def divide(a,b):
    print(f"dividing {a} / {b}")
    if b==0:
        print(f"Error : division by zero!")
        return None
    res = a/b
    print(f"Result : {res}")
    return res
divide (4,0)

# Better with logging
import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def divide_logged(a,b):
    logger.info(f"dividing {a}/{b}")
    if b==0:
        logger.error("division by zero!")
        return None
    res = a/b
    logger.info(f"Result : {res}")
    return res 
divide_logged(10,0)  # INFO:__main__:dividing 10/0 , ERROR:__main__:division by zero!


# Write a script that simulates a function for processing payments. If the amount is less than $1000, 
# log an INFO message. If it's over $10,000, log a WARNING for manual review. If the payment gateway is "offline", log an ERROR.

import logging
logging.basicConfig(level=logging.INFO,format='%(levelname)s: %(message)s')
def process_payment(amount,gateway_status="online"):
    if gateway_status == "offline":
        logging.error(f"Cannot process ${amount} : Payment gateway is offline.")
        return
    logging.info(f"Processing payment for ${amount}")
    if amount > 10000:
        logging.warning(f"Payment of ${amount} is large and requires manual review")

process_payment(500)
process_payment(15000)