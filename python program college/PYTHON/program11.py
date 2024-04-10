#a program that models a bank account
#with classes for bank and account the customer can deposit and withdraw money
import random
class customer:
    def __init__(self,name,balance=0):
        self.name=name
        self.balance=balance
        self.account_number=random.randint(1000,9999)
    def deposit(self,amount):
        self.balance+=amount
        print("Amount deposited:",amount)
        print("Current balance:",self.balance)
    def withdraw(self,amount):
        if amount>self.balance:
            print("Insufficient balance")
        else:
            self.balance-=amount
            print("Amount withdrawn:",amount)
            print("Current balance:",self.balance)
    def display(self):
        print("Name:",self.name)
        print("Account number:",self.account_number)
        print("Balance:",self.balance)
        
class bankaccount:
    def __init__(self):
        self.accounts={}
    def add_account(self,customer):
        self.accounts[customer.account_number]=customer
    def display_account(self,account_number):
        self.accounts[account_number].display()
    def deposit(self,account_number,amount):
        self.accounts[account_number].deposit(amount)
    def withdraw(self,account_number,amount):
        self.accounts[account_number].withdraw(amount)
class bank:
    def __init__(self):
        self.bankaccounts=bankaccount()
    def add_customer(self,name,balance=0):
        c=customer(name,balance)
        self.bankaccounts.add_account(c)
        print("Account created successfully")
        print("Account number:",c.account_number)
    def display_account(self,account_number):
        self.bankaccounts.display_account(account_number)
    def deposit(self,account_number,amount):
        self.bankaccounts.deposit(account_number,amount)
    def withdraw(self,account_number,amount):
        self.bankaccounts.withdraw(account_number,amount)
if __name__ == "__main__":
    b=bank()
    while True:
        print("1.Add customer")
        print("2.Display account")
        print("3.Deposit")
        print("4.Withdraw")
        print("5.Exit")
        choice=int(input("Enter your choice:"))
        if choice==1:
            name=input("Enter your name:")
            b.add_customer(name)
        elif choice==2:
            account_number=int(input("Enter the account number:"))
            b.display_account(account_number)
        elif choice==3:
            account_number=int(input("Enter the account number:"))
            amount=int(input("Enter the amount:"))
            b.deposit(account_number,amount)
        elif choice==4:
            account_number=int(input("Enter the account number:"))
            amount=int(input("Enter the amount:"))
            b.withdraw(account_number,amount)
        elif choice==5:
            break
        else:
            print("Invalid choice")
# Output:
# 1.Add customer
