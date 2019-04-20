import csv
import sqlite3

conn = sqlite3.connect('appstore.db')
c = conn.cursor()

c.execute('CREATE TABLE IF NOT EXISTS appstore(app STR, category STR, rating FLOAT)')

with open ('googleplaystore.csv', 'r') as fin:
    dr = csv.DictReader(fin)
    to_db = [(i['app'], i['category'], i['rating']) for i in dr]

c.executemany("INSERT INTO appstore VALUES  (?, ?, ?);", to_db)
conn.commit()

c.execute('SELECT * FROM appstore LIMIT 100')
#data = c.fetchall()
#print(data)
for row in c.fetchall():
    print('APP Name:',row[0])
conn.close()