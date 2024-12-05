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

fixed=[]
for update in needsHelp:
     count=0
     while True:
         count+=1
         for i in range(len(update)-1):
             page=update[i]
             if page in rulesdict.keys():
                 followers=rulesdict[page]
             else:
                 tmp=update.pop(i)
                 update.append(tmp)
                 print('Here')
                 #update[i],update[i+1]=update[i+1], update[i]
                 break
             jmax=0
             for j,nextpage in enumerate(update[i+1:]):
                 if nextpage not in followers:
                 	if (j>jmax): jmax=j
                 	# update[i],update[i+1]=update[i+1], update[i]
             #print(update)
             if jmax>0:
             	tmp=update.pop(i)
             	update.insert(i+1+jmax,tmp)
         if isRightOrder(update): 
             print('success')
             break
         if count>100:
             print("count exceeded")
             print(update)
             break
     #print(update)
     fixed.append(update)


 #print(fixed)
total=0
for update in fixed:
    total+=update[len(update)//2]

print("Part 2 is", total)
#91, 55, 32, 25, 77

#print(91, rulesdict[91])
#print(55, rulesdict[55])
#print(32, rulesdict[32])
#print(25, rulesdict[25])
#print(77, rulesdict[77])

#91 [71, 63, 77, 49, 57, 51, 53, 33, 38, 82, 93, 62, 32, 41, 15, 22, 97, 21, 54, 17, 72, 95, 67, 19]
#55 [49, 82, 72, 33, 15, 93, 12, 38, 22, 89, 58, 21, 62, 67, 19, 97, 91, 17, 32, 25, 57, 63, 77, 53]
#32 [24, 21, 93, 62, 51, 72, 41, 71, 19, 95, 17, 53, 57, 65, 37, 67, 38, 44, 97, 13, 31, 79, 54, 22]
#25 [57, 32, 62, 63, 33, 77, 71, 19, 91, 21, 38, 72, 97, 93, 95, 12, 15, 82, 54, 53, 22, 67, 49, 17]
#77 [19, 79, 31, 22, 21, 67, 97, 62, 54, 82, 32, 51, 71, 53, 44, 95, 38, 57, 41, 24, 13, 93, 72, 17]

#update=[91, 55, 32, 25, 77]
#count=0
#while True:
#    count+=1
#    for i in range(len(update)-1):
#        page=update[i]
#        #print(page)
#        if page in rulesdict.keys():
#            followers=rulesdict[page]
#         #   print('a')
#        else:
#            update[i],update[i+1]=update[i+1], update[i]
#           # print('b')
#            break
#        for nextpage in update[i+1:]:
#            if nextpage not in followers: 
#             #   print(update,i,i+1)

#                update[i],update[i+1]=update[i+1], update[i]
#             #3   print('c')
#       # print('end',update)
#    if isRightOrder(update): break
#    if count>100:
#        #print("count exceeded")
#        #print(update)
#        break