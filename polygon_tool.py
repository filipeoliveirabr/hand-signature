import cv2
import parser_polygon
import util

class PolygonTool:

    def principal_contours(self, image):
        (_, contours, _) = cv2.findContours(image, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        return contours

    def print_rectangle(self, image, polygon):
        cv2.rectangle(image, (polygon.max_left().x, polygon.max_top().y),(polygon.max_rigth().x, polygon.max_bottom().y), (255, 0, 0), 2)

    def print_line_from_polygon( self, image, polygon):
        index = 0
        for point in polygon.points:
            if index < len(polygon.points) - 1:
                cv2.line(image, (point.x, point.y), (polygon.points[index + 1].x, polygon.points[index + 1].y),
                         (0, 255, 0), 2)
            else:
                cv2.line(image, (point.x, point.y), (polygon.points[0].x, polygon.points[0].y), (0, 255, 0), 2)
            index = index + 1

    def fit_contours( self, contours ):
        polygons = []
        for contour in contours:
            hull = cv2.convexHull(contour)
            polygons.append(parser_polygon.points_to_polygon(hull))

        polygons_aux = []

        # remove the bigest border
        for polygon in polygons:
            if util.is_polygon_inside_polygon(polygon, polygons[0]):
                polygons_aux.append(polygon)

        polygons = []

        for polygon_a in polygons_aux:
            is_inside = False

            for polygon_b in polygons_aux:
                if util.is_polygon_inside_polygon(polygon_a, polygon_b):
                    is_inside = True

            if not (is_inside):
                polygons.append(polygon_a)

        return polygons