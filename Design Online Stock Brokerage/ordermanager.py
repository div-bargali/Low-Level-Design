from threading import Lock
from Helper.constants import OrderStatus, OrderType
from buyorder import BuyOrder
from sellorder import SellOrder

# Singleton class
class OrderManager:
    _lock = Lock()
    _instance = None

    @staticmethod
    def get_instance(): # double check locking
        if OrderManager._instance is None:
            with OrderManager._lock:
                if OrderManager._instance is None:
                    OrderManager._instance = OrderManager()
        return OrderManager._instance

    def __init__(self):
        self.__orders = []
        self.__next_order_id = 1
        self.__lock = Lock()
    
    def process_order(self, stock, quantity, user, order_type):
        price = stock.get_price()
        if order_type == OrderType.BUY:
            new_order = BuyOrder(self.__next_order_id, stock, user, quantity, price)
            
            if self.validate_order(quantity, price, user, order_type):
                new_order.place_order()
                new_order._status = OrderStatus.CLOSED
            else:
                new_order._status = OrderStatus.FAILED
            
            self.__orders.append(new_order)
            self.__next_order_id += 1
        

    def validate_order(self, quantity, price, user, order_type):
        return True