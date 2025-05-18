fname='input_day10.txt'
# fname='example_day10.txt'
with open(fname) as fp: data = fp.read().splitlines()

def solve(isPart2=False):
    def setGraph():
        graph={k:[] for k in range(len(data)*len(data))}
        for i in range(len(data)):
            for j in range(len(data[0])):
                vertex=(i)*len(data[0])+j
                if j!= len(data[0])-1:
                    # vertex to the right
                    if int(data[i][j+1])-int(data[i][j])==1: graph[vertex].append(vertex+1) # right facing connection
                    elif int(data[i][j+1])-int(data[i][j])==-1: graph[vertex+1].append(vertex) # left facing connection
                
                if i != len(data)-1:
                    #vertex down
                    if int(data[i+1][j])-int(data[i][j])==1: graph[vertex].append(vertex+len(data[0])) # downward connection
                    elif int(data[i+1][j])-int(data[i][j])==-1: graph[vertex+len(data[0])].append(vertex) # upward connection
        return graph

    def findElevations(elevation):
        elList=[]
        for i,line in enumerate(data):
            for j,el in enumerate(line):
                if int(el)==elevation: elList.append((i,j))
        return elList
        
    graph=setGraph()
    visited=[]

    def dfs(visited, graph, node):  #function for dfs 
        if node not in visited or isPart2:
            visited.append(node)
            for neighbor in graph[node]:
                dfs(visited, graph, neighbor)
    
    count=0
    for zero in findElevations(0):
        visited=[]

        node=zero[0]*len(data[0])+zero[1]
        dfs(visited,graph,node)
        for loc in visited:
            i=loc//len(data)
            j=loc%len(data)
            if int(data[i][j])==9: count+=1
    return count

print("Part 1",solve())
print("Part 2",solve(True))
