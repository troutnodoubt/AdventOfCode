import itertools

fname='/home/mark/Documents/git/AdventOfCode/2025/input_day10.txt'
# fname='/home/mark/Documents/git/AdventOfCode/2025/example_day10.txt'
# fname='/home/mark/Documents/git/AdventOfCode/2025/example_day10_full.txt'

with open(fname) as fp: data = fp.read().splitlines()

def nextState(currentState,button):
    nextState=[a for a in currentState]
    if isinstance(button,int): button=[button]
    for pos in button:
        if currentState[int(pos)]=='.': nextState[int(pos)]='#'
        elif currentState[int(pos)]=='#': nextState[int(pos)]='.'
    nextState=''.join(a for a in nextState)
    return nextState

total=0
for row in data:
    target=row.split(' ')[0][1:-1]
    current='.'*len(target)
    buttons=[eval(a) for a in row.split(' ')[1:-1]]
    joltage=row.split(' ')[-1]
    found=False
    for i in range(1,len(buttons)+1):
        for comb in itertools.combinations(buttons,i):
            current='.'*len(target)
            for button in comb:
                current=nextState(current,button)
            if current==target:
                found=True
        if found:
            total+=i
            break
print("Part 1 solution",total)       
  