from abc import *
from Job import Job

class DataAnalyzer(Job):

    _metaclass_=ABCMeta

    def doJob(self):
        self.analyzeData()

    @abstractmethod
    def analyzeData(self):
        pass