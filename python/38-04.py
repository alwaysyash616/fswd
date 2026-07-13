"""
Assignment: 38
Problem: 04
Topic: Recursion-2
Description: Write a recursive function to print cubes of first N natural numbers.
Date: 12-07-2026
"""

def firstNCubes(n):
    if n>1:
        firstNCubes(n-1)
    print(n**3)

firstNCubes(int(input("Enter a number: ")))