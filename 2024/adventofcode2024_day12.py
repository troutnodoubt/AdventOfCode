fname='input_day12.txt'
# fname='example_day12a.txt'
# fname='example_day12b.txt'
# fname='example_day12c.txt'
with open(fname) as fp: data = fp.read().splitlines()

# need to find distinct regions of the same crop type
def setGraph():
    graph={k:[] for k in range(len(data)*len(data))}
    for i in range(len(data)):
        for j in range(len(data[0])):
            vertex=(i)*len(data[0])+j
            if j!= len(data[0])-1:
                # vertex to the right
                if data[i][j+1]==data[i][j]: 
                    graph[vertex].append(vertex+1) # right facing connection
                    graph[vertex+1].append(vertex) # left facing connection

            if i != len(data)-1:
                #vertex down
                if data[i+1][j]==data[i][j]: 
                    graph[vertex].append(vertex+len(data[0])) # downward connection
                    graph[vertex+len(data[0])].append(vertex) # upward connection
    return graph

graph=setGraph()
visited=list()

def dfs(visited, graph, node):  #function for dfs 
    if node not in visited:
        visited.append(node)
        for neighbor in graph[node]:
            dfs(visited, graph, neighbor)


def countSamePlantTouching(region): 
    perimeter=0
    for node in region:
        i=node//len(data)
        j=node%len(data)
        touch=0
        plot=data[i][j]
        # print(i,j,plot)
        if i==0 and j==0: #top left
            if data[i+1][j]==plot: touch+=1
            if data[i][j+1]==plot: touch+=1
        elif i==0 and j==len(data[0])-1: #top right
            if data[i+1][j]==plot: touch+=1
            if data[i][j-1]==plot: touch+=1
        elif i==0 and j in range(1,len(data[0])-1): #top row
            # print("top row")
            if data[i+1][j]==plot: touch+=1
            if data[i][j-1]==plot: touch+=1
            if data[i][j+1]==plot: touch+=1
        elif i==len(data)-1 and j==0: #bottom left
            if data[i-1][j]==plot: touch+=1
            if data[i][j+1]==plot: touch+=1
        elif i==len(data)-1 and j==len(data[0])-1: #bottom right
            if data[i-1][j]==plot: touch+=1
            if data[i][j-1]==plot: touch+=1
        elif i==len(data)-1 and j in range(1,len(data[0])-1): #bottom row
            if data[i-1][j]==plot: touch+=1
            if data[i][j-1]==plot: touch+=1
            if data[i][j+1]==plot: touch+=1
        elif i in range(1,len(data)-1) and j==0: #left column
            if data[i-1][j]==plot: touch+=1
            if data[i+1][j]==plot: touch+=1
            if data[i][j+1]==plot: touch+=1
        elif i in range(1,len(data)-1) and j==len(data[0])-1: #right column
            if data[i-1][j]==plot: touch+=1
            if data[i+1][j]==plot: touch+=1
            if data[i][j-1]==plot: touch+=1
        else:
            if data[i-1][j]==plot: touch+=1
            if data[i+1][j]==plot: touch+=1
            if data[i][j-1]==plot: touch+=1
            if data[i][j+1]==plot: touch+=1
        perimeter+=4-touch
    return perimeter
    
def calculateCost(regions,discount=False):
    cost=0
    if discount:        
        for region in regions.keys(): cost+=regions[region][1]*(regions[region][3]+regions[region][4])*2
    else:
        for region in regions.keys(): cost+=regions[region][1]*regions[region][2]
    return cost

def countUniqueHorizontalEdges(region):
    def isTopEdge(i,j):
        if i==0: return True
        elif data[i-1][j]!=data[i][j]: return True
        else: return False
    def isBottomEdge(i,j):
        if i==len(data)-1: return True
        elif data[i+1][j]!=data[i][j]: return True
        else: return False
    
        
    topcount=0
    bottomcount=0
    for node in region:
        leftTop=False
        leftBottom=False
        i=node//len(data)
        j=node%len(data)
        #look left
        if j!=0: 
            leftTop=isTopEdge(i,j-1) and data[i][j-1]==data[i][j]
            leftBottom=isBottomEdge(i,j-1) and data[i][j-1]==data[i][j]
        if not leftTop and isTopEdge(i,j): topcount+=1
        if not leftBottom and isBottomEdge(i,j): bottomcount+=1
    return topcount,bottomcount

regions={}
for i,row in enumerate(data):
    for j,plant in enumerate(row):
        visited=list()
        node=i*len(data[0])+j
        dfs(visited,graph,node)
        visited.sort()
        if tuple(visited) not in regions.keys(): regions[tuple(visited)]=[plant,0,0,0,0]
     

for region in regions.keys():
    regions[region][2]=regions[region][2]+countSamePlantTouching(region)
    regions[region][1]=len(region)
    top,bottom=countUniqueHorizontalEdges(region)
    regions[region][3]=regions[region][3]+top
    regions[region][4]=regions[region][4]+bottom

print("Part 1",calculateCost(regions))
print("Part 2",calculateCost(regions,True)) 

