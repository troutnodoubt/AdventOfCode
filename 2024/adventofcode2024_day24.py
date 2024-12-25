
fname='input_day24.txt'
# fname='example_day24a.txt'
# fname='example_day24b.txt'
with open(fname) as fp: data = fp.read().splitlines()

toCompute=[]
knownGates={}
zlist=[]
ylist=[]
xlist=[]
hierarhcy={}

for row in data:
    if ':' in row:
        knownGates[row.split(' ')[0][:-1]]=int(row.split(' ')[1])
    elif '->' in row: 
        toCompute.append([a for a in row.split(' ') if a!='->'])
    if row!='':
        if 'z' in row: zlist.append(row.split()[-1])
        if 'y' in row.split()[-1]: ylist.append(row.split()[-1])
        if 'x' in row.split()[-1]: xlist.append(row.split()[-1])

xlist.sort(reverse=True)
ylist.sort(reverse=True)
zlist.sort(reverse=True)


level0=[a for a in zlist]
level1=[]
for a in level0:
    for op in toCompute:
        if op[-1]==a: 
            level1.append([op[0],op[2]])
            hierarhcy[a]=[op[0],op[2]]

level2a=[]
for a in level1:
    for op in toCompute:
        if op[-1]==a[0]: 
            level2a.append([op[0],op[2]])
            hierarhcy[a[0]]=[op[0],op[2]]


level2b=[]
for a in level1:
    for op in toCompute:
        if op[-1]==a[1]: 
            level2b.append([op[0],op[2]])
            hierarhcy[a[1]]=[op[0],op[2]]

level2a1=[]
for a in level2a:
    for op in toCompute:
        if op[-1]==a[0]: 
            level2a1.append([op[0],op[2]])
            hierarhcy[a[0]]=[op[0],op[2]]

level2a2=[]
for a in level2a:
    for op in toCompute:
        if op[-1]==a[0]: 
            level2a1.append([op[0],op[2]])
            hierarhcy[a[1]]=[op[0],op[2]]

level2b1=[]
for a in level2b:
    for op in toCompute:
        if op[-1]==a[0]: 
            level2b1.append([op[0],op[2]])
            hierarhcy[a[0]]=[op[0],op[2]]

level2b2=[]
for a in level2a:
    for op in toCompute:
        if op[-1]==a[0]: 
            level2b1.append([op[0],op[2]])
            hierarhcy[a[1]]=[op[0],op[2]]

print(len(hierarhcy))
print(hierarhcy)

                                       
# print(toCompute)
# print(knownGates)
# print(zlist)
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

print()
print(knownGates)
print(len(knownGates))

inx='0b'
for gate in xlist: final=final+str(knownGates[gate])
iny='0b'
for gate in xlist: final=final+str(knownGates[gate])

final='0b'
for gate in zlist: final=final+str(knownGates[gate])
print(len(final))
print('Part 1',final,eval(final))


# part 2
# make part 1 into a function that takes 2 numbers, sends them through the machine, and outputs z
# bitwise compare z to x+y using several different x and y's. Keep track of the z bits that are wrong
# DFS for the wrong z bits and then start swapping those in the tree until all x and y come out correctly.