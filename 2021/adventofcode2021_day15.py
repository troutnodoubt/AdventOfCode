#from collections import defaultdict
import numpy as np
# from numpy import Inf
fname="C://Users/Mark/Documents/Advent of Code/2021/day_15_example.txt"
fname="C://Users/Mark/Documents/Advent of Code/2021/input_day15.txt"
with open(fname) as fp: data = fp.read().splitlines()


danger=[[int(a) for a in row] for row in data]

#danger=np.array(danger)





# def findneighbors(danger,threshold):
def findneighbors(danger):
   # a=danger<threshold
    a=danger
    #print(a.all())
    neighbors=dict()
    
    for i in range(len(danger)):
        for j in range(len(danger)):
            # print(i,j)
            neighborlist=list()
            if a[i][j]:
                #corners
                if i==0 and j==0:
                    # print('top left corner')
                    if a[i+1][j] and (i+1,j):# not in neighbors.keys():
                        neighborlist.append((i+1,j))
                    if a[i][j+1] and (i,j+1):# not in neighbors.keys():
                        neighborlist.append((i,j+1))
                elif i==len(danger)-1 and j==0:
                    # print('bottom left corner')
                    if a[i-1][j] and (i-1,j):# not in neighbors.keys():
                        neighborlist.append((i-1,j))
                    if a[i][j+1] and (i,j+1):# not in neighbors.keys():
                        neighborlist.append((i,j+1))
                elif i==0 and j==len(danger)-1:
                    # print('top right corner')
                    if a[i+1][j] and (i+1,j):# not in neighbors.keys():
                        neighborlist.append((i+1,j))
                    if a[i][j-1] and (i,j-1):# not in neighbors.keys():
                        neighborlist.append((i,j-1))
                elif i==len(danger)-1 and j==len(danger)-1:
                    # print('bottom right corner')
                    if a[i-1][j] and (i-1,j):# not in neighbors.keys():
                        neighborlist.append((i-1,j))
                    if a[i][j-1] and (i,j-1):# not in neighbors.keys():
                        neighborlist.append((i,j-1))
                #edges
                elif i==0 and j>0 and j<len(danger)-1:
                    # print('top edge, no corners')
                    if a[i+1][j] and (i+1,j):# not in neighbors.keys():
                        neighborlist.append((i+1,j))
                    # if a[i+1][j-1]:
                    #     neighborlist.append((i+1,j-1))
                    # if a[i+1][j+1]:
                    #     neighborlist.append((i+1,j+1))
                    if a[i][j+1] and (i,j+1):# not in neighbors.keys():
                        neighborlist.append((i,j+1))
                    if a[i][j-1] and (i,j-1):# not in neighbors.keys():
                        neighborlist.append((i,j-1))
                elif i==len(danger)-1 and j>0 and j<len(danger)-1:
                    # print('bottom edge, no corners')
                    #     neighborlist.append((i-1,j-1))
                    if a[i-1][j] and (i-1,j):# not in neighbors.keys():
                        neighborlist.append((i-1,j))
                    # if a[i-1][j+1]:
                    #     neighborlist.append((i-1,j+1))
                    
                    if a[i][j+1] and (i,j+1):# not in neighbors.keys():
                        neighborlist.append((i,j+1))
                    if a[i][j-1] and (i,j-1):# not in neighbors.keys():
                        neighborlist.append((i,j-1))    
                    
                elif i>0 and i<len(danger)-1 and j==0:
                    # print('left edge, no corners')
                    if a[i+1][j] and (i+1,j):# not in neighbors.keys():
                        neighborlist.append((i+1,j))
                    if a[i-1][j] and (i-1,j):# not in neighbors.keys():
                        neighborlist.append((i-1,j))
                    # if a[i+1][j+1]:
                    #     neighborlist.append((i+1,j+1))
                    # if a[i-1][j+1]:
                    #     neighborlist.append((i-1,j+1))
                    if a[i][j+1] and (i,j+1):# not in neighbors.keys():
                        neighborlist.append((i,j+1))
                elif i>0 and i<len(danger)-1 and j==len(danger)-1:
                    # print('right edge, no corners')
                    if a[i+1][j] and (i+1,j):# not in neighbors.keys():
                        neighborlist.append((i+1,j))
                    if a[i-1][j] and (i-1,j):# not in neighbors.keys():
                        neighborlist.append((i-1,j))
                    # if a[i+1][j+1]:
                    #     neighborlist.append((i+1,j+1))
                    # if a[i-1][j+1]:
                    #     neighborlist.append((i-1,j+1))
                    if a[i][j-1] and (i,j-1):# not in neighbors.keys():
                        neighborlist.append((i,j-1))
                else:
                    # print('body')
                    if a[i+1][j] and (i+1,j):# not in neighbors.keys():
                        neighborlist.append((i+1,j))
                    if a[i-1][j] and (i-1,j):# not in neighbors.keys():
                        neighborlist.append((i-1,j))
                    # if a[i+1][j+1]:
                    #     neighborlist.append((i+1,j+1))
                    # if a[i-1][j+1]:
                    #     neighborlist.append((i-1,j+1))
                    if a[i][j-1] and (i,j-1):# not in neighbors.keys():
                        neighborlist.append((i,j-1))
                    if a[i][j+1] and (i,j+1):# not in neighbors.keys():
                        neighborlist.append((i,j+1))
             
                neighbors[(i,j)]=neighborlist
    return neighbors


