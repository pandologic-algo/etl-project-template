import os
import json

# internal
from .. import __app_name__


# 3rd party
from dotenv import load_dotenv


# load env
load_dotenv('utils/.env')


class Config:
    def __init__(self, config_path):
        # env mode
        self.env_mode = os.getenv('APP_ENV')

        # config path
        self.config_path = config_path

        # load config file
        self._config = self._load_config()

        # App name
        self.app_name=__app_name__

        # App
        self.flask_app_config = self._config.get('flask_app_config')

        # logger config
        self.logger_config = self._config.get('logger_config')

        # scheduler config
        self.scheduler_config = self._config.get('scheduler_config')

        # etl config
        self.etl_config = self._config.get('etl_config')

        # reader config
        self.reader_config = self._config.get('reader_config')
        
        # writer config
        self.writer_config = self._config.get('writer_config')

    def _load_config(self):
        # load config file
        with open(self.config_path, 'r') as fp:
            if self.env_mode in ['Production']:
                config = json.load(fp)['Production']
            elif self.env_mode in ['Staging']:
                config = json.load(fp)['Staging']
            elif self.env_mode in ['Development']:
                config = json.load(fp)['Development']
        
        return config
