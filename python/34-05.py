"""
Assignment: 34
Problem: 05
Topic: Functions-3
Description: Write a Python function to print all factors of a given number (TSRN)
Date: 04-07-2026
"""

def printAllFactors(n):
    for e in range(1,n+1):
        if not n%e:
            print(e,end=' ')
    print()

printAllFactors(int(input("Enter a number: ")))