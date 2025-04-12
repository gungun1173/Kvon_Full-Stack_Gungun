#  Create a Bank Account Class:
# Attributes: Name, Balance, Account Number
# Methods:
# deposit(amount) → Add money to balance
# withdraw(amount) → Deduct money if balance > amount
# show_balance() → Show current balance"


class Bank:
    def __init__(self, name, balance, acc_number):
        self.name = name
        self.balance = balance
        self.acc_number = acc_number

    def deposit(self, amount):
        self.balance += amount   
        print("Amount Deposited")

    def withdraw(self, amount):
        if self.balance <= amount:
            print("Insufficient Balance...")
        else :
            self.balance -= amount
            print("Amount Withdrawn")

    def show_balance(self):
        print("Balance:",self.balance)    



name = input("Enter the name of the Account Holder:")
balance = int(input("Enter the Balance of your Account:")) 
acc_number = int(input("Enter the account number:")) 
p1 = Bank(name, balance, acc_number)
task = input("Enter the Task(deposit, withdraw, show balance):")
while task != "Exit" :
    if task == "deposit":
        amount = int(input("Enter the amount to be deposited:"))
        p1.deposit(amount)

    elif task == "withdraw":
        amount = int(input("Enter the amount to be withdrawn:"))
        p1.withdraw(amount)

    else :
        p1.show_balance()

    task = input("Enter the Task(deposit, withdraw, show balance):")    




