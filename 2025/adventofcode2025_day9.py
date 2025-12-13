
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
        


# def point_in_polygon(polygon, point):
#     num_vertices = len(polygon)
#     x, y = point[0], point[1]
#     inside = False

#     # Store the first point in the polygon and initialize the second point
#     p1 = polygon[0]

#     # Loop through each edge in the polygon
#     for i in range(1, num_vertices + 1):
#         # Get the next point in the polygon
#         p2 = polygon[i % num_vertices]

#         # Check if the point is above the minimum y coordinate of the edge
#         if y > min(p1[1], p2[1]):
#             # Check if the point is below the maximum y coordinate of the edge
#             if y <= max(p1[1], p2[1]):
#                 # Check if the point is to the left of the maximum x coordinate of the edge
#                 if x <= max(p1[0], p2[0]):
#                     # Calculate the x-intersection of the line connecting the point to the edge
#                     x_intersection = (y - p1[1]) * (p2[0] - p1[0]) / (p2[1] - p1[1]) + p1[0]

#                     # Check if the point is on the same line as the edge or to the left of the x-intersection
#                     if p1[0] == p2[0] or x <= x_intersection:
#                         # Flip the inside flag
#                         inside = not inside

#         # Store the current point as the first point for the next iteration
#         p1 = p2

#     # Return the value of the inside flag
#     return inside

biggesta=0
biggestgreen=0
polygon=[]
for point1 in data:
    polygon.append((int(point1.split(',')[0]),int(point1.split(',')[1])))
# print("pointtests")
# print(point_in_polygon(polygon,(7,1)))
# print(point_in_polygon(polygon,(8,1)))
# print(point_in_polygon(polygon,(9,1)))
# print(point_in_polygon(polygon,(10,1)))
# print(point_in_polygon(polygon,(11,1)))
# print(point_in_polygon(polygon,(12,1)))
# print(point_in_polygon(polygon,(9,2)))
# print(point_in_polygon(polygon,(11,7)))
# print(point_in_polygon(polygon,(3,3)))
# print(point_in_polygon(polygon,(3,4)))
# print(point_in_polygon(polygon,(8,3)))
# print()
for i,point1 in enumerate(data):
     print(i+1," of ",len(data))
     for point2 in data:
        if point1!=point2:
            p1=(int(point1.split(',')[0]),int(point1.split(',')[1]))
            p2=(int(point2.split(',')[0]),int(point2.split(',')[1]))
            a=area(p1,p2)
            # print(p1,p2,oppositeCorners(p1,p2))
            testedges=perimeter(p1,p2)
            isgreen=True
            for edgepoint in testedges:
            # for edgepoint in oppositeCorners(p1,p2):
                # print(edgepoint,point_in_polygon(polygon,edgepoint))
                # print(not point_in_polygon(polygon,edgepoint) and not (edgepoint != p1 and edgepoint != p2))
                if not point_in_polygon(polygon,edgepoint) and not point_on_polygon_edge(polygon,edgepoint):
                    
                    # print("not green",p1,p2)
                    isgreen=False
                    break
            if isgreen:
                # print("green",p1,p2,a)
                if a>biggestgreen: biggestgreen=a
            # else: break   
            
            
            if a>biggesta: biggesta=a

print("Part 1 solution ",biggesta)
print("Part 2 solution ",biggestgreen)

# part 2:

# define perimeter of test area
# if any point on perimeter not in red/green area, move to the next test area
# check if points are in red green area with raytracing algorithm, see 2023 day 10
