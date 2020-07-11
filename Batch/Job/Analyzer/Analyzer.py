import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from abc import *
import Job.Job


class DataAnalyzer(Job, metaclass=ABCMeta):

    def __init__(self):
        pass

    def doJob(self):
        self.analyzeData()

    @abstractmethod
    def analyzeData(self):
        pass
