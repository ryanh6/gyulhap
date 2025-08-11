from states.state import State

class Menu(State):
    def __init__(self, game):
        State.__init__(self, game)

    def update(self):
        pass

    def draw(self, display):
        display.fill((0, 0, 255))
