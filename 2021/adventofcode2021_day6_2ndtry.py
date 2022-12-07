fname="C://Users/Mark/Documents/Advent of Code/2021/day_6_example.txt"
fname="C://Users/Mark/Documents/Advent of Code/2021/input_day6.txt"
with open(fname) as fp: data = fp.read().splitlines()

data=[int(a) for a in data[0].split(',')]

day=0
#nextdata=list()
while day<256:
    print(day)
    spawn=0
    #nextdata=list()
    for idx in range(len(data)):
        if data[idx]>0:
            data[idx]+=-1
        elif data[idx]==0:
            data[idx]=6
            spawn+=1
        else:
            print('something is wrong')
    for i in range(spawn):
        data.append(8)
   
    day+=1
    
        
print('Part 1 solution is', len(data))  
