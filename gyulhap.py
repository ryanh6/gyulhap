import random

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

    def __str__(self):
        return f"{self.attributes}"

class Board:
    def __init__(self, length, width, attributeNum):
        self.length = length
        self.width = width
        self.attributeNum = attributeNum
        self.grid = []
        
        for i in range(length):
            row = []
            for j in range(width):
                row.append(Cell((0,) * attributeNum))
            
            self.grid.append(row)

        self.generateBoard()

    def getCell(self, x, y):
        return self.grid[x][y]

    def setCell(self, x, y, attributes):
        self.grid[x][y] = Cell(attributes)

    def generateBoard(self):
        cellSet = set()

        for i in range(self.length):
            for j in range(self.width):
                newTuple = tuple(random.randint(0, 2) for _ in range(self.attributeNum))
                
                while (newTuple in cellSet):
                    newTuple = tuple(random.randint(0, 2) for _ in range(self.attributeNum))
                
                self.setCell(i, j, newTuple)
                cellSet.add(newTuple)

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

if __name__=="__main__":
    main()