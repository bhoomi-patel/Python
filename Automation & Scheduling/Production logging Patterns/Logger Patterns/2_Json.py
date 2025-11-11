'''Structured Logging (JSON)
Logging messages as JSON objects instead of plain strings. This makes logs machine-readable,
which is essential for modern log analysis platforms (like Datadog, Splunk, Elasticsearch).'''
# library use -> pip install python-json-logger

# Structured Logging with JSON Example
import logging
from logging.config import dictConfig
from pythonjsonlogger import jsonlogger  # Make sure you've installed this with pip

# Define the logging configuration dictionary
LOGGING_CONFIG = {
    'version': 1,  # Required by dictConfig
    'disable_existing_loggers': False,  # Don't disable existing loggers
    
    'formatters': {
        'json': {
            'class': 'pythonjsonlogger.jsonlogger.JsonFormatter',
            'format': '%(asctime)s %(levelname)s %(name)s %(message)s'
        },
    },
    
    'handlers': {
        'default': {
            'level': 'INFO',
            'formatter': 'json',  # Use the json formatter
            'class': 'logging.StreamHandler',
        },
    },
    
    'loggers': {
        '': {  # Root logger
            'handlers': ['default'],
            'level': 'INFO',
        }
    }
}

# Apply the configuration
dictConfig(LOGGING_CONFIG)

# Get a logger for the current module
logger = logging.getLogger(__name__)

# Log some messages
logger.info("This was configured from a dictionary!")
logger.warning("User attempted to access a restricted page.")
logger.error("Failed to write user session to cache.")

# You can also include additional data as key-value pairs
logger.info("User logged in", extra={
    "user_id": 12345,
    "ip_address": "192.168.1.1",
    "browser": "Chrome"
})

# Example of error with exception information
try:
    result = 1 / 0
except ZeroDivisionError as e:
    logger.error("A calculation error occurred", 
                extra={"operation": "division", "error_type": "ZeroDivisionError"}, 
                exc_info=True)


