"""
Assignment: 20
Problem: 03
Topic: for loop and range
Description: Write a python script to print the first M multiples of N.
Date: 30-06-2026
"""

print("Enter a number and number of multiples")
n,m=int(input()),int(input())
i=1
if n==0:
   while i<=m:
    print(0,end=' ')
    i+=1
elif n>0:
    r=range(n,n*m+1,n)
else:
    r=range(n,n*m-1,n)
for e in r:
    print(e,end=' ')
print()