"""
Assignment: 25
Problem: 04
Topic: more on list
Description: Write a Python script to add two matrices each or order 3x3. Store matrix elements in a list of lists.
Date: 30-06-2026
"""

l1=[[1,2,3],[4,5,6],[7,8,9]]
l2=[[2,3,4],[5,6,7],[8,9,10]]
l3=list()
temp=[]
for i in range(0,3):
    for j in range(0,3):
        temp.append(l1[i][j]+l2[i][j])
    l3.append(temp)
    # temp.clear()
    temp=list()
print(l3)