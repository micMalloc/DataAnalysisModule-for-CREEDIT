
from Batch.Job.ORMInterface.tableDefinition import stattable
from Batch.Job.ORMInterface.DatabaseConnection import s
from Batch.Job.ORMInterface.selectTable import getchannel

import urllib.request
import ssl
import json
from datetime import datetime

key = "AIzaSyC5didUPL_gr0qQmOSGkiTm-nTYAsyhF1s"
context = ssl._create_unverified_context()
now = datetime.now()
date = "{0}-{1}-{2}".format(now.year, now.month, now.day)

def updateStat(s,channel_list):
    for channel in channel_list:
        data = urllib.request.urlopen("https://www.googleapis.com/youtube/v3/channels?part=statistics&id=" + channel[0] + "&key=" + key,context=context).read()
        stat = json.loads(data)["items"][0]["statistics"]

        t=stattable(channel, date, stat['viewCount'], stat['subscriberCount'], stat['commentCount'], stat['hiddenSubscriberCount'],stat['videoCount'])


        #s.add(t)
        #s.commit()

def main():

    channel_list = getchannel(s)
    updateStat(s,channel_list)
    s.close()

if __name__=="__main__":
    main()