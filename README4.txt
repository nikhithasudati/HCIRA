In part 4 of Project 1, we implement $1 Algorithm

Team Members
1. Param Gupta
2. Nikhitha Sudati

Running the demo
1. open the project folder on the terminal
2. run `python3 main.py -u <user number>`

Project Structure
Our project contains 3 files:-
1. main.py :- The entry point of the project
2. gesture.py :- contains the Gesture class. Objects of this class will contains points.
3. point.py :- contains the Point class that will be used to store individual points. It also contains simple operations of points.
4. gestureXmlWriter.py :- contains the writeGestureXml function that when given a gesture and its tags, write the xml file.
5. dataCollectionCanvasManager.py :- contains the DataCollectionCanvasManager class that maintains the canvas used for data collection.
6. dataCollectionEventManager.py :- contains the DataCollectionEventManager class that contains all the events for the canvas and is responsible for binding them to the canvas.

a) Write Gesture Files
The file gestureXmlWriter.py contains a function called writeGestureXml that is responsible for writing a gesture. On line 11 of gestureXmlWriter.py the starting of the xml file is generated. Line 12 in gestureXmlWriter.py will create the string for each of the point node for the xml file. Line 16 of gestureXmlWriter.py will add the ending of the xml file. Line 24 of gestureXmlWriter.py will finally write the generataed string for the xml file to the file.

b) Prompt for Specific Samples
Line 27 in main.py contains the name of all the gestures that will be asked of the user to draw. Line 45 of in main.py will create a the canvas manager of user collection map. This also has parameter which is set as 10 signifying the number of samples for each gesture that has to be collected. Line 63 in dataCollectionCanvasManager.py generates the string that will displayed after the next button is pressed. Line 53 in dataCollectionCanvasManager.py will write the gesture after the next button is pressed. Line 43 in dataCollectionEventManager.py will clear the gesture when the clear button is pressed.

c) Recruit 6 People
We recruited 6 people from our friends to provide gesture samples by explaining gestures and provided a printed copy of 16 gestures. We made sure to thoroughly explain the consent process to them and had them sign a consent form to participate. They were then presented with our app to draw the gestures in. The app prompted the users with instruction for what gesture to draw. The instructions were setup in a way that all gestures types were prompted before repeating a gesture type.

d) Submit Full Dataset
The user_xml_logs folder in our zip file consists of 6 folders for each users. Then inside the folder for each user, inside the medium folder there are 160 xml files each gesture. This is the same file structure and format as in the previous part of the project. So, the total zip file consists of 960 gesture samples. 'Consent forms' folder in the zip also contains the consent form for 6 users.