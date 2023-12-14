fname='input_day14.txt'
#fname='example_day14.txt'

with open(fname) as fp: data = fp.read().splitlines()

def rotatecw(l):
    rl = [''.join(p for p in line) for line in [list(row) for row in zip(*reversed(l))]]
    return rl

def findFixedRocks(line):
    locs=[]
    for i,loc in enumerate(line):
        if loc=='#': locs.append(i+1)
    return locs

def tilt(line):
    nlines=len(line)
    a=[s.count('O') for s in line.split('#')]
    fixedlocs=findFixedRocks(line)
    fixedlocs.insert(0,0)
    newlocs={}
    for i,_ in enumerate(fixedlocs):
        newlocs[1+nlines-fixedlocs[i]]=a[i]
    return newlocs


def scoreDict(d):
    linescore=0
    for s in d.keys():
        for i in range(d[s]):
            linescore+=s-(i+1)
    return linescore

def scoreE(tilt):
    score=0
    for i,line in enumerate(tilt):
        score+=(i+1)*line.count('O')
    return score

def parseDict(d):
    line=['.' for i in range(max(d.keys())-1)]
    for key in d.keys():
        pos=max(d.keys()) - (key+1)
        if pos>=0: line[pos]='#'
    for key in d.keys():
        startpos=max(d.keys())-key
        for pos in range(startpos,startpos+d[key]):
            line[pos]='O'
    sline=''.join(p for p in line)
    return sline

def solve(rotspercycle,cycles):
    tdata=rotatecw(rotatecw(rotatecw(data)))
    rockpatterns={}
    foundpattern=False
    for i in range(1,cycles+1):
        if foundpattern: break
        for j in range(rotspercycle):
            newdata=[]
            for line in tdata:
                newdata.append(parseDict(tilt(line)))
            tdata=[]
            for line in newdata: tdata.append(line)
            tdata=rotatecw(tdata)
        if newdata in rockpatterns.values():
            foundpattern=True
        rockpatterns[i]=newdata
    return rockpatterns

testdata=rotatecw(rotatecw(rotatecw(data)))
testscore=0
testnewdata=[]
for line in testdata:
    testnewdata.append(parseDict(tilt(line)))
    testscore+=scoreDict(tilt(line))

nruns=1000000000

patterntest=solve(4,nruns)
keymatch=[]
for key in patterntest.keys():
    for key1 in patterntest.keys():
        if patterntest[key]==patterntest[key1] and key!=key1: keymatch.append(key1)
    
startpattern=min(keymatch)
patternlen=max(keymatch)-min(keymatch)

solidx=(nruns-startpattern)%patternlen + startpattern

print('Part 1 is', testscore)
print('Part 2 is', scoreE(patterntest[solidx]))
