"""
Assignment: 42
Problem: 03
Topic: Variable Length Arguments
Description: Write a function which receives variable length arguments to filter odd and even numbers. Store all odd numbers in a list and all even numbers in another list. Store both the lists in a tuple and return.
Date: 20-07-2026
"""

def filterOddEven(*t):
    l1=list()
    l2=list()
    for e in t:
        if e & 1:
            l1.append(e)
        else:
            l2.append(e)
    return (l1,l2)

print(filterOddEven(3,5,2,6,4,7,8,34,56,3,43,12))