from states.state import State
from states.loading import Loading
from engine.board import Board
from engine.player import Player
from engine.timer import Timer

import pygame

class Game(State):
    def __init__(self, game):
        State.__init__(self, game)

        # Add default settings of the game
        self.length = 3
        self.width = 3
        self.attributes = 3
        self.rounds = 10
        
        self.playerIndex = 0
        self.phaseIndex = 0
        self.phaseList = ["start", "running", "playeraction", "ending"]
        self.playerList = [Player(1, "Alice"), Player(2, "Bob")]
        self.timer = Timer()

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

    def update(self, display, position):
        self.game.resetKeys()

    def draw(self, display, position):
        display.fill((255, 255, 255))
        self.board.draw(display)