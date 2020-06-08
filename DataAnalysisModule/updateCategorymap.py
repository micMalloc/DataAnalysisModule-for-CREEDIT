import pymysql

# connection = pymysql.connect(host='203.245.30.13', user='ehdgus93', password='', db='db_creedit', charset='utf8')
connection = pymysql.connect(host='localhost', user='root', password='', db='creedit', charset='utf8')
cursor = connection.cursor()

sql = 'insert into Category(cid, category_id) values(%s, %s)'

channel_id = 'cid'
channel_name = 'category_id'

channels = [
    {
        channel_id: 'UCuVPc55mMEX0qcl4yV87bsQ',
        channel_name: 6,
    },
    {
        channel_id: 'UCJHYWXSx59KI2VPF2itKtVg',
        channel_name: 8,
    },
    {
        channel_id: 'UCnhZuoNcL89qNax7YlWvavQ',
        channel_name: 9,
    },
    {
        channel_id: 'UCi5HiGEMB5Cb_uUS3mPtPVA',
        channel_name: 3,
    },
    {
        channel_id: 'UC2hzrZSZqaJyxMIxWXjWL8w',
        channel_name: 8,
    },
    {
        channel_id: 'UC2hzrZSZqaJyxMIxWXjWL8w',
        channel_name: 3,
    },
    {
        channel_id: 'UCP2DzxpOoyep8S-xozGaPXQ',
        channel_name: 8,
    },
    {
        channel_id: 'UCEhUVkSiReYlXSE6hs5ugDQ',
        channel_name: 3,
    },
    {
        channel_id: 'UCEhUVkSiReYlXSE6hs5ugDQ',
        channel_name: 9,
    },
    {
        channel_id: 'UCLokFPMSPhz1Z7qXfScD9CA',
        channel_name: 3,
    },
    {
        channel_id: 'UCv9KfRS16BxoQdJhYNFAHGw',
        channel_name: 8,
    },
    {
        channel_id: 'UCUaFsXg6LZGxyvsH5IS8JIA',
        channel_name: 8,
    },
    {
        channel_id: 'UCTZY1CxZMAQtG0FVlvSE8iQ',
        channel_name: 6,
    },
    {
        channel_id: 'UCC5Cb58-PG1RiihXlxZNwvA',
        channel_name: 8,
    },
    # UCVfdF_LCAmVZ2Pgyamag5eg
    {
        channel_id: 'UCVfdF_LCAmVZ2Pgyamag5eg',
        channel_name: 7,
    }
]

for channel in channels:
    cursor.execute(sql, (channel[channel_id], channel[channel_name]))

connection.commit()
connection.close()