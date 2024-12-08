adapterfile="C://Users/Mark/Documents/Advent of Code/2020/day_10_exampleA.txt"
adapterfile="C://Users/Mark/Documents/Advent of Code/2020/day_10_exampleB.txt"
adapterfile="C://Users/Mark/Documents/Advent of Code/2020/input_day10.txt"

def readIntegers(pathToFile):

    with open(pathToFile) as f:
        a = [int(x) for x in f.read().split()]
    return a

adapters=readIntegers(adapterfile)
adapters.append(0) # starting joltage
adapters.append(max(adapters)+3) # ending joltage
adapters.sort()
#print(adapters)
count1=0
count3=0 #From max in bag to device is 3 jolts
ones=(len(adapters)-1)*[0]
for i in range(0,len(adapters)-1):
    diff=adapters[i+1]-adapters[i]
    if diff==3:
        count3=count3+1
    if diff==1:
        count1=count1+1
        ones[i]=1
    
#print(count3)
#print(count1)
print('Part 1 solution is',count3*count1)
count2=0
for i in range(0,len(ones)-3):
    #print(ones[i:i+4])
    if i==0 and ones[i:i+3]==[1,1,0]:
        count2=count2+1
    if ones[i:i+4]==[0,1,1,0]:
        #print(ones[i:i+4])
        count2=count2+1
count3=0
for i in range(0,len(ones)-4):
    if i==0 and ones[i:i+4]==[1,1,1,0]:
        count3=count3+1
    if ones[i:i+5]==[0,1,1,1,0]:
        #print(ones[i:i+5])
        count3=count3+1
count4=0
for i in range(0,len(ones)-3):
    if ones[i:i+4]==[1,1,1,1]:
        #print(ones[i:i+4])
        count4=count4+1

print('Part 2 solution is',7**count4*4**count3*2**count2)

        
    
