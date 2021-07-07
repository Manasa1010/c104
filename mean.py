import csv

f=open("HeightWeight.csv",newline="")
reader=csv.reader(f)
data=list(reader)


data.pop(0)
hdata=[]
for i in range(len(data)):
    height=data[i][1]
    hdata.append(float(height))


n=len(hdata)
total=0
for h in hdata:
    total+=h
print(total)
print(n)
mean=total/n
print("mean:"+str(mean))    