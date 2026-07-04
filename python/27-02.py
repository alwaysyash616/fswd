"""
Assignment: 27
Problem: 02
Topic: more on str
Description: Write a Python script to extract numbers from a given text and store all the numbers in a list.
Date: 04-07-2026
"""

l1=[float(e) for e in input("Enters numbers separated by comma: ").split(',')]
print(l1)