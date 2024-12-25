
fname='input_day25.txt'
# fname='example_day25.txt'
with open(fname) as fp: data = fp.read().splitlines()
data.append('')

tmp=[]
tmp2=[]
for row in data:
    if row!='':
        tmp2.append(row)
    elif row=='':
        tmp.append(tmp2)
        tmp2=[]
        
locks=set()
keys=set()

for item in tmp:
    tmp2=[]
    if item[0]=='#####' and item[-1]=='.....': #lock
        a=zip(*reversed(item))
        for b in a:
            tmp2.append(b.count('#')-1)
        locks.add(tuple(tmp2))
    elif item[0]=='.....' and item[-1]=='#####': #key
        a=zip(*reversed(item))
        for b in a:
            tmp2.append(b.count('#')-1)
        keys.add(tuple(tmp2))

fitcount=0
for key in keys:
    for lock in locks:
        fit=[]
        for pin in range(5):
            if key[pin]+lock[pin]<=5: fit.append(True)
            else: fit.append(False)
        if all(fit): fitcount+=1

print('Part 1', fitcount)
