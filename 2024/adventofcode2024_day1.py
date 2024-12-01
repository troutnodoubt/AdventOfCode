fname='input_day1.txt'
#fname='example_day1.txt'
with open(fname) as fp: data = fp.read().splitlines()

left=[]
right=[]

for entry in data:
    left.append(int(entry.split()[0]))
    right.append(int(entry.split()[1]))

left.sort()
right.sort()

total=0
total2=0
for i in range(len(left)):
    total+=abs(left[i] - right[i])
    total2+=left[i]*right.count(left[i])

print('Part 1 solution', total)
print('Part 2 solution', total2)
