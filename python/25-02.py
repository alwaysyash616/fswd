"""
Assignment: 25
Problem: 02
Topic: more on list
Description: Write a Python script to create a list of first N terms of a Fibonacci series
Date: 30-06-2026
"""

print("Enter a number: ")
n=int(input())
a,b=0,1
i=1
l1=list()
while i<=n:
    if i==1:
        l1.append(a)
    elif i==2:
        l1.append(b)
    else:
        a,b=b,a+b
        l1.append(b)
    i+=1
print(l1)