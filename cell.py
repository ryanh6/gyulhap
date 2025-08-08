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

    def draw(self, display, x, y, colours, backgroundColours):
        colour = colours[list(self.getAttributes())[0]]
        background = backgroundColours[list(self.getAttributes())[1]]
        
        pygame.draw.rect(display, background, pygame.Rect(x * 100, y * 100, 100, 100))
        pygame.draw.rect(display, colour, pygame.Rect((x * 100) + 25, (y * 100) + 25, 50, 50))

    def __str__(self):
        return f"{self.attributes}"