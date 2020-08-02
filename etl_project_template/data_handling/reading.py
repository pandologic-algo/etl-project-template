import datetime
import gzip
from io import BytesIO
import json
import os
import time

# internal
from ..settings import config, secrets
from ..app_logging import logger


class Reader:

    def __init__(self, arg=None):
        """[info]

        Args:
            arg ([type]): [info]
        """
        # env mode
        self.env_mode = config.env_mode

        # arguments
        self.arg = arg

    def func(self, arg=None):
        """[info]

        Args:
            arg ([type]): [info]

        Returns:
            result ([type]): [info]
        """
        result = arg

        return result

    def _private_func(self, arg=None):
        """[info]

        Args:
            arg ([type]): [info]

        Returns:
            result ([type]): [info]
        """
        result = arg

        return result
