"""
Assignment: 24
Problem: 05
Topic: list
Description: Write a python script to create a list from a given list by selecting only even places elements.
Date: 30-06-2026
"""

print("Enter numbers separated by comma")
l1=[int(e) for e in input().split(',')]
l2=list()
i=1
for e in l1:
    if(i%2==0):
        l2.append(e)
    i+=1