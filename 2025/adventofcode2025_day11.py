fname='2025\\input_day11.txt'
# fname='2025\\example_day11.txt'
# fname='2025\\example_day11pt2.txt'

with open(fname) as fp: data = fp.read().splitlines()

visited=set() 

def DFS(connections,node,allpaths,path,dest):
    if node in path: print("going in circles")
    path.append(node)
    # print(node)
    if node==dest:
        allpaths.append(path.copy())
    else:
        for neighbor in connections[node]:
            DFS(connections,neighbor,allpaths,path,dest)
    path.pop()

connections=dict()
for row in data:
    connections[row.split()[0][0:-1]]=row.split()[1:]

allpaths=[]
path=[]
connections['out']=[]        
# DFS(connections,'you',allpaths,path,'out')

# # print(allpaths)
# print('Part 1',len(allpaths))

allpaths=[]
path=[]
DFS(connections,'svr',allpaths,path,'out')

count=0

for path in allpaths:
    print(path)
    if 'fft' in path and 'dac' in path: count+=1

print('Part 2', count)