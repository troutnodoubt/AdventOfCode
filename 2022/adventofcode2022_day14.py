fname="day14_example.txt"
fname="input_day14.txt"
with open(fname) as fp: data = fp.read().splitlines()

def sign(a):
    val= 1 if a>=0 else -1
    return val


def findnextposition(currentposition):
    if (currentposition[0],currentposition[1]+1) not in allblocked:
        # move vertically
        nextposition=(currentposition[0],currentposition[1]+1)
        return(nextposition)
    elif (currentposition[0]-1,currentposition[1]+1) not in allblocked:
        # move vertically and left
        nextposition=(currentposition[0]-1,currentposition[1]+1)
        return(nextposition)
    elif (currentposition[0]+1,currentposition[1]+1) not in allblocked:
        # move vertically and right
        nextposition=(currentposition[0]+1,currentposition[1]+1)
        return(nextposition)
    else:
        # final resting space
        return(currentposition)
           
       
    

coord=[]

for row in data:
    block=[]
    for pair in row.split('->'):
        a=eval('('+pair+')')
        block.append(a)
    coord.append(block)

rocks=[] 
sand=[]
abyss=0
width=1   
for row in coord:
    for i in range(len(row)-1):
        if row[i][0]==row[i+1][0]: # same x coordinate, vertical line
            for j in range(row[i][1],row[i+1][1],sign(row[i+1][1]-row[i][1])):
                #print((row[i][0],j))
                rocks.append((row[i][0],j))
                if j>abyss:
                    abyss=j
                if row[i][0]>width: width=row[i][0]
        if row[i][1]==row[i+1][1]: # same y coordinate, vertical line
            for j in range(row[i][0],row[i+1][0],sign(row[i+1][0]-row[i][0])):
                #print((j,row[i][1]))
                rocks.append((j,row[i][1]))
                if row[i][1]>abyss:
                    abyss=row[i][1]
                if j>width: width=j
    for pair in row:
        if pair not in rocks:
            rocks.append(pair)
            if pair[1]>abyss:
                abyss=pair[1]


allblocked=[*rocks,*sand]

start=(500,0)
currentposition=start



nsand=0
full=False

while not full:
    finaldestination=False
    while not finaldestination:
        nextposition=findnextposition(currentposition)
        #print(nextposition)
        if nextposition==currentposition or full==True:
            finaldestination=True
        currentposition=(nextposition[0],nextposition[1])
        if nextposition[1]>abyss+1:
            full=True
            break
    sand.append(nextposition)
    allblocked=[*rocks,*sand]
    nsand+=1
    currentposition=start
    
print('Part 1 solution is', nsand-1)

nsand=0
full=False
currentposition=start

# Brute force. Takes a while but it gets there in the end
for i in range(500-2*width,500+2*width):
    rocks.append((i,abyss+2))

allblocked=[]
sand=[]
allblocked=[*rocks,*sand]

while not full:
    finaldestination=False
    while not finaldestination:
        nextposition=findnextposition(currentposition)
        #print(nextposition)
        if nextposition==currentposition or full==True:
            finaldestination=True
        currentposition=(nextposition[0],nextposition[1])
        if nextposition==start:
            full=True
            break
    sand.append(nextposition)
    allblocked=[*rocks,*sand]
    nsand+=1
    currentposition=start 

print('Part 2 solution is', nsand)
    
