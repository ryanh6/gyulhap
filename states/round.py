from states.state import State

import pygame

class Round(State):
    def __init__(self, game, number):
        State.__init__(self, game)
        self.number = number
        self.startTime = pygame.time.get_ticks()

    def update(self, controls, position):
        currentTime = pygame.time.get_ticks()

        if (currentTime - self.startTime >= 3000):
            self.exitState()

        self.game.resetKeys()

    def draw(self, display, position):
        display.fill((255, 0, 0))

        currentTime = pygame.time.get_ticks()
        print(currentTime)
        wideness = (currentTime - self.startTime) / 3000
        currentSize = display.get_width()
        pygame.draw.rect(display, (205, 0, 0), pygame.Rect(0, display.get_height() - 10, currentSize * wideness, 10))


