from gesture import Gesture
class OfflineGesture(Gesture):
    def __init__(self, points, targetLabel, name, subject, speed, preprocessor=None, canvasManager=None, debug=False):
        super().__init__(preprocessor, points=points, name=name, canvasManager=canvasManager, debug=debug, targetLabel=targetLabel)
        self.subject = subject
        self.speed = speed