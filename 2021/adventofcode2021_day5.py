from collections import Counter

fname="C://Users/Mark/Documents/Advent of Code/2021/day_5_example.txt"
fname="C://Users/Mark/Documents/Advent of Code/2021/input_day5.txt"
with open(fname) as fp: data = fp.read().splitlines()

a=list()
for row in data:
    a.append(row.split('->'))

begin=list()
end=list()    
for idx in range(0,len(a)):
    begin.append([int(val) for val in a[idx][0].split(',')])
    end.append([int(val) for val in a[idx][1].split(',')])

covered=list()
for idx in range(0,len(begin)):
    #print('working on',idx,'of',len(begin))
    if begin[idx][0]==end[idx][0]:
        ystart=min(begin[idx][1],end[idx][1])
        ystop=max(begin[idx][1],end[idx][1])
        x=begin[idx][0]
        for i in range(ystart,ystop+1):
            covered.append((x,i))
    if begin[idx][1]==end[idx][1]:
        xstart=min(begin[idx][0],end[idx][0])
        xstop=max(begin[idx][0],end[idx][0])
        y=begin[idx][1]
        for i in range(xstart,xstop+1):
            covered.append((i,y))


# count={}
# for i in covered:
#     #print('working on count',i)
#     count[i]=covered.count(i)
count=Counter(covered)
crosscount=0
for entry in count.values():
    if entry>1:
        crosscount+=1
        
print('Part 1 solution is', crosscount)

covered=list()
for idx in range(0,len(begin)):
    #print('working on',idx,'of',len(begin))
    if begin[idx][0]==end[idx][0]:
        ystart=min(begin[idx][1],end[idx][1])
        ystop=max(begin[idx][1],end[idx][1])
        x=begin[idx][0]
        for i in range(ystart,ystop+1):
            covered.append((x,i))
    elif begin[idx][1]==end[idx][1]:
        xstart=min(begin[idx][0],end[idx][0])
        xstop=max(begin[idx][0],end[idx][0])
        y=begin[idx][1]
        for i in range(xstart,xstop+1):
            covered.append((i,y))
    else:
        slope=(end[idx][1]-begin[idx][1])/(end[idx][0]-begin[idx][0])
        if slope==1:
            xstart=min(begin[idx][0],end[idx][0])
            xstop=max(begin[idx][0],end[idx][0])
            ystart=min(begin[idx][1],end[idx][1])
            for i in range(xstart,xstop+1):
                covered.append((i,ystart+(i-xstart)))
        if slope==-1:
            xstart=min(begin[idx][0],end[idx][0])
            xstop=max(begin[idx][0],end[idx][0])
            ystart=max(begin[idx][1],end[idx][1])
            for i in range(xstart,xstop+1):
                covered.append((i,ystart-(i-xstart)))
            
            
count=Counter(covered)

# count={}
# for i in covered:
#     #print('working on count',i)
#     count[i]=covered.count(i)
crosscount=0
for entry in count.values():
    if entry>1:
        crosscount+=1
print('Part 2 solution is', crosscount)        