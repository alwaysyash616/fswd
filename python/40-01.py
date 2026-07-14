"""
Assignment: 40
Problem: 01
Topic: Recursion-4
Description: Write a recursive function to calculate sum of digits of a given number.
Date: 14-07-2026
"""

def sumOfDigits(n):
    if n:
        return n%10+sumOfDigits(n//10)
    return 0

print(sumOfDigits(int(input("Enter a number: "))))