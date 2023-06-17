import tkinter
import tkinter.messagebox
from dataCollectionEventManager import DataCollectionEventManager
from gestureXmlWriter import writeGestureXml
class DataCollectionCanvasManager():
    def __init__(self, gestureList, numIters, user):
        self.gestureList = gestureList
        self.numIters = numIters
        self.currInstruction = 0
        self.gestures = []
        self.currentGesture = None
        self.user = user
    # This function create and stores instances of window, canvas and eventManager.
    def create(self):
        # creates window
        self.window = tkinter.Tk()
        # creates canvas
        self.canvas = tkinter.Canvas(self.window, bg="white", height=500, width=500)
        #creates clear button
        self.clearButton = tkinter.Button(self.window, text='clear')
        # creates the variable that stores the text to display on GUI
        self.instructionVar = tkinter.StringVar()
        self.instructionVar.set("Instruction 1/{}:- Draw {}".format(len(self.gestureList)*self.numIters, self.gestureList[0]))
        # creates label to display text on GUI
        self.guiLabel = tkinter.Label(self.window, textvariable=self.instructionVar)
        # creates the next button
        self.nextButton = tkinter.Button(self.window, text='next')
        # creates eventManager
        self.eventManager = DataCollectionEventManager(self)
        # binds all the events in eventManager
        self.eventManager.bindEvents()

    # function to show the window and the canvs    
    def show(self):
        # adds the instruction label to window
        self.guiLabel.pack()
        # adds clear button to window
        self.clearButton.pack()
        # adds the next button to the window
        self.nextButton.pack()
        # adds canvas to window
        self.canvas.pack()
        # shows the window
        self.window.mainloop()
    
    # function to display the next instruction
    def nextInstruction(self):
        # user cannot go the next instruction without drawing anything
        if self.currentGesture == None:
            tkinter.messagebox.showerror('Empty Gesture', 'Error:No gestures has been drawn!')
            return
        # writes the gestures of the previous instruction before moving to the next instruction
        writeGestureXml(self.currentGesture ,self.gestureList[self.currInstruction%len(self.gestureList)], self.currInstruction//len(self.gestureList)+1, self.user)
        self.gestures.append(self.currentGesture)
        # checks if all instructions have been completed
        if self.currInstruction == len(self.gestureList)*self.numIters-1:
            # If all instructions are completed, displays the message and closes the app
            tkinter.messagebox.showinfo('Done', 'All instructions have been completed')
            self.window.destroy()
            exit()
        self.currInstruction += 1
        # Display the text for the next instruction
        self.instructionVar.set("Instruction {}/{}:- Draw {}".format(self.currInstruction+1, len(self.gestureList)*self.numIters, self.gestureList[self.currInstruction%len(self.gestureList)]))
