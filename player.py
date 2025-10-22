class Player():
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.points = 0

    def __str__(self):
        return f"Player {self.id}: {self.name}"

    def getName(self):
        return f"{self.name}"

    def addPoints(self, points):
        self.points += points

    def getPoints(self):
        return self.points

    def setPoints(self, newPoints):
        self.points = newPoints

    def resetPoints(self):
        self.setPoints(0)