from collections import Counter
fname="C://Users/Mark/Documents/Advent of Code/2021/day_9_example.txt"
fname="C://Users/Mark/Documents/Advent of Code/2021/input_day9.txt"
with open(fname) as fp: data = fp.read().splitlines()

# pad with 9s
mapheight=len(data)+2
mapwidth=len(data[0])+2

heights=[[9 for width in range(mapwidth)] for height in range(mapheight) ]
for row in range(1,mapheight-1):
    for col in range(1,mapwidth-1):
        heights[row][col]=int(data[row-1][col-1])
risk=list()        
#find minimums
for row in range(1,mapheight-1):
    for col in range(1,mapwidth-1):
        if heights[row][col]<heights[row+1][col] and heights[row][col]<heights[row-1][col] and heights[row][col]<heights[row][col+1] and heights[row][col]<heights[row][col-1]:
            #print(row,col,heights[row][col])
            risk.append(heights[row][col]+1)

print('Part 1 solution is',sum(risk))


vector=dict()           
for row in range(1,mapheight-1):
    for col in range(1,mapwidth-1):
        pos=(row,col)
        test=heights[row][col]
        below=heights[row-1][col]
        above=heights[row+1][col]
        right=heights[row][col+1]
        left=heights[row][col-1]
        if test==9:
            vector[pos]=pos
            
        elif below<test and below!=9:
            vector[pos]=(row-1,col)
        elif above<test and above!=9:
            vector[pos]=(row+1,col)
        elif left<test and left!=9:
            vector[pos]=(row,col-1)
        elif right<test and right!=9:
            vector[pos]=(row,col+1)
        else:
            vector[pos]=pos

basins=dict()
for entry in vector.keys():
    flow=list()
    newkey=entry
    flow.append(newkey)
    flowing=True
    while flowing:
        newkey=vector[newkey]
        flow.append(newkey)
        if flow[-1]==flow[-2]:
            flowing=False
    basins[entry]=flow[-1]

counts=Counter(basins.values())
counts=list(counts.values())
counts.sort(reverse=True)

print('Part 2 solution is',counts[0]*counts[1]*counts[2])