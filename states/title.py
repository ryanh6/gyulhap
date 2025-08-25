from states.state import State
from states.game import Game
# from states.menu import Menu
# from states.rules import Rules
from engine.button import Button

class Title(State):
    def __init__(self, game):
        State.__init__(self, game)
        self.gameScreen = Game(self.game)

        # self.playButton = Button()
        # self.rulesButton = Button()
        # self.settingsButton = Button()
        # self.exitButton = Button()

    def update(self, controls, position):
        if (controls["escape"] == True):
            self.game.playing = False
            self.game.running = False

        if (controls["clicked"] == True):
            # if (self.playButton.rect.collidepoint(position)):
                self.gameScreen.enterState()
                # self.gameScreen.play()
            # if (self.rulesButton.rect.collidepoint(position)):
            #     rulesScreen = Rules(self.game)
            #     rulesScreen.enterState()
            # if (self.settingsButton.rect.collidepoint(position)):
            #     menuScreen = Menu(self.game, self.gameScreen)
            #     menuScreen.enterState()
            # if (self.exitButton.rect.collidepoint(position)):
            #     self.game.playing = False
            #     self.game.running = False

        self.game.resetKeys()

    def draw(self, display, position):
        display.fill((0, 255, 255))

        # self.playButton.draw(display, position)
        # self.rulesButton.draw(display, position)
        # self.settingsButton.draw(display, position)
        # self.exitButton.draw(display, position)
        
