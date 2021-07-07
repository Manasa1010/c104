import csv

f=open("HeightWeight.csv",newline="")
reader=csv.reader(f)
data=list(reader)


data.pop(0)
hdata=[]
for i in range(len(data)):
    height=data[i][1]
    hdata.append(float(height))

hdata.sort()
n=len(hdata)

if(n%2==0):
    median1=float(hdata[n//2])
    median2=float(hdata[n//2-1])
    median=(median1+median2)/2
else:
    median=float(hdata[n//2]) 

print(median)    

