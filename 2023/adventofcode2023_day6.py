import math

time=[54,     81,     70,     88]
distance=[446,   1292,   1035,   1007]

# time=[7,  15,   30]
# distance=[9,  40,  200]

def findNWinners(t,distance):
    a=1
    b=-t
    c=distance
    x1=(-b+math.sqrt(b*b-4*a*c))/(2*a)
    x2=(-b-math.sqrt(b*b-4*a*c))/(2*a)
    counts=math.floor(x1)-math.ceil(x2)+1
    return counts

def list2str(l):
    temp=[str(x) for x in l]
    res=''
    for s in temp: res=res+s
    return int(res)

counts=1  
for n,t in enumerate(time):
    counts*=findNWinners(t, distance[n])

print('Part 1 solution', counts) 

bigtime=list2str(time)
bigdist=list2str(distance)

print('Part 2 solution', findNWinners(bigtime,bigdist))
