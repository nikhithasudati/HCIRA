import os
# used to write the gesture to xml
def writeGestureXml(gesture, gestureType, number, userNumber):
    # gives a unique name to the gesture based on the type and iteration number
    Name = gestureType + ("0"+str(number))[-2:]
    # the number of the subject
    Subject = str(userNumber)
    # the name and path to the file where the gesture is stored
    filename = "user_xml_logs/s{}/medium/{}.xml".format(("0"+str(Subject))[-2:], Name)
    # Creates the starting of the file where the root node begins
    xmlStr = """<?xml version="1.0" encoding="utf-8" standalone="yes"?>\n<Gesture Name="{}" Subject="{}" Speed="medium">\n""".format(Name, Subject)
    # Nodes for each point in the gesture
    pointsStrs = "\n".join(["""\t<Point X="{}" Y="{}" T="{}"/>""".format(point.x, point.y, idx+1)
     for idx, point in enumerate(gesture.points)])
    # end of the gesture node
    xmlStrEnd = "\n</Gesture>"
    # create the string for the xml
    xmlFinalStr = xmlStr + pointsStrs + xmlStrEnd
    # if the directory does not already exists, create it
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    # open the file
    f = open(filename, "w")
    # write to the file
    f.write(xmlFinalStr)
    # close the file
    f.close()