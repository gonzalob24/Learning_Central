import math


class Account:

    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def deposit(self, money):
        self.balance += money
        return "The balance is {0} after depositing {1}".format(self.balance, money)

    def withdraw(self, money):
        if self.balance >= money:
            self.balance -= money
            return "The balance is {0} after withdrawing {1} ".format(self.balance, money)
        else:
            return "Insufficient funds\nTry another amount"

    def __str__(self):
        return "Owner: {0}\nBalance: {1}".format(self.name, self.balance)


if __name__ == "__main__":
    acc = Account('Gonzalo', 250)
    print(acc)
    print(acc.deposit(100))
    print(acc.withdraw(50))
    print(acc.withdraw(250))
    print(acc)
