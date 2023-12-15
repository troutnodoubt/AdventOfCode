import re

fname='input_day15.txt'
#fname='example_day15.txt'

with open(fname) as fp: data = fp.read().splitlines()

def HASH(s):
    currentval=0
    for c in s:
        currentval+=ord(c)
        currentval*=17
        currentval%=256
    return currentval

def focusPower(boxnum,lenses):
    power=0
    for pos,lens in enumerate(lenses):
        power+=(pos+1)*int(lens[1])
    return power*(boxnum+1)

total=0
lensbox={i:[] for i in range(256)}
for s in data[0].split(','):
    total+=HASH(s)
    label=re.match('[a-z]*',s).group(0)
    boxnumber=HASH(label)
    lensloc=[i for i,s in enumerate(lensbox[boxnumber]) if s[0]==label]
    if '=' in s:
        focallength=s[-1]
        if len(lensloc)>0:
            lensbox[boxnumber].pop(lensloc[0])
            lensbox[boxnumber].insert(lensloc[0],(label,focallength))
        else:    
            lensbox[boxnumber].append((label, focallength))
    elif '-' in s:
        if len(lensloc)>0: lensbox[boxnumber].pop(lensloc[0])

totalpower=0        
for key in lensbox.keys():
    if len(lensbox[key])>0: totalpower+=focusPower(key,lensbox[key])

print('Part 1 solution is', total)
print('Part 2 solution is', totalpower)   
    