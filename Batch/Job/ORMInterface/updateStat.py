from sqlalchemy import Column, Integer,String,DateTime
from Batch.Job.ORMInterface.DatabaseConnection import s
from Batch.Job.ORMInterface.DatabaseConnection import Base
from Batch.Job.Collector.Collector import channeltable

import urllib.request
import ssl
import json
from datetime import datetime

key = "AIzaSyC5didUPL_gr0qQmOSGkiTm-nTYAsyhF1s"
context = ssl._create_unverified_context()
now = datetime.now()
date = "{0}-{1}-{2}".format(now.year, now.month, now.day)

class stattable(Base):
    __tablename__="stat"

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
        self.time_stamp=time_stamp
        self.viewCount=viewCount
        self.subscriberCount=subscriberCount
        self.commentCount=commentCount
        self.hiddenSubscriberCount=hiddenSubscriberCount
        self.videoCount=videoCount

def update(s,channel_list):
    for channel in channel_list:
        data = urllib.request.urlopen("https://www.googleapis.com/youtube/v3/channels?part=statistics&id=" + channel[0] + "&key=" + key,context=context).read()
        stat = json.loads(data)["items"][0]["statistics"]
        t=stattable(channel, date, stat['viewCount'], stat['subscriberCount'], stat['commentCount'], stat['hiddenSubscriberCount'],stat['videoCount'])

        s.add(t)
        s.commit()

def main():

    ch = channeltable()
    channel_list = ch.getchannel(s)
    update(s,channel_list)
    s.close()

if __name__=="__main__":
    main()