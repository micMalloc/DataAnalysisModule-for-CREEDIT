from sqlalchemy import Column, Integer,String,DateTime
from Batch.Job.ORMInterface.DatabaseConnection import s
from Batch.Job.ORMInterface.DatabaseConnection import Base
from Batch.Job.ORMInterface.tableDefinition import categorymaptable
from Batch.Job.ORMInterface.tableDefinition import stattable
from Batch.Job.ORMInterface.tableDefinition import statisticstable

from datetime import datetime, timedelta, date

CATEGORY = [
    1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14
]
END = 'end'
START = 'start'
data = {}
#class statisticstable(Base):
#    __tablename__="statistics"
#    def __init__(self):
#        pass



def calculate():
    target=datetime.now()
    end=date(target.year,target.month,target.day)#today
    target = datetime.now() - timedelta(days=11)
    start = date(target.year, target.month, target.day)#before 11


def trun():
    s.execute('''TRUNCATE TABLE statistics''')
    s.commit()

def joinCategorymapWithStat():
    categorymap=categorymaptable()
    stat=stattable()
    for cno, cid, date, views, subs in s.query(categorymap,stat).filter(categorymap.cid==stat.cid).filter(stat.time_stamp>=calculate().start).filter(stat.time_stamp<=calculate().end):
        print(cno,cid,date,views,subs)




def main():
    #trun()
    calculate()
    joinCategorymapWithStat()



if __name__=="__main__":
    main()


