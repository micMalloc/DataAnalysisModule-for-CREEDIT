import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from Job.Job import Job
from abc import *


class DataAnalyzer(Job):

    _metaclass_=ABCMeta

    def __init__(self):
        pass

    def doJob(self):
        self.analyzeData()

    @abstractmethod
    def analyzeData(self):
        pass