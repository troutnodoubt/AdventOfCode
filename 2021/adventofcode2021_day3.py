fname="C://Users/Mark/Documents/Advent of Code/2021/day_3_example.txt"
fname="C://Users/Mark/Documents/Advent of Code/2021/input_day3.txt"
with open(fname) as fp: data = fp.read().splitlines()
        

nbits=len(data[0])
gamma=''
epsilon=''
for i in range(0,nbits):
    count1=0
    count0=0
    for row in data:
        if row[i]=='0':
            count0+=1
        elif row[i]=='1':
            count1+=1
        else:
            print('something is wrong')
    if count1>count0:
        gamma=gamma+'1'
        epsilon=epsilon+'0'
    else:
        gamma=gamma+'0'
        epsilon=epsilon+'1'
    
print('Part 1 solution is', int(gamma,2)*int(epsilon,2)) 



nbits=len(data[0])

reduced0=data.copy()
reduced1=data.copy()
print(reduced1)
for i in range(0,nbits):
    count1=0
    count0=0
    nrow=0
    for row in reduced1:
        if row[i]=='0':
            count0+=1
        elif row[i]=='1':
            count1+=1
        else:
            print('something is wrong')
    if count1>=count0:
        rating='1'
        
    else:
        rating='0'
    #print(rating)
    tempreduced1=list()
    for row in reduced1:
        
        if row[i]==rating:
            tempreduced1.append(row)
    reduced1=list()
    reduced1=tempreduced1.copy()
    
    print(reduced1)
    print(len(reduced1))
    if len(reduced1)==1:
        break
   

print(reduced0)
for i in range(0,nbits):
    count1=0
    count0=0
    nrow=0
    for row in reduced0:
        if row[i]=='0':
            count0+=1
        elif row[i]=='1':
            count1+=1
        else:
            print('something is wrong')
    if count0<=count1:
        rating='0'
        
    else:
        rating='1'
    #print(rating)
    tempreduced0=list()
    for row in reduced0:
        
        if row[i]==rating:
            tempreduced0.append(row)
    reduced0=list()
    reduced0=tempreduced0.copy()
    
    print(reduced0)
    print(len(reduced0))
    if len(reduced0)==1:
        break        

#Part 2 solution is 1753488 wrong   
print('Part 2 solution is', int(reduced1[0],2)*int(reduced0[0],2))