codefile="C://Users/Mark/Documents/Advent of Code/2020/day_9_example.txt"
codefile="C://Users/Mark/Documents/Advent of Code/2020/input_day9.txt"

def readIntegers(pathToFile):

    with open(pathToFile) as f:
        a = [int(x) for x in f.read().split()]
    return a

code=readIntegers(codefile)

window=25
idx=0
addset=[]
for idx in range(len(code)-window):
    available=code[idx:idx+window]
    #print(available)
    target=code[idx+window]
    #print(target)
    for i in range(len(available)):
        for j in range(len(available)):
            if i!=j:
                addset.append(available[i]+available[j])
    #print(addset)
    if target not in addset:
        print('Part 1 solution is',target)
        key=target
        break
    addset.clear()
    
#print(key)
solutionFound=False
idx=0
while not solutionFound:
    for sumlength in range(len(code)):
        summedlist=code[idx:idx+sumlength+1]
        #print(summedlist)
        test=sum(summedlist)
        #print(test)
        if test==key:
            print('Part 2 solution is',max(summedlist)+min(summedlist))
            solutionFound=True
            break
    idx=idx+1
