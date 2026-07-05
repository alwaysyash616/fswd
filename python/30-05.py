"""
Assignment: 30
Problem: 05
Topic: tuple
Description: Write a python script to create a set of tuples, where each tuple has two elements representing dice upper face number. Take a number N from the user and generate all possible tuples, in such a way that tuple element sums to N.
Date: 04-07-2026
"""

n=int(input("Enter a number: "))
s1=set()
for i in range(1,7):
    for j in range(1,7):
        if i+j==n:
            s1.add((i,j,))
print(s1)