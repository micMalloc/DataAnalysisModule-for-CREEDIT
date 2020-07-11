from abc import *
from .Analyzer.Analyzer import DataAnalyzer


class Job(metaclass=ABCMeta):

    @abstractmethod
    def doJob(self):
        pass


if __name__ == '__main__':
    job = DataAnalyzer()
