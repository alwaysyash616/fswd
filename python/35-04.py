"""
Assignment: 35
Problem: 04
Topic: Functions-4
Description: Write a Python function to filter out words from a text starting from some alphabet and store then in a list. Now create a dict with alphabets as data values. Take text as an argument and return dict object (TSRS)
Date: 04-07-2026
"""

letter=input('Enter the starting alphabet: ')
words=[e for e in input("Enter some text: ").split(' ') if e.startswith(letter) or e.startswith(letter.upper())]
print(words)