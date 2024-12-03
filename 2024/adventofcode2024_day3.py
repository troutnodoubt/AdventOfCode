import re

fname='input_day3.txt'
#fname='example_day3.txt'
#fname='example_day3a.txt'
with open(fname) as fp: data = fp.read().splitlines()

#part 1
total=0
for line in data:
    valid=re.findall("mul\(\d*,\d*\)",line)
    for entry in valid:
        prod=re.findall("\d*,\d*",entry)[0].split(',')
        total+=int(prod[0])*int(prod[1])
print('Part 1 solution', total)

#part 2
total=0
multiplier=1
for line in data:
    valid=re.findall("mul\(\d*,\d*\)|do\(\)|don't\(\)",line)
    for entry in valid:
        if entry[:3]=="mul":
            prod=re.findall("\d*,\d*",entry)[0].split(',')
            total+=int(prod[0])*int(prod[1])*multiplier
        elif entry[:3]=="do(":
            multiplier=1
        elif entry[:3]=="don":
            multiplier=0
        else:
            print("ruh roh")
print('Part 2 solution', total)

