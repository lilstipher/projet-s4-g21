import csv
scorefile= open('scores.csv', 'rb') 
reader =csv.reader(scorefile)
print(reader)
scorelist=[]
for i in reader:
    scorelist.append(i)
#print(scorelist[1:])
#header=scorelist[0]
header=[]
for x in scorelist[0]:
    y=x.split("/")
    if len(y)>2:
        y=y[len(y)-2]
    header.append(y)
for x in scorelist[1:]:
    print(x[0],header[x.index(max(x))],max(x))


