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
                    firstIndex = self.grid.index(firstCell)
                    secondIndex = self.grid.index(secondCell)
                    thirdIndex = self.grid.index(solutionCell)

                    solutionIndex = tuple(sorted(list(tuple((firstIndex, secondIndex, thirdIndex)))))
                    self.solutions.append(solutionIndex)

            checked.append(firstCell)

    def __str__(self):
        boardString = ""

        for i in range(self.length):
            for j in range(self.width):
                boardString += str(self.grid[(i * self.width) + j]) + " "
            boardString += "\n"
        
        return boardString[:-1]

class Game:
    def __init__(self, length, width, attributeNum):
        self.board = Board(length, width, attributeNum)
        self.players = [Player(1, "Alice"), Player(2, "Bob")]

def main():
    newGame = Game(3, 3, 3)
    print(newGame.board)

if __name__=="__main__":
    main()