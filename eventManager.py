from dp_preprocessor import DP_preprocessor
from gesture import Gesture
from dp_recognizer import DP_recognizer
from dataManager import templates
class EventManager():
    # initialized the eventManager
    def __init__(self, canvasManager):
        self.canvasManager = canvasManager
        self.currentGesture = Gesture(DP_preprocessor(), canvasManager=self.canvasManager, debug=self.canvasManager.showDebug.get())
        self.recognizer = DP_recognizer(templates)
        self.stroke_id = 0
    def bindEvents(self):
        # Mainains the previous x and y value of mouse.
        prevX, prevY = 0, 0

        # function that is called when the mouse is moved while being held down
        def mouseDownMoveEvent(event):
            nonlocal prevX, prevY
            # creates a line from the previous x and y to the new x and y of the mouse
            self.canvasManager.canvas.create_line(prevX, prevY, event.x, event.y)
            # store the captured point of the gesture
            self.currentGesture.addPoint(event.x, event.y, self.stroke_id)
            # print(prevX, prevY)
            # updates the previous x and y value of the mouse.
            prevX, prevY = event.x, event.y
        # binds the event to canvas
        self.canvasManager.canvas.bind('<B1-Motion>', mouseDownMoveEvent)
        
        # function that is called when the mouse button 1 is pressed.
        def mouseDownEvent(event):
            nonlocal prevX, prevY
            # set the previous x and y of the mouse.
            prevX, prevY = event.x, event.y
            # increment the stroke id for every stroke
            self.stroke_id += 1
            # reset the geture when mouse button 1 is pressed
            # self.currentGesture = Gesture(canvasManager=self.canvasManager, debug=self.canvasManager.showDebug.get())
            # clear the canvas
            # clearEvent(None)
            # create a larger dot where the stroke starts
            self.canvasManager.canvas.create_oval(event.x-3, event.y-3, event.x+3, event.y+3, fill="BLACK")
        # binds the event to canvas
        self.canvasManager.canvas.bind('<ButtonPress-1>', mouseDownEvent)

        # function that is called when mouse button 1 is released.
        def mouseUpEvent(event):
            # get the recognized label of the gesture
            label, score, n_best, _ = self.currentGesture.getLabel(self.recognizer)
            print(n_best)
            displayString = "Gesture: {} | score:{}".format(label, score)
            # display the recognized label
            self.canvasManager.setDisplayText(displayString)
        # commented because it is not being used for multi stroke gestures
        # self.canvasManager.canvas.bind('<ButtonRelease-1>', mouseUpEvent)

        def recognizeEvent(event):
            print(self.currentGesture)
            # get the recognized label of the gesture
            label, score, n_best, _ = self.currentGesture.getLabel(self.recognizer)
            print(n_best)
            displayString = "Gesture: {} | score:{}".format(label, score)
            # display the recognized label
            self.canvasManager.setDisplayText(displayString)
            # resets the current gesture
           
            self.currentGesture = Gesture(DP_preprocessor(), canvasManager=self.canvasManager, debug=self.canvasManager.showDebug.get())
        # binds the event to canvas
        self.canvasManager.recognizeButton.bind('<Button-1>', recognizeEvent)

        # function that is called when the clear button is clicked
        def clearEvent(event):
            # resets the stroke id
            self.stroke_id = 0
            # resets the current gesture
            self.currentGesture = Gesture(DP_preprocessor(), canvasManager=self.canvasManager, debug=self.canvasManager.showDebug.get())
            # clears the canvas
            self.canvasManager.canvas.delete("all")
            # clears the displayed label
            self.canvasManager.setDisplayText("")
        # binds the event to canvas
        self.canvasManager.clearButton.bind('<Button-1>', clearEvent)

        # Function that will display a random gesture from xml log for testing
        def showRandomOffline(event):
            from xmlGestureReader import XmlGestureReader
            reader = XmlGestureReader()
            gesture = reader.readGesture('user_xml_logs/s02/medium/left-curly-brace01.xml', self.canvasManager, True)
            print(gesture.targetLabel)
        # commented as it not used for this version
        # self.canvasManager.showOffline.bind('<Button-1>', showRandomOffline)
        