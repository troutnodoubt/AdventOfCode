fname="C://Users/Mark/Documents/Advent of Code/2021/day_6_example.txt"
fname="C://Users/Mark/Documents/Advent of Code/2021/input_day6.txt"
with open(fname) as fp: data = fp.read().splitlines()

data=[int(a) for a in data[0].split(',')]
fish={}
for i in range(9):
    fish[i]=data.count(i)


day=0
nextfish={}
while day<256:
    print(day)
    fishlist=list()
    for i in range(9):
        fishlist.append(fish[i])
    print(fishlist)
    for i in range(9):
        if i==8:
            nextfish[8]=fish[0]
        elif i==0:
            nextfish[0]=fish[1]
        elif i==6:
            nextfish[6]=fish[7]+fish[0]
        else:
            nextfish[i]=fish[i+1]
    
    
    fish={}
    fish=nextfish.copy()
    
   
    day+=1
    
        
print('Part 1 solution is', sum(fish.values()))  
