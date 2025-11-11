'''Mini-Project: A Log-Ready FastAPI Application
This project ties everything together: dictConfig, JSON logging, and contextual logging in a real API.
install ---> pip install fastapi uvicorn python-json-logger
'''
import logging 
class RequestIdFilter(logging.Filter):
      # This is a dummy filter, in a real app you'd have a middleware to set this
      _request_id = 'default-id'
      def set_request_id(self,rid):
            RequestIdFilter._request_id = rid
      def filter(self,record):
            record.request_id = RequestIdFilter._request_id
LOGGING_CONFIG = {
      'version':1,
      'disable_existing_loggers':False,
      'filters':{
            'request_id':{
                  '()': RequestIdFilter,
            }
      },
      'formatters':{
            'json':{
                  'class': 'pythonjsonlogger.jsonlogger.JsonFormatter',
            'format': '%(asctime)s %(levelname)s %(name)s %(request_id)s %(message)s'
            },
      },
      'handlers':{
            'default':{
                  'level':'INFO',
                  'formatter':'json',
                  'class':'logging.StreamHandler',
                  'filters':['request_id'],
            },
      },
      'loggers':{
            '':{
                  'handlers':['default'],
                  'level':'INFO',
            }
      }
}
