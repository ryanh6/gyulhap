from player import Player
from board import Board

class Game:
    def __init__(self, rounds):
        self.rounds = rounds
    
    def makeNewBoard(self, length, width, attributes):
        return Board(length, width, attributes)

    def startGame(self):
        for i in range(self.rounds):
            print("Round " + str(i + 1))
            self.board = self.makeNewBoard(3, 3, 3)
            # print(self.board.verifySolution((1, 2, 3)))
            # print(self.board.verifySolution((1, 2, 3)))
            print(self.board)
            # print(self.players[0].name)

def main():
    newGame = Game(10)
    newGame.startGame()

    # pygame.init()

    # screen = pygame.display.set_mode((400, 300))
    # pygame.display.set_caption("Gyul Hap")

    # running = True
    # while running:
    #     pygame.time.delay(100)

    #     for event in pygame.event.get():
    #         if (event.type == pygame.QUIT):
    #             running = False

    # pygame.quit()

if __name__=="__main__":
    main()


# NEED:
#   Board.draw()
#   Cell.draw() ???? (OVerload? different shapes and colours whatnot)

# Following: https://www.youtube.com/watch?v=b_DkQrJxpck