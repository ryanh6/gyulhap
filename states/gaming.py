from states.state import State
from states.loading import Loading
from engine.board import Board
from engine.player import Player
from engine.timer import Timer

import pygame

class Gaming(State):
    def __init__(self, game):
        State.__init__(self, game)
        self.timer = Timer()
        # self.board = Board()
        self.timer.startTimer(10)

    def update(self, display, position):
        self.timer.update()

        self.game.resetKeys()

    def draw(self, display, position):
        display.fill((255, 255, 255))
        self.board.draw(display)