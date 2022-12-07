#from collections import defaultdict
#import numpy as np
# from numpy import Inf
fname="C://Users/Mark/Documents/Advent of Code/2021/day_24_example2.txt"
fname="C://Users/Mark/Documents/Advent of Code/2021/input_day24.txt"
with open(fname) as fp: data = fp.read().splitlines()

def inp(a):
    
    return(a)

def add(a,b):
    
    a=a+b
    return(a)

def mul(a,b):
    
    a=a*b
    return(a)

def div(a,b):
    
    if b==0:
        a=0
    else:
        a=a//b
    return(a)

def mod(a,b):
   
    if b==0:
        a=0
    else:
        a=a%b
    return(a)

def eql(a,b):
   
    if a==b:
        a=1
    else:
        a=0
    return(a)


# digit=list()
# page=list()
# inpcount=0
# for row in data:
   
#     if row.split()[0]=='inp': inpcount+=1
#     if row.split()[0]=='inp' and inpcount>0:
#         digit.append(page)
#         page=list()
#     page.append(row)   
# digit.pop(0)      
# digit.append(page)

sol=dict()


model=99999999999999+1
inpcount=0
for dmodel in range(99999999999999):
    model=model-1
    # print(model)
    test=[int(i) for i in str(model)]
    if 0 in test: continue
    sol['w']=0
    sol['x']=0
    sol['y']=0
    sol['z']=0
    inpcount=0
    #print(sol)
    print(model)
    for row in data:
        command=row.split()
       
       
        if command[1] in sol.keys():
            
            if command[0]=='inp':
               sol[command[1]]=test[inpcount]
               #print(sol[command[1]])
              
               inp(sol[command[1]])
               inpcount+=1
            if len(command)>2:
                if command[2] in sol.keys():
                    if command[0]=='add':
                        sol[command[1]]=add(sol[command[1]],sol[command[2]])
                    if command[0]=='mul':
                        sol[command[1]]=mul(sol[command[1]],sol[command[2]])
                    if command[0]=='div':
                        sol[command[1]]=div(sol[command[1]],sol[command[2]])
                    if command[0]=='mod':
                        sol[command[1]]=mod(sol[command[1]],sol[command[2]])
                    if command[0]=='eql':
                        sol[command[1]]=eql(sol[command[1]],sol[command[2]])
                else:
                    if command[0]=='add':
                        sol[command[1]]=add(sol[command[1]],int(command[2]))
                    if command[0]=='mul':
                        sol[command[1]]=mul(sol[command[1]],int(command[2]))
                    if command[0]=='div':
                        sol[command[1]]=div(sol[command[1]],int(command[2]))
                    if command[0]=='mod':
                        sol[command[1]]=mod(sol[command[1]],int(command[2]))
                    if command[0]=='eql':
                        sol[command[1]]=eql(sol[command[1]],int(command[2]))
    print(sol['z'])
    #model=model-1        
    if sol['z']==0:
        #if val>valmax: valmax=val
         print(model,'is valid')
         break

