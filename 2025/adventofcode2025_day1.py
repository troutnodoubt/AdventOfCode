fname='input_day1.txt'
# fname='example_day1.txt'

with open(fname) as fp: data = fp.read().splitlines()

def newPos(position,rotation):
    if rotation[0]=='L':
        newPosition = position-int(rotation[1:])
    elif rotation[0]=='R':
        newPosition = position+int(rotation[1:])
    else:
        print('ruh roh')
    newPosition%=100    
   
    return newPosition

def countAll(position,rotation):
    extrazeros=0
    newPosition=position
    if rotation[0]=='L':
        for i in range(int(rotation[1:])):
            newPosition-=1
            newPosition%=100
            if newPosition==0: extrazeros+=1

    elif rotation[0]=='R':
        for i in range(int(rotation[1:])):
            newPosition+=1
            newPosition%=100
            if newPosition==0: extrazeros+=1
    else:
        print('ruh roh')
    return [newPosition, extrazeros]

pos=50
zerocount=0
pos2=50
zerocount2=0

for rotation in data:
    pos = newPos(pos,rotation)
    if pos == 0: zerocount+=1

    [pos2,zeros]=countAll(pos2,rotation)
    zerocount2+=zeros

print('Part 1 is',zerocount)
print('Part 2 is',zerocount2)
