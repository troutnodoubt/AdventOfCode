import re
fname="day_22_example1.txt"
fname="day_22_example2.txt"
fname="day_22_example3.txt"
#fname="day_22_example4.txt"
#fname="input_day22.txt"
with open(fname) as fp: data = fp.read().splitlines()

def cubeintersect(cubeA,cubeB):
    xtest=cubeA[0]<=cubeB[1] and cubeA[1]>=cubeB[0]
    ytest=cubeA[2]<=cubeB[3] and cubeA[3]>=cubeB[2]
    if len(cubeA)==6 and len(cubeB)==6:
        ztest=cubeA[4]<=cubeB[5] and cubeA[5]>=cubeB[4]
    else:
        ztest=True
    return(all((xtest,ytest,ztest)))


def findvolume(cubeA):
    xwidth=cubeA[1]-cubeA[0]+1
    
    ywidth=cubeA[3]-cubeA[2]+1
    if len(cubeA)==6:
        zwidth=cubeA[5]-cubeA[4]+1
    else:
        zwidth=1
    # if xwidth==1: print('xwidth is 1')
    # if ywidth==1: print('ywidth is 1')
    # if zwidth==1: print('zwidth is 1')
    # if xwidth<0: print('negative xwidth')
    # if ywidth<0: print('negative ywidth')
    # if zwidth<0: print('negative zwidth')
    return(xwidth*ywidth*zwidth)


    
def findintersect(cubeA,cubeB):
    if cubeintersect(cubeA,cubeB):
        xs=max(cubeA[0],cubeB[0])
        xf=min(cubeA[1],cubeB[1])
        ys=max(cubeA[2],cubeB[2])
        yf=min(cubeA[3],cubeB[3])
        if len(cubeA)==4 and len(cubeB)==4:
            return((xs,xf,ys,yf))
        else:
            zs=max(cubeA[4],cubeB[4])
            zf=min(cubeA[5],cubeB[5])
            return((xs,xf,ys,yf,zs,zf))

def reducecubes(listofcubes,spawned=False): #reduces first in list by remainder of list
    if listofcubes:
        cubeA=listofcubes[0]
        volumeA=0
        if not spawned: volumeA=findvolume(cubeA)
        spawnedlist=list()
        # print('Reducing',cubeA,'start vol',volumeA,'spawned=',spawned)
        # if len(listofcubes)<2: print('nothing left to reduce for',cubeA)
        for cubeB in listofcubes[1:]:
           
            if cubeintersect(cubeA,cubeB):
                spawnedzone=findintersect(cubeA,cubeB)
                spawnedlist.append(spawnedzone)
                volumeA-=findvolume(spawnedzone)
                
                # print('intersection of',cubeA,cubeB,'is',spawnedzone,'with volume',findvolume(spawnedzone))
                # print('spawned list',spawnedlist)
                # print('subvolume after intersections',volumeA)
            # else: 
                # print('no intersection of',cubeA,cubeB)
                # print('spawned list',spawnedlist)
        # if reducecubes(spawnedlist,True):
        if spawnedlist:
            for i in range(len(spawnedlist)):
                # print('subvolume before spawn',volumeA)
                # print('Parsing spawns')
                volumeA-=reducecubes(spawnedlist[i:],True)
                # print('done parsing spawns')
        # else:
        #     print('no spawns to parse')
        # print('returned value for',cubeA,volumeA)
        return(volumeA)
    # else:
    #     print('no list provided to reduce')

p1=re.compile('-{0,1}[0-9]+')
p2=re.compile('on')


reactor=dict()
rowcount=0
for row in data:
    rowcount+=1
    #print('row',rowcount,'of',len(data),row)
    xs,xf,ys,yf,zs,zf=re.findall(p1,row)
    xs=int(xs)
    xf=int(xf)
    ys=int(ys)
    yf=int(yf)
    zs=int(zs)
    zf=int(zf)
    
    if re.search(p2,row): state=1 
    else: state=0
    # print(xs,xf,ys,yf,zs,zf,state)
    if xs>50 or xf<-50 or ys>50 or yf<-50 or zs>50 or zf<-50: continue
    for x in range(xs,xf+1):
        if abs(x)>50: continue
        if xs>50 or xf<-50: continue
        for y in range(ys,yf+1):
            if abs(y)>50: continue
            if ys>50 or yf<-50: continue
            for z in range(zs,zf+1):
                if abs(z)>50: continue
                if zs>50 or zf<-50: continue
                if (abs(x)<=50 and abs(y)<=50 and abs(z)<=50):
                    if state==1: 
                        reactor[(x,y,z)]=state 
                    else:
                        if (x,y,z) in reactor.keys(): del reactor[(x,y,z)]
                
print('Part 1 solution is',len(reactor))


cubelist=list()
statelist=list()
for row in data:
    cube=tuple([int(a) for a in re.findall(p1,row)])
    if re.search(p2,row):
        state=True
    else:
        state=False
    cubelist.append(cube)
    statelist.append(state)

totals=list()   
for i in range(len(cubelist)):
    if statelist[i]:
        a=reducecubes(cubelist[i:])
        totals.append(a)
        #print(cubelist[i],a)
    

print('Part 2 solution is',sum(totals))