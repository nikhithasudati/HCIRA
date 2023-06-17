In part 5 of Project 1, we run random-100 loop on user collected data

Team Members
1. Param Gupta
2. Nikhitha Sudati

Running the demo
1. open the project folder on the terminal
2. run `python3 main.py --analyze

a) Run an Offline Recognition Test
Since the format of the xml files created in part 4 had the same format, the code for running the random-100 loop from part 3 was re-used and was run for each user repeating one time.

b) Output the Result
The same code from part 3 that run the random-100 loop

c) Analyze Dataset using GHoST
To analyze the gestures using GHoST, we wrote a script to add a T tag to each of the points in the xml files of the user collected data. Further we used a windows virtual machine on mac to run GHoST on mac. 

d) Extract User Articulation Insights
The variability was high on the ends of non closed shaped gestures. Further, for the closed shaped gestures, the variability was high on the corners. This implies that users are more consistent towards the middle of the gestures compared to the ends.