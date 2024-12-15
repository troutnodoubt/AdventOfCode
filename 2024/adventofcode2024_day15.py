
fname='input_day15.txt'
# fname='example_day15a.txt'
# fname='example_day15b.txt'

with open(fname) as fp: data = fp.read().splitlines()

walls=[]
blocks=[]
separator=[]
start=[]

for i,row in enumerate(data):
    if row=='':
        separator=i
        break
    for j,c in enumerate(row):
        if c=='#': walls.append((i,j))
        elif c=='O': blocks.append((i,j))
        elif c=='@': start=(i,j)

size=(i-1,j)

walls=tuple(walls)
# print(walls)
# print(blocks)
# # print(free)
# print(start)


instructions=[]
for row in data[separator:]:
    for c in row: instructions.append(c)

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

    if nextPos not in walls and nextPos not in blocks:
        return nextPos
    elif nextPos in walls:
        return robotPos
    elif nextPos in blocks:
        if canMoveBlock(nextPos,instruction): return nextPos
        else: return robotPos
    else:
        print('ruh roh')

def canMoveBlock(pos,instruction):
    offset=getOffset(instruction)     
    nextPos = (pos[0]+offset[0],pos[1]+offset[1])
    canMove=False
    if nextPos not in walls and nextPos not in blocks:
        canMove=True
    elif nextPos in walls:
        canMove=False
    elif nextPos in blocks:
        canMove=canMoveBlock(nextPos,instruction)
    else: print('something wrong in canmove')
    if canMove:
        blocks.remove(pos)
        blocks.append(nextPos)
    return canMove

def displayMap():
    for i in range(size[0]+1):
        row=''
        for j in range(size[1]+1):
            if (i,j) in walls: row=row+ '#'
            elif (i,j) in blocks: row=row + 'O'
            elif (i,j) == robotPos: row=row +'@'
            else: row=row+'.'
        print(row)
    print()
    print()

robotPos=start

# displayMap()
for instruction in instructions:
    robotPos=moveRobot(robotPos,instruction)
    # print(instruction)
    # displayMap()

total=0
for block in blocks:
    total+=100*block[0]+block[1]

print("Total", total)
