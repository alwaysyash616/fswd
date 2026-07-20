"""
Assignment: 42
Problem: 04
Topic: Variable Length Arguments
Description: Write a function which takes variable length arguments to receive strings. Return the list of max length string or strings if multiple strings have the same length.
Date: 20-07-2026
"""

def maxLengthStrings(*t):
    l=0
    for e in t:
        if len(e)>l:
            l=len(e)
    return [e for e in t if len(e)==l]

print(maxLengthStrings('varsha','shrishti','vanya','shivangi','yashika','lata','disha','karishma',))