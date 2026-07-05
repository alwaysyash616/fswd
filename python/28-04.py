"""
Assignment: 28
Problem: 04
Topic: list and str mixed
Description: Write a Python script to find first repeated string in a list of strings
Date: 04-07-2026
"""

l1=['MySirG','VeoLMS','OpenAI','GCP','ChatGPT','YouTUBE','ChatGPT','MySirG']
l2=list()
for e in l1:
    if e not in l2:
        l2.append(e)
    else:
        print(e)
        break

# l1=['MySirG','VeoLMS','OpenAI','GCP','ChatGPT','YouTUBE','ChatGPT','MySirG']
# i=0
# for e in l1:
#     if l1.index(e)!=i:
#         print(e)
#         break
#     i+=1