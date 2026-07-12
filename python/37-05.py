"""
Assignment: 37
Problem: 05
Topic: Recursion-1
Description: Write a recursive function to print MySirG N times on the screen.
Date: 12-07-2026
"""

def printMySirG(n):
    print("MySirG")
    if n>1:
        printMySirG(n-1)

printMySirG(int(input("Enter a number: ")))