import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from sqlalchemy import Column, Integer,String
from Batch.Job.ORMInterface.Connection import s
from Batch.Job.ORMInterface.Connection import Base
from abc import *
from Batch.Job.Job import Job
from Batch.Log.Logger import Logger


class DataCollector(Job):

    def __init__(self):
        super().__init__()      
        self.logger.info("DataCollector created")

    def do_job(self):
        self.collect_data()

    @abstractmethod
    def collect_data(self):
        pass


class YouTubeDataCollector(DataCollector):

    def __init__(self, **kwargs):
        super().__init__()
        self.logger.info("YouTubeDataCollector created")

        try:
            self.method = kwargs['method']
        except Exception:
            # kwargs['method'] must not be None
            self.logger.critical('method is None')

    def collect_data(self):
        if self.method in 'statistics':
            self.collect_statistics_data()

    def collect_statistics_data(self):
        self.logger.info("collect statistics")
        # DB 어세스
        # 여기서 유투브 겟 정보를 --> DB 넣어야 될거 아니야
        pass


class DataCollectorFactory:

    @classmethod
    def crate_data_collector(cls, meta_data):
        if meta_data['domain'] in 'youtube':
            return YouTubeDataCollector(method=meta_data['method'])


class channeltable(Base):
    __tablename__="channels"
    idchannel = Column(Integer, primary_key=True)
    cid = Column(String(100))
    cname = Column(String(100))

    def __init__(self):
        pass
    def getchannel(self,s):
        channellist=[]
        for cid in s.query(channeltable.cid):
            channellist.append(cid)
        return channellist