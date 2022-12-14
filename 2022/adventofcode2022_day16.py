import re
from queue import PriorityQueue

fname="day16_example.txt"
fname="input_day16.txt"
with open(fname) as fp: data = fp.read().splitlines()

class Valve:
    def __init__(self, name, idx, rate):
        self.name=name
        self.idx=idx
        self.rate=rate

class Graph:
    def __init__(self, num_of_vertices):
        self.v = num_of_vertices
        self.edges = [[-1 for i in range(num_of_vertices)] for j in range(num_of_vertices)]
        self.visited = []
        
    def add_edge(self, u, v, weight):
        self.edges[u][v] = 1*weight
        self.edges[v][u] = 1*weight
        
        
def dijkstra(graph, start_vertex):
    D = {v:float('inf') for v in range(graph.v)}
    D[start_vertex] = 0

    pq = PriorityQueue()
    pq.put((0, start_vertex))

    while not pq.empty():
        (dist, current_vertex) = pq.get()
        graph.visited.append(current_vertex)

        for neighbor in range(graph.v):
            if graph.edges[current_vertex][neighbor] != -1:
                distance = graph.edges[current_vertex][neighbor]
                if neighbor not in graph.visited:
                    old_cost = D[neighbor]
                    new_cost = D[current_vertex] + distance
                    if new_cost < old_cost:
                        pq.put((new_cost, neighbor))
                        D[neighbor] = new_cost
    return D
        
def distance(start,finish):
    g=Graph(len(data))
    for row in data:
        valves=re.findall('[A-Z][A-Z]',row)
        for valve in valves[1:]:
            g.add_edge(valvedict[valves[0]],valvedict[valve],1)
    return(dijkstra(g, valvedict[start])[valvedict[finish]])
    del(g)
       
def permutation(lst): # permutation function stolen from the web somewhere
    # If lst is empty then there are no permutations
    if len(lst) == 0:
        return []
    # If there is only one element in lst then, only
    # one permutation is possible
    if len(lst) == 1:
        return [lst]
    # Find the permutations for lst if there are
    # more than 1 characters
    l = [] # empty list that will store current permutation
    # Iterate the input(lst) and calculate the permutation
    for i in range(len(lst)):
        m = lst[i]
        # Extract lst[i] or m from the list.  remLst is
        # remaining list
        remLst = lst[:i] + lst[i+1:]
        # Generating all permutations where m is first
        # element
        for p in permutation(remLst):
            l.append([m] + p)
    return l

def calculatepressure(lst,t):
    #t=30
    p_released=0
    for idx in range(1,len(lst)):
        t-=distancedict[(lst[idx-1],lst[idx])]+1
        if t<=0: break
        p_released+=t*valves[lst[idx]].rate
    return(p_released)
    
def optimizepath(lst,ti):
    perms=permutation(lst)
    #print(perms)
    pscore=0
    for p in perms:
        cand=['AA', *p]
        newpscore=calculatepressure(cand,ti)
        if newpscore>pscore: 
            pscore=newpscore
    return(pscore)
    

# create index dictionary for use in dijkstra
index=0
valvedict={}
for row in data:
    valvedict[re.findall('[A-Z][A-Z]',row)[0]]=index
    index+=1

# calculate matrix of distance between valves that actually do something, so 
# that it only has to calculate distances once. Include starting point AA


valves={}
    
for row in data:
    valvenames=re.findall('[A-Z][A-Z]',row)
    pdecay=int(re.findall('[0-9]+',row)[0])
    if pdecay>0 or valvenames[0]=='AA': 
        valves[valvenames[0]]=valves.get(valvenames[0], Valve(valvenames[0], valvedict[valvenames[0]], pdecay))

distancedict={}
for begin in valves.keys():
    for end in valves.keys():
        distancedict[(begin,end)]=distance(begin,end)
        
# build all possible paths
valvelist=[valve for valve in valves.keys()]

valvesequence=['AA']
valvelist.remove('AA')
permutecount=0
score=0

# separate into two lists based on size to reduce number of permutations
threshold=10
highflow=[]
lowflow=[]
for v in valvelist:
    if valves[v].rate >= threshold:
        highflow.append(v)
    else:
        lowflow.append(v)

phigh=permutation(highflow)
plow=permutation(lowflow)

print('permutations complete')
print(len(phigh),len(plow))
print('possible combinations',len(phigh)*len(plow))
time=30
for h in phigh:
    for l in plow:
        candidate=['AA',*h,*l]
        if calculatepressure(candidate,time) > score: 
            score = calculatepressure(candidate,time)
            print()
            print(score)
        
#1206 too low (high/low threshold at 15)
#1219 too low (threshold at 13)
#1460 is right!! (threshold at 10)

print('Part 1 solution is', score)  

# make a mask to divide the valves roughly in two

mask=[]

for i in range(2**len(valvelist)):
    binmask=bin(i)
    pad=0
    if len(binmask[2:])<len(valvelist): # need to pad zeros
        pad=len(valvelist)-len(binmask[2:])
    if binmask.count('1')==len(valvelist)//2:
        currentmask=[int(bit) for bit in binmask[2:]]
        for p in range(pad):
            currentmask.insert(0,0)
        mask.append(currentmask)

# iterate part 1 solution over all masks
score=0
time=26
count=0
for m in mask:
    mypath=[]
    elephantpath=[]
    for idx in range(len(m)):
        if m[idx]==1:
            mypath.append(valvelist[idx])
        elif m[idx]==0:
            elephantpath.append(valvelist[idx])
        else:
            print('oh dear')

    count+=1
    
    myscore=optimizepath(mypath, time)

    elescore=optimizepath(elephantpath, time)
            
    newscore=elescore+myscore
    
    if newscore>score:
        score=newscore
        print('New potential solution',score)
        print('Completed',count,'of', len(mask))

print('Part 2 solution is', score)

# correct mypath is JJ, BB, CC
# correct elepath is DD, HH, EE