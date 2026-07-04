"""
Assignment: 27
Problem: 05
Topic: more on str
Description: Write a Python script to find maximum length word in a given text.
Date: 04-07-2026
"""

s=input("Enter some multiword string: ").split(' ')
lengths=[len(x) for x in s]
print(s[lengths.index(max(lengths))])