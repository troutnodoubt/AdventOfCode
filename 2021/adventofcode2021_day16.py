#from collections import defaultdict
#import numpy as np
# from numpy import Inf
# import matplotlib.pyplot as plt
# fname="day_13_example.txt"
# fname="input_day13.txt"
# with open(fname) as fp: data = fp.read().splitlines()
import sys

f=open('operations.txt','w')

packet='D2FE28'
packet='38006F45291200'
packet='EE00D40C823060'
packet='8A004A801A8002F478'
packet='620080001611562C8802118E34'
packet='C0015000016115A2E0802F182340'
packet='A0016C880162017C3686B18A3D4780'
packet='C200B40A82'
packet='04005AC33890'
packet='CE00C43D881120'
packet='D8005AC2A8F0'
packet='F600BC2D8F'
packet='9C005AC2F8F0'
packet='9C0141080250320F1802104A08'
packet='220D62004EF14266BBC5AB7A824C9C1802B360760094CE7601339D8347E20020264D0804CA95C33E006EA00085C678F31B80010B88319E1A1802D8010D4BC268927FF5EFE7B9C94D0C80281A00552549A7F12239C0892A04C99E1803D280F3819284A801B4CCDDAE6754FC6A7D2F89538510265A3097BDF0530057401394AEA2E33EC127EC3010060529A18B00467B7ABEE992B8DD2BA8D292537006276376799BCFBA4793CFF379D75CA1AA001B11DE6428402693BEBF3CC94A314A73B084A21739B98000010338D0A004CF4DCA4DEC80488F004C0010A83D1D2278803D1722F45F94F9F98029371ED7CFDE0084953B0AD7C633D2FF070C013B004663DA857C4523384F9F5F9495C280050B300660DC3B87040084C2088311C8010C84F1621F080513AC910676A651664698DF62EA401934B0E6003E3396B5BBCCC9921C18034200FC608E9094401C8891A234080330EE31C643004380296998F2DECA6CCC796F65224B5EBBD0003EF3D05A92CE6B1B2B18023E00BCABB4DA84BCC0480302D0056465612919584662F46F3004B401600042E1044D89C200CC4E8B916610B80252B6C2FCCE608860144E99CD244F3C44C983820040E59E654FA6A59A8498025234A471ED629B31D004A4792B54767EBDCD2272A014CC525D21835279FAD49934EDD45802F294ECDAE4BB586207D2C510C8802AC958DA84B400804E314E31080352AA938F13F24E9A8089804B24B53C872E0D24A92D7E0E2019C68061A901706A00720148C404CA08018A0051801000399B00D02A004000A8C402482801E200530058AC010BA8018C00694D4FA2640243CEA7D8028000844648D91A4001088950462BC2E600216607480522B00540010C84914E1E0002111F21143B9BFD6D9513005A4F9FC60AB40109CBB34E5D89C02C82F34413D59EA57279A42958B51006A13E8F60094EF81E66D0E737AE08'




def hex2bin(packet):
    binpacket=''
    for i in packet: 
        if i=='0': binpacket=binpacket+'0000'
        elif i=='1': binpacket=binpacket+'0001'
        elif i=='2': binpacket=binpacket+'0010'
        elif i=='3': binpacket=binpacket+'0011'
        elif i=='4': binpacket=binpacket+'0100'
        elif i=='5': binpacket=binpacket+'0101'
        elif i=='6': binpacket=binpacket+'0110'
        elif i=='7': binpacket=binpacket+'0111'
        elif i=='8': binpacket=binpacket+'1000'
        elif i=='9': binpacket=binpacket+'1001'
        elif i=='A': binpacket=binpacket+'1010'
        elif i=='B': binpacket=binpacket+'1011'
        elif i=='C': binpacket=binpacket+'1100'
        elif i=='D': binpacket=binpacket+'1101'
        elif i=='E': binpacket=binpacket+'1110'
        elif i=='F': binpacket=binpacket+'1111'
        else: print('something wrong parsing the hex number') 
    return(binpacket)

