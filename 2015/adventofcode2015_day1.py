#fname="day1_example.txt"
fname="input_day1.txt"
with open(fname) as fp: data = fp.read().splitlines()

print('Part 1 solution is',data[0].count('(')- data[0].count(')'))

a=data[0]
floor=0
position=1
for character in a:
    if character == '(': 
        floor+=1
    elif character == ')':
        floor+=-1
    if floor == -1:
        print('Part 2 solution is', position)
        break
    position+=1