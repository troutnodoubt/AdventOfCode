
fname='input_day15.txt'
# fname='example_day15a.txt'
# fname='example_day15b.txt'
# fname='example_day15c.txt'
# fname='example_day15d.txt'
# fname='example_day15e.txt'
# fname='example_day15f.txt'
# fname='example_day15g.txt'

with open(fname) as fp: data = fp.read().splitlines()

# data=['#############',
#       '#@..O..O.O..#',
#       '#############',
#       '',
#       '>>>>>>>>>>>>>>>>>>',
#       '']

walls=[]
blocks=[]
blocksr=[]
separator=[]
start=[]
doubledata=[]
canMoveList=[]
nextPoslList=[]
toRemoveList=[]

for i,row in enumerate(data):
    tmp=''
    if row=='':
        separator=i
        break
    for j,c in enumerate(row):
        if c=='#': tmp=tmp+'##'
        elif c=='O': tmp=tmp+'[]'
        elif c=='@': tmp=tmp+'@.'
        elif c=='.': tmp=tmp+'..'
    doubledata.append(tmp)

for i,row in enumerate(doubledata):
    if row=='':
        separator=i
        break
    for j,c in enumerate(row):
        if c=='#': walls.append((i,j))
        elif c=='[': blocks.append((i,j))
        elif c=='@': start=(i,j)

size=(i,j)
walls=tuple(walls)

instructions=[]
for row in data[separator:]:
    for c in row: instructions.append(c)

def findBlocksr():
    del blocksr[:]
    for block in blocks: blocksr.append((block[0],block[1]+1))
      
def getOffset(instruction):
    if   instruction=='>': offset=(0,1)
    elif instruction=='<': offset=(0,-1)
    elif instruction=='^': offset=(-1,0)
    elif instruction=='v': offset=(1,0)
    else: offset=(0,0)
    return offset

def moveRobot(robotPos,instuction):
    offset=getOffset(instruction)
    nextPos = (robotPos[0]+offset[0],robotPos[1]+offset[1])

    if nextPos not in walls and nextPos not in blocks and nextPos not in blocksr:
        return nextPos
    elif nextPos in walls:
        return robotPos
    elif nextPos in blocks:
        del canMoveList[:]
        del nextPoslList[:]
        del toRemoveList[:]
        canMoveBlock([nextPos],instruction)
        if all(canMoveList): 
            moveBlocks()
            return nextPos
        else: return robotPos
    elif nextPos in blocksr:
        del canMoveList[:]
        del nextPoslList[:]
        del toRemoveList[:]
        testPos=(nextPos[0],nextPos[1]-1)
        canMoveBlock([testPos],instruction) 
        if all(canMoveList): 
            moveBlocks()
            return nextPos
        else: return robotPos
    else:
        print('ruh roh')

def canMoveBlock(positions,instruction):
    for pos in positions:
        toRemoveList.append(pos)
        offset=getOffset(instruction)     
        canMove=False
        if instruction=='>':
            nextPosl=(pos[0]+offset[0],pos[1]+offset[1]+1)

            if nextPosl not in walls and nextPosl not in blocks:
                canMove=True
            elif nextPosl in walls:
                canMove=False
            elif nextPosl in blocks:
                canMove=canMoveBlock([(nextPosl[0],nextPosl[1]-0)],instruction)
            else: print('something wrong in canmove')
 
            nextPoslList.append((pos[0],pos[1]+1))

        elif instruction=='<':
            nextPosl=(pos[0]+offset[0],pos[1]+offset[1])
            if nextPosl not in walls and nextPosl not in blocksr:
                canMove=True
            elif nextPosl in walls:
                canMove=False
            elif nextPosl in blocksr:
                canMove=canMoveBlock([(nextPosl[0],nextPosl[1]-1)],instruction)
            else: print('something wrong in canmove')
            nextPoslList.append(nextPosl)

        elif instruction in '^v':
            nextPosl=(pos[0]+offset[0],pos[1]+offset[1])
            nextPosr=(pos[0]+offset[0],pos[1]+offset[1]+1)

            if nextPosl not in walls and nextPosl not in blocks and nextPosl not in blocksr and nextPosr not in walls and nextPosr not in blocks and nextPosr not in blocksr:
                canMove=True
            elif nextPosl in walls or nextPosr in walls:
                canMove=False
            elif nextPosl in blocks: # directly over/under another block
                canMove=canMoveBlock([nextPosl],instruction)
            elif nextPosl in blocksr and nextPosr not in walls and nextPosr not in blocks: #left side over/under right side, right side clear
                canMove=canMoveBlock([(nextPosl[0],nextPosl[1]-1)],instruction)
            elif nextPosr in blocks and nextPosl not in walls and nextPosl not in blocksr: #right side over/under left side, left side clear
                canMove=canMoveBlock([nextPosr],instruction)
            elif nextPosl in blocksr and nextPosr in blocks: # over/under two blocks
                canMove=canMoveBlock([(nextPosl[0],nextPosl[1]-1),nextPosr],instruction)
            else: print('something wrong in canmove')
            nextPoslList.append(nextPosl)
        canMoveList.append(canMove)
    return canMove

def moveBlocks():
    tmpnextPoslList=list(set(nextPoslList))
    tmptoRemoveList=list(set(toRemoveList))
    if all(canMoveList):
        for i,pos in enumerate(tmptoRemoveList):
            if pos in blocksr:
                blocks.remove((pos[0],pos[1]-1))
            else:
                blocks.remove(pos)
            blocks.append(tmpnextPoslList[i])
        findBlocksr()

def displayMap():
    for i in range(size[0]+1):
        row=''
        for j in range(size[1]+1):
            if (i,j) in walls: row=row+ '#'
            elif (i,j) in blocks: row=row + '['
            elif (i,j) in blocksr: row=row + ']'
            elif (i,j) == robotPos: row=row +'@'
            else: row=row+'.'
        print(row)
    print()
    print()

robotPos=start
findBlocksr()

startdisplay=0
enddisplay=20
for count,instruction in enumerate(instructions):
    
    robotPos=moveRobot(robotPos,instruction)
    if count in range(startdisplay,enddisplay):
        print(count,instruction)
        displayMap()

displayMap()
total=0

for i,block in enumerate(blocks):
    total+=100*block[0]+block[1]

print("Total", total) # 1444404 too low, 1449319 too low

