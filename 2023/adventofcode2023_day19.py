import re
    
def parseWF(part,wf):
    flow=wfdict[wf]
    x=part[0]
    m=part[1]
    a=part[2]
    s=part[3]
    nextwf=''
    for possibility in flow:
        if ':' in possibility:
            condition=re.match('.*:',possibility).group()[:-1]
            if eval(condition): nextwf=re.search(':.*',possibility).group()[1:]
        else: nextwf=possibility
        if nextwf=='R': return 0
        elif nextwf=='A': return 1
        else: 
            if nextwf in wfdict.keys(): 
                retval=parseWF(part,nextwf)
                if retval in [0,1]: return retval

# def findChildren(wf):
#     flow=wfdict[wf]
#     for possibility in flow:
#         if ':' in possibility
    


fname='input_day19.txt'
fname='example_day19.txt'
with open(fname) as fp: data = fp.read().splitlines()

delim=[i for i,x in enumerate(data) if x==''][0]

workflows=data[:delim]
parts=data[delim+1:]

wfdict={}
for line in workflows:
    key = re.match('.*\{', line).group()[:-1]
    val=line[len(key)+1:-1]
    wfdict[key]=val.split(',')
 
total=0
for line in parts:
    xmas=[int(x) for x in re.findall('[0-9]+',line)]
    if parseWF(xmas,'in')==1: total+=sum(xmas)

print('Part 1 is', total)

for key in wfdict.keys():
    nodes=[]
    edges=[]
    children=wfdict[key]
    for child in children:
        if ':' in child: 
            nodes.append(re.search(':.+',child).group()[1:])
            edges.append(re.search('.*:',child).group()[:-1])
        else: 
            nodes.append(child)
            edges.append('')
    print(nodes)
    print(edges)

    temp=''
    tempedge=[]
    for i,edge in enumerate(edges):
        if '<' in edge:
            complement=edge.replace('<','>=')
        elif '>' in edge:
            complement=edge.replace('>','<=')
        tempedge.append(complement)
        # print(temp)
    print(tempedge)
    print()
            
        
