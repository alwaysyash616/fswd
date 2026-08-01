"""
Assignment: 48
Problem: 01
Topic: Exception Handling
Description: Define a python function to calculate factorial of a number. Handle all possible exceptions.
Date: 01-08-2026
"""

def factorial(n):
    try:
        if type(n)!=int:
            raise TypeError("Factorial not defined for",type(n),"type values.")
        if n<0:
            raise ValueError("Factorial not defined for negative numbers.")
        f=1
        while n:
            f*=n
            n-=1
        return f
    except TypeError as t:
        print(t)
    except ValueError as e:
        print(e)
    except:
        print("Unknown Exception")

print(factorial(int(input("Enter a number: "))))