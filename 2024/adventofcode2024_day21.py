from collections import deque
from functools import lru_cache

def bfs(graph, start, parent, distance):
    q = deque()
    distance[start] = 0
    q.append(start)

    while q:
        node = q.popleft()
        for neighbor in graph[node]:
            if distance[neighbor] == float('inf'):
                parent[neighbor] = node
                distance[neighbor] = distance[node] + 1
                q.append(neighbor)

def find_shortest_distance(graph, start, destination, nvertices):
    
    
    parent = [-1] * nvertices
    distance = [float('inf')] * nvertices
    bfs(graph, start, parent, distance)

    if distance[destination] == float('inf'):
        print("Source and Destination are not connected")
        print(graph)
        return
    path = []
    current_node = destination
    path.append(destination)
    while parent[current_node] != -1:
        path.append(parent[current_node])
        current_node = parent[current_node]
    path.reverse()
    return path

def path2dpad(p):
    dpad=''
    if 10 in p:
        idx10=p.index(10)
        p[idx10]=-1
    for i in range(len(p)-1):
        test=p[i+1]-p[i]
        if test>1: dpad=dpad+'^'
        elif test<-1: dpad=dpad+'v'
        elif test==1 and p[i]!=-1: dpad=dpad+'>'
        elif test==-1 and p[i+1]!=-1: dpad=dpad+'<'
        elif test==1 and p[i]==-1: dpad=dpad+'<'
        elif test==-1 and p[i+1]==-1: dpad=dpad+'>'
    return dpad

def directionchanges(buttons):
    changes=0
    for i in range(len(buttons)-1):
        if buttons[i]!=buttons[i+1]: changes+=1
    return changes

keypad=[[] for _ in range(11)]
keypad[10]= [0,3] #node 10 is the A key, #prioritize horizontals
keypad[0]=[10,2]
keypad[1]=[2,4]
keypad[2]=[1,3,5,0]
keypad[3]=[2,10,6]
keypad[4]=[5,1,7]
keypad[5]=[4,6,2,8]
keypad[6]=[5,3,9]
keypad[7]=[8,4]
keypad[8]=[7,9,5]
keypad[9]=[8,6]

dpad=[[] for _ in range(7)]
dpad[1]=[2] #<
dpad[2]=[1,3,5] #v
dpad[3]=[2,6] #>
dpad[5]=[6,2] #^
dpad[6]=[5,3] #A

# dpad=[[] for _ in range(7)]
# dpad[1]=[2] #<
# dpad[2]=[5,1,3] #v
# dpad[3]=[6,2] #>
# dpad[5]=[2,6] #^
# dpad[6]=[3,5] #A

bestdpad={}
bestdpad[(1,1)]= ''
bestdpad[(1,2)]= '>'
bestdpad[(1,3)]= '>>'
bestdpad[(1,5)]= '>^'
bestdpad[(1,6)]= '>>^'
bestdpad[(2,1)]= '<'
bestdpad[(2,2)]= ''
bestdpad[(2,3)]= '>'
bestdpad[(2,5)]= '^'
bestdpad[(2,6)]= '^>' #or >^
bestdpad[(3,1)]= '<<'
bestdpad[(3,2)]= '<'
bestdpad[(3,3)]= ''
bestdpad[(3,5)]= '<^'# Changing this from what was attemped in the comments below + the 6,2 change found it
bestdpad[(3,6)]= '^'
bestdpad[(5,1)]= 'v<'
bestdpad[(5,2)]= 'v'
bestdpad[(5,3)]= 'v>' #or >v
bestdpad[(5,5)]= ''
bestdpad[(5,6)]= '>'
bestdpad[(6,1)]= 'v<<'
bestdpad[(6,2)]= '<v'# Changing this from what was attempted in the comments below + the 3,5 change found it
bestdpad[(6,3)]= 'v'
bestdpad[(6,5)]= '<'
bestdpad[(6,6)]= ''

def findBestButtons(start,end,pad):
    a=find_shortest_distance(pad,start,end,len(pad))
    bpress=path2dpad(a)
    nchange=directionchanges(bpress)
    if nchange>1:
        a=find_shortest_distance(pad,end,start,len(pad))
        a.reverse()
        bpress=path2dpad(a)
        nchange=directionchanges(bpress)
    print(bpress)
    if len(pad)<10: 
        print(bestdpad[(start,end)])
        print()
        bpress=bestdpad[(start,end)]
    return bpress

def dpad2nums(sequence):
    nums=''
    for s in sequence:
        if s=='<':   nums=nums+'1'
        elif s=='v': nums=nums+'2'
        elif s=='>': nums=nums+'3'
        elif s=='^': nums=nums+'5'
        elif s=='A': nums=nums+'6'
    return nums

def findchunks(sequence):
    chunks=[]
    while len(sequence)>0:
        idx=sequence.index('A')
        chunks.append(sequence[:idx+1])
        sequence=sequence[idx+1:]
    return chunks

@lru_cache(maxsize=None)
def processSequence(sequence):
    startcode='A'+dpad2nums(sequence)
    dpadseq=''
    for i in range(len(startcode)-1):
        if startcode[i]=='A': start=6
        else: start=int(startcode[i])
        if startcode[i+1]=='A': end=6
        else: end=int(startcode[i+1])
        dpadseq=dpadseq+findBestButtons(start,end,dpad)+'A'
    return dpadseq

