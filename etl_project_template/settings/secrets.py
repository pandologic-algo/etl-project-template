import os
import json


# 3rd party
from dotenv import load_dotenv


# load env
load_dotenv('utils/.env')


# secrets
secrets = dict(LOGZIO_TOKEN=os.getenv('LOGZIO_TOKEN'))