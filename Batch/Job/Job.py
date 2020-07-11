from abc import *


class Job(metaclass=ABCMeta):

    @abstractmethod
    def do_job(self):
        pass


class JobFactory:

    @classmethod
    def create_job(cls):
        from .Collector.Collector import DataCollectorFactory
        print("create data collector")
        return DataCollectorFactory.crate_data_collector()
