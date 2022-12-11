class monkey:
    def __init__(self, name, items, operation, test,  iftrue, iffalse, count):
        self.name=name
        self.items=items        
        self.test=test
        self.operation=operation
        self.iftrue=iftrue
        self.iffalse=iffalse
        self.count=count
        
    def examineobject(self):
        old=self.items[0]
        old+=0 #just to quiet the warning
        new=eval(self.operation)
        #new=new//worryfactor
        
        self.count+=1
        if new%self.test == 0:
            return self.iftrue
        else:
            return self.iffalse
        
    def additem(self,nextitem):
        self.items.append(nextitem)
     

# monkey0=monkey("monkey0", [79,98], "old*19", 23, 2, 3, 0)
# monkey1=monkey("monkey1", [54,65,75,74], "old+6", 19, 2, 0, 0)
# monkey2=monkey("monkey2", [79,60,97], "old*old", 13, 1, 3, 0)
# monkey3=monkey("monkey3", [74], "old+3", 17, 0, 1, 0)

# nmonkeys=4
# worryfactor=23*19*13*17

monkey0=monkey("monkey0", [54, 61, 97, 63, 74], "old*7", 17, 5, 3, 0)
monkey1=monkey("monkey1", [61, 70, 97, 64, 99, 83, 52, 87], "old+8", 2, 7, 6, 0)
monkey2=monkey("monkey2", [60, 67, 80, 65], "old*13", 5, 1, 6, 0)
monkey3=monkey("monkey3", [61, 70, 76, 69, 82, 56], "old+7", 3, 5, 2, 0)
monkey4=monkey("monkey4", [79, 98], "old+2", 7, 0, 3, 0)
monkey5=monkey("monkey5", [72, 79, 55], "old+1", 13, 2, 1, 0)
monkey6=monkey("monkey6", [63], "old+4", 19, 7, 4, 0)
monkey7=monkey("monkey7", [72, 51, 93, 63, 80, 86, 81], "old*old", 11, 0, 4, 0)

nmonkeys=8
worryfactor=17*2*5*3*7*13*19*11

for round in range(10000):
    
    for nmonkey in range(nmonkeys):

        currentmonkey=eval("monkey"+str(nmonkey))
        
        while len(currentmonkey.items)>0:
    
    
            targetmonkey = currentmonkey.examineobject()
            targetmonkey = "monkey"+str(targetmonkey)
            items = currentmonkey.items
            
            
            old = items.pop(0)
            targetitem=eval(currentmonkey.operation)
            currentmonkey.items=items
            
            
            
            eval(targetmonkey).additem(targetitem%worryfactor)

# print(monkey0.items)
# print(monkey1.items)
# print(monkey2.items)
# print(monkey3.items)

# print(monkey0.count)
# print(monkey1.count)
# print(monkey2.count)
# print(monkey3.count)

counts=[]
for nmonkey in range(nmonkeys):
    currentmonkey=eval("monkey"+str(nmonkey))
    counts.append(currentmonkey.count)

counts.sort()
sol=counts[-1]*counts[-2]
print(sol)

