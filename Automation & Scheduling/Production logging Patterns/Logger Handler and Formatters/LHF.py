''' - Logger: The entry point. This is the object your application code interacts with (logger.info(...)). You can create multiple loggers (e.g., one for database, one for api).

    - Handler: The destination. This determines where the log message goes.
               StreamHandler: Prints to the console (standard output/error).
               FileHandler: Writes to a file on disk.
               Many others (e.g., SysLogHandler, HTTPHandler).
    - Formatter: The layout. This controls what the log message looks like. You can include the timestamp, log level, module name, and the message itself. '''

# example
import logging
# 1 - create a logger
logger = logging.getLogger('my_logger')  # Create a logger
logger.setLevel(logging.DEBUG) 
# 2 - create a handler ( we use file handler)
file_handler = logging.FileHandler('app.log')
file_handler.setLevel(logging.WARNING) # only write WARNING

# 3 - create a formatter
'''asctime stands for "ASCII time".
In a logging format string, %(asctime)s is a special placeholder that gets replaced with a human-readable timestamp, indicating the exact time the log message was created.'''
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# 4 - Add the formatter to the handler, and the handler to the logger
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

# --- Now use the logger ---
logger.info("This is an info message. It will NOT go to the file.")
logger.warning("Disk space is low. This WILL go to the file.")
logger.error("Database connection failed. This WILL also go to the file.")
