import random
import math

class Player:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.points = 0

    def __str__(self):
        return f"Player {self.id}: {self.name}"

    def addPoints(self, points):
        self.points += points

class Cell:
    def __init__(self, attributes):
        self.attributes = attributes

    def __eq__(self, other):
        if (self.attributes == other.attributes):
            return True
        return False

    def getAttributes(self):
        return self.attributes
    
    def thirdCell(self, other):
        values = []

        for i in range(len(self.attributes)):
            sum = self.attributes[i] + other.attributes[i]
            rounded = 3 * math.ceil(sum / 3)

            desired = rounded - sum
            values.append(desired)

        desiredCell = Cell(tuple(values))
        return desiredCell

    def __str__(self):
        return f"{self.attributes}"

class Board:
    def __init__(self, length, width, attributeNum):
        self.length = length
        self.width = width
        self.size = length * width
        self.attributeNum = attributeNum
        self.grid = []
        self.solutions = []

        for i in range(self.size):
            self.grid.append(Cell((0,) * attributeNum))

        self.generateBoard()
        self.findSolutions()

    def getCell(self, index):
        return self.grid[index]

    def setCell(self, index, newCell):
        self.grid[index] = newCell

    def generateBoard(self):
        for i in range(self.size):
            newCell = Cell(tuple(random.randint(0, 2) for i in range(self.attributeNum)))
                
            while (newCell in self.grid):
                newCell = Cell(tuple(random.randint(0, 2) for i in range(self.attributeNum)))
                
            self.setCell(i, newCell)

    def findSolutions(self):
        checked = []

        for i in range(self.size):
            firstCell = self.getCell(i)
            for j in range(i + 1, self.size):
                secondCell = self.getCell(j)

                solutionCell = firstCell.thirdCell(secondCell)

                if (solutionCell in checked):
                    firstIndex = self.grid.index(firstCell) + 1
                    secondIndex = self.grid.index(secondCell) + 1
                    thirdIndex = self.grid.index(solutionCell) + 1

                    solutionIndex = tuple(sorted(list(tuple((firstIndex, secondIndex, thirdIndex)))))
                    self.solutions.append(solutionIndex)

            checked.append(firstCell)

        print(self.solutions)

    def verifySolution(self, solutionTuple):
        if (solutionTuple in self.solutions):
            self.solutions.remove(solutionTuple)
            return True
        return False

    def __str__(self):
        boardString = ""

        for i in range(self.length):
            for j in range(self.width):
                boardString += str(self.grid[(i * self.width) + j]) + " "
            boardString += "\n"
        
        return boardString[:-1]

class Game:
    def __init__(self, length, width, attributeNum, rounds):
        self.rounds = rounds
        self.boardLength = length
        self.boardWidth = width
        self.boardAttributeNum = attributeNum
        self.players = [Player(1, "Alice"), Player(2, "Bob")]

    def makeNewBoard(self):
        return Board(self.boardLength, self.boardWidth, self.boardAttributeNum)

    def startGame(self):
        for i in range(self.rounds):
            print("Round " + str(i + 1))
            self.board = self.makeNewBoard()
            print(self.board.verifySolution((1, 2, 3)))
            print(self.board.verifySolution((1, 2, 3)))
            print(self.board)
            print(self.players[0].name)

def main():
    newGame = Game(3, 3, 3, 10)
    # print(newGame.board)
    newGame.startGame()

if __name__=="__main__":
    main()