import csv
# -*- coding:utf-8 -*-

def transform(contents):
    contents = contents.encode('utf-8')
    contents = contents.decode('unicode_escape')
    return contents

f = open('data.csv', 'r', encoding='utf-8')
filereader = csv.reader(f)
data = []
for line in filereader:
    message = line[0]
    message = transform(message)
    name = line[1]
    name = transform(name)
    time = line[2]
    row=[]
    row.append(message)
    row.append(name)
    row.append(time)
    data.append(row)
f.close()

f = open('write.csv', 'w', encoding='utf-8', newline='')
wr = csv.writer(f)
for row in data:
    wr.writerow(row)
f.close()
