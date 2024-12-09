# ER=[1721,979,366,299,675,1456]
ERfile="C://Users/Mark/Documents/Advent of Code/2020/input_day1.txt"

def readIntegers(pathToFile):

    with open(pathToFile) as f:
        a = [int(x) for x in f.read().split()]
    return a

ER=readIntegers(ERfile)

#Part 1
issolved=False
ERsum=0
for i in range(len(ER)):
    if issolved:
        break
    for j in range(len(ER)):
        # print(ER[i])
        # print(ER[j])
        if i!=j:
            ERsum=ER[i]+ER[j]
        # print(ERsum)
        if ERsum==2020:
            issolved=True
            solution=ER[i]*ER[j]
            print("Part 1 Solution found")
            print(solution)
            break
#Part 2
issolved=False
ERsum=0
for i in range(len(ER)):
    if issolved:
        break
    for j in range(len(ER)):
        if issolved:
            break
        for k in range(len(ER)):
            if i!=j and i!=k and j!=k:
                ERsum=ER[i]+ER[j]+ER[k]
            if ERsum==2020:
                issolved=True
                solution=ER[i]*ER[j]*ER[k]
                print("Part 2 Solution found")
                print(solution)
                break


