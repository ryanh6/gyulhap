from states.state import State
from states.game import Game

class Title(State):
    def __init__(self, game):
        State.__init__(self, game)

        # Title should already have an instance of the game loaded (Like Line 16)
        #   if start game, then just enter game state
        #   if change settings, send that game instance to the menu state

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
