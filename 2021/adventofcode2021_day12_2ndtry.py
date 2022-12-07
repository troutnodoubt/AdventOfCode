#from collections import defaultdict
fname="C://Users/Mark/Documents/Advent of Code/2021/day_12_example.txt"
fname="C://Users/Mark/Documents/Advent of Code/2021/input_day12.txt"
with open(fname) as fp: data = fp.read().splitlines()


cavemap=dict()
a=[row.split('-') for row in data]
reverses=list()

# paths = defaultdict(list)

# for row in data:
#     one,two = row.split('-')
#     paths[one].append(two)
#     paths[two].append(one)


for row in a:
    #print(row)
    reverses.append([row[1],row[0]])
    # if all(l.isupper() for l in row[0]) or all(l.isupper() for l in row[1]):
    #     if row[0]!='start' and row[1]!='end':
    #         reverses.append([row[1],row[0]])
        
for row in reverses:
    #print(row)
    a.append(row)

cavemap=dict(a)
#print(cavemap)
for entry in cavemap.keys():
    newvalue=list()
    #print(entry)
    for row in a:
        if row[0]==entry:
            newvalue.append(row[1])
    #print(newvalue)
    cavemap[entry]=newvalue

def findpath(position,pastpath,dblvisit,smallcave):
    #print(position)
    if position=='start' and len(pastpath)!=0:
        #print('returned to start, nothing happens')
        #print(position,'\n',pastpath)
        return 0
        
    if position=='end':
        #print('found a possible path')
        #print(position,'\n',pastpath)
        return 1
        
    if position.islower() and position in pastpath and not dblvisit:
        #print(position,'\n',pastpath)
        #print('returned to previous lower case cave, nothing happens')
        return 0
    elif position.islower() and position in pastpath and dblvisit:
        if smallcave=='':
            smallcave=position
        else:
            return 0
        
     
    #print('\n',pastpath)
    #print(position)
    
    
    pastpath=pastpath|{position}
    #print(pastpath,'\n')
    
    #print('in main loop, path is',pastpath)
    #print('in main loop, position is',position)
    possiblepaths=0
    #print(possiblepaths)
    
    
    for route in cavemap[position]:
        #print('in recursion, current cave is',route)
        #print('in recursion, past visited is',pastpath)
        possiblepaths+=findpath(route,pastpath,dblvisit,smallcave)
    #print(possiblepaths)
    return possiblepaths

part1=findpath('start',set(),False,'')
part2=findpath('start',set(),True,'')
print('Part 1 solution is',part1)
print('Part 2 solution is',part2)
    
    


            

