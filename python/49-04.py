"""
Assignment: 49
Problem: 04
Topic: Iterators and Generators
Description: Use iter and next method to print values of a given list using while loop which works equivalent to for loop.
Date: 09-08-2026
"""

l1=[22,33,11,44,55,66,77,88,99]
it=iter(l1)
try:
    while True:
        print(next(it))
except StopIteration:
    pass