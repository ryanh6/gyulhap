from states.state import State
from engine.timer import Timer

import pygame

class Round(State):
    def __init__(self, game, roundNumber):
        State.__init__(self, game)
        self.roundNumber = roundNumber
        self.timer = Timer()
        self.timer.startTimer(3000)
        # self.startTime = pygame.time.get_ticks()


    # def timer(self, duration):
    #     if (pygame.time.get_ticks() - self.startTime >= duration):
    #         return True
    #     return False

    def update(self, controls, position):
        if (self.timer.checkTimer()):
            self.exitState()
        # if (self.timer(3000)):
        #     self.exitState()

        self.game.resetKeys()

    def draw(self, display, position):
        display.fill((220, 30, 40))

        # currentTime = pygame.time.get_ticks()
        # print(currentTime)
        wideness = self.timer.calculatePercentage()
        currentSize = display.get_width()
        pygame.draw.rect(display, (170, 30, 40), pygame.Rect(0, display.get_height() - 10, currentSize * wideness, 10))


