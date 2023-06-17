In part 3 of Project 1, we implement $1 Algorithm

Team Members
1. Param Gupta
2. Nikhitha Sudati

Running the demo
1. open the project folder on the terminal
2. run `python3 main.py`

Project Structure
Our project contains 3 files:-
1. main.py :- The entry point of the project
2. d1_preprocessor.py :- contains the D1_recognizer class that have the implementation of all steps of preprocessor in $1 algorithm
3. d1_recognizer.py :- contains the D1_recognizer class that has the implementation of $1 recognition algorithm that recognizes a gesture given processed points and list of templates.
4. gesture.py :- contains the Gesture class. Objects of this class will containe points. It will maintain a processed set of points with a target label and a function to recognize the points.
5. offlineGesture.py :- contains the OfflineGesture class that inherits from Gesture class. It also stores the subject and speed of the gesture.
5. point.py :- contains the Point class that will be used to store individual points. It also contains simple operations of points.
6. dataManager.py :- contains the function that loads the dataset.
7. logger.py :- contains the Logger class that has the functionality for writing to a csv file.
8. randomPicker.py :- contains the utility function that will randomly pick a stratified sample.
9. xmlGestureReader.py :- contain the class XmlGestureReader that the functionality of reading a gesture from an xml file.

a) Read in Dataset
In dataManager.py on line 15 is a function called loadXMLDataset. It will traverse the directory structure of the gesture logs and will load the gesture from xml file. xmlGestureReader.py contains the functionality for reading a gesture out of an xml file.

b) Connect to Recognizer
Line 29 of xmlGestureReader.py will create an object of OfflineGesture class that will preproceess the points on line 16 of gesture.py

c) Loop over Dataset
Line 28 in main.py has the implementation for random-100 loop. Line 35 in main.py choses E stratified random templates and a candidate without replacement. The implementation for getting the random is in randomPicker.py on line 3 in a function called stratified_random_templates_and_candidate. Line 39 in main.py calls the recognizer to get the recognized gesture type, score, n-best list and the specific template that was matched.

d) logger.py contains a Logger class that is responsible for wrting the csv log file. Line 6 in logger.py opens a csv file. Line 12 and 14 in logger.py adds the header to the csv file. Line 25 in main.py create an object of our Logger class. Line 16 of logger.py has a function called log that adds a row to the csv file.  Line 41 of main.py, writes each row in the log file after each recognition. 
logs1.csv contains the log file for 10 users and 10 iterations. logs2.csv contains the log file for 1 user and 1 iteration.