from state import State

class Game(State):
    def __init__(self, game):
        State.__init__(self, game)

    def update(self):
        pass

    def draw(self, display):
        display.fill((0, 255, 0))
