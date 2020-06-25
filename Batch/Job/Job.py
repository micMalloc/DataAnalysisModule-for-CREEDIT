from abs import *


class Job(metaclass=ABCMeta):
    
    @abstractmethod
    def do_job(self):
        pass