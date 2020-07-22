from sqlalchemy import Table,Column, Integer,String,DateTime
from Batch.Job.ORMInterface.DatabaseConnection import s
from Batch.Job.ORMInterface.DatabaseConnection import Base
from Batch.Job.ORMInterface.DatabaseConnection import engine
from datetime import datetime

#auto increment..?
# select하지 않아도 mapping이 되야 하는 거 아닌가.
class stattable(Base):
    __tablename__=Table("stat",Base.metadata,autoload=True,autoload_with=engine)
    ##__tablename__="stat"

    idstat=Column(Integer,primary_key=True)
    cid= Column(String(50))
    time_stamp = Column(DateTime)
    viewCount = Column(Integer)
    subscriberCount = Column(Integer)
    commentCount = Column(Integer)
    hiddenSubscriberCount=Column(Integer)
    videoCount=Column(Integer)

    def __init__(self,cid,time_stamp,viewCount,subscriberCount,commentCount,hiddenSubscriberCount,videoCount):
        self.cid=cid
        print("here", cid)
        self.time_stamp=time_stamp
        self.viewCount=viewCount
        self.subscriberCount=subscriberCount
        self.commentCount=commentCount
        self.hiddenSubscriberCount=hiddenSubscriberCount
        self.videoCount=videoCount

class categorymaptable(Base):
    #__tablename__="categorymap"
    __tablename__ = Table("categorymap", Base.metadata, autoload=True, autoload_with=engine)

    id=Column(Integer,primary_key=True)
    cid= Column(String(50))
    category_id=Column(Integer)

    def __init__(self,cid,category_id):
        self.cid=cid
        self.category_id=category_id

class statisticstable(Base):
    #__tablename__="statistics"
    __tablename__ = Table("statistics", Base.metadata, autoload=True, autoload_with=engine)

    id=Column(Integer,primary_key=True)
    category_id=(Integer)
    time_stamp = Column(DateTime)
    subscriberCount = Column(Integer)
    viewCount = Column(Integer)

    def __init__(self,category_id,time_stamp,subscriberCount,viewCount):
        self.category_id=category_id
        self.time_stamp = time_stamp
        self.subscriberCount=subscriberCount
        self.viewCount=viewCount

class channeltable(Base):
    #__tablename__="channels"
    __tablename__ = Table("channels", Base.metadata, autoload=True, autoload_with=engine)
    idchannel = Column(Integer, primary_key=True)
    cid = Column(String(100))
    cname = Column(String(100))

    def __init__(self,cid,cname):
        self.cid=cid
        self.cname=cname

