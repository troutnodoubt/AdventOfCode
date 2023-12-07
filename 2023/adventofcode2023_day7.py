fname='input_day7.txt'
#fname='example_day7.txt'
with open(fname) as fp: data = fp.read().splitlines()

def sortThird(val):
    return val[2] 

def determineType(jokers=False):
    for line in data:
        hand=line.split(' ')[0]
        if jokers:
            njokers=hand.count('J')
            a=set(hand.replace('J',''))
        else:
            njokers=0
            a=set(hand)
        if len(a) == 5: highCard.append(line)
        elif len(a) == 4: onePair.append(line)
        elif len(a) == 3: #either two pair or threekind
            maxrepeat=0
            for card in a:
                repeat = hand.count(card)+njokers
                if repeat>maxrepeat: maxrepeat=repeat
            if maxrepeat == 2: twoPair.append(line)
            elif maxrepeat == 3: threeKind.append(line)                
        elif len(a) == 2: #either full house or fourkind
            maxrepeat=0
            for card in a:
                repeat = hand.count(card)+njokers
                if repeat>maxrepeat: maxrepeat=repeat
            if maxrepeat == 3: fullHouse.append(line)
            elif maxrepeat == 4: fourKind.append(line)
        elif len(a) == 1 or len(a) == 0: fiveKind.append(line)
        
def sortCards(l,jokers=False):
    
    sortedCards=[]
    for line in l:
        hand=line.split(' ')[0]
        val=line.split(' ')[1]
        rankHand=[]
        for card in hand:
            if card=='A': score=14
            elif card=='K': score=13
            elif card=='Q': score=12
            elif card=='J': 
                if jokers: score=1
                else: score=11
            elif card=='T': score =10
            else: score = int(card)
            rankHand.append(score)
        bigscore=0
        for n,score in enumerate(rankHand):
            bigscore += (100**(5-n))*score
        sortedCards.append([hand,int(val),bigscore])
    sortedCards.sort(key=sortThird)
    return sortedCards

def getResult(jokers=False):
   
    determineType(jokers)
    fullsorted=[]
    for wintype in fullset:
        fullsorted.append([hand for hand in sortCards(wintype,jokers)])
    reallyfullsorted=[]
    for s in fullsorted:
        for h in s:
            if len(h)>0: reallyfullsorted.append(h)
    res=0    
    for rank,hand in enumerate(reallyfullsorted):
        res+=(rank+1)*hand[1]
    return res

highCard=[]
fiveKind=[]
fourKind=[]
fullHouse=[]
threeKind=[]
twoPair=[]
onePair=[]
fullset=[highCard,onePair,twoPair,threeKind,fullHouse,fourKind,fiveKind] 

print('Part 1', getResult())

highCard=[]
fiveKind=[]
fourKind=[]
fullHouse=[]
threeKind=[]
twoPair=[]
onePair=[]
fullset=[highCard,onePair,twoPair,threeKind,fullHouse,fourKind,fiveKind] 

print('Part 2', getResult(True))
