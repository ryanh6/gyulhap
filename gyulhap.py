class Player:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.points = 0

    def addPoints(self, points):
        self.points += points

    def __str__(self):
        return f"Player {self.id}: {self.name}"

class Cell:
    def __init__(self, colour, shape, background):
        self.colour = colour
        self.shape = shape
        self.background = background

    def __str__(self):
        return f"{self.colour}, {self.shape}, {self.background}"

class Board:
    def __init__(self, size):
        self.size = size
        self.grid = []
        
        for i in range(size):
            row = []
            for j in range(size):
                row.append(Cell(None, None, None))
            
            self.grid.append(row)

    def getCell(self, x, y):
        return self.grid[x][y]

    def setCell(self, x, y, colour, shape, background):
        self.grid[x][y] = Cell(colour, shape, background)

    def __str__(self):
        for i in range(self.size):
            for j in range(self.size):
                print(self.grid[i][j])

class Game:
    def __init__(self, size):
        self.board = Board(size)
        self.players = [Player(1, "Alice"), Player(2, "Bob")]

def main():
    p1 = Player(1, "Alice")
    p2 = Player(2, "Bob")

    print(p1)
    print(p2)

if __name__=="__main__":
    main()