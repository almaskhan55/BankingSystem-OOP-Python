class BankAccount:
    def __init__(self ,name ,balance):
        self.name = name 
        self.balance = balance

    def deposit(self ,amount):
        self.balance += amount
        print(f"{self.name} Balance After Deposit : {self.balance}")

    def withdraw(self ,amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"{self.name} Balance After Withdraw : {self.balance}")
        else:
            print("Insufficient Balance")

    def show_balance(self):
        print(f"{self.name} Balance : {self.balance}")

class SavingAccount(BankAccount):
        def add_interest(self, rate):
            self.balance += (self.balance * rate) / 100
            print(f"{self.name} Balance After Interest : {self.balance}")


acc = SavingAccount("Almas", 5000)
acc.show_balance()
acc.deposit(10000)
acc.add_interest(5)
acc.withdraw(2000)