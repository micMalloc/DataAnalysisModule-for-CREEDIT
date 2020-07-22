from sqlalchemy import Column, Integer,String
from Batch.Job.ORMInterface.DatabaseConnection import s
from Batch.Job.ORMInterface.DatabaseConnection import Base
from Batch.Job.ORMInterface.tableDefinition import channeltable

def getchannel(s):
    channellist=[]
    for cid in s.query(channeltable.cid):
        channellist.append(cid)
    return channellist

