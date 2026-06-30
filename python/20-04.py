"""
Assignment: 20
Problem: 04
Topic: for loop and range
Description: Write a python script to print the first 10 multiples of N in reverse order.
Date: 30-06-2026
"""

n=int(input("Enter a number: "))
if n==0:
    i=1
    while i<=10:
        print(0,end=' ')
        i+=1
elif n>0:
    for e in range(n,n*10+1,n):
        print(e,end=' ')
else:
    for e in range(n,n*10-1,n):
        print(e,end=' ')
print()