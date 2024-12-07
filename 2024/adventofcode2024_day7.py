from more_itertools import distinct_permutations

fname='input_day7.txt'
#fname='example_day7.txt'
with open(fname) as fp: data = fp.read().splitlines()

operators='+*'
permdict={}

def RPN(n1,n2,op):
    if op=='+':
        return(n1+n2)
    elif op=='*':
        return(n1*n2)
    elif op=='|':
        return(int(str(n1)+str(n2)))

def calculate(numbers,operators):
    res=numbers[0]
    for i in range(1,len(numbers)):
        res=RPN(res,numbers[i],operators[i-1])
    return res

caltotal=0
calrows=[]
for row in data:
    vals=row.split()
    total=int(vals[0][:-1])
    numbers=[int(a) for a in vals[1:]]
    ops=[a for a in operators*(len(numbers)-1)]
    # if len(numbers)-1 not in permdict.keys():
    #     combo=distinct_permutations(ops,len(numbers)-1)
    #     permdict[len(numbers)-1]=combo
    # combo=permdict[len(numbers)-1]
    #print(permdict.keys())
    comb=distinct_permutations(ops,len(numbers)-1)
   
    for i in list(comb):
        test=calculate(numbers,i)
        
        if test==total:
            # print(numbers)
            # print(i)
            # print(total)
            caltotal+=total
            calrows.append(row)
            break

print("Part 1",caltotal)

operators='+*|'

caltotal2=0
for row in data:
    if row not in calrows:
        vals=row.split()
        total=int(vals[0][:-1])
        numbers=[int(a) for a in vals[1:]]
        ops=[a for a in operators*(len(numbers)-1)]
        comb=distinct_permutations(ops,len(numbers)-1)
        for i in list(comb):
            test=calculate(numbers,i)
            if test==total:
                # print(numbers)
                # print(i)
                # print(total)
                caltotal2+=total
                break 

print("part 2",caltotal+caltotal2)
