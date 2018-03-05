import cv2
import parser_polygon
import util
import polygon as Polygon
from matplotlib import pyplot as plt

def print_line_from_polygon(image, polygon):
    index = 0
    for point in polygon.points:
        len(polygon.points)
        
        if index < len(polygon.points) - 1:
            cv2.line(image, (point.x, point.y), (polygon.points[index + 1].x, polygon.points[index + 1].y),(0,255,0), 2)
        else:
            cv2.line(image, (point.x, point.y), (polygon.points[0].x, polygon.points[0].y),(0,255,0), 2)
            
        index = index + 1

image     = cv2.imread('./examples/cut/1.jpg')
gray      = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY) 
blurred   = cv2.GaussianBlur(gray,(9,9),0)

th3 = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY,11,2)

threshold = cv2.adaptiveThreshold(blurred,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY, 11,1)

(_, contours,_) = cv2.findContours(threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

polygons = []
for contour in contours:
    hull = cv2.convexHull(contour)
    polygons.append( parser_polygon.points_to_polygon(hull) )

polygons_aux = []

#remove the bigest border
for polygon in polygons:
    if util.is_polygon_inside_polygon(polygon, polygons[0]):
        polygons_aux.append(polygon)

polygons = []

for polygon_a in polygons_aux:
    is_inside = False
    
    for polygon_b in polygons_aux:
        if util.is_polygon_inside_polygon(polygon_a, polygon_b):
            is_inside = True
            
    if not( is_inside ):
        polygons.append( polygon_a )

#for polygon in polygons:
    #print_line_from_polygon(image, polygon)


cv2.imshow("Gray", gray)
cv2.waitKey(0)


cv2.imshow("Image", image)
cv2.waitKey(0)

#plt.figure(1)
#plt.subplot(212)
#plt.imshow(gray)

#plt.subplot(211)
#plt.imshow(image)
#plt.show()