# Solve puzzle

# identify all possible moves
# for each amphipod
#   find paths to open nodes
#   if path is open, move to node, add cost
#       recursion



def bfs_shortest_path(graph, start, goal):
    # keep track of explored nodes
    explored = []
    # keep track of all the paths to be checked
    queue = [[start]]
 
    # return path if start is goal
    if start == goal:
        return "That was easy! Start = goal"
 
    # keeps looping until all possible paths have been checked
    while queue:
        # pop the first path from the queue
        path = queue.pop(0)
        # get the last node from the path
        node = path[-1]
        if node not in explored:
            neighbours = graph[node]
            # go through all neighbour nodes, construct a new path and
            # push it into the queue
            for neighbour in neighbours:
                new_path = list(path)
                new_path.append(neighbour)
                queue.append(new_path)
                # return path if neighbour is goal
                if neighbour == goal:
                    return new_path
 
            # mark node as explored
            explored.append(node)
 
    # in case there's no path between the 2 nodes
    #return "So sorry, but a connecting path doesn't exist :("

def move_amphipods(amphipods,grid):
    print('newcall')
    for critter in amphipods.keys():
        #print(critter)
        occupied=[entry[0] for entry in amphipods.values()]
        available=set(grid.keys())-set(occupied)
        available=available.intersection(set(amphipods[critter][2]))
        openwells=openwell(amphipods)
        #print(available)
        if amphipods[critter][0][0]=='Q':
            if openwells[critter[0]]:
                available=available.intersection(set(amphipods[critter][2][-4:]))
            else:
                available=available.intersection(set())
        #print(available)
        if amphipods[critter][0][0]=='W':
            if amphipods[critter][0][1]==critter[0] and openwells[critter[0]]:
                available=available.intersection(set())
            else:
                available=available.intersection(set(amphipods[critter][2][:-4]))
            # if not available:
        #     print('no open spaces, game over')
        # print(critter,available,occupied)
        for space in available:
            path=bfs_shortest_path(grid, amphipods[critter][0], space)
            pathset=set(path[1:])
            #print(path)
            clearpath=True
            if pathset.intersection(set(occupied)): clearpath=False
            if path and clearpath: #move along
                tempentry=amphipods[critter]
                amphipods[critter]=[space,len(path[1:])*tempentry[3],tempentry[2],tempentry[3]]
                print('amphipod',critter,'moved from',path[0],'to',space,'through path',path[1:])
                move_amphipods(amphipods, grid)   
                if amphipods:
                    return(amphipods)

def checkforsuccess(amphipods):
    check=list()
    for entry in amphipods.items():
        #print(entry[0][0],entry[1][0][1],entry[0][0]==entry[1][0][1])
        check.append(entry[0][0]==entry[1][0][1])
    if all(check):
        print('Solution Found!')
        return True

def openwell(amphipods):
    openwells={'A':True,
               'B':True,
               'C':True,
               'D':True}
    for letter in ['A','B','C','D']:   
        for critter in amphipods.keys():
            # print(letter,critter[0],amphipods[critter][0][1])
            if critter[0]!=letter and amphipods[critter][0][1]==letter:
                openwells[letter]=False
    return(openwells)
        
        

grid={'Q0':['Q1'],
      'Q1':['Q2','Q0'],
      'Q2':['Q1','Q3','WA3'],
      'Q3':['Q2','Q4'],
      'Q4':['Q3','Q5','WB3'],
      'Q5':['Q4','Q6'],
      'Q6':['Q5','Q7','WC3'],
      'Q7':['Q6','Q8'],
      'Q8':['Q7','Q9','WD3'],
      'Q9':['Q8','Q10'],
      'Q10':['Q9'],
      'WA3':['Q2','WA2'],
      'WA2':['WA3','WA1'],
      'WA1':['WA2','WA0'],
      'WA0':['WA1'],
      'WB3':['Q4','WB2'],
      'WB2':['WB3','WB1'],
      'WB1':['WB2','WB0'],
      'WB0':['WB1'],
      'WC3':['Q6','WC2'],
      'WC2':['WC3','WC1'],
      'WC1':['WC2','WC0'],
      'WC0':['WC1'],
      'WD3':['Q8','WD2'],
      'WD2':['WD3','WD1'],
      'WD1':['WD2','WD0'],
      'WD0':['WD1']}

allowableA=('Q0','Q1','Q3','Q5','Q7','Q9','Q10','WA0','WA1','WA2','WA3')
allowableB=('Q0','Q1','Q3','Q5','Q7','Q9','Q10','WB0','WB1','WB2','WB3')
allowableC=('Q0','Q1','Q3','Q5','Q7','Q9','Q10','WC0','WC1','WC2','WC3')
allowableD=('Q0','Q1','Q3','Q5','Q7','Q9','Q10','WD0','WD1','WD2','WD3')

amphipods={'A1':['WA3',0,allowableA,1],
           'A2':['WC3',0,allowableA,1],
           'A3':['WD2',0,allowableA,1],
           'A4':['WC1',0,allowableA,1],
           'B1':['WD3',0,allowableB,10],
           'B2':['WC2',0,allowableB,10],
           'B3':['WB1',0,allowableB,10],
           'B4':['WA0',0,allowableB,10],
           'C1':['WB2',0,allowableC,100],
           'C2':['WD1',0,allowableC,100],
           'C3':['WB0',0,allowableC,100],
           'C4':['WD0',0,allowableC,100],
           'D1':['WB3',0,allowableD,1000],
           'D2':['WA2',0,allowableD,1000],
           'D3':['WA1',0,allowableD,1000],
           'D4':['WC0',0,allowableD,1000]
           }
turn=0
while True:
    turn+=1
    print('turn',turn)
    amphipods=move_amphipods(amphipods,grid)
# amphipods=move_amphipods(amphipods,grid)
   
 #   if checkforsuccess(amphipods): break