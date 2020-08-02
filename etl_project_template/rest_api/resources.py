import time

from flask_restful import Resource

# internal
from ..etl import etl_worker
from ..settings import config
from ..app_logging import logger
from .api_parsing import parser, abort_if_task_doesnt_exist


class ETLRun(Resource):

    def get(self):
        # parse args
        args = parser.parse_args()

        # recieved datetime
        request_datetime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

        logger.info('{} - - {} "GET / HTTP/1.1" 200 - {}:'.format(config.flask_app_config.get('host'),
                                                                  config.flask_app_config.get('port'), 
                                                                  request_datetime, 
                                                                  args))

        # get task
        task = args.get('task')

        # check task 
        abort_if_task_doesnt_exist(task)
        
        if task == 'Ping':
            # ping task
            return {'response': 'Alive'}

        elif task == 'App Run':
            # check if succeed running task
            is_success = etl_worker.run()

            if not is_success:
                return {'response': 'fail'}

            return {'response': 'success'}


# resources
resources_mapping = [
    {'resource': ETLRun, 'route': '/{}/ETLRun'.format(config.app_name)}
]
