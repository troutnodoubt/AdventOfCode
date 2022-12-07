fname="C://Users/Mark/Documents/Advent of Code/2021/day_4_example.txt"
fname="C://Users/Mark/Documents/Advent of Code/2021/input_day4.txt"
with open(fname) as fp: data = fp.read().splitlines()
        
order=data[0]
order=[int(a) for a in order.split(',')]

data.pop(0)
data.pop(0)

allboards=list()
board=list()

for row in data:
    if row=='':
        allboards.append(board)
        board=list()
    else:
        board.append([int(a) for a in row.split()])

solved=[[[0 for entry in row] for row in board] for board in allboards]

nobingo=True
callidx=0
winner=list()
while nobingo:
    for nboard in range(0,len(allboards)):
        for nrow in range(0,5):
            for nentry in range(0,5):
                #print(order[callidx],allboards[nboard][nrow][nentry])
                if order[callidx]==allboards[nboard][nrow][nentry]:
                    solved[nboard][nrow][nentry]=1
    for nboard in range(0,len(allboards)):
        for nrow in range(0,5):
            rowsum=0
            for nentry in range(0,5):
                rowsum+=solved[nboard][nrow][nentry]
                if rowsum==5:
                    nobingo=False
                    for i in range(0,5):
                        winner.append(allboards[nboard][nrow][i])
                    winboard=nboard
                    break
    for nboard in range(0,len(allboards)):
        for nentry in range(0,5):
            colsum=0
            for nrow in range(0,5):
                colsum+=solved[nboard][nrow][nentry]
                if colsum==5:
                    nobingo=False
                    for i in range(0,5):
                        winner.append(allboards[nboard][i][nentry])
                    winboard=nboard
                    break
                    
                
    #print(solved)
    lastcalled=order[callidx]
    callidx+=1

sumuncalled=0
nrow=0
nentry=0
for row in solved[winboard]:
    nentry=0
    for entry in row:
        if entry==0:
            sumuncalled+=allboards[winboard][nrow][nentry]
        nentry+=1
    nrow+=1


print('Part 1 solution is', lastcalled*sumuncalled ) 


#Part 2, find last board to win

def delete_multiple_element(list_object, indices):
    indices = sorted(indices, reverse=True)
    for idx in indices:
        if idx < len(list_object):
            list_object.pop(idx)


solved=[[[0 for entry in row] for row in board] for board in allboards]

callidx=0
while len(allboards)>1:

    nobingo=True
   
    while nobingo:
        winboard=list()
        for nboard in range(0,len(allboards)):
            for nrow in range(0,5):
                for nentry in range(0,5):
                    #print(order[callidx],allboards[nboard][nrow][nentry])
                    if order[callidx]==allboards[nboard][nrow][nentry]:
                        solved[nboard][nrow][nentry]=1
        for nboard in range(0,len(allboards)):
            for nrow in range(0,5):
                rowsum=0
                for nentry in range(0,5):
                    rowsum+=solved[nboard][nrow][nentry]
                    if rowsum==5:
                        nobingo=False
                        
                        winboard.append(nboard)
                        
        for nboard in range(0,len(allboards)):
            for nentry in range(0,5):
                colsum=0
                for nrow in range(0,5):
                    colsum+=solved[nboard][nrow][nentry]
                    if colsum==5:
                        nobingo=False
                        
                        winboard.append(nboard)
                        
                        
                    
        #print(solved)
        lastcalled=order[callidx]
       
        callidx+=1
    # for n in winboard:
    #     print('Board',n,'wins on call',lastcalled)
    delete_multiple_element(allboards,winboard)
    delete_multiple_element(solved,winboard)
    
nobingo=True
#print(allboards)
#print(solved)

   
while nobingo:
    for nboard in range(0,len(allboards)):
        for nrow in range(0,5):
            for nentry in range(0,5):
                #print(order[callidx],allboards[nboard][nrow][nentry])
                if order[callidx]==allboards[nboard][nrow][nentry]:
                    solved[nboard][nrow][nentry]=1
    for nboard in range(0,len(allboards)):
        for nrow in range(0,5):
            rowsum=0
            for nentry in range(0,5):
                rowsum+=solved[nboard][nrow][nentry]
                if rowsum==5:
                    nobingo=False
                    
                    winboard=nboard
                    break
    for nboard in range(0,len(allboards)):
        for nentry in range(0,5):
            colsum=0
            for nrow in range(0,5):
                colsum+=solved[nboard][nrow][nentry]
                if colsum==5:
                    nobingo=False
                    
                    winboard=nboard
                    break  
    lastcalled=order[callidx]
       
    callidx+=1
    

sumuncalled=0
nrow=0
nentry=0
for row in solved[winboard]:
    nentry=0
    for entry in row:
        if entry==0:
            sumuncalled+=allboards[winboard][nrow][nentry]
        nentry+=1
    nrow+=1


print('Part 2 solution is', lastcalled*sumuncalled )     