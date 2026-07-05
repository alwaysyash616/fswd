"""
Assignment: 29
Problem: 05
Topic: tuple
Description: Write a Python script to find the sum of all odd numbers stored in a tuple.
Date: 04-07-2026
"""

t1=tuple([int(e) for e in input("Enter numbers separated by comma: ").split(',')])
sum=0
for x in t1:
    if x%2:
        sum+=x
print(sum)