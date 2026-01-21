import itertools
import numpy as np
import sympy

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
    # print(maxButton)
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
    # joltage=np.transpose(joltage)
    # print(buttons)
    # print(A)
    # print(joltage)
    A=np.append(A,joltage,1)
    # print(A)
    # print()
    
    A=sympy.Matrix(A)
    A=A.rref()[0]
    
    nrows=sympy.shape(A)[0]
    ncols=sympy.shape(A)[1]
    A=np.array(A)
    # print()
    # print(A)
    # print()
    # print(ncols)
    rowstoDelete=[]
    for i in range(nrows):
        # print(list(A[i,:]))
        row=list(A[i,:])
        count=len([a for a in row if a!=0])-1
        # print(row,count)
        if count==-1: rowstoDelete.append(i)
   
    for row in rowstoDelete:
        A=np.delete(A,-1,axis=0)
    # print()
    # print(A)
    # print()
    toAdd=[]
    maxVal=np.max(A[:,-1])
    minVal=0 #np.min(A[:,-1])
    possibilities=range(minVal,maxVal+1)
    for col in range(0,ncols-1):
        # print(col)
        # print(A[:,col],np.count_nonzero(A[:,col]))
        if np.count_nonzero(A[:,col])>1: toAdd.append(col)
   
    # print(len(toAdd))
    its=itertools.permutations(possibilities,len(toAdd))
    minpress=99999
    
    for it in its:
        B=np.copy(A)
        for i,col in enumerate(toAdd):
            newrow=np.zeros(ncols,dtype=int)
            newrow[-1]=int(it[i])
            newrow[col]=1
            B=np.vstack([B,newrow])
        # print(np.array(B))
        # print()
        # print("solving")
        
        B=sympy.Matrix(B)
        B=B.rref()[0]
        # print(np.array(B))
        # print(np.array(B[:,-1]).sum())
        # print(np.array(B[:,-1]))
        # print(np.array(B[:,-1])>=0)
        # print()
        # print(all(np.array(B[:,-1])>0))
        if all(np.array(B[:,-1])>=0): 
            if np.array(B[:,-1]).sum()<minpress: minpress = np.array(B[:,-1]).sum()
    print(minpress)
    print()
    total2+=minpress



print("Part 1 solution",total)       
print("Part 2 solution",total2)       
  