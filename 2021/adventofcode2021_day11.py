import numpy as np
fname="C://Users/Mark/Documents/Advent of Code/2021/day_11_example.txt"
#fname="C://Users/Mark/Documents/Advent of Code/2021/day_11_example_step9.txt"
fname="C://Users/Mark/Documents/Advent of Code/2021/input_day11.txt"
with open(fname) as fp: data = fp.read().splitlines()

octolevel=np.array([[int(a) for a in row]for row in data])
flashed=np.array([[False for a in row]for row in data])
finalflashed=flashed.copy()
oldflashed=flashed.copy()
flash=0
#print(octolevel)
for steps in range(1,100+1):
    octolevel+=1
    any9=True
    #print(octolevel)
    flashed=np.array([[False for a in row]for row in data])
    finalflashed=flashed.copy()
    oldflashed=flashed.copy()
    while any9:
        
        for i in range(10):
            for j in range(10):
               
                if octolevel[i][j]>9 and not flashed[i][j]:
                    #print('still flashing')
                    #print(i,j)
                    if i>0 and i<9 and j>0 and j<9: octolevel[i-1][j-1]+=1
                    if i>0 and i<9 and j>0 and j<9: octolevel[i-1][j-0]+=1
                    if i>0 and i<9 and j>0 and j<9: octolevel[i-1][j+1]+=1
                    if i>0 and i<9 and j>0 and j<9: octolevel[i-0][j-1]+=1
                    if i>0 and i<9 and j>0 and j<9: octolevel[i-0][j-0]+=1
                    if i>0 and i<9 and j>0 and j<9: octolevel[i-0][j+1]+=1
                    if i>0 and i<9 and j>0 and j<9: octolevel[i+1][j-1]+=1
                    if i>0 and i<9 and j>0 and j<9: octolevel[i+1][j-0]+=1
                    if i>0 and i<9 and j>0 and j<9: octolevel[i+1][j+1]+=1
                    
                    if i==0 and j==0: octolevel[i+1][j]+=1
                    if i==0 and j==0: octolevel[i][j+1]+=1
                    if i==0 and j==0: octolevel[i+1][j+1]+=1
                    if i==0 and j==0: octolevel[i][j]+=1
                    
                    if i==0 and j==9: octolevel[i+1][j]+=1
                    if i==0 and j==9: octolevel[i][j-1]+=1
                    if i==0 and j==9: octolevel[i+1][j-1]+=1
                    if i==0 and j==9: octolevel[i][j]+=1
                    
                    if i==9 and j==0: octolevel[i-1][j]+=1
                    if i==9 and j==0: octolevel[i][j+1]+=1
                    if i==9 and j==0: octolevel[i-1][j+1]+=1
                    if i==9 and j==0: octolevel[i][j]+=1
                    
                    if i==9 and j==9: octolevel[i-1][j]+=1
                    if i==9 and j==9: octolevel[i][j-1]+=1
                    if i==9 and j==9: octolevel[i-1][j-1]+=1
                    if i==9 and j==9: octolevel[i][j]+=1
                    
                    
                    # if i==0 and j>0 and j<9: octolevel[i-1][j-1]+=1
                    # if i==0 and j>0 and j<9: octolevel[i-1][j-0]+=1
                    # if i==0 and j>0 and j<9: octolevel[i-1][j+1]+=1
                    if i==0 and j>0 and j<9: octolevel[i-0][j-1]+=1
                    if i==0 and j>0 and j<9: octolevel[i-0][j-0]+=1
                    if i==0 and j>0 and j<9: octolevel[i-0][j+1]+=1
                    if i==0 and j>0 and j<9: octolevel[i+1][j-1]+=1
                    if i==0 and j>0 and j<9: octolevel[i+1][j-0]+=1
                    if i==0 and j>0 and j<9: octolevel[i+1][j+1]+=1
                    
                    if i==9 and j>0 and j<9: octolevel[i-1][j-1]+=1
                    if i==9 and j>0 and j<9: octolevel[i-1][j-0]+=1
                    if i==9 and j>0 and j<9: octolevel[i-1][j+1]+=1
                    if i==9 and j>0 and j<9: octolevel[i-0][j-1]+=1
                    if i==9 and j>0 and j<9: octolevel[i-0][j-0]+=1
                    if i==9 and j>0 and j<9: octolevel[i-0][j+1]+=1
                    # if i==0 and j>0 and j<9: octolevel[i+1][j-1]+=1
                    # if i==0 and j>0 and j<9: octolevel[i+1][j-0]+=1
                    # if i==0 and j>0 and j<9: octolevel[i+1][j+1]+=1
                    
                    #if i>0 and i<9 and j==0: octolevel[i-1][j-1]+=1
                    if i>0 and i<9 and j==0: octolevel[i-1][j-0]+=1
                    if i>0 and i<9 and j==0: octolevel[i-1][j+1]+=1
                    #if i>0 and i<9 and j==0: octolevel[i-0][j-1]+=1
                    if i>0 and i<9 and j==0: octolevel[i-0][j-0]+=1
                    if i>0 and i<9 and j==0: octolevel[i-0][j+1]+=1
                    #if i>0 and i<9 and j==0: octolevel[i+1][j-1]+=1
                    if i>0 and i<9 and j==0: octolevel[i+1][j-0]+=1
                    if i>0 and i<9 and j==0: octolevel[i+1][j+1]+=1
                    
                    if i>0 and i<9 and j==9: octolevel[i-1][j-1]+=1
                    if i>0 and i<9 and j==9: octolevel[i-1][j-0]+=1
                    #if i>0 and i<9 and j==9: octolevel[i-1][j+1]+=1
                    if i>0 and i<9 and j==9: octolevel[i-0][j-1]+=1
                    if i>0 and i<9 and j==9: octolevel[i-0][j-0]+=1
                    #if i>0 and i<9 and j==9: octolevel[i-0][j+1]+=1
                    if i>0 and i<9 and j==9: octolevel[i+1][j-1]+=1
                    if i>0 and i<9 and j==9: octolevel[i+1][j-0]+=1
                    #if i>0 and i<9 and j==9: octolevel[i+1][j+1]+=1
                    #print(octolevel)        
       
                    
                    flashed[i][j]=octolevel[i][j]>9
        finalflashed=flashed.copy()
        if np.count_nonzero(finalflashed==True)==np.count_nonzero(oldflashed==True): any9=False
        oldflashed=finalflashed.copy()
        
        #print(flashed)
    octolevel[octolevel>=10]=0
    flash+=np.count_nonzero(octolevel==0)
    #print(octolevel)
    #print(steps,flash)
    
