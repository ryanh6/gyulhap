from states.state import State
from states.loading import Loading
from engine.timer import Timer

import pygame

class Score(State):
    def __init__(self, game, engine, roundNumber):
        State.__init__(self, game)
        self.roundNumber = roundNumber
        self.engine = engine

    def update(self, controls, position):
        if (controls["clicked"]):
            self.loadScreen = Loading(self.game, self.engine, 1)
            self.exitState()
            self.loadScreen.enterState()

        self.game.resetKeys()

    def draw(self, display, position):
        display.fill((40, 30, 220))