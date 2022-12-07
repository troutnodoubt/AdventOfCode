#from collections import defaultdict
import numpy as np
# from numpy import Inf
fname="C://Users/Mark/Documents/Advent of Code/2021/day_19_example.txt"
#fname="C://Users/Mark/Documents/Advent of Code/2021/input_day15.txt"
with open(fname) as fp: data = fp.read().splitlines()


# 1   0   0   
# 0   1   0 x,y,z->x,y,z  1
# 0   0   1 

# 0   1   0
# 0   0   1 x,y,z->y,z,x  2
# 1   0   0

# 0   0   1
# 1   0   0 x,y,z->z,x,y  3
# 0   1   0

# -1   0   0   
#  0   1   0 x,y,z->-x,y,z 4
#  0   0   1 

# 0   -1   0
# 0    0   1 x,y,z->-y,z,x 5
# 1    0   0

# 0   0   -1
# 1   0    0 x,y,z->-z,x,y 6
# 0   1    0

# 1    0   0   
# 0   -1   0 x,y,z->x,-y,z 7
# 0    0   1 

# 0   1    0
# 0   0   -1 x,y,z->y,-z,x 8
# 1   0    0

#  0   0   1
# -1   0   0 x,y,z->z,-x,y 9
#  0   1   0

# 1    0   0   
# 0    1   0 x,y,z->x,y,-z 10
# 0    0  -1 

#  0   1    0
#  0   0    1 x,y,z->y,z,-x 11
# -1   0    0

#  0   0   1
#  1   0   0 x,y,z->z,x,-y 12
#  0  -1   0


# -1    0    0   
#  0   -1    0 x,y,z->-x,-y,z 13 
#  0    0    1 

# 0   -1    0
# 0    0   -1 x,y,z->-y,-z,x 14
# 1    0    0

#  0   0  -1
# -1   0   0 x,y,z->-z,-x,y 15
#  0   1   0

# -1    0    0   
#  0    1    0 x,y,z->-x,y,-z 16
#  0    0   -1 

#  0   -1   0
#  0    0   1 x,y,z->-y,z,-x 17
# -1    0   0

#  0   0  -1
#  1   0   0 x,y,z->-z,x,-y 18
#  0  -1   0


#  1    0    0   
#  0   -1    0 x,y,z->x,-y,-z 19
#  0    0   -1 

#  0    1   0
#  0    0  -1 x,y,z->y,-z,-x 20
# -1    0   0

#  0   0   1
# -1   0   0 x,y,z->z,-x,-y 21
#  0  -1   0

# -1    0    0   
#  0   -1    0 x,y,z->-x,-y,-z 22
#  0    0   -1 

#  0   -1   0
#  0    0  -1 x,y,z->-y,-z,-x 23
# -1    0   0

#  0   0  -1
# -1   0   0 x,y,z->-z,-x,-y 24
#  0  -1   0



