import datetime
import logging
import os

# 3rd party
from logzio.handler import LogzioHandler
from ..settings import secrets
    


class LoggingStreamHandler:
    @staticmethod
    def get_handler(log_format, logging_level):
        handler = logging.StreamHandler()
        handler.setLevel(logging.getLevelName(logging_level))
        formatter = logging.Formatter(log_format)
        handler.setFormatter(formatter)

        return handler


class LoggingLogzioHandler:
    @staticmethod
    def get_handler(url, log_format, logging_level, debug_mode):
        token = secrets.get('LOGZIO_TOKEN')

        handler = LogzioHandler(token=token, url=url, debug=debug_mode)
        handler.setLevel(logging.getLevelName(logging_level))
        formatter = logging.Formatter(log_format)
        handler.setFormatter(formatter)

        return handler


class LoggingFileHandler:
    _file_suffix_date_format = "%Y%m%d%H%M%S"

    @classmethod
    def get_handler(cls, output_dir, log_format, logging_level):
        timestamp = datetime.datetime.now().strftime(cls._file_suffix_date_format)

        file_name = timestamp + "_{}.log".format(logging_level.lower())

        file_path = os.path.join(output_dir, file_name)
        handler = logging.FileHandler(file_path, "w", encoding=None, delay="true")
        handler.setLevel(logging.getLevelName(logging_level))
        formatter = logging.Formatter(log_format)
        handler.setFormatter(formatter)

        return handler


handlers_mapping = dict(logging_stream_handler=LoggingStreamHandler,
                        logging_file_handler=LoggingFileHandler,
                        logging_logzio_handler=LoggingLogzioHandler)
