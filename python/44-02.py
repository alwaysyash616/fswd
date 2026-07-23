"""
Assignment: 44
Problem: 02
Topic: Decorator
Description: Define a decorator to display “Happy New Year” message at the beginning.
Date: 22-07-2026
"""

def newYear(greet):
    def fullGreet():
        print("Happy New Year")
        greet()
    return fullGreet

@newYear
def greet():
    print("Welcome")

greet()