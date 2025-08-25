from states.state import State
from engine.timer import Timer

import pygame

class Score(State):
    def __init__(self, game, roundNumber):
        State.__init__(self, game)
        self.roundNumber = roundNumber
        self.timer = Timer()
        self.timer.startTimer(3)

    def update(self, controls, position):
        self.timer.update()

        if (self.timer.active == False):
            self.exitState()

        self.game.resetKeys()

    def draw(self, display, position):
        display.fill((40, 30, 220))

        wideness = self.timer.calculatePercentage()
        currentSize = display.get_width()
        pygame.draw.rect(display, (40, 30, 170), pygame.Rect(0, display.get_height() - 10, currentSize * wideness, 10))