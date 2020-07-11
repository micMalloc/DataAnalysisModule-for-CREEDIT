import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from abc import *
from . import Job

class DataCollector(Job):
    
    _metaclass_=ABCMeta

    def __init__(self):
        pass

    def doJob(self):
        self.collectData()

    @abstractmethod
    def collectData(self):
        pass


class YouTubeDataCollector(DataCollector):

    def collectData(self):
        pass

    def collectStatisticsData(self):
        pass