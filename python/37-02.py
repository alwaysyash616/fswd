"""
Assignment: 37
Problem: 02
Topic: Recursion-1
Description: Write a recursive function to print first N natural numbers in reverse order
Date: 12-07-2026
"""

def firstN(n):
    print(n)
    if n>1:
        firstN(n-1)

firstN(int(input("Enter a number: ")))