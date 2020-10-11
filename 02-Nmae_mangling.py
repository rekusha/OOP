from datetime import datetime
import pytz

WHITE = '\033[00m'
GREEN = '\033[0;'
RED = '\033['


class Account:
    def __init__(self, acc_name, amount):
        self.acc_name = acc_name
        self.__balance = amount
        self.__history = []

    def deposit(self, amount):
        self.__balance += amount
        self.show_balance()
        self.__history.append([amount, self._get_current_time()])
        print(f'you deposit {amount}')
        self.show_balance()

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            print(f'you spend {amount}')
            self.show_balance()
            self.__history.append([-amount, self._get_current_time()])
        else:
            print("not enough money on You'r account")
            self.show_balance()

    def show_balance(self):
        print(f'Balance: {self.__balance}')

    def show_history(self):
        for amount, date in self.__history:
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
a.deposit(100)
a.show_balance()
a.__balance = 10000000
a.show_balance()
print(a.__dict__)
# __balance при компиляции стал _Account__balance а попытка внесенний изменений a.__balance = 10000000 провалилась по
# причине отсутствия a.__balance в словаре экземпляра
# сначало __balance искало в словаре экземпляра, не найдя перешло в родителю, а не найдя и у родителя просто создало в
# словаре экземпляра ключь __balance со значением 10000000
# именно это и называется name mangling
