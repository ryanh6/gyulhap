from states.state import State

import pygame

class Loading(State):
    def __init__(self, game, engine, roundNumber):
        State.__init__(self, game)
        self.roundNumber = roundNumber
        self.engine = engine

        self.background = pygame.image.load("./assets/background.png").convert_alpha()

    def update(self, controls, position):
        self.game.resetKeys()

    def draw(self, display, position):
        # display.fill((220, 30, 40))

    
        display.blit(self.background, (0, 0))

        transparent_surface = pygame.Surface((1000, 500), pygame.SRCALPHA)
        transparent_surface.fill((225, 0, 0, 200))
        display.blit(transparent_surface, (0, 0))

        # loadingBarWidth = self.timer.calculatePercentage() * display.get_width()
        # pygame.draw.rect(display, (170, 30, 40), pygame.Rect(0, display.get_height() - 10, loadingBarWidth, 10))


