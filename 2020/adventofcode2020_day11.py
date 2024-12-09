fname="C://Users/Mark/Documents/Advent of Code/2020/day_11_example.txt"
fname="C://Users/Mark/Documents/Advent of Code/2020/input_day11.txt"
with open(fname) as fp: layout = fp.read().splitlines()

#print(layout)



def cycleseats(layout):
    newlayout=[]
    rownum=0
    for row in layout:
        layout[rownum]=list(row)
        newlayout.append(row)
        rownum=rownum+1
    rownum=0   
    for row in newlayout:
        newlayout[rownum]=list(row)
        rownum=rownum+1



    rownum=0
    seatnum=0
    for row in layout:
        seatnum=0
        for seat in row:
            adjacentoccupied=0
            if rownum==0 and seatnum==0:
               # print('Top Left')
                if layout[rownum+1][seatnum]=='#':
                    adjacentoccupied=adjacentoccupied+1
                    #print('topleftdown')
                if layout[rownum+1][seatnum+1]=='#':
                    adjacentoccupied=adjacentoccupied+1
                    #print('topleftdownright')
                if layout[rownum][seatnum+1]=='#':
                    adjacentoccupied=adjacentoccupied+1
                    #print('topleftright')
                #print('Top left count',adjacentoccupied)
            elif rownum==0 and seatnum==len(row)-1:
                #print('Top Right')
                if layout[rownum+1][seatnum]=='#':
                    adjacentoccupied=adjacentoccupied+1
                    #print('toprightdown')
                if layout[rownum+1][seatnum-1]=='#':
                    adjacentoccupied=adjacentoccupied+1
                    #print('toprightdownleft')
                if layout[rownum][seatnum-1]=='#':
                    adjacentoccupied=adjacentoccupied+1
                    #print('toprightleft')
                #print('Top Right count',adjacentoccupied)
            elif rownum==len(layout)-1 and seatnum==0:
                #print('Bottom Left')
                if layout[rownum-1][seatnum]=='#':
                    adjacentoccupied=adjacentoccupied+1
                if layout[rownum-1][seatnum+1]=='#':
                    adjacentoccupied=adjacentoccupied+1
                if layout[rownum][seatnum+1]=='#':
                    adjacentoccupied=adjacentoccupied+1
                #print('Bottom left count',adjacentoccupied)
            elif rownum==len(layout)-1 and seatnum==len(row)-1:
                #print('Bottom Right')
                if layout[rownum-1][seatnum]=='#':
                    adjacentoccupied=adjacentoccupied+1
                if layout[rownum-1][seatnum-1]=='#':
                    adjacentoccupied=adjacentoccupied+1
                if layout[rownum][seatnum-1]=='#':
                    adjacentoccupied=adjacentoccupied+1
                #print('Bottom right count',adjacentoccupied)
            elif rownum==0 and (seatnum!=0 or seatnum!=len(row)-1):
                #print('Top Row')
                if layout[rownum][seatnum-1]=='#':
                    adjacentoccupied=adjacentoccupied+1
                if layout[rownum][seatnum+1]=='#':
                    adjacentoccupied=adjacentoccupied+1
                if layout[rownum+1][seatnum-1]=='#':
                    adjacentoccupied=adjacentoccupied+1
                if layout[rownum+1][seatnum]=='#':
                    adjacentoccupied=adjacentoccupied+1
                if layout[rownum+1][seatnum+1]=='#':
                    adjacentoccupied=adjacentoccupied+1
                #print('Top row count',adjacentoccupied)
            elif rownum==len(layout)-1 and (seatnum!=0 or seatnum!=len(row)-1):
                #print('Bottom Row')
                if layout[rownum][seatnum-1]=='#':
                    adjacentoccupied=adjacentoccupied+1
                if layout[rownum][seatnum+1]=='#':
                    adjacentoccupied=adjacentoccupied+1
                if layout[rownum-1][seatnum-1]=='#':
                    adjacentoccupied=adjacentoccupied+1
                if layout[rownum-1][seatnum]=='#':
                    adjacentoccupied=adjacentoccupied+1
                if layout[rownum-1][seatnum+1]=='#':
                    adjacentoccupied=adjacentoccupied+1
                #print('Bottom row count',adjacentoccupied)
            elif (rownum!=len(layout)-1 or rownum!=0) and seatnum==0:
                #print('Left Column')
                if layout[rownum-1][seatnum]=='#':
                    adjacentoccupied=adjacentoccupied+1
                if layout[rownum-1][seatnum+1]=='#':
                    adjacentoccupied=adjacentoccupied+1
                if layout[rownum][seatnum+1]=='#':
                    adjacentoccupied=adjacentoccupied+1
                if layout[rownum+1][seatnum]=='#':
                    adjacentoccupied=adjacentoccupied+1
                if layout[rownum+1][seatnum+1]=='#':
                    adjacentoccupied=adjacentoccupied+1
                #print('Left Column count',adjacentoccupied)
            elif (rownum!=len(layout)-1 or rownum!=0) and seatnum==len(row)-1:
                #print('Right Column')
                if layout[rownum-1][seatnum]=='#':
                    adjacentoccupied=adjacentoccupied+1
                if layout[rownum-1][seatnum-1]=='#':
                    adjacentoccupied=adjacentoccupied+1
                if layout[rownum][seatnum-1]=='#':
                    adjacentoccupied=adjacentoccupied+1
                if layout[rownum+1][seatnum]=='#':
                    adjacentoccupied=adjacentoccupied+1
                if layout[rownum+1][seatnum-1]=='#':
                    adjacentoccupied=adjacentoccupied+1
                #print('Right Column count',adjacentoccupied)
            
            else:
                #print('Center')
                if layout[rownum-1][seatnum-1]=='#':
                    adjacentoccupied=adjacentoccupied+1
                if layout[rownum-1][seatnum]=='#':
                    adjacentoccupied=adjacentoccupied+1
                if layout[rownum-1][seatnum+1]=='#':
                    adjacentoccupied=adjacentoccupied+1
                if layout[rownum][seatnum-1]=='#':
                    adjacentoccupied=adjacentoccupied+1
                if layout[rownum][seatnum+1]=='#':
                    adjacentoccupied=adjacentoccupied+1
                if layout[rownum+1][seatnum-1]=='#':
                    adjacentoccupied=adjacentoccupied+1
                if layout[rownum+1][seatnum]=='#':
                    adjacentoccupied=adjacentoccupied+1
                if layout[rownum+1][seatnum+1]=='#':
                    adjacentoccupied=adjacentoccupied+1
                #print('Center count',adjacentoccupied)
            if adjacentoccupied==0 and layout[rownum][seatnum]=='L':
                newlayout[rownum][seatnum]='#'
            if adjacentoccupied>=4 and layout[rownum][seatnum]=='#':
                newlayout[rownum][seatnum]='L'
                
            seatnum=seatnum+1
        rownum=rownum+1
    if layout==newlayout:
        changed=False
    else:
        changed=True

    return(newlayout,changed)
    





