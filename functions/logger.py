import logging
from datetime import datetime
from logging.handlers import TimedRotatingFileHandler
import os

def etl_logger(name:str):
    logger=logging.getLogger(name)

    os.makedirs('logs/',exist_ok=True)

    
    stream_handler = logging.StreamHandler()
    logger.addHandler(stream_handler)

    #Formatting handlers for 14 days interval
    file_handler = TimedRotatingFileHandler("logs/elt.log", when="midnight", interval=1, backupCount=0)

    #('Etl_app.log', when="D", interval=14, backupCount=3)
    logger.addHandler(file_handler)

    log_format = logging.Formatter(fmt='%(asctime)s - %(name)s - %(message)s', datefmt='%Y-%m-%d')
    
    stream_handler.setFormatter(log_format)        
    file_handler.setFormatter(log_format)

    logger.setLevel(logging.INFO)

    return logger        