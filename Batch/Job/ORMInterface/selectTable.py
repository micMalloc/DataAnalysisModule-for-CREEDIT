from sqlalchemy import Column, Integer,String
from Job.ORMInterface.DatabaseConnection import s
from Job.ORMInterface.DatabaseConnection import Base
from Job.ORMInterface.tableDefinition import Channels

def getchannel(s):
    channellist=[]
    for cid in s.query(Channels.cid):
        channellist.append(cid)
    return channellist

