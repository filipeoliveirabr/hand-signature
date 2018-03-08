import point as Point

class Polygon:

    def __init__(self):
        self.points = []

    def is_merge(self, polygon):
        is_width  = False
        is_heigth = False

        if ( polygon.max_left().x - self.max_rigth().x <= 10 ):
            is_width = True

        if (polygon.max_top().y - self.max_bottom().y <= 20):
            is_heigth = True

        return is_width and is_heigth

    def addPoints(self, x, y):
        self.points.append(Point.Point(x, y))

    def merge_points(self, points):
        self.points = self.points + points


    def max_rigth(self):
        max_point = None
        for point in self.points:
            if( max_point is None ):
                max_point = point
            elif( max_point.x  <  point.x ):
                max_point = point

        return max_point


    def max_left(self):
        max_point = None
        for point in self.points:
            if( max_point is None ):
                max_point = point
            elif( max_point.x  >  point.x ):
                max_point = point

        return max_point

    def max_top(self):
        max_point = None
        for point in self.points:
            if( max_point is None ):
                max_point = point
            elif( max_point.y  >  point.y ):
                max_point = point

        return max_point


    def max_bottom(self):
        max_point = None
        for point in self.points:
            if( max_point is None ):
                max_point = point
            elif( max_point.y  <  point.y ):
                max_point = point

        return max_point