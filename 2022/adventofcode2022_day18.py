
fname="day18_example.txt"
#fname="input_day18.txt"
with open(fname) as fp: data = fp.read().splitlines()

class Cube:
    def __init__(self, pos):
        self.pos=pos
        
    def adjacentcubes(self):
        self.neighbors=[ (pos[0]-1, pos[1], pos[2]),
                         (pos[0]+1, pos[1], pos[2]),
                         (pos[0], pos[1]-1, pos[2]),
                         (pos[0], pos[1]+1, pos[2]),
                         (pos[0], pos[1], pos[2]-1),
                         (pos[0], pos[1], pos[2]+1)]
        
    def addfaces(self,numfaces):
        self.numfaces=numfaces
        
cubes=[]
for row in data:
    pos=(int(row.split(',')[0]),int(row.split(',')[1]),int(row.split(',')[2]))
    cubes.append(Cube(pos))
    
poslist=[]
for cube in cubes:
    cube.adjacentcubes()
    poslist.append(cube.pos)

for cube in cubes:
    for pos in poslist:
        # print(pos)
        # print(cube.pos)
        # print(cube.neighbors)
        # print()
        if pos in cube.neighbors:
            print(pos,cube.pos)
    