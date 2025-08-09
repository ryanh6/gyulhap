from state import State
from board import Board

import pygame

class Game(State):
    def __init__(self, game):
        State.__init__(self, game)
        self.colours = [(255, 0, 0), (0, 0, 255), (255, 255, 0)]
        self.backgroundColours = [(255, 255, 255), (0, 0, 0), (100, 100, 100)]

        self.start()

    def makeNewBoard(self, length, width, attributes, colours, backgroundColours):
        return Board(length, width, attributes, colours, backgroundColours)

    def start(self):
        self.board = self.makeNewBoard(3, 3, 3, self.colours, self.backgroundColours)
        print(self.board)

    def update(self):
        pass

    def draw(self, display):
        display.fill((255, 255, 255))
        self.board.draw(display)
