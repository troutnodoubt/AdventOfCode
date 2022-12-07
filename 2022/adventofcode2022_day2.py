fname="day2_example.txt"
fname="input_day2.txt"
with open(fname) as fp: data = fp.read().splitlines()

def rps(opponent,you):
    xscore=1
    yscore=2
    zscore=3
    win=6
    draw=3
    lose=0
    if opponent=='A':
        if you=='X':
            return draw+xscore
        elif you=='Y':
            return win+yscore
        elif you=='Z':
            return lose+zscore
    elif opponent=='B':
        if you=='Y':
            return draw+yscore
        elif you=='Z':
            return win+zscore
        elif you=='X':
            return lose+xscore
    elif opponent=='C':
        if you=='X':
            return win+xscore
        elif you=='Y':
            return lose+yscore
        elif you=='Z':
            return draw+zscore

def rps_winlose(opponent,you):
    s=''
    if you=='X': # lose
        if opponent=='A':
            s='Z'
        elif opponent=='B':
            s='X'
        elif opponent=='C':
            s='Y'
    elif you=='Y': # draw
        if opponent=='A':
            s='X'
        elif opponent=='B':
            s='Y'
        elif opponent=='C':
            s='Z'
    elif you=='Z': # win
        if opponent=='A':
            s='Y'
        elif opponent=='B':
            s='Z'
        elif opponent=='C':
            s='X'
    return s
    
totalscore=0
for a in data:
    mychoice=a[2]
    opponent=a[0]
    score=rps(opponent,mychoice)
    totalscore+=score
    

print('Part 1 solution is',totalscore)
    
# part 2
totalscore=0
for a in data:
    mychoice=rps_winlose(a[0],a[2])
    opponent=a[0]
    score=rps(opponent,mychoice)
    totalscore+=score

print('Part 2 solution is',totalscore)
