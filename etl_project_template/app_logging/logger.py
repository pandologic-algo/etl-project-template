import logging

# internal
from ..app_logging.handlers import handlers_mapping


class Logger:
    @classmethod
    def create_logger(cls, name, config):
        """[summary]
        Args:
            name ([type]): [description]
            config ([type]): [description]
        Returns:
            [type]: [description]
        """
        logger = logging.getLogger(name)

        # logging level
        logging_level = config.get('logger').get('logging_level')
        cls.set_logger_level(logger, logging_level)

        for handler in config.get('handlers'):
            handler_type = handler.get('type') 
            handler_config = handler.get('config')

            handler = handlers_mapping.get(handler_type).get_handler(**handler_config)

            logger.addHandler(handler)

        return logger

    @staticmethod
    def set_logger_level(logger, level):
        """[summary]
        Args:
            logger ([type]): [description]
            level ([type]): [description]
        """
        logger.setLevel(logging.getLevelName(level))
