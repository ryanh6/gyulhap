class Player:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.points = 0

    def __str__(self):
        return f'Player {self.id}: {self.name}'

def main():
    print("Hello World")

if __name__=="__main__":
    main()