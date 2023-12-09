fname='input_day9.txt'
# fname='example_day9.txt'

with open(fname) as fp: data = fp.read().splitlines()

def getNextList(l):
    nxt=[]
    for i in range(len(l)-1): nxt.append(l[i+1]-l[i])
    return nxt

def extrapolate(l):
    for i in range(len(l)-1,0,-1):
        extrap=l[i-1][-1]+l[i][-1]
        l[i-1].append(extrap)
    return l

def extrapolateleft(l):
    for i in range(len(l)-1,0,-1):
        extrap=l[i-1][0]-l[i][0]
        l[i-1].insert(0,extrap)
    return l

def getScore(idx, callback):
    score=0
    for line in data:
        foundzeros=False
        pyramid=[]
        nxtline=[int(a) for a in line.split(' ')]
        pyramid.append(nxtline)
        while not foundzeros:
            nxtline=getNextList(nxtline)
            pyramid.append(nxtline)
            if all([x==0 for x in nxtline]): foundzeros=True
        newpyramid=callback(pyramid)
        score+=newpyramid[0][idx]
    return score
    
print('Part 1 is', getScore(-1,extrapolate))
print('Part 2 is', getScore(0,extrapolateleft))    