"""
Assignment: 28
Problem: 01
Topic: list and str mixed
Description: Write a Python script to remove all non int values from a list
Date: 04-07-2026
"""

l1=[3,20,4,8,3.4,5+6j,True,[23,322,],(23,22,1,2,)]
print([e for e in l1 if type(e) is int])