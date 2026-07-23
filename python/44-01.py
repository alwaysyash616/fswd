"""
Assignment: 44
Problem: 01
Topic: Decorator
Description: Write a function to calculate HCF of two numbers. Define a decorator for HCF function to tell whether the two numbers are co-prime or not.
Date: 22-07-2026
"""

def coPrimeCheckerMaker(hcf):
    def isCoPrime(x,y):
        result=hcf(x,y)
        if result==1:
            print("Co-Prime")
        else:
            print("Not Co-Prime")
        return result 
    return isCoPrime

@coPrimeCheckerMaker
def gcd(x,y):
    for e in range(min([x,y]),0,-1):
        if x%e==0 and y%e==0:
            return e

value=gcd(99991,99989)
print(value)