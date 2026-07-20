"""
Assignment: 42
Problem: 01
Topic: Variable Length Arguments
Description: Write a function which receives variable length arguments to calculate average of integers. It returns the average of numbers.
Date: 20-07-2026
"""

def avg(*t):
    return sum(t)/len(t)

print(avg(4,5,8,9,10,6))