from abs import *
from Job import Job

class Analyzer(Job):

    _metaclass_=ABCMeta

    @abstractmethod
    def anlayze_data():
        pass