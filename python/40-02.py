"""
Assignment: 40
Problem: 02
Topic: Recursion-4
Description: Write a recursive function to calculate factorial of a given number.
Date: 14-07-2026
"""

def factorial(n):
    if n>0:
        return n*factorial(n-1)
    return 1

print(factorial(int(input("Enter a number: "))))