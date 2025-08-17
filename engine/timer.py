import pygame

class Timer():
    def __init__(self):
        self.startTime = 0
        self.currentTime = 0
        self.duration = 0

    def startTimer(self, milliseconds):
        self.startTime = pygame.time.get_ticks()
        self.currentTime = self.startTime
        self.duration = milliseconds

    def checkTimer(self):
        self.currentTime = pygame.time.get_ticks()

        if (self.currentTime - self.startTime >= self.duration):
            return True
        return False

    # def endTimer(self):


    # def pauseTimer(self):


    def calculatePercentage(self):
        return (self.currentTime - self.startTime) / self.duration