def findseatsleft(layout,rownum,seatnum):
    #left direction
    sublist=layout[rownum][:seatnum]
    #print(sublist)
    occupied=False
    mseat=[]
    for m in range(len(sublist)):
        if sublist[m]=='#':
            occupied=True
            mseat=m
        elif sublist[m]=='L':
            occupied=False
            mseat=m
    return(occupied,mseat)
        
def findseatsright(layout,rownum,seatnum):
    #left direction
    sublist=layout[rownum][:seatnum:-1]
    #print(sublist)
    occupied=False
    mseat=[]
    for m in range(len(sublist)):
        if sublist[m]=='#':
            occupied=True
            mseat=len(sublist)-m-1
        elif sublist[m]=='L':
            occupied=False
            mseat=len(sublist)-m-1
    return(occupied,mseat)

def columnvector(layout,seatnum):
    column=[]
    for m in range(len(layout)):
        column.append(layout[m][seatnum])
    return(column)

def diagvectorpos(layout,rownum,seatnum):
    vector=[]
    startoffset=min(len(layout)-rownum-1,seatnum)
    #print(startoffset)
    endoffset=min(rownum,len(row)-seatnum-1)
    #print(endoffset)
    for m in range(startoffset+endoffset+1):
        vector.append(layout[rownum+startoffset-m][seatnum-startoffset+m])
    return(vector,startoffset)

def diagvectorneg(layout,rownum,seatnum):
    vector=[]
    startoffset=min(rownum,seatnum)
    #print(startoffset)
    endoffset=min(len(layout)-rownum-1,len(row)-seatnum-1)
    #print(endoffset)
    for m in range(startoffset+endoffset+1):
        vector.append(layout[rownum-startoffset+m][seatnum-startoffset+m])
    return(vector,startoffset)


def findseatsup(layout,rownum,seatnum):
    #left direction
    sublist=columnvector(layout,seatnum)[:rownum]
    #print(sublist)
    occupied=False
    mseat=[]
    for m in range(len(sublist)):
        if sublist[m]=='#':
            occupied=True
            mseat=m
        elif sublist[m]=='L':
            occupied=False
            mseat=m
    return(occupied,mseat)

def findseatsdown(layout,rownum,seatnum):
    #left direction
    sublist=columnvector(layout,seatnum)[:rownum:-1]
    #print(sublist)
    occupied=False
    mseat=[]
    for m in range(len(sublist)):
        if sublist[m]=='#':
            occupied=True
            mseat=len(sublist)-m-1
        elif sublist[m]=='L':
            occupied=False
            mseat=len(sublist)-m-1
    return(occupied,mseat)

