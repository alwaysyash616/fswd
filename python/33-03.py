"""
Assignment: 33
Problem: 03
Topic: Functions-2
Description: Write a python function to check wheather a number is Prime (TSRS)
Date: 04-07-2026
"""

def isPrime(n):
    i=2
    while i<=n//2:
        if n%i==0:
            break
        i+=1
    if i==n//2+1:
        return True
    else:
        return False


i=1
while i<=1000:
    if isPrime(i):
        print(i,end=' ')
    i+=1