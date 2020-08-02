  
# 3rd party
from flask import Flask
from flask_restful import Api

# internal
from ..settings import config
from .resources import resources_mapping


# init flask app
flask_app = Flask(config.app_name)
api = Api(flask_app)

# # add api endpoint
for resource in resources_mapping:
    api.add_resource(resource.get('resource'), resource.get('route'))