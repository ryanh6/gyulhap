class Player:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.points = 0

    def __str__(self):
        return f'Player {self.id}: {self.name}'

def main():
    p1 = Player(1, "Alice")
    p2 = Player(2, "Bob")

    print(p1)
    print(p2)

if __name__=="__main__":
    main()