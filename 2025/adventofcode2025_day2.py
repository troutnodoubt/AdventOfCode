fname='input_day2.txt'
# fname='example_day2.txt'

with open(fname) as fp: data = fp.read().splitlines()

def isValid(ID):
    ID=str(ID)
    if len(ID)%2!=0: return True # odd length IDs must be valid 
    if ID[:len(ID)/2] == ID[len(ID)/2:]: return False
    else: return True

def isValid2(ID):
    ID=str(ID)
    for i in range(1,len(ID)+1):
        chunk = ID[:i]
        if ID.count(chunk)>1 and ID.count(chunk)*len(chunk) == len(ID): return False
    return True

total=0
total2=0
for rng in data[0].split(','):
    for test in range(int(rng.split('-')[0]),int(rng.split('-')[1])+1):
        if not isValid(test): total+=test
        if not isValid2(test): total2+=test

print('Part 1 is', total)
print('Part 2 is', total2)
