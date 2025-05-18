
fname='input_day22.txt'
with open(fname) as fp: data = fp.read().splitlines()

def next(n):
    n0=n
    n<<=6
    n^=n0
    n&=((1<<24)-1)

    n0=n
    n>>=5
    n^=n0
    n&=((1<<24)-1)
    
    n0=n
    n<<=11
    n^=n0
    n&=((1<<24)-1)

    return n

new=2000
secretlist=[]
prices=[]
def findnext(n,m):
    price=[n%10]
    for _ in range(m):
        n=next(n)
        price.append(n%10)
    return n,price

# data=[1,2,3,2024]
# data=[1]
for val in data: 
    n,price=findnext(int(val),new)
    secretlist.append(n)
    prices.append(price)
print('Part 1', sum(secretlist))

pricechanges=[]
testset=set()
for price in prices:
    pricechange=[[] for _ in range(len(price))]
    pricechange[0]=99
    for i in range(1,len(price)):
        pricechange[i]=price[i]-price[i-1]
    pricechanges.append(pricechange)

sequencedict={}
for n,price in enumerate(prices):
    for i in range(1,len(price)-3):
        testsequence=pricechanges[n][i:i+4]
        a=tuple(testsequence)
        testset.add(tuple(a))

        if a not in sequencedict.keys():
            sequencedict[a]=[0]*len(prices)
            sequencedict[a][n]=price[i+3]
        elif a in sequencedict.keys():
            if sequencedict[a][n]==0:
                sequencedict[a][n]=price[i+3]

maxb=0
for val in sequencedict.values():
    test=sum(val)
    if test>maxb: maxb=test

print('Part 2',maxb)

