
fname='input_day22.txt'
# fname='example_day22.txt'
with open(fname) as fp: data = fp.read().splitlines()

class Block:
    def __init__(self, v1, v2):
        self.v1 = v1
        self.v2 = v2
        self.xrange=range(min(self.v1[0],self.v2[0]),max(self.v1[0],self.v2[0])+1)
        self.yrange=range(min(self.v1[1],self.v2[1]),max(self.v1[1],self.v2[1])+1)
        self.zrange=range(min(self.v1[2],self.v2[2]),max(self.v1[2],self.v2[2])+1)
        self.zrangefall=range(min(self.v1[2],self.v2[2])-1,max(self.v1[2],self.v2[2])+1-1)
        self.fixed=False
        self.supportedby=[]
        self.supporting=[]
        
    def fall(self):
        if self.v1[2] > 1 and self.v2[2]>1:
            self.v1[2]-=1
            self.v2[2]-=1
            self.xrange=range(min(self.v1[0],self.v2[0]),max(self.v1[0],self.v2[0])+1)
            self.yrange=range(min(self.v1[1],self.v2[1]),max(self.v1[1],self.v2[1])+1)
            self.zrange=range(min(self.v1[2],self.v2[2]),max(self.v1[2],self.v2[2])+1)
            self.zrangefall=range(min(self.v1[2],self.v2[2])-1,max(self.v1[2],self.v2[2])+1-1)
               
        else:
            self.fixed=True
    
    def addSupportedBy(self,idx):
        self.supportedby.append(idx)
        
    def addSupporting(self,idx):
        self.supporting.append(idx)

def findCollisions(a, b): # Will a hit b if a falls by one unit?
    collision=False
    xcollide=len(range(max(a.xrange[0],b.xrange[0]),min(a.xrange[-1],b.xrange[-1])+1))>0
    ycollide=len(range(max(a.yrange[0],b.yrange[0]),min(a.yrange[-1],b.yrange[-1])+1))>0
    zcollide=len(range(max(a.zrangefall[0],b.zrange[0]),min(a.zrangefall[-1],b.zrange[-1])+1))>0
    if xcollide and ycollide and zcollide: collision=True
    return collision
    

blocks={}
for i,line in enumerate(data):
    blocks[i]=Block([int(x) for x in line.split('~')[0].split(',')],[int(x) for x in line.split('~')[1].split(',')])
    
roomtofall=True
while roomtofall:
    fallcount=0
    for blocka in blocks.keys():
        collisions=[]
        for blockb in blocks.keys():
            if blockb != blocka:
                collisions.append(findCollisions(blocks[blocka], blocks[blockb]))
        if not any(collisions) and not blocks[blocka].fixed:
            blocks[blocka].fall()
            fallcount+=1
    print(fallcount) # Gives an indication of how much longer needed to wait
    if fallcount==0: roomtofall=False

for blocka in blocks.keys():
    for blockb in blocks.keys():
        if blockb != blocka:
            if findCollisions(blocks[blocka], blocks[blockb]):
                blocks[blocka].addSupportedBy(blockb)
                blocks[blockb].addSupporting(blocka)
                
nremovable=0
for blocka in blocks.keys():
    oktoremove=[]
    for supporting in blocks[blocka].supporting:
        if (len(blocks[supporting].supportedby))>1: 
            oktoremove.append(True)
        else:
            oktoremove.append(False)
    if all(oktoremove): 
        nremovable+=1

print('Part 1 solution', nremovable)

def findNFall(a):
    templist=[]
    for block in a.supporting:
        removed=[]
        for support in blocks[block].supportedby:
            if support in falllist: 
                removed.append(True)
            else:
                removed.append(False)
        if all(removed):
            falllist.append(block)
            templist.append(block)
    for block in templist:
        findNFall(blocks[block])

totalfall=0

for blocka in blocks.keys():
    falllist=[blocka]
    
    findNFall(blocks[blocka])
    totalfall+=len(set(falllist))-1

print('Part 2 solution', totalfall)

# slow as dirt but it works. Could really optimize the falling part
# to only check relevant pieces and to advance more than one step at
# a time. Class could be cleaned up as well to not have duplicate math functions in different methods.
