import sqlite3
conn = sqlite3.connect('raghulrider1.db')
print("Opened database succesfully")

conn.execute('''CREATE TABLE BIODATA
             (ID INT PRIMARY KEY NOT NULL,
             NAME TEXT NOT NULL,
             AGE INT NOT NULL,
             DEPARTMENT TEXT NULL);''')
print('Table created Succesfully')

conn.execute("INSERT INTO BIODATA (ID,NAME,AGE,DEPARTMENT) \
             VALUES (1, 'Raghul', 19, 'ECE' )");
conn.commit()
print('Record created ')

cursor = conn.execute("SELECT id, name, age ,department from BIODATA")
for row in cursor:
    print("ID = ", row[0])
    print ("NAME = ", row[1])
    print ("AGE = ", row[2])
    print ("DEPARTMENT = ", row[3])

conn.execute("UPDATE BIODATA set DEPARTMENT = 'EEE' where ID = 1")
conn.commit

conn.execute("INSERT INTO BIODATA (ID,NAME,AGE,DEPARTMENT) \
             VALUES (2, 'Kanmani', 19, 'BCA' )");