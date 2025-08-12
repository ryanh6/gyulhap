from states.state import State
from engine.button import Button

class Rules(State):
    def __init__(self, game):
        State.__init__(self, game)

        self.exitRulesButton = Button()

    def update(self, controls, position):
        if (controls["escape"] == True):
            self.exitState()

        if (controls["clicked"] == True):
            if (self.exitRulesButton.rect.collidepoint(position)):
                self.exitState()

        self.game.resetKeys()

    def draw(self, display, position):
        display.fill((255, 255, 255))

        self.exitRulesButton.draw(display, position)
