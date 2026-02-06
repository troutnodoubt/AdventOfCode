
fname='/home/mark/Documents/git/AdventOfCode/2025/input_day12.txt'

with open(fname) as fp: data = fp.read().splitlines()

shapes=dict()
shapes[0]=7
shapes[1]=7
shapes[2]=5
shapes[3]=6
shapes[4]=7
shapes[5]=7

count=0
wontfit=0
total=0
for row in data:
    if 'x' in row:
        total+=1
        width=int(row.split(' ')[0][0:2])
        height=int(row.split(' ')[0][3:5])
        print(width,height)
        npossiblefullboxes = (width//3)*(height//3)
        boxes=[int(a) for a in row.split(' ')[1:]]
        nboxes=sum(boxes)
        print(npossiblefullboxes,nboxes)
        npixels=0
        for i,n in enumerate(boxes):
            npixels+=n*shapes[i]
        print(npixels)
        print()
        if nboxes<=npossiblefullboxes: 
            count+=1
        elif npixels>width*height:
            wontfit+=1
print(total,count,wontfit) 

print('Part 1 is',count)
    
            
    