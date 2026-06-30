"""
Assignment: 20
Problem: 05
Topic: for loop and range
Description: Write a python script to print table of user's choice
Date: 30-06-2026
"""

n=int(input("Enter a number: "))
if n:
    if n>0:
        for e in range(n,n*10+1,n):
            print(e,end=' ')
    else:
        for e in range(n,n*10-1,n):
            print(e,end=' ')
else:
    i=1
    while i<=10:
        print(0,end=' ')
        i+=1
print()

# "{}x{}={}.format(n,x,n*x)"