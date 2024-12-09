fname="C://Users/Mark/Documents/Advent of Code/2020/day_13_example.txt"
fname="C://Users/Mark/Documents/Advent of Code/2020/input_day13.txt"
with open(fname) as fp: schedule = fp.read().splitlines()

starttime=int(schedule[0])

BusID=[]
increment=[]
xcount=0
for ID in schedule[1].split(','):
    #print(ID)
    if ID=='x':
        xcount=xcount+1
    elif ID!='x':
        BusID.append(int(ID))
        increment.append(xcount+1)
        xcount=0
    


ncycles=int(starttime/min(BusID))+2
times=[]
for cycles in range(ncycles):
    times.append([cycles*ID for ID in BusID])

waittime=100000000
rownum=0
for row in times:
    column=0
    for entry in row:
        if entry>=starttime:
            newwaittime=entry-starttime
            if newwaittime<waittime:
                waittime=newwaittime
                bestbus=BusID[column]
        column=column+1
    rownum=rownum+1
    
print('Part 1 solution is',waittime*bestbus)

# def findpattern(BusID,increment,m,starttime):
#     patternFound=False

#     multprev=int(starttime/BusID[m-1])
    
#     while not patternFound:
#         if (increment[m]+BusID[m-1]*multprev)%BusID[m]==0:
#            mult=int((increment[m]+BusID[m-1]*multprev)/BusID[m])
#            #print(BusID[m-1],BusID[m],multprev,mult,BusID[m-1]*multprev,BusID[m]*mult)
#            patternFound=True
#         if patternFound: return(multprev,mult)
#         multprev=multprev+1

# def findpatterngen(BusID,increment,n,m,starttime):
#     patternFound=False
#     multprev=int(starttime/BusID[n])
    
#     while not patternFound:
#         if (sum(increment[n+1:m+1])+BusID[n]*multprev)%BusID[m]==0:
#            mult=int((sum(increment[n+1:m+1])+BusID[n]*multprev)/BusID[m])
#            #print(BusID[m-1],BusID[m],multprev,mult,BusID[m-1]*multprev,BusID[m]*mult)
#            patternFound=True
#         if patternFound: return(multprev,mult)
#         multprev=multprev+1
        
# def findpatterntwonums(num1,num2,increment,n,m,starttime):
#     patternFound=False
#     multprev=int(starttime/BusID[n])
    
#     while not patternFound:
#         if (sum(increment[n+1:m+1])+BusID[n]*multprev)%BusID[m]==0:
#            mult=int((sum(increment[n+1:m+1])+BusID[n]*multprev)/BusID[m])
#            #print(BusID[m-1],BusID[m],multprev,mult,BusID[m-1]*multprev,BusID[m]*mult)
#            patternFound=True
#         if patternFound: return(multprev,mult)
#         multprev=multprev+1

##m=1
##multprev,mult=findpattern(BusID,increment,m,0)
##print(multprev*BusID[m-1],mult*BusID[m])
##candidatetime=mult*BusID[m]
# candidatetime=100000000000000
# solved=False
# count=0
# candidatetime=107374373391494
# candidatetime=109449922237008
# candidatetime=110263877204285
# candidatetime=114257352402836
# candidatetime=117436220384505
# candidatetime=123681024020941
# candidatetime=132999795105142
# candidatetime=146837786341676

# candidatetime=0

##multprev,mult=findpattern(BusID,increment,4,candidatetime)
##print(multprev,mult)
##n=0
##m=4
##multprev,mult=findpatterngen(BusID,increment,n,m,candidatetime)
##print(multprev,mult)
##print(BusID[n],BusID[m],multprev,mult,BusID[n]*multprev,BusID[m]*mult)
##print(sum(increment[n+1:m+1]))

# =============================================================================
# while not solved:
#     incrementcheck=[]
#     candidatetimevectors=[]
#     for m in range(1,len(BusID)):
#         multprev,mult=findpattern(BusID,increment,m,candidatetime)
#         #print(candidatetime)
#         #print(multprev*BusID[m-1],mult*BusID[m])
#         oldcandidatetime=candidatetime
#         candidatetime=mult*BusID[m]
#         #candidatetimevectors.append(candidatetime)
#         #print(mult*BusID[m]-oldcandidatetime)
#         incrementcheck.append(mult*BusID[m]-oldcandidatetime)
#         #print(incrementcheck)
#     #if incrementcheck==[0]*(len(BusID)-1):
#     if incrementcheck[1:]==increment[2:]:
#         solved=True
#         print('Part 2 solution is',candidatetime-sum(increment[1:]))
#     else:
#         #count=int(mult*BusID[m]/BusID[1])
#         for n1 in range(len(BusID)):
#                for n2 in range(len(BusID)):
#                    if n2>n1:
#                       multprev,mult=findpatterngen(BusID,increment,n1,n2,candidatetime)
#                       candidatetimevectors.append(mult*BusID[n2])
#         count=int(max(candidatetimevectors)/BusID[0])
#         candidatetime=count*BusID[0]
#     if candidatetime>100000000000000*10:
#         print('Timeout exceeded')
#         break
#     
# ##    if oldcandidatetime!=multprev*BusID[m-1]:
# ##        m=1
# ##        candidatetime=candidatetime+BusID[1]
# =============================================================================

    


candidatetime=0
step=1
increment[0]=0

for m in range(1,len(BusID)):
    step*=BusID[m-1]
    while (candidatetime+sum(increment[:m+1]))%BusID[m]!=0:
        candidatetime+=step
  

print('Part 2 solution is',candidatetime)




        
