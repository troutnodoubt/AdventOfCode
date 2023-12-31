import re
from itertools import permutations, product

fname='input_day12.txt'
# fname='example_day12.txt'
with open(fname) as fp: data = fp.read().splitlines()

def seedRecord(rec1,rec2):
    nhashneeded=sum(rec2)
    nhashhas=rec1.count('#')
    rec1list=[c for c in rec1]
    added=0
    for i in range(len(rec1list)): #range(nhashneeded - nhashhas):
#        print(i,len(rec1list))
        if rec1list[i]=='?':
            rec1list[i]='#'
            added+=1
        if added==nhashneeded-nhashhas: break
    rec1=''
    for c in rec1list:
        rec1=rec1+c
#    print(rec1)
    return rec1.replace('?','.')
    
def checkHashNumber(rec1,rec2):
    #rec1split=re.split('\.+',rec1)
    rec1cts=[a.count('#') for a in re.split('\.+',rec1) if a.count('#')>0]
    # if rec1cts==rec2: print('they match')
    # print(rec1cts)
    return rec1cts==rec2

def checkPositions(rec1,pattern):
    match=[]
    if len(rec1)!=len(pattern): return False
    for i,c in enumerate(pattern):
        if pattern[i]=='?' or pattern[i]==rec1[i]: match.append(True)
        else: match.append(False)
    return all(match)

def findCandidates(rec1, rec2): # make the bars be any known string. will have bars, hash, and dots to permutate
    nhashneeded=sum(rec2)
    nhashhas=rec1.count('#')
    nhashtoadd=nhashneeded-nhashhas
    openspots=rec1.count('?')
    ndots=openspots-nhashtoadd
    bars=re.split('\?+',rec1)
    bins=re.findall('\?+',rec1)
    balls=ndots*'.' + nhashtoadd*'#'
    for bar in bars:
        if bar=='': bars.remove('')
    # print(bars)
   # base=ndots*'.' + nhashtoadd*'#' + len(bars)*'|'
    # print(bins)
    # print(balls)
    cand={}
    for b in bins:
        perms=permutations(balls,len(b))
        cand[b]=set([''.join(p) for p in perms])
    
    return cand
    
    # print(rec1)
    # for key in cand.keys():
    #     print('*** ', key, ' ***' )
    #     for s in cand[key]: print(s)
    # print()
    
    
        
    # perms = permutations(base)
    # permlist=[]
    # for perm in perms:
    #     pstring=[''.join(p) for p in perm][0]
    #     if '||' not in pstring: permlist.append(pstring)
    # permutation = [''.join(p) for p in permutations(base)]
    #print(permutation)

# def buildStringList(fixed,cands):
#     keys=list(cands.keys())
#     keyidx=0
#     stringList=[]
#     for sub in fixed:
#         if len(sub)!=0:
#             stringList.append([sub])
#             if keyidx<len(keys):
#                 stringList.append(list(cands[keys[keyidx]]))
#                 keyidx+=1
#         else:
#             if keyidx<len(keys):
#                 stringList.append(list(cands[keys[keyidx]]))
#                 keyidx+=1
#     # temp=''.join('stringList['+str(i)+'],' for i in range(len(stringList)))
#     # print(temp[:-1])
#     # b=product(eval(temp[:-1]))
#     b=product(*stringList)
#     return stringList,b

def buildStringList(pattern,cands):
    indices=[]
    stringList=[]
    iterator=re.finditer('\?+',pattern)
    for match in iterator: 
        indices.append(match.span()[0])
        indices.append(match.span()[1])
    # print(indices)
    for i in range(len(indices)-1):
        stringList.append(pattern[indices[i]:indices[i+1]])
    if indices[0]!=0:
        stringList.insert(0,pattern[0:indices[0]])
    if indices[-1]!=len(pattern):
        stringList.append(pattern[indices[-1]:])
    
    print(stringList)
    
    buildList=[]
    for sub in stringList:
        if sub in cands.keys():
            buildList.append(list(cands[sub]))
        else:
            buildList.append([sub])
    print(buildList)
    return buildList,product(*buildList)
   
        
    
           
        
            
            

bigcount=0
for line in data:
    #r1=re.split('\.+',line.split(' ')[0])
    r1=line.split(' ')[0]
    r2=eval('[' + line.split(' ')[1] + ']')
    # r3=re.split('\?+',line.split(' ')[0])
    # r4=re.finditer('\?+',line.split(' ')[0])
    for s in r1:
        if s=='': r1.remove(s)
    print(r1)
    print(r2)
    # print(r3)
    # for match in r4: print(match.span())
    # print()
    c=findCandidates(r1, r2)
    # buildStringList(r1,c)
    # sl,b=buildStringList(r3,c)
    sl,b=buildStringList(r1,c)
    # print(sl)
    for a in b:
        temp=''.join(c for c in a)
        print(temp, checkHashNumber(temp,r2), checkPositions(temp,r1))
        if checkHashNumber(temp,r2) and checkPositions(temp,r1): bigcount+=1
    print()

print('Part 1 is', bigcount)    
    # make lists of equal length for the bins and the the bars, adding padding on the beginning or the end depending on who goes first
    # padding can be empty strings or a nonsense character that is stripped out later
    # then should be able to use a common index to build the test string
    
    
    
    
    # r1test = seedRecord(r1, r2)
    # # print(r1test)
    # # #doCountsMatch=checkHashNumber(r1test,r2)
    # # print(doCountsMatch)
    # # #doPatternsMatch=checkPositions(r1test,r1)
    # # print(doPatternsMatch)
    # # print()
    # permutation = [''.join(p) for p in permutations(r1test)]
    # count=0
    # for cand in permutation:
    #     if checkPositions(cand,r1) and checkHashNumber(cand, r2): count+=1
    # bigcount+=count
    
#make bigger string chunks, equal to the size of the arrays. Permute on the chunks rather than the individual characters
 

 

    