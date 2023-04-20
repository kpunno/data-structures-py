# up and down counter
class UpCounter:
    counter = 0
    stepSize = 1

    def __init__(self, stepSize):
        self.stepSize = stepSize

    def count(self):
        return self.counter

    def update(self):
        self.counter += self.stepSize

class DownCounter(UpCounter):
    def update(self):
        self.counter -= self.stepSize


