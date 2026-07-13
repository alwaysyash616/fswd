"""
Assignment: 39
Problem: 03
Topic: Recursion-3
Description: Write a recursive function to calculate sum of first N even natural numbers.
Date: 13-07-2026
"""

def sumNEven(n):
    if n>1:
        return 2*n+sumNEven(n-1)
    return 2

print(sumNEven(int(input("Enter a number: "))))