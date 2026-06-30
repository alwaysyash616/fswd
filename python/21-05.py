"""
Assignment: 21
Problem: 05
Topic: more on for loop and range
Description: Write a python script to display all prime numbers within a range. # range start = 15 end = 45
Date: 30-06-2026
"""

print("Specify range (max,min value to check for prime's)")
s,e=int(input()),int(input())
for x in range(s,e+1):
    i=2
    while i<=x//2:
        if x%i==0:
            break
        i+=1
    if i==x//2+1:
        print(x,end=' ')
print()


# else can be used with while and for loops.
# We can use for loop in place of while loop here and use else to print prime numbers