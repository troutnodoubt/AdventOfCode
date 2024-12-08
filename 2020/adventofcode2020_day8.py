fname="C://Users/Mark/Documents/Advent of Code/2020/day_8_example.txt"
fname="C://Users/Mark/Documents/Advent of Code/2020/input_day8.txt"
with open(fname) as fp: instructions = fp.readlines()
visited_records=[]
record=0
accumulator=0
while record not in visited_records:
    command=instructions[record][:3]
    number=int(instructions[record][4:])
    #print(instructions[record],accumulator)
    #print(record,visited_records)
    #print(command)
    visited_records.append(record)
    if command=='nop':
        record=record+1
    elif command=='acc':
        record=record+1
        accumulator=accumulator+number
    elif command=='jmp':
        record=record+number
    else:
        print('Something wrong, invalid command')
                  
    
    #print(record,visited_records)
print('Part 1 solution is',accumulator)


#Part 2
fixfound=False
testrecord=0
baselineinstructions=tuple(instructions)
while not fixfound:
    #print('in test loop')
    command=instructions[testrecord][:3]
    number=instructions[testrecord][4:]
    #print(instructions)
    #print(command)
    if command=='nop':
        instructions[testrecord]='jmp '+number
        #print('changing nop to jmp at',testrecord)
    if command=='jmp':
        instructions[testrecord]='nop '+number
        #print('changing jmp to nop at',testrecord)
    testrecord=testrecord+1
    
    #print(instructions)
    visited_records=[]
    record=0
    accumulator=0
    while record not in visited_records:
        #print('in program loop')
        command=instructions[record][:3]
        number=int(instructions[record][4:])
        #print(instructions[record],accumulator)
        #print(record,visited_records)
        visited_records.append(record)
        #print(command)
        if command=='nop':
            record=record+1
        elif command=='acc':
            record=record+1
            accumulator=accumulator+number
        elif command=='jmp':
            record=record+number
        else:
            print('Something wrong, invalid command')
            
        if record==len(instructions):
            print('Part 2 solution is',accumulator)
            fixfound=True
            break
    instructions=list(baselineinstructions)
