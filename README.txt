In part 1 of Project 1, we create a canvas on that allows us to draw on the canvas and clear the canvas.

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
3. eventManager.py :- contains the EventManager class that for binding and contains all functions that are called when an event is called. An object of this class is created within CanvasManager.

Project details
a) set up the development environment
We used vsCode to work on the project with python. This gives as an easy environment to run, test and debug. We also use virtualenv with python 3.8.9 to work on a virtual environment for consistent development environment among teammates.

b) Instantiating the canvas
Tkinter is used to create and manage the window on which the canvas is created. In the file canvasManager.py, a CanvasManager class is present that manages the instances of window and canvas. It has a show function on line 18 that displays the canvas. In main.py, on line 4, 7 and 10, an object of CanvasManager is created and the show function is called. On line 7 and 9 in canvasManager.py, an instance of window and canvas is created. On line 22 and 24 in canvasManager.py, canvas is attached to the window and the window is displayed.

c) Listening for Mouse events
For event listening, we have created an EventManager class in eventManager.py. This contains all the functions that will be called when an event occurs and also binds the functions to the canvas. The canvasManager, line 13 of canvasManager.py, creates an eventManger and calls the method to bind the methods. On line 24 in eventManager.py, is the function 'mouseDownEvent' that is called on mouse down event. This stores the current mouse x and y values. On line 13 in eventManager.py, is the function 'mouseDownMoveEvent' that is called when mouse is moved while being held down. It draws a line on the canvas from the previous x and y to the new x and w of the mouse. It then prints the positions and updates the stored x and y values of the mouse.

d) Clearing the canvas
On line 11 in canvasManager.py, a button is created for clearing the canvas. On line 20 in canvasManager.py, the button is attached to the window. On line 32 in eventManager.py, is the function 'clearEvent' that is called when the button is clicked. this function simply just clears the canvas. On line 34 is the call that clears the canvas.


