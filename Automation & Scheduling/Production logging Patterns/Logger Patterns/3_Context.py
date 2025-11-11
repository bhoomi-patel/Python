'''Contextual Logging
Automatically adding context-specific information to every log 
message generated during a request, such as a request_id or user_id.'''

import logging
import uuid
from logging.config import dictConfig

# 1. Define the Filter
class RequestIdFilter(logging.Filter):
    """
    This filter injects a new UUID into every log record.
    NOTE: In this simple form, it's a new ID per log, not per request.
    """
    def filter(self, record):
        record.request_id = str(uuid.uuid4())
        return True

# 2. Define the complete logging configuration dictionary
LOGGING_CONFIG = {
    'version': 1,
    'disable_existing_loggers': False,
    
    # Define the filter we created above
    'filters': {
        'request_id_filter': {  # Give the filter a name
            '()': RequestIdFilter,  # The '()' syntax creates an instance of the class
        }
    },
    
    # Define the format that will use our new 'request_id' field
    'formatters': {
        'standard': {
            'format': '%(asctime)s [%(levelname)s] %(name)s [rid:%(request_id)s]: %(message)s'
        }
    },
    
    # Define the handler that directs logs to the console
    'handlers': {
        'default': {
            'level': 'INFO',
            'formatter': 'standard',
            'class': 'logging.StreamHandler',
            'filters': ['request_id_filter'],  # Attach the filter to this handler
        }
    },
    
    # Define the logger which ties everything together
    'loggers': {
        '': {  # This is the root logger
            'handlers': ['default'],
            'level': 'INFO',
        }
    }
}

# 3. Apply the configuration
dictConfig(LOGGING_CONFIG)

# 4. Get a logger and use it
logger = logging.getLogger(__name__)
print("--- Logging with a new Request ID on every line ---")
logger.info("This was configured from a dictionary!")
logger.warning("User attempted to access a restricted page.")
logger.error("Failed to write user session to cache.")