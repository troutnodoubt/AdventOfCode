import re

fname='input_day14.txt'
# fname='example_day14.txt'

with open(fname) as fp: data = fp.read().splitlines()

if 'example' in fname:
    width=11
    height=7
else:
    width=101 
    height=103

def solve(time):

    finalpos=[]

    for row in data:
        a=[int(a) for a in re.findall('-?\d+',row)]
        finalpos.append([(a[1]+time*a[3])%height, (a[0]+time*a[2])%width])
    Qcounts=[0,0,0,0]
    halfwidth=width//2
    halfheight=height//2

    for pos in finalpos:
        if   pos[1] in (range(halfwidth))         and pos[0] in range(halfheight): Qcounts[0]+=1    
        elif pos[1] in (range(halfwidth+1,width)) and pos[0] in range(halfheight): Qcounts[1]+=1
        elif pos[1] in (range(halfwidth))         and pos[0] in range(halfheight+1,height): Qcounts[2]+=1
        elif pos[1] in (range(halfwidth+1,width)) and pos[0] in range(halfheight+1,height): Qcounts[3]+=1
   
    return Qcounts,finalpos

Qcounts,finalpos=solve(100)
print('Part 1',Qcounts[0]*Qcounts[1]*Qcounts[2]*Qcounts[3])
danger=Qcounts[0]*Qcounts[1]*Qcounts[2]*Qcounts[3]


treeFound=False
time=0
while not treeFound:
    Qcounts,finalpos=solve(time)
    rowmatch=[]
    centers=0
    if danger>Qcounts[0]*Qcounts[1]*Qcounts[2]*Qcounts[3]:
        danger=Qcounts[0]*Qcounts[1]*Qcounts[2]*Qcounts[3]
        plot=[[0 for a in range(width)] for row in range(height)]
        for pos in finalpos:
            plot[pos[0]][pos[1]]+=1
        adjacentcount=0
        for row in plot:
            if '111111111' in "".join(str(c) for c in row): adjacentcount+=1
        if adjacentcount>3:
            treeFound=True
            print(time)
            print()
            for row in plot: 
                print("".join(str(c) for c in row))
            print()
          
    if treeFound: print('Part 2', time) #1649 is too low, 885904 too high
    else: time+=1
    if time>10000: break

