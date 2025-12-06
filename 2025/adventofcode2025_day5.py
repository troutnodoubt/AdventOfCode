fname='input_day5.txt'
# fname='example_day5.txt'

with open(fname) as fp: data = fp.read().splitlines()
ranges=[]
ingredients=[]
nfresh=0
combinedranges=[[0,0]]
for entry in data:
    if '-' in entry:
        start=int(entry.split('-')[0])
        stop=int(entry.split('-')[1])
        ranges.append([start,stop])
        combine=False
        for combined in combinedranges:
            if start>=combined[0] and start<=combined[1]:
                if stop>combined[1]:
                    combined[1]=stop
                    combine=True
            elif stop>=combined[0] and stop<=combined[1]:
                if start<combined[0]:
                    combined[0]=start
                    combine=True
        if not combine: 
            combinedranges.append([start,stop])
    else:
        if len(entry) >0: 
            ingredients.append(int(entry))

for ingredient in ingredients:
    for rnge in ranges:
        if ingredient >= rnge[0] and ingredient<=rnge[1]:
            nfresh+=1
            break

print('Part 1 solution', nfresh)


combinedranges.pop(0)
itercount=0
prevlength=0
while True:
    tmp=set()
    for combined1 in combinedranges:
        overlapcnt=0
        for combined2 in combinedranges:
            overlap=combined1[0] <= combined2[1] and combined2[0] <= combined1[1] and combined1!=combined2
            if overlap:
                tmp.add((min(combined1[0],combined2[0]),max(combined1[1],combined2[1])))
                overlapcnt+=1
        if overlapcnt==0:
            tmp.add(tuple(combined1))
    itercount+=1
    if prevlength==len(tmp):
        break
    combinedranges=[]
    combinedranges=[a for a in tmp]
    prevlength=len(tmp)
    
total2=0
for rng in combinedranges:
    total2+=rng[1]-rng[0]+1

print('Part 2 solution', total2)
