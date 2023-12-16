
fname='input_day16.txt'
# fname='example_day16.txt'

with open(fname) as fp: data = fp.read().splitlines()

class Photon:
    def __init__(self,i=0,j=0,heading='E'):
        self.i=i
        self.j=j
        self.heading=heading
        self.visited=[(i,j,heading)]
        self.ongrid=True
        self.inloop=False
        self.directions={'N':(-1,0), 'E':(0,1), 'S':(1,0), 'W':(0,-1)}
        self.children=[]
        
    def updateposition(self):
        newi,newj=self.i,self.j
        if data[self.i][self.j]=='.':
            #no change to heading
            self.heading=self.heading
            
        elif data[self.i][self.j]=='/':
            if self.heading=='N': self.heading='E'
            elif self.heading=='E': self.heading='N'
            elif self.heading=='S': self.heading='W'
            elif self.heading=='W': self.heading='S'
            
        elif data[self.i][self.j]=='\\':
            if self.heading=='N': self.heading='W'
            elif self.heading=='W': self.heading='N'
            elif self.heading=='S': self.heading='E'
            elif self.heading=='E': self.heading='S'
        
        elif data[self.i][self.j]=='|':
            if self.heading=='N': self.heading='N'
            elif self.heading=='E': 
                self.heading='N' 
                self.children.append((self.i,self.j,'S'))
            elif self.heading=='S': self.heading='S'
            elif self.heading=='W': 
                self.heading='N' 
                self.children.append((self.i,self.j,'S'))
            
        elif data[self.i][self.j]=='-':
            if self.heading=='N': 
                self.heading='E' 
                self.children.append((self.i,self.j,'W'))
            elif self.heading=='E': self.heading='E' 
            elif self.heading=='S': 
                self.heading='E' 
                self.children.append((self.i,self.j,'W'))
            elif self.heading=='W': self.heading='W' 
        
        newi+=self.directions[self.heading][0]
        newj+=self.directions[self.heading][1]
        if (newi,newj,self.heading) in self.visited: self.inloop=True
        if newi in range(len(data)) and newj in range(len(data[0])):
            self.i=newi
            self.j=newj
            self.visited.append((self.i,self.j,self.heading))
        else:
            self.ongrid=False
 
def findPhotons(photons):
    for photon in photons:
        if (photon.visited[0][0],photon.visited[0][1],photon.visited[0][2]) not in visitedPhotons:
            visitedPhotons.append((photon.visited[0][0],photon.visited[0][1],photon.visited[0][2]))
            while photon.ongrid and not photon.inloop:
                photon.updateposition()
            for info in photon.children:
                photons.append(Photon(info[0],info[1],info[2]))
                
visitedPhotons=[]
photons=[]
photons.append(Photon())

findPhotons(photons)  

vecsummary=[vec for vec in [photon.visited for photon in photons]]

energized=[]
for line in vecsummary:
    for entry in line:
        energized.append((entry[0],entry[1]))
        
print('Part 1 solution', len(set(energized)))
    
starts=[]
for col in range(len(data[0])):
    starts.append((0,col,'S'))
    starts.append((len(data)-1,col,'N'))
    
for row in range(len(data)):
    starts.append((row,0,'E'))
    starts.append((row,len(data[0])-1,'W'))

maxenergized=0

for candidate in starts:
    visitedPhotons=[]
    photons=[]
    photons.append(Photon(candidate[0],candidate[1],candidate[2]))

    findPhotons(photons)  

    vecsummary=[vec for vec in [photon.visited for photon in photons]]

    energized=[]
    for line in vecsummary:
        for entry in line:
            energized.append((entry[0],entry[1]))
    if len(set(energized)) > maxenergized: maxenergized=len(set(energized))

print('Part 2 solution is', maxenergized)   
    