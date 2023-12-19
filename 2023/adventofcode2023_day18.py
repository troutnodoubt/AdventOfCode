import math

fname='input_day18.txt'
#fname='example_day18.txt'
with open(fname) as fp: data = fp.read().splitlines()

def shoelace(coords):
    area=0
    for i in range(len(coords)-1):
        area+=(coords[i][0]*coords[i+1][1] - coords[i+1][0]*coords[i][1])
    return area/2

def perimeter(coords):
    p=0
    for i in range(len(coords)-1):
        p+=math.sqrt((coords[i+1][0]-coords[i][0])**2 + (coords[i+1][1]-coords[i][1])**2)
    return p

plan=[line.split(' ') for line in data]
corners=[(0,0)]
for step in plan:
    lastx=corners[-1][0]
    lasty=corners[-1][1]
    if step[0]=='L':
        corners.append((lastx-int(step[1]),lasty))
    elif step[0]=='R':
        corners.append((lastx+int(step[1]),lasty))
    elif step[0]=='U':
        corners.append((lastx,lasty+int(step[1])))
    elif step[0]=='D':
        corners.append((lastx,lasty-int(step[1])))

a=shoelace(corners)
p=perimeter(corners)

print('Part 1 solution is', int(abs(a)+0.5*p+1))

corners=[(0,0)]
for step in plan:
    direction=int(step[2][-2])
    dist=eval('0x'+step[2][2:-2])
    lastx=corners[-1][0]
    lasty=corners[-1][1]
    if direction==2:
        corners.append((lastx-dist,lasty))
    elif direction==0:
        corners.append((lastx+dist,lasty))
    elif direction==3:
        corners.append((lastx,lasty+dist))
    elif direction==1:
        corners.append((lastx,lasty-dist))

a=shoelace(corners)
p=perimeter(corners)

print('Part 2 solution is', int(abs(a)+0.5*p+1))
