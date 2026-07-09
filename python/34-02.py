"""
Assignment: 34
Problem: 02
Topic: Functions-3
Description: Write a Python function to print first N Prime numbers. (TSRN)
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

def printFirstNPrimeNumbers(n):
    i=1
    count=0
    while count<n:
        if isPrime(i):
            print(i,end=' ')
            count+=1
        i+=1
    print()
        
printFirstNPrimeNumbers(int(input("Enter a number: ")))