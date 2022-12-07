
fname="C://Users/Mark/Documents/Advent of Code/2021/day_12_example.txt"
#fname="C://Users/Mark/Documents/Advent of Code/2021/input_day12.txt"
with open(fname) as fp: data = fp.read().splitlines()

cavemap=dict()
a=[row.split('-') for row in data]
reverses=list()


for row in a:
    #print(row)
    if all(l.isupper() for l in row[0]) or all(l.isupper() for l in row[1]):
        if row[0]!='start' and row[1]!='end':
            reverses.append([row[1],row[0]])
        
for row in reverses:
    #print(row)
    a.append(row)

startidx=[i for i, entry in enumerate(a) if entry[0]=='start']
currentcave='start'
pathstring=''
allpaths=list()
for entry in startidx:
    currentcave='start'
    pathstring=''
    nextcave=a[entry][1]
    pathstring=pathstring+currentcave+','+nextcave
    currentcave=nextcave
    while currentcave!='end':
        caveidx=[i for i, entry in enumerate(a) if entry[0]==currentcave]
        for cave in caveidx:
            nextcave=a[cave][1]
            pathstring=pathstring+','+nextcave
            currentcave=nextcave
    allpaths.append(pathstring)
    
            

