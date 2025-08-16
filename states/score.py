from states.state import State

import pygame

class Round(State):
    def __init__(self, game, roundNumber):
        State.__init__(self, game)
        self.roundNumber = roundNumber
        self.startTime = pygame.time.get_ticks()

    def timer(self, duration):
        if (pygame.time.get_ticks() - self.startTime >= duration):
            return True
        return False

    def update(self, controls, position):
        if (self.timer(3000)):
            self.exitState()

        self.game.resetKeys()

    def draw(self, display, position):
        display.fill((40, 30, 220))

        currentTime = pygame.time.get_ticks()
        print(currentTime)
        wideness = (currentTime - self.startTime) / 3000
        currentSize = display.get_width()
        pygame.draw.rect(display, (40, 30, 170), pygame.Rect(0, display.get_height() - 10, currentSize * wideness, 10))


