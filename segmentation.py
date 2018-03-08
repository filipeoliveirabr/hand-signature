import cv2
import polygon_tool as PolygonTool
from matplotlib import pyplot as plt

files = ['01.png', '02.png', '03.png', '04.png', '05.png']
images = []

for file in files:

    image     = cv2.imread('./examples/digital/'+file)
    gray      = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    blurred   = cv2.GaussianBlur(gray,(9,9),0)
    threshold = cv2.adaptiveThreshold(blurred, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY, 11,1)

    polygonTool = PolygonTool.PolygonTool()
    contours    = polygonTool.principal_contours(threshold)
    polygons    = polygonTool.fit_contours(contours)

    polygons_aux = []
    index = 0
    for polygon in polygons:
        if index < len(polygons) - 1:
            if( polygons[index].is_merge(polygons[index + 1]) ):
                polygons[index].merge_points(polygons[index + 1].points)
                polygons_aux.append(polygons[index])
                index = index + 1
            index = index + 1
    polygons = polygons_aux

    for polygon in polygons:
        polygonTool.print_rectangle(image, polygon)

    images.append(image)


for image in images:
    cv2.imshow("Image 1", image)
    cv2.waitKey(0)

