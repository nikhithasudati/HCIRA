from point import Point
import math


class DP_preprocessor():
    def __init__(self):
        # Number of points in the resampled gesture
        self.n = 32

    # Function to calculate the path length of the gesture
    def path_length(self, points):
        d = 0
        for i in range(1, len(points)):
            if points[i].stroke_id == points[i-1].stroke_id:
                d = d+points[i].distance(points[i-1])
        return d

    # Function to resample the Points
    def resample(self, points):
        I = self.path_length(points)/(self.n-1)
        D = 0
        newPoints = [points[0]]
        i = 1
        while i < len(points):
            if points[i].stroke_id == points[i-1].stroke_id:
                d = points[i].distance(points[i-1])
                if (D + d) >= I:
                    qx = points[i-1].x + ((I-D)/d)*(points[i].x - points[i-1].x)
                    qy = points[i-1].y + ((I-D)/d)*(points[i].y - points[i-1].y)
                    q = Point(qx, qy, points[i].stroke_id)
                    newPoints.append(q)
                    points.insert(i,q)
                    D = 0
                else:
                    D = D + d
            i += 1
        # Sometimes the algorithm misses the final point
        if len(newPoints) < self.n:
            newPoints.append(points[-1])
        if len(newPoints) < self.n:
            print("Error in resampling", len(newPoints), self.n)
        return newPoints

    # function to calculate centeroid of points
    def centeroid(self, points):
        xSum = sum(point.x for point in points)
        ySum = sum(point.y for point in points)
        centeroid = Point(xSum/len(points), ySum/len(points))
        return centeroid

    #Funtion to translate the points
    def translate_to(self, points, k):
        newPoints = []
        c = self.centeroid(points)
        for p in points:
            qx = p.x + k.x - c.x
            qy = p.y + k.y - c.y
            newPoints.append(Point(qx, qy))
        return newPoints

    def scale(self, points):
        xMin = float('inf')
        yMin = float('inf')
        xMax = float('0')
        yMax = float('0')
        for p in points:
            xMin = min(xMin, p.x)
            yMin = min(yMin, p.y)
            xMax = max(xMax, p.x)
            yMax = max(yMax, p.y)
        scale = max(xMax - xMin, yMax - yMin)
        newPoints = []
        for p in points:
            qx = (p.x - xMin)/scale*250
            qy = (p.y - yMin)/scale*250
            newPoints.append(Point(qx, qy))
        return newPoints
    
    # Function to run $1 algorithm
    def preprocess(self, points):
        # Resample the points
        resampledPoints = self.resample(points)
        # scale points to size 250
        scaledPoints = self.scale(resampledPoints)
        # translate the points to 250, 250 so that it is visible when displayed on the screen
        translatedPoints = self.translate_to(scaledPoints,  Point(250,250))
        # if the debug flag is set true, the processed points will be displayed on the canvas
        return translatedPoints
