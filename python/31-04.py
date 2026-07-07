"""
Assignment: 31
Problem: 04
Topic: dict
Description: Write a python script to find maximum size batch code from a dictionary where key-values in the dictionary are batch codes and data-values are size of the batch.
Date: 07-07-2026
"""

# d1={'ucf':320,'fswd':1200,'ujf':302,'python':1000,'javascript':800}
# for k in d1.keys():
#     if d1[k]==max(d1.values()):
#         print(k)

batches={
    'SA':200,
    'SB':189,
    'SC':207,
    'SD':385,
    'SE':280
}
max=0
batch_code=''
for k,v in batches.items():
    if v>max:
        max=v
        batch_code=k
print(batch_code,max)