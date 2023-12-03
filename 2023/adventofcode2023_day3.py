fname='input_day3.txt'
#fname='example_day3.txt'
with open(fname) as fp: data = fp.read().splitlines()

def findsymlocs(symbols):
    symlocs=[]
    for i in range(len(data)):
        for j in range(len(data[0])):
            if data[i][j] in symbols:
                symlocs.append((i,j))
    return symlocs
                
def findnumlocs():
    numlocs=[]
    for i in range(len(data)):
        for j in range(len(data[0])):               
            if data[i][j].isnumeric():
                numlocs.append((i,j,data[i][j]))
    return numlocs

def setnumberranges(numlocs):
    ndict={} 
    temp=''         
    for n in range(len(numlocs)):
        if n+1<len(numlocs) and numlocs[n][0]==numlocs[n+1][0] and numlocs[n+1][1]-numlocs[n][1]==1:
            temp=temp+numlocs[n][2]
        else:
            temp=temp+numlocs[n][2]
            ndict[((numlocs[n][0],numlocs[n][1]-len(temp)+1),(numlocs[n][0],numlocs[n][1]))]=[int(temp)]
            temp=''
    return ndict


syms='!@#$%^&*()-+/?<>\=|_~'

symlocs=findsymlocs(syms)
numlocs=findnumlocs()
ndict=setnumberranges(numlocs)
         
symplus=[]
for pair in symlocs:
    symplus.append((pair[0]-1,pair[1]-1))
    symplus.append((pair[0]-1,pair[1]-0))
    symplus.append((pair[0]-1,pair[1]+1))
    symplus.append((pair[0]-0,pair[1]-1))
    symplus.append((pair[0]-0,pair[1]-0))
    symplus.append((pair[0]-0,pair[1]+1))
    symplus.append((pair[0]+1,pair[1]-1))
    symplus.append((pair[0]+1,pair[1]-0))
    symplus.append((pair[0]+1,pair[1]+1))
 
total=0

for n in ndict.keys():
    loc=[]
    for i in range(n[0][1],n[1][1]+1):
        loc.append((n[0][0],i))
    for l in loc:
        if l in symplus:
            total+=ndict[n][0]
            break
           
print('Part 1 solution', total)

symlocs=findsymlocs('*')

gears=[]
for pair in symlocs:
    symplus=[]
    symplus.append((pair[0]-1,pair[1]-1))
    symplus.append((pair[0]-1,pair[1]-0))
    symplus.append((pair[0]-1,pair[1]+1))
    symplus.append((pair[0]-0,pair[1]-1))
    symplus.append((pair[0]-0,pair[1]-0))
    symplus.append((pair[0]-0,pair[1]+1))
    symplus.append((pair[0]+1,pair[1]-1))
    symplus.append((pair[0]+1,pair[1]-0))
    symplus.append((pair[0]+1,pair[1]+1))
    temp=[]
    for n in ndict.keys():
        loc=[]
        for i in range(n[0][1],n[1][1]+1):
            loc.append((n[0][0],i))
        for l in loc:
            if l in symplus:
                temp.append(ndict[n][0])
                break
    gears.append(temp)

totgear=0
for gear in gears:
    if len(gear) == 2: totgear+=gear[0]*gear[1]

print('Part 2 solution', totgear)
