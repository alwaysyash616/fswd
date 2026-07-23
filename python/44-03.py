"""
Assignment: 44
Problem: 03
Topic: Decorator
Description: Define a decorator to display “Good Bye” message at the end.
Date: 22-07-2026
"""

def message(greetfun):
    def fullMessage():
        greetfun()
        print("Good Bye")
    return fullMessage

@message
def greet():
    print("Welcome")

greet()