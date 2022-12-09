fname="day7_example.txt"
fname="input_day7.txt"
with open(fname) as fp: data = fp.read().splitlines()


children=dict()
sizes=dict()
alldirs=[]
totals=dict()

prevdirectory=''
currentdirectory=''

for row in data:
    if row[:4]=='$ cd':
        if row.split(' ')[2]=='/': #back to home
            currentdirectory='/'
        elif row.split(' ')[2]=='..': #go up a directory level
            updir=''
            for folder in currentdirectory.split('/')[:-1]:
                updir+=folder+'/'
            currentdirectory=updir[:-1]
            if currentdirectory=='': currentdirectory='/'
        else:
            if currentdirectory == '/':
                currentdirectory += row.split(' ')[2] 
            else: 
                currentdirectory +='/'+row.split(' ')[2]

        alldirs.append(currentdirectory)
       
    elif row[:3]=='dir':
        if currentdirectory not in children.keys():
            if currentdirectory=='/':
                children[currentdirectory]=[currentdirectory+row.split(' ')[1]]
            else:
                children[currentdirectory]=[currentdirectory+'/'+row.split(' ')[1]]
        else:
            if type(children[currentdirectory])==str:
                if currentdirectory=='/':
                    children[currentdirectory]=[children[currentdirectory],currentdirectory+row.split(' ')[1]]
                else:
                    children[currentdirectory]=[children[currentdirectory],currentdirectory+'/'+row.split(' ')[1]]
            elif type(children[currentdirectory])==list:
                if currentdirectory=='/':
                    children[currentdirectory]=[*children[currentdirectory],currentdirectory+row.split(' ')[1]]
                else:
                    children[currentdirectory]=[*children[currentdirectory],currentdirectory+'/'+row.split(' ')[1]]
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
            totalsize+=sumsizes(childkey)
    return totalsize


for a in alldirs: totals[a]=sumsizes(a)
        
sol=0    
for a in totals.values():
    if a<=100000: sol+=a

totalsize=70000000
sizeneeded=30000000

unused=totalsize-totals['/']

sizetoclear=sizeneeded-unused

size=totalsize
for cand in totals.keys():
    if totals[cand]>=sizetoclear:
        if totals[cand]<size:
            size=totals[cand]
            dirtoclear=cand
        
print('Part 1 solution is', sol)
print('Part 2 solution is', size)
