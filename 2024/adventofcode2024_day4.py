import re

fname='input_day4.txt'
#fname='example_day4.txt'
with open(fname) as fp: data = fp.read().splitlines()

# wacky idea, rotate and flip the array and just count xmas or samx

def diag1(wordsearch):
    res={}
    for i in range(len(wordsearch)):
        for j in range(len(wordsearch)):
            if i+j not in res.keys():
                res[i+j]=wordsearch[i][j]
            else:
                res[i+j]=res[i+j]+wordsearch[i][j]
    return [*res.values()]

def ninety(wordsearch):
    return [*map("".join, zip(*reversed(wordsearch)))]

def flip(wordsearch):
    a=[]
    for row in wordsearch:
        a.append(row[::-1])
    return a

total=0
p1=re.compile('XMAS')
p2=re.compile('SAMX')
for row in data:
    total+=len(re.findall(p1,row))
    total+=len(re.findall(p2,row))

rot=ninety(data)

for row in rot:
    total+=len(re.findall(p1,row))
    total+=len(re.findall(p2,row))

cross=diag1(data)

for row in cross:
    total+=len(re.findall(p1,row))
    total+=len(re.findall(p2,row))

cross=diag1(flip(data))

for row in cross:
    total+=len(re.findall(p1,row))
    total+=len(re.findall(p2,row))

print("Part 1 is", total) 

def searchDiags(i,j,data):
    scount=0
    mcount=0
    test=[data[i-1][j-1],data[i+1][j-1],data[i-1][j+1],data[i+1][j+1]]
    for e in test:
        if e=='M': mcount+=1
        elif e=='S': scount+=1
    if mcount==2 and scount==2 and data[i-1][j-1]!=data[i+1][j+1]: return 1
    else: return 0

total=0
for i in range(1,len(data)-1):
    for j in range(1,len(data)-1):
        if data[i][j]=='A': 
            total+=searchDiags(i,j,data)

print("Part 2 is", total) 
