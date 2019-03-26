import csv
import random

row = ['#','Num1','Num2','Num3','Num4','Num5','Num6']

with open('person1.csv', 'a') as csvFile:
        writer = csv.writer(csvFile)
        writer.writerow(row)
csvFile.close()
for i in range(0,10):
    res=[]
    res.append(int(i))
    for i in range(1,7):
        with open('person1.csv', 'a') as csvFile:
            writer = csv.writer(csvFile)
            res.append(random.randint(0,10))       
        
        csvFile.close()