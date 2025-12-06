import numpy as np

fname='/home/mark/Documents/git/AdventOfCode/2025/input_day6.txt'
# fname='/home/mark/Documents/git/AdventOfCode/2025/example_day6.txt'

with open(fname) as fp: data = fp.read().splitlines()

def hasNumbers(s):
    return any(c.isdigit() for c in s)

operators=data.pop(-1).split()
operators2=[a for a in operators]
values = [row.split() for row in data]
values = np.array(values,dtype=int)

tmprow=[]
total2=0
for colnum in range(len(data[0])):
    tmp=[]
    
    for row in data:
        tmp.append(row[colnum])
    tmpstr=''.join(a for a in tmp)
    if hasNumbers(tmpstr): 
        tmprow.append(int(tmpstr))
    else: 
        tmparray=np.array(tmprow)
        print(tmparray,operators[0])
        if operators2[0]=='+': 
            print(sum(tmparray))
            total2+=sum(tmparray)
            operators2.pop(0)
        elif operators2[0]=='*': 
            print(np.prod(tmparray))
            total2+=np.prod(tmparray) 
            operators2.pop(0)
        tmprow=[]

tmparray=np.array(tmprow)
print(tmparray,operators[0])
if operators2[0]=='+': 
    print(sum(tmparray))
    total2+=sum(tmparray)
    operators2.pop(0)
elif operators2[0]=='*': 
    print(np.prod(tmparray))
    total2+=np.prod(tmparray) 
    operators2.pop(0)  

total=0
for col in range(len(operators)):
    if operators[col]=='+': 
        total+=sum(values[:,col])
    elif operators[col]=='*': 
        total+=np.prod(values[:,col])

print('Part 1 solution', total)
print('Part 2 solution', total2)

