"""
Assignment: 37
Problem: 03
Topic: Recursion-1
Description: Write a recursive function to print first N odd natural numbers
Date: 12-07-2026
"""

def firstNOdd(n):
    if n>1:
        firstNOdd(n-1)
    print(2*n-1)

firstNOdd(int(input("Enter a number: ")))