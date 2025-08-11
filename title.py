from state import State
from game import Game

class Title(State):
    def __init__(self, game):
        State.__init__(self, game)

    def update(self, controls):
        if (controls["escape"] == True):
            self.game.playing = False
            self.game.running = False
        if (controls["enter"] == True):
            gameScreen = Game(self.game)
            gameScreen.enterState()
        self.game.resetKeys()

    def draw(self, display):
        display.fill((255, 0, 0))
