
fname='/home/mark/Documents/git/AdventOfCode/2025/input_day8.txt'
# fname='/home/mark/Documents/git/AdventOfCode/2025/example_day8.txt'
if 'example' in fname:
    tocount=10
else:
    tocount=1000

def distancesquared(box1,box2):
    x1=int(box1.split(',')[0])
    y1=int(box1.split(',')[1])
    z1=int(box1.split(',')[2])
    x2=int(box2.split(',')[0])
    y2=int(box2.split(',')[1])
    z2=int(box2.split(',')[2])
    return (x2-x1)*(x2-x1)+(y2-y1)*(y2-y1)+(z2-z1)*(z2-z1)

with open(fname) as fp: data = fp.read().splitlines()

'''
Create a dictionary of junction boxes, the key being the distance and the
values being the pair of boxes.

Create a list of sets, the sets are the connected junction boxes.
Will have to iterate through the list of sets each time, might not be 
the most efficient but shouldn't be too bad.

Add to the set in sorted order of the dictionary distance keys.
'''

ddict={}
for a in data:
    for b in data:
        if a!=b:
            d=distancesquared(a,b)
            ddict[d]=[a,b]

distances=[a for a in ddict.keys()]
distances.sort()

groups=[]
for i,d in enumerate(distances):
    found=False
    modified=[]
    tempset=set()
    for s in groups: 
        if ddict[d][0] in s:
            s.add(ddict[d][1])
            found=True
            modified.append(s)
        elif ddict[d][1] in s:
            s.add(ddict[d][0])
            found=True
            modified.append(s)
    if len(modified)>1:
        for a in modified: 
            groups.remove(a)
            for b in a:
                tempset.add(b)
        groups.append(tempset)   
    if not found: 
        temp=set()
        temp.add(ddict[d][1])
        temp.add(ddict[d][0])
        groups.append(temp)
    if i==tocount-1:
        break

lengths=[]
for s1 in groups:
    lengths.append(len(s1))

lengths.sort(reverse=True)
sol=1
for i in range(3):
    sol*=lengths[i]

print('Part 1 solution',sol)

groups=[]
last=[]
for i,d in enumerate(distances):
    found=False
    modified=[]
    tempset=set()
    for s in groups: 
        if ddict[d][0] in s:
            s.add(ddict[d][1])
            found=True
            modified.append(s)
        elif ddict[d][1] in s:
            s.add(ddict[d][0])
            found=True
            modified.append(s)
    if len(modified)>1:
        for a in modified: 
            groups.remove(a)
            for b in a:
                tempset.add(b)
        groups.append(tempset)   
    if not found: 
        temp=set()
        temp.add(ddict[d][1])
        temp.add(ddict[d][0])
        groups.append(temp)
    foundlist=[a in groups[0] for a in data]
    if i>tocount and len(groups)==1 and all(foundlist):
        last=ddict[d]
        break

x1=int(last[0].split(',')[0])
x2=int(last[1].split(',')[0])
print('Part 2 solution',x1*x2)