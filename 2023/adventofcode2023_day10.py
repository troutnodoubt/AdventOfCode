from queue import PriorityQueue
from numpy import inf

fname='input_day10.txt'
fname='example_day10.txt'
#fname='example_day10a.txt'
with open(fname) as fp: data = fp.read().splitlines()

def findStart():
    for i,line in enumerate(data):
        if 'S' in line:
            j=line.index('S')
            return i,j
        
class Graph:
    def __init__(self, num_of_vertices):
        self.v = num_of_vertices
        self.edges = [[-1 for i in range(num_of_vertices)] for j in range(num_of_vertices)]
        self.visited = []
        
    def add_edge(self, u, v, weight=1):
        #print(u,v)
        if u<=self.v and v<=self.v: self.edges[u][v] = weight
        
def dijkstra(graph, start_vertex):
    D = {v:[float('inf'),[-1]] for v in range(graph.v)}
    D[start_vertex][0] = 0

    pq = PriorityQueue()
    pq.put((0, start_vertex))

    while not pq.empty():
        (dist, current_vertex) = pq.get()
        graph.visited.append(current_vertex)

        for neighbor in range(graph.v):
            if graph.edges[current_vertex][neighbor] != -1:
                distance = graph.edges[current_vertex][neighbor]
                if neighbor not in graph.visited:
                    old_cost = D[neighbor][0]
                    new_cost = D[current_vertex][0] + distance
                    if new_cost < old_cost:
                        pq.put((new_cost, neighbor))
                        D[neighbor] = [new_cost,[current_vertex,*D[current_vertex][1]]]
    return D

def setedges(loop=False):
    connect=[]
    for i in range(len(data)):
        for j in range(len(data[0])):
            vertex=(i)*len(data[0])+j

            if data[i][j]=='|': connect=[(0,-1),(0,1)]
            elif data[i][j]=='-': connect=[(-1,0),(1,0)]
            elif data[i][j]=='L': connect=[(0,-1),(1,0)]
            elif data[i][j]=='J': connect=[(-1,0),(0,-1)]
            elif data[i][j]=='7': connect=[(-1,0),(0,1)]
            elif data[i][j]=='F': connect=[(1,0),(0,1)]
            elif data[i][j]=='S':
                if not loop:
                    connect=[]
                    if data[i][j+1]=='-' or data[i][j+1]=='7' or data[i][j+1]=='J': connect.append((1,0))
                    if data[i][j-1]=='-' or data[i][j-1]=='F' or data[i][j-1]=='L': connect.append((-1,0))
                    if data[i+1][j]=='|' or data[i+1][j]=='L' or data[i+1][j]=='J': connect.append((0,1))
                    if data[i-1][j]=='|' or data[i-1][j]=='F' or data[i+1][j]=='7': connect.append((0,-1))
                elif loop:
                    connect=[]
                    if data[i][j+1]=='-' or data[i][j+1]=='7' or data[i][j+1]=='J': connect.append((1,0))
                    elif data[i][j-1]=='-' or data[i][j-1]=='F' or data[i][j-1]=='L': connect.append((-1,0))
                    elif data[i+1][j]=='|' or data[i+1][j]=='L' or data[i+1][j]=='J': connect.append((0,1))
                    elif data[i-1][j]=='|' or data[i-1][j]=='F' or data[i+1][j]=='7': connect.append((0,-1))
       
            for coordinate in connect:
                if i+coordinate[1] in range(len(data)) and j+coordinate[0] in range(len(data[0])):
                    connectingvertex=(i+coordinate[1])*len(data[0])+j+coordinate[0]
                    g.add_edge(vertex,connectingvertex)
                    
def point_in_polygon(polygon, point): #taken from https://www.algorithms-and-technologies.com/point_in_polygon/python
    """
    Raycasting Algorithm to find out whether a point is in a given polygon.
    Performs the even-odd-rule Algorithm to find out whether a point is in a given polygon.
    This runs in O(n) where n is the number of edges of the polygon.
     *
    :param polygon: an array representation of the polygon where polygon[i][0] is the x Value of the i-th point and polygon[i][1] is the y Value.
    :param point:   an array representation of the point where point[0] is its x Value and point[1] is its y Value
    :return: whether the point is in the polygon (not on the edge, just turn < into <= and > into >= for that)
    """

    # A point is in a polygon if a line from the point to infinity crosses the polygon an odd number of times
    odd = False
    # For each edge (In this case for each point of the polygon and the previous one)
    i = 0
    j = len(polygon) - 1
    while i < len(polygon) - 1:
        i = i + 1
        # If a line from the point into infinity crosses this edge
        # One point needs to be above, one below our y coordinate
        # ...and the edge doesn't cross our Y corrdinate before our x coordinate (but between our x coordinate and infinity)

        if (((polygon[i][1] > point[1]) != (polygon[j][1] > point[1])) and (point[0] < (
                (polygon[j][0] - polygon[i][0]) * (point[1] - polygon[i][1]) / (polygon[j][1] - polygon[i][1])) +
                                                                            polygon[i][0])):
            # Invert odd
            odd = not odd
        j = i
    # If the number of crossings was odd, the point is in the polygon
    return odd

i,j=findStart()
g=Graph(len(data)*len(data[0]))

start_vertex=i*len(data[0])+j

setedges()
D = dijkstra(g, start_vertex)

    # i=vert//len(data[0])   
    # j=vert%len(data[0])

maxval=0
maxvert=0
for vert in D.keys():
    if D[vert][0]<inf:
        if D[vert][0]>maxval:
            maxval=D[vert][0]
            maxvert=vert

  



print('Part 1 is', maxval)


del(g)
i,j=findStart()
g=Graph(len(data)*len(data[0]))

start_vertex=i*len(data[0])+j

setedges(True)
D = dijkstra(g, start_vertex)

maxval=0
maxvert=0
for vert in D.keys():
    if D[vert][0]<inf:
        if D[vert][0]>maxval:
            maxval=D[vert][0]
            maxvert=vert

#print('Part 2 is', count) # close, need to only count horizontal lines in y and vertical lines in x. Maybe

coords=[(vert//len(data[0]),vert%len(data[0])) for vert in D[maxvert][1][:-1]]

#part 2 pseudocode doesn't work

# make 2d list with the boundary nodes indicated
# pass over all nodes in the x direction, if the count of the boundary is odd then flag nodes as countable in x
# pass over all nodes in the y direction, if the count of the boundary is odd then flag nodes as countable in y

# solution will be nodes that are countable in both x and y
