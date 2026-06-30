"""
Assignment: 19
Problem: 02
Topic: for loop
Description: Write a python script to print only vowels of the given string
Date: 30-06-2026
"""

vowels='aeiouAEIOU'
s=input("Enter some string: ")
for x in s:
    if x in vowels:
        print(x,sep=' ')