class Wallet:
  def __init__(self, balance):
    self.__balance = balance #Private Attribute

  def deposit(self, amount):
    if amount > 0:
      self.__balance += amount #Add to balance safely

  def withdraw(self, amount):
    if 0 < amount <= self.__balance:
      self.__balance -= amount #Remove from balance safely

  def get_balance(self):
    return self.__balance #To get current balance

acct_1 = Wallet(100)
acct_1.deposit(50)
print(acct_1.get_balance())

acct_2 = Wallet(450)
acct_2.withdraw(28)
print(acct_2.get_balance())

acct_2.deposit(150)
print(acct_2.get_balance())