def findseatsdownleft(layout,rownum,seatnum):
    #left direction
    sublist,startoffset=diagvectorpos(layout,rownum,seatnum)
    sublist=sublist[:startoffset]
    #print(sublist)
    occupied=False
    mseat=[]
    for m in range(len(sublist)):
        if sublist[m]=='#':
            occupied=True
            mseat=m
        elif sublist[m]=='L':
            occupied=False
            mseat=m
    return(occupied,mseat)

def findseatsupright(layout,rownum,seatnum):
    #left direction
    sublist,startoffset=diagvectorpos(layout,rownum,seatnum)
    sublist=sublist[:startoffset:-1]
    #print(sublist)
    occupied=False
    mseat=[]
    for m in range(len(sublist)):
        if sublist[m]=='#':
            occupied=True
            mseat=len(sublist)-m-1
        elif sublist[m]=='L':
            occupied=False
            mseat=len(sublist)-m-1
    return(occupied,mseat)

def findseatsupleft(layout,rownum,seatnum):
    #left direction
    sublist,startoffset=diagvectorneg(layout,rownum,seatnum)
    sublist=sublist[:startoffset]
    #print(sublist)
    occupied=False
    mseat=[]
    for m in range(len(sublist)):
        if sublist[m]=='#':
            occupied=True
            mseat=m
        elif sublist[m]=='L':
            occupied=False
            mseat=m
    return(occupied,mseat)

def findseatsdownright(layout,rownum,seatnum):
    #left direction
    sublist,startoffset=diagvectorneg(layout,rownum,seatnum)
    sublist=sublist[:startoffset:-1]
    #print(sublist)
    occupied=False
    mseat=[]
    for m in range(len(sublist)):
        if sublist[m]=='#':
            occupied=True
            mseat=len(sublist)-m-1
        elif sublist[m]=='L':
            occupied=False
            mseat=len(sublist)-m-1
    return(occupied,mseat)

def cycleseats2(layout):
    newlayout=[]
    rownum=0
    for row in layout:
        layout[rownum]=list(row)
        newlayout.append(row)
        rownum=rownum+1
    rownum=0   
    for row in newlayout:
        newlayout[rownum]=list(row)
        rownum=rownum+1



    rownum=0
    seatnum=0
    for row in layout:
        seatnum=0
        for seat in row:
            adjacentoccupied=0
            #print(rownum,seatnum)
            occupied,m=findseatsdown(layout,rownum,seatnum)
            #print('Down occupied',occupied)
            if occupied: adjacentoccupied=adjacentoccupied+1
            occupied,m=findseatsup(layout,rownum,seatnum)
            #print('Up occupied',occupied)
            if occupied: adjacentoccupied=adjacentoccupied+1
            occupied,m=findseatsleft(layout,rownum,seatnum)
            #print('Left occupied',occupied)
            if occupied: adjacentoccupied=adjacentoccupied+1
            occupied,m=findseatsright(layout,rownum,seatnum)
            #print('Right occupied',occupied)
            if occupied: adjacentoccupied=adjacentoccupied+1
            occupied,m=findseatsupright(layout,rownum,seatnum)
            #print('Upright occupied',occupied)
            if occupied: adjacentoccupied=adjacentoccupied+1
            occupied,m=findseatsdownright(layout,rownum,seatnum)
            #print('Downright occupied',occupied)
            if occupied: adjacentoccupied=adjacentoccupied+1
            occupied,m=findseatsupleft(layout,rownum,seatnum)
            #print('Upleft occupied',occupied)
            if occupied: adjacentoccupied=adjacentoccupied+1
            occupied,m=findseatsdownleft(layout,rownum,seatnum)
            #print('Downleft occupied',occupied)
            if occupied: adjacentoccupied=adjacentoccupied+1
            #print('Adjacent occupied',adjacentoccupied)
            if adjacentoccupied==0 and layout[rownum][seatnum]=='L':
                newlayout[rownum][seatnum]='#'
            if adjacentoccupied>=5 and layout[rownum][seatnum]=='#':
                newlayout[rownum][seatnum]='L'
            seatnum=seatnum+1
        rownum=rownum+1
    if layout==newlayout:
        changed=False
    else:
        changed=True

    return(newlayout,changed)





newlayout,changed=cycleseats(layout)
#print(newlayout)
#print(changed)
while changed:
    newlayout,changed=cycleseats(newlayout)
    #print(newlayout)
    #print(changed)

taken=0
for row in newlayout:
    taken=taken+row.count('#')
print('Part 1 solution is',taken)
##
##for row in layout:
##    print(row)

newlayout,changed=cycleseats2(layout)
#print(newlayout)
##print(changed)
##print('New layout')
##for row in newlayout:
##    print(row)
##print('Original layout')
##for row in layout:
##    print(row)
while changed:
    newlayout,changed=cycleseats2(newlayout)
    #print(newlayout)
##    print(changed)
##    for row in newlayout:
##        print(row)

taken=0
for row in newlayout:
    taken=taken+row.count('#')
print('Part 2 solution is',taken)

