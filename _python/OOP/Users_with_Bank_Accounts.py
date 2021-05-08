class User:
    def __init__(self,name):
        self.balance = 0
        self.name=name
    def make_deposite(self,amount):
        self.balance+=amount
    def make_withdrawal(self,amount):
        self.balance-=amount
    def display_user_balance(self):
        print(f"User: {self.name}, Balance: {self.balance}")
        return self


class Bank_Account:
    def __init__(self, balance, int_rate, accno):
        self.balance = balance
        self.int_rate = 0.01
        self.accno=accno
    def deposit(self, amount, accno):
        self.balance += amount
        return self
    def withdraw(self, amount, accno):
        self.balance-=amount
        return self
    def display_account_info(self):
        print (self.balance)
        return self
    def yield_interest(self):
        if self.balance > 0 :
            self.balance=self.balance+(self.balance*self.int_rate)
        return self


#  Allow a user to have multiple accounts; update methods so the user has to specify which account they are withdrawing or depositing to