"""
Assignment: 39
Problem: 04
Topic: Recursion-3
Description: Write a recursive function to calculate sum of squares of first N natural numbers.
Date: 13-07-2026
"""

def sumNSquares(n):
    if n>1:
        return n**2+sumNSquares(n-1)
    return 1

print(sumNSquares(int(input("Enter a number: "))))