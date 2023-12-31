fname='input_day11.txt'
# fname='example_day11.txt'
with open(fname) as fp: data = fp.read().splitlines()
       
galaxies={}
ngalaxy=0
for i,row in enumerate(data):
    for j,c in enumerate(row):
        if c=='#':
            galaxies[ngalaxy]=(i,j)
            ngalaxy+=1

rows=set([i[0] for i in galaxies.values()])
cols=set([i[1] for i in galaxies.values()])

emptyrows=[i for i in range(len(data)) if i not in rows]
emptycols=[i for i in range(len(data[0])) if i not in cols]

def findDistance(expand,g0,g1):
    row0=galaxies[g0][0]
    row1=galaxies[g1][0]
    col0=galaxies[g0][1]
    col1=galaxies[g1][1]
    
    expandcount=0
    for emptyrow in emptyrows:
        if emptyrow in range(row0,row1) or emptyrow in range(row1,row0): expandcount+=1
    rowdist=abs(row1-row0)+expandcount*(expand-1)
    
    expandcount=0
    for emptycol in emptycols:
        if emptycol in range(col0,col1) or emptycol in range(col1,col0): expandcount+=1
    coldist=abs(col1-col0)+expandcount*(expand-1)
    
    return rowdist+coldist

def findTotal(exp):
    total=0
    for i in range(len(galaxies.keys())-1):
        for j in range(i+1,len(galaxies.keys())):
            total+=findDistance(exp,i,j)
    return total
        
print('Part 1 is', findTotal(2))
print('Part 2 is', findTotal(1000000))    
    