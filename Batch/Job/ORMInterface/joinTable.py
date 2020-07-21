
from Batch.Job.ORMInterface.tableDefinition import Stat
from Batch.Job.ORMInterface.tableDefinition import Categorymap


CATEGORY = [
    1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14
]

class joinTable():

    def __init__(self):
        pass

    def joinCategorymapWithStat(self,s,end,start):
        data = {}
        for category in CATEGORY:
            data[category] = {}


        query = s.query(Categorymap.category_id, Stat.cid, Stat.time_stamp, Stat.viewCount,
                        Stat.subscriberCount).filter(Categorymap.cid == Stat.cid).filter(
            Stat.time_stamp >= start).filter(Stat.time_stamp <= end).order_by(Categorymap.category_id)

        for cno, cid, date, views, subs in query:
            data[cno][cid] = {}
            data[cno][cid]['end'] = str(end)

        category = 0

        for cno, cid, date, views, subs in query:
            date = str(date)

            if category != cno:
                category = cno
                data[cno][cid]['start'] = str(date)

            if subs != 0:
                data[cno][cid][date] = subs
            else:
                data[cno][cid][date] = views


        return data




