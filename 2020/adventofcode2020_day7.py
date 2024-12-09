import re

fname=open("C://Users/Mark/Documents/Advent of Code/2020/day_7_example.txt")
fname=open("C://Users/Mark/Documents/Advent of Code/2020/input_day7.txt")
bagrules = fname.readlines()
fname.close()

def unique(list1):
    unique_list=[]
    for x in list1:
        if x not in unique_list:
            unique_list.append(x)
    return unique_list

dataset=[];
colors=['shiny gold']
savedcolors=[]
newcolors=[]
moretosearch=True
while moretosearch:
    for color in colors:
        for rule in bagrules:
            pair=rule.split(' bags contain ')
            key=pair[0]
            value=pair[1]
            if color in value:
                newcolors.append(key)
                savedcolors.append(key)
    if not newcolors:
        moretosearch=False
    colors=newcolors
    newcolors=[]

okbags=unique(savedcolors)
print('Part 1 solution is',len(okbags))


colorlist=['shiny gold']
dataset={}
newcolorlist=[]
moretodo=True
while moretodo:
    for rule in bagrules:
        pair=rule.split(' bags contain ')
        key=pair[0]
        value=pair[1]
        dataset[key]=value
    for outercolor in colorlist:
        print(outercolor)
        for entry in dataset[outercolor].split(', '):
            if entry.split()[0]!='no':
                qty=int(entry.split()[0])
                innercolor=entry.split()[1]+' '+entry.split()[2]       
                print('\t',qty)
                print('\t',innercolor)
                newcolorlist.append(innercolor)
    colorlist=newcolorlist
    newcolorlist=[]
    dataset={}
    if not colorlist:
        moretodo=False
    


