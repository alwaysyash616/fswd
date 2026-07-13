"""
Assignment: 38
Problem: 01
Topic: Recursion-2
Description: Write a recursive function to print first N even natural numbers.
Date: 12-07-2026
"""

def firstNEven(n):
    if n>1:
        firstNEven(n-1)
    print(2*n)

firstNEven(int(input("Enter a number: ")))