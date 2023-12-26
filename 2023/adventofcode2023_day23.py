from queue import PriorityQueue
from numpy import inf

fname='input_day23.txt'
# fname='example_day23.txt'
with open(fname) as fp: data = fp.read().splitlines()

class Graph:
    def __init__(self, num_of_vertices):
        self.v = num_of_vertices
        self.edges = [[-1 for i in range(num_of_vertices)] for j in range(num_of_vertices)]
        self.visited = []
        
    def add_edge(self, u, v, tile, distance=0):
        if tile==0:
            self.edges[u][v] = 1
            self.edges[v][u] = 1
        elif tile==1:
            self.edges[u][v] = 1
            self.edges[v][u] = inf
        elif tile==2:
            self.edges[u][v] = distance
       
        
def dijkstra(graph, start_vertex):
    D = {v:float('inf') for v in range(graph.v)}
    D[start_vertex] = 0

    pq = PriorityQueue()
    pq.put((inf, start_vertex))
    
    path = {v:'' for v in range(graph.v)}
 
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
                        path[neighbor]=current_vertex
                        D[neighbor] = new_cost
    return D,path
        

def longest_dijkstra(graph, start_vertex):
    D = {v:float('-inf') for v in range(graph.v)}
    D[start_vertex] = 0

    pq = PriorityQueue()
    pq.put((inf, start_vertex))
    
    path = {v:'' for v in range(graph.v)}
 
    while not pq.empty():
        
        (dist, current_vertex) = pq.get()
        graph.visited.append(current_vertex)

        for neighbor in range(graph.v):
            if graph.edges[current_vertex][neighbor] != -1:
                distance = graph.edges[current_vertex][neighbor]
                print(current_vertex,neighbor,distance)
                if neighbor not in graph.visited:
                    old_cost = D[neighbor]
                    new_cost = D[current_vertex] + distance
                    print(old_cost,new_cost)
                    print()
                    if new_cost > old_cost:
                        pq.put((new_cost, neighbor))
                        path[neighbor]=current_vertex
                        D[neighbor] = new_cost
    return D,path 

g=Graph(len(data)*len(data[0]))

def isCheckValveNode(i,j):
    nchecks=0
    if data[i][j+1]=='>': nchecks+=1
    if data[i][j-1]=='>': nchecks+=1
    if data[i+1][j]=='v': nchecks+=1
    if data[i-1][j]=='v': nchecks+=1
    if nchecks>=2: return True
    else: return False
    
def findCheckValveNodes():
    nodelist=[]
    for i in range(len(data)):
        for j in range(len(data[0])):
            vertex=(i)*len(data[0])+j
            if j != len(data[0])-1 and j > 0 and i!=len(data)-1 and i >0:
                if isCheckValveNode(i,j): nodelist.append(vertex)
    return nodelist
                

def setedges():
    for i in range(len(data)):
        for j in range(len(data[0])):
            vertex=(i)*len(data[0])+j
            #print(vertex)
            
            if j != len(data[0])-1: 
                #vertex right
                if data[i][j] != '#' and data[i][j+1] != '#':
                    if data[i][j]=='>' or data[i][j+1]=='>':
                        g.add_edge(vertex, vertex+1, 1)
                        
                    elif data[i][j]=='.' and data[i][j+1]=='.':
                        g.add_edge(vertex, vertex+1, 0)
                
                        
            if i != len(data)-1:
                #vertex down
                if data[i][j] != '#' and data[i+1][j] != '#':
                    if data[i][j]=='v' or data[i+1][j]=='v':
                        g.add_edge(vertex, vertex+len(data[0]),1)
                    elif data[i][j]=='.' and data[i+1][j]=='.':
                        g.add_edge(vertex, vertex+len(data[0]),0)


def findPath(end_vertex):
        if path[end_vertex] != '':
            # print(path[end_vertex])
            pathlist.append(path[end_vertex])
            findPath(path[end_vertex])


checkvalvenodes=findCheckValveNodes()
start_vertex=1
end_vertex=len(data)*len(data[0])-2

checkvalvenodes.insert(0,start_vertex)
checkvalvenodes.append(end_vertex)

setedges()
pathlist=[]
print(checkvalvenodes)

cvgraph=Graph(len(checkvalvenodes))


for i,start in enumerate(checkvalvenodes):
    for j,stop in enumerate(checkvalvenodes):
        if i!=j:
            g.visited=[]
            D,path=dijkstra(g,start)
            pathlist=[]
            findPath(stop)
            pathlist.reverse()
            # print(pathlist)
            hitsothervalves = len(set(pathlist).intersection(checkvalvenodes))>1
            if D[stop]<inf and not hitsothervalves: 
                # print(start,stop)
                # print(D[stop])
                # print(pathlist)
                # print()
                cvgraph.add_edge(i, j, 2, D[stop])
                
        



D,path = longest_dijkstra(cvgraph,0)

print('Part 1 is', D[len(D)-1])
#1914 is too low

# plotted the map by hand and got 2174, also too low
# Need to find distance between nodes without dijkstra,
# there's only one path node to node, just walk it.
# After that there must be a problem with my algorithm or I wrote 
# value down wrong when trying by hand
# findPath(end_vertex)
# for stop in pathlist:
#     print(stop,pathlist.count(stop))




# i=11
# j=21
# v=i*len(data[0])+j
# a=len(data[0])

        

# print('Part 1 is', D[end_vertex])