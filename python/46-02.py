"""
Assignment: 46
Problem: 02
Topic: Inheritance
Description: Define a class Account with instance object variables accountNo, balance and static variable rate_of_interest. Provide needful methods. Define subclass FixedDeposit of Account class with instance object variable time. Provide setter and getter. Also define a method to calculate simple interest.
Date: 25-07-2026
"""

class Account:
    rate_of_interest=3.5
    def __init__(self,accountNo,balance):
        self.accountNo=accountNo
        self.accountBalance=balance
    def setBalance(self,balance):
        self.accountBalance=balance
    def getBalance(self):
        return self.accountBalance
    def setAccountNo(self,accountNo):
        self.accountNo=accountNo
    def getAccountNo(self):
        return self.accountNo
    def showAccount(self):
        print("Account No:",self.accountNo)
        print("Balance:",self.accountBalance)

class FixedDeposit(Account):
    def __init__(self,accountNo,amount,time):
        super().__init__(accountNo,amount)
        self.time=time
    def setTime(self,time):
        self.time=time
    def getTime(self):
        return self.time
    def calculate_si(self):
        return (self.accountBalance*Account.rate_of_interest*self.time)/100

f1=FixedDeposit(1001,1000,5)
print(f1.calculate_si())