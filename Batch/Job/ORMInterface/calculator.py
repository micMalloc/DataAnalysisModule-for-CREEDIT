from datetime import datetime, timedelta, date
CATEGORY = [
    1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14
]

class calculate():

    def __init__(self):
        pass

    def calcaulateTime(self,now):
        end = date(now.year, now.month, now.day)  # today
        target = datetime.now() - timedelta(days=11)
        start = date(target.year, target.month, target.day)  # before 11
        return end, start

    def calculateVariation(self,data,delta):
        channels = {}

        for cno in CATEGORY:
            dx = delta.days
            target_channel = ""
            val = 0

            for key in data[cno].keys():
                if 'start' not in data[cno][key].keys():
                    print(key)
                    continue

                u = data[cno][key]['start']
                v = data[cno][key]['end']

                dy = data[cno][key][v] - data[cno][key][u]

                if target_channel== "":
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
        return channels

