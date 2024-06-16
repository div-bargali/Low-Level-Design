import math
from Location import Location

class Cab(Location):
    def __init__(self, x, y):
        super().__init__(x, y)

    def __repr__(self):
        return f"({self.x}, {self.y})"