def startingSequence(code):
    startcode='A'+code
    dpadseq=''
    for i in range(len(startcode)-1):
        if startcode[i]=='A': start=10
        else: start=int(startcode[i])
        if startcode[i+1]=='A': end=10
        else: end=int(startcode[i+1])
        # print(start,end)
        # print(findBestButtons(start,end,keypad))
        # print()
        dpadseq=dpadseq+findBestButtons(start,end,keypad)+'A'
    return dpadseq



codes=['029A',
       '980A',
       '179A',
       '456A',
       '379A']

codes=['140A', #looks like 70 is the best, as generated ^<<A^A>vvA>A
       '143A', #looks like 72 is the best, better than generated ^<<A^Av>>AvA
       '349A', #looks like 72 is the best, as generated ^A<<^A>>^AvvvA
       '582A', #looks like 68 is the best, better than generated <^^A^AvvAv>A
       '964A'] #looks like 72 is the best, as generated ^^^AvA<<A>>vvA

for code in codes: 
    print(code)
    print(startingSequence(code))

keyseqs={}
keyseqs['140A']=['^<<A^A>vvA>A','<^<A^A>vvA>A','^<<A^Av>vA>A','<^<A^Av>vA>A']
keyseqs['143A']=['^<<A^A>>vAvA','^<<A^Av>>AvA']
keyseqs['349A']=['^A<<^A>>^AvvvA','^A^<<A>>^AvvvA','^A<<^A^>>AvvvA','^A^<<A^>>AvvvA']
keyseqs['582A']=['<^^A^AvvA>vA','<^^A^AvvAv>A','^^<A^AvvA>vA','^^<A^AvvAv>A']
keyseqs['964A']=['^^^AvA<<A>>vvA','^^^AvA<<A>v>vA','^^^AvA<<Av>>vA','^^^AvA<<Av>v>A']




total=0
print()
for code in codes:
    instructionmap={}
    dpadseqs=keyseqs[code]
    complexities=[]
    for dpadseq in dpadseqs:
        instructionmap={}
        chunks=findchunks(dpadseq)
               
        for chunk in chunks:
            if chunk not in instructionmap.keys(): instructionmap[chunk]=1
            else: instructionmap[chunk]+=1
        nextmap={}
        for _ in range(25):
            for chunk in instructionmap.keys():
                nextseq=processSequence(chunk)
                nextchunks=findchunks(nextseq)
                for nextchunk in nextchunks:
                    if nextchunk not in nextmap.keys(): nextmap[nextchunk]=1*instructionmap[chunk]
                    else: nextmap[nextchunk]+=1*instructionmap[chunk]
            instructionmap=nextmap.copy()
            nextmap={}
        complexity=0
        for key in instructionmap.keys():
            complexity+=len(key)*instructionmap[key]
        # print(complexity)
        complexity*=int(code[:-1])
        complexities.append(complexity)
    print()
    print(instructionmap)
    print(code)
    print(complexities)
    total+=min(complexities)
print("total",total) # 214633893742472 too high. 

# print(instructionmap)

# None of the combinations on the keypad help from here, so my heuristic for shortest dpads must fail somewhere.
# Will have to come back and find all paths and then find the shortest resulting path for all generating paths. Must have one wrong
# Not that many combinations, try to find manually:

# <A, A, vA, ^A, >A are all trivial
# v<<A and >>vA are less likely to improve with changes
# <vA, <^A, >^A, and >vA are the only candidates. >v is not showing up in the dictionary, which is awfully suspicious.

# <vA would be v<<A>A>^A yielding v<<A, >A, and >^A
# v<A would be v<A<A>>^A yielding v<A, <A, and >>^A

# which is better v<<A or >>^A?
# v<<A would be v<A<AA>>^A yielding v<A, <A, A, >>^A
# >>^A would be vAA^<A>A yielding vA, A,^<A, >A, so it seems like v< would be preferred to <v

# <^A would be v<<A>^A>A yielding v<<A, >^A, and >A
# ^<A would be <Av<A>>^A yielding <A, v<A, and >>^A
# Already know >>^A is fewer presses than v<<A, so it seems that ^< would be preferred to <^

# >^A would be vA^<A>A yielding vA, ^<A, and >A
# ^>A would be <Av>A^A yielding <A, v>A|>vA, and ^A
# seems like either works the same

# v>A would be v<A>A^A yielding v<A, >A, ^A
# >vA would be vA<A^>A yielding vA, <A, ^>A|>^A
# seems like either works the same

#So

#1 to 2: >
#1 to 3: >>
#1 to 5: >^
#1 to 6: >>^
#2 to 1: <
#2 to 3: >
#2 to 5: ^
#2 to 6: ^> or >^
#3 to 1: <<
#3 to 2: <
#3 to 5: ^<
#3 to 6: ^
#5 to 1: v<
#5 to 2: v
#5 to 3: v> or >v
#5 to 6: >
#6 to 1: v<<
#6 to 2: v<
#6 to 3: v
#6 to 5: <

# this didn't work but reversing the 6,2 and 5,3 entries fixed it. Needed to have the BFS find all possible paths instead of finding one and tweaking.

    