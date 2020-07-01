from abc import *
from Analyzer import Analyzer
from Collector import Collector


class Job(metaclass=ABCMeta):

    @abstractmethod
    def doJob(self):
        pass

if __name__ == "__main__":
    job = DataAnalyzer()