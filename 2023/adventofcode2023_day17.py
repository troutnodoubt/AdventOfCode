from queue import PriorityQueue
from numpy import inf

fname='input_day17.txt'
fname='example_day17.txt'
with open(fname) as fp: data = fp.read().splitlines()

class Graph:
    def __init__(self, num_of_vertices):
        self.v = num_of_vertices
        self.edges = [[-1 for i in range(num_of_vertices)] for j in range(num_of_vertices)]
        self.visited = []
        
    def add_edge(self, u, v, weightu, weightv):
        self.edges[u][v] = weightu
        self.edges[v][u] = weightv
      
        
def dijkstra(graph, start_vertex):
    D = {v:float('inf') for v in c} #range(graph.v)}
    D[start_vertex] = 0
    path={v:0 for v in c} #range(graph.v)}

    pq = PriorityQueue()
    pq.put((0, start_vertex))
    # last4=[start_vertex]
    # penalty=False
    while not pq.empty():
        # d=[]
        (dist, current_vertex) = pq.get()
        #print(dist,current_vertex)
        # graph.visited.append(current_vertex)
        
        

        for neighbor in c: #(graph.v):
            # if neighbor-current_vertex==1: print('moving right')
            # elif neighbor-current_vertex==-1: print('moving left')
            # elif neighbor-current_vertex==len(data[0]): print('moving down')
            # elif neighbor- current_vertex==-len(data[0]): print('moving up')

            if graph.edges[current_vertex][neighbor] != -1:
                distance = graph.edges[current_vertex][neighbor]
                if True: #neighbor not in graph.visited:
                    penalty=False
                    #last=[current_vertex,path[current_vertex],path[path[current_vertex]],path[path[path[current_vertex]]], path[path[path[path[current_vertex]]]]]
                    last=[neighbor,current_vertex,path[current_vertex],path[path[current_vertex]],path[path[path[current_vertex]]]]
                    d=[]
                    for i in range(len(last)-1):
                        d.append(last[i+1]-last[i])
                        
                    if len(set(d))==1:
                        penalty=True
                        print('penalty on the play')
                        print(last)
                    # if 7 in last: 
                        # print(last)
                        # print(d)
                    old_cost = D[neighbor]
                    new_cost = D[current_vertex] + distance #+ penalty
                    #print(penalty,new_cost)
                    if new_cost < old_cost and not penalty:
                        
                        # print(last4)
                        # if len(last4)>4: last4=last4[-4:]
                        # print(last4)
                        # if len(last4)==4:
                        #     for i in range(len(last4)-1):
                        #         d.append(last4[i+1]-last4[i])
                        #     if len(set(d))==1:
                        #         penalty=True
                        #         print('penalty enforced')
                        #     else:
                        #         penalty=False
                        # # if len(last4)<4 or not penalty:
                    
        
                      
                        pq.put((new_cost, neighbor))
                        D[neighbor] = new_cost
                        path[neighbor]=current_vertex
                        graph.visited.append(current_vertex)
                            
    print(path)
    return D

        
        
def setedges():
    for i in range(len(data)):
        for j in range(len(data[0])):
            vertex=(i)*len(data[0])+j
            #print(vertex)
          
            if j != len(data[0])-1: 
                #vertex right
                weightu=int(data[i][j+1])
                weightv=int(data[i][j])
                g.add_edge(vertex, vertex+1, weightu, weightv )
            
            if i != len(data)-1:
                #vertex down
                weightu=int(data[i+1][j])
                weightv=int(data[i][j])
                g.add_edge(vertex, vertex+len(data[0]), weightu, weightv)

g=Graph(len(data)*len(data[0]))

start_vertex=0

setedges()

a=[168,155,142,129,128,115,116,103,90,77,76,63,62,49,36,35,22,21,20,7,6,5,4,17,16,15,2,1,0]
a.reverse()
b=[168,167,154,141,142,129,116,103,102,89,76,63,62,49,36,35,34,21,8,7,6,5,18,17,16,15,2,1,0]
b.reverse()

c=set([*a,*b])
print(c)

for v in c:
    i=v//len(data[0])
    j=v%len(data[0])
    print(v,i,j,data[i][j])

D = dijkstra(g, start_vertex)

total=0
totalb=0
for i in range(len(a)-1):
    total+=g.edges[a[i]][a[i+1]]
    totalb+=g.edges[b[i]][b[i+1]]
   # print(total,totalb)
#print('Part 1 solution is', D[end_vertex])