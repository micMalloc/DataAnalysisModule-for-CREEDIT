import urllib.request
import json
import pymysql
import ssl


connection = pymysql.connect(
    host='localhost',
    user='root',
    password='gml7594!tn',
    db='creedit',
    charset='utf8'
)
# connection = pymysql.connect(host='203.245.30.13', user='ehdgus93', password='ehdgus93!', db='db_creedit', charset='utf8')
cursor = connection.cursor()

sql = 'insert into channels(cid, cname, category) values(%s, %s, %s)'

channel_id = 'cid'
channel_name = 'cname'

channels = [
    {
        channel_id: 'UCuVPc55mMEX0qcl4yV87bsQ',
        channel_name: '꽃보다로아',
    },
    {
        channel_id: 'UCJHYWXSx59KI2VPF2itKtVg',
        channel_name: '성형외과러쉬',
    },
    {
        channel_id: 'UCnhZuoNcL89qNax7YlWvavQ',
        channel_name: '미러볼 뮤직',
    },
    {
        channel_id: 'UCi5HiGEMB5Cb_uUS3mPtPVA',
        channel_name: '지호안',
    },
    {
        channel_id: 'UC2hzrZSZqaJyxMIxWXjWL8w',
        channel_name: '트라메-TRAME',
    },
    {
        channel_id: 'UCP2DzxpOoyep8S-xozGaPXQ',
        channel_name: '책갈피',
    },
    {
        channel_id: 'UCEhUVkSiReYlXSE6hs5ugDQ',
        channel_name: 'Boxerfury-박서퓨리',
    },
    {
        channel_id: 'UCLokFPMSPhz1Z7qXfScD9CA',
        channel_name: '정남브라더스',
    },
    {
        channel_id: 'UCv9KfRS16BxoQdJhYNFAHGw',
        channel_name: 'TOOL PLAYER',
    },
    {
        channel_id: 'UCUaFsXg6LZGxyvsH5IS8JIA',
        channel_name: '당민리뷰',
    },
    {
        channel_id: 'UCTZY1CxZMAQtG0FVlvSE8iQ',
        channel_name: '코트니 다솜샘',
    },
    {
        channel_id: 'UCC5Cb58-PG1RiihXlxZNwvA',
        channel_name: '욱가이버',
    },
    # UCVfdF_LCAmVZ2Pgyamag5eg
    {
        channel_id: 'UCVfdF_LCAmVZ2Pgyamag5eg',
        channel_name: '솔랜드',
    }
]

# print(len(channels))

for channel in channels:
    cursor.execute(sql, (channel[channel_id], channel[channel_name], 1))

connection.commit()
connection.close()
