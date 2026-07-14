"""
Assignment: 40
Problem: 04
Topic: Recursion-4
Description: Write a recursive function to print octal of a given decimal number.
Date: 14-07-2026
"""

def octal(n):
    if n:
        octal(n//8)
        print(n%8,end='')

octal(int(input("Enter a number: ")))
print()