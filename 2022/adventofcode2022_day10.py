fname="day10_example.txt"
fname="input_day10.txt"
with open(fname) as fp: data = fp.read().splitlines()

def checkstrength(cyclenum,xval):
    cycles=[20,60,100,140,180,220]
    if ncycles in cycles:
        return(cyclenum*xval)
    else:
        return(0)
    
def plotpixels(spriteloc,cycle):
    sprite=range(spriteloc-1,spriteloc+2)
    if cycle%40 in sprite:
        pixel='#'
    else:
        pixel=' '
    return(pixel)

x=1
ncycles=1
ss=0
CRT=plotpixels(x,ncycles)

for row in data:
    command=row.split(' ')[0]

    if command=='addx':
        CRT+=plotpixels(x,ncycles)
        
        ncycles+=1
        
        ss+=checkstrength(ncycles,x)
        x+=int(row.split(' ')[1])
        
        CRT+=plotpixels(x,ncycles)
                
        ncycles+=1
        
        ss+=checkstrength(ncycles,x)
    elif command=='noop':
        CRT+=plotpixels(x,ncycles)
        
        ncycles+=1
        
        ss+=checkstrength(ncycles,x)
        
print('Part 1 solution is', ss)
print()
print(CRT[:40])
print(CRT[40:80])
print(CRT[80:120])
print(CRT[120:160])
print(CRT[160:200])
print(CRT[200:240])
                                                            