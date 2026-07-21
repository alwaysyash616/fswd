"""
Assignment: 43
Problem: 05
Topic: map, reduce and filter
Description: Write a python function to calculate HCF (Highest Common Factor) of a list of numbers. Use reduce function.
Date: 21-07-2026
"""

def gcd(x,y):
    for e in range(min([x,y]),0,-1):
        if x%e==0 and y%e==0:
            return e

from functools import reduce
ans=reduce(gcd,[48,72,96,120])
print(ans)