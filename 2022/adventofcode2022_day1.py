fname="day1_example.txt"
fname="input_day1.txt"
with open(fname) as fp: data = fp.read().splitlines()
data.append('')
        
calories=0
sumcalories=[]

for a in data:
    if len(a)>0:
        calories+=int(a)
    else:
        sumcalories.append(calories)
        calories=0
   
print('Part 1 solution is', max(sumcalories))

sumcalories.sort()
print('Part 2 solution is', sum(sumcalories[-3:]))
