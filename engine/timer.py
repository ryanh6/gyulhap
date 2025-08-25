import time

class Timer():
    def __init__(self):
        self.active = False
        self.startTime = 0
        self.duration = 0

    def getActive(self):
        return self.active

    def startTimer(self, duration):
        self.active = True
        self.startTime = time.time()
        self.duration = duration

    def endTimer(self):
        self.active = False
        self.startTime = 0
        self.duration = 0

    def update(self):
        if (self.active):
            currentTime = time.time()

            if (currentTime - self.startTime >= self.duration):
                self.endTimer()

    def calculatePercentage(self):
        currentTime = time.time()
        return (currentTime - self.startTime) / self.duration
