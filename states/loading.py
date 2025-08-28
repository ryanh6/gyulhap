from states.state import State
from states.gaming import Gaming
from engine.timer import Timer

import pygame

class Loading(State):
    def __init__(self, game, engine, roundNumber):
        State.__init__(self, game)
        self.roundNumber = roundNumber
        self.engine = engine
        self.timer = Timer()
        self.timer.startTimer(3)

    def update(self, controls, position):
        self.timer.update()

        if not (self.timer.active):
            self.gameScreen = Gaming(self.game, self.engine)
            self.exitState()
            self.gameScreen.enterState()

        self.game.resetKeys()

    def draw(self, display, position):
        display.fill((220, 30, 40))

        loadingBarWidth = self.timer.calculatePercentage() * display.get_width()
        pygame.draw.rect(display, (170, 30, 40), pygame.Rect(0, display.get_height() - 10, loadingBarWidth, 10))


