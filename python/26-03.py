"""
Assignment: 26
Problem: 03
Topic: str
Description: Write a Python script to count vowels in a given string.
Date: 04-07-2026
"""

count=0
for x in input("Enter some string: "):
    if x in 'aeiouAEIOU':
        count+=1
print(count)