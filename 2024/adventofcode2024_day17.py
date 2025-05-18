output=[]
ip=0

#example

# Register A: 729
# Register B: 0
# Register C: 0

# Program: 0,1,5,4,3,0

A=2024
B=0
C=0

program=[0,3,5,4,3,0]

A=18427963
B=0
C=0

program=[2,4,1,1,7,5,0,3,4,3,1,6,5,5,3,0]





def opcode(instruction,operand):

    global A,B,C,ip,output
    combo=[]
    print(A)
    if operand in range(0,4): combo=operand
    elif operand==4: combo=A
    elif operand==5: combo=B
    elif operand==6: combo=C

    if instruction==0: # adv, divide A by 2^combor operand
        
        den=1<<combo
        # den=pow(2,combo)
        A=A//den
        ip+=2
    
    elif instruction==1: # bxl, B is bitwise XOR of B and literal operand 
        B^=operand
        ip+=2

    elif instruction==2: # bst B=combo%8
        # print(B,combo)
        B=combo%8
        ip+=2

    elif instruction==3: # jnz set instruction pointer to to literal operand if A!=0
        # print('A',A)
        if A!=0: ip=operand
        else: ip+=2 ##
        # print('ip',ip)
        
    elif instruction==4: # bxc B=B XOR C Operand is read but ignored
        B^=C
        ip+=2

    elif instruction==5: # out, append combo mod 8 to output
        output.append(combo%8)
        # print(output)
        # print(program)
        ip+=2
        


    elif instruction==6: # bdv same as adv except store result in B. den is still A
        den=1<<combo
        # den=pow(2,combo)
        B=A//den
        ip+=2

    elif instruction==7: # cdv same as adv except store result in C. den is still A
        den=1<<combo
        # den=pow(2,combo)
        C=A//den
        ip+=2




# for each 2 character chunk of the program, the first character is the opcode
# the second character is the combo operand, 0-3 are 0-3, 4, 5, 6 are A, B, C. 7 is invalid
# ip indicates instruction pointer

def solve(part1=False):
    global output
    global ip
    output=[]
    ip=0
    abort=False
    while True:
        # print(ip)
        # print(program[ip],program[ip+1])
    
        if ip in range(len(program)-1):
            # print(A,B,C)
            # print(program[ip],program[ip+1])      
            opcode(program[ip],program[ip+1])
            # print(A,B,C)
            # if ip in range(len(program)-1) and program[ip]==5: print(output)
            # print()
        else: break
    if not part1:
        if output:
            # for i,test in enumerate(output):
            #     if test!=program[i]: abort=True
            # if output[0]==1 and output[1]==7 and output[2]==5:# and output[3]==0 and output[4]==3: 
            #     print(output)
            #     print()
            #     return True
            if output==program: return True
            # if output==program[-6:]: return True
        if abort: return False


    # print(program)
    # if output[0]==2: print(output[0])
    # print(A,B,C)
    if part1:
        print('Part 1', end=' ')
        for a in output: print(a, end=',')
        print()

lowest=1<<3*(len(program)-1)
highest=1<<3*len(program)

A=484061580706 # so close, misread a number
A=247839539763386 # !! hooray!
solve(True)
n=7
explore='0b'+'1'*3*n
# print()
# print(explore,eval(explore))
# print(program[-6:])
# keepers=[]
# for a in range(eval(explore)):# range(8):
#     A0=0
#     A=a+A0
#     # print(A)
#     # print(program)
#     b=solve(False)
#     # print()
#     if b: #break
#         keepers.append(a)

# print(keepers)
# did figuredso far in a spreadsheet, day17 on google sheets.

# figuredsofar=14772387 #4,3,1,6,5,5,3,0
# digitstogo=8 #2,4,1,1,7,5,0,3
# maxrange=1<<digitstogo*3
# figuredsofar<<=(3*digitstogo)

# for test in range(maxrange):
#     print(test,'of',maxrange)
# # for test in range(lowest,highest):
#     # print(test,lowest,highest)
#     A=figuredsofar+test
#     # print(A,end=' ')
#     a=solve()
#     if a:
#         print('Part 2',test) 
#         break
# print()
# print(program)       