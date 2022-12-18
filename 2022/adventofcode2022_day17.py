fname="day17_example.txt"
#fname="input_day17.txt"
with open(fname) as fp: data = fp.read().splitlines()


class shape:
    def __init__(self,name,position,occupiednodes):
        self.name=name
        self.position=position
        self.occupiednodes # nodes which if occupied indicate that the shape is at a limit
                
    # def hitright(self): 
    #     return # need to define 
    
    # def hitleft(self):
    #     return # need to define 
    
    # def hitbottom(self):
    #     return # need to define 
    
    def collisionifmoved(self): # replace individual hit functions
        return # need to define
    
    def moveright(self): 
        return # need to define 
    
    def moveleft(self):
        return # need to define 
    
    def movedown(self):
        return # need to define
    
    def spawn(self): # place new block in appropriate spot
        return # need to define
    
    def petrify(self): # block becomes part of structure for next round
        return #

jetseq=data[0]
jetout=''

for i in range(2*len(jetseq)):
    jet=jetseq[i%len(jetseq)]
    jetout+=jet
    

# algorithm
# for number of drops
    # initiate floor - previous round + empty space above, 
                     # will likely need to limit size of the memory for part 2, 
                     # but need to recall all levels unless there's a complete 
                     # blockage somewhere
    # initiate shape at top
    # while not fixed
        # jet - check for collisions and allow if not
        # drop - check for collisions and allow if not, otherwise petrify
            # if petrified then destroy object
