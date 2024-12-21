from collections import deque
import copy

fname='input_day20.txt'
# fname='example_day20.txt'

with open(fname) as fp: data = fp.read().splitlines()

shortcuts={}

def bfs(graph, start, parent, distance):
    q = deque()
    distance[start] = 0
    q.append(start)

    while q:
        node = q.popleft()
        for neighbor in graph[node]:
            if distance[neighbor] == float('inf'):
                parent[neighbor] = node
                distance[neighbor] = distance[node] + 1
                q.append(neighbor)

def find_shortest_distance(graph, start, destination, nvertices):
    parent = [-1] * nvertices
    distance = [float('inf')] * nvertices
    bfs(graph, start, parent, distance)

    if distance[destination] == float('inf'):
        print("Source and Destination are not connected")
        print(graph)
        return
    path = []
    current_node = destination
    path.append(destination)
    while parent[current_node] != -1:
        path.append(parent[current_node])
        current_node = parent[current_node]
   
    return path

def findShortCuts(vertex,basepath,picoseconds):
    mdrange=range(-(picoseconds),picoseconds+1)
    i=vertex//len(data)
    j=vertex%len(data[0])
    remainingpath=basepath[basepath.index(vertex)+1:]
    for ioffset in mdrange:
        for joffset in mdrange:
            manhattandistance=abs(ioffset)+abs(joffset)
            
            if manhattandistance in range(2,picoseconds+1):
                icand=i+ioffset
                jcand=j+joffset
                if icand in range(len(data)) and jcand in range(len(data[0])):
                    vcand=icand*len(data)+jcand
                    if vcand in remainingpath:
                        timesaved=remainingpath.index(vcand)+1-manhattandistance
                        if (vertex,vcand) not in shortcuts.keys() and (vcand,vertex) not in shortcuts.keys() and timesaved>0:
                            shortcuts[(vertex,vcand)]=timesaved


nvertices=len(data)*len(data[0])
g=[[] for _ in range(nvertices)]
start=[]
end=[]

for i,row in enumerate(data):
    for j,pos in enumerate(row):
        vertex=i*len(data)+j
        if data[i][j]!='#':
            if j<len(row)-1 and i<len(data)-1:
                if data[i][j+1] != '#' and data: 
                    g[vertex].append(vertex+1)
                    g[vertex+1].append(vertex)
                if data[i+1][j] != '#':
                    g[vertex].append(vertex+len(row))
                    g[vertex+len(row)].append(vertex)
            elif j<len(row)-1 and i==len(data)-1: # bottom row of grid
                if data[i][j+1] != '#': 
                    g[vertex].append(vertex+1)
                    g[vertex+1].append(vertex)
            elif j==len(row)-1 and i<len(data)-1: # right hand side of grid
                if data[i+1][j] != '#':
                    g[vertex].append(vertex+len(row))
                    g[vertex+len(row)].append(vertex)
            if data[i][j]=='S': start=vertex
            if data[i][j]=='E': end=vertex

p=find_shortest_distance(g, start, end, nvertices)
p.reverse()
baseline=len(p)

for i,vertex in enumerate(p):
    print(i,'of',len(p))
    findShortCuts(vertex,p,20)

summary=[]
for time in shortcuts.values():
    summary.append(time)

over100=len([a for a in summary if a>=100])
print(over100)
