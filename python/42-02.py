"""
Assignment: 42
Problem: 02
Topic: Variable Length Arguments
Description: Write a function which receives variable length arguments to find greatest element. It returns the greatest element
Date: 20-07-2026
"""

def greatest(*t):
    return max(t)

print(greatest(91,9,60,40,20,9,100,345,23,999))