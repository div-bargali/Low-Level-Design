from account import Account

class User(Account):
    def __init__(self, id, name, email):
        super().__init__(id, name, email)
        self._portfolio = None
        self._balance = 0.0
    
    def get_portfolio(self):
        return self._portfolio

    def get_balance(self):
        return self._balance

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
        else:
            raise Exception("Invalid Deposit!")

    def withdraw(self, amount):
        if self._balance < amount:
            raise Exception("Invalid withdraw!")
        else:
            self._balance -= amount