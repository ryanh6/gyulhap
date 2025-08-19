from states.state import State
from states.round import Round
from engine.board import Board
from engine.player import Player
from engine.timer import Timer

from states.rules import Rules

import pygame

class Game(State):
    def __init__(self, game):
        State.__init__(self, game)

        # Add default settings of the game
        self.length = 3
        self.width = 3
        self.attributes = 3
        self.rounds = 10
        self.silentMax = 3


        self.playerCount = 0
        self.silentCount = 0
        self.roundIndex = 0
        self.active = False
        self.playerAction = False

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

    def generateRound(self, roundNumber):
        roundScreen = Round(self.game, roundNumber)
        roundScreen.enterState()

        self.board = Board(self.length, self.width, self.attributes, self.colours, self.backgroundColours)
        
        self.active = True
        self.playerCount = -1
        self.silentCount = 0
        print(self.board)
        # print(str(self.playerList[self.playerCount].getName()) + "'s Turn")

    def update(self, controls, position):
        self.timer.update()

        if (controls["escape"] == True):
            # Pause Timer
            # Pull up pause screen
            self.exitState()
        if (controls["clicked"] == True):
            # Set player action to true
            # print(self.playerList[self.playerCount].sayHi())
            self.playerAction = True

        if not (self.active):
            self.generateRound(self.roundIndex)
            self.roundIndex += 1
            print("Round " + str(self.roundIndex))
        elif (self.playerAction == True):
            print(self.playerList[self.playerCount].sayHi())
            rules = Rules(self.game)
            rules.enterState()
            self.playerAction = False
        elif not (self.timer.getActive()):
            self.timer.startTimer(10)
            self.playerCount += 1

            if (self.playerCount == len(self.playerList)):
                self.playerCount = 0
                self.silentCount += 1
            if (self.silentCount == self.silentMax):
                self.active = False
                self.timer.endTimer()
                return
            
            print(str(self.silentCount) + ": " + str(self.playerList[self.playerCount].getName()) + "'s Turn")

        if (self.roundIndex > self.rounds):
            self.exitState()
            return

        self.game.resetKeys()

    def draw(self, display, position):
        display.fill((255, 255, 255))

        if (self.active):
            self.board.draw(display)

        if (self.timer.duration != 0):
            wideness = self.timer.calculatePercentage()
            currentSize = display.get_width()
            pygame.draw.rect(display, (170, 30, 40), pygame.Rect(0, display.get_height() - 10, currentSize * wideness, 10))
