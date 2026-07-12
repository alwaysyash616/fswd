"""
Assignment: 37
Problem: 01
Topic: Recursion-1
Description: Write a recursive function to print first N natural numbers.
Date: 12-07-2026
"""

def firstN(n):
    if n>1:
        firstN(n-1)
    print(n)

firstN(int(input("Enter a number: ")))