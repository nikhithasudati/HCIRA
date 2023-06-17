from dp_preprocessor import DP_preprocessor
import math
class DP_recognizer():
    def __init__(self, templates):
        self.preprocessor = DP_preprocessor()
        self.templates = templates

    
    def cloud_distance(self, points, templ, n, start):
        matched = [False]*n
        Sum = 0
        i = start
        while True:
            minIndex = -1
            minVal = float('inf')
            for j in range(n):
                if not matched[j]:
                    d = points[i].distance(templ[j])
                    if d < minVal:
                        minVal = d
                        minIndex = j
            matched[minIndex] = True
            weight = 1 - ((i-start+n)%n)/n
            Sum = Sum + weight*minVal
            i = (i+1)%n
            if i == start:
                break
        return Sum
    
    def greedy_cloud_match(self, points, templ, n):
        eps = 0.5
        step = math.floor(math.pow(n, 1-eps))
        minVal = float('inf')
        for i in range(0, n, step):
            d1 = self.cloud_distance(points, templ, n, i)
            d2 = self.cloud_distance(templ, points, n, i)
            minVal = min(minVal, d1, d2)
        return minVal

    def recognize(self, points):
        n = len(points)
        n_best = {}
        minScore = float('inf')
        Td = None
        for template in self.templates:
            d = self.greedy_cloud_match(points, template.points, n)
            if d < minScore:
                minScore = d
                Td = template
            maxScore = min(1, 1/d)
            score = min(1, 1/d)
            n_best[template.name] = score
        if Td is None:
            return "", 0, {}
        sorted_n_best = {i:n_best[i] for i in sorted(n_best, key=lambda x:-n_best[x])}
        return Td.targetLabel, maxScore, sorted_n_best, Td


