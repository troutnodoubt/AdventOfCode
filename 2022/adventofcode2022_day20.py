fname="day20_example.txt"
fname="input_day20.txt"
with open(fname) as fp: data = fp.read().splitlines()

def decrypt(multiplier,nsorts):
    class card:
        def __init__(self,val):
            self.val=val
          
    originalcards=tuple(card(int(a)*multiplier) for a in data)
    workingcards=list(originalcards)
    mod=len(originalcards)
        
    for i in range(nsorts):
        for card in originalcards:
            n=card.val
            oldidx=workingcards.index(card)
            newidx=(oldidx+n)%(mod-1)         
            workingcards.remove(card)
            workingcards.insert(newidx,card)
        
    # find card with val 0
    for card in originalcards:
        if card.val==0:
            zerocard=card
            break
    
    zeroidx=workingcards.index(zerocard)
    onethou=workingcards[(zeroidx+1000)%(mod)].val
    twothou=workingcards[(zeroidx+2000)%(mod)].val
    threethou=workingcards[(zeroidx+3000)%(mod)].val
    return(onethou+twothou+threethou)

print('Part 1 solution is',decrypt(1,1))
print('Part 2 solution is',decrypt(811589153,10))
