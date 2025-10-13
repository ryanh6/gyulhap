import random
# from engine.cell import Cell
from cell import Cell

class Board():
    def __init__(self, length, width, attributeNum, colours, backgroundColours):
        self.length = length
        self.width = width
        self.size = length * width
        self.attributeNum = attributeNum
        self.colours = colours
        self.backgroundColours = backgroundColours
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

    def draw(self, display):
        for i in range(self.length):
            for j in range(self.width):
                self.grid[(i * self.width) + j].draw(display, j, i, self.colours, self.backgroundColours)

    def __str__(self):
        boardString = ""

        for i in range(self.length):
            for j in range(self.width):
                boardString += str(self.grid[(i * self.width) + j]) + " "
            boardString += "\n"
        
        return boardString[:-1]