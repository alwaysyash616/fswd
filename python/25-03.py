"""
Assignment: 25
Problem: 03
Topic: more on list
Description: Write a Python script to create a list of first N prime numbers.
Date: 30-06-2026
"""

n=int(input("Enter a number: "))
l1=[]
num,count=2,0
while count<n:
    for e in range(2,num):
        if num%e==0:
            break
    else:
        l1.append(num)
        count+=1
    num+=1
print(l1)