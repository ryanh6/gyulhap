# from engine.player import Player
# from engine.board import Board

from player import Player
from board import Board

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

    def startGame(self):
        for player in self.playerList:
            player.resetPoints()

        for i in range(self.rounds):
            print("Round " + str(i + 1))
            self.makeBoard()
            print(self.board)

            for player in self.playerList:
                print("It is now " + player.getName() + " turn to play!")
                print("Select 1 for Hap")
                print("Select 2 for Gyul")
                move = input("Type your option: ")

    def makeBoard(self):
        self.board = Board(self.length, self.width, self.attributes, self.colours, self.backgroundColours)
    
    def getBoard(self):
        return self.board
    
    def getLength(self):
        return self.length
    
    def setLength(self, newlength):
        self.length = newlength
        self.size = self.length * self.width
    
    def getWidth(self):
        return self.width

    def setWidth(self, newWidth):
        self.length = newWidth
        self.size = self.length * self.width

    def getSize(self):
        return self.size

    def getAttributes(self):
        return self.attributes
    
    def setAttributes(self, newAttributes):
        self.attributes = newAttributes

    def getRounds(self):
        return self.rounds
    
    def setRounds(self, newRounds):
        self.rounds = newRounds

    def getTurnTimer(self):
        return self.turnTimer
    
    def setTurnTimer(self, newTurnTimer):
        self.turnTimer = newTurnTimer
    
    def getAnswerTimer(self):
        return self.answerTimer
    
    def setAnswerTimer(self, newAnswerTimer):
        self.answerTimer = newAnswerTimer

    def getGyulTimer(self):
        return self.gyulTimer
    
    def setGyulTimer(self, newGyulTimer):
        self.gyulTimer = newGyulTimer
    
    def getSilentRounds(self):
        return self.silentRounds
    
    def setSilentRounds(self, newSilentRounds):
        self.silentRounds = newSilentRounds

def main():
    newGame = Game()
    newGame.startGame()

if __name__ == "__main__":
    main()