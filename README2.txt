In part 2 of Project 1, we implement $1 Algorithm

Team Members
1. Param Gupta
2. Nikhitha Sudati

Running the demo
1. open the project folder on the terminal
2. run `python3 main.py`

Project Structure
Our project contains 3 files:-
1. main.py :- The entry point of the project
2. canvasManager.py :- contains the CanvasManager class that is responsible for maintaining the window and the canvas. Object of this class is created in main.py
3. eventManager.py :- contains the EventManager class that is responsible for binding and contains all functions that are called when an event is called. An object of this class is created within CanvasManager.
4. d1_preprocessor.py :- contains the D1_recognizer class that have the implementation of all steps of preprocessor in $1 algorithm
5. d1_recognizer.py :- contains the D1_recognizer class that has the implementation of $1 recognition algorithm that recognizes a gesture given processed points and list of templates.
6. gesture.py :- contains the Gesture class. Objects of this class will containe points. It has a getLabel function that will either return a stored label or it will use the $1 algoithm to recognize the algorithm.
7. point.py :- contains the Point class that will be used to store individual points. It also contains simple operations of points.
8. templateManager.py :- contains the function that loads the templates. For this project, the templates are hard coded.

a) Store the Points
Points will be stored as list of objects of Point class. An object of Gesture class will containi the list. On line 32 of eventManager.py, an empty gesture is created when is pressed. On line 18 of eventManager.py a point is added to the gesture when the mouse is moved. In gesture.py in line 24 is a funtion called addPoint. It will create an object of Point class and add it to the list of points.
b) Store some Templates
templateManager.py contains the list of objects of class Gesture for each template. Line 8 in templateManager.py will create a the Gesture object for each template. In line 12 of gesture.py, these points of the template are processed using the processing steps of the $1 algorithm.
c) Implement $1 Algorithm
When the getLabel function in gesture.py in line 30 is called, the ponits are processed and recognized. d1_recognizer.py has all the functions for processing the points.
    1) resampling :- d1_preprocessor.py has a function called resample on line 19 that is responsible for resampling the points.
    2) rotation :- d1_preprocessor.py has a function called rotate on line 65 that is responsible for rotating the points by -indicativeAngle.
    3) scaling + translation :- d1_preprocessor.py has a function called scale_to on line 78 and a function called translate_to on line 88 that are responsible for scaling and translating the points. Points are scaled to 250 and translated to middle of the screan for displaying the processed points.
    4) matching process :- d1_recognizer.py has functions that implement the $1 recognition process. 
In eventManager.py on line 41 is a function called mouseUpEvent that is called when the mouse is up after drawing a gesture. This will call the getLabel function, which will recognize the gesture.
d) Output the Result :- Line 19 in canvasManager.py create a text label on the screen. The recognized label of the gesture and the score will be displayed in this. On line 39 in canvasManager.py is a function called setDisplayText that can be called to display any text on the window. Line 45 in eventManager.py will call this function with the recogized label of the gesture. 

Display processed points
In line 43 of canvasManager.py is function drawDebugPoints that draws a list of points on the canvas. Line 51 of d1_recognizer.py drawDebugPoints function will be called with the debug points if the debug checkbox is checked.

Note:-
In our video submission, we can see that once left square bracket was misrecognized as left curly bracket. We tested the official online demo and found that when we draw left sqaure bracket with short horizontal line, it also incorrectly recognized left curly bracket.