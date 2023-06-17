from dataManager import loadMmgXMLDataset, loadXMLDataset
from dp_preprocessor import DP_preprocessor
from dp_recognizer import DP_recognizer
from randomPicker import stratified_random_templates_and_candidate
from d1_recognizer import D1_recognizer
from d1_preprocessor import D1_preprocessor
from collections import defaultdict
from logger import Logger

def offlineRecognition(datasetName, recognizer, output):
    if recognizer == 'd1':
        preprocessor = D1_preprocessor()
        Recognizer = D1_recognizer
    elif recognizer == 'dp':
        preprocessor = DP_preprocessor()
        Recognizer = DP_recognizer
    else:
        print("Unknown recognizer")
        return
    if datasetName == 'mmg':
        dataPath = 'mmg'
        dataset = loadMmgXMLDataset(dataPath, preprocessor=preprocessor)
    elif datasetName == 'd1':
        dataPath = 'xml_logs'
        dataset = loadXMLDataset(dataPath, preprocessor=preprocessor)
    else:
        print("Unknown dataset")
        return

    
    print('dataset loaded and pre-processed')

    # Implementation of User-dependent random-100 loop

    # number of iterations
    num_iterations = 1

    logger = Logger(output)
    # stores the score for each U, G that 0 by default
    ug_score = defaultdict(int)
    for uidx, user in enumerate(list(dataset)[:1]): # made it into a list so that we can easility set number of users for loop
        print("User " + user + " " + str(uidx+1) + "/" + str(len(dataset)) )
        for E in range(1, 10): # till 10 because right limit of range is exlusive
            print("\t E="+str(E))
            for i in range(1,num_iterations+1):
                print("\t\t iter="+str(i)+"/"+str(num_iterations))
                # Gets the random templates and candidates
                candidates, templates = stratified_random_templates_and_candidate(E, dataset[user]['medium'])
                recognizer = Recognizer(templates)
                # performs recognition for each gesture type
                for candidate in candidates:
                    res, score, n_best, match = candidate.getLabel(recognizer)
                    # write a row in the log file
                    logger.log(user, candidate.targetLabel, i, E, len(templates), "{"+",".join([t.name for t in templates])+"}", candidate.name, res, int(res == candidate.targetLabel), "%.2f" % score, match.name, n_best)
                    if res == candidate.targetLabel:
                        ug_score[(user, candidate.targetLabel)] += 1
    # get percentage of correctly recognized for each U, G                    
    for ug in ug_score:
        ug_score[ug] /= (num_iterations*9)
    finalAccuracy = sum(ug_score.values())/len(ug_score)
    print("final average accuracy:-", "%.2f" % (finalAccuracy*100), "%")
    # save the csv log file with accurance at the end.
    logger.finish(finalAccuracy)