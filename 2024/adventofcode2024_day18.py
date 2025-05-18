
from queue import PriorityQueue

fname='input_day18.txt'
# fname='example_day18.txt'

with open(fname) as fp: data = fp.read().splitlines()
highestgood=0
lowestbad=len(data)

if 'example' in fname: highestgood=12
else: highestgood=1024

def findDistanceToExit(ncorrupted):
    if 'example' in fname:
        maxsize=6
    else:
        maxsize=70
    corruptedList=[]
    nvertices=(maxsize+1)*(maxsize+1)

    for i,byte in enumerate(data):
        if i==ncorrupted: break
        a=byte.split(',')
        corruptedList.append((int(a[1]),int(a[0])))

    class Graph:
        def __init__(self, num_of_vertices):
            self.v = num_of_vertices
            self.edges = [[-1 for i in range(num_of_vertices)] for j in range(num_of_vertices)]
            self.visited = []
            
        def add_edge(self, u, v, weight=1):
            self.edges[u][v] = 1*weight
            self.edges[v][u] = 1*weight
            
            
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

    g=Graph(nvertices)

    for i in range(maxsize+1):
        for j in range(maxsize+1):
            v=i*(maxsize+1)+j
            if (i,j) not in corruptedList:
                if (i,j+1) not in corruptedList and j<maxsize: 
                    g.add_edge(v,v+1)
                if (i+1,j) not in corruptedList and i<maxsize: 
                    g.add_edge(v,v+maxsize+1)
                
    distance = dijkstra(g,0)[nvertices-1]
    return distance

def binarysearch(start,end,highestgood,lowestbad):
    a=findDistanceToExit(start)
    b=findDistanceToExit(end)
    inf=float('inf')
    found=False
    if a!=inf and b==inf:
        if start+1==end: found=True
        if highestgood<start: highestgood=start
        if lowestbad>end: lowestbad=end
        nextstart=highestgood
        nextend=(end+start)//2
        
    elif a==inf:
        if lowestbad>start: lowestbad=start
        nextstart=highestgood
        nextend=lowestbad
    elif b!=inf:
        if end>highestgood: highestgood=end
        nextstart=highestgood
        nextend=lowestbad
    if not found:
        found=binarysearch(nextstart,nextend,highestgood,lowestbad)
    else: print('Part 2',data[highestgood])

    return found

print('Part 1',findDistanceToExit(highestgood))

binarysearch(highestgood,len(data),highestgood,len(data))
