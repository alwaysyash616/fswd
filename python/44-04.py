"""
Assignment: 44
Problem: 04
Topic: Decorator
Description: Write a function to check if a given number N is a Prime or not. Define a decorator to print total number of Prime numbers before N.
Date: 22-07-2026
"""

def allPrimesGenerator(p):
    def allPrimesBefore(n):
        count=0
        for e in range(2,n):
            if p(e):
                count+=1
        print(count)
        return p(n)
    return allPrimesBefore

@allPrimesGenerator
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

res=isPrime(int(input("Enter a number: ")))
print(res)