import numpy as np

fname='input_day6.txt'
with open(fname) as fp: data = fp.read().splitlines()

def updateArray(start,stop,operation):
    startx=int(start.split(',')[0])
    starty=int(start.split(',')[1])
    stopx=int(stop.split(',')[0])
    stopy=int(stop.split(',')[1])
    if operation == 'on':
        a[startx:stopx+1,starty:stopy+1]=True
    elif operation == 'off':
        a[startx:stopx+1,starty:stopy+1]=False
    elif operation == 'toggle':
        a[startx:stopx+1,starty:stopy+1]=np.invert(a[startx:stopx+1,starty:stopy+1])
        
def updateBrightness(start,stop,operation):
    startx=int(start.split(',')[0])
    starty=int(start.split(',')[1])
    stopx=int(stop.split(',')[0])
    stopy=int(stop.split(',')[1])
    if operation == 'on':
        b[startx:stopx+1,starty:stopy+1]+=1
    elif operation == 'off':
        b[startx:stopx+1,starty:stopy+1]-=1
        b[startx:stopx+1,starty:stopy+1][b[startx:stopx+1,starty:stopy+1]<0]=0
    elif operation == 'toggle':
        b[startx:stopx+1,starty:stopy+1]+=2

size=1000

a=np.zeros((size,size),bool)
b=np.zeros((size,size),int)

for entry in data:
    operation=entry.split(' ')[-4]
    start=entry.split(' ')[-3]
    stop=entry.split(' ')[-1]
    updateArray(start,stop,operation)
    updateBrightness(start,stop,operation)
    

print('Part 1 solution is', np.count_nonzero(a))
print('Part 2 solution is', sum(sum(b)))  
