import socket

# 3rd party
from apscheduler.schedulers.background import BackgroundScheduler
import requests

# internal
from ..settings import config
from ..app_logging import logger


class Scheduler:
    @classmethod
    def get_scheduler(cls):
        """[summary]
        Returns:
            [type]: [description]
        """
        # scheduler
        scheduler = BackgroundScheduler()

        # app address
        host, port = config.flask_app_config.get('host'), config.flask_app_config.get('port')

        for schedule in config.scheduler_config:
            # resource route
            route = '/{}'.format(config.app_name) + '/' + schedule.get('resource')

            # schedule task
            schedule_task = schedule.get('task')

            # run task args
            args = (host, port, route , schedule_task)

            # schedule config
            schedule_config = schedule.get('schedule')
        
            # add schedule jobs
            scheduler.add_job(cls.job_run_task, args=args, trigger='cron', **schedule_config)

        cls.log_scheduler_jobs(scheduler)

        return scheduler

    @staticmethod
    def job_run_task(host, port, route, task):
        """[summary]
        Args:
            host ([type]): [description]
            port ([type]): [description]
            route ([type]): [description]
            task ([type]): [description]
        """
        if host == '0.0.0.0':
            host = socket.gethostbyname(socket.gethostname())

        address = 'http://' + host + ':' + str(port) + '/' + route

        response = requests.get(address, data={'task': task}).json().get('response')

        logger.info("Scheduler - task response: {}".format(response))

    @staticmethod
    def log_scheduler_jobs(scheduler):
        """[summary]
        Args:
            scheduler ([type]): [description]
        """
        jobs_info = [str(job) for job in scheduler.get_jobs()]

        logger.info("Scheduler - Pending jobs: {}".format(jobs_info))