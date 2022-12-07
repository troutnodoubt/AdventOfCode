from collections import Counter
import math
fname="C://Users/Mark/Documents/Advent of Code/2021/day_14_example.txt"
fname="C://Users/Mark/Documents/Advent of Code/2021/input_day14.txt"
#fname="day_14_example.txt"
#fname="input_day14.txt"
with open(fname) as fp: data = fp.read().splitlines()

template=data[0]
instructions=dict()

for row in data:
    if row!='' and row!=template:
        a,b=row.split(' -> ')
        instructions[a]=b
        #print(row)

# count=0
# while count<1:

#     insertstring=' '*(len(template)-1)
#     insertstring=list(insertstring)    
#     for letteridx in range(len(template)-1):
      
#         test=template[letteridx]+template[letteridx+1]
#         #print(test)
#         if test in instructions.keys():
#             insertstring[letteridx]=instructions[test]
#     #print(insertstring)
#     newstring=''
#     for letteridx in range(len(template)-1):
#         newstring=newstring+template[letteridx]
#         if insertstring[letteridx]!=' ':
#             newstring=newstring+insertstring[letteridx]
#     newstring=newstring+template[-1]
#     template=newstring
#     #print(template)
#     count+=1
#     print(count)
    
# a=Counter(template).most_common()
# print('Part 1 solution is',a[0][1]-a[-1][1])

parentlist=list()
           
for letteridx in range(len(template)-1):
    parentlist.append(template[letteridx]+template[letteridx+1])
a=Counter(parentlist)

spawncount=dict()

# for letter1 in [char for char in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ']:
#         for letter2 in [char for char in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ']:
#             spawncount[letter1+letter2]=0

# parentcount=spawncount.copy()
# for key in a.keys():
#     parentcount[key]=a[key]
    

# for key in spawncount.keys():
#     if spawncount[key]>0:
#         print(key,spawncount[key])

# print('')
count=0
while count<40:
    spawncount=dict()  
    for key in a.keys():
        for i in range(1): #range(a[key]):
            # print(a)
            # print(key,a[key],instructions[key])
            # print(key[0]+instructions[key])
            # print(instructions[key]+key[1])
            if key[0]+instructions[key] in spawncount.keys():
                spawncount[key[0]+instructions[key]]+=a[key]
            else:
                spawncount[key[0]+instructions[key]]=a[key]
            if instructions[key]+key[1] in spawncount.keys():
                spawncount[instructions[key]+key[1]]+=a[key]
            else:
                spawncount[instructions[key]+key[1]]=a[key]
            # print(spawncount)
    a=spawncount.copy()
    # print(a)
    count+=1
        
# count=0
# while count<10:
#     spawn=list()
#     for key in a.keys():
#         #print(key,key[0],key[1])
#         for i in range(a[key]):
#             spawn.append(key[0]+instructions[key])
#             spawn.append(instructions[key]+key[1])
#     #print(spawn)
    
#     b=Counter(spawn)
#     a=b.copy()
#     count+=1
#     print(count)

letterdict=dict()
for letter in [char for char in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ']:
    #print(letter)
    letterdict[letter]=0


for letter in [char for char in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ']:
    for entry in a.keys():
        if entry[0]==letter:
            letterdict[letter]+=a[entry]
        if entry[1]==letter:
            letterdict[letter]+=a[entry]

results=list()
for number in letterdict.values():
    if number!=0:
        results.append(number)
        

#print('Solution is',math.ceil(max(letterdict.values())/2)-math.ceil(min(letterdict.values())/2))
print('Solution is',math.ceil(max(results)/2)-math.ceil(min(results)/2))

