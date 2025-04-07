import logging
import os
from logging.handlers import RotatingFileHandler

# if a custom environment is not set in the .env file the default logging 
# is set to development  
APP_ENV = os.getenv("ENVIRONMENT","development").lower()


def development_logs():
    """Configures logs for DEVELOPMENT environment"""
    logging.basicConfig(
        level=logging.DEBUG,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[
            logging.StreamHandler(),
        ]
    )
    logging.getLogger().debug("LOGGING SET TO DEVELOPMENT MODE")

def production_logs():
    """Configures logs for PRODUCTION environment"""
    os.makedirs('logs',exist_ok=True)

    logger = logging.getLogger()
    logger.setLevel = logging.INFO

    logfile = RotatingFileHandler('logs/app.log',maxBytes=1024 * 1024 * 20) # log file limit of 20MB
    logfile.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))

    console = logging.StreamHandler()
    console.setLevel(logging.ERROR)

    #handles log file in production
    logger.addHandler(logfile)
    logger.addHandler(console)
    logging.getLogger().info("LOGGING SET TO PRODUCTION MODE")

def setup_logging():
    if APP_ENV == "production":
        production_logs()
    else: 
        development_logs()