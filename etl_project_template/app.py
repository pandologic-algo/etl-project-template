import os
import sys

# import project path
sys.path.append(os.path.join(os.getcwd()))

# internal 
from etl_project_template.settings import config
from etl_project_template.app_logging import logger
from etl_project_template.rest_api import flask_app
from etl_project_template.scheduling import scheduler


if __name__ == '__main__':
    # start scheduler
    scheduler.start()

    # run flask app                                                                
    flask_app.run(**config.flask_app_config)

    # shutdown log
    logger.info("Flask {} API is down!".format(config.app_name))