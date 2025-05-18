fname='input_day9.txt'
# fname='example_day9.txt'
with open(fname) as fp: data = fp.read().splitlines()

diskmap=data[0]
# diskmap='12345'

def findBlocks(diskmap):
    blocks={}
    blocknum=0
    for i,val in enumerate(diskmap):
        if i%2==0: #even entries, number of blocks
            blocksize=int(val)
            if i+1 in range(len(diskmap)):
                emptyblocks=int(diskmap[i+1])
            else: emptyblocks=0
            blocks[blocknum] = [blocknum]
            for i in range(blocksize-1): blocks[blocknum].append(blocknum)
            for i in range(emptyblocks): blocks[blocknum].append('.')
            blocknum+=1
    return blocks

def blockList(blocks):
    tmp = [a for a in blocks.values()]
    bl=[]
    for a in tmp:
        for b in a:
            bl.append(b)
    return bl

def repackBlockList(blockstr):
    freeidx=len(blockstr)-1
    lastblock=len(blockstr)-1
    for idx in range(len(blockstr)):
        if blockstr[idx]=='.': 
            freeidx=idx
            blockToMove=[]
            for blockidx in range(lastblock,0,-1):
                if blockstr[blockidx]!='.':
                    blockToMove=blockstr[blockidx]
                    lastblock=blockidx
                    break
            if blockidx>idx and blockToMove!='':
                blockstr[blockidx]='.'
                blockstr[idx]=blockToMove            
    return blockstr

def repackWhole(blockstr):
    for i in range(len(blockstr)-1,0,-1):
        if blockstr[i]!='.': 
            maxblock=blockstr[i]
            break
    for block in range(maxblock,0,-1):
        blocksize=blockstr.count(block)
        blockidx=blockstr.index(block)
        print(block)
        moveblock=False
        for i in range(len(blockstr)):
            size=0
            if blockstr[i]=='.':
                size=1
                while True:
                    if i+size<len(blockstr)-1 and blockstr[i+size]=='.' and i < blockidx: size+=1
                    else: break                    
            if size>=blocksize and blockidx>i:
                moveblock=True
                break
        if moveblock:
            blockstr[blockidx:blockidx+blocksize]=['.' for a in range(blocksize)]
            blockstr[i:i+blocksize]=[block for a in range(blocksize)]        
    return blockstr

def calculateChecksum(blocklist):
    checksum=0
    for i,val in enumerate(blocklist):
        if val!='.':
            checksum+=i*int(val)
    return checksum
        
blocks=findBlocks(diskmap)
blist=blockList(blocks)
blist=repackBlockList(blist)
print('Part 1',calculateChecksum(blist)) #88960367801 is too low, 6241633730082 correct
    
blist=blockList(blocks)
blist=repackWhole(blist)
print('Part 2',calculateChecksum(blist))
