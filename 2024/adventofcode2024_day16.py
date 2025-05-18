from queue import PriorityQueue

fname='input_day16.txt'
# fname='example_day16a.txt'    # 7036
# fname='example_day16b.txt'  # 11048

with open(fname) as fp: data = fp.read().splitlines()
visited=set()
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
        parents = {}

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
            if current_node in self.graph.keys():
                for neighbor, weight in self.graph[current_node].items():
                    if neighbor in distances.keys():
                        tentative_distance = current_distance + weight
                        if tentative_distance < distances[neighbor]:
                            distances[neighbor] = tentative_distance
                            if neighbor not in parents.keys(): parents[neighbor] = [current_node]
                            else: parents[neighbor].append(current_node)
                            pq.put((tentative_distance, neighbor))
                        
        return distances,parents

def getShortestPath(parents,destination,source):
   
    shortest=destination
    path=[shortest]
    while shortest!=source:
        path.append(parents[shortest][0])
        # print(shortest, parents[shortest], int(shortest[:-1])//len(data[0]),int(shortest[:-1])%len(data[0]))
        shortest=parents[shortest][0]
    return path

def findBranches(parents,path):
    nodeset=set(path)
    branchnodes=set()
    for node in path:
        if node in parents.keys(): 
            nodeparents=parents[node]
            # print(node,nodeparents)
            for nodeparent in nodeparents:
                # print(node,nodeparent)
                if nodeparent not in nodeset:
                    branchnodes.add(nodeparent)
    return branchnodes

def findNextNodes(parents,branches,source):
    nextNodes=set()
    for branch in branches:
        if branch not in visited: 
            bestpath=getShortestPath(parents,branch,source)
            nextbranches=findBranches(parents,bestpath)
            nextNodes.update(nextbranches)
            # exploreBranches(parents,nextbranches,source)
    return nextNodes

def findIntermediateNodes(node1,node2):
    connections=[]
    i1=node1//len(data[0])
    i2=node2//len(data[0])
    j1=node1%len(data[0])
    j2=node2%len(data[0])
    if i1!=i2 and j1!=j2: return []
    elif i1==i2 and j1!=j2:
        start=min(j1,j2)
        stop=max(j1,j2)+1
        connections=[i1*len(data[0])+j for j in range(start,stop)]
    elif i1!=i2 and j1==j2:
        start=min(i1,i2)
        stop=max(i1,i2)+1
        connections=[i*len(data[0])+j1 for i in range(start,stop)]
    return connections

nodeconnections={}
opposite={}
opposite['N']='S'
opposite['S']='N'
opposite['E']='W'
opposite['W']='E'
start=[]
end=[]
simplenodes={}
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
                            if vertex not in simplenodes.keys(): simplenodes[vertex]=[nextnode[0]*len(data[0])+nextnode[1]]
                            else: simplenodes[vertex].append(nextnode[0]*len(data[0])+nextnode[1])
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
         
scores,parents=g.shortest_distances(source)

minscore=float('inf')
shortest=[]
for destination in destinations:
    if destination in scores.keys():
        # print(destination,scores[destination])
        if scores[destination]<minscore: 
            minscore=scores[destination]
            shortest=destination

print('Part 1', minscore)
print()

bestpath=getShortestPath(parents,shortest,source)
visited.update(set(bestpath))
# print(visited)
branches=findBranches(parents,bestpath)
# print(branches)
branches=set([branch for branch in branches if branch not in visited])
# print(branches)
nextnodes=findNextNodes(parents,branches,source)
# print(nextnodes)

while True:
    emptysets=[]
    for node in nextnodes:
        # print(node)
        bestpath=getShortestPath(parents,node,source)
        # print(bestpath)
        # print()
        visited.update(set(bestpath))
        # print(visited)
        branches=findBranches(parents,bestpath)
        # print(branches)
        branches=set([branch for branch in branches if branch not in visited])
        # print(branches)
        nextnodes=findNextNodes(parents,branches,source)
        # print(nextnodes)
        emptysets.append(len(nextnodes)==0)
        # print()
    if all(emptysets): break

# print(visited)


# strip off the directions
numbersonly=set()
for node in visited:
    numbersonly.add(int(node[:-1]))

# print(numbersonly)

coveredspaces=set()
# print(simplenodes)
for n in numbersonly:
    # i=n//len(data[0])
    # j=n%len(data[0])
    # # print(n//len(data[0]),n%len(data[0]))
    # data[i]=data[i][:j]+'o'+data[i][j+1:]
    for neighbor in simplenodes[n]:
        if neighbor in numbersonly:
            # print(findIntermediateNodes(n,neighbor))
            coveredspaces.update(set(findIntermediateNodes(n,neighbor)))
            # coveredspaces.add(a for a in findIntermediateNodes(n,neighbor))

for n in coveredspaces:
    i=n//len(data[0])
    j=n%len(data[0])
    # print(n//len(data[0]),n%len(data[0]))
    data[i]=data[i][:j]+'o'+data[i][j+1:]

print('Part 2',len(coveredspaces)) #485 too high 481 too high, 477 too high

for row in data:
    print(row)

# printing this out let me see where things went sideways, especially printing it out with just the < in dijkstra. Not sure how to fix it but that's
# more than enough time spent.

# for future reference, this is where both parts had issues. This was generated with just the < in dijkstra, but my search for alternate paths in the 
# part 2 section found alternate paths regardless, none of them correct, and the alternate paths are +4 from the correct path.

# #.###.#.#.#.#####.#.
# Sooooo#...#ooooooooE
# #.#o#o#####o#o#o###.
# ..#o#ooooooo#o#o....
# #.#o#####.#o#o#o####
# ...ooooooooooooo#...
# #.###.#.#.#.#.###.#.