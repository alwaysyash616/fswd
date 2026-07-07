"""
Assignment: 31
Problem: 02
Topic: dict
Description: Sort a dictionary by its keys in descending order.
Date: 07-07-2026
"""

d1={60:'Yash',51:'Siddarth',57:'Varsha',1:'Aditi',48:'Shivam'}
# new_dict={}
# for e in sorted(d1.keys(),reverse=True):
#     new_dict[e]=d1[e]
# for k,o in new_dict.items():
#     print(k,o)

# new_dict={e:d1[e] for e in sorted(d1.keys(),reverse=True)}
# for k,o in new_dict.items():
#     print(k,o)

l1=sorted(d1,reverse=True)
for k in l1:
    print(k,' ',d1[k])



'''
By default sorted() function works on keys
'''