from abc import *


class Job(metaclass=ABCMeta):
    
    @abstractmethod
    def doJob(self):
        pass