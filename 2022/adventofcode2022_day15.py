import re
import datetime
#import time

fname="day15_example.txt"
fname="input_day15.txt"
with open(fname) as fp: data = fp.read().splitlines()

def md(a):
    return(abs(a[2]-a[0])+abs(a[3]-a[1]))

def canreach(a,testrow):
    straighdist=abs(a[1]-testrow)
    overlap=md(a)-straighdist
    coveredlims=[]
    if overlap>=0: #row is visible by sensor a
       
        coveredlims=[a[0]-overlap,a[0]+overlap]
    return(coveredlims)

def merge(intervals):
    if len(intervals) == 0 or len(intervals) == 1:
        return intervals
    intervals.sort(key=lambda x:x[0])
    result = [intervals[0]]
    for interval in intervals[1:]:
        if interval[0] <= result[-1][1]:
            result[-1][1] = max(result[-1][1], interval[1])
        else:
            result.append(interval)
    return result

def findcoveredbeacon(ytest):
    coveredbeaconcount=0
    for beacon in beaconlist:
        for interval in limitlist:
            if beacon[0] in range(interval[0],interval[1]+1) and beacon[1]==ytest:
               
                coveredbeaconcount+=1
    return(coveredbeaconcount)

def findlimitlist(ytest):
    limitlist=[]
    for row in data:
        values=[int(a) for a in re.findall('-?[0-9]+',row)]
        
        if len(canreach(values,ytest))>0: limitlist.append(canreach(values,ytest))
    limitlist=merge(limitlist)
    return(limitlist)

starttime=datetime.datetime.now()
    
ytest=10
ytest=2000000

limitlist=findlimitlist(ytest)
coveredcount=0
for interval in limitlist:
    coveredcount+=(interval[1]-interval[0]+1)

    
beaconlist=[]
for row in data:
    values=[int(a) for a in re.findall('-?[0-9]+',row)]
    beacon=(values[2],values[3])
    if beacon not in beaconlist:
        beaconlist.append(beacon)
   
print('Part 1 solution is', coveredcount-findcoveredbeacon(ytest))

stoptime=datetime.datetime.now() 
print('Elapsed time',(stoptime-starttime))

maxcoordinate=20
maxcoordinate=4000000


#Brute force for part 2, using efficent solution from part 1. Takes about 5 minutes

starttime=datetime.datetime.now()
for y in range(maxcoordinate+1):
    limitlist=findlimitlist(y) 
    for idx in range(len(limitlist)):
        limitlist[idx][0]=max(0,limitlist[idx][0])
        limitlist[idx][1]=min(maxcoordinate,limitlist[idx][1])
    coveredcount=0
    for interval in limitlist:
        coveredcount+=(interval[1]-interval[0]+1)
    #print(y,findcoveredbeacon(y),coveredcount)
    if coveredcount<len(range(maxcoordinate+1)):
        print('match row is',y)
        break
    
stoptime=datetime.datetime.now() 

print('Part 2 solution is', maxcoordinate*(limitlist[0][1]+1)+y)
print('Elapsed time',(stoptime-starttime))