print('Part 1 solution is',flash)   


octolevel=np.array([[int(a) for a in row]for row in data])
flashed=np.array([[False for a in row]for row in data])
finalflashed=flashed.copy()
oldflashed=flashed.copy()
flash=0
#print(octolevel)
allflashed=False
steps=0
#for steps in range(1,100+1):
while not allflashed:
    
    octolevel+=1
    any9=True
    #print(octolevel)
    flashed=np.array([[False for a in row]for row in data])
    finalflashed=flashed.copy()
    oldflashed=flashed.copy()
    while any9:
        
        for i in range(10):
            for j in range(10):
               
                if octolevel[i][j]>9 and not flashed[i][j]:
                    #print('still flashing')
                    #print(i,j)
                    if i>0 and i<9 and j>0 and j<9: octolevel[i-1][j-1]+=1
                    if i>0 and i<9 and j>0 and j<9: octolevel[i-1][j-0]+=1
                    if i>0 and i<9 and j>0 and j<9: octolevel[i-1][j+1]+=1
                    if i>0 and i<9 and j>0 and j<9: octolevel[i-0][j-1]+=1
                    if i>0 and i<9 and j>0 and j<9: octolevel[i-0][j-0]+=1
                    if i>0 and i<9 and j>0 and j<9: octolevel[i-0][j+1]+=1
                    if i>0 and i<9 and j>0 and j<9: octolevel[i+1][j-1]+=1
                    if i>0 and i<9 and j>0 and j<9: octolevel[i+1][j-0]+=1
                    if i>0 and i<9 and j>0 and j<9: octolevel[i+1][j+1]+=1
                    
                    if i==0 and j==0: octolevel[i+1][j]+=1
                    if i==0 and j==0: octolevel[i][j+1]+=1
                    if i==0 and j==0: octolevel[i+1][j+1]+=1
                    if i==0 and j==0: octolevel[i][j]+=1
                    
                    if i==0 and j==9: octolevel[i+1][j]+=1
                    if i==0 and j==9: octolevel[i][j-1]+=1
                    if i==0 and j==9: octolevel[i+1][j-1]+=1
                    if i==0 and j==9: octolevel[i][j]+=1
                    
                    if i==9 and j==0: octolevel[i-1][j]+=1
                    if i==9 and j==0: octolevel[i][j+1]+=1
                    if i==9 and j==0: octolevel[i-1][j+1]+=1
                    if i==9 and j==0: octolevel[i][j]+=1
                    
                    if i==9 and j==9: octolevel[i-1][j]+=1
                    if i==9 and j==9: octolevel[i][j-1]+=1
                    if i==9 and j==9: octolevel[i-1][j-1]+=1
                    if i==9 and j==9: octolevel[i][j]+=1
                    
                    
                    # if i==0 and j>0 and j<9: octolevel[i-1][j-1]+=1
                    # if i==0 and j>0 and j<9: octolevel[i-1][j-0]+=1
                    # if i==0 and j>0 and j<9: octolevel[i-1][j+1]+=1
                    if i==0 and j>0 and j<9: octolevel[i-0][j-1]+=1
                    if i==0 and j>0 and j<9: octolevel[i-0][j-0]+=1
                    if i==0 and j>0 and j<9: octolevel[i-0][j+1]+=1
                    if i==0 and j>0 and j<9: octolevel[i+1][j-1]+=1
                    if i==0 and j>0 and j<9: octolevel[i+1][j-0]+=1
                    if i==0 and j>0 and j<9: octolevel[i+1][j+1]+=1
                    
                    if i==9 and j>0 and j<9: octolevel[i-1][j-1]+=1
                    if i==9 and j>0 and j<9: octolevel[i-1][j-0]+=1
                    if i==9 and j>0 and j<9: octolevel[i-1][j+1]+=1
                    if i==9 and j>0 and j<9: octolevel[i-0][j-1]+=1
                    if i==9 and j>0 and j<9: octolevel[i-0][j-0]+=1
                    if i==9 and j>0 and j<9: octolevel[i-0][j+1]+=1
                    # if i==0 and j>0 and j<9: octolevel[i+1][j-1]+=1
                    # if i==0 and j>0 and j<9: octolevel[i+1][j-0]+=1
                    # if i==0 and j>0 and j<9: octolevel[i+1][j+1]+=1
                    
                    #if i>0 and i<9 and j==0: octolevel[i-1][j-1]+=1
                    if i>0 and i<9 and j==0: octolevel[i-1][j-0]+=1
                    if i>0 and i<9 and j==0: octolevel[i-1][j+1]+=1
                    #if i>0 and i<9 and j==0: octolevel[i-0][j-1]+=1
                    if i>0 and i<9 and j==0: octolevel[i-0][j-0]+=1
                    if i>0 and i<9 and j==0: octolevel[i-0][j+1]+=1
                    #if i>0 and i<9 and j==0: octolevel[i+1][j-1]+=1
                    if i>0 and i<9 and j==0: octolevel[i+1][j-0]+=1
                    if i>0 and i<9 and j==0: octolevel[i+1][j+1]+=1
                    
                    if i>0 and i<9 and j==9: octolevel[i-1][j-1]+=1
                    if i>0 and i<9 and j==9: octolevel[i-1][j-0]+=1
                    #if i>0 and i<9 and j==9: octolevel[i-1][j+1]+=1
                    if i>0 and i<9 and j==9: octolevel[i-0][j-1]+=1
                    if i>0 and i<9 and j==9: octolevel[i-0][j-0]+=1
                    #if i>0 and i<9 and j==9: octolevel[i-0][j+1]+=1
                    if i>0 and i<9 and j==9: octolevel[i+1][j-1]+=1
                    if i>0 and i<9 and j==9: octolevel[i+1][j-0]+=1
                    #if i>0 and i<9 and j==9: octolevel[i+1][j+1]+=1
                    #print(octolevel)        
       
                    
                    flashed[i][j]=octolevel[i][j]>9
        finalflashed=flashed.copy()
        if np.count_nonzero(finalflashed==True)==np.count_nonzero(oldflashed==True): any9=False
        oldflashed=finalflashed.copy()
        
        #print(flashed)
    octolevel[octolevel>=10]=0
    flash+=np.count_nonzero(octolevel==0)
    #print(octolevel)
    #print(steps,flash)
    steps+=1
    allflashed=(octolevel==0).all()
    
print('Part 2 solution is',steps)  

   