import csv
from collections import Counter

f=open("HeightWeight.csv",newline="")
reader=csv.reader(f)
data=list(reader)


data.pop(0)
hdata=[]
for i in range(len(data)):
    height=data[i][1]
    hdata.append(float(height))

newData=Counter(data)
mode_data_for_range={
    "50-60":0,"60-70":0,"70-80":0 
}
for height,occurance in newData.items():
    if(50<float(height)<60):
        mode_data_for_range["50-60"]+=occurance
    elif(60<float(height)<70):
        mode_data_for_range["60-70"]+=occurance
    elif(70<float(height)<80):
        mode_data_for_range["70-80"]+=occurance

mode_range=0
mode_occurance=0

for range,occurance in mode_data_for_range.items():
    if(occurance>mode_occurance):
        mode_range=[int(range.split("-")[0]),int(range.split("-")[1])]
        mode_occurance=occurance
    
mode=float((mode_range[0]+mode_range[1])/2)

print(mode)
