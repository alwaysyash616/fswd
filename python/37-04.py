"""
Assignment: 37
Problem: 04
Topic: Recursion-1
Description: Write a recursive function to print first N natural numbers in reverse order.
Date: 12-07-2026
"""

def firstNOdd(n):
    print(2*n-1)
    if n>1:
        firstNOdd(n-1)

firstNOdd(int(input("Enter a number: ")))