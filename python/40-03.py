"""
Assignment: 40
Problem: 03
Topic: Recursion-4
Description: Write a recursive function to print binary of a given decimal number.
Date: 14-07-2026
"""

def binary(n):
    if n:
        binary(n//2)
        print(n%2,end='')

binary(int(input("Enter a number: ")))
print()