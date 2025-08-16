class Player():
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.points = 0

    def __str__(self):
        return f"Player {self.id}: {self.name}"

    def getName(self):
        return f"{self.name}"

    def sayHi(self):
        return f"{self.name} says Hi!"

    def addPoints(self, points):
        self.points += points