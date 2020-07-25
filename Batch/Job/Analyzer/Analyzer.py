import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from abc import *
from Job.Job import Job
from Log.Logger import Logger
from Job.ORMInterface import updateStatistics

class DataAnalyzer(Job):

    def __init__(self):
        super().__init__()
        self.logger.info("DataAnalyzer created")

    def do_job(self):
        self.analyze_data()

    @abstractmethod
    def analyze_data(self):
        pass


class YouTubeDataAnalyzer(DataAnalyzer):
    
    def __init__(self, **kwargs):
        super().__init__()
        self.logger.info("YouTubeDataAnalyzer created")

        try:
            self.method = kwargs['method']
        except Exception:
            # kwargs['method'] must not be None
            self.logger.critical('method is None')

    def analyze_data(self):
        self.analyze_rate_of_change()

    def analyze_rate_of_change(self):
        self.logger.info("analyze rate_of_change")
        updateStatistics.main()


class DataAnalyzerFactory:

    @classmethod
    def create_data_analyzer(cls, meta_data):
        if meta_data['domain'] in 'youtube':
            return YouTubeDataAnalyzer(method=meta_data['method'])
