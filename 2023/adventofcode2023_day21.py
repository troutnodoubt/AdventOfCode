from queue import PriorityQueue
from numpy import inf

fname='input_day21.txt'
# fname='example_day21.txt'
with open(fname) as fp: data = fp.read().splitlines()

class Graph:
    def __init__(self, num_of_vertices):
        self.v = num_of_vertices
        self.edges = [[-1 for i in range(num_of_vertices)] for j in range(num_of_vertices)]
        self.visited = []
        
    def add_edge(self, u, v):
        self.edges[u][v] = 1
        self.edges[v][u] = 1
       
        
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
        
 

g=Graph(len(data)*len(data[0]))

def setedges():
    for i in range(len(data)):
        for j in range(len(data[0])):
            vertex=(i)*len(data[0])+j
            #print(vertex)
          
            if j != len(data[0])-1: 
                #vertex right
                if data[i][j] != '#' and data[i][j+1] != '#':
                    g.add_edge(vertex, vertex+1)
            
            if i != len(data)-1:
                #vertex down
                if data[i][j] != '#' and data[i+1][j] != '#':
                    g.add_edge(vertex, vertex+len(data[0]))
        

starti=0
startj=0
for i,row in enumerate(data):
    if 'S' in row:
        starti=i
        for j,c in enumerate(row):
            if c=='S':
                startj=j
                break
        break

start_vertex=starti*len(data[0])+startj

print(starti,startj,data[starti][startj])

setedges()
D = dijkstra(g, start_vertex)

stepsleft=64
count=0
for plot in D.values():
    if plot<=stepsleft and plot%2==0: count+=1
        

print('Part 1 is', count)