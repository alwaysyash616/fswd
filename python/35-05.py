"""
Assignment: 35
Problem: 05
Topic: Functions-4
Description: Write a Python function to find all the common factors of two given numbers. Return a tuple of such factors (TSRS)
Date: 04-07-2026
"""

def factors(n):
    temp=set()
    for e in range(1,n+1):
        if not n%e:
            temp.add(e)
    return temp

def findCommonFactors(a,b):
    return tuple(factors(a).intersection(factors(b)))

print("Enter two numbers: ")
print(findCommonFactors(int(input()),int(input())))