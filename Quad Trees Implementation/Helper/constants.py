from enum import Enum

class QuadTreeNodeType(Enum):  
    DIVIDED = 0
    EMPTY_LEAF = 1
    FULL_LEAF = 2

class QuadType(Enum):
    NORTH_WEST = 0
    NORTH_EAST = 1
    SOUTH_WEST = 2
    SOUTH_EAST = 3

NO_OF_CABS = 2