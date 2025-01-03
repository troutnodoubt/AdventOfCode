from queue import PriorityQueue

fname='input_day16.txt'
# fname='example_day16a.txt'    # 7036
# fname='example_day16b.txt'  # 11048

with open(fname) as fp: data = fp.read().splitlines()

def findNeighbor(node,direction):
    neighborFound=False
    if   direction=='N': 
        d=(-1, 0)
        normal=(0,1)
    elif direction=='S': 
        d=( 1 ,0)
        normal=(0,1)
    elif direction=='W': 
        d=( 0,-1)
        normal=(1,0)
    elif direction=='E':
        d=( 0 ,1)
        normal=(1,0)
    testnode=[node[0],node[1]]
    while not neighborFound:
        testnode=[testnode[0]+d[0],testnode[1]+d[1]]
        nextnode=[testnode[0]+d[0],testnode[1]+d[1]]
        normal1 =[testnode[0]+normal[0],testnode[1]+normal[1]]
        normal2 =[testnode[0]-normal[0],testnode[1]-normal[1]]

        if data[testnode[0]][testnode[1]]!='#' and (data[nextnode[0]][nextnode[1]]=='#' or data[normal1[0]][normal1[1]]!='#' or data[normal2[0]][normal2[1]]!='#'):
            return testnode
        elif data[testnode[0]][testnode[1]]=='#':
            return []

class Graph:
    def __init__(self, graph: dict={}):
       self.graph=graph
        
    def add_edge(self, node1, node2, distance):
        if node1 not in self.graph:
            self.graph[node1]={}
        self.graph[node1][node2]=distance
    
    def shortest_distances(self, source: str):
        distances = {node: float("inf") for node in self.graph}
        distances[source] = 0  

        pq = PriorityQueue()
        pq.put((0, source))
        
        visited = set()

        while not pq.empty(): 
            current_distance,current_node = pq.get()
            if current_node in visited:
                continue  
            visited.add(current_node)

            for neighbor, weight in self.graph[current_node].items():
                if neighbor in distances.keys():
                    tentative_distance = current_distance + weight
                    if tentative_distance < distances[neighbor]:
                        distances[neighbor] = tentative_distance
                        pq.put((tentative_distance, neighbor))
                        
        return distances
    
nodeconnections={}
opposite={}
opposite['N']='S'
opposite['S']='N'
opposite['E']='W'
opposite['W']='E'
start=[]
end=[]

for i,row in enumerate(data):
    for j,pos in enumerate(row):
        vertex=i*len(data[0])+j
        if data[i][j]!='#':
            if data[i][j-1]!='#' or data[i][j+1]!='#':
                if data[i+1][j]!='#' or data[i-1][j]!='#': # this is a junction where we'll place a node
                    # move left, right, up, and down and find its neighboring node
                    for direction in ('N','S','E','W'):
                        nextnode=findNeighbor([i,j],direction)
                        if nextnode:
                            nodekey=str(vertex)+direction
                            connectingNode=str(nextnode[0]*len(data[0])+nextnode[1])+opposite[direction]
                            nodeconnections[nodekey]=connectingNode
            if data[i][j]=='E': end=vertex
            if data[i][j]=='S': start=vertex

g=Graph()

source=str(start)+'E'
destinations=[str(end)+dir for dir in 'NSEW']

for nodeAndDir in nodeconnections.keys():
    node=int(nodeAndDir[:-1])
    i=node//len(data[0])
    j=node%len(data[0])

    connectionAndDir=nodeconnections[nodeAndDir]
    connection=int(connectionAndDir[:-1])
    iconnection=connection//len(data[0])
    jconnection=connection%len(data[0])
    distance=abs(iconnection-i)+abs(jconnection-j)
    g.add_edge(nodeAndDir, connectionAndDir, distance)

    if nodeAndDir[-1]=='N':
        g.add_edge(nodeAndDir, str(node)+'S', 0)
        g.add_edge(nodeAndDir, str(node)+'E', 1000)
        g.add_edge(nodeAndDir, str(node)+'W', 1000)
    elif nodeAndDir[-1]=='S':
        g.add_edge(nodeAndDir, str(node)+'N', 0)
        g.add_edge(nodeAndDir, str(node)+'E', 1000)
        g.add_edge(nodeAndDir, str(node)+'W', 1000)
    elif nodeAndDir[-1]=='E':
        g.add_edge(nodeAndDir, str(node)+'W', 0)
        g.add_edge(nodeAndDir, str(node)+'S', 1000)
        g.add_edge(nodeAndDir, str(node)+'N', 1000)
    elif nodeAndDir[-1]=='W':
        g.add_edge(nodeAndDir, str(node)+'E', 0)
        g.add_edge(nodeAndDir, str(node)+'S', 1000)
        g.add_edge(nodeAndDir, str(node)+'N', 1000)
         
scores=g.shortest_distances(source)

minscore=float('inf')
for destination in destinations:
    if destination in scores.keys():
        # print(destination,scores[destination])
        if scores[destination]<minscore: minscore=scores[destination]

print('Part 1', minscore)
