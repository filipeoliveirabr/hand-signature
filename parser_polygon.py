import polygon as Polygon
    
def points_to_polygon(points):
    polygon = Polygon.Polygon()
    
    for point in points:
        polygon.addPoints(point[0][0], point[0][1])
    
    return polygon