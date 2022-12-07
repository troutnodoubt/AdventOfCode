#from collections import defaultdict
#import numpy as np
# from numpy import Inf
import matplotlib.pyplot as plt
fname="day_13_example.txt"
fname="input_day13.txt"
with open(fname) as fp: data = fp.read().splitlines()

# assign dictionary of tuples, all with value of #
# find fold number
# update dictionary, row is (foldnumber)-(row-foldnumber)=2foldnumber-row if row>foldnumber
# checked with a few examples ok

coordinates=dict()

for row in data:
    if 'fold' not in row:
        #print(row.split(','))
        a=row.split(',')
        if a!=['']: coordinates[(int(a[0]),int(a[1]))]='#'

for row in data:
    if 'fold' in row: print(row)
    
def fold(direction,foldnumber,coordinates):
    a=list(coordinates.keys())
    for key in a:
        if direction=='x':
            if int(key[0])>foldnumber:
                coordinates[(2*foldnumber-int(key[0]),key[1])]='#'
                coordinates.pop(key)
        if direction=='y':
            if int(key[1])>foldnumber:
                coordinates[(key[0],2*foldnumber-int(key[1]))]='#'
                coordinates.pop(key)
    
    return(coordinates) 
        
coordinates=fold('x',655,coordinates)

print('Part 1 solution is',len(coordinates))


coordinates=fold('y',447,coordinates)
coordinates=fold('x',327,coordinates)
coordinates=fold('y',223,coordinates)
coordinates=fold('x',163,coordinates)
coordinates=fold('y',111,coordinates)
coordinates=fold('x',81,coordinates)
coordinates=fold('y',55,coordinates)
coordinates=fold('x',40,coordinates)
coordinates=fold('y',27,coordinates)
coordinates=fold('y',13,coordinates)
coordinates=fold('y',6,coordinates)

x=list()
y=list()
for key in list(coordinates.keys()):
    x.append(key[1]*-1)
    y.append(key[0]*5)
    
plt.scatter(y,x)
plt.show