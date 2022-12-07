#fname="day1_example.txt"
fname="input_day3.txt"
with open(fname) as fp: data = fp.read().splitlines()


def findvisited(instructions):
    coordinate=[0,0]
    visited={tuple(coordinate):1}
    for heading in instructions:
        if heading == '^':
            coordinate[0]+=1
        elif heading=='v':
            coordinate[0]+=-1
        elif heading == '>':
            coordinate[1]+=1
        elif heading == '<':
            coordinate[1]+=-1
            
        if tuple(coordinate) in visited.keys():
            visited[tuple(coordinate)]+=1
        else:
            visited.update({tuple(coordinate):1})
    return(visited)
        
print('Part 1 solution is',len(findvisited(data[0])))

index=1
santa=''
rs=''
for a in data[0]:
    if index%2:
        santa+=a
    else:
        rs+=a
    index+=1

print('Part 2 solution is',len(findvisited(santa)|findvisited(rs)))