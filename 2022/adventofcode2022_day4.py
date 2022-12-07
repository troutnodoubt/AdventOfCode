fname="day4_example.txt"
fname="input_day4.txt"
with open(fname) as fp: data = fp.read().splitlines()


countall=0
countany=0

for a in data:
    range0=a.split(',')[0]
    range1=a.split(',')[1]
    check0=[]
    check1=[]
    #print(range0,range1)
    for number in range(int(range0.split('-')[0]),int(range0.split('-')[1])+1):
        check0.append(number in range(int(range1.split('-')[0]),int(range1.split('-')[1])+1))
    for number in range(int(range1.split('-')[0]),int(range1.split('-')[1])+1):
        check1.append(number in range(int(range0.split('-')[0]),int(range0.split('-')[1])+1))
    #print(check0)
    #print(check1)
    if all(check0) or all (check1):
        countall+=1
    if any(check0) or any (check1):
        countany+=1
print("Part 1 solution is",countall)
print("Part 2 solution is",countany)