def findbeacons(scanner1,scanner2):
    xxdelta=list()
    xydelta=list()
    xzdelta=list()
    yydelta=list()
    yzdelta=list()
    zzdelta=list()
    yxdelta=list()
    zxdelta=list()
    zydelta=list()
    rotation=[[0 for _ in range(4)] for _ in range(4)]
    # for rowidx1 in range(len(scandata[0])):
        # for rowidx2 in range(len(scandata[1])):
    for rowidx1 in range(len(scanner1)):
        for rowidx2 in range(len(scanner2)):
            xxdelta.append([scanner2[rowidx2][0]+scanner1[rowidx1][0],scanner2[rowidx2][0]*1-scanner1[rowidx1][0]])
            yydelta.append([scanner2[rowidx2][1]+scanner1[rowidx1][1],scanner2[rowidx2][1]*1-scanner1[rowidx1][1]])
            zzdelta.append([scanner2[rowidx2][2]+scanner1[rowidx1][2],scanner2[rowidx2][2]*1-scanner1[rowidx1][2]])
            xydelta.append([scanner2[rowidx2][0]+scanner1[rowidx1][1],scanner2[rowidx2][0]*1-scanner1[rowidx1][1]])
            xzdelta.append([scanner2[rowidx2][0]+scanner1[rowidx1][2],scanner2[rowidx2][0]*1-scanner1[rowidx1][2]])    
            yzdelta.append([scanner2[rowidx2][1]+scanner1[rowidx1][2],scanner2[rowidx2][1]*1-scanner1[rowidx1][2]])
            yxdelta.append([scanner1[rowidx1][0]+scanner2[rowidx2][1],scanner1[rowidx1][0]*1-scanner2[rowidx2][1]])
            zxdelta.append([scanner1[rowidx1][0]+scanner2[rowidx2][2],scanner1[rowidx1][0]*1-scanner2[rowidx2][2]])    
            zydelta.append([scanner1[rowidx1][1]+scanner2[rowidx2][2],scanner1[rowidx1][1]*1-scanner2[rowidx2][2]])
    
    xx1,offsetxx1,xx2,offsetxx2=getcounts(xxdelta)
    xy1,offsetxy1,xy2,offsetxy2=getcounts(xydelta)
    xz1,offsetxz1,xz2,offsetxz2=getcounts(xzdelta)
    yy1,offsetyy1,yy2,offsetyy2=getcounts(yydelta)
    yz1,offsetyz1,yz2,offsetyz2=getcounts(yzdelta)
    zz1,offsetzz1,zz2,offsetzz2=getcounts(zzdelta)
    yx1,offsetyx1,yx2,offsetyx2=getcounts(yxdelta)
    zx1,offsetzx1,zx2,offsetzx2=getcounts(zxdelta)
    zy1,offsetzy1,zy2,offsetzy2=getcounts(zydelta)
    
    # print(xx1,offsetxx1,xx2,offsetxx2)
    # print(xy1,offsetxy1,xy2,offsetxy2)
    # print(xz1,offsetxz1,xz2,offsetxz2)
    # print(yy1,offsetyy1,yy2,offsetyy2)
    # print(yz1,offsetyz1,yz2,offsetyz2)
    # print(zz1,offsetzz1,zz2,offsetzz2)
    # print(yx1,offsetyx1,yx2,offsetyx2)
    # print(zx1,offsetzx1,zx2,offsetzx2)
    # print(zy1,offsetzy1,zy2,offsetzy2)
    candidates1=list()
    candidates2=list()
    
    if xx1>=12: 
        rotation[0][0]=-1
        rotation[0][3]=offsetxx1
    if xx2>=12: 
        rotation[0][0]=1
        rotation[0][3]=offsetxx2
    if xy1>=12: 
        rotation[0][1]=-1
        rotation[0][3]=offsetxy1
    if xy2>=12: 
        rotation[0][1]=1
        rotation[0][3]=offsetxy2
    if xz1>=12: 
        rotation[0][2]=-1
        rotation[0][3]=offsetxz1
    if xz2>=12: 
        rotation[0][2]=1
        rotation[0][3]=offsetxz2
    if yx1>=12: 
        rotation[1][0]=-1
        rotation[1][3]=offsetyx1
    if yx2>=12: 
        rotation[1][0]=1
        rotation[1][3]=offsetyx2
    if yy1>=12: 
        rotation[1][1]=-1
        rotation[1][3]=offsetyy1
    if yy2>=12: 
        rotation[1][1]=1
        rotation[1][3]=offsetyy2
    if yz1>=12: 
        rotation[1][2]=-1
        rotation[1][3]=offsetyz1
    if yz2>=12: 
        rotation[1][2]=1
        rotation[1][3]=offsetyz2
    if zx1>=12: 
        rotation[2][0]=-1
        rotation[2][3]=offsetzx1
    if zx2>=12: 
        rotation[2][0]=1
        rotation[2][3]=offsetzx2
    if zy1>=12: 
        rotation[2][1]=-1
        rotation[2][3]=offsetzy1
    if zy2>=12: 
        rotation[2][1]=1
        rotation[2][3]=offsetzy2
    if zz1>=12: 
        rotation[2][2]=-1
        rotation[2][3]=offsetzz1
    if zz2>=12: 
        rotation[2][2]=1
        rotation[2][3]=offsetzz2
    rotation[3][3]=1
    
    
    for rowidx1 in range(len(scanner1)):
        for rowidx2 in range(len(scanner2)):
            xx=[scanner2[rowidx2][0]+scanner1[rowidx1][0],scanner2[rowidx2][0]*1-scanner1[rowidx1][0]]
            yy=[scanner2[rowidx2][1]+scanner1[rowidx1][1],scanner2[rowidx2][1]*1-scanner1[rowidx1][1]]
            zz=[scanner2[rowidx2][2]+scanner1[rowidx1][2],scanner2[rowidx2][2]*1-scanner1[rowidx1][2]]
            xy=[scanner2[rowidx2][0]+scanner1[rowidx1][1],scanner2[rowidx2][0]*1-scanner1[rowidx1][1]]
            xz=[scanner2[rowidx2][0]+scanner1[rowidx1][2],scanner2[rowidx2][0]*1-scanner1[rowidx1][2]]    
            yz=[scanner2[rowidx2][1]+scanner1[rowidx1][2],scanner2[rowidx2][1]*1-scanner1[rowidx1][2]]
            yx=[scanner1[rowidx1][0]+scanner2[rowidx2][1],scanner1[rowidx1][0]*1-scanner2[rowidx2][1]]
            zx=[scanner1[rowidx1][0]+scanner2[rowidx2][2],scanner1[rowidx1][0]*1-scanner2[rowidx2][2]]    
            zy=[scanner1[rowidx1][1]+scanner2[rowidx2][2],scanner1[rowidx1][1]*1-scanner2[rowidx2][2]]
            if xx1>=12 and xx[0]==offsetxx1: 
                if scanner1[rowidx1] not in candidates1: candidates1.append(scanner1[rowidx1])
                if scanner2[rowidx2] not in candidates2: candidates2.append(scanner2[rowidx2])
                
            if xx2>=12 and xx[1]==offsetxx2: 
                if scanner1[rowidx1] not in candidates1: candidates1.append(scanner1[rowidx1])
                if scanner2[rowidx2] not in candidates2: candidates2.append(scanner2[rowidx2])
            if xy1>=12 and xy[0]==offsetxy1: 
                if scanner1[rowidx1] not in candidates1: candidates1.append(scanner1[rowidx1])
                if scanner2[rowidx2] not in candidates2: candidates2.append(scanner2[rowidx2])
            if xy2>=12 and xy[1]==offsetxy2: 
                if scanner1[rowidx1] not in candidates1: candidates1.append(scanner1[rowidx1])
                if scanner2[rowidx2] not in candidates2: candidates2.append(scanner2[rowidx2])
            if xz1>=12 and xz[0]==offsetxz1: 
                if scanner1[rowidx1] not in candidates1: candidates1.append(scanner1[rowidx1])
                if scanner2[rowidx2] not in candidates2: candidates2.append(scanner2[rowidx2])
            if xz2>=12 and xz[1]==offsetxz2: 
                if scanner1[rowidx1] not in candidates1: candidates1.append(scanner1[rowidx1])
                if scanner2[rowidx2] not in candidates2: candidates2.append(scanner2[rowidx2])
            if yy1>=12 and yy[0]==offsetyy1: 
                if scanner1[rowidx1] not in candidates1: candidates1.append(scanner1[rowidx1])
                if scanner2[rowidx2] not in candidates2: candidates2.append(scanner2[rowidx2])
            if yy2>=12 and yy[1]==offsetyy2: 
                if scanner1[rowidx1] not in candidates1: candidates1.append(scanner1[rowidx1])
                if scanner2[rowidx2] not in candidates2: candidates2.append(scanner2[rowidx2])
            if yz1>=12 and yz[0]==offsetyz1: 
                if scanner1[rowidx1] not in candidates1: candidates1.append(scanner1[rowidx1])
                if scanner2[rowidx2] not in candidates2: candidates2.append(scanner2[rowidx2])
            if yz2>=12 and yz[1]==offsetyz2: 
                if scanner1[rowidx1] not in candidates1: candidates1.append(scanner1[rowidx1])
                if scanner2[rowidx2] not in candidates2: candidates2.append(scanner2[rowidx2])
            if zz1>=12 and zz[0]==offsetzz1: 
                if scanner1[rowidx1] not in candidates1: candidates1.append(scanner1[rowidx1])
                if scanner2[rowidx2] not in candidates2: candidates2.append(scanner2[rowidx2])
            if zz2>=12 and xy[1]==offsetzz2: 
                if scanner1[rowidx1] not in candidates1: candidates1.append(scanner1[rowidx1])
                if scanner2[rowidx2] not in candidates2: candidates2.append(scanner2[rowidx2])
            if yx1>=12 and yx[0]==offsetyx1: 
                if scanner1[rowidx1] not in candidates1: candidates1.append(scanner1[rowidx1])
                if scanner2[rowidx2] not in candidates2: candidates2.append(scanner2[rowidx2])
            if yx2>=12 and yx[1]==offsetyx2: 
                if scanner1[rowidx1] not in candidates1: candidates1.append(scanner1[rowidx1])
                if scanner2[rowidx2] not in candidates2: candidates2.append(scanner2[rowidx2])
            if zx1>=12 and zx[0]==offsetzx1: 
                if scanner1[rowidx1] not in candidates1: candidates1.append(scanner1[rowidx1])
                if scanner2[rowidx2] not in candidates2: candidates2.append(scanner2[rowidx2])
            if zx2>=12 and zx[1]==offsetzx2: 
                if scanner1[rowidx1] not in candidates1: candidates1.append(scanner1[rowidx1])
                if scanner2[rowidx2] not in candidates2: candidates2.append(scanner2[rowidx2])
            if zy1>=12 and zy[0]==offsetzy1: 
                if scanner1[rowidx1] not in candidates1: candidates1.append(scanner1[rowidx1])
                if scanner2[rowidx2] not in candidates2: candidates2.append(scanner2[rowidx2])
            if zy2>=12 and zy[1]==offsetzy2: 
                if scanner1[rowidx1] not in candidates1: candidates1.append(scanner1[rowidx1])
                if scanner2[rowidx2] not in candidates2: candidates2.append(scanner2[rowidx2])
    # print(candidates1)
    # print(candidates2)
    return(candidates1,candidates2,rotation)
    
    
    

