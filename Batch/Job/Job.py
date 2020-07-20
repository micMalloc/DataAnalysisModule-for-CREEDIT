from abc import *
import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from Log.Logger import Logger

class Job(metaclass=ABCMeta):
    logger = None

    def __init__(self):
        self.logger = Logger.get_instance().get_logger()
        self.logger.info('Job init')

    @abstractmethod
    def do_job(self):
        pass


class JobFactory:

    @classmethod
    def create_job(cls, meta_data):
        # TODO 직접적인 문자열 비교가 아닌 좀 더 추상적인 방식의 팩토리 메소드 구현 - ex) ENUM
        Logger.get_instance().get_logger().info('Job Factory')
        if meta_data['name'] in 'data_collect':
            from .Collector.Collector import DataCollectorFactory
            return DataCollectorFactory.crate_data_collector(meta_data)
        elif meta_data['name'] in 'data_analyze':
            from .Analyzer.Analyzer import DataAnalyzerFactory
            return DataAnalyzerFactory.create_data_analyzer(meta_data)
