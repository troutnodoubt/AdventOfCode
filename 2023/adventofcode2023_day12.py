import re
from more_itertools import distinct_permutations as idp
# import multiprocessing
# import time

fname='input_day12.txt'
# fname='example_day12.txt'
with open(fname) as fp: data = fp.read().splitlines()
   
def checkHashNumber(rec1,rec2):
    rec1cts=[a.count('#') for a in re.split('\.+',rec1) if a.count('#')>0]
    return rec1cts==rec2

def checkPositions(rec1,pattern):
    match=[]
    if len(rec1)!=len(pattern): return False
    for i,c in enumerate(pattern):
        if pattern[i]=='?' or pattern[i]==rec1[i]: match.append(True)
        else: match.append(False)
    return all(match)

def findM(m,springs):
    p=re.compile('[.?][#?]{'+str(m)+',}[.?]')
    return p.match(springs)
    

bigcount=0
springlist=[]
for line in data:
    r1=line.split(' ')[0]
    r2=eval('[' + line.split(' ')[1] + ']')
    for s in r1:
        if s=='': r1.remove(s)
    base='.'*(len(r1)-sum(r2))+'|'*len(r2)
    perms=idp(base)
    candidates=[]
    for perm in perms:
        pstring=[''.join(p for p in perm)][0]
        if '||' not in pstring and pstring not in candidates: 
            candidates.append(pstring)
    springcount=0
    for cand in candidates:
        builtstring=''
        nhash=[a*'#' for a in r2]

        for c in cand:
            if c=='.':
                builtstring=builtstring+c
            else:
                builtstring=builtstring+nhash.pop(0)
        if checkHashNumber(builtstring,r2) and checkPositions(builtstring,r1): 
            bigcount+=1
            springcount+=1
    springlist.append(springcount)

print('Part 1 is', bigcount)  

subspring=line  

b=findM(4,subspring)
print(b)
subspring=subspring[b.span()[1]-1:]
print(subspring)
b=findM(4,subspring)
print(b)
subspring=subspring[b.span()[1]-1:]
print(subspring)
b=findM(4,subspring)
print(b)
subspring=subspring[b.span()[1]-1:]
print(subspring)
b=findM(4,subspring)
print(b)

# # bigcount=0
# foldspringlist=[]
# # for line in data:
# def foldedOnce(line):
#     pattern=line.split(' ')[0]
#     count=eval('[' + line.split(' ')[1] + ']')
#     r1=pattern+'?'+pattern
#     r2=[]
#     for i in range(2):
#         for n in count:
#             r2.append(n)
#     for s in r1:
#         if s=='': r1.remove(s)
#     print(r1)
#     print(r2)
#     base='.'*(len(r1)-sum(r2))+'|'*len(r2)
#     print('Generating permutations')
#     perms=idp(base)
#     candidates=[]
#     print('Generating candidates from permutations')
#     candidates = set([''.join(str(b) for b in a) for i, a in enumerate(perms)])
#     foldspringcount=0
#     print('Evaluating candidates')
#     for cand in candidates:
#         if '||' not in cand:
#             builtstring=''
#             nhash=[a*'#' for a in r2]
#             for c in cand:
#                 if c=='.':
#                     builtstring=builtstring+c
#                 else:
#                     builtstring=builtstring+nhash.pop(0)
#             if checkHashNumber(builtstring,r2) and checkPositions(builtstring,r1): 
#                 # bigcount+=1
#                 foldspringcount+=1
#     # foldspringlist.append(foldspringcount)
#     print()
#     return foldspringcount

# # pool = multiprocessing.Pool()
# # print('made a pool')
# # foldspringlist_async=pool.map_async(foldedOnce, data)
# # print('did the thing')
# # foldspringlist = foldspringlist_async.get()
# # print('got the deets')

# for line in data:
#     foldspringlist.append(foldedOnce(line))

# bigcount=0
# for i in range(len(springlist)):
#     temp=springlist[i]*(foldspringlist[i]//springlist[i])**4
#     print(temp)
#     bigcount+=temp

# print('Part 2 is', bigcount)      
