
fname='input_day5.txt'
#fname='example_day5.txt'
with open(fname) as fp: data = fp.read().splitlines()

rules=[]
rulesdict={}
produced=[]
for row in data:
    if '|' in row: 
        rules.append(tuple(int(a) for a in row.split('|')))
    else:
        produced.append(list(int(a) for a in row.split(',') if a is not ''))

produced=produced[1:]

for rule in rules:
    if rule[0] not in rulesdict.keys(): rulesdict[rule[0]]=[rule[1]]
    else: rulesdict[rule[0]].append(rule[1])

#print(rulesdict.keys(),rulesdict.values())

def isRightOrder(update):
    rightorder=1
    for i in range(len(update)-1):
        page=update[i]
        if page in rulesdict.keys():
            followers=rulesdict[page]
        else:
            rightorder=0
            break
        for nextpage in update[i+1:]:
            if nextpage not in followers: rightorder=0
    return rightorder

total=0
needsHelp=[]
for update in produced:
    rightorder=isRightOrder(update)
    total+=rightorder*update[len(update)//2]
    if not rightorder: needsHelp.append(update)
    
print("Part 1 is", total) 
#print("Part 1 is", total) 

# fixed=[]
# for update in needsHelp:
#     count=0
#     while True:
#         count+=1
#         for i in range(len(update)-1):
#             page=update[i]
#             if page in rulesdict.keys():
#                 followers=rulesdict[page]
#             else:
#                 update[i],update[i+1]=update[i+1], update[i]
#                 break
#             for nextpage in update[i+1:]:
#                 if nextpage not in followers: update[i],update[i+1]=update[i+1], update[i]
#             #print(update)
#         if isRightOrder(update): break
#         if count>1000:
#             print("count exceeded")
#             print(update)
#             break
#     #print(update)
#     fixed.append(update)


# #print(fixed)
# total=0
# for update in fixed:
#     total+=update[len(update)//2]

# print("Part 2 is", total)
#91, 55, 32, 25, 77

print(91, rulesdict[91])
print(55, rulesdict[55])
print(32, rulesdict[32])
print(25, rulesdict[25])
print(77, rulesdict[77])

update=[91, 55, 32, 25, 77]
count=0
while True:
    count+=1
    for i in range(len(update)-1):
        page=update[i]
        print(page)
        if page in rulesdict.keys():
            followers=rulesdict[page]
            print('a')
        else:
            update[i],update[i+1]=update[i+1], update[i]
            print('b')
            break
        for nextpage in update[i+1:]:
            if nextpage not in followers: 
                print(update,i,i+1)
                
                update[i],update[i+1]=update[i+1], update[i]
                print('c')
        print('end',update)
    if isRightOrder(update): break
    if count>100:
        print("count exceeded")
        print(update)
        break
