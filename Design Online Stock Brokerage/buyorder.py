from order import Order
from Helper.constants import OrderType

class BuyOrder(Order):
    def __init__(self, id, stock, user, quantity, price):
        super().__init__(id, stock, user, quantity, price, OrderType.BUY)

    def place_order(self):
        amount = self._quantity * self._price
        self._user.withdraw(amount)
        print(f"Buy order for user {self._user._name} for amount {amount} was successful")
        self._status = OrderStatus.CLOSED