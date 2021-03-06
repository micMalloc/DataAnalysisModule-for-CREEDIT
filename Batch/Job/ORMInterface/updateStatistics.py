'''
from Job.ORMInterface.DatabaseConnection import s
from Job.ORMInterface.tableDefinition import Statistics
from Job.ORMInterface.truncateTable import trun
from Job.ORMInterface.calculator import calculate
from Job.ORMInterface.joinTable import joinTable
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
            if row=='end':
                continue
            if row=='start':
                continue
            print(row, data[cno][channels[cno]][row])
            updatedata = {'idcategory': cno, 'time_stamp': row,'subscriberCount': data[cno][channels[cno]][row],'viewCount': 0}
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
'''

import pymysql
import os
import datetime
#from datetime import datetime,timedelta,date


def main():
    db_ip = str(os.environ['DB_IP_ADDRESS'])
    db_id = str(os.environ['DB_ID'])
    db_pw = str(os.environ['DB_PASSWORD'])



    creedit = pymysql.connect(host=db_ip, user=db_id, password=db_pw, db='db_creedit', charset='utf8')
    manager = creedit.cursor()

    CATEGORY = [
        1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14
    ]

    END = 'end'
    START = 'start'

    manager.execute("truncate table statistics")
    creedit.commit()

    data = {}

    for category in CATEGORY:
        data[category] = {}

    target = datetime.datetime.now()

    end = datetime.date(target.year, target.month, target.day)

    target = datetime.datetime.now() - datetime.timedelta(days=11)
    start = datetime.date(target.year, target.month, target.day)
    print(end,start)

    sql = "select categorymap.category_id, stat.cid, stat.time_stamp, stat.viewCount, stat.subscriberCount from categorymap join stat where categorymap.cid = stat.cid and stat.time_stamp between \'{0}\' and \'{1}\' order by stat.time_stamp".format(
        str(start), str(end))
    # sql = "select Category.category_id, stat.cid, stat.time_stamp, stat.viewCount, stat.subscriberCount from Category join stat where Category.cid = stat.cid and stat.time_stamp between \'{0}\' and \'{1}\' order by stat.time_stamp".format(str(start), str(end))
    manager.execute(sql)
    rows = manager.fetchall()

    for cno, cid, date, views, subs in rows:
        data[cno][cid] = {}
        data[cno][cid][END] = str(end)

    channel_id = ""
    category = 0

    for cno, cid, date, views, subs in rows:
        date = str(date)

        if category != cno:
            category = cno
            data[cno][cid][START] = str(date)

        if subs != 0:
            data[cno][cid][date] = subs
        else:
            data[cno][cid][date] = views

    delta = end - start
    channels = {}

    for cno in CATEGORY:
        dx = delta.days
        target_channel = ""
        val = 0

        for key in data[cno].keys():
            if START not in data[cno][key].keys():
                print(key)
                continue

            u = data[cno][key][START]
            v = data[cno][key][END]

            dy = data[cno][key][v] - data[cno][key][u]

            if target_channel is "":
                target_channel = key
                val = dy / dx
                continue

            if val <= (dy / dx):
                if val == (dy / dx):
                    if data[cno][target_channel][v] < data[cno][key][v]:
                        target_channel = key
                        val = dy / dx
                else:
                    target_channel = key
                    val = dy / dx

        channels[cno] = target_channel

    for cno in CATEGORY:
        if channels[cno] == "":
            continue

        sql = "select cname from channels where cid = \'{0}\'".format(channels[cno])
        manager.execute(sql)
        cname = manager.fetchall()[0][0]
        print(cno, cname)

        for row in data[cno][channels[cno]]:
            if row is END:
                continue
            if row is START:
                continue
            print(row, data[cno][channels[cno]][row])
            sql = "insert into statistics(category, time_stamp, subscriberCount, viewCount) values(%s, %s, %s, %s)"
            manager.execute(sql, (cno, row, data[cno][channels[cno]][row], 0))

    creedit.commit()
    creedit.close()

if __name__=="__main__":
    main()