import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from abc import *
from Job.Job import Job


class DataCollector(Job):

    def __init__(self):
        pass

    def do_job(self):
        self.collect_data()

    @abstractmethod
    def collect_data(self):
        pass


class YouTubeDataCollector(DataCollector):

    def collect_data(self):
        self.collect_statistics_data()

    def collect_statistics_data(self):
        print("collect statistics")
        pass


class DataCollectorFactory:

    @classmethod
    def crate_data_collector(cls):
        return YouTubeDataCollector()

