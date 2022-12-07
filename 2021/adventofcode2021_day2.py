import re

fname="C://Users/Mark/Documents/Advent of Code/2021/day_2_example.txt"
fname="C://Users/Mark/Documents/Advent of Code/2021/input_day2.txt"
with open(fname) as fp: data = fp.read().splitlines()
        
p1=re.compile('[a-z]+')
p2=re.compile('[0-9]+')
instruction=list()
value=list()
for command in data:
    instruction.append(re.search(p1,command).group())
    value.append(int(re.search(p2,command).group()))

position=0
depth=0

for i in range(0,len(data)):
    print(i)
    if instruction[i]=='forward':
        position+=value[i]
    elif instruction[i]=='up':
        depth+=-1*value[i]
    elif instruction[i]=='down':
        depth+=value[i]
    else:
        print('something is wrong with the instructions')

print('Part 1 solution is', depth*position)

position=0
depth=0
aim=0
for i in range(0,len(data)):
    print(i)
    if instruction[i]=='forward':
        position+=value[i]
        depth+=aim*value[i]
    elif instruction[i]=='up':
        aim+=-1*value[i]
    elif instruction[i]=='down':
        aim+=value[i]
    else:
        print('something is wrong with the instructions')

print('Part 2 solution is', depth*position)