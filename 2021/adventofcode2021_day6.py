
fname="C://Users/Mark/Documents/Advent of Code/2021/day_6_example.txt"
fname="C://Users/Mark/Documents/Advent of Code/2021/input_day6.txt"
with open(fname) as fp: data = fp.read().splitlines()

data=[int(a) for a in data[0].split(',')]

day=0
nextdata=list()
while day<256:
    print(day)
    spawn=0
    nextdata=list()
    for i in data:
        if i>0:
            nextdata.append(i-1)
        elif i==0:
            nextdata.append(6)
            spawn+=1
        else:
            print('something is wrong')
    for i in range(spawn):
        nextdata.append(8)
    data=list()
    data=nextdata.copy()
    day+=1
    
        
print('Part 1 solution is', len(data))       
