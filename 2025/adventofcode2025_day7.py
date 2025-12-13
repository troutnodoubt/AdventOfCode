
fname='/home/mark/Documents/git/AdventOfCode/2025/input_day7.txt'
fname='/home/mark/Documents/git/AdventOfCode/2025/example_day7.txt'

branches=dict()

def hasSplittingDescendants(node):
    if node in branches.keys():
        children=branches[node]
        # print(node,branches[node],children)
        
           
        if len(children)>1: return True
        elif len(children)==1 and hasSplittingDescendants(children[0]): return True
        else: return False

    else:
        return False


with open(fname) as fp: data1 = fp.read().splitlines()

splitcnt=0
data=[]
for row in data1:
    data.append(list(row))


splits=dict()
start=0
rowlength=len(data[0])
for row in range(len(data)-1):
    for col in range(1,len(data[0])):
        if data[row][col]=='S':
            data[row+1][col]='|'
            start=(row+1)*rowlength+col
        elif data[row][col]=='|':
            if data[row+1][col]=='.':
                data[row+1][col]='|'
                branches[row*rowlength+col]=[(row+1)*rowlength+col]
            elif data[row+1][col]=='^':
                data[row+1][col-1]='|'
                data[row+1][col+1]='|'
                splitcnt+=1
                branches[row*rowlength+col]=[(row+1)*rowlength+col]
                branches[(row+1)*rowlength+col]=[(row+1)*rowlength+col-1,(row+1)*rowlength+col+1]
finalrow=len(data)-1
for col in range(1,rowlength):
    if data[finalrow][col]=='|':
        branches[finalrow*rowlength+col]=[]

# for key in branches.keys():
    # print(key)
    # if len(branches[key])>1: 
        # nsplits+=1
        # print('haschildren',key)

for key in branches.keys():
    print(key,branches[key])
print()

for row in range(len(data),0,-1):
    for col in range(rowlength):
        node=row*rowlength+col
        count=0
        if node in branches.keys() and len(branches[node])>1: #splitting node
            # print(node,row,len(data))
            if row==len(data)-2: # final row of splitters
                # print('final row',node)
                splits[node]=2
            else:
                for child in branches[node]:
                    splits[node]=0
                    
                    # print(node,branches[node],child)
                    print(child,hasSplittingDescendants(child))
                    print(child in splits.keys()) # on the right track, but keys to the right haven't processed yet

# Need to do this in steps:
# 1. Populate last row (done)
# 2. Propagate values up to next row
# 3. Populate splitting cells
# 4. Repeat 2 and 4 until done




                    if hasSplittingDescendants(child) and child in splits.keys():
                        count+=splits[child]
                        print('has splitters',node,count)
                    else:
                        count+=1
                        print('no more splitters',node,count)
                    splits[node]+=count
                    print(node,splits[node])
        else: # non splitting node, just propagate the count up the chain
            if node in branches.keys() and len(branches[node])>0 and branches[node][0] in splits.keys(): 
                # print(branches[node])
                splits[node]=splits[branches[node][0]]

print()
for key in splits.keys():
    print(key,splits[key])            
print()
print('Part 1 is',splitcnt)
# print(branches)

