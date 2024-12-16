
fname='input_day15.txt'
fname='example_day15a.txt'
fname='example_day15b.txt'
fname='example_day15c.txt'

with open(fname) as fp: data = fp.read().splitlines()

walls=[]
blocks=[]
blocksr=[]
separator=[]
start=[]
doubledata=[]

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
# print(walls)
# print(blocks)
# # print(free)
# print(start)


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
        if canMoveBlock([nextPos],instruction): return nextPos
        else: return robotPos
    elif nextPos in blocksr:
        testPos=(nextPos[0],nextPos[1]-1)
        print(testPos)
        print()
        if canMoveBlock([testPos],instruction): return nextPos
        else: return robotPos
    else:
        print('ruh roh')

def canMoveBlock(positions,instruction):
    canMoveList=[]
    nextPoslList=[]
    # nextPosrList=[]
    for pos in positions:
        offset=getOffset(instruction)     
        # nextPos = (pos[0]+offset[0],pos[1]+offset[1])
        canMove=False
        if instruction=='>':
            nextPosl=(pos[0]+offset[0],pos[1]+offset[1]+1)
            print(pos)
            print(offset)
            print(nextPosl)
            if nextPosl not in walls and nextPosl not in blocks:
                canMove=True
            elif nextPosl in walls:
                canMove=False
            elif nextPosl in blocks:
                print('next block right')
                canMove=canMoveBlock([(nextPosl[0],nextPosl[1]+0)],instruction)
            else: print('something wrong in canmove')
            # if canMove:
                # blocks.remove(pos)
                # blocks.append(nextPosl)
                # findBlocksr()
            # return canMove
            canMoveList.append(canMove)
            nextPoslList.append((nextPosl[0],nextPosl[1]-1))
        elif instruction=='<':
            nextPosl=(pos[0]+offset[0],pos[1]+offset[1]-2)
            if nextPosl not in walls and nextPosl not in blocks:
                canMove=True
            elif nextPosl in walls:
                canMove=False
            elif nextPosl in blocks:
                canMove=canMoveBlock([nextPosl],instruction)
            else: print('something wrong in canmove')
            # if canMove:
            #     print(pos)
                # blocks.remove(pos)
                # blocks.append((nextPosl[0],nextPosl[1]+1))
                # findBlocksr()
            # return canMove
            canMoveList.append(canMove)
            nextPoslList.append((nextPosl[0],nextPosl[1]+1))
        elif instruction in '^v':
            print(pos)
            print(offset)
            nextPosl=(pos[0]+offset[0],pos[1]+offset[1])
            nextPosr=(pos[0]+offset[0],pos[1]+offset[1]+1)
            # print(nextPosl,nextPosr)
            # test = (pos[0]+offset[0],pos[1]+offset[1])
            # print(test)
            # if test in blocks:
            #     nextPosl=(pos[0]+offset[0],pos[1]+offset[1])
            #     nextPosr=(pos[0]+offset[0],pos[1]+offset[1]+1)
            # elif test in blocksr:
            #     nextPosl=(pos[0]+offset[0],pos[1]+offset[1]-1)
            #     nextPosr=(pos[0]+offset[0],pos[1]+offset[1])
            # elif test in walls:
            #     return False
            
            if nextPosl not in walls and nextPosl not in blocks and nextPosl not in blocksr and nextPosr not in walls and nextPosr not in blocks and nextPosr not in blocksr:
                canMove=True
                # canMoveList.append(canMove)
            elif nextPosl in walls or nextPosr in walls:
                canMove=False
            elif nextPosl in blocks: # directly over/under another block
                canMove=canMoveBlock([nextPosl],instruction)
            elif nextPosl in blocksr and nextPosr not in walls and nextPosr not in blocks: #left side over/under right side, right side clear
                canMove=canMoveBlock([nextPosl],instruction)
            elif nextPosr in blocks and nextPosl not in walls and nextPosl not in blocksr: #right side over/under left side, left side clear
                canMove=canMoveBlock([nextPosr],instruction)
            elif nextPosl in blocksr and nextPosr in blocks: # over/under two blocks
                canMove=canMoveBlock([(nextPosl[0],nextPosl[1]-1),nextPosr],instruction)
                # canMover=canMoveBlock(nextPosr,instruction)
                # if canMovel and canMover: canMove=True
                # else: return
            else: print('something wrong in canmove')
            # return canMove
            canMoveList.append(canMove)
            nextPoslList.append(nextPosl)
    if all(canMoveList):
        # print(positions)
        # print(nextPoslList)
        # print(canMoveList)
        for i,pos in enumerate(positions):
            
            # print(i,pos)
            # print(pos,nextPoslList[i])
            if pos in blocksr:
                print('right',pos)
                blocks.remove((pos[0],pos[1]-1))
            else:
                blocks.remove(pos)
            blocks.append(nextPoslList[i])
        findBlocksr()
    return all(canMoveList)

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

displayMap()
for instruction in instructions:
    print(instruction)
    robotPos=moveRobot(robotPos,instruction)
    
    displayMap()

total=0
for block in blocks:
    total+=100*block[0]+block[1]

print("Total", total)