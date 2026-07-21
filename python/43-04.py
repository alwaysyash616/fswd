"""
Assignment: 43
Problem: 04
Topic: map, reduce and filter
Description: Write a python script to filter only int type values in a given list of elements. Use filter function.
Date: 21-07-2026
"""

l1=[34,55.4,67,89,100.4,90+9j,44,True,50.3,55.342,70,-88,20,5.1,10]
l2=list(filter(lambda n:type(n)==int,l1))
print(l2)