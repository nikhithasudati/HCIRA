from d1_preprocessor import D1_preprocessor
from gesture import Gesture
from d1_recognizer import D1_recognizer
from dataManager import templates
class DataCollectionEventManager():
    # initialized the eventManager
    def __init__(self, canvasManager):
        self.canvasManager = canvasManager
        self.recognizer = D1_recognizer(templates)
    def bindEvents(self):
        # Mainains the previous x and y value of mouse.
        prevX, prevY = 0, 0

        # function that is called when the mouse is moved while being held down
        def mouseDownMoveEvent(event):
            nonlocal prevX, prevY
            # creates a line from the previous x and y to the new x and y of the mouse
            self.canvasManager.canvas.create_line(prevX, prevY, event.x, event.y)
            # store the captured point of the gesture
            self.canvasManager.currentGesture.addPoint(event.x, event.y)
            print(prevX, prevY)
            # updates the previous x and y value of the mouse.
            prevX, prevY = event.x, event.y
        # binds the event to canvas
        self.canvasManager.canvas.bind('<B1-Motion>', mouseDownMoveEvent)
        
        # function that is called when the mouse button 1 is pressed.
        def mouseDownEvent(event):
            nonlocal prevX, prevY
            # clear the canvas
            clearEvent(None)
            # set the previous x and y of the mouse.
            prevX, prevY = event.x, event.y
            # reset the geture when mouse button 1 is pressed
            self.canvasManager.currentGesture = Gesture(D1_preprocessor(), canvasManager=self.canvasManager, debug=False)
            
            # create a larger dot where the stroke starts
            self.canvasManager.canvas.create_oval(event.x-3, event.y-3, event.x+3, event.y+3, fill="BLACK")
        # binds the event to canvas
        self.canvasManager.canvas.bind('<ButtonPress-1>', mouseDownEvent)


        # function that is called when the clear button is clicked
        def clearEvent(event):
            # clears the canvas
            self.canvasManager.canvas.delete("all")
            self.canvasManager.currentGesture = None
         # binds the event to canvas
        self.canvasManager.clearButton.bind('<Button-1>', clearEvent)
        
        # function that is called when the next button is clicked
        def nextEvent(event):
            # saves the current gesture and changes to the next instruction
            self.canvasManager.nextInstruction()
            clearEvent(None)
        # binds the event to button
        self.canvasManager.nextButton.bind('<Button-1>', nextEvent)

       

