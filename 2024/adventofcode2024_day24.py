
fname='input_day24.txt'
fname='input_day24_working.txt'
# fname='example_day24a.txt'
# fname='example_day24b.txt'
with open(fname) as fp: data = fp.read().splitlines()

connections=[]
knownGates={}


def setGraph():
    graph={}
    for row in data:
        if '->' in row:
            vals=[a for a in row.split(' ') if a!='->']
            graph[vals[-1]]=[vals[0],vals[2],vals[1]]
        elif ':' in row:
            graph[row.split(' ')[0][:-1]]=[]
    return graph

visited=list()
graph=setGraph()

def dfs(visited, graph, node):  #function for dfs 
    if node not in visited:
        visited.append(node)
        for neighbor in graph[node][:-1]:
            dfs(visited, graph, neighbor)

def setconnections():
    for row in data:
        if ':' in row:
            knownGates[row.split(' ')[0][:-1]]=int(row.split(' ')[1])
        elif '->' in row: 
            connections.append([a for a in row.split(' ') if a!='->'])
    

def findBadBits(x,y,toCompute):
    shouldbe=x+y
    addend=adderMachine(toCompute,x,y)
    return shouldbe^addend

def adderMachine(toCompute,x,y):
    bitlistx=[]
    bitlisty=[]
    # print('0b'+bin(x)[2:].zfill(45))
    for bit in bin(x)[2:].zfill(45)[::-1]: 
        # print(bit)
        bitlistx.append(int(bit))
    for bit in bin(y)[2:].zfill(45)[::-1]: 
        # print(bit)
        bitlisty.append(int(bit))
    for i in range(45):
        xkey='x'+str(i).zfill(2)
        ykey='y'+str(i).zfill(2)
        knownGates[xkey]=bitlistx[i]
        knownGates[ykey]=bitlisty[i]
        # print(xkey,testdict[xkey],knownGates[xkey])
    count=0
    while len(toCompute)>0:
        # print(toCompute)
        # print()
        count+=1
        for gate in toCompute:
            if gate[0] in knownGates.keys() and gate[2] in knownGates.keys():
                if   gate[1]=='AND': res=knownGates[gate[0]]&knownGates[gate[2]]
                elif gate[1]=='OR':  res=knownGates[gate[0]]|knownGates[gate[2]]
                elif gate[1]=='XOR': res=knownGates[gate[0]]^knownGates[gate[2]]
                knownGates[gate[3]]=res
                toCompute.remove(gate)
        if count>10000: break #something's wrong

    final='0b'
    for i in reversed(range(46)): 
        gate='z'+str(i).zfill(2)
        final=final+str(knownGates[gate])
    return(eval(final))

setconnections()
xnum=''
ynum=''
for key in knownGates:
    if 'x' in key:
        xnum=xnum+str(knownGates[key])
    if 'y' in key:
        ynum=ynum+str(knownGates[key])
xnum=xnum+'b0'
ynum=ynum+'b0'
xnum=xnum[::-1]
ynum=ynum[::-1]
x=eval(xnum)
y=eval(ynum)
# print(xnum,x)
# print(ynum,y)
result=adderMachine(connections,x,y)
print('Part 1',result)

mask=eval('0b'+'1'*45)

badbitlist=[]
for xtest in [x,0,mask]:
    for ytest in [y,0,mask]:
        badbits=findBadBits(xtest,ytest,connections)
        result=adderMachine(connections,xtest,ytest)
        # print(xtest,ytest,xtest+ytest)
        # print(result)
        # print(bin(result))
        # print('0b'+bin(xtest+ytest)[2:].zfill(46))
        # print('0b'+bin(badbits)[2:].zfill(46))
        # print()
        badbitlist.append(badbits)

commonbits=eval('0b'+'1'*46)
candidate=[]
maxwrong=46
for badbits in badbitlist:
    # print('0b'+bin(commonbits)[2:].zfill(46))
    # print('0b'+bin(badbits)[2:].zfill(46))
    # print()
    nwrong=sum([int(a) for a in bin(badbits)[2:].zfill(46)])
    if nwrong<maxwrong: 
        maxwrong=nwrong
        candidate=badbits
    commonbits&=badbits

candidatebits=[]
print(bin(candidate)[2:].zfill(46))
# print(bin(candidate)[2:].zfill(46)[::-1])
for i,bit in enumerate(bin(candidate)[2:].zfill(46)[::-1]):
    # print(i,'z'+str(i).zfill(2),bit)
    if int(bit)==1: candidatebits.append('z'+str(i).zfill(2))
    
setconnections()
# print(candidatebits)
# print(connections)

# print(graph)


