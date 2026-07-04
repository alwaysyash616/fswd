"""
Assignment: 27
Problem: 03
Topic: more on str
Description: Write a Python script to check wheather it is a palindrome or not.
Date: 04-07-2026
"""

s=input("Enter some string: ")
if s==s[::-1]:
    print("Yes it's Palindrome")
else:
    print("No it's not Palindrome")