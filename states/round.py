from states.state import State

class Round(State):
    def __init__(self, game):
        State.__init__(self, game)

    def update(self, controls, position):
        if (controls["escape"] == True):
            self.exitState()

        self.game.resetKeys()

    def draw(self, display, position):
        display.fill((255, 0, 0))
