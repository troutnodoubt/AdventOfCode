
fname="day_20_example.txt"
fname="input_day20.txt"
with open(fname) as fp: data = fp.read().splitlines()


# pad dark
# scan image
# calculate new value
# generate new image

def paddark(image):
    width=len(image[0])
    height=len(image)
    padwidth=3
    paddedimage=[['.' for _ in range(width+2*padwidth)]for _ in range(height+2*padwidth)]
    for i in range(height):
        for j in range(width):
            paddedimage[i+padwidth][j+padwidth]=image[i][j]
    return(paddedimage)

def padlight(image):
    width=len(image[0])
    height=len(image)
    padwidth=3
    paddedimage=[['#' for _ in range(width+2*padwidth)]for _ in range(height+2*padwidth)]
    for i in range(height):
        for j in range(width):
            paddedimage[i+padwidth][j+padwidth]=image[i][j]
    return(paddedimage)

def getpixelvalue(image,i,j):
    if image[i-1][j-1]=='#':
        pixelvalue='1'
    else:
        pixelvalue='0'
    if image[i-1][j]=='#':
        pixelvalue=pixelvalue+'1'
    else:
        pixelvalue=pixelvalue+'0'
    if image[i-1][j+1]=='#':
        pixelvalue=pixelvalue+'1'
    else:
        pixelvalue=pixelvalue+'0'
    if image[i][j-1]=='#':
        pixelvalue=pixelvalue+'1'
    else:
        pixelvalue=pixelvalue+'0'
    if image[i][j]=='#':
        pixelvalue=pixelvalue+'1'
    else:
        pixelvalue=pixelvalue+'0'
    if image[i][j+1]=='#':
        pixelvalue=pixelvalue+'1'
    else:
        pixelvalue=pixelvalue+'0'
    if image[i+1][j-1]=='#':
        pixelvalue=pixelvalue+'1'
    else:
        pixelvalue=pixelvalue+'0'
    if image[i+1][j]=='#':
        pixelvalue=pixelvalue+'1'
    else:
        pixelvalue=pixelvalue+'0'
    if image[i+1][j+1]=='#':
        pixelvalue=pixelvalue+'1'
    else:
        pixelvalue=pixelvalue+'0'
    return(int(pixelvalue,2))
    
def filteredvalue(filt,pixelvalue):
    return(filt[pixelvalue])


def processimage(image,filt):
    if image[0][0]=='.': image=paddark(image)
    if image[0][0]=='#': image=padlight(image)
    
    width=len(image[0])
    height=len(image)
    newimage=list()
    for i in range(1,height-1):
        newimagerow=list()
        for j in range(1,width-1):
            a=getpixelvalue(image,i,j)
            newimagerow.append(filteredvalue(filt,a))
        newimage.append(newimagerow)
    return(newimage)

filt=data[0]
image=data[2:]

#[print(row) for row in image]
image=paddark(image)

for _ in range(50):
    image=processimage(image,filt)


nhash=0
for row in image:
    nhash+=row.count('#')
    
print('Part 1 solution is',nhash)