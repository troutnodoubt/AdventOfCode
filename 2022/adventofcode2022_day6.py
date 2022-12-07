# fname="day6_example.txt"
fname="input_day6.txt"
with open(fname) as fp: data = fp.read().splitlines()

def signal_lock(buffer,windowsize):
    for index in range(windowsize-1,len(buffer)+1):
        test=buffer[index-windowsize:index]
        if len(set(test))==windowsize:
            return(index)
        
print('Part 1 solution is',signal_lock(data[0],4))
print('Part 2 solution is',signal_lock(data[0],14))
