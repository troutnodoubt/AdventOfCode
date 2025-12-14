
fname='/home/mark/Documents/git/AdventOfCode/2025/input_day7.txt'
# fname='/home/mark/Documents/git/AdventOfCode/2025/example_day7.txt'

with open(fname) as fp: data1 = fp.read().splitlines()

splitcnt=0
data=[]
for row in data1:
    data.append(list(row))


splits=dict()
start=0
rowlength=len(data[0])
for row in range(len(data)-1):
    for col in range(0,len(data[0])):
        if data[row][col]=='S':
            data[row+1][col]='|'
            start=(row+1)*rowlength+col
        elif data[row][col]=='|':
            if data[row+1][col]=='.':
                data[row+1][col]='|'
            elif data[row+1][col]=='^':
                data[row+1][col-1]='|'
                data[row+1][col+1]='|'
                splitcnt+=1

nworlds=[]
nrow=0
sol=0
for row in range(len(data)-1,0,-1):
    temp=[]
    for col in range(len(data[0])):
        if row==len(data)-1:
            if data[row][col]=='|':
                temp.append(1)
            else:
                temp.append(0)
        else:
            if data[row][col]=='|':
                temp.append(nworlds[nrow-1][col])
            else:
                temp.append(0)
               
    nworlds.append(temp)
    for col in range(len(data[0])):
        if data[row][col]=='^':
            temp[col]=temp[col-1]+temp[col+1]
            if temp[col]>sol: sol=temp[col]
    nrow+=1

print('Part 1 is',splitcnt)
print('Part 2 is',sol)
