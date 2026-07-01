"""
Assignment: 23
Problem: 02
Topic: Loops again
Description: Write a python script to count digits in a given number.
Date: 30-06-2026
"""

n=int(input("Enter a number: "))
n=-n if n<0 else n
if n==0:
    print(1)
else:
    count=0
    for x in str(n):
        count+=1
    print(count)