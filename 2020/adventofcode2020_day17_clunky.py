fname="C://Users/Mark/Documents/Advent of Code/2020/day_17_example.txt"
#fname="C://Users/Mark/Documents/Advent of Code/2020/input_day17.txt"
with open(fname) as fp: data = fp.read().splitlines()
        
#change to char list

for i in range(0,len(data)):
    data[i]=[a for a in data[i]]


#pad the array for the first time

size=max(len(data),len(data[0]))+4

tempdata=list()
tempdata=[['.' for a in range(size)] for b in range(size)]




zpad=list()
fulldata=list()
newlen=len(data[0])+2
for i in range(0,len(data)):
    data[i].insert(0,'.')
    data[i].append('.')



# data.insert(0,[a for a in newlen*'.'])
# data.append([a for a in newlen*'.'])
# tempdata=list()
# tempdata=data.copy()
# data=list()
# for i in range(0,len(tempdata[0])):
#     zpad.append([a for a in newlen*'.'])

# data.append([[field for field in row] for row in zpad])
# #data.append([[[field for field in row] for row in page] for page in tempdata])
# data.append([[field for field in row] for row in tempdata])
# data.append([[field for field in row] for row in zpad])


# cycles=0
# while cycles<6:
    
#     #pad again
#     zpad=list()
#     fulldata=list()
#     newlen=len(data[0])+2
#     npage=len(data)
#     width=len(data[0])
    
#     for k in range(0,npage):
#         for i in range(0,width):
#             data[k][i].insert(0,'.')
#             data[k][i].append('.')
    
#         data[k].insert(0,[a for a in newlen*'.'])
#         data[k].append([a for a in newlen*'.'])
#     tempdata=list()
#     tempdata=data.copy()
#     data=list()
    
    
#     for i in range(0,len(tempdata[0])):
#         zpad.append([a for a in newlen*'.'])
    
#     data.append([[field for field in row] for row in zpad])
#     for page in tempdata:
#     #data.append([[[field for field in row] for row in page] for page in tempdata])
#         data.append([[field for field in row] for row in page])
#     data.append([[field for field in row] for row in zpad])
    
    
    
    
#     #find changes
    
#     npage=len(data)
#     width=len(data[0])
#     tempdata=[[['.' for a in range(width)] for b in range(width)] for c in range(npage)]
    
#     for page in range(npage):#(0,npage-1):
#         #print(page)
#         for row in range(width):#(1,width-1):
#             #print(row)
#             for entry in range(width):#(1,width-1):
#                 #print(entry)
#                 #print(page,row,entry)
#                 #print(data[page][row][entry])
#                 neighbors=list()
#                 if row<width-1:
#                     if entry>0:
#                         if page>0:
#                             neighbors.append(data[page-1][row+1][entry-1])
#                         neighbors.append(data[page+0][row+1][entry-1])
#                         if page<npage-1:
#                             neighbors.append(data[page+1][row+1][entry-1])
#                     if page>0:
#                         neighbors.append(data[page-1][row+1][entry+0])
#                     neighbors.append(data[page+0][row+1][entry+0])
#                     if page<npage-1:
#                         neighbors.append(data[page+1][row+1][entry+0])
#                     if entry<width-1:
#                         if page>0:
#                             neighbors.append(data[page-1][row+1][entry+1])
#                         neighbors.append(data[page+0][row+1][entry+1])
#                         if page<npage-1:
#                             neighbors.append(data[page+1][row+1][entry+1])
      
#                 if True:
#                     if entry>0:
#                         if page>0:
#                             neighbors.append(data[page-1][row+0][entry-1])
#                         neighbors.append(data[page+0][row+0][entry-1])
#                         if page<npage-1:
#                             neighbors.append(data[page+1][row+0][entry-1])
#                     if page>0:
#                         neighbors.append(data[page-1][row+0][entry+0])
#                     #omit, active cube neighbors.append(data[page+0][row+0][entry+0])
#                     if page<npage-1:
#                         neighbors.append(data[page+1][row+0][entry+0])
#                     if entry<width-1:
#                         if page>0:
#                             neighbors.append(data[page-1][row+0][entry+1])
#                         neighbors.append(data[page+0][row+0][entry+1])
#                         if page<npage-1:
#                             neighbors.append(data[page+1][row+0][entry+1])
                            
#                 if row>0:
#                     if entry>0:
#                         if page>0:
#                             neighbors.append(data[page-1][row-1][entry-1])
#                         neighbors.append(data[page+0][row-1][entry-1])
#                         if page<npage-1:
#                             neighbors.append(data[page+1][row-1][entry-1])
#                     if page>0:
#                         neighbors.append(data[page-1][row-1][entry+0])
#                     neighbors.append(data[page+0][row-1][entry+0])
#                     if page<npage-1:
#                         neighbors.append(data[page+1][row-1][entry+0])
#                     if entry<width-1:
#                         if page>0:
#                             neighbors.append(data[page-1][row-1][entry+1])
#                         neighbors.append(data[page+0][row-1][entry+1])
#                         if page<npage-1:
#                             neighbors.append(data[page+1][row-1][entry+1])
      
        
      
#     # =============================================================================
#     #             neighbors.append(data[page-1][row+0][entry-1])
#     #             neighbors.append(data[page+0][row+0][entry-1])
#     #             neighbors.append(data[page+1][row+0][entry-1])
#     #             neighbors.append(data[page-1][row+0][entry+0])
#     #             #0,0,0 is the middle of the cube and is omitted
#     #             neighbors.append(data[page+1][row+0][entry+0])
#     #             neighbors.append(data[page-1][row+0][entry+1])
#     #             neighbors.append(data[page+0][row+0][entry+1])
#     #             neighbors.append(data[page+1][row+0][entry+1])
#     #             
#     #             neighbors.append(data[page-1][row-1][entry-1])
#     #             neighbors.append(data[page+0][row-1][entry-1])
#     #             neighbors.append(data[page+1][row-1][entry-1])
#     #             neighbors.append(data[page-1][row-1][entry+0])
#     #             neighbors.append(data[page+0][row-1][entry+0])
#     #             neighbors.append(data[page+1][row-1][entry+0])
#     #             neighbors.append(data[page-1][row-1][entry+1])
#     #             neighbors.append(data[page+0][row-1][entry+1])
#     #             neighbors.append(data[page+1][row-1][entry+1])
#     # =============================================================================
                
                
               
#                 #print(neighbors)
#                 #print(neighbors.count('#'))
#                 activecount=neighbors.count('#')
#                 if data[page][row][entry]=='#' and activecount==2:
#                     tempdata[page][row][entry]='#'
               
#                 if activecount==3:
#                     tempdata[page][row][entry]='#'
#                 #print(activecount,data[page][row][entry],tempdata[page][row][entry])
                
#     data=list()
#     data=tempdata.copy()       
#     cycles+=1 

# activecount=0
# for page in data:
#     for row in page:
#         for field in row:
#             if field=='#':
#                 activecount+=1
            


# print('Part 1 solution is', activecount)