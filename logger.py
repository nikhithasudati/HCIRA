import csv

class Logger:
    def __init__(self, filename):
        # Open the file
        self.file = open(filename, 'w', newline='')
        # Create a csv writer
        self.writer = csv.writer(self.file)
        # The headers for the csv file
        header = ["User[all-users]", "GestureType[all-gestures-types]", "RandomIteration[1to100]", "#ofTrainingExamples[E]", "TotalSizeOfTrainingSet[count]", "TrainingSetContents[specific-gesture-instances]", "Candidate[specific-instance]", "RecoResultGestureType[what-was-recognized]", "CorrectIncorrect[1or0]", "RecoResultScore", "RecoResultBestMatch[specific-instance]", "RecoResultNBestSorted[instance-and-score]"]
        # Write top of the file
        self.writer.writerow(["Recognition Log: [Param Gupta & Nikhitha Sudati] // [$1] // [$1 dataset] // USER-DEPENDENT RANDOM-100"])
        # write the header
        self.writer.writerow(header)

    def log(self, user, gestureType, iteration, numE, totalTrainingSize, trainingContent, candidate, recognizedType, correct, score, match, nBest):
        # write each row in the log file
        nbestList = []
        for name in nBest:
            nbestList.append(name)
            nbestList.append("%.2f"%nBest[name])
        nBestStr = '{' + ",".join(nbestList[:100]) + "}" # only output upto 50 items in n-best list
        self.writer.writerow([user, gestureType, iteration, numE, totalTrainingSize, trainingContent, candidate, recognizedType, correct, score, match, nBestStr])
    
    def finish(self, acc=0):
        # write the accuracy at the end of the file
        self.writer.writerow(["TotalAvgAccuracy", acc])
        # close the file
        self.file.close()