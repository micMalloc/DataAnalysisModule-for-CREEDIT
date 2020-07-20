import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from abc import *
from Job.Job import Job
from Log.Logger import Logger


class DataCollector(Job):

    def __init__(self):
        super().__init__()      
        self.logger.info("DataCollector init")

    def do_job(self):
        self.collect_data()

    @abstractmethod
    def collect_data(self):
        pass


class YouTubeDataCollector(DataCollector):

    def __init__(self):
        super().__init__()
        self.logger.info("YouTubeDataCollector init")

    def collect_data(self):
        self.collect_statistics_data()

    def collect_statistics_data(self):
        self.logger.info("collect statistics")
        pass


class DataCollectorFactory:

    @classmethod
    def crate_data_collector(cls):
        return YouTubeDataCollector()

