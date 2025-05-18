import re

fname='input_day13.txt'
# fname='example_day13.txt'

with open(fname) as fp: data = fp.read().splitlines()
data.append('')
  
def cramersRule(A,B,Prize):
    det=A[0]*B[1]-A[1]*B[0]
    nA=(Prize[0]*B[1]-Prize[1]*B[0])/det
    nB=(Prize[1]*A[0]-Prize[0]*A[1])/det
    return nA,nB

def solve(part2=0):
    ACost=3
    BCost=1
    maxpress=100
    options=[]
    for row in data:
        if len(row)>0:
            n = re.findall('\d+',row)
            n=[int(a) for a in n]
            if "A" in row: A=[a for a in n]
            elif "B" in row: B=[a for a in n]
            elif "Prize" in row: Prize=[a+10000000000000*part2 for a in n]
        if len(row)==0: # time to party
            a,b=cramersRule(A,B,Prize)
            gamecost=[]
            if a-int(a)==0 and b-int(b)==0 and ((a<=maxpress and b<=maxpress) or part2): gamecost=a*ACost+b*BCost 
            if gamecost:
                options.append(gamecost)
    return sum(options)

print("Part 1",int(solve(0)))
print("Part 2",int(solve(1))) 
                         