#importing libraries
import csv
import sqlite3
to_db =[]

conn = sqlite3.connect('appstore.db')
c = conn.cursor()

c.execute('CREATE TABLE IF NOT EXISTS appstore(app STR, category STR, rating FLOAT)')

with open('googleplaystore.csv', "r") as ps:
    reader = csv.DictReader(ps)
    for count,i in enumerate(reader):
        to_db.append((i['app'], i['category'], i['rating']))
        if count == 99:
            break

c.executemany("INSERT INTO appstore VALUES  (?, ?, ?);", to_db)
conn.commit()

c.execute('SELECT * FROM appstore LIMIT 100')
#data = c.fetchall()
#print(data)
for row in c.fetchall():
    print(row)
conn.close()