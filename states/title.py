from states.state import State
from states.game import Game
from engine.button import Button

import pygame

class Title(State):
    def __init__(self, game):
        State.__init__(self, game)

        self.test = Button(300, 300, "./assets/triangle.png")

        self.gameScreen = Game(self.game)

        # Title should already have an instance of the game loaded (Like Line 16)
        #   if start game, then just enter game state
        #   if change settings, send that game instance to the menu state

    def update(self, controls, position):
        if (controls["escape"] == True):
            self.game.playing = False
            self.game.running = False
        if (controls["enter"] == True):
            self.gameScreen.start()
            self.gameScreen.enterState()
        if (controls["clicked"] == True):
            if (self.test.rect.collidepoint(position)):
                print("SIDUBF")

        self.game.resetKeys()

    def draw(self, display, position):
        display.fill((255, 0, 0))
        self.test.draw(display, position)
        
