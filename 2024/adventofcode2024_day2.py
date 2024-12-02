fname='input_day2.txt'
#fname='example_day2.txt'
with open(fname) as fp: data = fp.read().splitlines()

def safe(record,dampener=0):
    distance=[]
    
    for i in range(len(record)-1):
        distance.append(record[i+1]-record[i])
    close = all(abs(d)<=3 for d in distance)
    samesign = all(d>0 for d in distance) or all(d<0 for d in distance)
    if (not samesign or not close) and dampener:
        for i in range(len(record)):
            test=[e for e in record]
            test.pop(i)
            if safe(test) == 1: return 1
            test=[]
    
    if close and samesign: return 1
    else: return 0  

total=0 
total2=0      
for line in data:
    record=[int(a) for a in line.split()]
    total+=safe(record)
    total2+=safe(record,1)

print('Part 1 solution', total)
print('Part 2 solution', total2)

