from functools import lru_cache

fname='input_day19.txt'

with open(fname) as fp: data = fp.read().splitlines()

towels=data[0].split(', ')
data.pop(0)
data.pop(0)
maxsizetocheck=0
for towel in towels:
    if len(towel)>maxsizetocheck: maxsizetocheck=len(towel)

@lru_cache(maxsize=None)
def isValidPattern2(patterntomatch,towels,maxsize,target,builtpattern='',debug=False):
    size=min(maxsize,len(patterntomatch))
    patterns=[patterntomatch[:size-reduction] for reduction in range(size) if patterntomatch[:size-reduction] in towels]
    nmatch=0
    for i,pattern in enumerate(patterns):
        if i>0: builtpattern=builtpattern[:-len(patterns[i-1])]
        builtpattern+=pattern
        newpatterntomatch=patterntomatch[len(pattern):]
        if debug:
            print('Patterns this step   ',patterns)
            print('Pattern being checked',pattern)
            print('Remaining to check   ',newpatterntomatch)
            print('Prior step remaining ',patterntomatch)
            
            # print(visited)
            print('Built so far         ',builtpattern)
            print('Target pattern       ',target)
            print()
        nmatch+=isValidPattern2(newpatterntomatch,towels,maxsize,target,builtpattern,debug)
        if builtpattern==target: 
            nmatch=1
            
    return nmatch
    
validpatterns=set()
invalidpatterns=set()
total1=0
total2=0
for i,pattern in enumerate(data):
    nmatch=isValidPattern2(str(pattern),tuple(towels),maxsizetocheck,str(pattern))
    total1+=nmatch>0
    total2+=nmatch

print('Part 1',total1)
print('Part 2',total2)
