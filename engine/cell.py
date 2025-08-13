import math
import pygame

from engine.button import Button

class Cell():
    def __init__(self, attributes):
        self.attributes = attributes

        circleImg = pygame.image.load("./assets/circle.png").convert_alpha()
        circleImg.set_colorkey((255, 255, 255))
        squareImg = pygame.image.load("./assets/square.png").convert_alpha()
        squareImg.set_colorkey((255, 255, 255))
        triangleImg = pygame.image.load("./assets/triangle.png").convert_alpha()
        triangleImg.set_colorkey((255, 255, 255))

        self.circle = circleImg
        self.square = squareImg
        self.triangle = triangleImg

        self.cellButton = Button("./assets/blank.png")
        self.cellButton.image.set_colorkey((255, 255, 255))

        self.shapes = [self.circle, self.square, self.triangle]

    def __eq__(self, other):
        if (self.attributes == other.attributes):
            return True
        return False

    def getAttributes(self):
        return self.attributes
    
    def thirdCell(self, other):
        values = []

        for i in range(len(self.attributes)):
            sum = self.attributes[i] + other.attributes[i]
            rounded = 3 * math.ceil(sum / 3)

            desired = rounded - sum
            values.append(desired)

        desiredCell = Cell(tuple(values))
        return desiredCell

    def draw(self, display, x, y, colours, backgroundColours):
        colour = colours[list(self.getAttributes())[0]]
        background = backgroundColours[list(self.getAttributes())[1]]
        shape = self.shapes[list(self.getAttributes())[2]]
        
        pygame.draw.rect(display, background, pygame.Rect(x * 100, y * 100, 100, 100))
        self.cellButton.draw(display, x * 100, y * 100, (0, 0))

        pixelArray1 = pygame.PixelArray(self.circle)
        pixelArray1.replace((0, 0, 0), colour)
        del pixelArray1
        pixelArray2 = pygame.PixelArray(self.square)
        pixelArray2.replace((0, 0, 0), colour)
        del pixelArray2
        pixelArray3 = pygame.PixelArray(self.triangle)
        pixelArray3.replace((0, 0, 0), colour)
        del pixelArray3

        display.blit(shape, ((x * 100) + 25, (y * 100) + 25))

    def __str__(self):
        return f"{self.attributes}"