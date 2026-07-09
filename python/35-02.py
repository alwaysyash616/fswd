"""
Assignment: 35
Problem: 02
Topic: Functions-4
Description: Write a Python function to count words in a given string (TSRS)
Date: 04-07-2026
"""

def countWords(s):
    return len([e for e in s.split(' ') if e != ''])

print(countWords(input("Enter some string: ")))