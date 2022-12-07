import numpy as np

fname="C://Users/Mark/Documents/Advent of Code/2021/day_6_example.txt"
fname="C://Users/Mark/Documents/Advent of Code/2021/input_day6.txt"
with open(fname) as fp: data = fp.read().splitlines()

data=[int(a) for a in data[0].split(',')]
data=np.array(data)

day=0
#nextdata=list()
while day<256:
    #print(day,data)
    data=np.array(data)
    print(day)
    #nextdata=list()
    where_0=np.where(data==0)
   # print(where_0)
    spawn=len(data)-np.count_nonzero(data)
    data[where_0]=7
    data=data-1
    #print(spawn)
    data=data.tolist()
    for i in range(spawn):
        #print(i)
        data.append(8)
   
    day+=1
    
        
print('Part 1 solution is', len(data))  
