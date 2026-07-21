"""
Assignment: 43
Problem: 03
Topic: map, reduce and filter
Description: Write a python script to create a list of numbers greater than a given number N (taken from user) for each element in a given set of numbers. Use filter function.
Date: 21-07-2026
"""

s1={3,-12,453,23,1,-100,23,-56,-99,-3.14,-1,0,55}
num=int(input("Enter a number: "))
def checkNumber(n):
    if n>num:
        return n
l1=list(filter(checkNumber,s1))
print(l1)

# I saw something that the function checkNumber should return a Boolean value.