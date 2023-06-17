from point import Point
from d1_recognizer import D1_recognizer
from d1_preprocessor import D1_preprocessor
class Gesture():
    # contructor for gesture
    def __init__(self, preprocessor, points=None, targetLabel = None, name = "new", canvasManager=None, debug=False):
        self.preprocessor = preprocessor
        self.canvasManager = canvasManager
        self.debug = debug
        self.targetLabel = targetLabel
        self.name = name
        if points is None:
            self.points = []
            self.processed = False
        else:
            self.points =  self.preprocessor.preprocess(points[:])
            self.showDebug()
            self.processed = True

    # Function to display processed points on canvas
    def showDebug(self):
        if self.canvasManager and self.debug:
            print(len(self.points))
            self.canvasManager.drawDebugPoints(self.points)
    # function to add point to a label
    def addPoint(self, x, y, stroke_id=0):
        if self.processed:
            raise Exception("Cannot add points to a processed gesture")
        self.points.append(Point(x, y, stroke_id))

    # function to get the label of a gesture
    def getLabel(self, recognizer):
        # if the label is not already known or recognized, recognize it
        if len(self.points) < 2:
            return ""
        if not self.processed:
            # preprocess the points
            self.points =  self.preprocessor.preprocess(self.points[:])
            self.processed = True
            self.showDebug()
        # recognize the points
        return recognizer.recognize(self.points[:])
    def __str__(self):
        return "Gesture("+str(self.points)+")"
    def __repr__(self):
        return "Gesture("+str(self.points)+")"
