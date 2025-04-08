import logging
import os
from logging.handlers import RotatingFileHandler

# if a custom environment is not set in the .env file the default logging 
# is set to development  
APP_ENV = os.getenv("ENVIRONMENT","development").lower()

def setup_logging():
    logger = logging.getLogger("devcontainer_generator")
    logger.setLevel(logging.DEBUG if APP_ENV == "development" else logging.INFO)

    logger.handlers = []

    format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    #console handler
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(format)

    if APP_ENV == "development":
        console_handler.setLevel(logging.DEBUG)
        logging.getLogger("devcontainer_generator").debug("LOGGING STARTED IN DEVELOPMENT MODE")
    else:
        console_handler.setLevel(logging.WARNING)
        logging.getLogger("devcontainer_generator").warning("LOGGING STARTED IN PRODUCTION MODE")


    logger.addHandler(console_handler)

    if APP_ENV == "production":
        os.makedirs('logs',exist_ok=True)
        file_handler = logging.FileHandler('logs/app.log')
        file_handler.setFormatter(format)
        file_handler.setLevel(logging.INFO)
        logger.addHandler(file_handler)
        
    