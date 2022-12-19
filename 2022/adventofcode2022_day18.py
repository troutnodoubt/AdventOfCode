
fname="day18_example.txt"
fname="input_day18.txt"
with open(fname) as fp: data = fp.read().splitlines()

class Cube:
    def __init__(self, pos):
        self.pos=pos
        self.numfaces=6
        
    def adjacentcubes(self):
        self.neighbors=[ (self.pos[0]-1, self.pos[1], self.pos[2]),
                         (self.pos[0]+1, self.pos[1], self.pos[2]),
                         (self.pos[0], self.pos[1]-1, self.pos[2]),
                         (self.pos[0], self.pos[1]+1, self.pos[2]),
                         (self.pos[0], self.pos[1], self.pos[2]-1),
                         (self.pos[0], self.pos[1], self.pos[2]+1)]
        
    def subtractface(self):
        self.numfaces=self.numfaces-1
        
    
        
cubes=[]
for row in data:
    position=(int(row.split(',')[0]),int(row.split(',')[1]),int(row.split(',')[2]))
    cubes.append(Cube(position))
    
poslist=[]
for cube in cubes:
    cube.adjacentcubes()
    poslist.append(cube.pos)


for cube in cubes:
    for position in poslist:
        # print(pos)
        # print(cube.pos)
        # print(cube.neighbors)
        # print()
        if position in cube.neighbors:
            #print(position,cube.pos)
            cube.subtractface()

nfacelist=[]
for cube in cubes:
    nfacelist.append(cube.numfaces)
    
print('Part 1 solution is', sum(nfacelist))
    

# establish a node outside, map paths to each other node
# if can't reach then it's inside. 
# Subtract inside facing faces
# depends on size. Looks like it's 20x20x20, so doable

# find empties (opposite set as cubes)
# path from 0,0,0 to empties
# if no path then internal 
# subtract faces contacting internal nodes 