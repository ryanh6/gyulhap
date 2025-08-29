from states.state import State

class Gaming(State):
    def __init__(self, game, gameEngine):
        State.__init__(self, game)
        self.engine = gameEngine

    def update(self, display, position):
        self.game.resetKeys()

    def draw(self, display, position):
        display.fill((255, 255, 255))
        self.engine.board.draw(display)