from states.state import State
from engine.board import Board
from engine.player import Player
# from engine.timer import Timer

import pygame

class Gaming(State):
    def __init__(self, game, gameEngine):
        State.__init__(self, game)
        # self.timer = Timer()
        self.engine = gameEngine
        # self.timer.startTimer(10)

        self.engine.makeBoard()

    def update(self, display, position):
        # self.timer.update()

        # if not (self.timer.active):
        #     # self.scoreScreen = Score(self.game, self.engine, 1)
        #     self.exitState()
        #     # self.scoreScreen.enterState()

        self.game.resetKeys()

    def draw(self, display, position):
        display.fill((255, 255, 255))
        self.engine.board.draw(display)

        # loadingBarWidth = self.timer.calculatePercentage() * display.get_width()
        # pygame.draw.rect(display, (170, 30, 40), pygame.Rect(0, display.get_height() - 10, loadingBarWidth, 10))