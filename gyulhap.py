import pygame
import sys

class Cell:
    def __init__(self, color, shape, background):
        self.color = color
        self.shape = shape
        self.background = background

    def __str__(self):
        return f"{self.color}::{self.shape}::{self.background}"

def main():
    p1 = Cell("Red", "Square", "Gray")
    print(p1)

    pygame.init()
    screenWidth = 400
    screenHeight = 300

    screen = pygame.display.set_mode((screenWidth, screenHeight))
    pygame.display.set_caption("Gyul Hap")

    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.fill((255, 255, 255))
        pygame.display.flip()
        clock.tick(40)

if __name__=="__main__":
    main()