import pygame

class Button():
    def __init__(self, x, y, imageLink):
        self.image = pygame.image.load(imageLink)
        self.width = self.image.get_width()
        self.height = self.image.get_height()

        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

    def draw(self, display, position):
        # if (self.rect.collidepoint(position)):
            # print("HOVER")

        display.blit(self.image, (self.rect.x, self.rect.y))