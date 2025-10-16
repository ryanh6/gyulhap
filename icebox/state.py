class State():
    def __init__(self, game):
        self.game = game
        self.previousState = None

    def update(self):
        pass

    def draw(self):
        pass

    def enterState(self):
        if (len(self.game.stateStack) > 1):
            self.previousState = self.game.stateStack[-1]
        self.game.stateStack.append(self)

    def exitState(self):
        self.game.stateStack.pop()