"""
Assignment: 19
Problem: 04
Topic: for loop
Description: Write a python script to print unique digits of a given integer.
Date: 30-06-2026
"""

s=int(input("Enter an integer: "))
s=str(abs(s))
done=""
for x in s:
    if x not in done:
        print(x,end=' ')
        done+=x
print()