# print(commonbits)
# print('0b'+bin(commonbits)[2:].zfill(46))
masterlist=[]
for cand in candidatebits:
    visited=list()
    dfs(visited,graph,cand)
    # print(cand,visited)
    masterlist.append(set(visited))
    print()

# print(masterlist)

masterset=set()
for row in masterlist:
    # print(row)
    for a in row:
        if a[0]!='x' and a[0]!='y':
            masterset.add(a)
        
print()
# print(masterset)
a=list(masterset)
a.sort()
print(a)

print(len(masterset))

toswap=[]
xorcount=0
andcount=0
orcount=0
for output in a:
# for output in graph.keys():
    if output[0]=='z':
        if graph[output][2]!='XOR': toswap.append(output)
    
    d=''.join(graph[output])
    if ('x' in d and 'y' in d) and graph[output][2]=='XOR':
        print(output,graph[output])
        xorcount+=1
        
    elif ('x' in d and 'y' in d) and graph[output][2]=='OR':
        print(output,graph[output])
        orcount+=1
    elif ('x' in d and 'y' in d) and graph[output][2]=='AND':
        print(output,graph[output])
        andcount+=1
        # toswap.append(output)
    elif ('x' in d or 'y' in d):
        print(output,graph[output])
    

print(toswap)
print(andcount,orcount,xorcount)

print(7*45)
print(len(graph.keys()))



# This is definitely a ripple carry adder. Why are there only 38 andcount and xorcount for the inputs? Because I'm only looking at nodes that 
# result in bad bits. So the inputs count up to 45 and each have an AND and an XOR.

# Let's try to track each through
# Each input should got to and AND and an XOR
# Internal to each block are 4 signals, call them ina, inb, inc, and ind.
# Then there are two outputs, the z bit zn and the carry bit cn:

# ina is xn XOR yn
# inb is xn AND yn
# inc is cn-1 AND ina
# zn is ina XOR cn-1
# cn is inc or inb

# The very last bit becomes just the carry of the previous, or xn-1 OR yn-1

# part 2
# make part 1 into a function that takes 2 numbers, sends them through the machine, and outputs z
# bitwise compare z to x+y using several different x and y's. Keep track of the z bits that are wrong
# DFS for the wrong z bits and then start swapping those in the tree until all x and y come out correctly.

# So, for the bits I've already identified, if I work backwards maybe I can find the ones to swap in addition
# to the z's already identified

# z0 is also a special case since there's not a carry from previous.

# So in this case z0 is just x0 XOR y0, and I think the cn is just x0 AND y0, so there are no internal variables for x0, y0, z0
# which also accounts for my 315-312 discrepancy when counting total variables above

def checkzero():
    print(graph['z00'])
    c0=[]
    if graph['z00']==['x00','y00','XOR']: print('z00 ok')
    for key in graph.keys():
        # print(key,graph[key])
        if graph[key]==['x00','y00','AND'] or graph[key]==['y00','x00','AND'] :
            print('c00 is',key)
            print()
            c0=key
    return c0

def checkn(n,previouscarry):
    print(previouscarry)
    x='x'+str(n).zfill(2)
    y='y'+str(n).zfill(2)
    z='z'+str(n).zfill(2)
    ia=[]
    ib=[]
    ic=[]
    cout=[]
    zout=[]
    # print(x,y,z)
    for key in graph.keys():
        if graph[key]==[x,y,'AND'] or graph[key]==[y,x,'AND']:
            ib=key
        elif graph[key]==[x,y,'XOR'] or graph[key]==[y,x,'XOR']:
            ia=key
    for key in graph.keys():
        if (graph[key]==[previouscarry,ia,'AND'] or graph[key]==[ia,previouscarry,'AND']) and key[0]!='z':
            ic=key
    for key in graph.keys():
        if graph[key]==[ic,ib,'OR'] or graph[key]==[ib,ic,'OR']:
            cout=key
    print(ia,ib,ic)
    print('z is',graph[z],'z should be',[ia,previouscarry,'XOR'])
    print('cout is', ib,'OR',ic)
    print('c'+str(n).zfill(2),'is',cout)
    return(cout)

print()
print()
print()
cprevious=checkzero()
for n in range(1,45):
    print(cprevious)
    cnext=checkn(n,cprevious)
    print(cnext)
    cprevious=cnext
    print()

# working throught the above it will report empty values where there's errors, using the full adder network diagram at https://www.circuitstoday.com/ripple-carry-adder
# and the information given by the checkn function I figured that I needed to swap:

# bit 11: z11 and wpd
# bit 15: skh and jqf
# bit 19: z19 and mdd
# bit 37: z37 and wts
a=['z11','wpd','skh','jqf','z19','mdd','z37','wts']
a.sort()
print('Part 2',end=' ')
for s in a:
    print(s,end=',')
print()
