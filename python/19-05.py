"""
Assignment: 19
Problem: 05
Topic: for loop
Description: Write a python script to count number of digits in a given number.
Date: 30-06-2026
"""

# s=abs(int(input("Enter a number: ")))
# if s:
#     count=0
#     while s:
#         count+=1
#         s//=10
#     print(count)
# else:
#     print("1")

n=abs(int(input("Enter a number: ")))
if n:
    count=0
    for e in str(n):
        count+=1
    print("Toatl digits:",count)
else:
    print(1)