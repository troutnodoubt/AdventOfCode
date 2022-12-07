import re
p=re.compile('([0-9]+)')
# fname="day_18_example.txt"
# fname="input_day18.txt"
# with open(fname) as fp: data = fp.read().splitlines()

# check for level 4s
# if 4s explode
# back to start
# if no level 4s check for 10s
# split
# back to start
fname="day_18_example.txt"
fname="input_day18.txt"
with open(fname) as fp: data = fp.read().splitlines()




def findfours(snailfish):
    countleft=0
    pos=0
    for a in snailfish:
        if a=='[': countleft+=1
        if a==']': countleft+=-1
        if countleft==5: return(pos)
        pos+=1
    #return(0)
def explode(snailfish,pos):
    if pos==0: return
    leftpart=snailfish[:pos]
    rightpart=snailfish[pos:]
    #print(snailfish)
    #print(leftpart)
    #print(rightpart)
    leftlist=re.split(p,leftpart)
    rightlist=re.split(p,rightpart)
    #print('leftlist',leftlist)
    # print('rightlist',rightlist)
    if len(leftlist)>1:
        leftlist[-2]=str(int(leftlist[-2])+int(rightlist[1]))
    if len(rightlist)>5:
        rightlist[5]=str(int(rightlist[5])+int(rightlist[3]))
    #print('newleftlist',leftlist)
    #print('newrightlist',rightlist)
    newlist=''
    for i in leftlist:
        newlist=newlist+i
    newlist=newlist+'0'
    if len(rightlist)>5:
        newlist=newlist+','
        if rightlist[4]!='],': newlist=newlist+rightlist[4][1:]
    for i in rightlist[5:]:
        newlist=newlist+i
    if len(rightlist)<=5: newlist=newlist+rightlist[-1][1:]
    #print(newlist)
    newlist=re.sub(',]',']',newlist)
    newlist=re.sub(',,',',',newlist)
    return(newlist)
    
def check10s(snailfish):
    return(re.search('[0-9]{2,}',snailfish))

def splitfish(snailfish,number):
    left=int(number)//2
    right=int(number)-left
    newstring='['+str(left)+','+str(right)+']'
    return(re.sub(number,newstring,snailfish,count=1))

def checkfishsum(snailfish):
    #sumlist=list()
    while True:
        pair=re.search('\[([0-9]+),([0-9]+)]',snailfish)
        if not pair: break
        left=int(pair.group(1))
        right=int(pair.group(2))
        newsum=3*left+2*right
        # print(snailfish,pair.group())
        # print(left,right,newsum)
        toreplace='\['+str(left)+','+str(right)+']'
        snailfish=re.sub(toreplace,str(newsum),snailfish)
        # print(snailfish)
        #break
    #sumlist=eval(snailfish)
    return snailfish

# example='[[[[[9,8],1],2],3],4]'
# # example='[7,[6,[5,[4,[3,2]]]]]'
# # example='[[6,[5,[4,[3,2]]]],1]'
# example='[[3,[2,[1,[7,3]]]],[6,[5,[4,[3,2]]]]]'
# # example='[[3,[2,[8,0]]],[9,[5,[4,[3,2]]]]]'
# #example='[7,2]'
# example='[[[[[4,3],4],4],[7,[[8,4],9]]],[1,1]]'

# print(example)
# a=findfours(example)
# #if a: print(example[a:a+5])
# if a: print(explode(example,a))
# example=explode(example,a)
# a=findfours(example)
# #if a: print(example[a:a+5])
# if a: print(explode(example,a))
# example=explode(example,a)
# b=check10s(example)
# if b: print(b)
# c=splitfish(example,b.group())
# if c: print(c)

numbers=''
rowcount=0
for row in data:
    if rowcount==0:
        numbers=row
        rowcount=1
    else:
        numbers='['+numbers+','+row+']'
    while True: #reduce numbers
        #print(numbers)
        a=findfours(numbers)
        if a: 
            #print('explode',numbers[a:a+5])
            numbers=explode(numbers,a)
            continue
        b=check10s(numbers)
        if b:
            #print('split',b.group())
            numbers=splitfish(numbers,b.group())
        if not b: break
#print(numbers)

a=checkfishsum(numbers)
print('Part 1 solution is', a)


amax=0
for i in range(len(data)):
    for j in range(len(data)):
        if i!=j:
            numbers='['+data[i]+','+data[j]+']'
            while True: #reduce numbers
                #print(numbers)
                a=findfours(numbers)
                if a: 
                    #print('explode',numbers[a:a+5])
                    numbers=explode(numbers,a)
                    continue
                b=check10s(numbers)
                if b:
                    #print('split',b.group())
                    numbers=splitfish(numbers,b.group())
                if not b: break
            c=checkfishsum(numbers)
            if int(c)>amax: amax=int(c)
print('Part 2 solution is', amax)
