
from Batch.Job.ORMInterface.DatabaseConnection import s
from Batch.Job.ORMInterface.tableDefinition import Statistics
from Batch.Job.ORMInterface.truncateTable import trun
from Batch.Job.ORMInterface.calculator import calculate
from Batch.Job.ORMInterface.joinTable import joinTable
from datetime import datetime

now = datetime.now()
CATEGORY = [
    1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14
]
def updateStatistics(data,channels):
    for cno in CATEGORY:
        if channels[cno] == "":
            continue

        for row in data[cno][channels[cno]]:
            if row is 'end':
                continue
            if row is 'start':
                continue
            print(row, data[cno][channels[cno]][row])
            updatedata = {'category_id': cno, 'time_stamp': row,'subscriberCount': data[cno][channels[cno]][row],'viewCount': 0}
            statisitcsinstance = Statistics(**updatedata)
            s.add(statisitcsinstance)

    s.commit()
    s.close()

def main():

    t=trun()
    t.trunStatistics(s)

    c=calculate()
    end,start=c.calcaulateTime(now)

    j=joinTable()
    data=j.joinCategorymapWithStat(s,end,start)

    channels=c.calculateVariation(data,end-start)
    updateStatistics(data,channels)



if __name__=="__main__":
    main()


