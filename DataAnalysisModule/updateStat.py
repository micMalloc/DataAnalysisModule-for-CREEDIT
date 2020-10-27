import pymysql
import urllib.request
import json
import ssl
from datetime import datetime

key = ""

#local = pymysql.connect(host='localhost', user='root', password='', db='creedit', charset='utf8')
creedit = pymysql.connect(host='203.245.30.13', user='ehdgus93', password='ehdgus93!', db='db_creedit', charset='utf8')

cursor = creedit.cursor()
#manager = creedit.cursor()

sql = 'select cid from channels'

cursor.execute(sql)

channels = cursor.fetchall()

sql = 'insert into stat(cid, time_stamp, viewCount, subscriberCount, commentCount, hiddenSubscriberCount, videoCount) values(%s, %s, %s, %s, %s, %s, %s)'

context = ssl._create_unverified_context()

now = datetime.now()

date = "{0}-{1}-{2}".format(now.year, now.month, now.day)

print(len(channels))

for channel in channels:
    print(channel[0])
    data = urllib.request.urlopen("https://www.googleapis.com/youtube/v3/channels?part=statistics&id="+channel[0]+"&key="+key, context=context).read()

    try:
        stat = json.loads(data)["items"][0]["statistics"]
        print(stat)
    except KeyError:
        continue 
    #cursor.execute(sql, (channel, date, stat['viewCount'], stat['subscriberCount'], stat['commentCount'], stat['hiddenSubscriberCount'], stat['videoCount']))
    # manager.execute(sql, (channel, date, stat['viewCount'], stat['subscriberCount'], stat['commentCount'], stat['hiddenSubscriberCount'], stat['videoCount']))

#local.commit()

#local.close()

#creedit.commit()
creedit.close()