def decodepacket(binpacket):
    #global nbitsread
    version=int(binpacket[0:3],2)
    # sumversion+=version
    packettype=int(binpacket[3:6],2)
    # if packettype==0: instruction.append('add')
    # if packettype==1: instruction.append('mult')
    # if packettype==2: instruction.append('min')
    # if packettype==3: instruction.append('max')
    # if packettype==5: instruction.append('gt')
    # if packettype==6: instruction.append('lt')
    # if packettype==7: instruction.append('eq')
    if packettype==0: instruction='add'
    if packettype==1: instruction='mult'
    if packettype==2: instruction='min'
    if packettype==3: instruction='max'
    if packettype==5: instruction='gt'
    if packettype==6: instruction='lt'
    if packettype==7: instruction='eq'
    
    
    #print(version,packettype)
    nbitsread=0
    if packettype==4: #literal container
        n=0
        chunk=''
        # print(n,binpacket[6+5*n:7+5*n])
        moretoread=binpacket[6+5*n:7+5*n]=='1'
        # print(moretoread)
        if binpacket[6+5*n:7+5*n]=='0':
            chunk=chunk+binpacket[7+5*n:11+5*n]
            moretoread=False
        while moretoread:
            chunk=chunk+binpacket[7+5*n:11+5*n]
            #print(chunk)
            n+=1
            if binpacket[6+5*n:7+5*n]=='0':
                chunk=chunk+binpacket[7+5*n:11+5*n]
                moretoread=False
        #print('literal',int(chunk,2))
        #instruction.append('literal ' + str(int(chunk,2)))
        
        #nbitsread+=11+5*n
        #print(nbitsread)
        #return(version,packettype,nbitsread)
        remainder=binpacket[11+5*n:]
        #instruction.append('bitsread '+ str(11+5*n))
        #print(remainder)
        if '1' in remainder:
            stack.append(remainder)
        #print('processed command was',binpacket[:11+5*n],'literal',int(chunk,2),11+5*n,'bits read')
        f.write('processed command '+str(binpacket[:11+5*n])+' literal '+str(int(chunk,2)) +' '+str(11+5*n) +' bits read')
        #print(stack)
        stack.pop(0)
        
    else: #operator
        lentype=int(binpacket[6:7],2)
        #print('operator type',lentype)
        if lentype==0:
            nbits=int(binpacket[7:22],2) #22 is 7 + 15
            #print(nbits)
            #instruction.append('nbits to read '+ str(nbits))
            shortpacket=binpacket[22:22+nbits]
            #print(binpacket)
            #print(shortpacket)
            stack.append(shortpacket)
            #decodepacket(shortpacket)
            remainder=binpacket[22+nbits:]
            #print(remainder)
            if '1' in remainder:
                stack.append(remainder)
            #print('processed command was',binpacket[:22+nbits],'instruction',instruction,nbits,'bits',22+nbits,'bits read')
            f.write('processed command '+str(binpacket[:22+nbits])+' instruction '+str(instruction)+' '+str(nbits) +' bits '+str(22+nbits)+' bits read')
            #print(stack)
            stack.pop(0)
            # while nbitsread<nbits:
            #     shortpacket=shortpacket[nbitsread:]
            #     a,b,bitsread=decodepacket(shortpacket)
            #     nbitsread+=bitsread
            #     print(nbitsread)
            #     #print('in while')
        elif lentype==1:
            npackets=int(binpacket[7:18],2) #18 is 7 + 11
            #print(nbits)
            
            #print('operator 1 npackets',npackets)
            #instruction.append('bits read 18')
            #instruction.append('packets to read '+ str(npackets))
            # for j in range(npackets):
            #     shortpacket=binpacket[18+11*j:818+11+11*j]
            #     print(shortpacket)
            #     stack.append(shortpacket)
            # #print(shortpacket)
            
            # remainder=binpacket[18+11+11*j:]
            remainder=binpacket[18:]
            #print('remainder',remainder)
            if '1' in remainder:
                stack.append(remainder)
            #print('processed command was',binpacket[:18],'instruction',instruction,npackets,'packets 18 bits read')
            f.write('processed command '+str(binpacket[:18])+' instruction '+str(instruction)+' '+str(npackets)+' packets 18 bits read')
            #print(stack)
            stack.pop(0)
            
            # while nbitsread<nbits:
            #     shortpacket=shortpacket[nbitsread:]
            #     a,b,bitsread=decodepacket(shortpacket)
            #     nbitsread+=bitsread
            #     print(nbitsread)
            #     #print('in while')
    return version
           
               
            
            
    
binpacket=hex2bin(packet)
stack=[binpacket]
sumversion=0
instruction=list()
#print(stack)
while stack:
    sumversion+=decodepacket(stack[0])
    #print(stack)
    print('sumversion',sumversion)

f.close()

   

   