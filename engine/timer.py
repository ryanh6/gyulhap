import pygame

class Timer():
    def __init__(self):
        self.active = False
        self.startTime = 0
        self.duration = 0

    def getActive(self):
        return self.active

    def startTimer(self, duration):
        self.active = True
        self.startTime = pygame.time.get_ticks()
        self.duration = duration * 1000

    def endTimer(self):
        self.active = False
        self.startTime = 0
        self.duration = 0

    def update(self):
        if (self.active):
            currentTime = pygame.time.get_ticks()

            if (currentTime - self.startTime >= self.duration):
                self.endTimer()

    def calculatePercentage(self):
        currentTime = pygame.time.get_ticks()
        return (currentTime - self.startTime) / self.duration
