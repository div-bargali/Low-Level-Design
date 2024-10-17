from abc import ABC, abstractmethod
from Helper.constants import *

class Order(ABC):
    def __init__(self, id, stock, user, quantity, price, order_type):
        self._id = id
        self._stock = stock
        self._user = user
        self._quantity = quantity
        self._price = price
        self._order_type = order_type
        self._status = OrderStatus.OPEN

    @abstractmethod
    def place_order(self):
        pass