targetx=range(20,30+1)
targety=range(-10,-5+1)


# target area: x=281..311, y=-74..-54

targetx=range(281,311+1)
targety=range(-74,-54+1)


def hitstarget(vx0,vy0):
    y=0
    x=0
    vx=vx0
    vy=vy0
    while True:
        x+=vx
        y+=vy
        vx=max(0,vx-1)
        vy+=-1
        if x in targetx and y in targety: return True
        if y<targety[0]:
            return False
            break
    


pastxrange=False
vx=1
vxcands=list()
while not pastxrange:
    xfinal=((vx+1)*vx)//2
    if xfinal in targetx: vxcands.append(vx)
    if xfinal>targetx[-1]: pastxrange=True
    vx+=1
    


pastyrange=False
vy0=max(vxcands)
vx0=max(vxcands)
vycands=list()
y=0
# while not pastyrange:
while vy0<max(vxcands)*10:
    y=0
  
    vy=vy0
    stepping=True
    while stepping:
        y+=vy
        vy+=-1
        #print(vy0,y)
        
        if y in targety: 
            vycands.append(vy0)
           
            stepping=False
        if y<targety[0]: 
            pastyrange=True
            #print(pastyrange)
            break
    vy0+=1   
    #print(pastyrange)
        
maxv=max(vycands)   
maxheight=(maxv*(maxv+1))//2
print('Part 1 Solution is',maxheight)  

candidates=list()
for vx in range(targetx[-1]+1):
    for vy in range(-2*targetx[-1],2*targetx[-1]):
        if hitstarget(vx,vy): candidates.append((vx,vy))

print('Part 2 solution is', len(candidates))