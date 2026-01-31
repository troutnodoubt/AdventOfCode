fname='2025/input_day11.txt'
# fname='2025/example_day11.txt'
# fname='2025/example_day11pt2.txt'

with open(fname) as fp: data = fp.read().splitlines()

def DFS(connections,node,dest,memo):
    if node==dest:
        return 1
    if memo[node]!=-1:
        return memo[node]
    count=0
    for neighbor in connections[node]:
        count+=DFS(connections,neighbor,dest,memo)
    memo[node]=count
    return count

connections={}
memo={}
for row in data:
    connections[row.split()[0][0:-1]]=set(row.split()[1:])

for key in connections.keys():
    memo[key]=-1

connections['out']=()
for key in connections.keys():
    memo[key]=-1
count=DFS(connections,'you','out',memo)

print('Part 1',count)

for key in connections.keys():
    memo[key]=-1
counta1=DFS(connections,'svr','fft',memo)
for key in connections.keys():
    memo[key]=-1
counta2=DFS(connections,'fft','dac',memo)
for key in connections.keys():
    memo[key]=-1
counta3=DFS(connections,'dac','out',memo)

for key in connections.keys():
    memo[key]=-1
countb1=DFS(connections,'svr','dac',memo)
for key in connections.keys():
    memo[key]=-1
countb2=DFS(connections,'dac','fft',memo)
for key in connections.keys():
    memo[key]=-1
countb3=DFS(connections,'fft','out',memo)

count=counta1*counta2*counta3+countb1*countb2*countb3

print('Part 2', count)
