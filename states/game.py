from states.state import State
from states.round import Round
from engine.board import Board

import pygame

class Game(State):
    def __init__(self, game):
        State.__init__(self, game)

        # Add default settings of the game
        self.length = 3
        self.width = 3
        self.attributes = 3
        self.rounds = 10
        self.count = 0
        self.playerCount = 0
        self.startTime = pygame.time.get_ticks()

        self.colours = [(255, 0, 0), (0, 0, 255), (255, 255, 0)]
        self.backgroundColours = [(255, 255, 255), (0, 0, 0), (100, 100, 100)]

    def getLength(self):
        return self.length
    
    def getWidth(self):
        return self.width
    
    def getAttributes(self):
        return self.attributes
    
    def setLength(self, newLength):
        self.length = newLength

    def setWidth(self, newWidth):
        self.width = newWidth

    def setAttributes(self, newAttributes):
        self.attributes = newAttributes

    def play(self):
        roundScreen = Round(self.game, 1)
        roundScreen.enterState()

        self.board = Board(self.length, self.width, self.attributes, self.colours, self.backgroundColours)
        print(self.board)

    def update(self, controls, position):
        currentTime = pygame.time.get_ticks()

        if (currentTime - self.startTime >= 10000):
            print("PLayer " + str(self.playerCount) + "'s Turn")
            self.playerCount += 1
            self.startTime = pygame.time.get_ticks()

        if (controls["escape"] == True):
            self.exitState()
        if (controls["up"] == True):
            print("Player " + str(self.playerCount) + " performed action")
        if (controls["clicked"] == True):
            if (self.count <= 10):
                self.play()
                self.count += 1
            else:
                self.count = 0
                self.exitState()

        self.game.resetKeys()

    def draw(self, display, position):
        display.fill((255, 255, 255))
        self.board.draw(display)
