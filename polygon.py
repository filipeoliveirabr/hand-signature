import point as Point

class Polygon:
    
    def __init__(self):
        self.points = []
        
    def addPoints(self, x, y):
        self.points.append(Point.Point(x, y))
        
    def print_points(self):
        for p in self.points:
            print("point ")
            print( p.x )
            print( p.y )