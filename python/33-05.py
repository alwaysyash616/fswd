"""
Assignment: 33
Problem: 05
Topic: Functions-2
Description: Write a python function to calculate factorial of a number (TSRS)
Date: 04-07-2026
"""

def factorial(n):
    i,f=1,1
    while i<=n:
        f*=i
        i+=1
    return f

print(factorial(int(input("Enter a number: "))))