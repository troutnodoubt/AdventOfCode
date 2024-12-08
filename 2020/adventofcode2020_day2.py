import re
inputfile=open("C://Users/Mark/Documents/Advent of Code/2020/input_day2.txt")

passwordList=(
'1-3 a: abcde',
'1-3 b: cdefg',
'2-9 c: ccccccccc')

passwordList=inputfile.readlines()
inputfile.close()

count=0
count2=0
for entry in passwordList:
    #print(entry)
    minnum=re.search('^[0-9]*',entry)
    minchar=entry[minnum.start():minnum.end()]
    #print(minchar)
    #print(minnum.span())
    maxnum=re.search('-[0-9]* ',entry)
    maxchar=entry[maxnum.start()+1:maxnum.end()-1]
    #print(maxchar)
    #print(maxnum.span())
    letter=re.search('[a-z]:',entry)
    required=entry[letter.start():letter.end()-1]
    #print(required)
    #print(letter.span())
    pw=re.search(': [a-z]*',entry)
    pwstring=entry[pw.start()+2:pw.end()]
    #print(pwstring)
    #print(pw.span())
    strippedpw=re.findall(required,pwstring)
    #print(len(strippedpw))
    
    if len(strippedpw)>=int(minchar) and len(strippedpw)<=int(maxchar):
        #print('Meets criteria')
        count=count+1
    if pwstring[int(minchar)-1]==required and pwstring[int(maxchar)-1]!=required:
        #print('Meets criteria 2')
        count2=count2+1
    if pwstring[int(minchar)-1]!=required and pwstring[int(maxchar)-1]==required:
        #print('Meets criteria 2')
        count2=count2+1
print('Solution to part 1')
print(count)
print('Solution to part 2')
print(count2)
    
    
