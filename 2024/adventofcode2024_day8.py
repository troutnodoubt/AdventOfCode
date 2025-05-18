fname='input_day8.txt'
# fname='example_day8.txt'
with open(fname) as fp: data = fp.read().splitlines()

def findAntinodes(locs,gridsize,resonant=False):
    antinodelist=[]
    for n,loc1 in enumerate(locs):
        if n<len(locs):
            for loc2 in locs[n+1:]:
                deltai=loc2[0] - loc1[0]
                deltaj=loc2[1] - loc1[1]
                cand1i = loc1[0]-deltai
                cand1j = loc1[1]-deltaj
                cand2i = loc2[0]+deltai
                cand2j = loc2[1]+deltaj
                if cand1i in range(0,gridsize) and cand1j in range(0,gridsize): antinodelist.append((cand1i,cand1j))
                if cand2i in range(0,gridsize) and cand2j in range(0,gridsize): antinodelist.append((cand2i,cand2j))
    return antinodelist

def findResonantAntinodes(locs,gridsize):
    antinodelist=[]
    for n,loc1 in enumerate(locs):
        if n<len(locs):
            for loc2 in locs[n+1:]:
                if loc1==loc2: 
                    print(loc1,loc2)
                    break
                deltai=loc2[0] - loc1[0]
                deltaj=loc2[1] - loc1[1]
                m=0
                offgrid1=False
                offgrid2=False
                while not offgrid1 or not offgrid2:
                    cand1i = loc1[0]-deltai*m
                    cand1j = loc1[1]-deltaj*m
                    cand2i = loc2[0]+deltai*m
                    cand2j = loc2[1]+deltaj*m
                    if cand1i in range(0,gridsize) and cand1j in range(0,gridsize): antinodelist.append((cand1i,cand1j))
                    else: 
                        offgrid1=True
                    if cand2i in range(0,gridsize) and cand2j in range(0,gridsize): antinodelist.append((cand2i,cand2j))
                    else: 
                        offgrid2=True
                    m+=1
    return antinodelist
 
antennas={}
allantennas=[]
for i,row in enumerate(data):
    for j,pos in enumerate(row):
        if pos!='.':
            if pos not in antennas.keys():
                antennas[pos]=[(i,j)]
            else:
                antennas[pos].append((i,j))
            allantennas.append((i,j))

antinodes={}
allantinodes=[]
for antenna in antennas.keys():
    antinodes[antenna] = findAntinodes(antennas[antenna],len(data))
    # print(antenna)
    # print(antinodes[antenna])
    for antinode in antinodes[antenna]:
        if antinode not in allantinodes: allantinodes.append(antinode)

print("Part 1",len(allantinodes))

antinodes={}
allantinodes=[]
for antenna in antennas.keys():
    antinodes[antenna] = findResonantAntinodes(antennas[antenna],len(data))
    # print(antenna)
    # print(antinodes[antenna])
    for antinode in antinodes[antenna]:
        if antinode not in allantinodes: allantinodes.append(antinode)

print("Part 2",len(allantinodes))
