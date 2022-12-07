fname="day7_example.txt"
fname="input_day7.txt"
with open(fname) as fp: data = fp.read().splitlines()


children=dict()
sizes=dict()
alldirs=[]
totals=dict()

for row in data:
    if row[:4]=='$ cd':
        currentdirectory=row.split(' ')[2]
        #print(currentdirectory)
        if currentdirectory=='/': currentdirectory='home'
        if currentdirectory != '..': alldirs.append(currentdirectory)
    elif row[:3]=='dir':
        if currentdirectory not in children.keys():
            children[currentdirectory]=[row.split(' ')[1]]
        else:
            if type(children[currentdirectory])==str:
                children[currentdirectory]=[children[currentdirectory],row.split(' ')[1]]
            elif type(children[currentdirectory])==list:
                children[currentdirectory]=[*children[currentdirectory],row.split(' ')[1]]
    elif row[:4] != "$ ls":
        if currentdirectory not in sizes.keys():
            sizes[currentdirectory]=int(row.split(' ')[0])
        else:
            sizes[currentdirectory]=sizes[currentdirectory]+int(row.split(' ')[0])

def sumsizes(keyname):
    if keyname in sizes.keys():
        totalsize=sizes[keyname]
    else:
        totalsize=0
    if keyname in children.keys():
        for childkey in children[keyname]:
            #print(keyname,childkey)
            # sumsizes(childkey)<=100000:
            totalsize+=min(sumsizes(childkey),100001)
            print(keyname,totalsize)
            #else: 
            #    break
    if totalsize<=100000:
        return totalsize
    else:
        return 100001


for a in children.keys():
    if a in children[a]: print(a)    
        
# print(sumsizes('home'))
# print(sumsizes('a'))
# print(sumsizes('e'))
# print(sumsizes('d'))

# for a in alldirs:
#     if a in sizes.keys():
#         if sizes[a]<=100000:
#             totals[a]=sumsizes(a)
#     else:
#         totals[a]=sumsizes(a)
        
# sol=0    
# for a in totals.values():
#     if a<=100000: sol+=a
    

        
#print('Part 1 solution is', sol)
# print('Part 2 solution is')
