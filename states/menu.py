from states.state import State

class Menu(State):
    def __init__(self, game):
        State.__init__(self, game)

    def update(self, controls, position):
        pass

    def draw(self, display, position):
        display.fill((0, 0, 255))
