import re
from itertools import permutations, product

fname='input_day12.txt'
fname='example_day12.txt'
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
    

bigcount=0
for line in data:
    #r1=re.split('\.+',line.split(' ')[0])
    r1=line.split(' ')[0]
    r2=eval('[' + line.split(' ')[1] + ']')
    for s in r1:
        if s=='': r1.remove(s)
    print(r1)
    print(r2)
    c=findCandidates(r1, r2)
    
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
 

 

    