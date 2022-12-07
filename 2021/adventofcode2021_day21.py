import numpy as np
# fname="day_20_example.txt"
# fname="input_day20.txt"
# with open(fname) as fp: data = fp.read().splitlines()

p1=4
p2=2 #8 was the example

p1_0=p1
p2_0=p2

nturns=0
dice=0
score1=0
score2=0
nrolls=0
while True:
    for _ in range(3):
        dice+=1
        if dice>100: dice=1
        p1+=dice
        p1=p1%10
        if p1==0: p1=10
        nrolls+=1
    score1+=p1
    # print('p1',nturns,p1,score1)
    if score1>=1000: break
    for _ in range(3):
        dice+=1
        if dice>100: dice=1
        p2+=dice
        p2=p2%10
        if p2==0: p2=10
        nrolls+=1
    score2+=p2
    nturns+=1
    if score2>=1000: break
    # print('p2',nturns,p2,score2)
#print(nrolls)  
print('Part 1 solution is',min(score1,score2)*nrolls)

# Part 2 - Parallel Universes!

#possible forward movement and universes per turn generated per possibility
fwd=dict()
fwd[3]=1
fwd[4]=3
fwd[5]=6
fwd[6]=7
fwd[7]=6
fwd[8]=3
fwd[9]=1

def newpos(pos,fwd):
    pos=(pos+fwd)%10
    if pos==0: pos=10
    return(pos)

def duplicate7(data):
    newdata=list()
    for row in data:
        for _ in range(7):
            newdata.append(row.copy())
    return(newdata)

oldpos=p1_0
pos=p1_0
oldscore=0
score=0
old_n_universes=1
n_universes=1
solved_this_turn=0

# turn=[[oldpos,pos,oldscore,score,old_n_universes,n_universes,solved_this_turn]]
# history=list()
# solved=False
# cycles=0
# while not solved:
#     turn=duplicate7(turn)
#     stepforward=0
#     for row in turn:
#         row[1]=newpos(row[0],3+stepforward%7)
#         row[5]=fwd[3+stepforward%7]*row[4]
#         row[3]=row[2]+row[1]
#         if row[3]>=21 and row[2]<21:
#             row[6]=1
#         else:
#             row[6]=0
#         stepforward+=1
#     universessolved=0
#     for row in turn:
#         universessolved+=row[5]*row[6]
#     history.append(universessolved)
#     #[print(row) for row in turn]
#     #print('')
#     #history.append(turn.copy())
#     solvedvector=list()
#     for row in turn:
#         if row[3]>=21: solvedvector.append(True)
#         else: solvedvector.append(False)
#     if all(solvedvector): solved=True
#     cycles+=1
#     if cycles>8: break
#     for row in turn:
#         row[0]=row[1]
#         row[2]=row[3]
#         row[4]=row[5]
# This doesn't work because the list gets too large after 6 cycles. So close. Need to try a dictionary approach

maxscore=21
universes=dict()

# for place in range(1,10+1):
#     for score in range(maxscore+1):
#         universes[(place,score)]=0
        
# universes[(p1_0,0)]=1
# history=list()
# for _ in range(15):
#     newuniverses=dict()
#     cumsols=0
#     for key in universes.keys():
#         if universes[key]!=0 and key[1]<21:
#             for advance in range(3,10):
#                 pos=newpos(key[0],advance)
#                 score=key[1]+pos
#                 if score>21: score=21
#                 if (pos,score) in newuniverses.keys():
#                     newuniverses[(pos,score)]+=universes[key]*fwd[advance]
#                 else:
#                     newuniverses[(pos,score)]=universes[key]*fwd[advance]
    
#     for key in newuniverses:
#         if key[1]>=21: cumsols+=newuniverses[key]
#     history.append(cumsols)
#     universes=dict()
#     universes=newuniverses.copy()
#     newuniverses=dict()
# This looks like the right track, but need to simulate both a and b states
    
universes[(p1_0,0,p2_0,0)]=1
history1=list()
history2=list()

for _ in range(15):
    newuniverses=dict()
    sols1=0
    for key in universes.keys():
        if universes[key]!=0 and key[1]<21 and key[3]<21:
            for advance in range(3,10):
                pos=newpos(key[0],advance)
                score=key[1]+pos
                if score>21: 
                    score=21
                    # sols1+=universes[key]
                if (pos,score,key[2],key[3]) in newuniverses.keys():
                    newuniverses[(pos,score,key[2],key[3])]+=universes[key]*fwd[advance]
                else:
                    newuniverses[(pos,score,key[2],key[3])]=universes[key]*fwd[advance]
    
    for key in newuniverses:
        if key[1]>=21: sols1+=newuniverses[key]
           
    history1.append(sols1)
    
    
    
    universes=dict()
    universes=newuniverses.copy()
    newuniverses=dict()   
    sols2=0
    for key in universes.keys():
        if universes[key]!=0 and key[3]<21 and key[1]<21:
            for advance in range(3,10):
                pos=newpos(key[2],advance)
                score=key[3]+pos
                if score>21: score=21
                if (key[0],key[1],pos,score) in newuniverses.keys():
                    newuniverses[(key[0],key[1],pos,score)]+=universes[key]*fwd[advance]
                else:
                    newuniverses[(key[0],key[1],pos,score)]=universes[key]*fwd[advance]
    
    for key in newuniverses:
        if key[3]>=21: sols2+=newuniverses[key]
    history2.append(sols2)
    
    
    
    universes=dict()
    universes=newuniverses.copy()

print('Part 2 solution is',max(sum(history1),sum(history2)))