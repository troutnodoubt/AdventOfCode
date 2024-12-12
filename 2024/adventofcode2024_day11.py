

def solve(nblinks):
    data=['125 17']
    
    stones={a:1 for a in data[0].split()}
    blinks=0
    totalstones=0
    while blinks<nblinks:
        # print(stones)
        newstones={}
        keys=list(stones.keys())
        
        totalstones=0
        for key in keys:
            if stones[key]>0:
                if key=='0':
                    if '1' not in newstones.keys(): newstones['1']=stones[key]
                    else: newstones['1']=newstones['1']+stones[key]
                
                elif len(key)%2==0:
                    left=key[:len(key)//2]
                    right=str(int(key[len(key)//2:]))
                    if left not in newstones.keys(): newstones[left]=stones[key]
                    else: newstones[left]=newstones[left]+stones[key]
                    if right not in newstones.keys(): newstones[right]=stones[key]
                    else: newstones[right]=newstones[right]+stones[key]
                    
                else:
                    if str(int(key)*2024) not in newstones.keys(): newstones[str(int(key)*2024)]=stones[key]
                    else: newstones[str(int(key)*2024)]=newstones[str(int(key)*2024)]+stones[key]
                    
        totalstones=sum(newstones.values())
        
        blinks+=1
        stones={}
        stones=newstones.copy()
    return totalstones
    
print("Part 1",solve(25))
print("Part 2",solve(75))

