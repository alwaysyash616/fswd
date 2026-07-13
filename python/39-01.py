"""
Assignment: 39
Problem: 01
Topic: Recursion-3
Description: Write a recursive function to calculate sum of first N natural numbers.
Date: 13-07-2026
"""

def sumN(n):
    if n>1:
        return n+sumN(n-1)
    return 1

print(sumN(int(input("Enter a number: "))))