import pygame as pg

from board import Board
from color import background_color
from tuples import Size

screen_size = Size(width=1000, height=1000)


def rules(board, cell):
    live_neighbors = board.live_neighbors_of(cell)
    new_cell = next_board[cell.x, cell.y]

    # Life game rules...
    if cell.is_death() and live_neighbors == 3:
        new_cell.give_life()
    if cell.is_alive() and (live_neighbors < 2 or live_neighbors > 3):
        new_cell.kill()


def init(board):
    board[5, 3].give_life()
    board[5, 4].give_life()
    board[5, 5].give_life()

    board[21, 21].give_life()
    board[22, 22].give_life()
    board[22, 23].give_life()
    board[21, 23].give_life()
    board[20, 23].give_life()

    board[31, 31].give_life()
    board[32, 32].give_life()
    board[32, 33].give_life()
    board[31, 33].give_life()
    board[30, 33].give_life()
    
    board[11, 11].give_life()
    board[12, 12].give_life()
    board[12, 13].give_life()
    board[11, 13].give_life()
    board[10, 13].give_life()


if __name__ == "__main__":
    board = Board(rows=40, columns=40, size=screen_size)
    init(board)

    pg.init()
    screen = pg.display.set_mode(screen_size)
    while True:
        screen.fill(background_color)
        next_board = board.copy()

        for cell in board.cells():
            cell.draw_on(screen)
            rules(board, cell)

        pg.display.flip()
        board = next_board
