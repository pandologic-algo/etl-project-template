import os
import json

# internal
from .secrets import secrets
from .config import Config


# config
config = Config(config_path='utils/config.json')