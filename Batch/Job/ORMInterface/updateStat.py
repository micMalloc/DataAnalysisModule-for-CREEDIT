import os
from Job.ORMInterface.DatabaseConnection import s
from Job.ORMInterface.tableDefinition import Stat
from Job.ORMInterface.selectTable import getchannel

import urllib.request
import ssl
import json
from datetime import datetime

key = os.environ['GOOGLE_API_KEY']
context = ssl._create_unverified_context()
now = datetime.now()
date = "{0}-{1}-{2}".format(now.year, now.month, now.day)

def updateStat(s,channel_list):
    tempit=0
    for channel in channel_list:
        if tempit==0:
            tempit=tempit+1
            continue

        data = urllib.request.urlopen("https://www.googleapis.com/youtube/v3/channels?part=statistics&id=" + channel[0] + "&key=" + key,context=context).read()
        
        try:
            stat = json.loads(data)["items"][0]["statistics"]
            #t=stattable(channel, date, stat['viewCount'], stat['subscriberCount'], stat['commentCount'], stat['hiddenSubscriberCount'],stat['videoCount'])
            updatedata={'cid':channel,'time_stamp':date,'viewCount':stat['viewCount'],'subscriberCount':stat['subscriberCount'],'commentCount':stat['commentCount'],'hiddenSubscriberCount':stat['hiddenSubscriberCount'],'videoCount':stat['videoCount']}
            statinstance=Stat(**updatedata)
            print("done")

            s.add(statinstance)
            s.commit()
        except KeyError:
            print("Does Not Exist Channel : " + channel[0])
            continue

def main():

    channel_list = getchannel(s)
    updateStat(s,channel_list)
    s.close()

if __name__=="__main__":
    main()
