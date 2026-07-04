"""
Assignment: 26
Problem: 04
Topic: str
Description: Write a Python script to count words in a given string.
Date: 04-07-2026
"""

# print(len(input("Enter some string: ").split(' ')))

count=0
for e in input("Enter some string: ").split(' '):
    if e!='':
        count+=1
print(count)



# strObject.strip() function