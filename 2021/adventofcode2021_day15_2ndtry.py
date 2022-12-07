#from collections import defaultdict
import numpy as np
from numpy import Inf
fname="C://Users/Mark/Documents/Advent of Code/2021/day_15_example.txt"
#fname="C://Users/Mark/Documents/Advent of Code/2021/input_day15.txt"
with open(fname) as fp: data = fp.read().splitlines()


danger=[[int(a) for a in row] for row in data]

danger=np.array(danger)





def findneighbors(danger,threshold):
    a=danger<threshold
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
                        neighborlist.append((i+1,j,1+abs(danger[i+1][j]-danger[i][j])))
                    if a[i][j+1] and (i,j+1):# not in neighbors.keys():
                        neighborlist.append((i,j+1,1+abs(danger[i][j+1]-danger[i][j])))
                elif i==len(danger)-1 and j==0:
                    # print('bottom left corner')
                    if a[i-1][j] and (i-1,j):# not in neighbors.keys():
                        neighborlist.append((i-1,j,1+abs(danger[i-1][j]-danger[i][j])))
                    if a[i][j+1] and (i,j+1):# not in neighbors.keys():
                        neighborlist.append((i,j+1,1+abs(danger[i][j+1]-danger[i][j])))
                elif i==0 and j==len(danger)-1:
                    # print('top right corner')
                    if a[i+1][j] and (i+1,j):# not in neighbors.keys():
                        neighborlist.append((i+1,j,1+abs(danger[i+1][j]-danger[i][j])))
                    if a[i][j-1] and (i,j-1):# not in neighbors.keys():
                        neighborlist.append((i,j-1,1+abs(danger[i][j-1]-danger[i][j])))
                elif i==len(danger)-1 and j==len(danger)-1:
                    # print('bottom right corner')
                    if a[i-1][j] and (i-1,j):# not in neighbors.keys():
                        neighborlist.append((i-1,j,1+abs(danger[i-1][j]-danger[i][j])))
                    if a[i][j-1] and (i,j-1):# not in neighbors.keys():
                        neighborlist.append((i,j-1,1+abs(danger[i][j-1]-danger[i][j])))
                #edges
                elif i==0 and j>0 and j<len(danger)-1:
                    # print('top edge, no corners')
                    if a[i+1][j] and (i+1,j):# not in neighbors.keys():
                        neighborlist.append((i+1,j,1+abs(danger[i+1][j]-danger[i][j])))
                    # if a[i+1][j-1]:
                    #     neighborlist.append((i+1,j-1))
                    # if a[i+1][j+1]:
                    #     neighborlist.append((i+1,j+1))
                    if a[i][j+1] and (i,j+1):# not in neighbors.keys():
                        neighborlist.append((i,j+1,1+abs(danger[i][j+1]-danger[i][j])))
                    if a[i][j-1] and (i,j-1):# not in neighbors.keys():
                        neighborlist.append((i,j-1,1+abs(danger[i][j-1]-danger[i][j])))
                elif i==len(danger)-1 and j>0 and j<len(danger)-1:
                    # print('bottom edge, no corners')
                    #     neighborlist.append((i-1,j-1))
                    if a[i-1][j] and (i-1,j):# not in neighbors.keys():
                        neighborlist.append((i-1,j,1+abs(danger[i-1][j]-danger[i][j])))
                    # if a[i-1][j+1]:
                    #     neighborlist.append((i-1,j+1))
                    
                    if a[i][j+1] and (i,j+1):# not in neighbors.keys():
                        neighborlist.append((i,j+1,1+abs(danger[i][j+1]-danger[i][j])))
                    if a[i][j-1] and (i,j-1):# not in neighbors.keys():
                        neighborlist.append((i,j-1,1+abs(danger[i][j-1]-danger[i][j])))    
                    
                elif i>0 and i<len(danger)-1 and j==0:
                    # print('left edge, no corners')
                    if a[i+1][j] and (i+1,j):# not in neighbors.keys():
                        neighborlist.append((i+1,j,1+abs(danger[i+1][j]-danger[i][j])))
                    if a[i-1][j] and (i-1,j):# not in neighbors.keys():
                        neighborlist.append((i-1,j,1+abs(danger[i-1][j]-danger[i][j])))
                    # if a[i+1][j+1]:
                    #     neighborlist.append((i+1,j+1))
                    # if a[i-1][j+1]:
                    #     neighborlist.append((i-1,j+1))
                    if a[i][j+1] and (i,j+1):# not in neighbors.keys():
                        neighborlist.append((i,j+1,1+abs(danger[i][j+1]-danger[i][j])))
                elif i>0 and i<len(danger)-1 and j==len(danger)-1:
                    # print('right edge, no corners')
                    if a[i+1][j] and (i+1,j):# not in neighbors.keys():
                        neighborlist.append((i+1,j,1+abs(danger[i+1][j]-danger[i][j])))
                    if a[i-1][j] and (i-1,j):# not in neighbors.keys():
                        neighborlist.append((i-1,j,1+abs(danger[i-1][j]-danger[i][j])))
                    # if a[i+1][j+1]:
                    #     neighborlist.append((i+1,j+1))
                    # if a[i-1][j+1]:
                    #     neighborlist.append((i-1,j+1))
                    if a[i][j-1] and (i,j-1):# not in neighbors.keys():
                        neighborlist.append((i,j-1,1+abs(danger[i][j-1]-danger[i][j])))
                else:
                    # print('body')
                    if a[i+1][j] and (i+1,j):# not in neighbors.keys():
                        neighborlist.append((i+1,j,1+abs(danger[i+1][j]-danger[i][j])))
                    if a[i-1][j] and (i-1,j):# not in neighbors.keys():
                        neighborlist.append((i-1,j,1+abs(danger[i-1][j]-danger[i][j])))
                    # if a[i+1][j+1]:
                    #     neighborlist.append((i+1,j+1))
                    # if a[i-1][j+1]:
                    #     neighborlist.append((i-1,j+1))
                    if a[i][j-1] and (i,j-1):# not in neighbors.keys():
                        neighborlist.append((i,j-1,1+abs(danger[i][j-1]-danger[i][j])))
                    if a[i][j+1] and (i,j+1):# not in neighbors.keys():
                        neighborlist.append((i,j+1,1+abs(danger[i][j+1]-danger[i][j])))
             
                neighbors[(i,j)]=neighborlist
    return neighbors


# def DFS(b,start,end,path):
#     print(path)
#     if start==end:
#        return path
#     else:
#         for coordinate in b[start]:
#             print(path)
#             path.append(coordinate)
            
#             DFS(b,coordinate,end,path)
#             path.pop()

# def findPaths(b,start,end,allpaths):
#     path=list()
#     path.append(start)
#     DFS(b,start,end,path)


def naive_dijkstras(graph,root):
    n=len(graph)                    
    
    for i in graph.keys():
        dist[i]=Inf
        visited[i]=False

    dist[root]=0
    
    for i in graph.keys():
        
    
    for _ in range(n):
        u=(-1,-1)
        for i in graph.keys():
            if not visited[i] and (u==(-1,-1) or dist[i]<dist[u]):
                u=i
        if dist[u]==Inf:
            break
        visited[u]=True
        
        for v in graph[u]:
            if dist[u]+1<dist[v]:
                dist[v]=dist[u]+1
                
    return(dist)
         
print(naive_dijkstras(b,(0,0)))


threshold=10                

b=findneighbors(danger,threshold)

start=(0,0)
end=(9,9)

path=list()

#test=DFS(b,start,end,path)

    


            

