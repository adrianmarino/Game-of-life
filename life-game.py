import numpy as np
import pygame as pg

from board import Board
from color import background_color
from tuples import Size

screen_size = Size(width=1600, height=1600)


def rules(board, cell):
    live_neighbors = board.live_neighbors_of(cell)
    new_cell = next_board[cell.x, cell.y]

    # Life game rules...
    if cell.is_death() and live_neighbors == 3:
        new_cell.give_life()
    if cell.is_alive() and (live_neighbors < 2 or live_neighbors > 3):
        new_cell.kill()


if __name__ == "__main__":
    play = False
    execute = True
    board = Board(rows=40, columns=40, size=screen_size)
    pg.init()
    screen = pg.display.set_mode(screen_size)
    while execute:
        for event in pg.event.get():
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    execute = False
                elif event.key == pg.K_SPACE:
                    play = not play

        if not play:
            mouse_click = pg.mouse.get_pressed()
            if sum(mouse_click) > 0:
                mouse_x, mouse_y = pg.mouse.get_pos()
                cel_x = int(np.floor(mouse_x / board.rows))
                cel_y = int(np.floor(mouse_y / board.columns))

                if mouse_click[2]:
                    board[cel_x, cel_y].kill()
                else:
                    board[cel_x, cel_y].give_life()

        screen.fill(background_color)
        next_board = board.copy()
        for cell in board.cells():
            cell.draw_on(screen)

            if play:
                rules(board, cell)

        pg.display.flip()
        board = next_board
