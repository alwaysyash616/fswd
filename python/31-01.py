"""
Assignment: 31
Problem: 01
Topic: dict
Description: Create a dict object where first N natural numbers are keys and their squares are data values.
Date: 07-07-2026
"""

# d1={e:e**2 for e in range(1,int(input("Enter a number: "))+1)}
# print(d1)

d1={}
for e in range(1,int(input("Enter a number: "))+1):
    d1[e]=e**2
print(d1)