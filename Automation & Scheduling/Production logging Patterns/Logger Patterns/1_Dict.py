# 1: Configuration with a Dictionary (dictConfig)
'''Instead of creating objects in code, you define your entire logging setup in a Python dictionary. 
This is the standard for web frameworks like Django and FastAPI because it's clean, configurable, 
and can be loaded from a file (like a YAML or JSON file).'''
import logging
from logging.config import dictConfig
# Define the logging configuration using a dictionary
'''LOGGING_CONFIG = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'standard': {
            'format': '%(asctime)s [%(levelname)s] %(name)s: %(message)s'
        },
    },
    'handlers': {
        'default': {
            'level': 'INFO',
            'formatter': 'standard',
            'class': 'logging.StreamHandler',
            'stream': 'ext://sys.stdout',  # Important for Docker/services
        },
    },
    'loggers': {
        '': {  # root logger
            'handlers': ['default'],
            'level': 'INFO',
            'propagate': True
        }
    }
}

dictConfig(LOGGING_CONFIG)
logger = logging.getLogger(__name__)
logger.info("This was configured from a dictionary!")'''

# Task -->  Configure a logger that has two handlers: [../../Configure_logger.py]
'''
A StreamHandler that shows INFO and higher level messages on the console.
A FileHandler that saves ERROR and higher level messages to a file named errors.log.
Use a different format for each handler.'''

import logging
from logging.config import dictConfig
#  create a logger
logger = logging.getLogger('dual_handle_logger')
logger.setLevel(logging.INFO) 



LOGGING_CONFIG = {
    'version': 1,
    'formatters': {
        's_format': {'format': '%(name)s - %(levelname)s - %(message)s'},
        'f_format': {'format': '%(asctime)s - %(name)s - %(levelname)s - %(message)s'},
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 's_format',
            'level': 'INFO',
        },
        'file': {
            'class': 'logging.FileHandler',
            'formatter': 'f_format',
            'filename': '1_Dict_error.log',
            'level': 'ERROR',
        },
    },
    'loggers': {
        '': { # root logger
            'handlers': ['console', 'file'],
            'level': 'INFO',
        }
    }
}
# ... then call dictConfig(LOGGING_CONFIG)
dictConfig(LOGGING_CONFIG)
logger = logging.getLogger(__name__)
logger.info("This was configured from a dictionary!")
logger.warning("User attempted to access a restricted page.")
logger.error("Failed to write user session to cache.")