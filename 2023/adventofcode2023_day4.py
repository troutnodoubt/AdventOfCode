fname='input_day4.txt'
#fname='example_day4.txt'
with open(fname) as fp: data = fp.read().splitlines()

def getCount(s):
    substring = s.split(' | ')
    nums = [int(x) for x in substring[1].split(' ') if len(x)>0]
    wins = [int(x) for x in substring[0].split(' ') if len(x)>0 and x.isnumeric()]
    count=0
    for n in nums:
        if n in wins: count+=1
    return count

def scoreCard(card):
    count=cardcount[card]
    if count>0:
        return 2**(count-1)
    else:
        return 0

def addCards(cardnum, card):
    count=cardcount[card]
    for bonuscard in range(cardnum+1,cardnum+1+count): 
        cards[bonuscard]+=1 
        addCards(bonuscard, data[bonuscard])

totalscore=0
cards = {i:1 for i in range(len(data))}
cardcount={card:getCount(card) for card in data}
for cardnum, card in enumerate(data):
    totalscore+=scoreCard(card)
    addCards(cardnum, card)

print('Part 1 solution', totalscore)
print('Part 2 solution', sum([i for i in cards.values()]))
