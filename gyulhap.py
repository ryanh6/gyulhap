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

    def getAttributes(self):
        return self.attributes

    def thirdCell(self, other):
        properties = []

        for i in range(len(self.attributes)):
            sum = self.attributes[i] + other.attributes[i]
            rounded = 3 * math.ceil(sum / 3)

            desired = rounded - sum
            properties.append(desired)

        desiredProperties = tuple(properties)
        
        print(desiredProperties)
        return desiredProperties

    def __str__(self):
        return f"{self.attributes}"

class Board:
    def __init__(self, length, width, attributeNum):
        self.length = length
        self.width = width
        self.attributeNum = attributeNum
        self.grid = []
        self.cellSet = []
        
        for i in range(length):
            row = []
            for j in range(width):
                row.append(Cell((0,) * attributeNum))
            
            self.grid.append(row)

        self.generateBoard()
        # self.findSolutions()

    def getCell(self, x, y):
        return self.grid[x][y]

    def setCell(self, x, y, attributes):
        self.grid[x][y] = Cell(attributes)

    def generateBoard(self):
        for i in range(self.length):
            for j in range(self.width):
                newTuple = tuple(random.randint(0, 2) for i in range(self.attributeNum))
                
                while (newTuple in self.cellSet):
                    newTuple = tuple(random.randint(0, 2) for i in range(self.attributeNum))
                
                self.setCell(i, j, newTuple)
                self.cellSet.append(newTuple)

        print(self.cellSet)


    def __str__(self):
        boardString = ""
        for i in range(self.length):
            for j in range(self.width):
                boardString += str(self.grid[i][j]) + " "
            boardString += "\n"
        
        return boardString[:-1]

class Game:
    def __init__(self, length, width, attributeNum):
        # DO SOME SORT OF LENGTH / WIDTH CHECK
        # LENGTH / WIDTH SHOULDNT EXCEED NUMBER OF PROPERTIES IN A SENSE (?)
        self.board = Board(length, width, attributeNum)
        self.players = [Player(1, "Alice"), Player(2, "Bob")]

def main():
    newGame = Game(3, 3, 3)
    print(newGame.board)
    cell1 = newGame.board.getCell(0, 0)
    cell2 = newGame.board.getCell(1, 1)
    print(cell1)
    print(cell2)

    print(newGame.board.cellSet.index(cell1.getAttributes()))
    print(newGame.board.cellSet.index(cell2.getAttributes()))

    cell1.thirdCell(cell2)

if __name__=="__main__":
    main()