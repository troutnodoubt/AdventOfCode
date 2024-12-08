fname=open("C://Users/Mark/Documents/Advent of Code/2020/day_6_example.txt")
fname=open("C://Users/Mark/Documents/Advent of Code/2020/input_day6.txt")
rawforms = fname.readlines()
fname.close()

forms=list(rawforms)
forms.append('\n')
count=0
countall=0
family=[]
word=''
for entry in forms:
    a=entry.split()
    if a:
        family.append(a)
        #word=word+a
    if not a:
        for m in family:
            word=word+m[0]
            #print(m[0])
        #print(word)
        #print(family)
        #print('New family')
        for letter in 'abcdefghijklmnopqrstuvwxyz':
            if letter in word:
                count=count+1
                countall=countall+1
        #print(count)
        family.clear()
        word=''
        count=0
        
print('Part one solution is',countall)


count=0
countall=0
family=[]
cleanlist=[]
truecount=0
for entry in forms:
    a=entry.split()
    if a:
        family.append(a)
        #word=word+a
    if not a:
        #print(family)
        #print(len(family))
        for entry in family:
            #print(entry[0])
            cleanlist.append(entry[0])
        #print(cleanlist)
        #print('New family')
        
        for letter in 'abcdefghijklmnopqrstuvwxyz':
            for word in cleanlist:
                if letter in word:
                    truecount=truecount+1
            if truecount==len(cleanlist):
                count=count+1
            truecount=0
        #print(count)
        family.clear()
        cleanlist.clear()
print('Part two solution is',count)
