import sys
import traceback
from loguru import logger
import yaml
import os

DEFAULT_LOGGING_CONFIG = {
    'handlers': [
        {'sink': sys.stdout, 'level': 'INFO'},
    ],
    'extra': {}
}

def load_logging_config(config_file: str):
    """

    :param config_file:
    :return:
    """
    if os.path.exists(config_file):
        with open(config_file, 'r') as file:
            config = yaml.safe_load(file)
    else:
        config = DEFAULT_LOGGING_CONFIG
    return config

def setup_logger(config_file: str):
    config = load_logging_config(config_file)
    for handler in config['handlers']:
        if handler['sink'] == "sys.stdout":
            handler['sink'] = sys.stdout
    logger.configure(handlers=config['handlers'], extra=config.get('extra', {}))

def log_exception(exc_type, exc_value, exc_traceback):
    if issubclass(exc_type, KeyboardInterrupt):
        sys.__excepthook__(exc_type, exc_value, exc_traceback)
        return
    logger.error("Uncaught exception", exc_info=(exc_type, exc_value, exc_traceback))

# Initialize logger with configuration
setup_logger('logging_config.yaml')

# Set custom exception handler
sys.excepthook = log_exception

# Example usage
logger.info("Logger is configured and ready to use.")