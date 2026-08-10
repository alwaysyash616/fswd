"""
Assignment: 49
Problem: 05
Topic: Iterators and Generators
Description: Use iter and next method to check if all the elements of a list are even numbers using while loop which should work equivalent to for loop
Date: 10-08-2026
"""

l1=[22,44,8,6,4,2,10,11,24]
isEven=True
it=iter(l1)
try:
    while True:
        if next(it)&1:
            isEven=False
            break
except StopIteration:
    pass
if isEven:
    print("Yes, all are even")
else:
    print("Odd number found")