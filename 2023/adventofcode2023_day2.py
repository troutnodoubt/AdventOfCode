fname='input_day2.txt'
#fname='example_day2.txt'
with open(fname) as fp: data = fp.read().splitlines()

nblue=14
ngreen=13
nred=12
sumID=0
sumPower=0
for entry in data:
    line=entry.split(' ')
    gameID=line[1][:-1]
    bluecount=0
    redcount=0
    greencount=0
    for i in range(len(line)):
        if 'blue' in line[i]: bluecount=max(int(line[i-1]),bluecount)
        elif 'red' in line[i]: redcount=max(int(line[i-1]),redcount)
        elif 'green' in line[i]: greencount=max(int(line[i-1]),greencount)
    sumPower+=bluecount*redcount*greencount
    if bluecount <= nblue and redcount <= nred and greencount <= ngreen:
        sumID+=int(gameID)
           
print('Part 1 solution', sumID)
print('Part 2 solution', sumPower)
