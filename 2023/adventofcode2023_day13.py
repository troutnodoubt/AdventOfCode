fname='input_day13.txt'
#fname='example_day13.txt'
with open(fname) as fp: data = fp.read().splitlines()
data.append('')

def findreflection(mirror):
    for idx in range(1,len(mirror)):
        if mirror[idx]==mirror[idx-1]:
            half1=mirror[:idx]
            half2=mirror[-1:idx-1:-1]
            matchsize=min(len(half1),len(half2))
            if half1[-matchsize:]==half2[-matchsize:]: return idx
    return 0
            
def transpose(mirror):
    tmirror=[['' for _ in range(len(mirror))] for _ in range(len(mirror[0]))]
    for i in range(len(mirror)):
        for j in range(len(mirror[0])):
            tmirror[j][i]=mirror[i][j]
    return tmirror

def findpossiblereflections(mirror):
    idxlist=[]
    for idx in range(1,len(mirror)):
        nmatch=0
        for i in range(len(mirror[0])):
            c1=mirror[idx][i]
            c2=mirror[idx-1][i]
            if c1==c2: nmatch+=1
        if len(mirror[0])-nmatch<=1:
            half1=mirror[:idx]
            half2=mirror[-1:idx-1:-1]
            matchsize=min(len(half1),len(half2))
            nmatchrow=0
            nonmatchlist=[]
            for i in range(matchsize):
                nmatchchar=0
                nnonmatchchar=0
                for j in range(len(mirror[0])):
                    c1=half1[-matchsize:][i][j]
                    c2=half2[-matchsize:][i][j]
                    if c1==c2: 
                        nmatchchar+=1
                    else:
                        nnonmatchchar+=1
                nonmatchlist.append(nnonmatchchar)
                if len(mirror[0])-nmatchchar<=1: nmatchrow+=1
            if matchsize-nmatchrow<=1 and max(nonmatchlist)<=1: idxlist.append(idx)
    return(idxlist)
    

mirrors={}
idx=0

temp=[]
for line in data:
    if len(line)>0: 
        temp.append(line)
    else: 
        mirrors[idx] = temp
        idx+=1
        temp=[]
    
aboves=[]
lefts=[]
abovesfixed=[]
leftsfixed=[]     
for mirror in mirrors.keys():
    aboveindices=findpossiblereflections(mirrors[mirror])
    smudgedabove=findreflection(mirrors[mirror])
    aboves.append(smudgedabove)
    tmirror=transpose(mirrors[mirror])
    smudgedleft=findreflection(tmirror)
    lefts.append(smudgedleft)
    leftindices=findpossiblereflections(tmirror)
    if smudgedabove in aboveindices: aboveindices.remove(smudgedabove)
    if smudgedleft in leftindices: leftindices.remove(smudgedleft)
    if len(aboveindices)>1 or len(leftindices)>1: 
        print('too many reflections after fixing', aboveindices, leftindices, mirror)
    if len(aboveindices)>0: abovesfixed.append(aboveindices[0])
    if len(leftindices)>0: leftsfixed.append(leftindices[0])

print('Part 1 is', 100*sum(aboves)+sum(lefts)) 
print('Part 2 is', 100*sum(abovesfixed)+sum(leftsfixed)) 
