"""
Assignment: 28
Problem: 02
Topic: list and str mixed
Description: Write a Python script to print distinct elements along with their frequencies of occurences in the list.
Date: 04-07-2026
"""

# l1=[2,3.14,False,4+7j,3.14,True,2]
# s=str(l1)
# l2=s[1:len(s)-1:].split(',')
# i=0
# while i<len(l2):
#     l2[i]=l2[i].strip()
#     i+=1
# l2.sort()
# count=1
# i=0
# while i<len(l2):
#     if i<len(l2)-1 and l2[i]==l2[i+1]:
#         count+=1
#     else:
#         print(l2[i],"\t",count)
#         count=1
#     i+=1


'''
I was confused before writing a program for this problem, because a list can have heterogenous elements. But that was't even a problem. I don't know, why I think this much.
'''

# l1=[2,3.14,False,4+7j,3.14,True,2]
# l2=list()
# for e in l1:
#     if e not in l2:
#         l2.append(e)
# for e in l2:
#     print(e,"\t",l1.count(e))

l1=[2,3.14,False,4+7j,3.14,True,2]
i=0
for e in l1:
    if i==l1.index(e):
        print(e,"\t",l1.count(e))
    i+=1

'''
We're not removing elements from the list. We're just finding index, so we can use 'for' loop.
'''