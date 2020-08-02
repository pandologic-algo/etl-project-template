import datetime
import json
import os
import sys

# internal
from ..settings import config
from ..app_logging import logger
from ..data_handling import Reader, Writer


class ETLWorker:
    # class properties
    min_date = datetime.date(2020, 6, 22)

    def __init__(self):
        """[summary]
        """
        # env mode
        self.env_mode = config.env_mode

        # etl properties
        

        # es reader
        self._reader = Reader(**config.reader_config)

        # s3 reader
        self._writer = Writer(**config.writer_config)

        logger.info('App - start app in mode: {}'.format(self.env_mode))

    def run(self):
        """The etl main run. 

        Returns:
            (bool): Return True if no exceptions were caught without handling.
        """

        try:

            logger.info('App - start app run')

            # do stuffs

        except Exception as e:
            logger.exception('App - crucial error in app:\n{}'.format(e))

            return False

        logger.info('App - app run is finished')

        return True
            