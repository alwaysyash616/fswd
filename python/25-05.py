"""
Assignment: 25
Problem: 05
Topic: more on list
Description: Write a Python script to create two lists from a given list of numbers in such a way that the first list can have only positive numbers and second list can have only non positive numbers.
Date: 30-06-2026
"""

print("Enter numbers separated by comma: ")
l1=[int(e) for e in input().split(',')]
l2=list()
l3=list()
for e in l1:
    if e>0:
        l2.append(e)
    else:
        l3.append(e)
print(l2)
print(l3)