
fname="C://Users/Mark/Documents/Advent of Code/2021/day_8_example.txt"
#fname="C://Users/Mark/Documents/Advent of Code/2021/day_8_shortexample.txt"
fname="C://Users/Mark/Documents/Advent of Code/2021/input_day8.txt"
with open(fname) as fp: data = fp.read().splitlines()

output=list()
for row in data:
    #print(row)
    splitrow=[a for a in row.split('|')]
    output.append(splitrow[1])
    
ones=0
fours=0
sevens=0
eights=0

for row in output:
   
    test=row.split()
    for entry in test:
        if len(entry)==2:
            ones+=1
            
        elif len(entry)==4:
            fours+=1
           
        elif len(entry)==3:
            sevens+=1
            
        elif len(entry)==7:
            eights+=1
           

print('Part 1 solution is', ones+fours+sevens+eights)

#part 2

#     top TL  TR  middle  BL  BR  Bottom
# 0   1   1   1   0       0   1   1
# 1   0   0   1   0       0   1   0 
# 2   1   0   1   1       1   0   1
# 3   0   0   1   0       0   1   1
# 4   0   1   1   1       0   1   0
# 5   1   1   0   1       0   1   1
# 6   1   1   0   1       1   1   1
# 7   1   0   1   0       0   1   0
# 8   1   1   1   1       1   1   1
# 9   1   1   1   1       0   1   1

# top is in 7 but not 1
# TL and middle are in 4 and 8 but not 1 or 7
# BL and bottom are in 8 but not 7 or 4
# TR and BR are in 1, 4, 7, and 8

output=list()
solutions=list()
for row in data:
    label1=list()
    label2=list()
    label3=list()
    label4=list()
    label5=list()
    label069=list()
    label35=list()
    label235=list()
    label7=list()
    label8=list()
    label9=list()
    test=row.split()
    for entry in test:
        if len(entry)==2:
            ones+=1
            label1.append(entry)
        elif len(entry)==4:
            fours+=1
            label4.append(entry)
        elif len(entry)==3:
            sevens+=1
            label7.append(entry)
        elif len(entry)==6:
            label069.append(entry)
        elif len(entry)==5:
            label235.append(entry)
        elif len(entry)==7:
            eights+=1
            label8.append(entry)
        
    label1=list(dict.fromkeys(label1))
    label4=list(dict.fromkeys(label4))
    label7=list(dict.fromkeys(label7))
    label8=list(dict.fromkeys(label8))
    for letter in str(label7[0]):
        if letter not in str(label1[0]):
            top=letter
    for possible in label235:
        #print(possible)
        test=str(label4[0])+top
        #print(test)
        lettercount=0
        possibleletters=list()
        for letter in possible:
            if letter not in test:
                lettercount+=1
                possibleletters.append(letter)
        #print(lettercount)
        #print(possibleletters)
        if len(possibleletters)==2:
            label2.append(possible)
            letters2=possibleletters
        else:
            bottom=possibleletters[0]
            label35.append(possible)
    for letter in letters2:
        if letter != bottom:
            bl=letter
    for possible in label35:
        #print(possible)
        test=str(label1[0])+top+bottom
        #print(test)
        lettercount=0
        possibleletters=list()
        for letter in possible:
            if letter not in test:
                lettercount+=1
                possibleletters.append(letter)
        #print(lettercount)
        #print(possibleletters)
        if len(possibleletters)==2:
            label5.append(possible)
            letters5=possibleletters
        else:
            middle=possibleletters[0]
    for letter in letters5:
        if letter != middle:
            tl=letter
    for letter in label5[0]:
        #print(letter)       
        if letter != middle and letter != top and letter != bottom and letter != tl:
            br=letter
    for letter in label1[0]:
        if letter != br:
            tr=letter
            
    #print(row)
    splitrow=[a for a in row.split('|')]
    #output.append(splitrow[1])
    output=splitrow[1]
    string0=top+tr+br+bottom+bl+tl
    string1=tr+br
    string2=top+tr+middle+bl+bottom
    string3=top+middle+bottom+tr+br
    string4=tl+tr+middle+br
    string5=top+tl+middle+br+bottom
    string6=top+tl+middle+bl+br+bottom
    string7=top+string1
    string8=string0+middle
    string9=string4+top+bottom
    outputval=''
    #print(output)
    for code in output.split():
        #print(code)
        # print(sorted(code))
        # print('0-',sorted(string0))
        # print('1-',sorted(string1))
        # print('2-',sorted(string2))
        # print('3-',sorted(string3))
        # print('4-',sorted(string4))
        # print('5-',sorted(string5))
        # print('6-',sorted(string6))
        # print('7-',sorted(string7))
        # print('8-',sorted(string8))
        # print('9-',sorted(string9))
        if sorted(code)==sorted(string0):
            outputval=outputval+'0'
        if sorted(code)==sorted(string1):
            outputval=outputval+'1'
        if sorted(code)==sorted(string2):
            outputval=outputval+'2'
        if sorted(code)==sorted(string3):
            outputval=outputval+'3'
        if sorted(code)==sorted(string4):
            outputval=outputval+'4'
        if sorted(code)==sorted(string5):
            outputval=outputval+'5'
        if sorted(code)==sorted(string6):
            outputval=outputval+'6'
        if sorted(code)==sorted(string7):
            outputval=outputval+'7'
        if sorted(code)==sorted(string8):
            outputval=outputval+'8'
        if sorted(code)==sorted(string9):
            outputval=outputval+'9'
        #print(outputval)
    solutions.append(outputval)

print('Part 2 solution is',sum([int(a) for a in solutions]))
        