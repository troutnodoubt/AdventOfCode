from queue import PriorityQueue

fname='input_day16.txt'
fname='example_day16a.txt'
# fname='example_day16b.txt'
with open(fname) as fp: data = fp.read().splitlines()

def findNeighbor(node,direction):
    neighborFound=False
    if   direction=='u': 
        d=(-1, 0)
        normal=(0,1)
    elif direction=='d': 
        d=( 1 ,0)
        normal=(0,1)
    elif direction=='l': 
        d=( 0,-1)
        normal=(1,0)
    elif direction=='r':
        d=( 0 ,1)
        normal=(1,0)
    testnode=[node[0],node[1]]
    while not neighborFound:
        testnode=[testnode[0]+d[0],testnode[1]+d[1]]
        nextnode=[testnode[0]+d[0],testnode[1]+d[1]]
        normal1 =[testnode[0]+normal[0],testnode[1]+normal[1]]
        normal2 =[testnode[0]-normal[0],testnode[1]-normal[1]]

        if data[testnode[0]][testnode[1]]!='#' and (data[nextnode[0]][nextnode[1]]=='#' or data[normal1[0]][normal1[1]]!='#' or data[normal2[0]][normal2[1]]!='#'):
            return(testnode) 
        elif data[testnode[0]][testnode[1]]=='#':
            return []

class Graph:
    def __init__(self, num_of_vertices):
        self.v = num_of_vertices
        self.edges = [[-1 for i in range(num_of_vertices)] for j in range(num_of_vertices)]
        self.visited = []
        # self.coordinates= [[] for i in range(num_of_vertices)]
        self.heading=[]
        
    def add_edge(self, u, v, distance):
        # print('setting edge',u,v,distance)
        self.edges[u][v] = distance
        self.edges[v][u] = distance
        
def dijkstra(graph, start_vertex):
    D = {v:float('inf') for v in range(graph.v)}
    D[start_vertex] = 0
    
    turn=0
    nturns=0
    pq = PriorityQueue()
    pq.put((0, (0,1), start_vertex, nturns)) # cost, heading, vertex number
    
    while not pq.empty():
        (dist, heading, current_vertex,nturns) = pq.get()
        graph.visited.append(current_vertex)

        for neighbor in range(graph.v):
            
            if graph.edges[current_vertex][neighbor] != -1:
                distance = graph.edges[current_vertex][neighbor]
                if neighbor not in graph.visited:
                    
                    current_i=current_vertex//len(data)
                    current_j=current_vertex%len(data)
                    neighbor_i=neighbor//len(data)
                    neighbor_j=neighbor%len(data)
                    new_heading=((neighbor_i-current_i)//distance,(neighbor_j-current_j)//distance)
                    
                    if new_heading!=heading: 
                        # nturns=1
                        turn=1000
                    elif new_heading==heading: turn=0
                    old_cost = D[neighbor]
                    new_cost = D[current_vertex] + distance + turn
                    # new_cost = D[current_vertex] + distance + nturns*1000
                    
                    if new_cost < old_cost and new_cost%1000!=old_cost%1000:
                        # print(new_cost,new_heading,neighbor)
                        # print(current_i,current_j,neighbor_i,neighbor_j,heading,new_heading,distance)
                        # print()
                        pq.put((new_cost, new_heading, neighbor, nturns))
                        D[neighbor] = new_cost
    return D

nvertices=len(data)*len(data[0])
nodeconnections=[[] for _ in range(nvertices)]
start=[]
end=[]

g=Graph(nvertices)

for i,row in enumerate(data):
    for j,pos in enumerate(row):
        vertex=i*len(data)+j
        if data[i][j]!='#':
            if data[i][j-1]!='#' or data[i][j+1]!='#':
                if data[i+1][j]!='#' or data[i-1][j]!='#': # this is a junction where we'll place a node
                    # move left, right, up, and down and find its neighboring node
                    for direction in ('l','r','u','d'):
                        nextnode=findNeighbor([i,j],direction)
                        if nextnode: nodeconnections[vertex].append(nextnode)
            if data[i][j]=='E': end=vertex
            if data[i][j]=='S': start=vertex

for node,_ in enumerate(nodeconnections):
    i=node//len(data)
    j=node%len(data)
    
    if nodeconnections[node]:
        for connection in nodeconnections[node]:
            # print(connection)
            distance=abs(connection[0]-i)+abs(connection[1]-j)
            v=connection[0]*len(data)+connection[1]
            # print(i,j,connection)
            # print(node,v,distance)
            g.add_edge(node, v, distance)
            # print(g.edges[node][v])
            # print()
            # print(len(nodeconnections[node]))

print()
print(start,end)
score = dijkstra(g,start)[end]
print(score) #68432 is too low. 72432, 76432 is too high. I bet I'm double counting turns somehow, so try others in increments of 1000
#69432, nope
#70432, nope
#71432, nope

# shoot

# more test cases to check https://www.reddit.com/r/adventofcode/comments/1hgyuqm/2024_day_16_part_1/, https://www.reddit.com/r/adventofcode/comments/1hfhgl1/2024_day_16_part_1_alternate_test_case/


# maybe try putting the heading inside of the D dictionary rather than the queue?