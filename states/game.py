from states.state import State
from engine.board import Board

import pygame

class Game(State):
    def __init__(self, game):
        State.__init__(self, game)

        # Add default settings of the game
        self.length = 3
        self.width = 3
        self.attributes = 3

        self.colours = [(255, 0, 0), (0, 0, 255), (255, 255, 0)]
        self.backgroundColours = [(255, 255, 255), (0, 0, 0), (100, 100, 100)]

    def start(self):
        self.board = Board(self.length, self.width, self.attributes, self.colours, self.backgroundColours)
        print(self.board)

    def update(self, controls, position):
        if (controls["escape"] == True):
            self.exitState()

        self.game.resetKeys()
        

    def draw(self, display, position):
        display.fill((255, 255, 255))
        self.board.draw(display)
