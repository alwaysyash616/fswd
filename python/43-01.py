"""
Assignment: 43
Problem: 01
Topic: map, reduce and filter
Description: Write a python script to find number of vowels in each of the string in a given list of strings. Use map function.
Date: 21-07-2026
"""

l1=['vishakhapatnam','vizag','ooty','krishnanagar','haveri','chitradurga','nashik','cuddalore','jamshedpur','rourkela','dhanbad','siliguri','bhagalpur','mysore','erode']
def countVowels(s):
    count=0
    for e in s:
        if e in 'aeiouAEIOU':
            count+=1
    return count
l2=list(map(countVowels,l1))
i=0
while i<len(l1):
    print(l1[i],l2[i])
    i+=1
