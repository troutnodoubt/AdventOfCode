#from collections import defaultdict
#import numpy as np
# from numpy import Inf
fname="day_25_example.txt"
fname="input_day25.txt"
with open(fname) as fp: data = fp.read().splitlines()

# assign dictionary of tuples, with each tuple being a state
# or just leave as list of lists
# check states to the right of those with >
# move right
# check states to the below of those with v
# move down
# continue while states are open

# bed=dict()
#bed=data.copy()

# for i in range(len(data)):
#     for j in range(len(data[0])):
#         bed[(i,j)]=data[i][j]
bed=[['.' for _ in row] for row in data]
for i in range(len(data)):
    for j in range(len(data[0])):
        bed[i][j]=data[i][j]


def checkright(bed):
    openright=[[0 for _ in row] for row in bed]
    for i in range(len(bed)):
        for j in range(len(bed[0])):
            #print(j)
            if j==len(bed[0])-1:
                if bed[i][0]=='.' and bed[i][j]=='>': 
                    openright[i][j]=1
                    # print(i,j)
                    # print(bed[i][j])
            else:
                if bed[i][j+1]=='.' and bed[i][j]=='>': 
                    openright[i][j]=1
                    # print(i,j)
                
    return(openright)

def checkdown(bed):
    opendown=[[0 for _ in row] for row in bed]
    for i in range(len(bed)):
        for j in range(len(bed[0])):
            #print(j)
            if i==len(bed)-1:
                if bed[0][j]=='.' and bed[i][j]=='v': opendown[i][j]=1
            else:
                if bed[i+1][j]=='.' and bed[i][j]=='v': opendown[i][j]=1
    return(opendown)

def moveright(bed,openright):
    newbed=bed.copy()
    for i in range(len(bed)):
        for j in range(len(bed[0])):
            if openright[i][j]==1:
                if j==len(bed[0])-1:
                    newbed[i][j]='.'
                    newbed[i][0]='>'
                else:
                    newbed[i][j]='.'
                    newbed[i][j+1]='>'
    return(newbed)

def movedown(bed,opendown):
    newbed=bed.copy()
    for i in range(len(bed)):
        for j in range(len(bed[0])):
            if opendown[i][j]==1:
                if i==len(bed)-1:
                    newbed[i][j]='.'
                    newbed[0][j]='v'
                else:
                    newbed[i][j]='.'
                    newbed[i+1][j]='v'
    return(newbed)
            

# print(bed)

movesavailable=True

cycles=0
while movesavailable:
    openright=checkright(bed)
    a=sum([sum(i) for i in zip(*openright)])
    bed=moveright(bed,openright)
    # bed=list()
    # bed=newbed.copy()
    # print(bed)
    opendown=checkdown(bed)
    bed=movedown(bed,opendown)
    b=sum([sum(i) for i in zip(*opendown)])
    cycles+=1
    if a+b==0: movesavailable=False
    
print('Part 1 solution is',cycles)

    