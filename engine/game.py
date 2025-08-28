from engine.player import Player
from engine.board import Board

class Game():
    def __init__(self):
        self.length = 3
        self.width = 3
        self.size = self.length * self.width
        self.attributes = 3
        self.rounds = 10
        self.turnTimer = 10
        self.answerTimer = 5
        self.gyulTimer = 5
        self.silentRounds = 3
        self.board = None
        
        self.playerList = [Player(1, "Alice"), Player(2, "Bob")]
        self.colours = [(255, 0, 0), (0, 0, 255), (255, 255, 0)]
        self.backgroundColours = [(255, 255, 255), (0, 0, 0), (100, 100, 100)]

    def makeBoard(self):
        self.board = Board(self.length, self.width, self.attributes, self.colours, self.backgroundColours)
    
    def getBoard(self):
        return self.board