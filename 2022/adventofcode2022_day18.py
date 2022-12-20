from queue import PriorityQueue
from numpy import inf

fname="day18_example.txt"
#fname="input_day18.txt"
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
        
class Graph:
    def __init__(self, num_of_vertices):
        self.v = num_of_vertices
        self.edges = [[-1 for i in range(num_of_vertices)] for j in range(num_of_vertices)]
        self.visited = []
        
    def add_edge(self, u, v, weight):
        self.edges[u][v] = weight
        self.edges[v][u] = weight

def dijkstra(graph, start_vertex):
    D = {v:float('inf') for v in range(graph.v)}
    D[start_vertex] = 0

    pq = PriorityQueue()
    pq.put((0, start_vertex))

    while not pq.empty():
        (dist, current_vertex) = pq.get()
        graph.visited.append(current_vertex)

        for neighbor in range(graph.v):
            if graph.edges[current_vertex][neighbor] != -1:
                distance = graph.edges[current_vertex][neighbor]
                if neighbor not in graph.visited:
                    old_cost = D[neighbor]
                    new_cost = D[current_vertex] + distance
                    if new_cost < old_cost:
                        pq.put((new_cost, neighbor))
                        D[neighbor] = new_cost
    return D
 
      
def setedges(dim):
    weight=1
    for i in range(0,dim):
        for j in range(0,dim):
            for k in range(0,dim):
                #vertex=(i,j,k)
                vertex=i*dim*dim+j*dim+k
                #print(vertex)
               
                
                if i != dim-1:
                    #vertex into page
                    if (n_to_pos(vertex+dim*dim,dim)) in poslist or (n_to_pos(vertex,dim)) in poslist:
                        weight=inf
                    else:
                        weight=1
                    g.add_edge(vertex, vertex+dim*dim, weight)
              
                if j != dim-1: 
                    #vertex down
                    if (n_to_pos(vertex+dim,dim)) in poslist or (n_to_pos(vertex,dim)) in poslist:
                        weight=inf
                    else:
                        weight=1
                    g.add_edge(vertex, vertex+dim, weight)
                    
                if k != dim-1: 
                    #vertex right
                    if (n_to_pos(vertex+1,dim)) in poslist or (n_to_pos(vertex,dim)) in poslist:
                        weight=inf
                    else:
                        weight=1
                    g.add_edge(vertex, vertex+1, weight)
            
            
def n_to_pos(n,d):
    i=n//(d*d)
    j=(n-d*d*i)//d
    k=n-i*d*d-j*d
#    return((i+1,j+1,k+1))
    return((i,j,k))

def pos_to_n(p,d):
    # return((p[0]-1)*d*d + (p[1]-1)*d + (p[2] - 1))
    return((p[0])*d*d + (p[1])*d + (p[2]))

    
        
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
    #print(cube.pos,cube.numfaces)
    nfacelist.append(cube.numfaces)

    
print('Part 1 solution is', sum(nfacelist))
    

# find void cubes and add them to the list of solid cubes, then recalculate
# open boundaries facing the edge of the space are still open. Tricky.

dim=0
for vertex in poslist:
    for size in vertex:
        if size>dim: dim=size
   
dim+=5       
g=Graph(dim*dim*dim)
setedges(dim)

start=(1,1,1)
distancematrix=dijkstra(g, pos_to_n(start,dim))
voidlist=[]
for key in distancematrix.keys():
    val = distancematrix[key]
    if val==inf:
        #print(key)
        #print(n_to_pos(key,dim))
        if n_to_pos(key,dim) not in poslist:
            print('This space is void')
            print(n_to_pos(key,dim))
            # cubes.append(Cube(n_to_pos(key,dim)))
            # cubes[-1].adjacentcubes()
            # poslist.append(cubes[-1].pos)
            voidlist.append(n_to_pos(key,dim))

cubes=[]
for row in data:
    position=(int(row.split(',')[0]),int(row.split(',')[1]),int(row.split(',')[2]))
    cubes.append(Cube(position))
    
for empty in voidlist:
    cubes.append(Cube(empty))
    
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
    #print(cube.pos,cube.numfaces)
    nfacelist.append(cube.numfaces)

    
print('Part 2 solution is', sum(nfacelist))
