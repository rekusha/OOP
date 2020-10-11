from datetime import datetime
import pytz

WHITE = '\033[00m'
GREEN = '\033[0;'
RED = '\033['


class Account:
    def __init__(self, acc_name, amount):
        self.acc_name = acc_name
        self.balance = amount
        self.history = []

    def deposit(self, amount):
        self.balance += amount
        self.show_balance()
        self.history.append([amount, self._get_current_time()])
        print(f'you deposit {amount}')
        self.show_balance()

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f'you spend {amount}')
            self.show_balance()
            self.history.append([-amount, self._get_current_time()])
        else:
            print("not enough money on You'r account")
            self.show_balance()

    def show_balance(self):
        print(f'Balance: {self.balance}')

    def show_history(self):
        for amount, date in self.history:
            if amount > 0:
                transaction = 'deposited'
                color = GREEN
            else:
                transaction = 'withdrawn'
                color = RED
            print(f'{color} {amount} {WHITE} {transaction} on {date.astimezone()}')

    @staticmethod
    def _get_current_time():
        return pytz.utc.localize(datetime.utcnow())


a = Account('rekusha', 0)
a.deposit(50)
a.deposit(150)
a.deposit(100)
a.withdraw(50)
a.deposit(50)
a.withdraw(50)

a.show_balance()
a.show_history()
