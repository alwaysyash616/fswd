"""
Assignment: 29
Problem: 03
Topic: tuple
Description: Write a Python script to create a list of tuples from a given list of strings, where each tuple is a collection of strings begin with the same character.
Date: 04-07-2026
"""

l1=['bhopal','itarasi','mehsana','jodhpur','bharatpur','patna','faridabad','chitradurga','dehradun','asansol','pune']
# l2=list()
# l3=list()
# l1.sort()
# i=0
# while i<len(l1):
#     l3.append(l1[i])
#     if i<len(l1)-1 and l1[i][0]==l1[i+1][0]:
#         pass
#     else:
#         l2.append(tuple(l3))
#         l3.clear()
#     i+=1
# print(l2)

mylist=[]
temp=[]
alpha='abcdefghijklmnopqrstuvwxyz'
l1.sort()
for letter in alpha:
    for x in l1:
        if x.startswith(letter):
            temp.append(x)
    if len(temp)>0:    
        mylist.append(tuple(temp))
        temp.clear()
print(mylist)