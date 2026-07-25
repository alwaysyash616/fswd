"""
Assignment: 46
Problem: 04
Topic: Inheritance
Description: Define a class Account with instance object variable balance with initial value as 0. Provide withdraw and deposit methods. Now define a subclass MinimumBalanceAccount of Account with provided minimum balance. Override withdraw method according to minimum balance condition.
Date: 25-07-2026
"""

class Account:
    def __init__(self):
        self.balance=0
    def withdraw(self,amount):
        if amount<=self.balance:
            self.balance-=amount
            print("Please collect your cash.")
        else:
            print("Insufficient Balance.")
    def deposit(self,amount):
        self.balance+=amount
        print("Amount deposited to your account")
        print("Balance:",self.balance)

class MinimumBalanceAccount(Account):
    def __init__(self,minBalance,balance):
        super().__init__()
        self.minBalance=minBalance
        if balance>=minBalance:
            self.balance=balance
        else:
            self.balance=minBalance
    def withdraw(self,amount):
        if amount<=self.balance-self.minBalance:
            self.balance-=amount
            print("Balance:",self.balance)
        else:
            print("You request cannot be processed.")

mb1=MinimumBalanceAccount(500,2000)
mb1.withdraw(1400)
