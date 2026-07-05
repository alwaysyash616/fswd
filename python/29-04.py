"""
Assignment: 29
Problem: 04
Topic: tuple
Description: Write a Python script to create a list of tuples, where each tuple is a pair of elements, first element is uppercase character and second element is it's unicode.
Date: 04-07-2026
"""

l1=list()
s=input("Enter some string: ")
for x in s:
    l1.append(tuple([x.upper(),ord(x.upper())]))
print(l1)