import pygame

from cell import Cell


class Creature:

    cells:list[Cell] = []

    def __init__(self, model):
        pass

    def read_model():
        try:
            model_file = open("models/model1.txt", "r")
        except IOError:
            print("File not found or path is incorrect")
    

    def tick(self):
        pass

    def draw(self, surface: pygame.Surface):
        for cell in self.cells:
            cell.draw(surface)

