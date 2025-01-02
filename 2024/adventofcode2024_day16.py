from queue import PriorityQueue

fname='input_day16.txt'
# fname='example_day16a.txt'    # 7036
# fname='example_day16b.txt'  # 11048
# fname='example_day_16c.txt' # extra input 5027
# fname='example_day_16d.txt' # extra input 21148
# fname='example_day_16e.txt' # extra input 4013
# fname='example_day_16f.txt' # test having to do a 180 on the first step 7016 works fine
# fname='example_day_16g.txt' # two endpoint paths, doesn't seem to be a problem
# fname='example_day_16h.txt' # open grid for giggles
# fname='example_day_16i.txt' # open grid for giggles
# fname='example_day_16j.txt' # open grid for giggles


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
    D = {v:[[float('inf'),(0,0)]] for v in range(graph.v)}
    D[start_vertex] = [[0,(0,1)]] #cost, heading
    
    turn=0
    nturns=0
    pq = PriorityQueue()
    pq.put((0, start_vertex)) # cost, vertex number
    
    while not pq.empty():
        (dist, current_vertex) = pq.get()
        graph.visited.append(current_vertex)
       
        # print(current_vertex)
        for neighbor in range(graph.v):
            
            
            if graph.edges[current_vertex][neighbor] != -1:
                distance = graph.edges[current_vertex][neighbor]
                if True: #neighbor not in graph.visited:
                    # print('   ',neighbor)
                    new_cost=float('inf')
                   
                    current_i=current_vertex//len(data[0])
                    current_j=current_vertex%len(data[0])
                    neighbor_i=neighbor//len(data[0])
                    neighbor_j=neighbor%len(data[0])
                    new_heading=((neighbor_i-current_i)//distance,(neighbor_j-current_j)//distance)
                    for idx,option in enumerate(D[current_vertex]): 
                        p=False
                        if len(D[current_vertex])>2: p=True
                        
                      
                        tmp_cost,heading=D[current_vertex][idx]
                        if p:
                            print()
                            print(D[current_vertex],tmp_cost,heading,current_vertex,neighbor,new_heading)
                        if new_heading!=heading: 
                            if new_heading[0]==heading[0] or new_heading[1]==heading[1]: turn=2000 #180 degree turn
                            else: turn=1000
                        elif new_heading==heading: turn=0
                        old_cost,_ = D[neighbor][0]
                        tmp_cost += distance + turn
                        acost=min([cost for cost,heading in D[neighbor]])
                        if acost!=old_cost: print('cost error',current_vertex,neighbor)
                        if tmp_cost<new_cost: new_cost=tmp_cost
                        if p: 
                            print(D[neighbor])
                            print(distance)
                            print(acost,acost==old_cost)
                            print(old_cost,tmp_cost,new_cost)
                    if new_cost < old_cost:# and new_cost%1000!=old_cost%1000:
                        # print(new_cost,new_heading,neighbor)
                        # print(current_i,current_j,neighbor_i,neighbor_j,heading,new_heading,distance)
                        # print()
                        pq.put((new_cost, neighbor))
                        # print(pq.queue)
                        D[neighbor] = [[new_cost,new_heading]]
                    elif neighbor in D.keys():
                        # print(D[neighbor])
                        
                        if [new_cost,new_heading] not in D[neighbor]: D[neighbor].append([new_cost,new_heading])
                        # print(len(D[neighbor]))
                        # if len(D[neighbor])<4: pq.put((new_cost, neighbor))
    
    return D

nvertices=len(data)*len(data[0])
nodeconnections=[[] for _ in range(nvertices)]
start=[]
end=[]

g=Graph(nvertices)

for i,row in enumerate(data):
    for j,pos in enumerate(row):
        vertex=i*len(data[0])+j
        if data[i][j]!='#':
            print(i,j,vertex)
            if data[i][j-1]!='#' or data[i][j+1]!='#':
                if data[i+1][j]!='#' or data[i-1][j]!='#': # this is a junction where we'll place a node
                    # move left, right, up, and down and find its neighboring node
                    for direction in ('l','r','u','d'):
                        nextnode=findNeighbor([i,j],direction)
                        if nextnode: nodeconnections[vertex].append(nextnode)
            if data[i][j]=='E': end=vertex
            if data[i][j]=='S': start=vertex

for node,_ in enumerate(nodeconnections):
    i=node//len(data[0])
    j=node%len(data[0])
    
    if nodeconnections[node]:
        for connection in nodeconnections[node]:
            # print(connection)
            distance=abs(connection[0]-i)+abs(connection[1]-j)
            v=connection[0]*len(data[0])+connection[1]
            # print(i,j,connection)
            # print(node,v,distance)
            g.add_edge(node, v, distance)
            # print(g.edges[node][v])
            # print()
            # print(len(nodeconnections[node]))

print()
print(start,end)
dijk = dijkstra(g,start)[end]
print(dijk)
score=dijk[0][0]

print(score) #68432 is too low. 72432, 76432 is too high. I bet I'm double counting turns somehow, so try others in increments of 1000

for test in [18242,16266,830,430]:
    print(test//len(data[0]),test%len(data[0]))
# some guy on reddit was off by 4 so I decided to try that, and sure enough I'm off by 4. 72428 is the correct answer. Don't understand why still.
# something to do with what happens if you come to a cross, and considering the path from there to be from the lowest value, not just the value you came from?
# A cross test case from here works though. https://www.reddit.com/r/adventofcode/comments/1hfiony/advent_of_code_2024_day_16_part_1_using_dijkstra/
# Might need to try on the cross I identified in the puzzle input. Towards the bottom left.

# cross vertices at 18242 (129,53), 16266 (115,51), 830 (5,125), and 430 (3,7)

# plan from here, print path to end, have to do this anyways for part 2. For the cross nodes on that path, make subgrids and verify functionality.

#69432, nope
#70432, nope
#71432, nope

# shoot

# more test cases to check https://www.reddit.com/r/adventofcode/comments/1hgyuqm/2024_day_16_part_1/, https://www.reddit.com/r/adventofcode/comments/1hfhgl1/2024_day_16_part_1_alternate_test_case/


# maybe try putting the heading inside of the D dictionary rather than the queue?