def getcounts(deltas):
    col1=[row[0] for row in deltas]
    col2=[row[1] for row in deltas]
    repeat1=max(set(col1),key=col1.count)
    repeat2=max(set(col2),key=col2.count)
    n1=col1.count(repeat1)
    n2=col2.count(repeat2)
    return(n1,repeat1,n2,repeat2)

def mappaths(keys,start,end):
    temppaths=list()
    paths=dict()
    for idx in range(end+1):
        temppaths=list()
        for key in keys:
            if key[0]==idx: temppaths.append(key[1])
        paths[idx]=temppaths
    #print(paths)
    return(paths)
                
def findpath(connections,start,end):
    explored=[]
    queue=[[start]]
    
    while queue:
        path=queue.pop(0)
        node=path[-1]
        if node not in explored:
            neighbors=connections[node]
            for neighbor in neighbors:
                new_path=list(path)
                new_path.append(neighbor)
                queue.append(new_path)
                if neighbor==end:
                    return(new_path)

            
   

scanner=0
scandata=list()
page=list()
for row in data:
    if '---' in row:
        
        print(row)
        if page:
            scandata.append(page)
            page=list()
        continue
    if row: page.append(row)
scandata.append(page)

scandata=[[[int(a) for a in row.split(',')] for row in page] for page in scandata]

