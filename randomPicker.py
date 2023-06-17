import random
# picks stratified random set of E templates and a candidate
def stratified_random_templates_and_candidate(E, gestures):
    candidatates = []
    templates = []
    for gestureType in gestures:
        # picking random sample of E+1 elements without replacement.
        # E+1 so that candidate is not in templates
        randomGestures = random.sample(gestures[gestureType], k=E+1)
        currentCandidate = randomGestures[-1]
        currentTemplates = randomGestures[:-1]
        templates.extend(currentTemplates)
        candidatates.append(currentCandidate)
    return candidatates, templates