import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from abc import *
from Job.Job import Job
from Job.ORMInterface import updateStat


class DataCollector(Job):

    def __init__(self):
        super().__init__()      
        self.logger.info("DataCollector created")

    def do_job(self):
        self.collect_data()

    @abstractmethod
    def collect_data(self):
        pass


class YouTubeDataCollector(DataCollector):

    def __init__(self, **kwargs):
        super().__init__()
        self.logger.info("YouTubeDataCollector created")

        try:
            self.method = kwargs['method']
        except Exception:
            # kwargs['method'] must not be None
            self.logger.critical('method is None')

    def collect_data(self):
        if self.method in 'statistics':
            self.collect_statistics_data()

    def collect_statistics_data(self):
        self.logger.info("collect statistics")
        updateStat.main()


class DataCollectorFactory:

    @classmethod
    def crate_data_collector(cls, meta_data):
        if meta_data['domain'] in 'youtube':
            return YouTubeDataCollector(method=meta_data['method'])


