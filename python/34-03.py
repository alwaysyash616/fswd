"""
Assignment: 34
Problem: 03
Topic: Functions-3
Description: Write a Python function to print all prime numbers between two given numbers (TSRN)
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

def printPrimeNumbersBetween(a,b):
    for e in range(a,b+1):
        if isPrime(e):
            print(e,end=' ')
    print()

print("Enter two numbers:")
printPrimeNumbersBetween(int(input()),int(input()))