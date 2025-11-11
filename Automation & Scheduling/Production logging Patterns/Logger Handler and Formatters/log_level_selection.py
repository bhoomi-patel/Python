import logging
import random

logging.basicConfig(level=logging.DEBUG,format='%(levelname)s: %(message)s')
logger = logging.getLogger(__name__) #  automatically named after the module it is in -->  example: In myapp/api/users.py: __name__ is "myapp.api.users"

def process_user_request(user_id , request_data):
    # Debug: Detailed info useful during development
    logger.debug(f"Processing request : {request_data} for user {user_id}")

    if not request_data:
        # Warning: Something unexpected but not an error
        logger.warning(f"Empty request received from user {user_id}")
        return {"status" : "empty_request"}
    success = random.choice([True,True,False])
    if not success:
        # Error: Operation failed
        logger.error(f"Database error while processing request for user {user_id}")
        return {"status":"error" , "reason":"database_error"}
    logger.info(f"Successfully processed request for user {user_id}")
    return {"status":"success"}
process_user_request("user123",{"action": "update"})