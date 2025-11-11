import logging
import uuid 
from logging.config import dictConfig
from fastapi import FastAPI ,Request

# Import and apply  logging config
from logging_config import LOGGING_CONFIG ,RequestIdFilter
dictConfig(LOGGING_CONFIG)

app=FastAPI()
logger = logging.getLogger(__name__)
request_id_filter = RequestIdFilter() # Get instance of our filter

@app.middleware("http")
async def add_request_id(request:Request , call_next):
     # Assign a unique ID to each request
     request_id=str(uuid.uuid4())
     request_id_filter.set_request_id(request_id) #set it on our filter

     logger.info(f"Request started for path : {request.url.path}")
     response = await call_next(request)
     logger.info("Request finished .")
     return response
@app.get("/")
def read_root():
     logger.info("Processing request for the root endpoint.")
     return {"message" : "Hello World"}
@app.get("/error")
def trigger_error():
    try:
          res = 1/0
    except Exception:
          logger.exception("An unhandled exception occurred.")
          return {"message":"An error occured!"}
    return {}

# to Run -->uvicorn main:app --reload