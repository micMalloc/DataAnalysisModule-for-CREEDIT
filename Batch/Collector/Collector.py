from Job import Job
from abc import *


class DataCollector(Job):
    
    _metaclass_=ABCMeta

    def doJob(self):
        self.collectData()

    @abstractmethod
    def collectData(self):
        pass


class YouTubeDataCollector(DataCollector):

    def collectData(self):
        pass