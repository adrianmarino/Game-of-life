class Cords:
    def __init__(self, (x, y), size):
        self.top_left = x * size.width, y * size.height
        self.bottom_left = x * size.width, (y + 1) * size.height
        self.bottom_right = (x + 1) * size.width, (y + 1) * size.height
        self.top_right = (x + 1) * size.width, y * size.height

    def as_tuple(self):
        return self.top_left, self.bottom_left, self.bottom_right, self.top_right