# def dijkstra(nodes, distances):
#     # These are all the nodes which have not been visited yet
#     unvisited = {node: None for node in nodes}
#     # It will store the shortest distance from one node to another
#     visited = {}
#     current = start
#     # It will store the predecessors of the nodes
#     currentDistance = 0
#     unvisited[current] = currentDistance
#     # Running the loop while all the nodes have been visited
#     while True:
#         # iterating through all the unvisited node
#         for neighbour, distance in distances[current].items():
#             # Iterating through the connected nodes of current_node (for 
#             # example, a is connected with b and c having values 10 and 3
#             # respectively) and the weight of the edges
#             if neighbour not in unvisited: continue
#             newDistance = currentDistance + distance
#             if unvisited[neighbour] is None or unvisited[neighbour] > newDistance:
#                 unvisited[neighbour] = newDistance
#         # Till now the shortest distance between the source node and target node 
#         # has been found. Set the current node as the target node
#         visited[current] = currentDistance
#         del unvisited[current]
#         if not unvisited: break
#         candidates = [node for node in unvisited.items() if node[1]]
#         current, currentDistance = sorted(candidates, key = lambda x: x[1])[0]
#     return visited


def dijkstra(nodes,penalties):
    unvisited={node: None for node in nodes}
    visited={}
    current=(0,0)
    currentpenalty=0
    unvisited[current]=currentpenalty
    while True:
        for neighbor in nodes[current]:
            if neighbor not in unvisited: continue
            newpenalty=currentpenalty+penalties[neighbor]
            if unvisited[neighbor] is None or unvisited[neighbor] > newpenalty:
                unvisited[neighbor]=newpenalty
        visited[current]=currentpenalty
        del unvisited[current]
        print(len(unvisited))
        if not unvisited: break
        candidates = [node for node in unvisited.items() if node[1]]
        current, currentpenalty = sorted(candidates, key = lambda x: x[1])[0]
    return visited
        
        
                
            

                      

#threshold=11               
penalty=dict()
# neighbors=findneighbors(danger,threshold)
neighbors=findneighbors(danger)
for key in neighbors.keys():
    penalty[key]=danger[key[0]][key[1]]
    
start=(0,0)
end=(len(danger)-1,len(danger)-1)

distances=dijkstra(neighbors,penalty)

print('Part 1 solution is',distances[end])

# Duplicate array

danger=np.array(danger)
newdanger=np.empty((5*len(danger),5*len(danger)))
# for n in range(5):
#     for m in range(5):
#         for i in range(len(danger)):
#             for j in range(len(danger)):
#                 newdanger[n*len(danger)+i][m*len(danger)+j]=(n+m+1)*danger[i][j]
#                 if newdanger[n*len(danger)+i][m*len(danger)+j]>9:
#                     newdanger[n*len(danger)+i][m*len(danger)+j]=1

for i in range(len(danger)):
    for j in range(len(danger)):
        newdanger[i][j]=danger[i][j]
        

for i in range(len(newdanger)):
    for j in range(len(danger)):
        if i>=len(danger):
            newdanger[i][j]=newdanger[i-len(danger)][j]+1
            if newdanger[i][j]>9: newdanger[i][j]=1
            
for i in range(len(newdanger)):
    for j in range(len(newdanger)):
        if j>=len(danger):
            newdanger[i][j]=newdanger[i][j-len(danger)]+1
            if newdanger[i][j]>9: newdanger[i][j]=1
            
            

penalty=dict()
# neighbors=findneighbors(danger,threshold)
neighbors=findneighbors(newdanger)
for key in neighbors.keys():
    penalty[key]=newdanger[key[0]][key[1]]
    
start=(0,0)
end=(len(newdanger)-1,len(newdanger)-1)

distances=dijkstra(neighbors,penalty)

print('Part 2 solution is',distances[end])
    


            

