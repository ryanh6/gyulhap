from states.state import State
from engine.button import Button

class Menu(State):
    def __init__(self, game, gameEngine):
        State.__init__(self, game)

        self.gameEngine = gameEngine

        # self.increaseLengthButton = Button()
        # self.decreaseLengthButton = Button()
        # self.increaseWidthButton = Button()
        # self.decreaseWidthButton = Button()
        # self.increaseAttributesButton = Button()
        # self.decreaseAttributesButton = Button()
        # self.exitMenuButton = Button()

    def update(self, controls, position):
        if (controls["escape"] == True):
            self.exitState()

        if (controls["clicked"] == True):
            if (self.exitMenuButton.rect.collidepoint(position)):
                self.exitState()

        self.game.resetKeys()

    def draw(self, display, position):
        display.fill((0, 0, 255))

        self.exitMenuButton.draw(display, position)