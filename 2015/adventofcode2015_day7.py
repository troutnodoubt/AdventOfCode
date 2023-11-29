fname='input_day7.txt'
#fname='example_day7.txt'
with open(fname) as fp: data = fp.read().splitlines()

wirelist={}

def processCircuit(instruction):
    temp=instruction.split(' -> ')
    wire=temp[1]
    op=temp[0].split(' ')
    val=''
    if len(op)==1:
        if op[0].isnumeric():
            val=int(op[0])
        elif op[0] in wirelist.keys():
            val=wirelist[op[0]]
        # else:
        #     print(instruction)
    elif len(op)==2:
        if op[0]=='NOT':
            if op[1] in wirelist.keys():
                val=~wirelist[op[1]]
        # else:
        #     print(instruction)
    elif len(op)==3:
        if op[1]=='AND':
            if op[0] in wirelist.keys() and op[2] in wirelist.keys():
                val=wirelist[op[0]] & wirelist[op[2]]
            elif op[0] in wirelist.keys() and op[2].isnumeric():
                val=wirelist[op[0]] & int(op[2])
            elif op[0].isnumeric() and op[2] in wirelist.keys():
                    val=int(op[0]) & wirelist[op[2]]
            elif op[0].isnumeric() and op[2].isnumeric():
                    val=int(op[0]) & int(op[2])
            # else:
            #     print(instruction)
        elif op[1]=='OR':
            if op[0] in wirelist.keys() and op[2] in wirelist.keys():
                val=wirelist[op[0]] | wirelist[op[2]]
            elif op[0] in wirelist.keys() and op[2].isnumeric():
                val=wirelist[op[0]] | int(op[2])
            elif op[0].isnumeric() and op[2] in wirelist.keys():
                    val=int(op[0]) | wirelist[op[2]]
            elif op[0].isnumeric() and op[2].isnumeric():
                    val=int(op[0]) | int(op[2])
            # else:
            #     print(instruction)
        elif op[1]=='LSHIFT':
            if op[0] in wirelist.keys():
                val=wirelist[op[0]] << int(op[2])
        elif op[1]=='RSHIFT':
            if op[0] in wirelist.keys():
                val=wirelist[op[0]] >> int(op[2])
        # else:
        #     print(instruction)
        
    if isinstance(val,int):
        if val<0: val+=2**16
        wirelist[wire]=val
 
while len(wirelist) < len(data):
    for instruction in data:
        processCircuit(instruction)
    if 'a' in wirelist.keys():
        break
    
print('Part 1 solution is', wirelist['a'])

for i in range(len(data)):
    if data[i].split(' -> ')[-1]=='b':
        print(data[i])
        data[i]=str(wirelist['a']) + ' -> b'

for i in range(len(data)):
    if data[i].split(' -> ')[-1]=='b':
        print(data[i])

wirelist={}
   
while len(wirelist) < len(data):
    for instruction in data:
        processCircuit(instruction)
    if 'a' in wirelist.keys():
        break
print('Part 2 solution is', wirelist['a']) 
