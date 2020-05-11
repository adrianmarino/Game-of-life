import numpy as np

from cell import Cell
from cords import Cords
from tuples import Size, Point


class Board:
    def __init__(self, rows, columns, size, state=None):
        self.size = size
        self.rows = rows
        self.columns = columns
        if state is None:
            self.state = np.zeros((rows, columns))
        else:
            self.state = state
        self.cell_size = Size(
            width=size.width / columns,
            height=size.height / rows
        )

    def copy(self):
        return Board(self.rows, self.columns, self.size, np.copy(self.state))

    def cells(self):
        for y in range(0, self.columns):
            for x in range(0, self.rows):
                yield self[Point(x, y)]

    def __getitem__(self, (x, y)):
        cords = Cords((x, y), self.cell_size)
        return Cell((x, y), cords, self.state)

    def live_neighbors_of(self, cell):
        return sum([n.value() for n in self.neighbors_of(cell)])

    def neighbors_of(self, cell):
        return [
            self[(cell.x - 1) % self.rows, (cell.y - 1) % self.columns],
            self[cell.x % self.rows, (cell.y - 1) % self.columns],
            self[(cell.x + 1) % self.rows, (cell.y - 1) % self.columns],
            self[(cell.x - 1) % self.rows, cell.y % self.columns],
            self[(cell.x + 1) % self.rows, cell.y % self.columns],
            self[(cell.x - 1) % self.rows, (cell.y + 1) % self.columns],
            self[cell.x % self.rows, (cell.y + 1) % self.columns],
            self[(cell.x + 1) % self.rows, (cell.y + 1) % self.columns]
        ]
