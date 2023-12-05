import math

fname='input_day5.txt'
#fname='example_day5.txt'
with open(fname) as fp: data = fp.read().splitlines()

def getMaps():
    data.pop(0)
    data.pop(0)
    newmap=[]
    for line in data:
        if len(line)==0:
            break
        else:
            newmap.append([int(x) for x in line.split(' ')])
    return newmap

def getRanges(maps):
    rng={}
    for line in maps:
        for i in range(line[2]):
            rng[line[1]+i]=line[0]+i
    return rng

def nextIdx(idx,maps):
    for line in maps:
        if idx in range(line[1],line[1]+line[2]):
            nextidx=line[0]+idx-line[1]
            break
        else:
            nextidx=idx
    return nextidx

def findMaxVal(maps):
    m=0
    for line in maps:
        m=max(m,line[1]+line[2],line[0]+line[2])
    return m

seeds = [int(x) for x in data[0].split(' ') if x.isnumeric()]
data.pop(0)

seed2soilmap=getMaps()
for i in range(len(seed2soilmap)): data.pop(0)
soil2fertmap=getMaps()
for i in range(len(soil2fertmap)): data.pop(0)
fert2watermap=getMaps()
for i in range(len(fert2watermap)): data.pop(0)
water2lightmap=getMaps()
for i in range(len(water2lightmap)): data.pop(0)
light2tempmap=getMaps()
for i in range(len(light2tempmap)): data.pop(0)
temp2humidmap=getMaps()
for i in range(len(temp2humidmap)): data.pop(0)
humid2locmap=getMaps()

seedloc=math.inf
for seed in seeds:
    soil=nextIdx(seed,seed2soilmap)
    fert=nextIdx(soil,soil2fertmap)
    water=nextIdx(fert,fert2watermap)
    light=nextIdx(water,water2lightmap)
    temp=nextIdx(light,light2tempmap)
    humid=nextIdx(temp,temp2humidmap)
    loc=nextIdx(humid,humid2locmap)
    if loc<seedloc: seedloc=loc

print('Part 1 solution', seedloc)

maxseed=0
maxseed=max(maxseed,findMaxVal(seed2soilmap))
maxseed=max(maxseed,findMaxVal(soil2fertmap))
maxseed=max(maxseed,findMaxVal(fert2watermap))
maxseed=max(maxseed,findMaxVal(water2lightmap))
maxseed=max(maxseed,findMaxVal(light2tempmap))
maxseed=max(maxseed,findMaxVal(temp2humidmap))
maxseed=max(maxseed,findMaxVal(humid2locmap))

seedloc=math.inf
for i in range(0,len(seeds),2):
    extraseeds=range(seeds[i],seeds[i]+seeds[i+1])
    print(i,len(seeds),extraseeds)
    print(maxseed)
    for seed in extraseeds:
        if seed>maxseed: 
            print('broken')
            break
        soil=nextIdx(seed,seed2soilmap)
        fert=nextIdx(soil,soil2fertmap)
        water=nextIdx(fert,fert2watermap)
        light=nextIdx(water,water2lightmap)
        temp=nextIdx(light,light2tempmap)
        humid=nextIdx(temp,temp2humidmap)
        loc=nextIdx(humid,humid2locmap)
        if loc<seedloc: seedloc=loc
        
print('Part 2 solution', seedloc)
