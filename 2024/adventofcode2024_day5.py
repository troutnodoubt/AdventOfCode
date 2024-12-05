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
        produced.append(list(int(a) for a in row.split(',') if a != ''))

produced=produced[1:]

for rule in rules:
    if rule[0] not in rulesdict.keys(): rulesdict[rule[0]]=[rule[1]]
    else: rulesdict[rule[0]].append(rule[1])

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
                break
            jmax=0
            jchanged=False
            for j,nextpage in enumerate(update[i+1:]):
               if nextpage not in followers:
                   jchanged=True
                   if (j>jmax): jmax=j
            if jchanged:
            	tmp=update.pop(i)
            	update.insert(i+1+jmax,tmp)
        if isRightOrder(update): 
            #print('success')
            break
        if count>100:
            #print("count exceeded")
            #print(update)
            break
    fixed.append(update)

total=0
for update in fixed:
    total+=update[len(update)//2]

print("Part 2 is", total)
