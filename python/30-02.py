"""
Assignment: 30
Problem: 02
Topic: tuple
Description: Create two sets from a given set of numbers to spearate even and odd numbers.
Date: 04-07-2026
"""

s1=set([int(e) for e in input("Enter numbers separated by comma: ").split(',')])
s2=set()
s3=set()
for e in s1:
    if e%2:
        s3.add(e)
    else:
        s2.add(e)
print(s2,s3,sep='\n')