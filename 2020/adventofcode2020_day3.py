trees=(
'..##.......',
'#...#...#..',
'.#....#..#.',
'..#.#...#.#',
'.#...##..#.',
'..#.##.....',
'.#.#.#....#',
'.#........#',
'#.##...#...',
'#...##....#',
'.#..#...#.#')

fname="C://Users/Mark/Documents/Advent of Code/2020/input_day3.txt"

with open(fname) as fp: trees = fp.read().splitlines()
#print(trees)


def count_trees(trees,rise,run):
    nrows=len(trees);
    ncols=len(trees[0]);
    count=0
    position=run;
    for n in range(rise,nrows,rise):
        currentrow=trees[n]
        #print(currentrow)
        currentchar=currentrow[position]
        #print(currentchar)
        #print('Position is ', position)
        if currentchar=='#':
            count=count+1
        position=position+run
        position=position%ncols
    return count

a=count_trees(trees,1,1)
b=count_trees(trees,1,3)
print('Part 1 solution is',b)
c=count_trees(trees,1,5)
d=count_trees(trees,1,7)
e=count_trees(trees,2,1)
print('Part 2 solution is',a*b*c*d*e)

