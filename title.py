from state import State

class Title(State):
    def __init__(self, game):
        State.__init__(self, game)

    def update(self):
        pass

    def draw(self, display):
        display.fill((255, 0, 0))
