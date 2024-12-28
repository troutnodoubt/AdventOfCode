from functools import lru_cache

fname='input_day19.txt'

with open(fname) as fp: data = fp.read().splitlines()

data=['r, wr, b, g, bwu, rb, gb, br',
       '',
       'brwrr',
       'bggr',
       'gbbr',
       'rrbgbr',
       'ubwu',
       'bwurrg',
       'brgr',
       'bbrgwb']

# data=['r, wr, b, g, bwu, rb, gb, br',
#        '',
#        'rrbgbr']

# data=['abcd, abc, def, ef',
#       '',
#       'abcdef']

towels=data[0].split(', ')
data.pop(0)
data.pop(0)
maxsizetocheck=0
for towel in towels:
    if len(towel)>maxsizetocheck: maxsizetocheck=len(towel)

# print(towels)
print(maxsizetocheck)

@lru_cache(maxsize=None)
def isValidPattern(patterntomatch,towels,maxsize,debug=False):
    size=min(maxsize,len(patterntomatch))
    patterns=[patterntomatch[:size-reduction] for reduction in range(size)]
    if debug:
        print()
        print('patterns',patterns)
    builtpattern=''
    for pattern in patterns:

        if pattern in towels:
            newpatterntomatch=patterntomatch[len(pattern):]
            if debug: 
                print('before recursive call', pattern)
                print('to match',newpatterntomatch)
                print('built   ',builtpattern)
                    
            builtpattern=pattern+isValidPattern(newpatterntomatch,towels,maxsize,debug)
            if debug:
                print('after recursive call', pattern)
                print('to match',newpatterntomatch)
                print('built   ',builtpattern)
            if builtpattern==pattern+newpatterntomatch: 
                if debug: print('early return',builtpattern)
                return builtpattern
    if debug: print('return  ',builtpattern) 
    return builtpattern


possibilities={}
# @lru_cache(maxsize=None)
def isValidPattern2(patterntomatch,towels,maxsize,target,builtpattern='',debug=False):
    size=min(maxsize,len(patterntomatch))
    patterns=[patterntomatch[:size-reduction] for reduction in range(size) if patterntomatch[:size-reduction] in towels]
    visited=[]
    matched=False
    # print(patterns)
    for i,pattern in enumerate(patterns):
        matched=False
        visited.append(pattern)
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
        matched=isValidPattern2(newpatterntomatch,towels,maxsize,target,builtpattern,debug)
       
        if builtpattern==target: 
            if builtpattern in possibilities.keys(): possibilities[builtpattern]+=1
            else: possibilities[builtpattern]=1
            matched=True
            # builtpattern=''
    return matched
    
validpatterns=set()
invalidpatterns=set()
for i,pattern in enumerate(data):
    a=isValidPattern(str(pattern),tuple(towels),maxsizetocheck)
    if a==pattern: 
        validpatterns.add(a)

print('Part 1',len(validpatterns)) #296 is too low, but is valid answer for someone else, #301 is too low

validpatterns=set()
invalidpatterns=set()
for i,pattern in enumerate(data):
    print(i+1,'of',len(data))
    a=isValidPattern2(str(pattern),tuple(towels),maxsizetocheck,str(pattern))
    if a==True: 
        validpatterns.add(a)

print(possibilities)
print('Part 2',sum(possibilities.values()))

# Looks like I might have outsmarted myself, maybe

# Might have been smarter to see if towel in towels was in the pattern, and then generate combinations from that, but maybe not. Would still be a bunch of combos.

# For part 2, try returning the list of towels that were used, and then expand each of those into their smaller components.

# Only thing that might not work is if there is overlap, like if there was abcd and efgh and cdef and gh and ab in towels, which should then give [abcd,efgh] and [ab,cedf,gh] as options
# So recursion might still be the way to go, but without the early return. Not quite sure how to go about that one

