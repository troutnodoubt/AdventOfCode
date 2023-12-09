fname='input_day8.txt'
#fname='example_day8a.txt'
#fname='example_day8b.txt'
#fname='example_day8c.txt'
with open(fname) as fp: data = fp.read().splitlines()

LR=data[0]
data.pop(0)

m = {line.split('=')[0][:-1]:(line.split('=')[1][1:].split(',')[0][1:],line.split('=')[1][1:].split(',')[1][1:-1]) for line in data if len(line)>0}


def findNextLoc(currentLoc,direction):
    if direction=='L':
        nextLoc=m[currentLoc][0]
    elif direction=='R':
        nextLoc=m[currentLoc][1]
    else:
        print('something is wrong')
    return nextLoc

solved=False
step=0
loc='AAA'
while not solved:
    direction=LR[step%len(LR)]
    loc=findNextLoc(loc,direction)
    step+=1
    if loc=='ZZZ':
        solved=True
        
print('Part 1', step)

loclist=[key for key in m.keys() if key[-1]=='A']
destlist=[key for key in m.keys() if key[-1]=='Z']

steplist=[]
solvedestlist=[]
for location in loclist:
    solved=False
    loc=location
    step=0
    while not solved:
        direction=LR[step%len(LR)]
        loc=findNextLoc(loc,direction)
        step+=1
        if loc in destlist:
            solved=True
            #print(location,loc,step)
            steplist.append(step)
            solvedestlist.append(loc)
            destlist.remove(loc)
    if len(destlist)==0: break
            
# solution is lowest common multiple of steplist. Did that outside the program, need to add a function to compute the final answer.

# sol=1
# for step in steplist:
#     sol*=step

print('Part 2 is lowest multiple of', steplist)
