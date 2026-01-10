
import math

fname='/home/mark/Documents/git/AdventOfCode/2025/input_day10.txt'
# fname='/home/mark/Documents/git/AdventOfCode/2025/example_day10.txt'
fname='/home/mark/Documents/git/AdventOfCode/2025/example_day10_full.txt'

with open(fname) as fp: data = fp.read().splitlines()

buttonTree=dict()

unpressed=[]
pressed=[]
pendingPress=[]

results=[]

trouble=[]

def nextState(currentState,button):
    nextState=[a for a in currentState]
    if isinstance(button,int): button=[button]
    for pos in button:
        # print('pos',pos)
        if currentState[int(pos)]=='.': nextState[int(pos)]='#'
        elif currentState[int(pos)]=='#': nextState[int(pos)]='.'
    nextState=''.join(a for a in nextState)
    return nextState

def findError(currentState,targetState):
    error=0
    for i in range(len(currentState)):
        if currentState[i]!=targetState[i]: error+=1
    return error

def findUnmatched(currentState,targetState):
    unmatched=[]
    # print(currentState,targetState)
    for i in range(len(currentState)):
        # print(currentState[i],targetState[i])
        if currentState[i]!=targetState[i]: unmatched.append(i)
    return unmatched

def findButtons(idx,buttons):
    candidates=[]
    for button in buttons:
        if isinstance(button,int):
            if button==idx: candidates.append(button)
        elif idx in button: candidates.append(button)
    return candidates

# def buildTree(start,target,buttons):
#     # find the position that has the fewest buttons that toggle it
#     ncands=999999
#     unmatched = findUnmatched(start,target)
#     # print(unmatched)
#     toTest=[]
#     print(start,target,buttons)
#     # print()
#     # if buttons==[]: return
#     '''This is close, but the starting state of each iteration isn't resetting
#     '''
#     for pos in unmatched:
#         cands=findButtons(pos,buttons)
#         if len(cands)<ncands:
#             ncands=len(cands)
#             toTest=[a for a in cands]
#     print('toTest',toTest)
#     for cand in toTest:
#         print('testing',cand)
#         print('start',start)
#         test=nextState(start,cand)
#         print(start,test)
#         if test==target:
#             # npress+=1
#             # return npress
#             buttonTree[cand].append(-1)
#             print()
#         else:
#             nextButtons=[a for a in buttons if a != cand]
#             # print(cand,nextButtons)
#             buttonTree[cand].append(nextButtons)
#             buildTree(test,target,nextButtons)

total=0
for row in data:
    print()
    pressed=[]
    unpressed=[]
    pressed=[]
    pendingPress=[]

    results=[]
    
    target=row.split(' ')[0][1:-1]
    current='.'*len(target)
    temp='.'*len(target)
    buttons=[eval(a) for a in row.split(' ')[1:-1]]
    unpressed=[a for a in buttons]
    best=''
    joltage=row.split(' ')[-1]
    print(buttons)
    print(target)
    # needs an outer while loop to cycle through other candidates, so also need an outer list to keep track of unvisited
    # try just doing this same thing, but on the first press start with different buttons
    found=False
    while not found:
    #find candidate buttons
        
        unmatched=findUnmatched(current,target)
        ncands=9999

    # stage the candidate buttons 

        for pos in unmatched:
            cands=findButtons(pos,unpressed)
            if len(cands)<ncands:
                ncands=len(cands)
                pendingPress=[a for a in cands]
        print(pendingPress)

        if len(pendingPress)==0:
            if len(unpressed)>0:
                print("filling in from the whole queue")
                pendingPress=[a for a in unpressed]
            else: # all cands exhausted
                trouble.append(row)
                break

        
        for button in pendingPress:
            # unpressed.remove(button)
            # check if any of them are sufficient to solve
            tempstate=nextState(current,button)
            if target==nextState(current,button) and not found:
                results.append([button,tempstate,target==tempstate])
                print(results)
                print(len(results))
                total+=len(results)
                found=True

    # press the first button in the list
        if not found:
            pressed.append(pendingPress.pop())
            unpressed.remove(pressed[-1])
            # print(pressed)
            current=nextState(current,pressed[-1])
            # print(current)
            results.append([pressed[-1],current,current==target])
            
            print(results)
            if current==target:
                print(results)
                print(len(results))
                total+=len(results)
                found=True

print()
print("Part 1 is",total)
print(trouble)

'''    
[(0, 3, 4, 5, 6, 7), (0, 1, 2, 3, 5, 7, 8), (0, 2, 3, 5, 6, 7, 8), (1, 5, 6, 7), (0, 1, 3, 4, 5, 6, 7), (1, 2, 3, 4, 5, 7), (2, 4, 6, 7, 8)]
.#...#...

is pressing every button but not finding a solution, so need to get the outer while loop going to try a different order, or try brute force on those that don't 
give a result
'''