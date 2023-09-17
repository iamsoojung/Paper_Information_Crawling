import pymysql

conn=pymysql.connect(host='127.0.0.1', user='sj', password='tnwjd1211', db='homepage', charset='utf8')
if conn.open:
    with conn.cursor() as curs:
        print("connected")
conn.close()