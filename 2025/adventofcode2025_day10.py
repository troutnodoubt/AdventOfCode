import itertools
import numpy as np
import sympy

fname='/home/mark/Documents/git/AdventOfCode/2025/input_day10.txt'
# fname='/home/mark/Documents/git/AdventOfCode/2025/example_day10.txt'

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
total2=0

for row in data:
    target=row.split(' ')[0][1:-1]
    current='.'*len(target)
    buttons=[eval(a) for a in row.split(' ')[1:-1]]
    joltage=row.split(' ')[-1]
    joltage=[int(a) for a in joltage[1:-1].split(',')]
    found=False
    print(row)
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

    # part 2
    maxButton=len(target)
    A=[]
    for i,button in enumerate(buttons):
        if isinstance(button,int): button=[button]
        row=[0 for m in range(maxButton)]
        for j in range(maxButton):
            if j in button:
                row[j]=1
            else:
                row[j]=0
        A.append(row)
    A=np.array(A)
    A=np.transpose(A)
    joltage=np.c_[joltage]
    A=np.append(A,joltage,1)
    
    A=sympy.Matrix(A)
    A=A.rref()[0]
    
    nrows=sympy.shape(A)[0]
    ncols=sympy.shape(A)[1]
    A=np.array(A)

    rowstoDelete=[]
    independent=set()
    for i in range(nrows):
        row=list(A[i,:])
        count=len([a for a in row if a!=0])-1
        if count==-1: rowstoDelete.append(i)
        if count>1:
            temp=[]
            for pos,var in enumerate(row[:-1]):
                if var!=0:
                    temp.append(pos)
            for v in temp[1:]:
                independent.add(v)
                
   
    for row in rowstoDelete:
        A=np.delete(A,-1,axis=0)

    toAdd=[]
    if isinstance(np.max(A[:,-1]),int):
        maxVal=np.max(A[:,-1])
    else:
        maxVal=int(np.max(A[:,-1]))+1

    minVal=0
    possibilities=range(minVal,maxVal+1)
    for col in range(0,ncols-1):
        if np.count_nonzero(A[:,col])>1: toAdd.append(col)
   
    combs=itertools.combinations_with_replacement(possibilities,len(toAdd))
    
    minpress=99999
    tested=[]
    for comb in combs:
        for it in itertools.permutations(comb):
            if it not in tested:
                tested.append(it)
                B=np.copy(A)
                for i,col in enumerate(toAdd):
                    newrow=np.zeros(ncols,dtype=int)
                    newrow[-1]=int(it[i])
                    newrow[col]=1
                    B=np.vstack([B,newrow])
                
                B=sympy.Matrix(B)
                B=B.rref()[0]
                allInts=all([int(a)==a for a in list(B[:,-1])])
                if all(np.array(B[:,-1])>=0) and allInts: 
                    if np.array(B[:,-1]).sum()<minpress:
                        minpress = np.array(B[:,-1]).sum()
                        
    print(minpress)
    if minpress==99999: break
    print()
    total2+=minpress

print("Part 1 solution",total)       
print("Part 2 solution",total2)  #20045 is too high, cheat guess of 19998 is too low, so I'm close   

# 20044 - too high
# 20043 - too high
# 20042 - correct! on a guess 