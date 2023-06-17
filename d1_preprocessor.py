from point import Point
import math


class D1_preprocessor():
    def __init__(self):
        # Number of points in the resampled gesture
        self.n = 64
        # Size to scale the points to
        self.size = 250
    # Function to calculate the path length of the gesture
    def path_length(self, points):
        d = 0
        for i in range(1, len(points)):
            d = d+points[i].distance(points[i-1])
        return d

    # Function to resample the Points
    def resample(self, points):
        I = self.path_length(points)/(self.n-1)
        D = 0
        newPoints = [points[0]]
        i = 1
        while i < len(points):
            d = points[i].distance(points[i-1])
            if (D + d) >= I:
                qx = points[i-1].x + ((I-D)/d)*(points[i].x - points[i-1].x)
                qy = points[i-1].y + ((I-D)/d)*(points[i].y - points[i-1].y)
                q = Point(qx, qy)
                newPoints.append(q)
                points.insert(i,q)
                D = 0
            else:
                D = D + d
            i += 1
        # Sometimes the algorithm misses the final point
        if len(newPoints) < self.n:
            newPoints.append(points[-1])
        return newPoints

    # function to calculate centeroid of points
    def centeroid(self, points):
        xSum = sum(point.x for point in points)
        ySum = sum(point.y for point in points)
        centeroid = Point(xSum/len(points), ySum/len(points))
        return centeroid

    # Function to rotate the points by indicative angle
    def indicative_angle(self, points):
        c = self.centeroid(points)
        return math.atan2(c.y - points[0].y, c.x - points[0].x)

    #Function to ratate points by w
    def rotate_by(self, points, w):
        newPoints = []
        c = self.centeroid(points)
        for p in points:
            qx = (p.x - c.x) * math.cos(w) - (p.y - c.y)*math.sin(w) + c.x
            qy = (p.x - c.x) * math.sin(w) + (p.y - c.y)*math.cos(w) + c.y
            newPoints.append(Point(qx, qy))
        return newPoints
            

    #Function to Rotate Once Based on the “Indicative Angle”
    def rotate(self, points):
        newPoints = self.rotate_by(points, -self.indicative_angle(points))
        return newPoints

    #Function to calculate bounding box of points
    def bounding_box(self, points):
        minX = min(point.x for point in points)
        maxX = max(point.x for point in points)
        minY = min(point.y for point in points)
        maxY = max(point.y for point in points)
        return {"width":maxX-minX+0.001, "height":maxY-minY+0.001}

    #Function to scale the points to a given size
    def scale_to(self, points, size):
        b = self.bounding_box(points)
        newPoints = []
        for p in points:
            qx = p.x * size / b["width"]
            qy = p.y * size / b["height"]
            newPoints.append(Point(qx, qy))
        return newPoints

    #Funtion to translate the points
    def translate_to(self, points, k):
        newPoints = []
        c = self.centeroid(points)
        for p in points:
            qx = p.x + k.x - c.x
            qy = p.y + k.y - c.y
            newPoints.append(Point(qx, qy))
        return newPoints

    # Function to run $1 algorithm
    def preprocess(self, points):
        # Resample the points
        resampledPoints = self.resample(points)
        # rotate the points by indicative angle
        rotatedPoints = self.rotate(resampledPoints)
        # scale points to size 250
        scaledPoints = self.scale_to(rotatedPoints, self.size)
        # translate the points to 250, 250 so that it is visible when displayed on the screen
        translatedPoints = self.translate_to(scaledPoints,  Point(250,250))
        # if the debug flag is set true, the processed points will be displayed on the canvas
        return translatedPoints
