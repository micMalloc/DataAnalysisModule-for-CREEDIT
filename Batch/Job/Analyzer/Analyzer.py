import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from abc import *
import Job.Job


class DataAnalyzer(Job):

    def __init__(self):
        pass

    def do_job(self):
        self.analyzeData()

    @abstractmethod
    def analyze_data(self):
        pass


class YouTubeDataAnalyzer(DataAnalyzer):
    
    def analyze_data(self):
        pass


class DataAnalyzerFactory:

    @classmethod
    def create_data_analyzer(cls, meta):
        pass
