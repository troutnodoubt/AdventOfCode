
def parse_ticket(ticket):
    rows=range(128)
    ticketrows=ticket[:7]
    ticketseats=ticket[-3:]
    newrows=rows
    for letter in ticketrows:
        if letter=='F':
            newrows=newrows[:int(len(newrows)/2)]
            #print('F, new range is',newrows)
        if letter=='B':
            newrows=newrows[-(int(len(newrows)/2)):]
            #print('B, new range is',newrows)
    if len(newrows)==1:
        row=newrows[0]
    else:
        print('Something went wrong with the row calculation')
    newseats=ticketseats
    newseats=range(8)
    for letter in ticketseats:
        if letter=='L':
            newseats=newseats[:int(len(newseats)/2)]
            #print('F, new range is',newrows)
        if letter=='R':
            newseats=newseats[-(int(len(newseats)/2)):]
            #print('B, new range is',newrows)
    if len(newseats)==1:
        seat=newseats[0]
    else:
        print('Something went wrong with the seat calculation')
    ID=row*8+seat
    result=(row,seat,ID)
    return result


tickets=('FBFBBFFRLR','BFFFBBFRRR','FFFBBBFRRR','BBFFBBFRLL')

fname="C://Users/Mark/Documents/Advent of Code/2020/input_day5.txt"
with open(fname) as fp: tickets = fp.read().splitlines()


maxID=0
ticketID=[]
for ticket in tickets:
    result=parse_ticket(ticket)
    ticketID.append(result[2])
##    if ticketID>maxID:
##        maxID=ticketID
maxID=max(ticketID)
print('Part 1 solution is',maxID)
alltickets=[]
for row in range(128):
    for seat in range(8):
        alltickets.append(row*8+seat)
emptyseat=[]
for m in alltickets:
    if m not in ticketID:
        emptyseat.append(m)
for m in emptyseat:
    if m-1 in ticketID and m+1 in ticketID:
        print('Part 2 solution is',m)
    
