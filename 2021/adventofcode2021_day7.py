fname="C://Users/Mark/Documents/Advent of Code/2021/day_7_example.txt"
fname="C://Users/Mark/Documents/Advent of Code/2021/input_day7.txt"
with open(fname) as fp: data = fp.read().splitlines()

data=[int(a) for a in data[0].split(',')]

maxposition=max(data)
fuelmin=maxposition*len(data)
for postest in data:
    fuel=0
    for pos in data:
        fuel+=abs(pos-postest)
    if fuel<fuelmin:
        fuelmin=fuel
        bestpos=postest

print('Part 1 solution is', fuelmin, 'at location', bestpos)


maxposition=max(data)
fuelmin=maxposition*len(data)*100
for postest in range(max(data)+1):
    fuel=0
    for pos in data:
        distance=abs(pos-postest)
        
        fuel+=distance*(distance+1)//2
        if postest==5:
            print(pos,distance*(distance+1)/2)
    if fuel<fuelmin:
        fuelmin=fuel
        bestpos=postest

print('Part 2 solution is', fuelmin, 'at location', bestpos)