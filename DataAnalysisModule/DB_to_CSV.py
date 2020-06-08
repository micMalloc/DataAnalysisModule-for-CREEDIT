import pymysql
import json
import csv
import pandas as pd
from datetime import datetime


# connection = pymysql.connect(host='localhost', user='root', password='', db='creedit', charset='utf8')
connection = pymysql.connect(host='203.245.30.13', user='ehdgus93', password='', db='db_creedit', charset='utf8')
cursor = connection.cursor()


def make_csv(feature):

    column = []
    sql = "show full columns from %s" % feature

    cursor.execute(sql)
    rows = cursor.fetchall()

    for i in range(len(rows)):
        column.append(rows[i][0])

    
    sql = "select * from %s" % feature
    cursor.execute(sql)
    rows = cursor.fetchall()

    rows = list(rows)
    for a in range(len(rows)):
        rows[a] = list(rows[a])

    
    f = open('%s.csv' % feature, 'w', encoding='utf-8', newline='')

    wr = csv.writer(f)

    wr.writerow(column)

    for i in range(len(rows)):
        wr.writerow(rows[i])

    f.close()

    connection.close()

def open_csv(feature):
    f = open("%s.csv" % feature, 'r', encoding='utf-8')
    data = pd.read_csv(f)

    return data

if __name__ == "__main__":
    
    item = 'statistics'

    try:
        make_csv(item)
        data = open_csv(item)
        print(data)

    except:
        print("error")
