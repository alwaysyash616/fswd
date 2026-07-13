"""
Assignment: 38
Problem: 03
Topic: Recursion-2
Description: Write a recursive function to print squares of first N natural numbers
Date: 12-07-2026
"""

def firstNSquares(n):
    if n>1:
        firstNSquares(n-1)
    print(n**2)

firstNSquares(int(input("Enter a number: ")))