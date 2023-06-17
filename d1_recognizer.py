from d1_preprocessor import D1_preprocessor
import math
class D1_recognizer():
    def __init__(self, templates):
        self.preprocessor = D1_preprocessor()
        self.templates = templates

    # Funtion to calculate the distance between 2 paths
    def path_distance(self, A, B):
        d = 0
        for i in range(len(A)):
            d = d + A[i].distance(B[i])
        return d/len(A)

    # Function to calculate the distance bwteen 2 paths at an angle
    def distance_at_angle(self, points, T, theta):
        newPoints = self.preprocessor.rotate_by(points, theta)
        d = self.path_distance(newPoints, T)
        return d

    # Finds the distance which is at the best angle using the algorithm in the paper
    def distance_at_best_angle(self, points, T, thetaA, thetaB, thetaD):
        # constant value from paper
        phi = 0.61803
        x1 = phi*thetaA + (1 - phi)*thetaB
        f1 = self.distance_at_angle(points, T, x1)
        x2 = (1-phi)*thetaA + phi*thetaB
        f2 = self.distance_at_angle(points, T, x2)
        while abs(thetaB - thetaA) > thetaD:
            if f1 < f2:
                thetaB = x2
                x2 = x1
                f2 = f1
                x1 = phi*thetaA + (1-phi)*thetaB
                f1 = self.distance_at_angle(points, T, x1)
            else:
                thetaA = x1
                x1 = x2
                f1 = f2
                x2 = (1-phi)*thetaA + phi*thetaB
                f2 = self.distance_at_angle(points, T, x2)
            return min(f1, f2)
        return self.path_distance(points, T)

    # Function to run $1 algorithm from processed points
    def recognize(self, points):
        # n best list
        n_best = {}
        # if the debug flag is set true, the processed points will be displayed on the canvas
        b = float('inf')
        Td = None
        bestScore = 0
        for template in self.templates:
            T = template.points
            # The float parameters are radian angles 45, -45, 2. These are parameters from the paper
            d = self.distance_at_best_angle(points, T, 0.7853, -0.7853, 0.0349066)
            if d < b:
                b = d
                Td = template
            bestScore = max(bestScore, 1 - b/(0.5 * math.sqrt(self.preprocessor.size**2 + self.preprocessor.size**2)))
            score = 1 - d/(0.5 * math.sqrt(self.preprocessor.size**2 + self.preprocessor.size**2))
            n_best[template.name] = score
        if Td is None:
            return "", 0, {}
        # Sort the n best list from highest to lowest scores
        sorted_n_best = {i:n_best[i] for i in sorted(n_best, key=lambda x:-n_best[x])}
        return Td.targetLabel, bestScore, sorted_n_best, Td