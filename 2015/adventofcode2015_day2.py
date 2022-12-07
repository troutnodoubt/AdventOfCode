#fname="day1_example.txt"
fname="input_day2.txt"
with open(fname) as fp: data = fp.read().splitlines()


paperneeded=0
ribbonneeded=0
for a in data:
    dim = [int(b) for b in a.split('x')] 
    
    dim.sort()
    
    area=2*(dim[0]*dim[1]+dim[0]*dim[2]+dim[1]*dim[2])+dim[0]*dim[1]
    volume=dim[0]*dim[1]*dim[2]
    perimeter=2*(dim[0]+dim[1])
    
    paperneeded+=area
    ribbonneeded+=volume+perimeter

print('Part 1 solution is',paperneeded)
print('Part 2 solution is',ribbonneeded)
    