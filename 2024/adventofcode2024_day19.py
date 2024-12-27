
# fname='input_day19.txt'

# with open(fname) as fp: data = fp.read().splitlines()

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

towels=data[0].split(', ')
data.pop(0)
data.pop(0)
maxsizetocheck=0
for towel in towels:
    if len(towel)>maxsizetocheck: maxsizetocheck=len(towel)

# print(towels)
# print(maxsizetocheck)

def isValidPattern(pattern,towels):
    idx=0
    patternstring=pattern[idx]
    matches=[]
    
    while len(patternstring)>0:
        print(patternstring)
        # print(idx)
        # print(len(pattern))
        print(matches)
        print()
        if patternstring in towels and idx in range(len(pattern)):
            
            matches.append(patternstring)
            if idx+1 in range(len(pattern)):
                print('next char is', pattern[idx+1])
                patternstring=pattern[idx+1]
        else:
            if idx+1 in range(len(pattern)): patternstring=patternstring+pattern[idx+1]
            else: 
                matchFound=False
                break
        idx+=1
        if idx>len(pattern): break

        test=''.join(a for a in matches)
        
        if test==pattern:
            matchFound=True
            break
    print(test)
    print(pattern)  
    print(matchFound)
    return matchFound  

# isValidPattern('brwrr',towels)

validcount=0
for pattern in data:
    print()
    print()
    print(pattern)
    if isValidPattern(pattern,towels): validcount+=1

print(validcount)
# pattern=brwrr
# put first character on stack
# stack = b
# is stack in towels
# if yes, pattern = rwrr and empty the stack, repeat with rest of the string
# if no, put next character on stack