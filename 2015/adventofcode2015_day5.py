fname='input_day5.txt'
with open(fname) as fp: data = fp.read().splitlines()
#data=['ugknbfddgicrmopn','jchzalrnumimnmhp','haegwjzuvuyypxyu','dvszwmarrgswjxmb']

def check3Vowels(s):
    nvowels=0
    vowels='aeiou'
    for letter in s:
        if letter in vowels:
            nvowels+=1
    if nvowels>=3:
        return True
    else:
        return False
    
def checkDoubleLetter(s):
    for i in range(len(s)-1):
        if s[i]==s[i+1]:
            return True
    return False

def checkNaughty(s):
    naughty=['ab','cd', 'pq', 'xy']
    for pair in naughty:
        if pair in s:
            return True
    return False

def checkRepeatPairs(s):
    for i in range(len(s)-1):
        pair=s[i:i+2]
        if pair in s[i+2:]:
            return True
    return False

def checkGapDoubleLetter(s):
    for i in range(len(s)-2):
        if s[i]==s[i+2]:
            return True
    return False

niceCount=0        
for entry in data:
    if check3Vowels(entry) and checkDoubleLetter(entry) and not checkNaughty(entry):
        niceCount+=1
        
print('Part 1 solution is', niceCount)

niceCount=0        
for entry in data:
    if checkRepeatPairs(entry) and checkGapDoubleLetter(entry):
        niceCount+=1
        
print('Part 2 solution is', niceCount)
