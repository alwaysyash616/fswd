"""
Assignment: 43
Problem: 02
Topic: map, reduce and filter
Description: Write a python script to find number of digits in each of the element in a given tuple of numbers. Use map function.
Date: 21-07-2026
"""

t1=(3,5,132,923423,42,5055,24,323236,40,45,456,2353,12)
l1=list(map(lambda n:len(str(n)) if n>=0 else len(str(n*-1)),t1))
i=0
while i<len(l1):
    print(t1[i],l1[i])
    i+=1