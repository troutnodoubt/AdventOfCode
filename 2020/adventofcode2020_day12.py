fname="C://Users/Mark/Documents/Advent of Code/2020/day_12_example.txt"
fname="C://Users/Mark/Documents/Advent of Code/2020/input_day12.txt"
with open(fname) as fp: instructions = fp.read().splitlines()

theta=0
x=0
y=0




for row in instructions:
    #print(row)
    command=row[0]
    #print(command)
    value=int(row[1:])
    #print(value)
    theta=theta%360
   # print(theta)
    if command=='F':
        if theta==0:
            x=x+value
        elif theta==180:
            x=x-value
        elif theta==90:
            y=y+value
        elif theta==270:
            y=y-value
        else:
            print('Something is wrong with theta')
#        x=x+value*math.cos(math.radians(theta))
#        y=y+value*math.sin(math.radians(theta))
    elif command=='N':
        y=y+value
    elif command=='S':
        y=y-value
    elif command=='E':
        x=x+value
    elif command=='W':
        x=x-value
    elif command=='R':
        theta=theta-value
    elif command=='L':
        theta=theta+value
    else:
        print('Something is wrong with the commands')


print('Part 1 solution is',abs(x)+abs(y))

x=0
y=0
theta=0
wpx=10
wpy=1

for row in instructions:
    #print(row)
    command=row[0]
    #print(command)
    value=int(row[1:])
    #print(value)
    theta=theta%360
    #print(theta)
    if command=='F':
       x=value*wpx+x
       y=value*wpy+y
    elif command=='N':
        wpy=wpy+value
    elif command=='S':
        wpy=wpy-value
    elif command=='E':
        wpx=wpx+value
    elif command=='W':
        wpx=wpx-value
    elif command=='R':
        if value==0:
            wpx=wpx
            wpy=wpy
        elif value==90:
            wpxnew=wpy
            wpynew=-wpx
            wpx=wpxnew
            wpy=wpynew
        elif value==180:
            wpx=-wpx
            wpy=-wpy
        elif value==270:
            wpxnew=-wpy
            wpynew=wpx
            wpx=wpxnew
            wpy=wpynew
        else:
            print('Something is wrong with the R rotation')
        
    elif command=='L':
        if value==0:
            wpx=wpx
            wpy=wpy
        elif value==90:
            wpxnew=-wpy
            wpynew=wpx
            wpx=wpxnew
            wpy=wpynew
        elif value==180:
            wpx=-wpx
            wpy=-wpy
        elif value==270:
            wpxnew=wpy
            wpynew=-wpx
            wpx=wpxnew
            wpy=wpynew
        else:
            print('Something is wrong with the R rotation')        
    else:
        print('Something is wrong with the commands')       
print('Part 2 solution is',abs(x)+abs(y))