import re

def crane(sidestack,instructions,config):
    for row in instructions:
        nums = [int(a) for a in (re.findall("[0-9]+",row))]
        
        if config==9000:
            for n in range(nums[0]):
                moved=sidestack[nums[1]-1][:1]
                sidestack[nums[2]-1]=moved+sidestack[nums[2]-1]
                sidestack[nums[1]-1]=sidestack[nums[1]-1][1:]
        elif config==9001:
            moved=sidestack[nums[1]-1][:nums[0]]
            sidestack[nums[2]-1]=moved+sidestack[nums[2]-1]
            sidestack[nums[1]-1]=sidestack[nums[1]-1][nums[0]:]
  
    sol=''
    for col in range(0,nstack):
        sol+=sidestack[col][0]
    return(sol)


fname="day5_example.txt"
fname="input_day5.txt"
with open(fname) as fp: data = fp.read().splitlines()

stacks=[]
rowcount=0
for row in data:
    stacks.append(row)
    rowcount+=1
    if len(row)==0: break

instructions = data[rowcount:]

nstack = int([a for a in stacks[-2]][-2])

stacks.pop()

sidestack=[]

for col in range(1,nstack+1):
    sidestackn=''
    for row in stacks:        
        #print(row[col*4-3])
        if (row[col*4-3]) != ' ': sidestackn+=(row[col*4-3])
    sidestack.append(sidestackn)

sidestack2=sidestack.copy()

print('Part 1 solution is', crane(sidestack,instructions,9000))
print('Part 2 solution is', crane(sidestack2,instructions,9001))