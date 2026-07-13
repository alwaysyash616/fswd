"""
Assignment: 39
Problem: 02
Topic: Recursion-3
Description: Write a recursive function to calculate sum of first N odd natural numbers.
Date: 13-07-2026
"""

def sumNOdd(n):
    if n>1:
        return 2*n-1+sumNOdd(n-1)
    return 1

print(sumNOdd(int(input("Enter a number: "))))