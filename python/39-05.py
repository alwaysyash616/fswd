"""
Assignment: 39
Problem: 05
Topic: Recursion-3
Description: Write a recursive function to calculate sum of cubes of first N natural numbers.
Date: 13-07-2026
"""

def sumNCubes(n):
    if n>1:
        return n**3+sumNCubes(n-1)
    return 1

print(sumNCubes(int(input("Enter a number: "))))