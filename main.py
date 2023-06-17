import argparse
from d1_preprocessor import D1_preprocessor
from d1_recognizer import D1_recognizer
from dataCollectionCanvasManager import DataCollectionCanvasManager
from offlineRecognition import offlineRecognition
from canvasManager import CanvasManager


parser = argparse.ArgumentParser()

# Used for command line arguements to pick what action to run
parser.add_argument('-u','--user',  default=1, type=int,const=0,
              help='The number of the user starting from 1', nargs='?')
parser.add_argument("--analyze", help="perform offline recognition on data", action='store_true')
parser.add_argument("--recognize", help="perform offline recognition on data", action='store_true')
parser.add_argument("-d", "--dataset", help="mmg or d1", default="mmg")
parser.add_argument("-r", "--recognizer", help="d1 or dp", default="d1")
parser.add_argument("-o", "--output", help="output file name", default="logs.csv")
# sample command for offline recognition
# python main.py --analyze -d mmg -r d1 -o logs.csv
args = parser.parse_args()
if args.analyze:
    offlineRecognition(datasetName=args.dataset, recognizer=args.recognizer, output=args.output)
elif args.recognize:
    canvasManager = CanvasManager()
    # instantiate the window, canvas and button
    canvasManager.create()

    # display the window, canvas and button
    canvasManager.show()
else:
    
    userNumber = args.user

    gestures = ["triangle",
                "x",
                "rectangle",
                "circle",
                "check",
                "caret",
                "zig-zag",
                "arrow",
                "left-square-bracket",
                "right-square-bracket",
                "v",
                "delete",
                "left-curly-brace",
                "right-curly-brace",
                "star",
                "pigtail"]

    # creates an object of DataCollectionCanvasManager that intantiates, creates and maintains the window, canvas and buttons for data collection.
    canvasManager = DataCollectionCanvasManager(gestures, 10, userNumber)

    # instantiate the window, canvas and button
    canvasManager.create()

    # display the window, canvas and button
    canvasManager.show()

