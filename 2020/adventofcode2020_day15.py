# -*- coding: utf-8 -*-
"""
Created on Sun Nov  7 09:23:48 2021

@author: Mark
"""

numbers=[0,3,6]
numbers=[1,3,2]
numbers=[3,1,2]
numbers=[15,12,0,14,3,1]

# nstart=len(numbers)
# for turn in range(1,2020+1):
   
#     #print(turn)
#     if turn>nstart:
#         last=numbers[-1]
#         #print(last)
#         idx=[idx for idx, x in enumerate(numbers) if x==last]
#         #print(idx)
#         if len(idx)==1: #last was the first time it was used
#             numbers.append(0)
#         else:
#             numbers.append(idx[-1]-idx[-2])
        
#     #print(numbers)       
           
# print("The solution to part one is",numbers[-1])  

# Populate dictionary
counts={}
lastidx={}
for i in range(0,len(numbers)):
    lastidx[numbers[i]]=i+1
    counts[numbers[i]]=1
nstart=len(numbers)
last=numbers[-1]
previdx=lastidx.copy()
pprevidx=previdx.copy()

target=2020
target=30000000

for turn in range(1,target+1):

    
    if turn>nstart:
        
        
        if counts[last]==1: #first time last number was used
            newnumber=0
            lastidx[newnumber]=turn
            if newnumber in counts:
                counts[newnumber]=counts[newnumber]+1
            else:
                counts[newnumber]=1
            #last=newnumber
            
        else:
            newnumber=previdx[last]-pprevidx[last]
            lastidx[newnumber]=turn
            if newnumber in counts:
                counts[newnumber]=counts[newnumber]+1
            else:
                counts[newnumber]=1
            #last=newnumber
        
        #pprevidx=previdx.copy()
        #previdx=lastidx.copy()
        pprevidx[last]=turn-1
        previdx[newnumber]=turn
        last=newnumber
    
    #if turn%10000==0: print(turn,last)
print("The solution is",last)  
        