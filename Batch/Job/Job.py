from abc import *
import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from Log.Logger import Logger

class Job(metaclass=ABCMeta):
    logger = None

    def __init__(self):
        self.logger = Logger.get_instance()
        pass

    @abstractmethod
    def do_job(self):
        pass


class JobFactory:

    @classmethod
    def create_job(cls):
        from .Collector.Collector import DataCollectorFactory
        print("create data collector")
        return DataCollectorFactory.crate_data_collector()
