import pygame as pg

from color import death_cell_color, living_cell_color


class Cell:
    def __init__(self, (x, y), cords, state):
        self.x = x
        self.y = y
        self.cords = cords
        self.state = state

    def draw_on(self, output):
        if self.is_death():
            pg.draw.polygon(output, death_cell_color, self.cords.as_tuple(), 1)
        else:
            pg.draw.polygon(output, living_cell_color, self.cords.as_tuple(), 0)

    def is_alive(self):
        return self.value() == 1

    def is_death(self):
        return not self.is_alive()

    def give_life(self):
        self.__value(1)

    def kill(self):
        self.__value(0)

    def value(self):
        return self.state[self.x, self.y]

    def __value(self, v):
        self.state[self.x, self.y] = v
