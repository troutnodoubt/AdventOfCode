from collections import Counter
fname="C://Users/Mark/Documents/Advent of Code/2021/day_10_example.txt"
fname="C://Users/Mark/Documents/Advent of Code/2021/input_day10.txt"
with open(fname) as fp: data = fp.read().splitlines()


matches=dict()

matches['(']=')'
matches['[']=']'
matches['{']='}'
matches['<']='>'

cmatches=dict()

cmatches[')']='('
cmatches[']']='['
cmatches['>']='<'
cmatches['}']='{'

mismatch=list()
cleanlist=list()
cleanidx=list()
rowidx=0
termination=''

totalscore=list()

for row in data:
    reducing=True
    
    while reducing:
        oldlength=len(row)
        row=row.replace('()','')
        row=row.replace('[]','')
        row=row.replace('<>','')
        row=row.replace('{}','')
        #print(row)
        if len(row)==oldlength:
            reducing=False
    print(row)
    clean=True
    for value in row:
        if value in matches.values():
            print(value)
            mismatch.append(value)
            clean=False
            break
    if clean:
        
        cleanidx.append(rowidx)
        termination=''
        for value in row:
            termination=termination+matches[value]
        termination=termination[::-1]
        cleanlist.append(data[rowidx]+termination)
        
        score=0
        for y in termination:
            if y==')': score=score*5+1
            if y==']': score=score*5+2
            if y=='}': score=score*5+3
            if y=='>': score=score*5+4
        
        totalscore.append(score)
        
    rowidx+=1
      
a=Counter(mismatch)           

totalscore.sort()

print('Part 1 solution is', a[')']*3+a[']']*57+a['}']*1197+a['>']*25137)        
print('Part 2 solution is', totalscore[len(totalscore)//2])