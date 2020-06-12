import pymysql
import pandas
import scipy.stats as stats_module

def get_channels_from_database(database):
    cursor = database.cursor()
    cursor.execute('select cid from channels')

    channels = []

    rows = cursor.fetchall()

    for row in rows:
        channels.append(row[0])

    return channels

def get_data_frame(channel, database):
    SUBS = 'subciberCount'
    VIDEO = 'videoCount'
    cursor = database.cursor()
    query = "select time_stamp, videoCount, subscriberCount from stat where cid = \'%s\' order by time_stamp" % channel
    x = []
    y = []

    cursor.execute(query)
    rows = cursor.fetchall()

    stats = {}

    for row in rows:
        stats[row[0]] = {}
        stats[row[0]][VIDEO] = row[1]
        stats[row[0]][SUBS] = row[2]

    video_cnt = None
    prev_date = None

    for date in stats.keys():
        if prev_date is None:
            video_cnt = stats[date][VIDEO]
            prev_date = date
        
        if video_cnt != stats[date][VIDEO]:
            video_cnt = stats[date][VIDEO]
            
            x.append((date - prev_date).days)
            y.append(stats[date][SUBS] - stats[prev_date][SUBS])
            prev_date = date

    print(x)
    print(y)

    return pandas.DataFrame([x, y]).T


def correlation_anlysis(channel, database):
    cor_coeif = 0
    
    data_frame = get_data_frame(channel, database)
    cor_coeif = data_frame.corr(method='pearson')

    return cor_coeif

def print_list_to_csv(rows):
    import csv
    # CSV 파일 한글 깨짐 현상을 방지하기 위해 encoding='utf-8-sig'를 해주어야 한다.
    with open('CorrelationAnalysis.csv', 'w', encoding='utf-8-sig', newline='') as file:
        writer = csv.writer(file)
        
        writer.writerow(['채널명', '상관계수'])
        for row in rows:
            writer.writerow(row)


if __name__ == "__main__":
    db_creedit = pymysql.connect(host='203.245.30.13', user='', password='', db='db_creedit', charset='utf8')
    channels = get_channels_from_database(db_creedit)

    for channel in channels:
        p = correlation_anlysis(channel, db_creedit)
        print(p[0][1])

    db_creedit.close()
