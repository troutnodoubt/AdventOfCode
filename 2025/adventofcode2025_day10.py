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

maxIndependent=0
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
    # print(np.matmul(A,np.array(np.transpose(test))))
    # print(sum(test))
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
    independent=set()
    for i in range(nrows):
        # print(list(A[i,:]))
        row=list(A[i,:])
        count=len([a for a in row if a!=0])-1
        # print(row,count)
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
    # print()
    # print(A)
    # print()
    toAdd=[]
    if isinstance(np.max(A[:,-1]),int):
        maxVal=np.max(A[:,-1])
    else:
        maxVal=int(np.max(A[:,-1]))+1
    # maxVal=10
    # print(maxVal)
    # maxVal=max(joltage)[0]
    # max2=max(np.array(A[:,-1]))*2//2
    
    # print(maxVal,max2)
    # maxVal=min(maxVal,max2)
    # maxVal=2
    minVal=0 #np.min(A[:,-1])
    possibilities=range(minVal,maxVal+1)
    for col in range(0,ncols-1):
        # print(col)
        # print(A[:,col],np.count_nonzero(A[:,col]))
        if np.count_nonzero(A[:,col])>1: toAdd.append(col)
   
    # print(len(toAdd))
    its1=itertools.combinations_with_replacement(possibilities,len(toAdd))
    its=itertools.permutations(possibilities,len(toAdd))
    minpress=99999
    
    # print("independent variables")
    # print("column method - should be wrong in some instances")
    # t1=[]
    # t2=[]
    # for a in toAdd:
    #     print(a)
    #     t1.append(a)
    # print("row method - should be accurate")
    # for a in independent:
    #     print(a)
    #     t2.append(a)
    # t1.sort()
    # t2.sort()

    # print(t1==t2)
    # print(len(t1))
    # if len(t1)>maxIndependent: maxIndependent=len(t1)
    # if t1!=t2: break
    # toAdd.sort()
    for it in its:
        B=np.copy(A)
        for i,col in enumerate(toAdd):
            newrow=np.zeros(ncols,dtype=int)
            newrow[-1]=int(it[i])
            newrow[col]=1
            B=np.vstack([B,newrow])
            # print(int(it[i]))
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
        # print(list(B[:,-1]))
        allInts=all([int(a)==a for a in list(B[:,-1])])
        # allInts=[isinstance(a,int) for a in list(np.array(B[:,-1]))[0]]
        # print(allInts)
        # if (allInts): print(np.array(B))
        if all(np.array(B[:,-1])>=0) and allInts: 
            
            if np.array(B[:,-1]).sum()<minpress:
                minpress = np.array(B[:,-1]).sum()
                # for r in np.array(B):
                #     print(r)
                # print(minpress)
                # print()
    for it in its1:
        B=np.copy(A)
        for i,col in enumerate(toAdd):
            newrow=np.zeros(ncols,dtype=int)
            newrow[-1]=int(it[i])
            newrow[col]=1
            B=np.vstack([B,newrow])
            # print(int(it[i]))
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
        # print(list(B[:,-1]))
        allInts=all([int(a)==a for a in list(B[:,-1])])
        # allInts=[isinstance(a,int) for a in list(np.array(B[:,-1]))[0]]
        # print(allInts)
        # if (allInts): print(np.array(B))
        if all(np.array(B[:,-1])>=0) and allInts: 
            
            if np.array(B[:,-1]).sum()<minpress:
                minpress = np.array(B[:,-1]).sum()
                # for r in np.array(B):
                #     print(r)
                # print(minpress)
                # print()
    print(minpress)
    if minpress==99999: break
    print()
    total2+=minpress


print(maxIndependent)
print("Part 1 solution",total)       
print("Part 2 solution",total2)  #20045 is too high, cheat guess of 19998 is too low, so I'm close   

# 20044 - too high
# 20043 - too high
# 20042 - correct! on a guess 
# 20020 - not right, no indication of high or low
# 20008 - random guess, not right

# might be able to speed things up by running two points for each new row and tracing those lines

# I can get 69 instead of 70 on test0 with 0, 0, 1 for x3, x6, x8 by hand, test those with the current method