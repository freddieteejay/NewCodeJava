class Account:
    def __init__(self, name: str, balance:int, pin:str):
        self._pin:str = "pin"
        self._balance = balance
        pass

    def check_balance(self, pin: str):
        return self._balance

    def deposit(self, amount:int):
        if amount > 0:
            self._balance += amount
        pass
    def withdraw(self, amount: int, pin: str):
        pin_is_valid_and_balance_is_sufficient: bool = self._pin.__eq__("pin") and amount <= self._balance
        if pin_is_valid_and_balance_is_sufficient:

            self._balance = self._balance - amount
