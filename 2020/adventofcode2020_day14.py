import re

fname="C://Users/Mark/Documents/Advent of Code/2020/day_14_example.txt"
fname="C://Users/Mark/Documents/Advent of Code/2020/day_14_example2.txt"
fname="C://Users/Mark/Documents/Advent of Code/2020/input_day14.txt"
with open(fname) as fp: data = fp.read().splitlines()

#find largest address
addressmax=0
valuemax=0
for row in data:
    if('mem' in row):
        memstuff=re.findall("[0-9]+",row)
        address=int(memstuff[0])
        value=int(memstuff[1])
        if address>addressmax:
            addressmax=address
        if value>valuemax:
            valuemax=value
    
mem=[0]*(addressmax+1)

for row in data:
    if('mask' in row):
        mask=row[-36:]
    if('mem' in row):
        memstuff=re.findall("[0-9]+",row)
        address=int(memstuff[0])
        value=int(memstuff[1])
        decvalue=bin(value)
        decvalue=decvalue[2:]
        if len(decvalue)<36:
            decvalue="{0:036b}".format(value)
        #print(mask,decvalue, int(decvalue,2))
        #MSC is most significant chunk, LSC is least significant chunk
        MSC=decvalue[:-36]
        LSC=decvalue[-36:]
        LSC=list(LSC)
        #print(MSC)
        for bitnum in range(0,len(mask)):
            if mask[bitnum]!='X':
                LSC[bitnum]=mask[bitnum]
            #print(bitnum,mask[bitnum],LSC[bitnum])
        LSC=''.join([str(item) for item in LSC])
        #print(mask,MSC+LSC,int(MSC+LSC,2))
        mem[address]=int(MSC+LSC,2)
        
print('Part 1 solution is',sum(mem))


mem={}         
for row in data:
    if('mask' in row):
        mask=row[-36:]
        nfloat=len(re.findall("X",mask))
        #print(nfloat)
        fstring='{:0'+str(nfloat)+'b}'
    if('mem' in row):
        memstuff=re.findall("[0-9]+",row)
        address=int(memstuff[0])
        value=int(memstuff[1])
        binaddress="{0:036b}".format(address)
        binaddress=list(binaddress)
        #print(binaddress)
        for bitnum in range(0,len(mask)):
            if mask[bitnum]!='0':
                binaddress[bitnum]=mask[bitnum]
        #print(binaddress)  
        for i in range(0,2**nfloat):
            xvec=fstring.format(i)
            #print(i,xvec)
            k=0
            binaddressnew=binaddress.copy()
            for j in range(0,len(binaddressnew)):
                if binaddressnew[j]=="X":
                    binaddressnew[j]=xvec[k]
                    k=k+1
            binaddressnew=''.join([str(item) for item in binaddressnew])
            #print(int(binaddressnew,2))
            #mem[int(binaddressnew,2)]=value
            mem[int(binaddressnew,2)]=value
sol=0
for x in mem:
    sol=sol+mem[x]        
print('Part 2 solution is',sol)               
       
        
         
         