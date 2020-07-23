from sqlalchemy import Column, Integer,String
from Batch.Job.ORMInterface.DatabaseConnection import s
from Batch.Job.ORMInterface.DatabaseConnection import Base
from Batch.Job.ORMInterface.tableDefinition import Channels

def getchannel(s):
    channellist=[]
    for cid in s.query(Channels.cid):
        channellist.append(cid)
    return channellist

