"""
Assignment: 38
Problem: 05
Topic: Recursion-2
Description: Write a recursive function to print reverse of a given number.
Date: 12-07-2026
"""

def reverseDigits(n):
    if n:
        print(n%10,end='')
        reverseDigits(n//10)

reverseDigits(int(input("Enter a number: ")))
print()