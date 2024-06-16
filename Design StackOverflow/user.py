from account import Account
from Helper.constants import AccountType

class User(Account):
    def __init__(self, id, name, email, password):
        super().__init__(id, name, email, password)
        self.__account_type = AccountType.NORMAL
        self.__reputation = 0
        self.__questions = []
        self.__answers = []
        self.__comments = []

    def get_reputation(self):
        return self.__reputation

    def incr_reputation(self):
        self.__reputation += 1

    def add_question(self, question):
        self.__questions.append(question)
        print(f"Question added successfully to {self._name}")