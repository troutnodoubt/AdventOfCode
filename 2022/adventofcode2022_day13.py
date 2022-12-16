# quick sort functions shamelessly adapted from https://stackabuse.com/quicksort-in-python/

fname="day13_example.txt"
fname="input_day13.txt"
with open(fname) as fp: data = fp.read().splitlines()
data.append('')

def comparepackets(leftp,rightp):
    if type(leftp)==int and type(rightp)==int:
        rightorder=compareints(leftp,rightp)
       
        return(rightorder)
          
    elif type(leftp)==list and type(rightp)==list:
       
        for i in range(min(len(leftp),len(rightp))):
            
            test=comparepackets(leftp[i],rightp[i])
            
            if test!='na': return(test)
       
        if len(leftp) < len(rightp):
            return 'rightorder'
        elif len(leftp) > len(rightp):
            return 'wrongorder'
        else:
            return 'na'
        
    elif type(leftp)==int and type(rightp)==list:
        return(comparepackets([leftp],rightp))
        
    elif type(leftp)==list and type(rightp)==int:
        return(comparepackets(leftp,[rightp]))
    else:
        print('oh boy')
        return

def compareints(l,r): 
   
    if l<r:
        return 'rightorder'
    elif l>r:
        return 'wrongorder'
    else:
        return 'na'

def partition(array, start, end):
    pivot = array[start]
    low = start + 1
    high = end

    while True:
       
        while low <= high and comparepackets(pivot,array[high])=='rightorder':
            high = high - 1
       
        while low <= high and comparepackets(pivot,array[low])=='wrongorder':
            low = low + 1

        if low <= high:
            array[low], array[high] = array[high], array[low]
            
        else:
           
            break

    array[start], array[high] = array[high], array[start]

    return high

def quick_sort(array, start, end):
    if start >= end:
        return

    p = partition(array, start, end)
    quick_sort(array, start, p-1)
    quick_sort(array, p+1, end)

idx=0
pairnum=1
packets={}
for row in data:

    if idx%3==0:
        left=eval(row)
    elif idx%3==1:
        right=eval(row)
    elif idx%3==2:
        packets[pairnum]=(left,right)
        pairnum+=1
    idx+=1
    


sol_idx=[]

for index in packets.keys():
    test=packets[index]
    a=comparepackets(test[0],test[1])
    if a=='rightorder':
        sol_idx.append(index)

print('Part 1 solution is', sum(sol_idx))


array=[]
for row in data:
    if len(row)>0:
        array.append(eval(row))
        

dp1=[[2]]
dp2=[[6]]
array.append(dp1)
array.append(dp2)

quick_sort(array, 0, len(array) - 1)

print('Part 2 solution is',(array.index(dp1)+1)*(array.index(dp2)+1))
