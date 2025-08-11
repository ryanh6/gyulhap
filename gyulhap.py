import time
import pygame
from title import Title
from game import Game

class GyulHap:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Gyul Hap")
        self.screen = pygame.display.set_mode((1000, 500))
        self.running = True
        self.playing = True
        self.controls = {"left": False,
                         "right": False,
                         "up": False,
                         "down": False,
                         "clicked": False,
                         "escape": False,
                         "space": False,
                         "enter": False}
        self.stateStack = []

        self.loadStates()

    def gameLoop(self):
        while (self.playing == True):
            self.getEvents()
            self.update()
            self.draw()

    def getEvents(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
                self.running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.controls["clicked"] = True
            if event.type == pygame.MOUSEBUTTONUP:
                self.controls["clicked"] = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.controls["escape"] = True
                if event.key == pygame.K_SPACE:
                    self.controls["space"] = True
                if event.key == pygame.K_RETURN:
                    self.controls["enter"] = True
                if event.key == pygame.K_UP:
                    self.controls["up"] = True
                if event.key == pygame.K_DOWN:
                    self.controls["down"] = True
                if event.key == pygame.K_LEFT:
                    self.controls["left"] = True
                if event.key == pygame.K_RIGHT:
                    self.controls["right"] = True
                if event.key == pygame.K_w:
                    self.controls["up"] = True
                if event.key == pygame.K_s:
                    self.controls["down"] = True
                if event.key == pygame.K_a:
                    self.controls["left"] = True
                if event.key == pygame.K_d:
                    self.controls["right"] = True
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_ESCAPE:
                    self.controls["escape"] = False
                if event.key == pygame.K_SPACE:
                    self.controls["space"] = False
                if event.key == pygame.K_RETURN:
                    self.controls["enter"] = False
                if event.key == pygame.K_UP:
                    self.controls["up"] = False
                if event.key == pygame.K_DOWN:
                    self.controls["down"] = False
                if event.key == pygame.K_LEFT:
                    self.controls["left"] = False
                if event.key == pygame.K_RIGHT:
                    self.controls["right"] = False
                if event.key == pygame.K_w:
                    self.controls["up"] = False
                if event.key == pygame.K_s:
                    self.controls["down"] = False
                if event.key == pygame.K_a:
                    self.controls["left"] = False
                if event.key == pygame.K_d:
                    self.controls["right"] = False

    def update(self):
        self.stateStack[-1].update(self.controls)

    def draw(self):
        self.stateStack[-1].draw(self.screen)
        pygame.display.flip()

    def loadStates(self):
        self.titleScreen = Title(self)
        self.stateStack.append(self.titleScreen)

if __name__=="__main__":
    gyulHapGame = GyulHap()
    
    while (gyulHapGame.running == True):
        gyulHapGame.gameLoop()