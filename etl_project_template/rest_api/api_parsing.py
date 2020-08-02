from flask_restful import reqparse, abort

# internal
from ..settings import config


TASKS = ['App Run', 'Ping']

def abort_if_task_doesnt_exist(task):
    if task not in TASKS:
        abort(404, message="Task {} doesn't exist".format(task))

# init parser
parser = reqparse.RequestParser()
parser.add_argument('task')
