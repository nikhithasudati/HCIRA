import xml.etree.ElementTree as ET
from offlineGesture import OfflineGesture
from point import Point
# Expected format of the xml
# <Gesture Name="arrowXX" Subject="1" Speed="fast">
#   <Point X="69" Y="228" T="1363112" />
#   <Point X="67" Y="228" T="1363125" />
#   .
#   .
# </Gesture>
class XmlGestureReader:
    def readGesture(self, filePath, preprocessor, canvasManager = None, debug=False):
        # parse the xml file
        tree = ET.parse(filePath)
        # get the gesture node in the xml
        gestureNode = tree.getroot()
        # get the label of the gesture from the node
        gestureLabel = gestureNode.get('Name')[:-2]
        subject = gestureNode.get('Subject')
        speed = gestureNode.get('Speed')
        pointsArray = []
        # get every point of the gesture
        for pointNode in gestureNode:
            xVal = int(pointNode.get('X'))
            yVal = int(pointNode.get('Y'))
            pointsArray.append(Point(xVal, yVal))
        # Generate a name for the gesture with user, gesture type and number
        name = "s"+("0"+subject)[-2:]+'-'+gestureLabel+ gestureNode.get('Name')[-2:]
        gesture = OfflineGesture(pointsArray, gestureLabel, name, subject, speed, preprocessor, canvasManager, debug)
        return gesture