# a2,a1,rot=findbeacons(scandata[4],scandata[1])

# test=np.array(a2[0].append(1))

rots=dict()
matches=dict()

for idx1 in range(len(scandata)):
    for idx2 in range(len(scandata)):
        #print((idx1,idx2))
        if idx1!=idx2: 
            a2,a1,rot=findbeacons(scandata[idx2],scandata[idx1])
            if a1:
                rots[(idx1,idx2)]=rot
                matches[(idx1,idx2)]=a1

connections=mappaths(rots.keys(),0,4)
origin=np.array([0,0,0,1])
for idx1 in range(len(scandata)):
    d=findpath(connections,0,idx1)
    # print((d[-2],d[-1]))
    # neworigin=np.matmul(rots[(d[-2],d[-1])],origin)
    neworigin=origin
    for n in range(len(d)-1):
        # print((d[-2-n],d[-1-n]))
        # print(neworigin)
        neworigin=np.matmul(rots[(d[-2-n],d[-1-n])],neworigin)
    print(idx1)
    print(neworigin)
# for idx in range(len(a1)):
#     print(a1[idx][0]-a2[idx][0],a1[idx][0]-a2[idx][1],a1[idx][0]-a2[idx][2],a1[idx][1]-a2[idx][1],a1[idx][1]-a2[idx][2],a1[idx][2]-a2[idx][2])
#     print(a1[idx][0]+a2[idx][0],a1[idx][0]+a2[idx][1],a1[idx][0]+a2[idx][2],a1[idx][1]+a2[idx][1],a1[idx][1]+a2[idx][2],a1[idx][2]+a2[idx][2])

    


            

