fname="day9_example.txt"
fname="input_day9.txt"
with open(fname) as fp: data = fp.read().splitlines()

def touching(knota,knotb):
    distance=abs(knota[0]-knotb[0])+abs(knota[1]-knotb[1])
    if distance==2:
        if (knota[0]==knotb[0]) or (knota[1]==knotb[1]):
            return False
        else:
            return True
    elif distance>2:
        return False
    else:
        return True
    
def sign(a):
    if a>=0:
        return 1
    elif a<0:
        return -1
    else:
        return

def vector(fromnode,tonode): 
    vector=[sign(tonode[0]-fromnode[0]) if (tonode[0] != fromnode[0]) else 0,
            sign(tonode[1]-fromnode[1]) if (tonode[1] != fromnode[1]) else 0]
    return vector

def nextknot(knota_nodes): #knotb follows knota
    knotb_nodes=[[0,0]]
    for idx in range(1,len(knota_nodes)):
        knota=knota_nodes[idx]
        knotb=knotb_nodes[-1]
       
        if not touching(knotb,knota):
            knotb=[knotb[0]+vector(knotb,knota)[0],knotb[1]+vector(knotb,knota)[1]]
        else:
            pass
        knotb_nodes.append(knotb)
        
    return(knotb_nodes)

def nvisited(knotsvisited,nknots):
    for i in range(1,nknots):
        knotsvisited=nextknot(knotsvisited)
    setvisited=set()
    for pos in knotsvisited: setvisited.add(tuple(pos))
    return(len(setvisited))

knot0=[0,0]
knotstart=[knot0[:]]

for instruction in data:
    direction = instruction.split(' ')[0]
    nstep = int(instruction.split(' ')[1])
    for i in range(nstep):
            
        if direction == "R":
            knot0[1]+=1
                
        elif direction== "L":
           knot0[1]-=1
            
        elif direction== "U":
           knot0[0]+=1
            
        elif direction== "D":
           knot0[0]-=1
            
        else:
            print('Something wrong')
        
        knotstart.append(knot0[:])

print('Part 1 solution is', nvisited(knotstart,2))
print('Part 2 solution is', nvisited(knotstart,10))
                                                            