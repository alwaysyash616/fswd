"""
Assignment: 33
Problem: 01
Topic: Functions-2
Description: Write a python function to check if a number is even. (TSRS)
Date: 04-07-2026
"""

def isEven(n):
    return "Not Even" if n%2 else "Yes, Even"

print(isEven(int(input("Enter a number: "))))