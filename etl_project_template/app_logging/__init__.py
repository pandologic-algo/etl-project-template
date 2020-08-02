# internal
from ..settings import config
from ..app_logging.logger import Logger


__all__ = ['logger']


# logger
logger = Logger.create_logger(name=config.app_name, config=config.logger_config)
