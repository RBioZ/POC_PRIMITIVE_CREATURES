import pygame

CELL_SIZE = 5

class Cell:

    x = 50
    y = 50

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def tick(self):
        self.x += 1

    def draw(self, surface: pygame.Surface):
        pygame.draw.rect(surface, (255,255,255) , (self.x, self.y, CELL_SIZE, CELL_SIZE))
        self.tick()
