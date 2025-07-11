class Account:
    def __init__(self,name):
        self._balance=0
    def set_balance(self,amount):
        self._balance=amount
    def get_balance(self,amount):
        return self._balance
    def _calculate_loanlimit(self):
        return limit
