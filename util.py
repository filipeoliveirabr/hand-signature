import polygon as Polygon
import point as Point
from numba.cgutils import ifnot

def is_point_inside_poly(x, y, poly):

    n = len(poly.points)
    inside = False

    p1x = poly.points[0].x
    p1y = poly.points[0].y
    
    print(poly.points[0])
    print(p1x)
    print(p1y)
    print(y)
    
    
    
    for i in range(n+1):
        p2x = poly.points[i % n].x
        p2y = poly.points[i % n].y
        
        if y > min(p1y, p2y):
            if y <= max(p1y,p2y):
                if x <= max(p1x,p2x):
                    if p1y != p2y:
                        xints = (y-p1y)*(p2x-p1x)/(p2y-p1y)+p1x
                    if p1x == p2x or x <= xints:
                        inside = not inside
        p1x,p1y = p2x,p2y

    return inside


def is_polygon_inside_polygon(polygon_a, polygon_b):
    is_all_inside = True
    
    for point in polygon_a.points:
        
        if is_all_inside:
            is_all_inside = is_point_inside_poly(point.x, point.y, polygon_b)
        else:
            break;
            
    return is_all_inside