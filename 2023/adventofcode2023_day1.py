fname='input_day1.txt'
#fname='example_day1.txt'
with open(fname) as fp: data = fp.read().splitlines()

n=['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'zero', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

vals={'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9}

total=0
total2=0
for line in data:
    nums=[]
    ndictfwd={}
    ndictrev={}
    
    for char in line:
        if char.isnumeric():
            nums.append(char)
    if len(nums)>0: total+=int(nums[0]+nums[-1])
    
    for s in n:
        idx1 = line.find(s)
        idx2 = line.rfind(s)
        if idx1>=0: ndictfwd[idx1]=s
        if idx2>=0: ndictrev[idx2]=s
    dig1=ndictfwd[min(ndictfwd.keys())]
    dig2=ndictrev[max(ndictrev.keys())]
    
    if len(dig1)==1: 
        dig1=int(dig1)
    else:
        dig1=vals[dig1]
    if len(dig2)==1: 
        dig2=int(dig2)
    else:
        dig2=vals[dig2]
    
    total2+=dig1*10+dig2
    # print(line)
    # print(dig1, dig2)
            
print('Part 1 solution', total)
print('Part 2 solution', total2)
