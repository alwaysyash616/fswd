"""
Assignment: 36
Problem: 02
Topic: Functions-4
Description: Write a Python function to count frequency of each element of the list and store list elements in the dict object as keys and element frequency as data values (TSRS)
Date: 04-07-2026
"""

def frequencyDict(mylist):
    return {e:l1.count(e) for e in set(mylist)}

# def frequencyDict(mylist):
#     temp={}
#     i=0
#     while i<len(mylist):
#         if mylist.index(mylist[i])==i:
#             f=mylist.count(mylist[i])
#             temp[mylist[i]]=f
#         i+=1
#     return temp

l1 = [10, "apple", 3.14, True, 10, "apple", 5+2j, 3.14, False, True,10,3.14,"apple",5+2j,False]

for k,o in frequencyDict(l1).items():
    print(k,o)