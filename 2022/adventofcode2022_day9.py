
fname="day9_example.txt"
fname="input_day9.txt"
with open(fname) as fp: data = fp.read().splitlines()

tail=[0,0]
head=[0,0]

def touching():
    distance=abs(tail[0]-head[0])+abs(tail[1]-head[1])
    if distance==2:
        if (tail[0]==head[0]) or (tail[1]==head[1]):
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
  
visited=[]

for instruction in data:
    direction = instruction.split(' ')[0]
    nstep = int(instruction.split(' ')[1])
    for i in range(nstep):
        
        if head not in visited: visited.append(head[:])
                
        if touching():
            if direction == "R":
                tail[1]+=1
                    
            elif direction== "L":
               tail[1]-=1
                
            elif direction== "U":
               tail[0]+=1
                
            elif direction== "D":
               tail[0]-=1
                
            else:
                print('Something wrong')
        
       
        if not touching():
            if (head[0]==tail[0]) and (head[1]!=tail[1]): #same row
                head[1]+=sign(tail[1]-head[1])*(abs(tail[1]-head[1])-1)
            elif (head[0]!=tail[0]) and (head[1]==tail[1]): #same col
                head[0]+=sign(tail[0]-head[0])*(abs(tail[0]-head[0])-1)
            elif (head[0]==tail[0]) and (head[1]==tail[1]): #same space
                bananas=0# do nothing
            else:
                if direction=="R" or direction=="L":
                    head[0]+=sign(tail[0]-head[0])*(abs(tail[0]-head[0])-0)
                    head[1]+=sign(tail[1]-head[1])*(abs(tail[1]-head[1])-1)
                if direction=="U" or direction=="D":
                    head[0]+=sign(tail[0]-head[0])*(abs(tail[0]-head[0])-1)
                    head[1]+=sign(tail[1]-head[1])*(abs(tail[1]-head[1])-0)
        
print('Part 1 solution is', len(visited))      
                                                            