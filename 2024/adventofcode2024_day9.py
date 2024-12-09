fname='input_day9.txt'
fname='example_day9.txt'
with open(fname) as fp: data = fp.read().splitlines()

diskmap=data[0]
#diskmap='12345'

#print(diskmap)

def findBlocks(diskmap):
    blocks={}
    blocknum=0
    for i,val in enumerate(diskmap):
        if i%2==0: #even entries, number of blocks
            blocksize=int(val)
            if i+1 in range(len(diskmap)):
                emptyblocks=int(diskmap[i+1])
            else: emptyblocks=0
            # print(blocknum,blocksize-emptyblocks)
            blocks[blocknum] = [str(blocknum)*blocksize+'.'*emptyblocks]
            blocknum+=1
    return blocks

def blockList(blocks):
    tmp = [a for a in [b[0] for b in blocks.values()]]
    bl=[]
    for a in tmp:
        for b in a:
            bl.append(b)
    return bl

# def moveBlocks(blocks):
#     for block in blocks.keys():
#         if '.' in blocks[block]:
#             if 

def repackBlockStr(blockstr):
    freeidx=len(blockstr)-1
    lastblock=len(blockstr)-1
    for idx in range(len(blockstr)):
        if blockstr[idx]=='.': 
            freeidx=idx
            blockToMove=''
            #print(idx,freeidx)
            for blockidx in range(lastblock,0,-1):
               # print("blockidx",blockidx)
                if blockstr[blockidx]!='.':
                    blockToMove=blockstr[blockidx]
                    lastblock=blockidx
                  #  print(blockToMove)
                    break
            if blockidx>idx and blockToMove!='':
                blockstr[blockidx]='.'
                blockstr[idx]=blockToMove
            elif blockidx<=idx:
                break
        # print(blockstr)
    return blockstr

def calculateChecksum(blocklist):
    checksum=0
    for i,val in enumerate(blocklist):
        if val!='.':
            checksum+=i*int(val)
    return checksum

        
blocks=findBlocks(diskmap)
blockstr=blockList(blocks)
# print(blockstr)
blockstr=repackBlockStr(blockstr)
print(len(blockstr))
print(calculateChecksum(blockstr)) #88960367801 is too low

