"""
Assignment: 47
Problem: 03
Topic: Polymorphism
Description: Define a class Result to hold result data for a test (attempt, right and wrong). Overload + operator to combine the result of two tests.
Date: 26-07-2026
"""

class Result:
    def __init__(self,attempt,right,wrong):
        self.attempt=attempt
        self.right=right
        self.wrong=wrong
    def showResult(self):
        print(self.attempt,self.right,self.wrong)
    def __add__(self,other):
        return Result(self.attempt+other.attempt,self.right+other.right,self.wrong+other.wrong)

r1=Result(8,5,3)
r2=Result(10,8,2)
r3=r1+r2
r3.showResult()

# This below was a suggestion (to modify) in my solution, but it was also mentioned that this is (type checking) is advanced. But I think it's not that advanced.
# def __add__(self, other):
#     if not isinstance(other, Result):
#         return NotImplemented
#     return Result(
#         self.attempt + other.attempt,
#         self.right + other.right,
#         self.wrong + other.wrong
#     )
# r1 + 10
