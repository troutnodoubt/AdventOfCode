import numpy as np

fname="day8_example.txt"
fname="input_day8.txt"
with open(fname) as fp: data = fp.read().splitlines()

trees = np.array([[int(a) for a in row] for row in data])
resultarray=np.zeros((len(trees),len(trees)),int)
p=1
left=2
right=4
top=8
bottom=16


for row in range(1,len(trees[:,0])-1):
    for col in range(1,len(trees[0,:])-1):
        if (all(trees[row,col]>trees[row,:col])): #left
            resultarray[row,col]+=left
        if (all(trees[row,col]>trees[row,col+1:])): #right
            resultarray[row,col]+=right
        if (all(trees[row,col]>trees[:row,col])): #top
            resultarray[row,col]+=top
        if (all(trees[row,col]>trees[row+1:,col])): #bottom
            resultarray[row,col]+=bottom
            
resultarray[0,:]=p
resultarray[-1,:]=p
resultarray[:,0]=p
resultarray[:,-1]=p

print('Part 1 solution is',(resultarray>0).sum())

oldscore=0        
for row in range(1,len(trees[:,0])-1):
    for col in range(1,len(trees[0,:])-1):
        blocked=trees[row,col]<=trees[row,:col]
        nvisiblel=0
        for test in blocked[::-1]:
            if test==False:
                nvisiblel+=1
            else:
                nvisiblel+=1
                break
        
        blocked=trees[row,col]<=trees[row,col+1:]
        #print(blocked[::1])
        nvisibler=0
        for test in blocked[::1]:
            if test==False:
                nvisibler+=1
            else:
                nvisibler+=1
                break
            
        blocked=trees[row,col]<=trees[:row,col]
        #print(blocked[::-1])
        nvisiblet=0
        for test in blocked[::-1]:
            if test==False:
                nvisiblet+=1
            else:
                nvisiblet+=1
                break
        
        blocked=trees[row,col]<=trees[row+1:,col]
        #print(blocked[::1])
        nvisibleb=0
        for test in blocked[::1]:
            if test==False:
                nvisibleb+=1
            else:
                nvisibleb+=1
                break
        
        viewscore=nvisibler*nvisiblel*nvisiblet*nvisibleb

        if viewscore>oldscore:
            oldscore=viewscore
            
print('Part 2 solution is',oldscore)
