import tkinter
from eventManager import EventManager
class CanvasManager():
    # This function create and stores instances of window, canvas and eventManager.
    def create(self):
        # creates window
        self.window = tkinter.Tk()
        # creates canvas
        self.canvas = tkinter.Canvas(self.window, bg="white", height=500, width=500)
        #creates clear button
        self.clearButton = tkinter.Button(self.window, text='clear')
        # creates recognize button
        self.recognizeButton = tkinter.Button(self.window, text='recognize')
        # creates the variable that stores the text to display on GUI
        self.labelVar = tkinter.StringVar()
        # creates the variables that strores whether to show debug points
        self.showDebug = tkinter.IntVar()
        # create a checkbox for debug points toggle
        self.debugCheck = tkinter.Checkbutton(self.window, text='Show processed points',variable=self.showDebug, onvalue=1, offvalue=0,)
        # creates label to display text on GUI
        self.guiLabel = tkinter.Label(self.window, textvariable=self.labelVar)
        #creates a button to display a gesture from the logs
        self.showOffline = tkinter.Button(self.window, text='Show Gesture')
        # creates eventManager
        self.eventManager = EventManager(self)
        # binds all the events in eventManager
        self.eventManager.bindEvents()

    # function to show the window and the canvas    
    def show(self):
        # adds clear button to window
        self.clearButton.pack()
        # adds recognize button to window
        self.recognizeButton.pack()
        # adds the show button to window
        # commented this line because it is not used in this version of the app
        # self.showOffline.pack()
        # adds the show debug points checkbox to window
        self.debugCheck.pack()
        # adds the label to window
        self.guiLabel.pack()
        # adds canvas to window
        self.canvas.pack()
        # shows the window
        self.window.mainloop()
    
    # function to set the display text on GUI
    def setDisplayText(self, text):
        # set the value of the label that is stored on the GUI
        self.labelVar.set(text)
    # function to draw points during processing for testing
    def drawDebugPoints(self, points):
        for point in points:
            x1, y1 = (point.x - 1), (point.y - 1)
            x2, y2 = (point.x + 1), (point.y + 1)
            self.canvas.create_oval(x1, y1, x2, y2, fill="green")