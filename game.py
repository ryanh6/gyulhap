from state import State
from board import Board

import pygame

class Game(State):
    def __init__(self, game):
        State.__init__(self, game)
        self.colours = [(255, 0, 0), (0, 0, 255), (255, 255, 0)]
        self.backgroundColours = [(255, 255, 255), (0, 0, 0), (100, 100, 100)]

        circleImg = pygame.image.load("circle.png").convert_alpha()
        circleImg.set_colorkey((255, 255, 255))
        squareImg = pygame.image.load("square.png").convert_alpha()
        squareImg.set_colorkey((255, 255, 255))
        triangleImg = pygame.image.load("triangle.png").convert_alpha()
        triangleImg.set_colorkey((255, 255, 255))

        self.circle = circleImg
        self.square = squareImg
        self.triangle = triangleImg

        self.shapes = [self.circle, self.square, self.triangle]

        self.start()

    def makeNewBoard(self, length, width, attributes, colours, backgroundColours, shapes):
        return Board(length, width, attributes, colours, backgroundColours, shapes)

    def start(self):
        self.board = self.makeNewBoard(3, 3, 3, self.colours, self.backgroundColours, self.shapes)
        print(self.board)

    def update(self):
        pass

    def draw(self, display):
        display.fill((255, 255, 255))
        self.board.draw(display)
