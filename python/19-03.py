"""
Assignment: 19
Problem: 03
Topic: for loop
Description: Write a python script to count occurence of spaces in a given string.
Date: 30-06-2026
"""

s=input("Enter some string: ")
count=0
for x in s:
    if x == ' ':
        count+=1
print("There are",count,"spaces in the entered string")