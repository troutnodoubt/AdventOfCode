#adapting dijkstra from https://stackabuse.com/courses/graphs-in-python-theory-and-implementation/lessons/dijkstras-algorithm/

from queue import PriorityQueue
from numpy import inf

fname="day12_example.txt"
fname="input_day12.txt"
with open(fname) as fp: data = fp.read().splitlines()

class Graph:
    def __init__(self, num_of_vertices):
        self.v = num_of_vertices
        self.edges = [[-1 for i in range(num_of_vertices)] for j in range(num_of_vertices)]
        self.visited = []
        
    def add_edge(self, u, v, weight):
        if weight==0 or weight==1 or weight==-1:
            self.edges[u][v] = 1
            self.edges[v][u] = 1
        elif weight>1:
            self.edges[u][v] = inf
            self.edges[v][u] = 1
        elif weight<-1:
            self.edges[u][v] = 1
            self.edges[v][u] = inf
        
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
        
        



heights={}
score={}
height=0
for letter in 'abcdefghijklmnopqrstuvwxyz':
    score[letter]=height
    height+=1

for i in range(len(data)):
    for j in range(len(data[0])):
        #print(i,j)
        if data[i][j] != 'S' and data[i][j] != 'E':
            heights[(i,j)]=score[data[i][j]]
        if data[i][j]=='S':
            start=(i,j)
            heights[(i,j)]=score['a']
        elif data[i][j]=='E':
            end=(i,j)
            heights[(i,j)]=score['z']

g=Graph(len(data)*len(data[0]))

def setedges():
    for i in range(len(data)):
        for j in range(len(data[0])):
            vertex=(i)*len(data[0])+j
            #print(vertex)
          
            if j != len(data[0])-1: 
                #vertex right
                weight=heights[(i,j+1)]-heights[(i,j)]
                g.add_edge(vertex, vertex+1, weight)
            
            if i != len(data)-1:
                #vertex down
                weight=heights[(i+1,j)]-heights[(i,j)]
                g.add_edge(vertex, vertex+len(data[0]), weight)
        

start_vertex=start[0]*len(data[0])+start[1]
end_vertex=end[0]*len(data[0])+end[1]

setedges()
D = dijkstra(g, start_vertex)

print('Part 1 solution is', D[end_vertex])

nstepsold=inf

for i in range(len(data)):
    for j in range(len(data[0])):
        if data[i][j]=='a':
            del(g)
            g=Graph(len(data)*len(data[0]))
            start_vertex=(i)*len(data[0])+j
            #print(start_vertex)
            setedges()
            D = dijkstra(g, start_vertex)
            nsteps=D[end_vertex]
            #print(nsteps)
            if nsteps<nstepsold:
                nstepsold=nsteps
                
print('Part 2 solution is', nstepsold)



            