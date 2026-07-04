"""
Assignment: 26
Problem: 02
Topic: str
Description: Write a Python script to check if a given character is present in a given string or not.
Date: 04-07-2026
"""

# s='vision for open education learning management system'
# if 'v' in s:
#     print("Present")

s,ch=input("Enter some string: "),input("Enter a character: ")
if ch in s:
    print("Present")
else:
    print("Not Present")
