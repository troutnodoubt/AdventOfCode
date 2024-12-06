fname='input_day6.txt'
#fname='example_day6.txt'
with open(fname) as fp: data = fp.read().splitlines()

grid=[row for row in data]

def turnRight(heading):
    sequence='urdl'
    for index,h in enumerate(sequence):
        if h==heading: return sequence[(index+1)%len(sequence)]

def canMoveForward(position,heading):
    i=position[0]
    j=position[1]
    # print(i,j)
    # print(grid[i][j])
    if heading=='u':
        if i>0 and grid[i-1][j]!='#': return True
    elif heading=='d':
        if i<len(grid)-1 and grid[i+1][j]!='#': return True
    elif heading=='l':
        if j>0 and grid[i][j-1]!='#': return True
    elif heading=='r':
        if j<len(grid)-1 and grid[i][j+1]!='#': return True
    return False

def willExit(position,heading):
    i=position[0]
    j=position[1]

    if heading=='u':
        if i==0: return True
    elif heading=='d':
        if i==len(grid)-1: return True
    elif heading=='l':
        if j==0: return True
    elif heading=='r':
        if j==len(grid)-1: return True
    return False

def stepForward(position,heading):
    i=position[0]
    j=position[1]

    if heading=='u': return [i-1,j]
    elif heading=='d': return [i+1,j]
    elif heading=='l': return [i,j-1]
    elif heading=='r': return [i,j+1]
    else: print('ruh roh')

def walk(position,heading):
    visited=[position]
    history=[[position,heading]]
    # heading=[heading]
    onGrid=True
    count=0
    stuck=False
    while onGrid:
        count+=1
        if count>1000000: break
       # print(position)
        if canMoveForward(position,heading):
           # print("Can move")
        
        
            position=stepForward(position,heading)
            #print("stepping forward")
            if [position,heading] not in history: history.append([position,heading])
            else: 
                print("stuck in a loop")
                count+=100000000
                stuck=True
            if position not in visited: visited.append(position)
        else:
            if willExit(position,heading):
                onGrid=False
               # print("Exiting")
                break
            else:
                heading=turnRight(heading)
              #  print("new heading",heading)
    return visited, stuck


heading='u'

for i,row in enumerate(grid):
    for j,val in enumerate(row):
        if val=='^': position=[i,j]

start=[position[0],position[1]]
visited,stuck=walk(position,heading)
print("Part 1 is",len(visited))

#brute force this thing, lol

stuckcount=0
for ii,datarow in enumerate(data):
    for jj,dataval in enumerate(datarow):
        grid=[row for row in data]
        if grid[ii][jj]==".": 
            print(grid[ii])
            s=list(grid[ii])
            s[jj]="#"
            grid[ii]="".join(s)
            print(grid[ii])
        visited,stuck=walk(start,'u')
        if stuck: stuckcount+=1

print("Part 2",stuckcount)


#print("Part 2 is", total)
