from collections import namedtuple

import numpy as np
import pygame as pg

Point = namedtuple('Point', 'x y')
Size = namedtuple('Size', 'width height')
Division = namedtuple('Division', 'x y')

screen_size = Size(width=1000, height=1000)
background_color = (25, 25, 25)
cell_color = (128, 128, 128)
screen_division = Point(x=25, y=25)

cell_size = Size(
    width=screen_size.width / screen_division.x,
    height=screen_size.height / screen_division.x
)

game_state = np.zeros(screen_division)

pg.init()
screen = pg.display.set_mode(screen_size)
screen.fill(background_color)


def box_cords(point, size):
    return [
        (point.x * size.width, point.y * size.height),
        (point.x * size.width, (point.y + 1) * size.height),
        ((point.x + 1) * size.width, (point.y + 1) * size.height),
        ((point.x + 1) * size.width, point.y * size.height)
    ]


def draw_cell(output, point, size, color=cell_color):
    pg.draw.polygon(output, color, box_cords(point, size), 1)


while True:
    for y in range(0, screen_division.y):
        for x in range(0, screen_division.x):
            draw_cell(screen, Point(x, y), cell_size)

    pg.display.flip()
