# -*- coding: utf-8 -*-
"""
Created on Wed Nov 10 22:23:42 2021

@author: Mark
"""

import re

fname="C://Users/Mark/Documents/Advent of Code/2020/day_16_example.txt"
fname="C://Users/Mark/Documents/Advent of Code/2020/day_16_example_2.txt"
fname="C://Users/Mark/Documents/Advent of Code/2020/input_day16.txt"
with open(fname) as fp: data = fp.read().splitlines()


invalid=list(range(0,1000))
p=re.compile('[0-9]+')
p2=re.compile('[a-z]* *[a-z]+:')
notelist=[]
for row in data:
    sublist=list()
    if "-" in row:
        astring=p.findall(row)
        desc=p2.findall(row)
        a=[int(a) for a in astring]
        valid1=range(a[0],a[1]+1)
        valid2=range(a[2],a[3]+1)
        sublist=[desc,valid1,valid2]
        notelist.append(sublist)
        for i in valid1:
            if i in invalid:
                invalid.remove(i)
        for i in valid2:
            if i in invalid:
                invalid.remove(i)
        
#find rows with nearby ticket numbers
rownum=0
for row in data:
    if "nearby tickets:" in row:
        break
    rownum+=1

nearby=data[rownum+1:-1]
nearbynums=[]
for row in nearby:
    nearbynums.append([int(a) for a in row.split(',')])



invalidtickets=[]
validtickets=[]
for row in nearbynums:
    validticket=True
    for ticket in row:
        if ticket in invalid:
            invalidtickets.append(ticket)
            validticket=False
    if validticket:
        validtickets.append(row)
        

print('Part 1 solution is', sum(invalidtickets))


transposedtickets=list()

for i in range(len(validtickets[0])):
    row=list()
    for sublist in validtickets:
        row.append(sublist[i])
    transposedtickets.append(row)
rowidx=0
logiclist=list()   
for row in transposedtickets:
    descmatch=list()
    logicsublist=list()
    for note in notelist:
        numbermatch=list()
        
        for number in row:
            if number in note[1] or number in note[2]:
                numbermatch.append(True)
            else:
                numbermatch.append(False)
            
        if all(numbermatch):
            #print(row)
            #print(note[0])
            descmatch.append(note[0])
            logicsublist.append(1)
        else:
            logicsublist.append(0)
    print(rowidx)
    print(descmatch)
    logiclist.append(logicsublist)
    rowidx+=1
        
        
                