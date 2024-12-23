
fname='input_day23.txt'
# fname='example_day23.txt'
with open(fname) as fp: data = fp.read().splitlines()

graph={}
for row in data:
    computers=row.split('-')
    
    # print(computers)
    if computers[0] not in graph.keys():
        graph[computers[0]]=[computers[1]]
    else: graph[computers[0]].append(computers[1])
    if computers[1] not in graph.keys():
        graph[computers[1]]=[computers[0]]
    else: graph[computers[1]].append(computers[0])

# super inefficient way to do part 1 
cluster3=set()
for c1 in graph.keys():
    for c2 in graph.keys():
        for c3 in graph.keys():
            if c1!=c2 and c2!=c3 and c1!=c3:
                if c1 in graph[c2] and c1 in graph[c3] and c2 in graph[c1] and c2 in graph[c3] and c3 in graph[c1] and c3 in graph[c2]:
                    a=[c1,c2,c3]
                    a.sort()
                    cluster3.add(tuple(a))

tcount=0
for row in cluster3: 
    # print(row)
    for comp in row:
        if comp[0]=='t':
            tcount+=1
            break
print('Part 1',tcount)

candidatecycles=set()
for comp in graph.keys():
    cands=graph[comp]
    possible=len(cands)+1
    # print(comp,'connected to',cands)
    cyclelist={comp}
    test=[]
    for n,cand in enumerate(cands):
        
        if cands[n+1:]:
            # print('check if',cand,'connected to',cands[n+1:])
            truecount=0
            for sub in cands[n+1:]:
                # print('   ',cand,'in',sub,'?',cand in graph[sub])
                if cand in graph[sub]: 
                    truecount+=1
                    cyclelist.add(cand)
                    cyclelist.add(sub)
            if truecount>=len(cands[n+1:])-1:
                # print(truecount,len(cands[n+1:]-1))
                test.append(True)
            else: test.append(False)
    # print(len(cyclelist),cyclelist) 
    cyclelist=list(cyclelist)
    cyclelist.sort()
    
    if all(test): candidatecycles.add(tuple(cyclelist))
    
print('Part 2',end=' ')
for cand in candidatecycles:
    for node in cand[:-1]:
        print(node,end=',')
    print(cand[-1])
