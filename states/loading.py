from states.state import State

class Loading(State):
    def __init__(self, game, engine, roundNumber):
        State.__init__(self, game)
        self.roundNumber = roundNumber
        self.engine = engine

    def update(self, controls, position):
        self.game.resetKeys()

    def draw(self, display, position):
        display.fill((220, 30, 40))

        # loadingBarWidth = self.timer.calculatePercentage() * display.get_width()
        # pygame.draw.rect(display, (170, 30, 40), pygame.Rect(0, display.get_height() - 10, loadingBarWidth, 10))


