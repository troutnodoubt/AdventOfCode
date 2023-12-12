import math

fname='input_day11.txt'
fname='example_day11.txt'
with open(fname) as fp: data = fp.read().splitlines()

def transposeListofLists(lst):
    tr_lst=[['' for i in lst] for j in lst[0]]
    print(tr_lst)
    for i in range(len(lst)):
        for j in range(len(lst[0])):
            tr_lst[j][i]=lst[i][j]
    return tr_lst
            

expanded=[] #need to expand columns as well, use numpy

empty=['.' for i in range(len(data[0]))]


universe=0
universelocs={}
for i,line in enumerate(data):
    if '#' not in line:
        expanded.append(empty)
        expanded.append(empty)
    else:
        linecopy=[]
        j=0
        for c in line:
            if c=='#':
                linecopy.append(str(universe))
                universelocs[universe]=(i,j)
                universe+=1
            else:
                linecopy.append(c)
            j+=1
        expanded.append(linecopy)
        


# def findDistance()