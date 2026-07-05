"""
Assignment: 30
Problem: 03
Topic: tuple
Description: Given a set of 5 player names. Write a Python script to form all possible pairs of players that is selecting two players at a time.
Date: 04-07-2026
"""

s1={'Diego Maradona','Christiano Ronaldo','Michael Jordan','Kobe Bryant','LeBron James'}
l1=list(s1)
i=0
while i<len(l1):
    j=i+1
    while j<len(l1):
        print(l1[i],l1[j],sep='\n')
        print("---------------------------")
        j+=1
    i+=1

# s2={'Virat','Rahul','Sachin','Kapil','Dhoni'}
# i=0
# for p1 in s2:
#     i+=1
#     for p2 in list(s2)[i::]:
#         print(p1,p2)