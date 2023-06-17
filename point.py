import math
class Point():
    def __init__(self, x, y, stroke_id = 0):
        self.x = x
        self.y = y
        self.stroke_id = stroke_id
    #overloading the add operator to add two points    
    def __add__(self, p1):
        return Point(self.x + p1.x, self.y + p1.y)
    # overloading the mul operator to multiple a point with a constant
    def __mul__(self, c):
        return Point(self.x * c, self.y * c)
    # Function to print a point to console
    def __str__(self):
        return "Point("+str(self.x) + ", " + str(self.y)+")" + (("strokeid(" + str(self.stroke_id) + ")") if self.stroke_id != 0 else "")
    def __repr__(self):
        return "Point("+str(self.x) + ", " + str(self.y)+")" + (("strokeid(" + str(self.stroke_id) + ")") if self.stroke_id != 0 else "")
    # function to get the distance with a point
    def distance(self, p1):
        return math.dist((self.x, self.y), (p1.x, p1.y))