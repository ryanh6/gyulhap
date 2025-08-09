import math
import pygame

class Cell():
    def __init__(self, attributes):
        self.attributes = attributes

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

    def processImage(self, shape, colour):
        pixelArray = pygame.PixelArray(shape)
        pixelArray.replace((0, 0, 0), colour)
        del pixelArray
        return shape

    def draw(self, display, x, y, colours, backgroundColours, shapes):
        colour = colours[list(self.getAttributes())[0]]
        background = backgroundColours[list(self.getAttributes())[1]]
        shape = shapes[list(self.getAttributes())[2]]
        
        pygame.draw.rect(display, background, pygame.Rect(x * 100, y * 100, 100, 100))
        newShape = self.processImage(shape, colour)

        display.blit(newShape, ((x * 100) + 25, (y * 100) + 25))

    def __str__(self):
        return f"{self.attributes}"