"""
Assignment: 34
Problem: 01
Topic: Functions-3
Description: Write a Python function to print first N odd natural numbers. (TSRN)
Date: 04-07-2026
"""

def printFirstNOddNumbers(n):
    for e in range(1,n+1):
        print(2*e-1,end=' ')
    print()

printFirstNOddNumbers(int(input("Enter a number: ")))