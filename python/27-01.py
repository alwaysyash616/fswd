"""
Assignment: 27
Problem: 01
Topic: more on str
Description: Write a Python script to reverse a string word wise (for example- "mysirg education services" is a given string and resulting string should be "services education Mysirg")
Date: 04-07-2026
"""

s=' '.join((input("Enter some string: ").split(' ')[::-1]))
print(s)