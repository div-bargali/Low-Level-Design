from enum import Enum

class OrderStatus(Enum):
    OPEN = 1 
    CLOSED = 2
    FAILED = 3

class OrderType(Enum):
    BUY = 1
    SELL = 2