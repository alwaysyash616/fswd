"""
Assignment: 36
Problem: 05
Topic: Functions-4
Description: Write a Python function to check if two given list have same elements in any order or not. Return True or False. (TSRS)
Date: 04-07-2026
"""

def compareList(l1,l2):
    return sorted(l1)==sorted(l2)

print(compareList([3,2,5,1],[2,5,3,1]))