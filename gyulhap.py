import time
import pygame

class GyulHap:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Gyul Hap")
        self.screen = pygame.display.set_mode((400, 300))
        self.running = True
        self.playing = True
        self.stateStack = []

    def gameLoop(self):
        while (self.playing == True):
            self.getEvents()
            self.update()
            self.render()

    def getEvents(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
                self.running = False

    def update(self):
        pass

    def render(self):
        pass

if __name__=="__main__":
    gyulHapGame = GyulHap()
    
    while (gyulHapGame.running == True):
        gyulHapGame.gameLoop()