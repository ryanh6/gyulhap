from states.state import State
from states.gaming import Gaming
# from states.menu import Menu
# from states.rules import Rules
from engine.button import Button
from states.loading import Loading

import pygame

class Title(State):
    def __init__(self, game, gameEngine):
        State.__init__(self, game)
        self.engine = gameEngine

        self.logo = pygame.image.load("./assets/logo.png").convert_alpha()
        self.background = pygame.image.load("./assets/background.png").convert_alpha()

        self.playButton = Button("./assets/blank.png")
        # self.rulesButton = Button()
        # self.settingsButton = Button()
        self.exitButton = Button("./assets/blank.png")

    def update(self, controls, position):
        if (controls["escape"] == True):
            self.game.playing = False
            self.game.running = False

        if (controls["clicked"] == True):
            # if (self.playButton.rect.collidepoint(position)):
                # self.gameScreen = Gaming(self.game, self.engine)
                # self.gameScreen.enterState()
                self.loadScreen = Loading(self.game, self.engine, 1)
                self.loadScreen.enterState()
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
        # overlay_color = (255, 0, 0, 50) # Red with 100 alpha (out of 255)
        # overlay_surface = pygame.Surface(self.background.get_size(), pygame.SRCALPHA)
        # overlay_surface.fill(overlay_color)

        # self.background.blit(overlay_surface, (0, 0))

        display.blit(self.background, (0, 0))

        transparent_surface = pygame.Surface((1000, 500), pygame.SRCALPHA)
        transparent_surface.fill((255, 255, 255, 200))
        display.blit(transparent_surface, (0, 0))

        # pygame.display.flip()

        transparent_color = (255, 255, 255)
        self.logo.set_colorkey(transparent_color)
        display.blit(self.logo, (350, 100))

        # self.playButton.draw(display, 0, 0, position)
        # self.rulesButton.draw(display, position)
        # self.settingsButton.draw(display, position)
        # self.exitButton.draw(display, 100, 100, position)
        
