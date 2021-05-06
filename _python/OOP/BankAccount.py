class Bank_Account:
    def __init__(self, balance, int_rate):
        self.balance = balance
        self.int_rate = 0.01
    def deposit(self, amount):
        self.balance += amount
        return self
    def withdraw(self, amount):
        self.balance-=amount
        return self
    def display_account_info(self):
        print (self.balance)
        return self
    def yield_interest(self):
        if self.balance > 0 :
            self.balance=self.balance+(self.balance*self.int_rate)
        return self
layth=Bank_Account(10000, 0.01)
layth2=Bank_Account(15000, 0.01)

layth.deposit(100).deposit(200).deposit(150).withdraw(300).yield_interest().display_account_info()

layth2.deposit(100).deposit(200).withdraw(100).withdraw(100).withdraw(500).withdraw(300).yield_interest().display_account_info()







#  make 2 deposits and 4 withdrawals, then yield interest and display the account's info all in one line of code