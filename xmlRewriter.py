import xml.etree.ElementTree as ET
import os
filepath = "user_xml_logs/s01/medium/arrow01.xml"
folderPath = "user_xml_logs"


for user in os.listdir(folderPath):
        # required for mac
        if user == '.DS_Store':
            continue
        userFullDir = os.path.join(folderPath, user)
        for speed in os.listdir(userFullDir):
            # required for mac
            if speed == '.DS_Store':
                continue
            speedDir = os.path.join(userFullDir, speed)
            for gesture in os.listdir(speedDir):
                # required for mac
                if speed == '.DS_Store':
                    continue 
                gesturePath = os.path.join(speedDir, gesture)


                tree = ET.parse(gesturePath)
                gestureNode = tree.getroot()
                for idx, pointNode in enumerate(gestureNode):
                    pointNode.set('T', str(idx+1))
                tree.write(gesturePath)