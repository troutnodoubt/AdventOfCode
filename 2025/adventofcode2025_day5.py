fname='input_day5.txt'
# fname='example_day5.txt'

# from math import inf

with open(fname) as fp: data = fp.read().splitlines()
ranges=[]
ingredients=[]
# fresh=set()
nfresh=0
# maxfresh=0
# minfresh=float('inf')
combinedranges=[[0,0]]
for entry in data:
    # print(entry)
    if '-' in entry:
        start=int(entry.split('-')[0])
        stop=int(entry.split('-')[1])
        # ranges.append((int(entry.split('-')[0]),int(entry.split('-')[1])+1))
        ranges.append([start,stop])
        combine=False
        for combined in combinedranges:
            # print(combined,start,stop)
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
            
        # print(combinedranges)
        # if int(entry.split('-')[0])<minfresh: minfresh=int(entry.split('-')[0])
        # if int(entry.split('-')[1])>maxfresh: maxfresh=int(entry.split('-')[1])
    else:
        if len(entry) >0: 
            ingredients.append(int(entry))

# print(minfresh)
# print(maxfresh)
for ingredient in ingredients:
    for rnge in ranges:
        if ingredient >= rnge[0] and ingredient<=rnge[1]:
            nfresh+=1
            break

print('Part 1 solution', nfresh)


combinedranges.pop(0)
itercount=0
while True:
    tmp=set()
    # print(combinedranges)
    # print(tmp)
    for combined1 in combinedranges:
        overlapcnt=0
        for combined2 in combinedranges:
            overlap=combined1[0] <= combined2[1] and combined2[0] <= combined1[1] and combined1!=combined2
            # print(overlap)
            if overlap:
                tmp.add((min(combined1[0],combined2[0]),max(combined1[1],combined2[1])))
                overlapcnt+=1
            # print(combined1)
            # print(combined2)
            # print(tmp)
            # print()
        if overlapcnt==0:
            tmp.add(tuple(combined1))
            # print('ddd',combined1)
    print(len(tmp))
    itercount+=1
    if combinedranges==[a for a in tmp] or itercount==4:
        print(combinedranges)
        print(tmp)
        break
    combinedranges=[]
    combinedranges=[a for a in tmp]
    
#print(combinedranges)
total2=0
for rng in combinedranges:
    total2+=rng[1]-rng[0]+1

# nfresh=0
# ingredient=minfresh
# while ingredient <= maxfresh:
#     for rnge in ranges:
#         if ingredient >= rnge[0] and ingredient<=rnge[1]:
#             nfresh+=1
#             break
#     ingredient+=1

print('Part 2 solution', total2)


