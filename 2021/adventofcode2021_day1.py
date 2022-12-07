fname="C://Users/Mark/Documents/Advent of Code/2021/day_1_example.txt"
fname="C://Users/Mark/Documents/Advent of Code/2021/input_day1.txt"
with open(fname) as fp: data = fp.read().splitlines()
        
data=[int(a) for a in data]
count=0
for i in range(1,len(data)):
    #print(data[i],data[i-1])
    if data[i]>data[i-1]:
        count+=1

print('Part 1 solution is', count)

#part 2
#sum 3s

sum_threes=list()

for i in range(0,len(data)-2):
    sum_threes.append(data[i]+data[i+1]+data[i+2])
#print(data)
#print(sum_threes)

count=0
for i in range(1,len(sum_threes)):
    #print(sum_threes[i],sum_threes[i-1])
    if sum_threes[i]>sum_threes[i-1]:
        count+=1
        
print('Part 2 solution is', count)