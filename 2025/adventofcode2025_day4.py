fname='input_day4.txt'
# fname='example_day4.txt'

with open(fname) as fp: data = fp.read().splitlines()

# pad the area with dots
data.insert(0,'.'*len(data[0]))
data.append('.'*len(data[0]))
for i,row in enumerate(data):
    row='.'+row+'.'
    data[i]=list(row)

forkliftcount=0
for i in range(1,len(data)-1):
    for j in range(1,len(data[0])-1):
        neighborcount=0
        isSelfRoll=False
        if data[i-1][j-1]=='@': neighborcount+=1
        if data[i-1][j-0]=='@': neighborcount+=1
        if data[i-1][j+1]=='@': neighborcount+=1
        if data[i-0][j-1]=='@': neighborcount+=1
        if data[i-0][j-0]=='@': isSelfRoll=True
        if data[i-0][j+1]=='@': neighborcount+=1
        if data[i+1][j-1]=='@': neighborcount+=1
        if data[i+1][j-0]=='@': neighborcount+=1
        if data[i+1][j+1]=='@': neighborcount+=1
        if neighborcount<4 and isSelfRoll: forkliftcount+=1

print('Part 1 solution',forkliftcount)

totalRemoved=0
prevTotalRemoved=0
while True:
    forkliftcount=0
    for i in range(1,len(data)-1):
        for j in range(1,len(data[0])-1):
            neighborcount=0
            isSelfRoll=False
            if data[i-1][j-1]=='@': neighborcount+=1
            if data[i-1][j-0]=='@': neighborcount+=1
            if data[i-1][j+1]=='@': neighborcount+=1
            if data[i-0][j-1]=='@': neighborcount+=1
            if data[i-0][j-0]=='@': isSelfRoll=True
            if data[i-0][j+1]=='@': neighborcount+=1
            if data[i+1][j-1]=='@': neighborcount+=1
            if data[i+1][j-0]=='@': neighborcount+=1
            if data[i+1][j+1]=='@': neighborcount+=1
            if neighborcount<4 and isSelfRoll:
                data[i][j]='.'
                totalRemoved+=1
    if totalRemoved==prevTotalRemoved: break
    prevTotalRemoved=totalRemoved

print('Part 2 solution is', totalRemoved)
