class User:
    def __init__(self,name):
        self.balance = 0
        self.name=name
    def make_deposite(self,amount):
        self.balance+=amount
        return self
    def make_withdrawal(self,amount):
        self.balance-=amount
        return self
huthifa=User("huthifa")
huthifa.make_deposite(1000).make_deposite(1000).make_deposite(1000).make_withdrawal(100)
print(f"His name is {huthifa.name} and he has {huthifa.balance} $$ in his bank")
layth=User("layth")
layth.make_deposite(1000).make_deposite(1000).make_withdrawal(100)
print(f"His name is {layth.name} and he has {layth.balance} $ in his bank")
lana=User("lana")
lana.make_deposite(1000).make_withdrawal(100).make_withdrawal(100).make_withdrawal(100)
print(f"Her name is {lana.name} and she has {lana.balance} $ in her bank")


