import csv
from PIL import Image
from os import listdir,walk,path
from os.path import isfile, join
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

count=0
nbr=0
for x in scorelist[1:]:
    nbr+=1
    y=header[x.index(max(x))]
    z=header[x.index(min(x))]
    a,b=float(max(x)),float(min(x))
    #print(float(a))
    if abs(a) > abs(b):
        y=y
    else :
        y=z
    print(x[0],y)#,max(x))
    if y in x[0]:
        count+=1
mypath="test"
imageFiles = [ join(mypath,f) for f in listdir(mypath) if isfile(join(mypath,f)) and (f.endswith("G") or f.endswith("g")) ]
numberFace=len(imageFiles)
print("accuracy:",float(count)/nbr)
print("recall:",float(count)/numberFace)
print(count)
#print(scorelist[1:2])


