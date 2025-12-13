
fname='/home/mark/Documents/git/AdventOfCode/2025/input_day9.txt'
# fname='/home/mark/Documents/git/AdventOfCode/2025/example_day9.txt'


with open(fname) as fp: data = fp.read().splitlines()

def area(point1,point2):
    return (abs(point1[0]-point2[0])+1)*(abs(point1[1]-point2[1])+1)

def perimeter(point1,point2):
    per=set()
    topedge=[(point1[0],a) for a in range(min(point1[1],point2[1]),max(point1[1],point2[1])+1)]
    bottomedge=[(point2[0],a) for a in range(min(point1[1],point2[1]),max(point1[1],point2[1])+1)]
    leftedge=[(a,point1[1]) for a in range(min(point1[0],point2[0]),max(point1[0],point2[0])+1)]
    rightedge=[(a,point2[1]) for a in range(min(point1[0],point2[0]),max(point1[0],point2[0])+1)]
    for point in topedge: per.add(point)
    for point in bottomedge: per.add(point)
    for point in rightedge: per.add(point)
    for point in leftedge: per.add(point)
    return per

def oppositeCorners(point1,point2):
    return([(point2[0],point1[1]),(point1[0],point2[1])])

def point_in_polygon(polygon, point): #taken from https://www.algorithms-and-technologies.com/point_in_polygon/python
    """
    Raycasting Algorithm to find out whether a point is in a given polygon.
    Performs the even-odd-rule Algorithm to find out whether a point is in a given polygon.
    This runs in O(n) where n is the number of edges of the polygon.
     *
    :param polygon: an array representation of the polygon where polygon[i][0] is the x Value of the i-th point and polygon[i][1] is the y Value.
    :param point:   an array representation of the point where point[0] is its x Value and point[1] is its y Value
    :return: whether the point is in the polygon (not on the edge, just turn < into <= and > into >= for that)
    """

    # A point is in a polygon if a line from the point to infinity crosses the polygon an odd number of times
    odd = False
    # For each edge (In this case for each point of the polygon and the previous one)
    i = 0
    j = len(polygon) - 1
    while i < len(polygon) - 1:
        i = i + 1
        # If a line from the point into infinity crosses this edge
        # One point needs to be above, one below our y coordinate
        # ...and the edge doesn't cross our Y coordinate before our x coordinate (but between our x coordinate and infinity)

        if (((polygon[i][1] > point[1]) != (polygon[j][1] > point[1])) and (point[0] < (
                (polygon[j][0] - polygon[i][0]) * (point[1] - polygon[i][1]) / (polygon[j][1] - polygon[i][1])) +
                                                                            polygon[i][0])):
            # Invert odd
            odd = not odd
        j = i
    # If the number of crossings was odd, the point is in the polygon
    return odd

def point_on_polygon_edge(polygon, point):
    i = 0
    j = len(polygon) - 1
    onedge=False
    while i < len(polygon) - 1:
        i+=1
        if (point[0] == polygon[i][0] and point[0] == polygon[j][0] and 
            point[1] in range(min(polygon[i][1],polygon[j][1]),max(polygon[i][1],polygon[j][1])+1)):
                onedge|=True
        if (point[1] == polygon[i][1] and point[1] == polygon[j][1] and 
            point[0] in range(min(polygon[i][0],polygon[j][0]),max(polygon[i][0],polygon[j][0])+1)):
                onedge|=True
        j=i
    return onedge
        
biggesta=0
biggestgreen=0
polygon=[]
for point1 in data:
    polygon.append((int(point1.split(',')[0]),int(point1.split(',')[1])))

for i,point1 in enumerate(data):
     print(i+1," of ",len(data))
     for point2 in data:
        if point1!=point2:
            p1=(int(point1.split(',')[0]),int(point1.split(',')[1]))
            p2=(int(point2.split(',')[0]),int(point2.split(',')[1]))
            a=area(p1,p2)

            testedges=perimeter(p1,p2)
            isgreen=True
            for edgepoint in testedges:
                if not point_in_polygon(polygon,edgepoint) and not point_on_polygon_edge(polygon,edgepoint):
                    isgreen=False
                    break
            if isgreen:
                if a>biggestgreen: biggestgreen=a            
            
            if a>biggesta: biggesta=a

print("Part 1 solution ",biggesta)
print("Part 2 solution ",biggestgreen)

# part 2:

'''
This works and gives the right answer, but is highly inefficient. Would have been better to check
for intersecting lines to determine if a square was enclosed by the polygon rather than
every point, even with early exit on the point checks.
'''
